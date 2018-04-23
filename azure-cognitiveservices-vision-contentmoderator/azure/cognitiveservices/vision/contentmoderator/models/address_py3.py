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


class Address(Model):
    """Address details.

    :param text: Detected Address.
    :type text: str
    :param index: Index(Location) of the Address in the input text content.
    :type index: int
    """

    _attribute_map = {
        'text': {'key': 'Text', 'type': 'str'},
        'index': {'key': 'Index', 'type': 'int'},
    }

    def __init__(self, *, text: str=None, index: int=None, **kwargs) -> None:
        super(Address, self).__init__(**kwargs)
        self.text = text
        self.index = index