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

try:
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .key_py3 import Key
    from .usage_counter_name_py3 import UsageCounterName
    from .usage_py3 import Usage
    from .statistics_py3 import Statistics
    from .runbook_association_property_py3 import RunbookAssociationProperty
    from .webhook_py3 import Webhook
    from .variable_py3 import Variable
    from .job_provisioning_state_property_py3 import JobProvisioningStateProperty
    from .dsc_configuration_association_property_py3 import DscConfigurationAssociationProperty
    from .dsc_compilation_job_py3 import DscCompilationJob
    from .credential_py3 import Credential
    from .connection_type_association_property_py3 import ConnectionTypeAssociationProperty
    from .connection_py3 import Connection
    from .certificate_py3 import Certificate
    from .proxy_resource_py3 import ProxyResource
    from .resource_py3 import Resource
    from .runbook_parameter_py3 import RunbookParameter
    from .content_hash_py3 import ContentHash
    from .content_link_py3 import ContentLink
    from .runbook_draft_py3 import RunbookDraft
    from .runbook_py3 import Runbook
    from .module_error_info_py3 import ModuleErrorInfo
    from .module_py3 import Module
    from .content_source_py3 import ContentSource
    from .dsc_configuration_parameter_py3 import DscConfigurationParameter
    from .dsc_configuration_py3 import DscConfiguration
    from .tracked_resource_py3 import TrackedResource
    from .sku_py3 import Sku
    from .automation_account_py3 import AutomationAccount
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .automation_account_create_or_update_parameters_py3 import AutomationAccountCreateOrUpdateParameters
    from .automation_account_update_parameters_py3 import AutomationAccountUpdateParameters
    from .certificate_update_parameters_py3 import CertificateUpdateParameters
    from .certificate_create_or_update_parameters_py3 import CertificateCreateOrUpdateParameters
    from .connection_update_parameters_py3 import ConnectionUpdateParameters
    from .connection_create_or_update_parameters_py3 import ConnectionCreateOrUpdateParameters
    from .field_definition_py3 import FieldDefinition
    from .connection_type_py3 import ConnectionType
    from .connection_type_create_or_update_parameters_py3 import ConnectionTypeCreateOrUpdateParameters
    from .credential_update_parameters_py3 import CredentialUpdateParameters
    from .credential_create_or_update_parameters_py3 import CredentialCreateOrUpdateParameters
    from .activity_parameter_py3 import ActivityParameter
    from .activity_parameter_set_py3 import ActivityParameterSet
    from .activity_output_type_py3 import ActivityOutputType
    from .activity_py3 import Activity
    from .advanced_schedule_monthly_occurrence_py3 import AdvancedScheduleMonthlyOccurrence
    from .advanced_schedule_py3 import AdvancedSchedule
    from .agent_registration_keys_py3 import AgentRegistrationKeys
    from .agent_registration_py3 import AgentRegistration
    from .agent_registration_regenerate_key_parameter_py3 import AgentRegistrationRegenerateKeyParameter
    from .dsc_compilation_job_create_parameters_py3 import DscCompilationJobCreateParameters
    from .dsc_configuration_create_or_update_parameters_py3 import DscConfigurationCreateOrUpdateParameters
    from .dsc_configuration_update_parameters_py3 import DscConfigurationUpdateParameters
    from .dsc_meta_configuration_py3 import DscMetaConfiguration
    from .dsc_node_configuration_create_or_update_parameters_py3 import DscNodeConfigurationCreateOrUpdateParameters
    from .dsc_node_configuration_association_property_py3 import DscNodeConfigurationAssociationProperty
    from .dsc_node_extension_handler_association_property_py3 import DscNodeExtensionHandlerAssociationProperty
    from .dsc_node_update_parameters_properties_py3 import DscNodeUpdateParametersProperties
    from .dsc_node_update_parameters_py3 import DscNodeUpdateParameters
    from .dsc_report_error_py3 import DscReportError
    from .dsc_report_resource_navigation_py3 import DscReportResourceNavigation
    from .dsc_report_resource_py3 import DscReportResource
    from .dsc_node_report_py3 import DscNodeReport
    from .hybrid_runbook_worker_py3 import HybridRunbookWorker
    from .run_as_credential_association_property_py3 import RunAsCredentialAssociationProperty
    from .hybrid_runbook_worker_group_py3 import HybridRunbookWorkerGroup
    from .hybrid_runbook_worker_group_update_parameters_py3 import HybridRunbookWorkerGroupUpdateParameters
    from .job_py3 import Job
    from .job_create_parameters_py3 import JobCreateParameters
    from .job_list_result_py3 import JobListResult
    from .schedule_association_property_py3 import ScheduleAssociationProperty
    from .job_schedule_create_parameters_py3 import JobScheduleCreateParameters
    from .job_schedule_py3 import JobSchedule
    from .job_stream_py3 import JobStream
    from .job_stream_list_result_py3 import JobStreamListResult
    from .linked_workspace_py3 import LinkedWorkspace
    from .module_create_or_update_parameters_py3 import ModuleCreateOrUpdateParameters
    from .module_update_parameters_py3 import ModuleUpdateParameters
    from .runbook_draft_undo_edit_result_py3 import RunbookDraftUndoEditResult
    from .runbook_create_or_update_parameters_py3 import RunbookCreateOrUpdateParameters
    from .runbook_create_or_update_draft_properties_py3 import RunbookCreateOrUpdateDraftProperties
    from .runbook_create_or_update_draft_parameters_py3 import RunbookCreateOrUpdateDraftParameters
    from .runbook_update_parameters_py3 import RunbookUpdateParameters
    from .schedule_create_or_update_parameters_py3 import ScheduleCreateOrUpdateParameters
    from .schedule_properties_py3 import ScheduleProperties
    from .schedule_py3 import Schedule
    from .schedule_update_parameters_py3 import ScheduleUpdateParameters
    from .sub_resource_py3 import SubResource
    from .test_job_create_parameters_py3 import TestJobCreateParameters
    from .test_job_py3 import TestJob
    from .type_field_py3 import TypeField
    from .variable_create_or_update_parameters_py3 import VariableCreateOrUpdateParameters
    from .variable_update_parameters_py3 import VariableUpdateParameters
    from .webhook_create_or_update_parameters_py3 import WebhookCreateOrUpdateParameters
    from .webhook_update_parameters_py3 import WebhookUpdateParameters
    from .job_collection_item_py3 import JobCollectionItem
    from .windows_properties_py3 import WindowsProperties
    from .linux_properties_py3 import LinuxProperties
    from .update_configuration_py3 import UpdateConfiguration
    from .software_update_configuration_py3 import SoftwareUpdateConfiguration
    from .collection_item_update_configuration_py3 import CollectionItemUpdateConfiguration
    from .software_update_configuration_collection_item_py3 import SoftwareUpdateConfigurationCollectionItem
    from .software_update_configuration_list_result_py3 import SoftwareUpdateConfigurationListResult
    from .update_configuration_navigation_py3 import UpdateConfigurationNavigation
    from .job_navigation_py3 import JobNavigation
    from .software_update_configuration_run_py3 import SoftwareUpdateConfigurationRun
    from .software_update_configuration_run_list_result_py3 import SoftwareUpdateConfigurationRunListResult
    from .software_update_configuration_machine_run_py3 import SoftwareUpdateConfigurationMachineRun
    from .software_update_configuration_machine_run_list_result_py3 import SoftwareUpdateConfigurationMachineRunListResult
    from .source_control_create_or_update_parameters_py3 import SourceControlCreateOrUpdateParameters
    from .source_control_py3 import SourceControl
    from .source_control_update_parameters_py3 import SourceControlUpdateParameters
    from .source_control_sync_job_py3 import SourceControlSyncJob
    from .source_control_sync_job_create_parameters_py3 import SourceControlSyncJobCreateParameters
    from .source_control_sync_job_by_id_errors_py3 import SourceControlSyncJobByIdErrors
    from .source_control_sync_job_by_id_py3 import SourceControlSyncJobById
    from .dsc_node_py3 import DscNode
    from .dsc_node_configuration_py3 import DscNodeConfiguration
