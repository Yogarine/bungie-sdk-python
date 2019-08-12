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


class GlobalAlert(object):
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
        'alert_key': 'str',
        'alert_html': 'str',
        'alert_timestamp': 'datetime',
        'alert_link': 'str',
        'alert_level': 'int',
        'alert_type': 'int',
        'stream_info': 'StreamInfo'
    }

    attribute_map = {
        'alert_key': 'AlertKey',
        'alert_html': 'AlertHtml',
        'alert_timestamp': 'AlertTimestamp',
        'alert_link': 'AlertLink',
        'alert_level': 'AlertLevel',
        'alert_type': 'AlertType',
        'stream_info': 'StreamInfo'
    }

    def __init__(self, alert_key=None, alert_html=None, alert_timestamp=None, alert_link=None, alert_level=None, alert_type=None, stream_info=None):  # noqa: E501
        """GlobalAlert - a model defined in OpenAPI"""  # noqa: E501

        self._alert_key = None
        self._alert_html = None
        self._alert_timestamp = None
        self._alert_link = None
        self._alert_level = None
        self._alert_type = None
        self._stream_info = None
        self.discriminator = None

        if alert_key is not None:
            self.alert_key = alert_key
        if alert_html is not None:
            self.alert_html = alert_html
        if alert_timestamp is not None:
            self.alert_timestamp = alert_timestamp
        if alert_link is not None:
            self.alert_link = alert_link
        if alert_level is not None:
            self.alert_level = alert_level
        if alert_type is not None:
            self.alert_type = alert_type
        if stream_info is not None:
            self.stream_info = stream_info

    @property
    def alert_key(self):
        """Gets the alert_key of this GlobalAlert.  # noqa: E501


        :return: The alert_key of this GlobalAlert.  # noqa: E501
        :rtype: str
        """
        return self._alert_key

    @alert_key.setter
    def alert_key(self, alert_key):
        """Sets the alert_key of this GlobalAlert.


        :param alert_key: The alert_key of this GlobalAlert.  # noqa: E501
        :type: str
        """

        self._alert_key = alert_key

    @property
    def alert_html(self):
        """Gets the alert_html of this GlobalAlert.  # noqa: E501


        :return: The alert_html of this GlobalAlert.  # noqa: E501
        :rtype: str
        """
        return self._alert_html

    @alert_html.setter
    def alert_html(self, alert_html):
        """Sets the alert_html of this GlobalAlert.


        :param alert_html: The alert_html of this GlobalAlert.  # noqa: E501
        :type: str
        """

        self._alert_html = alert_html

    @property
    def alert_timestamp(self):
        """Gets the alert_timestamp of this GlobalAlert.  # noqa: E501


        :return: The alert_timestamp of this GlobalAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._alert_timestamp

    @alert_timestamp.setter
    def alert_timestamp(self, alert_timestamp):
        """Sets the alert_timestamp of this GlobalAlert.


        :param alert_timestamp: The alert_timestamp of this GlobalAlert.  # noqa: E501
        :type: datetime
        """

        self._alert_timestamp = alert_timestamp

    @property
    def alert_link(self):
        """Gets the alert_link of this GlobalAlert.  # noqa: E501


        :return: The alert_link of this GlobalAlert.  # noqa: E501
        :rtype: str
        """
        return self._alert_link

    @alert_link.setter
    def alert_link(self, alert_link):
        """Sets the alert_link of this GlobalAlert.


        :param alert_link: The alert_link of this GlobalAlert.  # noqa: E501
        :type: str
        """

        self._alert_link = alert_link

    @property
    def alert_level(self):
        """Gets the alert_level of this GlobalAlert.  # noqa: E501


        :return: The alert_level of this GlobalAlert.  # noqa: E501
        :rtype: int
        """
        return self._alert_level

    @alert_level.setter
    def alert_level(self, alert_level):
        """Sets the alert_level of this GlobalAlert.


        :param alert_level: The alert_level of this GlobalAlert.  # noqa: E501
        :type: int
        """

        self._alert_level = alert_level

    @property
    def alert_type(self):
        """Gets the alert_type of this GlobalAlert.  # noqa: E501


        :return: The alert_type of this GlobalAlert.  # noqa: E501
        :rtype: int
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this GlobalAlert.


        :param alert_type: The alert_type of this GlobalAlert.  # noqa: E501
        :type: int
        """

        self._alert_type = alert_type

    @property
    def stream_info(self):
        """Gets the stream_info of this GlobalAlert.  # noqa: E501


        :return: The stream_info of this GlobalAlert.  # noqa: E501
        :rtype: StreamInfo
        """
        return self._stream_info

    @stream_info.setter
    def stream_info(self, stream_info):
        """Sets the stream_info of this GlobalAlert.


        :param stream_info: The stream_info of this GlobalAlert.  # noqa: E501
        :type: StreamInfo
        """

        self._stream_info = stream_info

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
        if not isinstance(other, GlobalAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other