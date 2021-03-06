# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ..version import VERSION


class ManagementLockClientConfiguration(AzureConfiguration):
    """Configuration for ManagementLockClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ManagementLockClientConfiguration, self).__init__(base_url)

        self.add_user_agent('managementlockclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ManagementLockClient(MultiApiClientMixin):
    """Azure resources can be locked to prevent other users in your organization from deleting or modifying resources.

    :ivar config: Configuration for client.
    :vartype config: ManagementLockClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A dict using operation group name to API version.
    :type profile: dict[str, str]
    """

    DEFAULT_API_VERSION = '2016-09-01'
    _PROFILE_TAG = "azure.mgmt.resource.locks.ManagementLockClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        super(ManagementLockClient, self).__init__(
            credentials=credentials,
            subscription_id=subscription_id,
            api_version=api_version,
            base_url=base_url,
            profile=profile
        )

        self.config = ManagementLockClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

############ Generated from here ############

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-01-01: :mod:`v2015_01_01.models<azure.mgmt.resource.locks.v2015_01_01.models>`
           * 2016-09-01: :mod:`v2016_09_01.models<azure.mgmt.resource.locks.v2016_09_01.models>`
        """
        if api_version == '2015-01-01':
            from .v2015_01_01 import models
            return models
        elif api_version == '2016-09-01':
            from .v2016_09_01 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))
    
    @property
    def management_locks(self):
        """Instance depends on the API version:

           * 2015-01-01: :class:`ManagementLocksOperations<azure.mgmt.resource.locks.v2015_01_01.operations.ManagementLocksOperations>`
           * 2016-09-01: :class:`ManagementLocksOperations<azure.mgmt.resource.locks.v2016_09_01.operations.ManagementLocksOperations>`
        """
        api_version = self._get_api_version('management_locks')
        if api_version == '2015-01-01':
            from .v2015_01_01.operations import ManagementLocksOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import ManagementLocksOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
