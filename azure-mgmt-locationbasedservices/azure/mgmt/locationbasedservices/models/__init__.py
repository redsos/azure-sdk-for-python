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
    from .error_details_item_py3 import ErrorDetailsItem
    from .error_py3 import Error, ErrorException
    from .resource_py3 import Resource
    from .sku_py3 import Sku
    from .location_based_services_account_py3 import LocationBasedServicesAccount
    from .location_based_services_account_create_parameters_py3 import LocationBasedServicesAccountCreateParameters
    from .location_based_services_account_update_parameters_py3 import LocationBasedServicesAccountUpdateParameters
    from .location_based_services_accounts_move_request_py3 import LocationBasedServicesAccountsMoveRequest
    from .location_based_services_key_specification_py3 import LocationBasedServicesKeySpecification
    from .location_based_services_account_keys_py3 import LocationBasedServicesAccountKeys
    from .location_based_services_operations_value_item_display_py3 import LocationBasedServicesOperationsValueItemDisplay
    from .location_based_services_operations_value_item_py3 import LocationBasedServicesOperationsValueItem
except (SyntaxError, ImportError):
    from .error_details_item import ErrorDetailsItem
    from .error import Error, ErrorException
    from .resource import Resource
    from .sku import Sku
    from .location_based_services_account import LocationBasedServicesAccount
    from .location_based_services_account_create_parameters import LocationBasedServicesAccountCreateParameters
    from .location_based_services_account_update_parameters import LocationBasedServicesAccountUpdateParameters
    from .location_based_services_accounts_move_request import LocationBasedServicesAccountsMoveRequest
    from .location_based_services_key_specification import LocationBasedServicesKeySpecification
    from .location_based_services_account_keys import LocationBasedServicesAccountKeys
    from .location_based_services_operations_value_item_display import LocationBasedServicesOperationsValueItemDisplay
    from .location_based_services_operations_value_item import LocationBasedServicesOperationsValueItem
from .location_based_services_account_paged import LocationBasedServicesAccountPaged
from .location_based_services_operations_value_item_paged import LocationBasedServicesOperationsValueItemPaged
from .location_based_services_management_client_enums import (
    KeyType,
)

__all__ = [
    'ErrorDetailsItem',
    'Error', 'ErrorException',
    'Resource',
    'Sku',
    'LocationBasedServicesAccount',
    'LocationBasedServicesAccountCreateParameters',
    'LocationBasedServicesAccountUpdateParameters',
    'LocationBasedServicesAccountsMoveRequest',
    'LocationBasedServicesKeySpecification',
    'LocationBasedServicesAccountKeys',
    'LocationBasedServicesOperationsValueItemDisplay',
    'LocationBasedServicesOperationsValueItem',
    'LocationBasedServicesAccountPaged',
    'LocationBasedServicesOperationsValueItemPaged',
    'KeyType',
]