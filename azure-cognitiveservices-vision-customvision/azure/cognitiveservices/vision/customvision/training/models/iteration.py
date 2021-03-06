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


class Iteration(Model):
    """Iteration model to be sent over JSON.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Gets the id of the iteration
    :vartype id: str
    :param name: Gets or sets the name of the iteration
    :type name: str
    :param is_default: Gets or sets a value indicating whether the iteration
     is the default iteration for the project
    :type is_default: bool
    :ivar status: Gets the current iteration status
    :vartype status: str
    :ivar created: Gets the time this iteration was completed
    :vartype created: datetime
    :ivar last_modified: Gets the time this iteration was last modified
    :vartype last_modified: datetime
    :ivar trained_at: Gets the time this iteration was last modified
    :vartype trained_at: datetime
    :ivar project_id: Gets the project id of the iteration
    :vartype project_id: str
    :ivar exportable: Whether the iteration can be exported to another format
     for download
    :vartype exportable: bool
    :ivar domain_id: Get or sets a guid of the domain the iteration has been
     trained on
    :vartype domain_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'status': {'readonly': True},
        'created': {'readonly': True},
        'last_modified': {'readonly': True},
        'trained_at': {'readonly': True},
        'project_id': {'readonly': True},
        'exportable': {'readonly': True},
        'domain_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'name': {'key': 'Name', 'type': 'str'},
        'is_default': {'key': 'IsDefault', 'type': 'bool'},
        'status': {'key': 'Status', 'type': 'str'},
        'created': {'key': 'Created', 'type': 'iso-8601'},
        'last_modified': {'key': 'LastModified', 'type': 'iso-8601'},
        'trained_at': {'key': 'TrainedAt', 'type': 'iso-8601'},
        'project_id': {'key': 'ProjectId', 'type': 'str'},
        'exportable': {'key': 'Exportable', 'type': 'bool'},
        'domain_id': {'key': 'DomainId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Iteration, self).__init__(**kwargs)
        self.id = None
        self.name = kwargs.get('name', None)
        self.is_default = kwargs.get('is_default', None)
        self.status = None
        self.created = None
        self.last_modified = None
        self.trained_at = None
        self.project_id = None
        self.exportable = None
        self.domain_id = None
