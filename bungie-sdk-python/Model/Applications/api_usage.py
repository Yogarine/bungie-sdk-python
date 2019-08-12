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


class ApiUsage(object):
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
        'range': 'DateRange',
        'api_calls': 'list[Series]',
        'throttled_requests': 'list[Series]'
    }

    attribute_map = {
        'range': 'range',
        'api_calls': 'apiCalls',
        'throttled_requests': 'throttledRequests'
    }

    def __init__(self, range=None, api_calls=None, throttled_requests=None):  # noqa: E501
        """ApiUsage - a model defined in OpenAPI"""  # noqa: E501

        self._range = None
        self._api_calls = None
        self._throttled_requests = None
        self.discriminator = None

        if range is not None:
            self.range = range
        if api_calls is not None:
            self.api_calls = api_calls
        if throttled_requests is not None:
            self.throttled_requests = throttled_requests

    @property
    def range(self):
        """Gets the range of this ApiUsage.  # noqa: E501

        The date range for the data being reported.  # noqa: E501

        :return: The range of this ApiUsage.  # noqa: E501
        :rtype: DateRange
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this ApiUsage.

        The date range for the data being reported.  # noqa: E501

        :param range: The range of this ApiUsage.  # noqa: E501
        :type: DateRange
        """

        self._range = range

    @property
    def api_calls(self):
        """Gets the api_calls of this ApiUsage.  # noqa: E501

        Counts for on API calls made for the time range.  # noqa: E501

        :return: The api_calls of this ApiUsage.  # noqa: E501
        :rtype: list[Series]
        """
        return self._api_calls

    @api_calls.setter
    def api_calls(self, api_calls):
        """Sets the api_calls of this ApiUsage.

        Counts for on API calls made for the time range.  # noqa: E501

        :param api_calls: The api_calls of this ApiUsage.  # noqa: E501
        :type: list[Series]
        """

        self._api_calls = api_calls

    @property
    def throttled_requests(self):
        """Gets the throttled_requests of this ApiUsage.  # noqa: E501

        Instances of blocked requests or requests that crossed the warn threshold during the time range.  # noqa: E501

        :return: The throttled_requests of this ApiUsage.  # noqa: E501
        :rtype: list[Series]
        """
        return self._throttled_requests

    @throttled_requests.setter
    def throttled_requests(self, throttled_requests):
        """Sets the throttled_requests of this ApiUsage.

        Instances of blocked requests or requests that crossed the warn threshold during the time range.  # noqa: E501

        :param throttled_requests: The throttled_requests of this ApiUsage.  # noqa: E501
        :type: list[Series]
        """

        self._throttled_requests = throttled_requests

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
        if not isinstance(other, ApiUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other