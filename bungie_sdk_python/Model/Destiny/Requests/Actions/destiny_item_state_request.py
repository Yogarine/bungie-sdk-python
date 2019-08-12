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


class DestinyItemStateRequest(object):
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
        'state': 'bool',
        'item_id': 'int',
        'character_id': 'int',
        'membership_type': 'int'
    }

    attribute_map = {
        'state': 'state',
        'item_id': 'itemId',
        'character_id': 'characterId',
        'membership_type': 'membershipType'
    }

    def __init__(self, state=None, item_id=None, character_id=None, membership_type=None):  # noqa: E501
        """DestinyItemStateRequest - a model defined in OpenAPI"""  # noqa: E501

        self._state = None
        self._item_id = None
        self._character_id = None
        self._membership_type = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if item_id is not None:
            self.item_id = item_id
        if character_id is not None:
            self.character_id = character_id
        if membership_type is not None:
            self.membership_type = membership_type

    @property
    def state(self):
        """Gets the state of this DestinyItemStateRequest.  # noqa: E501


        :return: The state of this DestinyItemStateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DestinyItemStateRequest.


        :param state: The state of this DestinyItemStateRequest.  # noqa: E501
        :type: bool
        """

        self._state = state

    @property
    def item_id(self):
        """Gets the item_id of this DestinyItemStateRequest.  # noqa: E501


        :return: The item_id of this DestinyItemStateRequest.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this DestinyItemStateRequest.


        :param item_id: The item_id of this DestinyItemStateRequest.  # noqa: E501
        :type: int
        """

        self._item_id = item_id

    @property
    def character_id(self):
        """Gets the character_id of this DestinyItemStateRequest.  # noqa: E501


        :return: The character_id of this DestinyItemStateRequest.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this DestinyItemStateRequest.


        :param character_id: The character_id of this DestinyItemStateRequest.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

    @property
    def membership_type(self):
        """Gets the membership_type of this DestinyItemStateRequest.  # noqa: E501


        :return: The membership_type of this DestinyItemStateRequest.  # noqa: E501
        :rtype: int
        """
        return self._membership_type

    @membership_type.setter
    def membership_type(self, membership_type):
        """Sets the membership_type of this DestinyItemStateRequest.


        :param membership_type: The membership_type of this DestinyItemStateRequest.  # noqa: E501
        :type: int
        """

        self._membership_type = membership_type

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
        if not isinstance(other, DestinyItemStateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other