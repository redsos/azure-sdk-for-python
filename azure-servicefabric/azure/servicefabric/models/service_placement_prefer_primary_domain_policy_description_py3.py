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

from .service_placement_policy_description import ServicePlacementPolicyDescription


class ServicePlacementPreferPrimaryDomainPolicyDescription(ServicePlacementPolicyDescription):
    """Describes the policy to be used for placement of a Service Fabric service
    where the service's Primary replicas should optimally be placed in a
    particular domain.
    This placement policy is usually used with fault domains in scenarios where
    the Service Fabric cluster is geographically distributed in order to
    indicate that a service�s primary replica should be located in a particular
    fault domain, which in geo-distributed scenarios usually aligns with
    regional or datacenter boundaries. Note that since this is an optimization
    it is possible that the Primary replica may not end up located in this
    domain due to failures, capacity limits, or other constraints.
    .

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param domain_name: The name of the domain that should used for placement
     as per this policy.
    :type domain_name: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'Type', 'type': 'str'},
        'domain_name': {'key': 'DomainName', 'type': 'str'},
    }

    def __init__(self, *, domain_name: str=None, **kwargs) -> None:
        super(ServicePlacementPreferPrimaryDomainPolicyDescription, self).__init__(, **kwargs)
        self.domain_name = domain_name
        self.type = 'PreferPrimaryDomain'