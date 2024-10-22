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


class DestinyPlayer(object):
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
        'character_class': 'str',
        'class_hash': 'int',
        'race_hash': 'int',
        'gender_hash': 'int',
        'character_level': 'int',
        'light_level': 'int',
        'bungie_net_user_info': 'UserInfoCard',
        'clan_name': 'str',
        'clan_tag': 'str',
        'emblem_hash': 'int'
    }

    attribute_map = {
        'destiny_user_info': 'destinyUserInfo',
        'character_class': 'characterClass',
        'class_hash': 'classHash',
        'race_hash': 'raceHash',
        'gender_hash': 'genderHash',
        'character_level': 'characterLevel',
        'light_level': 'lightLevel',
        'bungie_net_user_info': 'bungieNetUserInfo',
        'clan_name': 'clanName',
        'clan_tag': 'clanTag',
        'emblem_hash': 'emblemHash'
    }

    def __init__(self, destiny_user_info=None, character_class=None, class_hash=None, race_hash=None, gender_hash=None, character_level=None, light_level=None, bungie_net_user_info=None, clan_name=None, clan_tag=None, emblem_hash=None):  # noqa: E501
        """DestinyPlayer - a model defined in OpenAPI"""  # noqa: E501

        self._destiny_user_info = None
        self._character_class = None
        self._class_hash = None
        self._race_hash = None
        self._gender_hash = None
        self._character_level = None
        self._light_level = None
        self._bungie_net_user_info = None
        self._clan_name = None
        self._clan_tag = None
        self._emblem_hash = None
        self.discriminator = None

        if destiny_user_info is not None:
            self.destiny_user_info = destiny_user_info
        if character_class is not None:
            self.character_class = character_class
        if class_hash is not None:
            self.class_hash = class_hash
        if race_hash is not None:
            self.race_hash = race_hash
        if gender_hash is not None:
            self.gender_hash = gender_hash
        if character_level is not None:
            self.character_level = character_level
        if light_level is not None:
            self.light_level = light_level
        if bungie_net_user_info is not None:
            self.bungie_net_user_info = bungie_net_user_info
        if clan_name is not None:
            self.clan_name = clan_name
        if clan_tag is not None:
            self.clan_tag = clan_tag
        if emblem_hash is not None:
            self.emblem_hash = emblem_hash

    @property
    def destiny_user_info(self):
        """Gets the destiny_user_info of this DestinyPlayer.  # noqa: E501

        Details about the player as they are known in game (platform display name, Destiny emblem)  # noqa: E501

        :return: The destiny_user_info of this DestinyPlayer.  # noqa: E501
        :rtype: UserInfoCard
        """
        return self._destiny_user_info

    @destiny_user_info.setter
    def destiny_user_info(self, destiny_user_info):
        """Sets the destiny_user_info of this DestinyPlayer.

        Details about the player as they are known in game (platform display name, Destiny emblem)  # noqa: E501

        :param destiny_user_info: The destiny_user_info of this DestinyPlayer.  # noqa: E501
        :type: UserInfoCard
        """

        self._destiny_user_info = destiny_user_info

    @property
    def character_class(self):
        """Gets the character_class of this DestinyPlayer.  # noqa: E501

        Class of the character if applicable and available.  # noqa: E501

        :return: The character_class of this DestinyPlayer.  # noqa: E501
        :rtype: str
        """
        return self._character_class

    @character_class.setter
    def character_class(self, character_class):
        """Sets the character_class of this DestinyPlayer.

        Class of the character if applicable and available.  # noqa: E501

        :param character_class: The character_class of this DestinyPlayer.  # noqa: E501
        :type: str
        """

        self._character_class = character_class

    @property
    def class_hash(self):
        """Gets the class_hash of this DestinyPlayer.  # noqa: E501


        :return: The class_hash of this DestinyPlayer.  # noqa: E501
        :rtype: int
        """
        return self._class_hash

    @class_hash.setter
    def class_hash(self, class_hash):
        """Sets the class_hash of this DestinyPlayer.


        :param class_hash: The class_hash of this DestinyPlayer.  # noqa: E501
        :type: int
        """

        self._class_hash = class_hash

    @property
    def race_hash(self):
        """Gets the race_hash of this DestinyPlayer.  # noqa: E501


        :return: The race_hash of this DestinyPlayer.  # noqa: E501
        :rtype: int
        """
        return self._race_hash

    @race_hash.setter
    def race_hash(self, race_hash):
        """Sets the race_hash of this DestinyPlayer.


        :param race_hash: The race_hash of this DestinyPlayer.  # noqa: E501
        :type: int
        """

        self._race_hash = race_hash

    @property
    def gender_hash(self):
        """Gets the gender_hash of this DestinyPlayer.  # noqa: E501


        :return: The gender_hash of this DestinyPlayer.  # noqa: E501
        :rtype: int
        """
        return self._gender_hash

    @gender_hash.setter
    def gender_hash(self, gender_hash):
        """Sets the gender_hash of this DestinyPlayer.


        :param gender_hash: The gender_hash of this DestinyPlayer.  # noqa: E501
        :type: int
        """

        self._gender_hash = gender_hash

    @property
    def character_level(self):
        """Gets the character_level of this DestinyPlayer.  # noqa: E501

        Level of the character if available. Zero if it is not available.  # noqa: E501

        :return: The character_level of this DestinyPlayer.  # noqa: E501
        :rtype: int
        """
        return self._character_level

    @character_level.setter
    def character_level(self, character_level):
        """Sets the character_level of this DestinyPlayer.

        Level of the character if available. Zero if it is not available.  # noqa: E501

        :param character_level: The character_level of this DestinyPlayer.  # noqa: E501
        :type: int
        """

        self._character_level = character_level

    @property
    def light_level(self):
        """Gets the light_level of this DestinyPlayer.  # noqa: E501

        Light Level of the character if available. Zero if it is not available.  # noqa: E501

        :return: The light_level of this DestinyPlayer.  # noqa: E501
        :rtype: int
        """
        return self._light_level

    @light_level.setter
    def light_level(self, light_level):
        """Sets the light_level of this DestinyPlayer.

        Light Level of the character if available. Zero if it is not available.  # noqa: E501

        :param light_level: The light_level of this DestinyPlayer.  # noqa: E501
        :type: int
        """

        self._light_level = light_level

    @property
    def bungie_net_user_info(self):
        """Gets the bungie_net_user_info of this DestinyPlayer.  # noqa: E501

        Details about the player as they are known on BungieNet. This will be undefined if the player has marked their credential private, or does not have a BungieNet account.  # noqa: E501

        :return: The bungie_net_user_info of this DestinyPlayer.  # noqa: E501
        :rtype: UserInfoCard
        """
        return self._bungie_net_user_info

    @bungie_net_user_info.setter
    def bungie_net_user_info(self, bungie_net_user_info):
        """Sets the bungie_net_user_info of this DestinyPlayer.

        Details about the player as they are known on BungieNet. This will be undefined if the player has marked their credential private, or does not have a BungieNet account.  # noqa: E501

        :param bungie_net_user_info: The bungie_net_user_info of this DestinyPlayer.  # noqa: E501
        :type: UserInfoCard
        """

        self._bungie_net_user_info = bungie_net_user_info

    @property
    def clan_name(self):
        """Gets the clan_name of this DestinyPlayer.  # noqa: E501

        Current clan name for the player. This value may be null or an empty string if the user does not have a clan.  # noqa: E501

        :return: The clan_name of this DestinyPlayer.  # noqa: E501
        :rtype: str
        """
        return self._clan_name

    @clan_name.setter
    def clan_name(self, clan_name):
        """Sets the clan_name of this DestinyPlayer.

        Current clan name for the player. This value may be null or an empty string if the user does not have a clan.  # noqa: E501

        :param clan_name: The clan_name of this DestinyPlayer.  # noqa: E501
        :type: str
        """

        self._clan_name = clan_name

    @property
    def clan_tag(self):
        """Gets the clan_tag of this DestinyPlayer.  # noqa: E501

        Current clan tag for the player. This value may be null or an empty string if the user does not have a clan.  # noqa: E501

        :return: The clan_tag of this DestinyPlayer.  # noqa: E501
        :rtype: str
        """
        return self._clan_tag

    @clan_tag.setter
    def clan_tag(self, clan_tag):
        """Sets the clan_tag of this DestinyPlayer.

        Current clan tag for the player. This value may be null or an empty string if the user does not have a clan.  # noqa: E501

        :param clan_tag: The clan_tag of this DestinyPlayer.  # noqa: E501
        :type: str
        """

        self._clan_tag = clan_tag

    @property
    def emblem_hash(self):
        """Gets the emblem_hash of this DestinyPlayer.  # noqa: E501

        If we know the emblem's hash, this can be used to look up the player's emblem at the time of a match when receiving PGCR data, or otherwise their currently equipped emblem (if we are able to obtain it).  # noqa: E501

        :return: The emblem_hash of this DestinyPlayer.  # noqa: E501
        :rtype: int
        """
        return self._emblem_hash

    @emblem_hash.setter
    def emblem_hash(self, emblem_hash):
        """Sets the emblem_hash of this DestinyPlayer.

        If we know the emblem's hash, this can be used to look up the player's emblem at the time of a match when receiving PGCR data, or otherwise their currently equipped emblem (if we are able to obtain it).  # noqa: E501

        :param emblem_hash: The emblem_hash of this DestinyPlayer.  # noqa: E501
        :type: int
        """

        self._emblem_hash = emblem_hash

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
        if not isinstance(other, DestinyPlayer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
