# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
import io
import logging
import unittest

import requests

import azure.mgmt.batch
from azure.mgmt.batch import models
from azure.common.exceptions import CloudError
from mgmt_batch_preparers import KeyVaultPreparer, SimpleBatchPreparer

from devtools_testutils import (
    AzureMgmtTestCase,
    ResourceGroupPreparer,
    StorageAccountPreparer
)


AZURE_LOCATION = 'eastus2'
EXISTING_BATCH_ACCOUNT = {'name': 'pythonsdktest', 'location': 'brazilsouth'}


class MgmtBatchTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtBatchTest, self).setUp()
        self.mgmt_batch_client = self.create_mgmt_client(
            azure.mgmt.batch.BatchManagementClient)
        self.mgmt_keyvault_client = self.create_mgmt_client(
            azure.mgmt.keyvault.KeyVaultManagementClient)

    def _get_account_name(self):
        return self.get_resource_name('batch')[-24:]

    def test_mgmt_batch_list_operations(self):
        operations = self.mgmt_batch_client.operations.list()
        all_ops = list(operations)
        self.assertEqual(len(all_ops), 30)
        self.assertEqual(all_ops[0].name, 'Microsoft.Batch/batchAccounts/providers/Microsoft.Insights/diagnosticSettings/read')
        self.assertEqual(all_ops[0].origin, 'system')
        self.assertEqual(all_ops[0].display.provider, 'Microsoft Batch')
        self.assertEqual(all_ops[0].display.operation, 'Read diagnostic setting')

    def test_mgmt_batch_subscription_quota(self):
        quotas = self.mgmt_batch_client.location.get_quotas(AZURE_LOCATION)
        self.assertIsInstance(quotas, models.BatchLocationQuota)
        self.assertEqual(quotas.account_quota, 1)

    def test_mgmt_batch_account_name(self):
        # Test Invalid Account Name
        availability = self.mgmt_batch_client.location.check_name_availability(
            AZURE_LOCATION, "randombatchaccount@5^$g9873495873")
        self.assertIsInstance(availability, models.CheckNameAvailabilityResult)
        self.assertFalse(availability.name_available)
        self.assertEqual(availability.reason, models.NameAvailabilityReason.invalid)

        # Test Unvailable Account Name
        availability = self.mgmt_batch_client.location.check_name_availability(
            EXISTING_BATCH_ACCOUNT['location'], EXISTING_BATCH_ACCOUNT['name'])
        self.assertIsInstance(availability, models.CheckNameAvailabilityResult)
        self.assertFalse(availability.name_available)
        self.assertEqual(availability.reason, models.NameAvailabilityReason.already_exists)

        # Test Available Account Name
        availability = self.mgmt_batch_client.location.check_name_availability(
            AZURE_LOCATION, self._get_account_name())
        self.assertIsInstance(availability, models.CheckNameAvailabilityResult)
        self.assertTrue(availability.name_available)

    @ResourceGroupPreparer(location=AZURE_LOCATION)
    @KeyVaultPreparer(location=AZURE_LOCATION)
    def test_mgmt_batch_byos_account(self, resource_group, location, keyvault):
        batch_account = models.BatchAccountCreateParameters(
                location=location,
                pool_allocation_mode=models.PoolAllocationMode.user_subscription)
        with self.assertRaises(Exception):  # TODO: What exception
            creating = self.mgmt_batch_client.batch_account.create(
                resource_group.name,
                self._get_account_name(),
                batch_account)
            creating.result()

        keyvault_id = "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.KeyVault/vaults/{}".format(
            self.settings.SUBSCRIPTION_ID, resource_group.name, keyvault.name)
        keyvault_url = "https://{}.vault.azure.net/".format(keyvault.name)
        batch_account = models.BatchAccountCreateParameters(
                location=location,
                pool_allocation_mode=models.PoolAllocationMode.user_subscription,
                key_vault_reference={'id': keyvault_id, 'url': keyvault_url})
        creating =  self.mgmt_batch_client.batch_account.create(
                resource_group.name,
                self._get_account_name(),
                batch_account)
        creating.result()

    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_mgmt_batch_account(self, resource_group, location):
        batch_account = models.BatchAccountCreateParameters(
            location=location,
        )
        account_name = self._get_account_name()
        account_setup = self.mgmt_batch_client.batch_account.create(
            resource_group.name,
            account_name,
            batch_account)
        account_setup.result()

        # Test Get Account
        account = self.mgmt_batch_client.batch_account.get(resource_group.name, account_name)
        self.assertEqual(account.dedicated_core_quota, 20)
        self.assertEqual(account.low_priority_core_quota, 20)
        self.assertEqual(account.pool_quota, 20)
        self.assertEqual(account.pool_allocation_mode.value, 'BatchService')

        # Test List Accounts by Resource Group
        accounts = self.mgmt_batch_client.batch_account.list_by_resource_group(resource_group.name)
        self.assertEqual(len(list(accounts)), 1)

        # Test List Account Keys
        keys = self.mgmt_batch_client.batch_account.get_keys(resource_group.name, account_name)
        self.assertIsInstance(keys, models.BatchAccountKeys)
        self.assertEqual(keys.account_name, account_name)
        secondary = keys.secondary

        # Test Regenerate Account Key
        keys = self.mgmt_batch_client.batch_account.regenerate_key(
            resource_group.name, account_name, 'Secondary')
        self.assertIsInstance(keys, models.BatchAccountKeys)
        self.assertFalse(keys.secondary == secondary)

        # Test Update Account
        update_tags = {'Name': 'tagName', 'Value': 'tagValue'}
        updated = self.mgmt_batch_client.batch_account.update(resource_group.name, account_name, update_tags)
        self.assertIsInstance(updated, models.BatchAccount)
        self.assertEqual(updated.tags['Name'], 'tagName')
        self.assertEqual(updated.tags['Value'], 'tagValue')

        # Test Delete Account
        response = self.mgmt_batch_client.batch_account.delete(resource_group.name, account_name)
        self.assertIsNone(response.result())

    @ResourceGroupPreparer(location=AZURE_LOCATION)
    @StorageAccountPreparer(name_prefix='batch', location=AZURE_LOCATION)
    def test_mgmt_batch_applications(self, resource_group, location, storage_account, storage_account_key):
        # Test Create Account with Auto-Storage 
        storage_resource = '/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Storage/storageAccounts/{}'.format(
            self.settings.SUBSCRIPTION_ID,
            resource_group.name,
            storage_account.name
        )
        batch_account = models.BatchAccountCreateParameters(
            location=location,
            auto_storage=models.AutoStorageBaseProperties(storage_resource)
        )
        account_name = self._get_account_name()
        account_setup = self.mgmt_batch_client.batch_account.create(
            resource_group.name,
            account_name,
            batch_account)
        account_setup.result()

        # Test Sync AutoStorage Keys
        response = self.mgmt_batch_client.batch_account.synchronize_auto_storage_keys(
                                   resource_group.name, account_name)
        self.assertIsNone(response)

        # Test Add Application
        application_id = 'my_application_id'
        application_name = 'my_application_name'
        application_ver = 'v1.0'
        application = self.mgmt_batch_client.application.create(
            resource_group.name, account_name, application_id,
            allow_updated=True, display_name=application_name)
        self.assertIsInstance(application, models.Application)
        self.assertEqual(application.id, application_id)
        self.assertEqual(application.display_name, application_name)
        self.assertTrue(application.allow_updates)

        # Test Mgmt Get Application
        application = self.mgmt_batch_client.application.get(resource_group.name, account_name, application_id)
        self.assertIsInstance(application, models.Application)
        self.assertEqual(application.id, application_id)
        self.assertEqual(application.display_name, application_name)
        self.assertTrue(application.allow_updates)

        # Test Mgmt List Applications
        applications = self.mgmt_batch_client.application.list(resource_group.name, account_name)
        self.assertTrue(len(list(applications)) > 0)

        # Test Add Application Package
        package_ref = self.mgmt_batch_client.application_package.create(
            resource_group.name, account_name, application_id, application_ver)
        self.assertIsInstance(package_ref, models.ApplicationPackage)
        with io.BytesIO(b'Hello World') as f:
            headers = {'x-ms-blob-type': 'BlockBlob'}
            upload = requests.put(package_ref.storage_url, headers=headers, data=f.read())
            if not upload:
                raise ValueError('Upload failed: {!r}'.format(upload))

        # Test Activate Application Package
        response = self.mgmt_batch_client.application_package.activate(
            resource_group.name, account_name, application_id, application_ver, 'zip')
        self.assertIsNone(response)

        # Test Update Application
        params = models.ApplicationUpdateParameters(
            allow_updates=False,
            display_name='my_updated_name',
            default_version=application_ver
        )
        response = self.mgmt_batch_client.application.update(
            resource_group.name, account_name, application_id, params)
        self.assertIsNone(response)

        # Test Get Application Package
        package_ref = self.mgmt_batch_client.application_package.get(
            resource_group.name, account_name, application_id, application_ver)
        self.assertIsInstance(package_ref, models.ApplicationPackage)
        self.assertEqual(package_ref.id, application_id)
        self.assertEqual(package_ref.version, application_ver)
        self.assertEqual(package_ref.format, 'zip')
        self.assertEqual(package_ref.state, models.PackageState.active)

        # Test Delete Application Package
        response = self.mgmt_batch_client.application_package.delete(
            resource_group.name, account_name, application_id, application_ver)
        self.assertIsNone(response)

        # Test Delete Application
        response = self.mgmt_batch_client.application.delete(
            resource_group.name, account_name, application_id)
        self.assertIsNone(response)

        # Test Delete Account
        response = self.mgmt_batch_client.batch_account.delete(resource_group.name, account_name)
        self.assertIsNone(response.result())

    @ResourceGroupPreparer(location=AZURE_LOCATION)
    @SimpleBatchPreparer(location=AZURE_LOCATION)
    def test_mgmt_batch_certificates(self, resource_group, location, batch_account):
        # Test Add Certificate
        parameters = models.CertificateCreateOrUpdateParameters(
            thumbprint='cff2ab63c8c955aaf71989efa641b906558d9fb7',
            thumbprint_algorithm='sha1',
            data='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',
            format=models.CertificateFormat.pfx,
            password='nodesdk')

        certificate = 'SHA1-cff2ab63c8c955aaf71989efa641b906558d9fb7'
        response = self.mgmt_batch_client.certificate.create(resource_group.name, batch_account.name, certificate, parameters)
        self.assertIsInstance(response.result(), models.Certificate)

        # Test List Certificates
        certs = self.mgmt_batch_client.certificate.list_by_batch_account(resource_group.name, batch_account.name)
        self.assertEqual(len(list(certs)), 1)

        # Test Get Certificate
        cert = self.mgmt_batch_client.certificate.get(resource_group.name, batch_account.name, certificate)
        self.assertIsInstance(cert, models.Certificate)
        self.assertEqual(cert.thumbprint.lower(), 'cff2ab63c8c955aaf71989efa641b906558d9fb7')
        self.assertEqual(cert.thumbprint_algorithm, 'SHA1')
        self.assertIsNone(cert.delete_certificate_error)

        # Test Update Certiciate
        parameters = models.CertificateCreateOrUpdateParameters(
            password='nodesdk',
            data='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',)
        response = self.mgmt_batch_client.certificate.update(resource_group.name, batch_account.name, certificate, parameters)
        self.assertIsInstance(response, models.Certificate)

        # Test Cancel Certificate Delete
        #with self.assertRaises(models.DeleteCertificateError):
        self.mgmt_batch_client.certificate.cancel_deletion(
            resource_group.name, batch_account.name, certificate)

        # Test Delete Certificate
        response = self.mgmt_batch_client.certificate.delete(resource_group.name, batch_account.name, certificate)
        self.assertIsNone(response.result())

    @ResourceGroupPreparer(location=AZURE_LOCATION)
    @SimpleBatchPreparer(location=AZURE_LOCATION)
    def test_mgmt_batch_pools(self, resource_group, location, batch_account):
        # Test create PAAS pool
        paas_pool = "test_paas_pool"
        parameters = models.Pool(
            display_name="test_pool",
            vm_size='small',
            deployment_configuration=models.DeploymentConfiguration(
                cloud_service_configuration=models.CloudServiceConfiguration(os_family='5')
            ),
            start_task=models.StartTask(
                command_line="cmd.exe /c \"echo hello world\"",
                resource_files=[models.ResourceFile('https://blobsource.com', 'filename.txt')],
                environment_settings=[models.EnvironmentSetting('ENV_VAR', 'env_value')],
                user_identity=models.UserIdentity(
                    auto_user=models.AutoUserSpecification(
                        elevation_level=models.ElevationLevel.admin
                    )
                )
            ),
            user_accounts=[models.UserAccount('UserName', 'p@55wOrd')],
            scale_settings=models.ScaleSettings(
                fixed_scale=models.FixedScaleSettings(
                    target_dedicated_nodes=0,
                    target_low_priority_nodes=0
                )
            )
        )
        response = self.mgmt_batch_client.pool.create(
            resource_group.name, batch_account.name, paas_pool, parameters)
        self.assertIsInstance(response.result(), models.Pool)

        # Test create IAAS pool
        iaas_pool = "test_iaas_pool"
        parameters = models.Pool(
            display_name="test_pool",
            vm_size='Standard_A1',
            deployment_configuration=models.DeploymentConfiguration(
                virtual_machine_configuration=models.VirtualMachineConfiguration(
                    image_reference=models.ImageReference(
                        publisher='MicrosoftWindowsServer',
                        offer='WindowsServer',
                        sku='2016-Datacenter-smalldisk'
                    ),
                    node_agent_sku_id='batch.node.windows amd64',
                    windows_configuration=models.WindowsConfiguration(True)
                )
            ),
            scale_settings=models.ScaleSettings(
                fixed_scale=models.FixedScaleSettings(
                    target_dedicated_nodes=0,
                    target_low_priority_nodes=0
                )
            )
        )

        response = self.mgmt_batch_client.pool.create(
            resource_group.name, batch_account.name, iaas_pool, parameters)
        self.assertIsInstance(response.result(), models.Pool)

        # Test list pools
        pools = self.mgmt_batch_client.pool.list_by_batch_account(resource_group.name, batch_account.name)
        self.assertEqual(len(list(pools)), 2)

        # Test Update pool
        parameters = models.Pool(
            scale_settings=models.ScaleSettings(
                auto_scale=models.AutoScaleSettings(
                    formula='$TargetDedicatedNodes=1'
                )
            )
        )
        response = self.mgmt_batch_client.pool.update(
            resource_group.name, batch_account.name, iaas_pool, parameters)
        self.assertIsInstance(response, models.Pool)

        # Test Get pool
        pool = self.mgmt_batch_client.pool.get(
            resource_group.name, batch_account.name, iaas_pool)
        self.assertIsInstance(pool, models.Pool)
        self.assertEqual(pool.vm_size, 'STANDARD_A1'),
        self.assertIsNone(pool.display_name),
        self.assertEqual(pool.allocation_state, models.AllocationState.resizing)
        self.assertEqual(
            pool.deployment_configuration.virtual_machine_configuration.node_agent_sku_id,
            'batch.node.windows amd64')

        # Test stop resizing
        with self.assertRaises(CloudError):
            self.mgmt_batch_client.pool.stop_resize(resource_group.name, batch_account.name, iaas_pool)

        # Test disable auto-scale
        response = self.mgmt_batch_client.pool.disable_auto_scale(
            resource_group.name, batch_account.name, iaas_pool)
        self.assertIsInstance(response, models.Pool)

        # Test delete pool
        response = self.mgmt_batch_client.pool.delete(
            resource_group.name, batch_account.name, iaas_pool)
        self.assertIsNone(response.result())