except (SyntaxError, ImportError):
    from .error_response import ErrorResponse, ErrorResponseException
    from .key import Key
    from .usage_counter_name import UsageCounterName
    from .usage import Usage
    from .statistics import Statistics
    from .runbook_association_property import RunbookAssociationProperty
    from .webhook import Webhook
    from .variable import Variable
    from .job_provisioning_state_property import JobProvisioningStateProperty
    from .dsc_configuration_association_property import DscConfigurationAssociationProperty
    from .dsc_compilation_job import DscCompilationJob
    from .credential import Credential
    from .connection_type_association_property import ConnectionTypeAssociationProperty
    from .connection import Connection
    from .certificate import Certificate
    from .proxy_resource import ProxyResource
    from .resource import Resource
    from .runbook_parameter import RunbookParameter
    from .content_hash import ContentHash
    from .content_link import ContentLink
    from .runbook_draft import RunbookDraft
    from .runbook import Runbook
    from .module_error_info import ModuleErrorInfo
    from .module import Module
    from .content_source import ContentSource
    from .dsc_configuration_parameter import DscConfigurationParameter
    from .dsc_configuration import DscConfiguration
    from .tracked_resource import TrackedResource
    from .sku import Sku
    from .automation_account import AutomationAccount
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .automation_account_create_or_update_parameters import AutomationAccountCreateOrUpdateParameters
    from .automation_account_update_parameters import AutomationAccountUpdateParameters
    from .certificate_update_parameters import CertificateUpdateParameters
    from .certificate_create_or_update_parameters import CertificateCreateOrUpdateParameters
    from .connection_update_parameters import ConnectionUpdateParameters
    from .connection_create_or_update_parameters import ConnectionCreateOrUpdateParameters
    from .field_definition import FieldDefinition
    from .connection_type import ConnectionType
    from .connection_type_create_or_update_parameters import ConnectionTypeCreateOrUpdateParameters
    from .credential_update_parameters import CredentialUpdateParameters
    from .credential_create_or_update_parameters import CredentialCreateOrUpdateParameters
    from .activity_parameter import ActivityParameter
    from .activity_parameter_set import ActivityParameterSet
    from .activity_output_type import ActivityOutputType
    from .activity import Activity
    from .advanced_schedule_monthly_occurrence import AdvancedScheduleMonthlyOccurrence
    from .advanced_schedule import AdvancedSchedule
    from .agent_registration_keys import AgentRegistrationKeys
    from .agent_registration import AgentRegistration
    from .agent_registration_regenerate_key_parameter import AgentRegistrationRegenerateKeyParameter
    from .dsc_compilation_job_create_parameters import DscCompilationJobCreateParameters
    from .dsc_configuration_create_or_update_parameters import DscConfigurationCreateOrUpdateParameters
    from .dsc_configuration_update_parameters import DscConfigurationUpdateParameters
    from .dsc_meta_configuration import DscMetaConfiguration
    from .dsc_node_configuration_create_or_update_parameters import DscNodeConfigurationCreateOrUpdateParameters
    from .dsc_node_configuration_association_property import DscNodeConfigurationAssociationProperty
    from .dsc_node_extension_handler_association_property import DscNodeExtensionHandlerAssociationProperty
    from .dsc_node_update_parameters_properties import DscNodeUpdateParametersProperties
    from .dsc_node_update_parameters import DscNodeUpdateParameters
    from .dsc_report_error import DscReportError
    from .dsc_report_resource_navigation import DscReportResourceNavigation
    from .dsc_report_resource import DscReportResource
    from .dsc_node_report import DscNodeReport
    from .hybrid_runbook_worker import HybridRunbookWorker
    from .run_as_credential_association_property import RunAsCredentialAssociationProperty
    from .hybrid_runbook_worker_group import HybridRunbookWorkerGroup
    from .hybrid_runbook_worker_group_update_parameters import HybridRunbookWorkerGroupUpdateParameters
    from .job import Job
    from .job_create_parameters import JobCreateParameters
    from .job_list_result import JobListResult
    from .schedule_association_property import ScheduleAssociationProperty
    from .job_schedule_create_parameters import JobScheduleCreateParameters
    from .job_schedule import JobSchedule
    from .job_stream import JobStream
    from .job_stream_list_result import JobStreamListResult
    from .linked_workspace import LinkedWorkspace
    from .module_create_or_update_parameters import ModuleCreateOrUpdateParameters
    from .module_update_parameters import ModuleUpdateParameters
    from .runbook_draft_undo_edit_result import RunbookDraftUndoEditResult
    from .runbook_create_or_update_parameters import RunbookCreateOrUpdateParameters
    from .runbook_create_or_update_draft_properties import RunbookCreateOrUpdateDraftProperties
    from .runbook_create_or_update_draft_parameters import RunbookCreateOrUpdateDraftParameters
    from .runbook_update_parameters import RunbookUpdateParameters
    from .schedule_create_or_update_parameters import ScheduleCreateOrUpdateParameters
    from .schedule_properties import ScheduleProperties
    from .schedule import Schedule
    from .schedule_update_parameters import ScheduleUpdateParameters
    from .sub_resource import SubResource
    from .test_job_create_parameters import TestJobCreateParameters
    from .test_job import TestJob
    from .type_field import TypeField
    from .variable_create_or_update_parameters import VariableCreateOrUpdateParameters
    from .variable_update_parameters import VariableUpdateParameters
    from .webhook_create_or_update_parameters import WebhookCreateOrUpdateParameters
    from .webhook_update_parameters import WebhookUpdateParameters
    from .job_collection_item import JobCollectionItem
    from .windows_properties import WindowsProperties
    from .linux_properties import LinuxProperties
    from .update_configuration import UpdateConfiguration
    from .software_update_configuration import SoftwareUpdateConfiguration
    from .collection_item_update_configuration import CollectionItemUpdateConfiguration
    from .software_update_configuration_collection_item import SoftwareUpdateConfigurationCollectionItem
    from .software_update_configuration_list_result import SoftwareUpdateConfigurationListResult
    from .update_configuration_navigation import UpdateConfigurationNavigation
    from .job_navigation import JobNavigation
    from .software_update_configuration_run import SoftwareUpdateConfigurationRun
    from .software_update_configuration_run_list_result import SoftwareUpdateConfigurationRunListResult
    from .software_update_configuration_machine_run import SoftwareUpdateConfigurationMachineRun
    from .software_update_configuration_machine_run_list_result import SoftwareUpdateConfigurationMachineRunListResult
    from .source_control_create_or_update_parameters import SourceControlCreateOrUpdateParameters
    from .source_control import SourceControl
    from .source_control_update_parameters import SourceControlUpdateParameters
    from .source_control_sync_job import SourceControlSyncJob
    from .source_control_sync_job_create_parameters import SourceControlSyncJobCreateParameters
    from .source_control_sync_job_by_id_errors import SourceControlSyncJobByIdErrors
    from .source_control_sync_job_by_id import SourceControlSyncJobById
    from .dsc_node import DscNode
    from .dsc_node_configuration import DscNodeConfiguration
