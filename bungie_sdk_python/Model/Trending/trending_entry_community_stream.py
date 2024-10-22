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


class TrendingEntryCommunityStream(object):
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
        'image': 'str',
        'title': 'str',
        'partnership_identifier': 'str',
        'partnership_type': 'int'
    }

    attribute_map = {
        'image': 'image',
        'title': 'title',
        'partnership_identifier': 'partnershipIdentifier',
        'partnership_type': 'partnershipType'
    }

    def __init__(self, image=None, title=None, partnership_identifier=None, partnership_type=None):  # noqa: E501
        """TrendingEntryCommunityStream - a model defined in OpenAPI"""  # noqa: E501

        self._image = None
        self._title = None
        self._partnership_identifier = None
        self._partnership_type = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if title is not None:
            self.title = title
        if partnership_identifier is not None:
            self.partnership_identifier = partnership_identifier
        if partnership_type is not None:
            self.partnership_type = partnership_type

    @property
    def image(self):
        """Gets the image of this TrendingEntryCommunityStream.  # noqa: E501


        :return: The image of this TrendingEntryCommunityStream.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this TrendingEntryCommunityStream.


        :param image: The image of this TrendingEntryCommunityStream.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def title(self):
        """Gets the title of this TrendingEntryCommunityStream.  # noqa: E501


        :return: The title of this TrendingEntryCommunityStream.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TrendingEntryCommunityStream.


        :param title: The title of this TrendingEntryCommunityStream.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def partnership_identifier(self):
        """Gets the partnership_identifier of this TrendingEntryCommunityStream.  # noqa: E501


        :return: The partnership_identifier of this TrendingEntryCommunityStream.  # noqa: E501
        :rtype: str
        """
        return self._partnership_identifier

    @partnership_identifier.setter
    def partnership_identifier(self, partnership_identifier):
        """Sets the partnership_identifier of this TrendingEntryCommunityStream.


        :param partnership_identifier: The partnership_identifier of this TrendingEntryCommunityStream.  # noqa: E501
        :type: str
        """

        self._partnership_identifier = partnership_identifier

    @property
    def partnership_type(self):
        """Gets the partnership_type of this TrendingEntryCommunityStream.  # noqa: E501


        :return: The partnership_type of this TrendingEntryCommunityStream.  # noqa: E501
        :rtype: int
        """
        return self._partnership_type

    @partnership_type.setter
    def partnership_type(self, partnership_type):
        """Sets the partnership_type of this TrendingEntryCommunityStream.


        :param partnership_type: The partnership_type of this TrendingEntryCommunityStream.  # noqa: E501
        :type: int
        """

        self._partnership_type = partnership_type

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
        if not isinstance(other, TrendingEntryCommunityStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
