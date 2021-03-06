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

from .proxy_resource import ProxyResource


class DatabaseAutomaticTuning(ProxyResource):
    """Database-level Automatic Tuning.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param desired_state: Automatic tuning desired state. Possible values
     include: 'Inherit', 'Custom', 'Auto', 'Unspecified'
    :type desired_state: str or ~azure.mgmt.sql.models.AutomaticTuningMode
    :ivar actual_state: Automatic tuning actual state. Possible values
     include: 'Inherit', 'Custom', 'Auto', 'Unspecified'
    :vartype actual_state: str or ~azure.mgmt.sql.models.AutomaticTuningMode
    :param options: Automatic tuning options definition.
    :type options: dict[str, ~azure.mgmt.sql.models.AutomaticTuningOptions]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'actual_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'desired_state': {'key': 'properties.desiredState', 'type': 'AutomaticTuningMode'},
        'actual_state': {'key': 'properties.actualState', 'type': 'AutomaticTuningMode'},
        'options': {'key': 'properties.options', 'type': '{AutomaticTuningOptions}'},
    }

    def __init__(self, *, desired_state=None, options=None, **kwargs) -> None:
        super(DatabaseAutomaticTuning, self).__init__(**kwargs)
        self.desired_state = desired_state
        self.actual_state = None
        self.options = options
