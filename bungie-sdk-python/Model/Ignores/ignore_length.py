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


class IgnoreLength(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    IGNORE_LENGTH__0 = "0"
    IGNORE_LENGTH__1 = "1"
    IGNORE_LENGTH__2 = "2"
    IGNORE_LENGTH__3 = "3"
    IGNORE_LENGTH__4 = "4"
    IGNORE_LENGTH__5 = "5"
    IGNORE_LENGTH__6 = "6"
    IGNORE_LENGTH__7 = "7"
    IGNORE_LENGTH__8 = "8"
    IGNORE_LENGTH__9 = "9"
    IGNORE_LENGTH__10 = "10"
    IGNORE_LENGTH__11 = "11"

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """IgnoreLength - a model defined in OpenAPI"""  # noqa: E501
        self.discriminator = None

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
        if not isinstance(other, IgnoreLength):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
