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


class FireteamMember(object):
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
        'destiny_user_info': 'UserInfoCard',
        'bungie_net_user_info': 'UserInfoCard',
        'character_id': 'int',
        'date_joined': 'datetime',
        'has_microphone': 'bool',
        'last_platform_invite_attempt_date': 'datetime',
        'last_platform_invite_attempt_result': 'int'
    }

    attribute_map = {
        'destiny_user_info': 'destinyUserInfo',
        'bungie_net_user_info': 'bungieNetUserInfo',
        'character_id': 'characterId',
        'date_joined': 'dateJoined',
        'has_microphone': 'hasMicrophone',
        'last_platform_invite_attempt_date': 'lastPlatformInviteAttemptDate',
        'last_platform_invite_attempt_result': 'lastPlatformInviteAttemptResult'
    }

    def __init__(self, destiny_user_info=None, bungie_net_user_info=None, character_id=None, date_joined=None, has_microphone=None, last_platform_invite_attempt_date=None, last_platform_invite_attempt_result=None):  # noqa: E501
        """FireteamMember - a model defined in OpenAPI"""  # noqa: E501

        self._destiny_user_info = None
        self._bungie_net_user_info = None
        self._character_id = None
        self._date_joined = None
        self._has_microphone = None
        self._last_platform_invite_attempt_date = None
        self._last_platform_invite_attempt_result = None
        self.discriminator = None

        if destiny_user_info is not None:
            self.destiny_user_info = destiny_user_info
        if bungie_net_user_info is not None:
            self.bungie_net_user_info = bungie_net_user_info
        if character_id is not None:
            self.character_id = character_id
        if date_joined is not None:
            self.date_joined = date_joined
        if has_microphone is not None:
            self.has_microphone = has_microphone
        if last_platform_invite_attempt_date is not None:
            self.last_platform_invite_attempt_date = last_platform_invite_attempt_date
        if last_platform_invite_attempt_result is not None:
            self.last_platform_invite_attempt_result = last_platform_invite_attempt_result

    @property
    def destiny_user_info(self):
        """Gets the destiny_user_info of this FireteamMember.  # noqa: E501


        :return: The destiny_user_info of this FireteamMember.  # noqa: E501
        :rtype: UserInfoCard
        """
        return self._destiny_user_info

    @destiny_user_info.setter
    def destiny_user_info(self, destiny_user_info):
        """Sets the destiny_user_info of this FireteamMember.


        :param destiny_user_info: The destiny_user_info of this FireteamMember.  # noqa: E501
        :type: UserInfoCard
        """

        self._destiny_user_info = destiny_user_info

    @property
    def bungie_net_user_info(self):
        """Gets the bungie_net_user_info of this FireteamMember.  # noqa: E501


        :return: The bungie_net_user_info of this FireteamMember.  # noqa: E501
        :rtype: UserInfoCard
        """
        return self._bungie_net_user_info

    @bungie_net_user_info.setter
    def bungie_net_user_info(self, bungie_net_user_info):
        """Sets the bungie_net_user_info of this FireteamMember.


        :param bungie_net_user_info: The bungie_net_user_info of this FireteamMember.  # noqa: E501
        :type: UserInfoCard
        """

        self._bungie_net_user_info = bungie_net_user_info

    @property
    def character_id(self):
        """Gets the character_id of this FireteamMember.  # noqa: E501


        :return: The character_id of this FireteamMember.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this FireteamMember.


        :param character_id: The character_id of this FireteamMember.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

    @property
    def date_joined(self):
        """Gets the date_joined of this FireteamMember.  # noqa: E501


        :return: The date_joined of this FireteamMember.  # noqa: E501
        :rtype: datetime
        """
        return self._date_joined

    @date_joined.setter
    def date_joined(self, date_joined):
        """Sets the date_joined of this FireteamMember.


        :param date_joined: The date_joined of this FireteamMember.  # noqa: E501
        :type: datetime
        """

        self._date_joined = date_joined

    @property
    def has_microphone(self):
        """Gets the has_microphone of this FireteamMember.  # noqa: E501


        :return: The has_microphone of this FireteamMember.  # noqa: E501
        :rtype: bool
        """
        return self._has_microphone

    @has_microphone.setter
    def has_microphone(self, has_microphone):
        """Sets the has_microphone of this FireteamMember.


        :param has_microphone: The has_microphone of this FireteamMember.  # noqa: E501
        :type: bool
        """

        self._has_microphone = has_microphone

    @property
    def last_platform_invite_attempt_date(self):
        """Gets the last_platform_invite_attempt_date of this FireteamMember.  # noqa: E501


        :return: The last_platform_invite_attempt_date of this FireteamMember.  # noqa: E501
        :rtype: datetime
        """
        return self._last_platform_invite_attempt_date

    @last_platform_invite_attempt_date.setter
    def last_platform_invite_attempt_date(self, last_platform_invite_attempt_date):
        """Sets the last_platform_invite_attempt_date of this FireteamMember.


        :param last_platform_invite_attempt_date: The last_platform_invite_attempt_date of this FireteamMember.  # noqa: E501
        :type: datetime
        """

        self._last_platform_invite_attempt_date = last_platform_invite_attempt_date

    @property
    def last_platform_invite_attempt_result(self):
        """Gets the last_platform_invite_attempt_result of this FireteamMember.  # noqa: E501


        :return: The last_platform_invite_attempt_result of this FireteamMember.  # noqa: E501
        :rtype: int
        """
        return self._last_platform_invite_attempt_result

    @last_platform_invite_attempt_result.setter
    def last_platform_invite_attempt_result(self, last_platform_invite_attempt_result):
        """Sets the last_platform_invite_attempt_result of this FireteamMember.


        :param last_platform_invite_attempt_result: The last_platform_invite_attempt_result of this FireteamMember.  # noqa: E501
        :type: int
        """

        self._last_platform_invite_attempt_result = last_platform_invite_attempt_result

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
        if not isinstance(other, FireteamMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other