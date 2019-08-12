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


class ClanBanner(object):
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
        'decal_id': 'int',
        'decal_color_id': 'int',
        'decal_background_color_id': 'int',
        'gonfalon_id': 'int',
        'gonfalon_color_id': 'int',
        'gonfalon_detail_id': 'int',
        'gonfalon_detail_color_id': 'int'
    }

    attribute_map = {
        'decal_id': 'decalId',
        'decal_color_id': 'decalColorId',
        'decal_background_color_id': 'decalBackgroundColorId',
        'gonfalon_id': 'gonfalonId',
        'gonfalon_color_id': 'gonfalonColorId',
        'gonfalon_detail_id': 'gonfalonDetailId',
        'gonfalon_detail_color_id': 'gonfalonDetailColorId'
    }

    def __init__(self, decal_id=None, decal_color_id=None, decal_background_color_id=None, gonfalon_id=None, gonfalon_color_id=None, gonfalon_detail_id=None, gonfalon_detail_color_id=None):  # noqa: E501
        """ClanBanner - a model defined in OpenAPI"""  # noqa: E501

        self._decal_id = None
        self._decal_color_id = None
        self._decal_background_color_id = None
        self._gonfalon_id = None
        self._gonfalon_color_id = None
        self._gonfalon_detail_id = None
        self._gonfalon_detail_color_id = None
        self.discriminator = None

        if decal_id is not None:
            self.decal_id = decal_id
        if decal_color_id is not None:
            self.decal_color_id = decal_color_id
        if decal_background_color_id is not None:
            self.decal_background_color_id = decal_background_color_id
        if gonfalon_id is not None:
            self.gonfalon_id = gonfalon_id
        if gonfalon_color_id is not None:
            self.gonfalon_color_id = gonfalon_color_id
        if gonfalon_detail_id is not None:
            self.gonfalon_detail_id = gonfalon_detail_id
        if gonfalon_detail_color_id is not None:
            self.gonfalon_detail_color_id = gonfalon_detail_color_id

    @property
    def decal_id(self):
        """Gets the decal_id of this ClanBanner.  # noqa: E501


        :return: The decal_id of this ClanBanner.  # noqa: E501
        :rtype: int
        """
        return self._decal_id

    @decal_id.setter
    def decal_id(self, decal_id):
        """Sets the decal_id of this ClanBanner.


        :param decal_id: The decal_id of this ClanBanner.  # noqa: E501
        :type: int
        """

        self._decal_id = decal_id

    @property
    def decal_color_id(self):
        """Gets the decal_color_id of this ClanBanner.  # noqa: E501


        :return: The decal_color_id of this ClanBanner.  # noqa: E501
        :rtype: int
        """
        return self._decal_color_id

    @decal_color_id.setter
    def decal_color_id(self, decal_color_id):
        """Sets the decal_color_id of this ClanBanner.


        :param decal_color_id: The decal_color_id of this ClanBanner.  # noqa: E501
        :type: int
        """

        self._decal_color_id = decal_color_id

    @property
    def decal_background_color_id(self):
        """Gets the decal_background_color_id of this ClanBanner.  # noqa: E501


        :return: The decal_background_color_id of this ClanBanner.  # noqa: E501
        :rtype: int
        """
        return self._decal_background_color_id

    @decal_background_color_id.setter
    def decal_background_color_id(self, decal_background_color_id):
        """Sets the decal_background_color_id of this ClanBanner.


        :param decal_background_color_id: The decal_background_color_id of this ClanBanner.  # noqa: E501
        :type: int
        """

        self._decal_background_color_id = decal_background_color_id

    @property
    def gonfalon_id(self):
        """Gets the gonfalon_id of this ClanBanner.  # noqa: E501


        :return: The gonfalon_id of this ClanBanner.  # noqa: E501
        :rtype: int
        """
        return self._gonfalon_id

    @gonfalon_id.setter
    def gonfalon_id(self, gonfalon_id):
        """Sets the gonfalon_id of this ClanBanner.


        :param gonfalon_id: The gonfalon_id of this ClanBanner.  # noqa: E501
        :type: int
        """

        self._gonfalon_id = gonfalon_id

    @property
    def gonfalon_color_id(self):
        """Gets the gonfalon_color_id of this ClanBanner.  # noqa: E501


        :return: The gonfalon_color_id of this ClanBanner.  # noqa: E501
        :rtype: int
        """
        return self._gonfalon_color_id

    @gonfalon_color_id.setter
    def gonfalon_color_id(self, gonfalon_color_id):
        """Sets the gonfalon_color_id of this ClanBanner.


        :param gonfalon_color_id: The gonfalon_color_id of this ClanBanner.  # noqa: E501
        :type: int
        """

        self._gonfalon_color_id = gonfalon_color_id

    @property
    def gonfalon_detail_id(self):
        """Gets the gonfalon_detail_id of this ClanBanner.  # noqa: E501


        :return: The gonfalon_detail_id of this ClanBanner.  # noqa: E501
        :rtype: int
        """
        return self._gonfalon_detail_id

    @gonfalon_detail_id.setter
    def gonfalon_detail_id(self, gonfalon_detail_id):
        """Sets the gonfalon_detail_id of this ClanBanner.


        :param gonfalon_detail_id: The gonfalon_detail_id of this ClanBanner.  # noqa: E501
        :type: int
        """

        self._gonfalon_detail_id = gonfalon_detail_id

    @property
    def gonfalon_detail_color_id(self):
        """Gets the gonfalon_detail_color_id of this ClanBanner.  # noqa: E501


        :return: The gonfalon_detail_color_id of this ClanBanner.  # noqa: E501
        :rtype: int
        """
        return self._gonfalon_detail_color_id

    @gonfalon_detail_color_id.setter
    def gonfalon_detail_color_id(self, gonfalon_detail_color_id):
        """Sets the gonfalon_detail_color_id of this ClanBanner.


        :param gonfalon_detail_color_id: The gonfalon_detail_color_id of this ClanBanner.  # noqa: E501
        :type: int
        """

        self._gonfalon_detail_color_id = gonfalon_detail_color_id

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
        if not isinstance(other, ClanBanner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
