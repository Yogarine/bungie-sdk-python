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


class DestinyReportReasonDefinition(object):
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
        'reason_hash': 'int',
        'display_properties': 'DestinyDisplayPropertiesDefinition'
    }

    attribute_map = {
        'reason_hash': 'reasonHash',
        'display_properties': 'displayProperties'
    }

    def __init__(self, reason_hash=None, display_properties=None):  # noqa: E501
        """DestinyReportReasonDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._reason_hash = None
        self._display_properties = None
        self.discriminator = None

        if reason_hash is not None:
            self.reason_hash = reason_hash
        if display_properties is not None:
            self.display_properties = display_properties

    @property
    def reason_hash(self):
        """Gets the reason_hash of this DestinyReportReasonDefinition.  # noqa: E501

        The identifier for the reason: they are only guaranteed unique under the Category in which they are found.  # noqa: E501

        :return: The reason_hash of this DestinyReportReasonDefinition.  # noqa: E501
        :rtype: int
        """
        return self._reason_hash

    @reason_hash.setter
    def reason_hash(self, reason_hash):
        """Sets the reason_hash of this DestinyReportReasonDefinition.

        The identifier for the reason: they are only guaranteed unique under the Category in which they are found.  # noqa: E501

        :param reason_hash: The reason_hash of this DestinyReportReasonDefinition.  # noqa: E501
        :type: int
        """

        self._reason_hash = reason_hash

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyReportReasonDefinition.  # noqa: E501


        :return: The display_properties of this DestinyReportReasonDefinition.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyReportReasonDefinition.


        :param display_properties: The display_properties of this DestinyReportReasonDefinition.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

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
        if not isinstance(other, DestinyReportReasonDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
