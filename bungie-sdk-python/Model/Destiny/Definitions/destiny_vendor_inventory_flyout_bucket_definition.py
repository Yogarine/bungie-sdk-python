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


class DestinyVendorInventoryFlyoutBucketDefinition(object):
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
        'collapsible': 'bool',
        'inventory_bucket_hash': 'int',
        'sort_items_by': 'int'
    }

    attribute_map = {
        'collapsible': 'collapsible',
        'inventory_bucket_hash': 'inventoryBucketHash',
        'sort_items_by': 'sortItemsBy'
    }

    def __init__(self, collapsible=None, inventory_bucket_hash=None, sort_items_by=None):  # noqa: E501
        """DestinyVendorInventoryFlyoutBucketDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._collapsible = None
        self._inventory_bucket_hash = None
        self._sort_items_by = None
        self.discriminator = None

        if collapsible is not None:
            self.collapsible = collapsible
        if inventory_bucket_hash is not None:
            self.inventory_bucket_hash = inventory_bucket_hash
        if sort_items_by is not None:
            self.sort_items_by = sort_items_by

    @property
    def collapsible(self):
        """Gets the collapsible of this DestinyVendorInventoryFlyoutBucketDefinition.  # noqa: E501

        If true, the inventory bucket should be able to be collapsed visually.  # noqa: E501

        :return: The collapsible of this DestinyVendorInventoryFlyoutBucketDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._collapsible

    @collapsible.setter
    def collapsible(self, collapsible):
        """Sets the collapsible of this DestinyVendorInventoryFlyoutBucketDefinition.

        If true, the inventory bucket should be able to be collapsed visually.  # noqa: E501

        :param collapsible: The collapsible of this DestinyVendorInventoryFlyoutBucketDefinition.  # noqa: E501
        :type: bool
        """

        self._collapsible = collapsible

    @property
    def inventory_bucket_hash(self):
        """Gets the inventory_bucket_hash of this DestinyVendorInventoryFlyoutBucketDefinition.  # noqa: E501

        The inventory bucket whose contents should be shown.  # noqa: E501

        :return: The inventory_bucket_hash of this DestinyVendorInventoryFlyoutBucketDefinition.  # noqa: E501
        :rtype: int
        """
        return self._inventory_bucket_hash

    @inventory_bucket_hash.setter
    def inventory_bucket_hash(self, inventory_bucket_hash):
        """Sets the inventory_bucket_hash of this DestinyVendorInventoryFlyoutBucketDefinition.

        The inventory bucket whose contents should be shown.  # noqa: E501

        :param inventory_bucket_hash: The inventory_bucket_hash of this DestinyVendorInventoryFlyoutBucketDefinition.  # noqa: E501
        :type: int
        """

        self._inventory_bucket_hash = inventory_bucket_hash

    @property
    def sort_items_by(self):
        """Gets the sort_items_by of this DestinyVendorInventoryFlyoutBucketDefinition.  # noqa: E501

        The methodology to use for sorting items from the flyout.  # noqa: E501

        :return: The sort_items_by of this DestinyVendorInventoryFlyoutBucketDefinition.  # noqa: E501
        :rtype: int
        """
        return self._sort_items_by

    @sort_items_by.setter
    def sort_items_by(self, sort_items_by):
        """Sets the sort_items_by of this DestinyVendorInventoryFlyoutBucketDefinition.

        The methodology to use for sorting items from the flyout.  # noqa: E501

        :param sort_items_by: The sort_items_by of this DestinyVendorInventoryFlyoutBucketDefinition.  # noqa: E501
        :type: int
        """

        self._sort_items_by = sort_items_by

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
        if not isinstance(other, DestinyVendorInventoryFlyoutBucketDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other