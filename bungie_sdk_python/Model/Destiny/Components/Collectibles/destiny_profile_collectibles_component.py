# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.  # noqa: E501

    OpenAPI spec version: 2.3.6
    Contact: support@bungie.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DestinyProfileCollectiblesComponent(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'recent_collectible_hashes': 'list[int]',
        'newness_flagged_collectible_hashes': 'list[int]',
        'collectibles': 'dict(str, DestinyCollectibleComponent)'
    }

    attribute_map = {
        'recent_collectible_hashes': 'recentCollectibleHashes',
        'newness_flagged_collectible_hashes': 'newnessFlaggedCollectibleHashes',
        'collectibles': 'collectibles'
    }

    def __init__(self, recent_collectible_hashes=None, newness_flagged_collectible_hashes=None, collectibles=None):  # noqa: E501
        """DestinyProfileCollectiblesComponent - a model defined in OpenAPI"""  # noqa: E501

        self._recent_collectible_hashes = None
        self._newness_flagged_collectible_hashes = None
        self._collectibles = None
        self.discriminator = None

        if recent_collectible_hashes is not None:
            self.recent_collectible_hashes = recent_collectible_hashes
        if newness_flagged_collectible_hashes is not None:
            self.newness_flagged_collectible_hashes = newness_flagged_collectible_hashes
        if collectibles is not None:
            self.collectibles = collectibles

    @property
    def recent_collectible_hashes(self):
        """Gets the recent_collectible_hashes of this DestinyProfileCollectiblesComponent.  # noqa: E501

        The list of collectibles determined by the game as having been \"recently\" acquired.  # noqa: E501

        :return: The recent_collectible_hashes of this DestinyProfileCollectiblesComponent.  # noqa: E501
        :rtype: list[int]
        """
        return self._recent_collectible_hashes

    @recent_collectible_hashes.setter
    def recent_collectible_hashes(self, recent_collectible_hashes):
        """Sets the recent_collectible_hashes of this DestinyProfileCollectiblesComponent.

        The list of collectibles determined by the game as having been \"recently\" acquired.  # noqa: E501

        :param recent_collectible_hashes: The recent_collectible_hashes of this DestinyProfileCollectiblesComponent.  # noqa: E501
        :type: list[int]
        """

        self._recent_collectible_hashes = recent_collectible_hashes

    @property
    def newness_flagged_collectible_hashes(self):
        """Gets the newness_flagged_collectible_hashes of this DestinyProfileCollectiblesComponent.  # noqa: E501

        The list of collectibles determined by the game as having been \"recently\" acquired.  The game client itself actually controls this data, so I personally question whether anyone will get much use out of this: because we can't edit this value through the API. But in case anyone finds it useful, here it is.  # noqa: E501

        :return: The newness_flagged_collectible_hashes of this DestinyProfileCollectiblesComponent.  # noqa: E501
        :rtype: list[int]
        """
        return self._newness_flagged_collectible_hashes

    @newness_flagged_collectible_hashes.setter
    def newness_flagged_collectible_hashes(self, newness_flagged_collectible_hashes):
        """Sets the newness_flagged_collectible_hashes of this DestinyProfileCollectiblesComponent.

        The list of collectibles determined by the game as having been \"recently\" acquired.  The game client itself actually controls this data, so I personally question whether anyone will get much use out of this: because we can't edit this value through the API. But in case anyone finds it useful, here it is.  # noqa: E501

        :param newness_flagged_collectible_hashes: The newness_flagged_collectible_hashes of this DestinyProfileCollectiblesComponent.  # noqa: E501
        :type: list[int]
        """

        self._newness_flagged_collectible_hashes = newness_flagged_collectible_hashes

    @property
    def collectibles(self):
        """Gets the collectibles of this DestinyProfileCollectiblesComponent.  # noqa: E501


        :return: The collectibles of this DestinyProfileCollectiblesComponent.  # noqa: E501
        :rtype: dict(str, DestinyCollectibleComponent)
        """
        return self._collectibles

    @collectibles.setter
    def collectibles(self, collectibles):
        """Sets the collectibles of this DestinyProfileCollectiblesComponent.


        :param collectibles: The collectibles of this DestinyProfileCollectiblesComponent.  # noqa: E501
        :type: dict(str, DestinyCollectibleComponent)
        """

        self._collectibles = collectibles

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DestinyProfileCollectiblesComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
