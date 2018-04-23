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

from msrest.serialization import Model


class UpdateSystemServicesResponse(Model):
    """Response of the update system services API.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar update_status: Update status. Possible values include: 'Unknown',
     'Updating', 'Creating', 'Deleting', 'Succeeded', 'Failed', 'Canceled'
    :vartype update_status: str or
     ~azure.mgmt.machinelearningcompute.models.OperationStatus
    :ivar update_started_on: The date and time when the last system services
     update was started.
    :vartype update_started_on: datetime
    :ivar update_completed_on: The date and time when the last system services
     update completed.
    :vartype update_completed_on: datetime
    """

    _validation = {
        'update_status': {'readonly': True},
        'update_started_on': {'readonly': True},
        'update_completed_on': {'readonly': True},
    }

    _attribute_map = {
        'update_status': {'key': 'updateStatus', 'type': 'str'},
        'update_started_on': {'key': 'updateStartedOn', 'type': 'iso-8601'},
        'update_completed_on': {'key': 'updateCompletedOn', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs) -> None:
        super(UpdateSystemServicesResponse, self).__init__(**kwargs)
        self.update_status = None
        self.update_started_on = None
        self.update_completed_on = None