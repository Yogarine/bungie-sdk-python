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


class AwaInitializeResponse(object):
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
        'correlation_id': 'str',
        'sent_to_self': 'bool'
    }

    attribute_map = {
        'correlation_id': 'correlationId',
        'sent_to_self': 'sentToSelf'
    }

    def __init__(self, correlation_id=None, sent_to_self=None):  # noqa: E501
        """AwaInitializeResponse - a model defined in OpenAPI"""  # noqa: E501

        self._correlation_id = None
        self._sent_to_self = None
        self.discriminator = None

        if correlation_id is not None:
            self.correlation_id = correlation_id
        if sent_to_self is not None:
            self.sent_to_self = sent_to_self

    @property
    def correlation_id(self):
        """Gets the correlation_id of this AwaInitializeResponse.  # noqa: E501

        ID used to get the token. Present this ID to the user as it will identify this specific request on their device.  # noqa: E501

        :return: The correlation_id of this AwaInitializeResponse.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this AwaInitializeResponse.

        ID used to get the token. Present this ID to the user as it will identify this specific request on their device.  # noqa: E501

        :param correlation_id: The correlation_id of this AwaInitializeResponse.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def sent_to_self(self):
        """Gets the sent_to_self of this AwaInitializeResponse.  # noqa: E501

        True if the PUSH message will only be sent to the device that made this request.  # noqa: E501

        :return: The sent_to_self of this AwaInitializeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._sent_to_self

    @sent_to_self.setter
    def sent_to_self(self, sent_to_self):
        """Sets the sent_to_self of this AwaInitializeResponse.

        True if the PUSH message will only be sent to the device that made this request.  # noqa: E501

        :param sent_to_self: The sent_to_self of this AwaInitializeResponse.  # noqa: E501
        :type: bool
        """

        self._sent_to_self = sent_to_self

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
        if not isinstance(other, AwaInitializeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
