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


class VendorItemStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    VENDOR_ITEM_STATUS__0 = "0"
    VENDOR_ITEM_STATUS__1 = "1"
    VENDOR_ITEM_STATUS__2 = "2"
    VENDOR_ITEM_STATUS__4 = "4"
    VENDOR_ITEM_STATUS__8 = "8"
    VENDOR_ITEM_STATUS__16 = "16"
    VENDOR_ITEM_STATUS__32 = "32"
    VENDOR_ITEM_STATUS__64 = "64"
    VENDOR_ITEM_STATUS__128 = "128"
    VENDOR_ITEM_STATUS__256 = "256"
    VENDOR_ITEM_STATUS__512 = "512"
    VENDOR_ITEM_STATUS__1024 = "1024"
    VENDOR_ITEM_STATUS__2048 = "2048"
    VENDOR_ITEM_STATUS__4096 = "4096"
    VENDOR_ITEM_STATUS__8192 = "8192"

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
        """VendorItemStatus - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, VendorItemStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
