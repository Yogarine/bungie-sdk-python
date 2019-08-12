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


class InterpolationPoint(object):
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
        'value': 'int',
        'weight': 'int'
    }

    attribute_map = {
        'value': 'value',
        'weight': 'weight'
    }

    def __init__(self, value=None, weight=None):  # noqa: E501
        """InterpolationPoint - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._weight = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if weight is not None:
            self.weight = weight

    @property
    def value(self):
        """Gets the value of this InterpolationPoint.  # noqa: E501


        :return: The value of this InterpolationPoint.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InterpolationPoint.


        :param value: The value of this InterpolationPoint.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def weight(self):
        """Gets the weight of this InterpolationPoint.  # noqa: E501


        :return: The weight of this InterpolationPoint.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this InterpolationPoint.


        :param weight: The weight of this InterpolationPoint.  # noqa: E501
        :type: int
        """

        self._weight = weight

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
        if not isinstance(other, InterpolationPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