from .automation_account_paged import AutomationAccountPaged
from .operation_paged import OperationPaged
from .statistics_paged import StatisticsPaged
from .usage_paged import UsagePaged
from .key_paged import KeyPaged
from .certificate_paged import CertificatePaged
from .connection_paged import ConnectionPaged
from .connection_type_paged import ConnectionTypePaged
from .credential_paged import CredentialPaged
from .dsc_configuration_paged import DscConfigurationPaged
from .hybrid_runbook_worker_group_paged import HybridRunbookWorkerGroupPaged
from .job_schedule_paged import JobSchedulePaged
from .activity_paged import ActivityPaged
from .module_paged import ModulePaged
from .type_field_paged import TypeFieldPaged
from .runbook_paged import RunbookPaged
from .job_stream_paged import JobStreamPaged
from .schedule_paged import SchedulePaged
from .variable_paged import VariablePaged
from .webhook_paged import WebhookPaged
from .source_control_paged import SourceControlPaged
from .source_control_sync_job_paged import SourceControlSyncJobPaged
from .job_collection_item_paged import JobCollectionItemPaged
from .dsc_node_paged import DscNodePaged
from .dsc_node_report_paged import DscNodeReportPaged
from .dsc_compilation_job_paged import DscCompilationJobPaged
from .dsc_node_configuration_paged import DscNodeConfigurationPaged
from .automation_client_enums import (
    AutomationKeyName,
    AutomationKeyPermissions,
    JobProvisioningState,
    JobStatus,
    RunbookTypeEnum,
    RunbookState,
    RunbookProvisioningState,
    ModuleProvisioningState,
    ContentSourceType,
    DscConfigurationProvisioningState,
    DscConfigurationState,
    SkuNameEnum,
    AutomationAccountState,
    ScheduleDay,
    AgentRegistrationKeyName,
    JobStreamType,
    HttpStatusCode,
    ScheduleFrequency,
    OperatingSystemType,
    WindowsUpdateClasses,
    LinuxUpdateClasses,
    SourceType,
    ProvisioningState,
)

