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


class InlineResponse20025(object):
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
        'response': 'SearchResultOfGroupBan',
        'error_code': 'int',
        'throttle_seconds': 'int',
        'error_status': 'str',
        'message': 'str',
        'message_data': 'dict(str, str)',
        'detailed_error_trace': 'str'
    }

    attribute_map = {
        'response': 'Response',
        'error_code': 'ErrorCode',
        'throttle_seconds': 'ThrottleSeconds',
        'error_status': 'ErrorStatus',
        'message': 'Message',
        'message_data': 'MessageData',
        'detailed_error_trace': 'DetailedErrorTrace'
    }

    def __init__(self, response=None, error_code=None, throttle_seconds=None, error_status=None, message=None, message_data=None, detailed_error_trace=None):  # noqa: E501
        """InlineResponse20025 - a model defined in OpenAPI"""  # noqa: E501

        self._response = None
        self._error_code = None
        self._throttle_seconds = None
        self._error_status = None
        self._message = None
        self._message_data = None
        self._detailed_error_trace = None
        self.discriminator = None

        if response is not None:
            self.response = response
        if error_code is not None:
            self.error_code = error_code
        if throttle_seconds is not None:
            self.throttle_seconds = throttle_seconds
        if error_status is not None:
            self.error_status = error_status
        if message is not None:
            self.message = message
        if message_data is not None:
            self.message_data = message_data
        if detailed_error_trace is not None:
            self.detailed_error_trace = detailed_error_trace

    @property
    def response(self):
        """Gets the response of this InlineResponse20025.  # noqa: E501


        :return: The response of this InlineResponse20025.  # noqa: E501
        :rtype: SearchResultOfGroupBan
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this InlineResponse20025.


        :param response: The response of this InlineResponse20025.  # noqa: E501
        :type: SearchResultOfGroupBan
        """

        self._response = response

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse20025.  # noqa: E501


        :return: The error_code of this InlineResponse20025.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse20025.


        :param error_code: The error_code of this InlineResponse20025.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def throttle_seconds(self):
        """Gets the throttle_seconds of this InlineResponse20025.  # noqa: E501


        :return: The throttle_seconds of this InlineResponse20025.  # noqa: E501
        :rtype: int
        """
        return self._throttle_seconds

    @throttle_seconds.setter
    def throttle_seconds(self, throttle_seconds):
        """Sets the throttle_seconds of this InlineResponse20025.


        :param throttle_seconds: The throttle_seconds of this InlineResponse20025.  # noqa: E501
        :type: int
        """

        self._throttle_seconds = throttle_seconds

    @property
    def error_status(self):
        """Gets the error_status of this InlineResponse20025.  # noqa: E501


        :return: The error_status of this InlineResponse20025.  # noqa: E501
        :rtype: str
        """
        return self._error_status

    @error_status.setter
    def error_status(self, error_status):
        """Sets the error_status of this InlineResponse20025.


        :param error_status: The error_status of this InlineResponse20025.  # noqa: E501
        :type: str
        """

        self._error_status = error_status

    @property
    def message(self):
        """Gets the message of this InlineResponse20025.  # noqa: E501


        :return: The message of this InlineResponse20025.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse20025.


        :param message: The message of this InlineResponse20025.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def message_data(self):
        """Gets the message_data of this InlineResponse20025.  # noqa: E501


        :return: The message_data of this InlineResponse20025.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._message_data

    @message_data.setter
    def message_data(self, message_data):
        """Sets the message_data of this InlineResponse20025.


        :param message_data: The message_data of this InlineResponse20025.  # noqa: E501
        :type: dict(str, str)
        """

        self._message_data = message_data

    @property
    def detailed_error_trace(self):
        """Gets the detailed_error_trace of this InlineResponse20025.  # noqa: E501


        :return: The detailed_error_trace of this InlineResponse20025.  # noqa: E501
        :rtype: str
        """
        return self._detailed_error_trace

    @detailed_error_trace.setter
    def detailed_error_trace(self, detailed_error_trace):
        """Sets the detailed_error_trace of this InlineResponse20025.


        :param detailed_error_trace: The detailed_error_trace of this InlineResponse20025.  # noqa: E501
        :type: str
        """

        self._detailed_error_trace = detailed_error_trace

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
        if not isinstance(other, InlineResponse20025):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
