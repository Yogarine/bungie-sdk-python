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


class DestinyKioskItem(object):
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
        'index': 'int',
        'can_acquire': 'bool',
        'failure_indexes': 'list[int]',
        'flavor_objective': 'DestinyObjectiveProgress'
    }

    attribute_map = {
        'index': 'index',
        'can_acquire': 'canAcquire',
        'failure_indexes': 'failureIndexes',
        'flavor_objective': 'flavorObjective'
    }

    def __init__(self, index=None, can_acquire=None, failure_indexes=None, flavor_objective=None):  # noqa: E501
        """DestinyKioskItem - a model defined in OpenAPI"""  # noqa: E501

        self._index = None
        self._can_acquire = None
        self._failure_indexes = None
        self._flavor_objective = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if can_acquire is not None:
            self.can_acquire = can_acquire
        if failure_indexes is not None:
            self.failure_indexes = failure_indexes
        if flavor_objective is not None:
            self.flavor_objective = flavor_objective

    @property
    def index(self):
        """Gets the index of this DestinyKioskItem.  # noqa: E501

        The index of the item in the related DestinyVendorDefintion's itemList property, representing the sale.  # noqa: E501

        :return: The index of this DestinyKioskItem.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyKioskItem.

        The index of the item in the related DestinyVendorDefintion's itemList property, representing the sale.  # noqa: E501

        :param index: The index of this DestinyKioskItem.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def can_acquire(self):
        """Gets the can_acquire of this DestinyKioskItem.  # noqa: E501

        If true, the user can not only see the item, but they can acquire it. It is possible that a user can see a kiosk item and not be able to acquire it.  # noqa: E501

        :return: The can_acquire of this DestinyKioskItem.  # noqa: E501
        :rtype: bool
        """
        return self._can_acquire

    @can_acquire.setter
    def can_acquire(self, can_acquire):
        """Sets the can_acquire of this DestinyKioskItem.

        If true, the user can not only see the item, but they can acquire it. It is possible that a user can see a kiosk item and not be able to acquire it.  # noqa: E501

        :param can_acquire: The can_acquire of this DestinyKioskItem.  # noqa: E501
        :type: bool
        """

        self._can_acquire = can_acquire

    @property
    def failure_indexes(self):
        """Gets the failure_indexes of this DestinyKioskItem.  # noqa: E501

        Indexes into failureStrings for the Vendor, indicating the reasons why it failed if any.  # noqa: E501

        :return: The failure_indexes of this DestinyKioskItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._failure_indexes

    @failure_indexes.setter
    def failure_indexes(self, failure_indexes):
        """Sets the failure_indexes of this DestinyKioskItem.

        Indexes into failureStrings for the Vendor, indicating the reasons why it failed if any.  # noqa: E501

        :param failure_indexes: The failure_indexes of this DestinyKioskItem.  # noqa: E501
        :type: list[int]
        """

        self._failure_indexes = failure_indexes

    @property
    def flavor_objective(self):
        """Gets the flavor_objective of this DestinyKioskItem.  # noqa: E501

        I may regret naming it this way - but this represents when an item has an objective that doesn't serve a beneficial purpose, but rather is used for \"flavor\" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item.  # noqa: E501

        :return: The flavor_objective of this DestinyKioskItem.  # noqa: E501
        :rtype: DestinyObjectiveProgress
        """
        return self._flavor_objective

    @flavor_objective.setter
    def flavor_objective(self, flavor_objective):
        """Sets the flavor_objective of this DestinyKioskItem.

        I may regret naming it this way - but this represents when an item has an objective that doesn't serve a beneficial purpose, but rather is used for \"flavor\" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item.  # noqa: E501

        :param flavor_objective: The flavor_objective of this DestinyKioskItem.  # noqa: E501
        :type: DestinyObjectiveProgress
        """

        self._flavor_objective = flavor_objective

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
        if not isinstance(other, DestinyKioskItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other