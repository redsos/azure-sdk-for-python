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


class ServerConnectionPolicy(ProxyResource):
    """A server secure connection policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar kind: Metadata used for the Azure portal experience.
    :vartype kind: str
    :ivar location: Resource location.
    :vartype location: str
    :param connection_type: Required. The server connection type. Possible
     values include: 'Default', 'Proxy', 'Redirect'
    :type connection_type: str or ~azure.mgmt.sql.models.ServerConnectionType
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'readonly': True},
        'location': {'readonly': True},
        'connection_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'connection_type': {'key': 'properties.connectionType', 'type': 'ServerConnectionType'},
    }

    def __init__(self, *, connection_type, **kwargs) -> None:
        super(ServerConnectionPolicy, self).__init__(, **kwargs)
        self.kind = None
        self.location = None
        self.connection_type = connection_type