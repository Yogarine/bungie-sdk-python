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


class DestinyFactionDefinition(object):
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
        'display_properties': 'DestinyDisplayPropertiesDefinition',
        'progression_hash': 'int',
        'token_values': 'dict(str, int)',
        'reward_item_hash': 'int',
        'reward_vendor_hash': 'int',
        'vendors': 'list[DestinyFactionVendorDefinition]',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'progression_hash': 'progressionHash',
        'token_values': 'tokenValues',
        'reward_item_hash': 'rewardItemHash',
        'reward_vendor_hash': 'rewardVendorHash',
        'vendors': 'vendors',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, progression_hash=None, token_values=None, reward_item_hash=None, reward_vendor_hash=None, vendors=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyFactionDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._display_properties = None
        self._progression_hash = None
        self._token_values = None
        self._reward_item_hash = None
        self._reward_vendor_hash = None
        self._vendors = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
            self.display_properties = display_properties
        if progression_hash is not None:
            self.progression_hash = progression_hash
        if token_values is not None:
            self.token_values = token_values
        if reward_item_hash is not None:
            self.reward_item_hash = reward_item_hash
        if reward_vendor_hash is not None:
            self.reward_vendor_hash = reward_vendor_hash
        if vendors is not None:
            self.vendors = vendors
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyFactionDefinition.  # noqa: E501


        :return: The display_properties of this DestinyFactionDefinition.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyFactionDefinition.


        :param display_properties: The display_properties of this DestinyFactionDefinition.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def progression_hash(self):
        """Gets the progression_hash of this DestinyFactionDefinition.  # noqa: E501

        The hash identifier for the DestinyProgressionDefinition that indicates the character's relationship with this faction in terms of experience and levels.  # noqa: E501

        :return: The progression_hash of this DestinyFactionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._progression_hash

    @progression_hash.setter
    def progression_hash(self, progression_hash):
        """Sets the progression_hash of this DestinyFactionDefinition.

        The hash identifier for the DestinyProgressionDefinition that indicates the character's relationship with this faction in terms of experience and levels.  # noqa: E501

        :param progression_hash: The progression_hash of this DestinyFactionDefinition.  # noqa: E501
        :type: int
        """

        self._progression_hash = progression_hash

    @property
    def token_values(self):
        """Gets the token_values of this DestinyFactionDefinition.  # noqa: E501

        The faction token item hashes, and their respective progression values.  # noqa: E501

        :return: The token_values of this DestinyFactionDefinition.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._token_values

    @token_values.setter
    def token_values(self, token_values):
        """Sets the token_values of this DestinyFactionDefinition.

        The faction token item hashes, and their respective progression values.  # noqa: E501

        :param token_values: The token_values of this DestinyFactionDefinition.  # noqa: E501
        :type: dict(str, int)
        """

        self._token_values = token_values

    @property
    def reward_item_hash(self):
        """Gets the reward_item_hash of this DestinyFactionDefinition.  # noqa: E501

        The faction reward item hash, usually an engram.  # noqa: E501

        :return: The reward_item_hash of this DestinyFactionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._reward_item_hash

    @reward_item_hash.setter
    def reward_item_hash(self, reward_item_hash):
        """Sets the reward_item_hash of this DestinyFactionDefinition.

        The faction reward item hash, usually an engram.  # noqa: E501

        :param reward_item_hash: The reward_item_hash of this DestinyFactionDefinition.  # noqa: E501
        :type: int
        """

        self._reward_item_hash = reward_item_hash

    @property
    def reward_vendor_hash(self):
        """Gets the reward_vendor_hash of this DestinyFactionDefinition.  # noqa: E501

        The faction reward vendor hash, used for faction engram previews.  # noqa: E501

        :return: The reward_vendor_hash of this DestinyFactionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._reward_vendor_hash

    @reward_vendor_hash.setter
    def reward_vendor_hash(self, reward_vendor_hash):
        """Sets the reward_vendor_hash of this DestinyFactionDefinition.

        The faction reward vendor hash, used for faction engram previews.  # noqa: E501

        :param reward_vendor_hash: The reward_vendor_hash of this DestinyFactionDefinition.  # noqa: E501
        :type: int
        """

        self._reward_vendor_hash = reward_vendor_hash

    @property
    def vendors(self):
        """Gets the vendors of this DestinyFactionDefinition.  # noqa: E501

        List of vendors that are associated with this faction. The last vendor that passes the unlock flag checks is the one that should be shown.  # noqa: E501

        :return: The vendors of this DestinyFactionDefinition.  # noqa: E501
        :rtype: list[DestinyFactionVendorDefinition]
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        """Sets the vendors of this DestinyFactionDefinition.

        List of vendors that are associated with this faction. The last vendor that passes the unlock flag checks is the one that should be shown.  # noqa: E501

        :param vendors: The vendors of this DestinyFactionDefinition.  # noqa: E501
        :type: list[DestinyFactionVendorDefinition]
        """

        self._vendors = vendors

    @property
    def hash(self):
        """Gets the hash of this DestinyFactionDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyFactionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyFactionDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyFactionDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyFactionDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyFactionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyFactionDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyFactionDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyFactionDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyFactionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyFactionDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyFactionDefinition.  # noqa: E501
        :type: bool
        """

        self._redacted = redacted

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
        if not isinstance(other, DestinyFactionDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
