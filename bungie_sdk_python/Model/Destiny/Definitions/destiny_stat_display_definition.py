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


class DestinyStatDisplayDefinition(object):
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
        'stat_hash': 'int',
        'maximum_value': 'int',
        'display_as_numeric': 'bool',
        'display_interpolation': 'list[InterpolationPoint]'
    }

    attribute_map = {
        'stat_hash': 'statHash',
        'maximum_value': 'maximumValue',
        'display_as_numeric': 'displayAsNumeric',
        'display_interpolation': 'displayInterpolation'
    }

    def __init__(self, stat_hash=None, maximum_value=None, display_as_numeric=None, display_interpolation=None):  # noqa: E501
        """DestinyStatDisplayDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._stat_hash = None
        self._maximum_value = None
        self._display_as_numeric = None
        self._display_interpolation = None
        self.discriminator = None

        if stat_hash is not None:
            self.stat_hash = stat_hash
        if maximum_value is not None:
            self.maximum_value = maximum_value
        if display_as_numeric is not None:
            self.display_as_numeric = display_as_numeric
        if display_interpolation is not None:
            self.display_interpolation = display_interpolation

    @property
    def stat_hash(self):
        """Gets the stat_hash of this DestinyStatDisplayDefinition.  # noqa: E501

        The hash identifier for the stat being transformed into a Display stat.  Use it to look up the DestinyStatDefinition, or key into a DestinyInventoryItemDefinition's stats property.  # noqa: E501

        :return: The stat_hash of this DestinyStatDisplayDefinition.  # noqa: E501
        :rtype: int
        """
        return self._stat_hash

    @stat_hash.setter
    def stat_hash(self, stat_hash):
        """Sets the stat_hash of this DestinyStatDisplayDefinition.

        The hash identifier for the stat being transformed into a Display stat.  Use it to look up the DestinyStatDefinition, or key into a DestinyInventoryItemDefinition's stats property.  # noqa: E501

        :param stat_hash: The stat_hash of this DestinyStatDisplayDefinition.  # noqa: E501
        :type: int
        """

        self._stat_hash = stat_hash

    @property
    def maximum_value(self):
        """Gets the maximum_value of this DestinyStatDisplayDefinition.  # noqa: E501

        Regardless of the output of interpolation, this is the maximum possible value that the stat can be. It should also be used as the upper bound for displaying the stat as a progress bar (the minimum always being 0)  # noqa: E501

        :return: The maximum_value of this DestinyStatDisplayDefinition.  # noqa: E501
        :rtype: int
        """
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, maximum_value):
        """Sets the maximum_value of this DestinyStatDisplayDefinition.

        Regardless of the output of interpolation, this is the maximum possible value that the stat can be. It should also be used as the upper bound for displaying the stat as a progress bar (the minimum always being 0)  # noqa: E501

        :param maximum_value: The maximum_value of this DestinyStatDisplayDefinition.  # noqa: E501
        :type: int
        """

        self._maximum_value = maximum_value

    @property
    def display_as_numeric(self):
        """Gets the display_as_numeric of this DestinyStatDisplayDefinition.  # noqa: E501

        If this is true, the stat should be displayed as a number. Otherwise, display it as a progress bar. Or, you know, do whatever you want. There's no displayAsNumeric police.  # noqa: E501

        :return: The display_as_numeric of this DestinyStatDisplayDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._display_as_numeric

    @display_as_numeric.setter
    def display_as_numeric(self, display_as_numeric):
        """Sets the display_as_numeric of this DestinyStatDisplayDefinition.

        If this is true, the stat should be displayed as a number. Otherwise, display it as a progress bar. Or, you know, do whatever you want. There's no displayAsNumeric police.  # noqa: E501

        :param display_as_numeric: The display_as_numeric of this DestinyStatDisplayDefinition.  # noqa: E501
        :type: bool
        """

        self._display_as_numeric = display_as_numeric

    @property
    def display_interpolation(self):
        """Gets the display_interpolation of this DestinyStatDisplayDefinition.  # noqa: E501

        The interpolation table representing how the Investment Stat is transformed into a Display Stat.   See DestinyStatDefinition for a description of the stages of stat transformation.  # noqa: E501

        :return: The display_interpolation of this DestinyStatDisplayDefinition.  # noqa: E501
        :rtype: list[InterpolationPoint]
        """
        return self._display_interpolation

    @display_interpolation.setter
    def display_interpolation(self, display_interpolation):
        """Sets the display_interpolation of this DestinyStatDisplayDefinition.

        The interpolation table representing how the Investment Stat is transformed into a Display Stat.   See DestinyStatDefinition for a description of the stages of stat transformation.  # noqa: E501

        :param display_interpolation: The display_interpolation of this DestinyStatDisplayDefinition.  # noqa: E501
        :type: list[InterpolationPoint]
        """

        self._display_interpolation = display_interpolation

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
        if not isinstance(other, DestinyStatDisplayDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