__all__ = [
    'ErrorResponse', 'ErrorResponseException',
    'Key',
    'UsageCounterName',
    'Usage',
    'Statistics',
    'RunbookAssociationProperty',
    'Webhook',
    'Variable',
    'JobProvisioningStateProperty',
    'DscConfigurationAssociationProperty',
    'DscCompilationJob',
    'Credential',
    'ConnectionTypeAssociationProperty',
    'Connection',
    'Certificate',
    'ProxyResource',
    'Resource',
    'RunbookParameter',
    'ContentHash',
    'ContentLink',
    'RunbookDraft',
    'Runbook',
    'ModuleErrorInfo',
    'Module',
    'ContentSource',
    'DscConfigurationParameter',
    'DscConfiguration',
    'TrackedResource',
    'Sku',
    'AutomationAccount',
    'OperationDisplay',
    'Operation',
    'AutomationAccountCreateOrUpdateParameters',
    'AutomationAccountUpdateParameters',
    'CertificateUpdateParameters',
    'CertificateCreateOrUpdateParameters',
    'ConnectionUpdateParameters',
    'ConnectionCreateOrUpdateParameters',
    'FieldDefinition',
    'ConnectionType',
    'ConnectionTypeCreateOrUpdateParameters',
    'CredentialUpdateParameters',
    'CredentialCreateOrUpdateParameters',
    'ActivityParameter',
    'ActivityParameterSet',
    'ActivityOutputType',
    'Activity',
    'AdvancedScheduleMonthlyOccurrence',
    'AdvancedSchedule',
    'AgentRegistrationKeys',
    'AgentRegistration',
    'AgentRegistrationRegenerateKeyParameter',
    'DscCompilationJobCreateParameters',
    'DscConfigurationCreateOrUpdateParameters',
    'DscConfigurationUpdateParameters',
    'DscMetaConfiguration',
    'DscNodeConfigurationCreateOrUpdateParameters',
    'DscNodeConfigurationAssociationProperty',
    'DscNodeExtensionHandlerAssociationProperty',
    'DscNodeUpdateParametersProperties',
    'DscNodeUpdateParameters',
    'DscReportError',
    'DscReportResourceNavigation',
    'DscReportResource',
    'DscNodeReport',
    'HybridRunbookWorker',
    'RunAsCredentialAssociationProperty',
    'HybridRunbookWorkerGroup',
    'HybridRunbookWorkerGroupUpdateParameters',
    'Job',
    'JobCreateParameters',
    'JobListResult',
    'ScheduleAssociationProperty',
    'JobScheduleCreateParameters',
    'JobSchedule',
    'JobStream',
    'JobStreamListResult',
    'LinkedWorkspace',
    'ModuleCreateOrUpdateParameters',
    'ModuleUpdateParameters',
    'RunbookDraftUndoEditResult',
    'RunbookCreateOrUpdateParameters',
    'RunbookCreateOrUpdateDraftProperties',
    'RunbookCreateOrUpdateDraftParameters',
    'RunbookUpdateParameters',
    'ScheduleCreateOrUpdateParameters',
    'ScheduleProperties',
    'Schedule',
    'ScheduleUpdateParameters',
    'SubResource',
    'TestJobCreateParameters',
    'TestJob',
    'TypeField',
    'VariableCreateOrUpdateParameters',
    'VariableUpdateParameters',
    'WebhookCreateOrUpdateParameters',
    'WebhookUpdateParameters',
    'JobCollectionItem',
    'WindowsProperties',
    'LinuxProperties',
    'UpdateConfiguration',
    'SoftwareUpdateConfiguration',
    'CollectionItemUpdateConfiguration',
    'SoftwareUpdateConfigurationCollectionItem',
    'SoftwareUpdateConfigurationListResult',
    'UpdateConfigurationNavigation',
    'JobNavigation',
    'SoftwareUpdateConfigurationRun',
    'SoftwareUpdateConfigurationRunListResult',
    'SoftwareUpdateConfigurationMachineRun',
    'SoftwareUpdateConfigurationMachineRunListResult',
    'SourceControlCreateOrUpdateParameters',
    'SourceControl',
    'SourceControlUpdateParameters',
    'SourceControlSyncJob',
    'SourceControlSyncJobCreateParameters',
    'SourceControlSyncJobByIdErrors',
    'SourceControlSyncJobById',
    'DscNode',
    'DscNodeConfiguration',
    'AutomationAccountPaged',
    'OperationPaged',
    'StatisticsPaged',
    'UsagePaged',
    'KeyPaged',
    'CertificatePaged',
    'ConnectionPaged',
    'ConnectionTypePaged',
    'CredentialPaged',
    'DscConfigurationPaged',
    'HybridRunbookWorkerGroupPaged',
    'JobSchedulePaged',
    'ActivityPaged',
    'ModulePaged',
    'TypeFieldPaged',
    'RunbookPaged',
    'JobStreamPaged',
    'SchedulePaged',
    'VariablePaged',
    'WebhookPaged',
    'SourceControlPaged',
    'SourceControlSyncJobPaged',
    'JobCollectionItemPaged',
    'DscNodePaged',
    'DscNodeReportPaged',
    'DscCompilationJobPaged',
    'DscNodeConfigurationPaged',
    'AutomationKeyName',
    'AutomationKeyPermissions',
    'JobProvisioningState',
    'JobStatus',
    'RunbookTypeEnum',
    'RunbookState',
    'RunbookProvisioningState',
    'ModuleProvisioningState',
    'ContentSourceType',
    'DscConfigurationProvisioningState',
    'DscConfigurationState',
    'SkuNameEnum',
    'AutomationAccountState',
    'ScheduleDay',
    'AgentRegistrationKeyName',
    'JobStreamType',
    'HttpStatusCode',
    'ScheduleFrequency',
    'OperatingSystemType',
    'WindowsUpdateClasses',
    'LinuxUpdateClasses',
    'SourceType',
    'ProvisioningState',
]