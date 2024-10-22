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


class DestinyItemGearsetBlockDefinition(object):
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
        'tracking_value_max': 'int',
        'item_list': 'list[int]'
    }

    attribute_map = {
        'tracking_value_max': 'trackingValueMax',
        'item_list': 'itemList'
    }

    def __init__(self, tracking_value_max=None, item_list=None):  # noqa: E501
        """DestinyItemGearsetBlockDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._tracking_value_max = None
        self._item_list = None
        self.discriminator = None

        if tracking_value_max is not None:
            self.tracking_value_max = tracking_value_max
        if item_list is not None:
            self.item_list = item_list

    @property
    def tracking_value_max(self):
        """Gets the tracking_value_max of this DestinyItemGearsetBlockDefinition.  # noqa: E501

        The maximum possible number of items that can be collected.  # noqa: E501

        :return: The tracking_value_max of this DestinyItemGearsetBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._tracking_value_max

    @tracking_value_max.setter
    def tracking_value_max(self, tracking_value_max):
        """Sets the tracking_value_max of this DestinyItemGearsetBlockDefinition.

        The maximum possible number of items that can be collected.  # noqa: E501

        :param tracking_value_max: The tracking_value_max of this DestinyItemGearsetBlockDefinition.  # noqa: E501
        :type: int
        """

        self._tracking_value_max = tracking_value_max

    @property
    def item_list(self):
        """Gets the item_list of this DestinyItemGearsetBlockDefinition.  # noqa: E501

        The list of hashes for items in the gearset. Use them to look up DestinyInventoryItemDefinition entries for the items in the set.  # noqa: E501

        :return: The item_list of this DestinyItemGearsetBlockDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._item_list

    @item_list.setter
    def item_list(self, item_list):
        """Sets the item_list of this DestinyItemGearsetBlockDefinition.

        The list of hashes for items in the gearset. Use them to look up DestinyInventoryItemDefinition entries for the items in the set.  # noqa: E501

        :param item_list: The item_list of this DestinyItemGearsetBlockDefinition.  # noqa: E501
        :type: list[int]
        """

        self._item_list = item_list

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
        if not isinstance(other, DestinyItemGearsetBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
