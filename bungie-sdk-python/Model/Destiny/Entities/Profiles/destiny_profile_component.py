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


class DestinyProfileComponent(object):
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
        'user_info': 'UserInfoCard',
        'date_last_played': 'datetime',
        'versions_owned': 'int',
        'character_ids': 'list[int]'
    }

    attribute_map = {
        'user_info': 'userInfo',
        'date_last_played': 'dateLastPlayed',
        'versions_owned': 'versionsOwned',
        'character_ids': 'characterIds'
    }

    def __init__(self, user_info=None, date_last_played=None, versions_owned=None, character_ids=None):  # noqa: E501
        """DestinyProfileComponent - a model defined in OpenAPI"""  # noqa: E501

        self._user_info = None
        self._date_last_played = None
        self._versions_owned = None
        self._character_ids = None
        self.discriminator = None

        if user_info is not None:
            self.user_info = user_info
        if date_last_played is not None:
            self.date_last_played = date_last_played
        if versions_owned is not None:
            self.versions_owned = versions_owned
        if character_ids is not None:
            self.character_ids = character_ids

    @property
    def user_info(self):
        """Gets the user_info of this DestinyProfileComponent.  # noqa: E501

        If you need to render the Profile (their platform name, icon, etc...) somewhere, this property contains that information.  # noqa: E501

        :return: The user_info of this DestinyProfileComponent.  # noqa: E501
        :rtype: UserInfoCard
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this DestinyProfileComponent.

        If you need to render the Profile (their platform name, icon, etc...) somewhere, this property contains that information.  # noqa: E501

        :param user_info: The user_info of this DestinyProfileComponent.  # noqa: E501
        :type: UserInfoCard
        """

        self._user_info = user_info

    @property
    def date_last_played(self):
        """Gets the date_last_played of this DestinyProfileComponent.  # noqa: E501

        The last time the user played with any character on this Profile.  # noqa: E501

        :return: The date_last_played of this DestinyProfileComponent.  # noqa: E501
        :rtype: datetime
        """
        return self._date_last_played

    @date_last_played.setter
    def date_last_played(self, date_last_played):
        """Sets the date_last_played of this DestinyProfileComponent.

        The last time the user played with any character on this Profile.  # noqa: E501

        :param date_last_played: The date_last_played of this DestinyProfileComponent.  # noqa: E501
        :type: datetime
        """

        self._date_last_played = date_last_played

    @property
    def versions_owned(self):
        """Gets the versions_owned of this DestinyProfileComponent.  # noqa: E501

        If you want to know what expansions they own, this will contain that data.   IMPORTANT: This field may not return the data you're interested in for Cross-Saved users. It returns the last ownership data we saw for this account - which is to say, what they've purchased on the platform on which they last played, which now could be a different platform.   If you don't care about per-platform ownership and only care about whatever platform it seems they are playing on most recently, then this should be \"good enough.\" Otherwise, this should be considered deprecated. We do not have a good alternative to provide at this time with platform specific ownership data for DLC.  # noqa: E501

        :return: The versions_owned of this DestinyProfileComponent.  # noqa: E501
        :rtype: int
        """
        return self._versions_owned

    @versions_owned.setter
    def versions_owned(self, versions_owned):
        """Sets the versions_owned of this DestinyProfileComponent.

        If you want to know what expansions they own, this will contain that data.   IMPORTANT: This field may not return the data you're interested in for Cross-Saved users. It returns the last ownership data we saw for this account - which is to say, what they've purchased on the platform on which they last played, which now could be a different platform.   If you don't care about per-platform ownership and only care about whatever platform it seems they are playing on most recently, then this should be \"good enough.\" Otherwise, this should be considered deprecated. We do not have a good alternative to provide at this time with platform specific ownership data for DLC.  # noqa: E501

        :param versions_owned: The versions_owned of this DestinyProfileComponent.  # noqa: E501
        :type: int
        """

        self._versions_owned = versions_owned

    @property
    def character_ids(self):
        """Gets the character_ids of this DestinyProfileComponent.  # noqa: E501

        A list of the character IDs, for further querying on your part.  # noqa: E501

        :return: The character_ids of this DestinyProfileComponent.  # noqa: E501
        :rtype: list[int]
        """
        return self._character_ids

    @character_ids.setter
    def character_ids(self, character_ids):
        """Sets the character_ids of this DestinyProfileComponent.

        A list of the character IDs, for further querying on your part.  # noqa: E501

        :param character_ids: The character_ids of this DestinyProfileComponent.  # noqa: E501
        :type: list[int]
        """

        self._character_ids = character_ids

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
        if not isinstance(other, DestinyProfileComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
