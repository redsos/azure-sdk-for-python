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


class CreateOrUpdateFirewallRuleParameters(Model):
    """The parameters used to create a new firewall rule.

    All required parameters must be populated in order to send to Azure.

    :param start_ip_address: Required. The start IP address for the firewall
     rule. This can be either ipv4 or ipv6. Start and End should be in the same
     protocol.
    :type start_ip_address: str
    :param end_ip_address: Required. The end IP address for the firewall rule.
     This can be either ipv4 or ipv6. Start and End should be in the same
     protocol.
    :type end_ip_address: str
    """

    _validation = {
        'start_ip_address': {'required': True},
        'end_ip_address': {'required': True},
    }

    _attribute_map = {
        'start_ip_address': {'key': 'properties.startIpAddress', 'type': 'str'},
        'end_ip_address': {'key': 'properties.endIpAddress', 'type': 'str'},
    }

    def __init__(self, *, start_ip_address: str, end_ip_address: str, **kwargs) -> None:
        super(CreateOrUpdateFirewallRuleParameters, self).__init__(**kwargs)
        self.start_ip_address = start_ip_address
        self.end_ip_address = end_ip_address