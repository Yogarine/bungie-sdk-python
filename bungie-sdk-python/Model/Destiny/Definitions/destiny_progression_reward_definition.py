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


class DestinyProgressionRewardDefinition(object):
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
        'progression_mapping_hash': 'int',
        'amount': 'int',
        'apply_throttles': 'bool'
    }

    attribute_map = {
        'progression_mapping_hash': 'progressionMappingHash',
        'amount': 'amount',
        'apply_throttles': 'applyThrottles'
    }

    def __init__(self, progression_mapping_hash=None, amount=None, apply_throttles=None):  # noqa: E501
        """DestinyProgressionRewardDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._progression_mapping_hash = None
        self._amount = None
        self._apply_throttles = None
        self.discriminator = None

        if progression_mapping_hash is not None:
            self.progression_mapping_hash = progression_mapping_hash
        if amount is not None:
            self.amount = amount
        if apply_throttles is not None:
            self.apply_throttles = apply_throttles

    @property
    def progression_mapping_hash(self):
        """Gets the progression_mapping_hash of this DestinyProgressionRewardDefinition.  # noqa: E501

        The hash identifier of the DestinyProgressionMappingDefinition that contains the progressions for which experience should be applied.  # noqa: E501

        :return: The progression_mapping_hash of this DestinyProgressionRewardDefinition.  # noqa: E501
        :rtype: int
        """
        return self._progression_mapping_hash

    @progression_mapping_hash.setter
    def progression_mapping_hash(self, progression_mapping_hash):
        """Sets the progression_mapping_hash of this DestinyProgressionRewardDefinition.

        The hash identifier of the DestinyProgressionMappingDefinition that contains the progressions for which experience should be applied.  # noqa: E501

        :param progression_mapping_hash: The progression_mapping_hash of this DestinyProgressionRewardDefinition.  # noqa: E501
        :type: int
        """

        self._progression_mapping_hash = progression_mapping_hash

    @property
    def amount(self):
        """Gets the amount of this DestinyProgressionRewardDefinition.  # noqa: E501

        The amount of experience to give to each of the mapped progressions.  # noqa: E501

        :return: The amount of this DestinyProgressionRewardDefinition.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DestinyProgressionRewardDefinition.

        The amount of experience to give to each of the mapped progressions.  # noqa: E501

        :param amount: The amount of this DestinyProgressionRewardDefinition.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def apply_throttles(self):
        """Gets the apply_throttles of this DestinyProgressionRewardDefinition.  # noqa: E501

        If true, the game's internal mechanisms to throttle progression should be applied.  # noqa: E501

        :return: The apply_throttles of this DestinyProgressionRewardDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._apply_throttles

    @apply_throttles.setter
    def apply_throttles(self, apply_throttles):
        """Sets the apply_throttles of this DestinyProgressionRewardDefinition.

        If true, the game's internal mechanisms to throttle progression should be applied.  # noqa: E501

        :param apply_throttles: The apply_throttles of this DestinyProgressionRewardDefinition.  # noqa: E501
        :type: bool
        """

        self._apply_throttles = apply_throttles

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
        if not isinstance(other, DestinyProgressionRewardDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
