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


class DestinyItemInvestmentStatDefinition(object):
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
        'stat_type_hash': 'int',
        'value': 'int',
        'is_conditionally_active': 'bool'
    }

    attribute_map = {
        'stat_type_hash': 'statTypeHash',
        'value': 'value',
        'is_conditionally_active': 'isConditionallyActive'
    }

    def __init__(self, stat_type_hash=None, value=None, is_conditionally_active=None):  # noqa: E501
        """DestinyItemInvestmentStatDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._stat_type_hash = None
        self._value = None
        self._is_conditionally_active = None
        self.discriminator = None

        if stat_type_hash is not None:
            self.stat_type_hash = stat_type_hash
        if value is not None:
            self.value = value
        if is_conditionally_active is not None:
            self.is_conditionally_active = is_conditionally_active

    @property
    def stat_type_hash(self):
        """Gets the stat_type_hash of this DestinyItemInvestmentStatDefinition.  # noqa: E501

        The hash identifier for the DestinyStatDefinition defining this stat.  # noqa: E501

        :return: The stat_type_hash of this DestinyItemInvestmentStatDefinition.  # noqa: E501
        :rtype: int
        """
        return self._stat_type_hash

    @stat_type_hash.setter
    def stat_type_hash(self, stat_type_hash):
        """Sets the stat_type_hash of this DestinyItemInvestmentStatDefinition.

        The hash identifier for the DestinyStatDefinition defining this stat.  # noqa: E501

        :param stat_type_hash: The stat_type_hash of this DestinyItemInvestmentStatDefinition.  # noqa: E501
        :type: int
        """

        self._stat_type_hash = stat_type_hash

    @property
    def value(self):
        """Gets the value of this DestinyItemInvestmentStatDefinition.  # noqa: E501

        The raw \"Investment\" value for the stat, before transformations are performed to turn this raw stat into stats that are displayed in the game UI.  # noqa: E501

        :return: The value of this DestinyItemInvestmentStatDefinition.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DestinyItemInvestmentStatDefinition.

        The raw \"Investment\" value for the stat, before transformations are performed to turn this raw stat into stats that are displayed in the game UI.  # noqa: E501

        :param value: The value of this DestinyItemInvestmentStatDefinition.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def is_conditionally_active(self):
        """Gets the is_conditionally_active of this DestinyItemInvestmentStatDefinition.  # noqa: E501

        If this is true, the stat will only be applied on the item in certain game state conditions, and we can't know statically whether or not this stat will be applied. Check the \"live\" API data instead for whether this value is being applied on a specific instance of the item in question, and you can use this to decide whether you want to show the stat on the generic view of the item, or whether you want to show some kind of caveat or warning about the stat value being conditional on game state.  # noqa: E501

        :return: The is_conditionally_active of this DestinyItemInvestmentStatDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_conditionally_active

    @is_conditionally_active.setter
    def is_conditionally_active(self, is_conditionally_active):
        """Sets the is_conditionally_active of this DestinyItemInvestmentStatDefinition.

        If this is true, the stat will only be applied on the item in certain game state conditions, and we can't know statically whether or not this stat will be applied. Check the \"live\" API data instead for whether this value is being applied on a specific instance of the item in question, and you can use this to decide whether you want to show the stat on the generic view of the item, or whether you want to show some kind of caveat or warning about the stat value being conditional on game state.  # noqa: E501

        :param is_conditionally_active: The is_conditionally_active of this DestinyItemInvestmentStatDefinition.  # noqa: E501
        :type: bool
        """

        self._is_conditionally_active = is_conditionally_active

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
        if not isinstance(other, DestinyItemInvestmentStatDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
