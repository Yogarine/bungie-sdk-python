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


class DestinyVendorSaleItemActionBlockDefinition(object):
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
        'execute_seconds': 'float',
        'is_positive': 'bool'
    }

    attribute_map = {
        'execute_seconds': 'executeSeconds',
        'is_positive': 'isPositive'
    }

    def __init__(self, execute_seconds=None, is_positive=None):  # noqa: E501
        """DestinyVendorSaleItemActionBlockDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._execute_seconds = None
        self._is_positive = None
        self.discriminator = None

        if execute_seconds is not None:
            self.execute_seconds = execute_seconds
        if is_positive is not None:
            self.is_positive = is_positive

    @property
    def execute_seconds(self):
        """Gets the execute_seconds of this DestinyVendorSaleItemActionBlockDefinition.  # noqa: E501


        :return: The execute_seconds of this DestinyVendorSaleItemActionBlockDefinition.  # noqa: E501
        :rtype: float
        """
        return self._execute_seconds

    @execute_seconds.setter
    def execute_seconds(self, execute_seconds):
        """Sets the execute_seconds of this DestinyVendorSaleItemActionBlockDefinition.


        :param execute_seconds: The execute_seconds of this DestinyVendorSaleItemActionBlockDefinition.  # noqa: E501
        :type: float
        """

        self._execute_seconds = execute_seconds

    @property
    def is_positive(self):
        """Gets the is_positive of this DestinyVendorSaleItemActionBlockDefinition.  # noqa: E501


        :return: The is_positive of this DestinyVendorSaleItemActionBlockDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_positive

    @is_positive.setter
    def is_positive(self, is_positive):
        """Sets the is_positive of this DestinyVendorSaleItemActionBlockDefinition.


        :param is_positive: The is_positive of this DestinyVendorSaleItemActionBlockDefinition.  # noqa: E501
        :type: bool
        """

        self._is_positive = is_positive

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
        if not isinstance(other, DestinyVendorSaleItemActionBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
