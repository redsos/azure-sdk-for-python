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

from .proxy_only_resource import ProxyOnlyResource


class SourceControl(ProxyOnlyResource):
    """The source control OAuth token.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param source_control_name: Name or source control type.
    :type source_control_name: str
    :param token: OAuth access token.
    :type token: str
    :param token_secret: OAuth access token secret.
    :type token_secret: str
    :param refresh_token: OAuth refresh token.
    :type refresh_token: str
    :param expiration_time: OAuth token expiration.
    :type expiration_time: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'source_control_name': {'key': 'properties.name', 'type': 'str'},
        'token': {'key': 'properties.token', 'type': 'str'},
        'token_secret': {'key': 'properties.tokenSecret', 'type': 'str'},
        'refresh_token': {'key': 'properties.refreshToken', 'type': 'str'},
        'expiration_time': {'key': 'properties.expirationTime', 'type': 'iso-8601'},
    }

    def __init__(self, kind=None, source_control_name=None, token=None, token_secret=None, refresh_token=None, expiration_time=None):
        super(SourceControl, self).__init__(kind=kind)
        self.source_control_name = source_control_name
        self.token = token
        self.token_secret = token_secret
        self.refresh_token = refresh_token
        self.expiration_time = expiration_time
