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


class DestinyVendorItemQuantity(object):
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
        'item_hash': 'int',
        'item_instance_id': 'int',
        'quantity': 'int'
    }

    attribute_map = {
        'item_hash': 'itemHash',
        'item_instance_id': 'itemInstanceId',
        'quantity': 'quantity'
    }

    def __init__(self, item_hash=None, item_instance_id=None, quantity=None):  # noqa: E501
        """DestinyVendorItemQuantity - a model defined in OpenAPI"""  # noqa: E501

        self._item_hash = None
        self._item_instance_id = None
        self._quantity = None
        self.discriminator = None

        if item_hash is not None:
            self.item_hash = item_hash
        self.item_instance_id = item_instance_id
        if quantity is not None:
            self.quantity = quantity

    @property
    def item_hash(self):
        """Gets the item_hash of this DestinyVendorItemQuantity.  # noqa: E501

        The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.  # noqa: E501

        :return: The item_hash of this DestinyVendorItemQuantity.  # noqa: E501
        :rtype: int
        """
        return self._item_hash

    @item_hash.setter
    def item_hash(self, item_hash):
        """Sets the item_hash of this DestinyVendorItemQuantity.

        The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.  # noqa: E501

        :param item_hash: The item_hash of this DestinyVendorItemQuantity.  # noqa: E501
        :type: int
        """

        self._item_hash = item_hash

    @property
    def item_instance_id(self):
        """Gets the item_instance_id of this DestinyVendorItemQuantity.  # noqa: E501

        If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.  # noqa: E501

        :return: The item_instance_id of this DestinyVendorItemQuantity.  # noqa: E501
        :rtype: int
        """
        return self._item_instance_id

    @item_instance_id.setter
    def item_instance_id(self, item_instance_id):
        """Sets the item_instance_id of this DestinyVendorItemQuantity.

        If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.  # noqa: E501

        :param item_instance_id: The item_instance_id of this DestinyVendorItemQuantity.  # noqa: E501
        :type: int
        """

        self._item_instance_id = item_instance_id

    @property
    def quantity(self):
        """Gets the quantity of this DestinyVendorItemQuantity.  # noqa: E501

        The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used.  # noqa: E501

        :return: The quantity of this DestinyVendorItemQuantity.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this DestinyVendorItemQuantity.

        The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used.  # noqa: E501

        :param quantity: The quantity of this DestinyVendorItemQuantity.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if not isinstance(other, DestinyVendorItemQuantity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
