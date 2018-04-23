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

from .response import Response


class TrendingVideos(Response):
    """TrendingVideos.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :param banner_tiles: Required.
    :type banner_tiles:
     list[~azure.cognitiveservices.search.videosearch.models.TrendingVideosTile]
    :param categories: Required.
    :type categories:
     list[~azure.cognitiveservices.search.videosearch.models.TrendingVideosCategory]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'banner_tiles': {'required': True},
        'categories': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'banner_tiles': {'key': 'bannerTiles', 'type': '[TrendingVideosTile]'},
        'categories': {'key': 'categories', 'type': '[TrendingVideosCategory]'},
    }

    def __init__(self, *, banner_tiles, categories, **kwargs) -> None:
        super(TrendingVideos, self).__init__(, **kwargs)
        self.banner_tiles = banner_tiles
        self.categories = categories
        self._type = 'TrendingVideos'