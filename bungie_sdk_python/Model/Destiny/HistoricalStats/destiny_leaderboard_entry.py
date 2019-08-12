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


class DestinyLeaderboardEntry(object):
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
        'rank': 'int',
        'player': 'DestinyPlayer',
        'character_id': 'int',
        'value': 'DestinyHistoricalStatsValue'
    }

    attribute_map = {
        'rank': 'rank',
        'player': 'player',
        'character_id': 'characterId',
        'value': 'value'
    }

    def __init__(self, rank=None, player=None, character_id=None, value=None):  # noqa: E501
        """DestinyLeaderboardEntry - a model defined in OpenAPI"""  # noqa: E501

        self._rank = None
        self._player = None
        self._character_id = None
        self._value = None
        self.discriminator = None

        if rank is not None:
            self.rank = rank
        if player is not None:
            self.player = player
        if character_id is not None:
            self.character_id = character_id
        if value is not None:
            self.value = value

    @property
    def rank(self):
        """Gets the rank of this DestinyLeaderboardEntry.  # noqa: E501

        Where this player ranks on the leaderboard. A value of 1 is the top rank.  # noqa: E501

        :return: The rank of this DestinyLeaderboardEntry.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this DestinyLeaderboardEntry.

        Where this player ranks on the leaderboard. A value of 1 is the top rank.  # noqa: E501

        :param rank: The rank of this DestinyLeaderboardEntry.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def player(self):
        """Gets the player of this DestinyLeaderboardEntry.  # noqa: E501

        Identity details of the player  # noqa: E501

        :return: The player of this DestinyLeaderboardEntry.  # noqa: E501
        :rtype: DestinyPlayer
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this DestinyLeaderboardEntry.

        Identity details of the player  # noqa: E501

        :param player: The player of this DestinyLeaderboardEntry.  # noqa: E501
        :type: DestinyPlayer
        """

        self._player = player

    @property
    def character_id(self):
        """Gets the character_id of this DestinyLeaderboardEntry.  # noqa: E501

        ID of the player's best character for the reported stat.  # noqa: E501

        :return: The character_id of this DestinyLeaderboardEntry.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this DestinyLeaderboardEntry.

        ID of the player's best character for the reported stat.  # noqa: E501

        :param character_id: The character_id of this DestinyLeaderboardEntry.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

    @property
    def value(self):
        """Gets the value of this DestinyLeaderboardEntry.  # noqa: E501

        Value of the stat for this player  # noqa: E501

        :return: The value of this DestinyLeaderboardEntry.  # noqa: E501
        :rtype: DestinyHistoricalStatsValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DestinyLeaderboardEntry.

        Value of the stat for this player  # noqa: E501

        :param value: The value of this DestinyLeaderboardEntry.  # noqa: E501
        :type: DestinyHistoricalStatsValue
        """

        self._value = value

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
        if not isinstance(other, DestinyLeaderboardEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other