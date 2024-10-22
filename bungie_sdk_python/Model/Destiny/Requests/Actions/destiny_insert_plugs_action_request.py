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


class DestinyInsertPlugsActionRequest(object):
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
        'action_token': 'str',
        'item_instance_id': 'int',
        'plug': 'DestinyInsertPlugsRequestEntry',
        'character_id': 'int',
        'membership_type': 'int'
    }

    attribute_map = {
        'action_token': 'actionToken',
        'item_instance_id': 'itemInstanceId',
        'plug': 'plug',
        'character_id': 'characterId',
        'membership_type': 'membershipType'
    }

    def __init__(self, action_token=None, item_instance_id=None, plug=None, character_id=None, membership_type=None):  # noqa: E501
        """DestinyInsertPlugsActionRequest - a model defined in OpenAPI"""  # noqa: E501

        self._action_token = None
        self._item_instance_id = None
        self._plug = None
        self._character_id = None
        self._membership_type = None
        self.discriminator = None

        if action_token is not None:
            self.action_token = action_token
        if item_instance_id is not None:
            self.item_instance_id = item_instance_id
        if plug is not None:
            self.plug = plug
        if character_id is not None:
            self.character_id = character_id
        if membership_type is not None:
            self.membership_type = membership_type

    @property
    def action_token(self):
        """Gets the action_token of this DestinyInsertPlugsActionRequest.  # noqa: E501

        Action token provided by the AwaGetActionToken API call.  # noqa: E501

        :return: The action_token of this DestinyInsertPlugsActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._action_token

    @action_token.setter
    def action_token(self, action_token):
        """Sets the action_token of this DestinyInsertPlugsActionRequest.

        Action token provided by the AwaGetActionToken API call.  # noqa: E501

        :param action_token: The action_token of this DestinyInsertPlugsActionRequest.  # noqa: E501
        :type: str
        """

        self._action_token = action_token

    @property
    def item_instance_id(self):
        """Gets the item_instance_id of this DestinyInsertPlugsActionRequest.  # noqa: E501

        The instance ID of the item having a plug inserted. Only instanced items can have sockets.  # noqa: E501

        :return: The item_instance_id of this DestinyInsertPlugsActionRequest.  # noqa: E501
        :rtype: int
        """
        return self._item_instance_id

    @item_instance_id.setter
    def item_instance_id(self, item_instance_id):
        """Sets the item_instance_id of this DestinyInsertPlugsActionRequest.

        The instance ID of the item having a plug inserted. Only instanced items can have sockets.  # noqa: E501

        :param item_instance_id: The item_instance_id of this DestinyInsertPlugsActionRequest.  # noqa: E501
        :type: int
        """

        self._item_instance_id = item_instance_id

    @property
    def plug(self):
        """Gets the plug of this DestinyInsertPlugsActionRequest.  # noqa: E501

        The plugs being inserted.  # noqa: E501

        :return: The plug of this DestinyInsertPlugsActionRequest.  # noqa: E501
        :rtype: DestinyInsertPlugsRequestEntry
        """
        return self._plug

    @plug.setter
    def plug(self, plug):
        """Sets the plug of this DestinyInsertPlugsActionRequest.

        The plugs being inserted.  # noqa: E501

        :param plug: The plug of this DestinyInsertPlugsActionRequest.  # noqa: E501
        :type: DestinyInsertPlugsRequestEntry
        """

        self._plug = plug

    @property
    def character_id(self):
        """Gets the character_id of this DestinyInsertPlugsActionRequest.  # noqa: E501


        :return: The character_id of this DestinyInsertPlugsActionRequest.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this DestinyInsertPlugsActionRequest.


        :param character_id: The character_id of this DestinyInsertPlugsActionRequest.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

    @property
    def membership_type(self):
        """Gets the membership_type of this DestinyInsertPlugsActionRequest.  # noqa: E501


        :return: The membership_type of this DestinyInsertPlugsActionRequest.  # noqa: E501
        :rtype: int
        """
        return self._membership_type

    @membership_type.setter
    def membership_type(self, membership_type):
        """Sets the membership_type of this DestinyInsertPlugsActionRequest.


        :param membership_type: The membership_type of this DestinyInsertPlugsActionRequest.  # noqa: E501
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
        if not isinstance(other, DestinyInsertPlugsActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
