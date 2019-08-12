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


class DestinyPlugRuleDefinition(object):
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
        'failure_message': 'str'
    }

    attribute_map = {
        'failure_message': 'failureMessage'
    }

    def __init__(self, failure_message=None):  # noqa: E501
        """DestinyPlugRuleDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._failure_message = None
        self.discriminator = None

        if failure_message is not None:
            self.failure_message = failure_message

    @property
    def failure_message(self):
        """Gets the failure_message of this DestinyPlugRuleDefinition.  # noqa: E501

        The localized string to show if this rule fails.  # noqa: E501

        :return: The failure_message of this DestinyPlugRuleDefinition.  # noqa: E501
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """Sets the failure_message of this DestinyPlugRuleDefinition.

        The localized string to show if this rule fails.  # noqa: E501

        :param failure_message: The failure_message of this DestinyPlugRuleDefinition.  # noqa: E501
        :type: str
        """

        self._failure_message = failure_message

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
        if not isinstance(other, DestinyPlugRuleDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other