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


class Destiny2CoreSettings(object):
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
        'collection_root_node': 'int',
        'badges_root_node': 'int',
        'records_root_node': 'int',
        'medals_root_node': 'int',
        'current_rank_progression_hashes': 'list[int]',
        'undiscovered_collectible_image': 'str',
        'ammo_type_heavy_icon': 'str',
        'ammo_type_special_icon': 'str',
        'ammo_type_primary_icon': 'str'
    }

    attribute_map = {
        'collection_root_node': 'collectionRootNode',
        'badges_root_node': 'badgesRootNode',
        'records_root_node': 'recordsRootNode',
        'medals_root_node': 'medalsRootNode',
        'current_rank_progression_hashes': 'currentRankProgressionHashes',
        'undiscovered_collectible_image': 'undiscoveredCollectibleImage',
        'ammo_type_heavy_icon': 'ammoTypeHeavyIcon',
        'ammo_type_special_icon': 'ammoTypeSpecialIcon',
        'ammo_type_primary_icon': 'ammoTypePrimaryIcon'
    }

    def __init__(self, collection_root_node=None, badges_root_node=None, records_root_node=None, medals_root_node=None, current_rank_progression_hashes=None, undiscovered_collectible_image=None, ammo_type_heavy_icon=None, ammo_type_special_icon=None, ammo_type_primary_icon=None):  # noqa: E501
        """Destiny2CoreSettings - a model defined in OpenAPI"""  # noqa: E501

        self._collection_root_node = None
        self._badges_root_node = None
        self._records_root_node = None
        self._medals_root_node = None
        self._current_rank_progression_hashes = None
        self._undiscovered_collectible_image = None
        self._ammo_type_heavy_icon = None
        self._ammo_type_special_icon = None
        self._ammo_type_primary_icon = None
        self.discriminator = None

        if collection_root_node is not None:
            self.collection_root_node = collection_root_node
        if badges_root_node is not None:
            self.badges_root_node = badges_root_node
        if records_root_node is not None:
            self.records_root_node = records_root_node
        if medals_root_node is not None:
            self.medals_root_node = medals_root_node
        if current_rank_progression_hashes is not None:
            self.current_rank_progression_hashes = current_rank_progression_hashes
        if undiscovered_collectible_image is not None:
            self.undiscovered_collectible_image = undiscovered_collectible_image
        if ammo_type_heavy_icon is not None:
            self.ammo_type_heavy_icon = ammo_type_heavy_icon
        if ammo_type_special_icon is not None:
            self.ammo_type_special_icon = ammo_type_special_icon
        if ammo_type_primary_icon is not None:
            self.ammo_type_primary_icon = ammo_type_primary_icon

    @property
    def collection_root_node(self):
        """Gets the collection_root_node of this Destiny2CoreSettings.  # noqa: E501


        :return: The collection_root_node of this Destiny2CoreSettings.  # noqa: E501
        :rtype: int
        """
        return self._collection_root_node

    @collection_root_node.setter
    def collection_root_node(self, collection_root_node):
        """Sets the collection_root_node of this Destiny2CoreSettings.


        :param collection_root_node: The collection_root_node of this Destiny2CoreSettings.  # noqa: E501
        :type: int
        """

        self._collection_root_node = collection_root_node

    @property
    def badges_root_node(self):
        """Gets the badges_root_node of this Destiny2CoreSettings.  # noqa: E501


        :return: The badges_root_node of this Destiny2CoreSettings.  # noqa: E501
        :rtype: int
        """
        return self._badges_root_node

    @badges_root_node.setter
    def badges_root_node(self, badges_root_node):
        """Sets the badges_root_node of this Destiny2CoreSettings.


        :param badges_root_node: The badges_root_node of this Destiny2CoreSettings.  # noqa: E501
        :type: int
        """

        self._badges_root_node = badges_root_node

    @property
    def records_root_node(self):
        """Gets the records_root_node of this Destiny2CoreSettings.  # noqa: E501


        :return: The records_root_node of this Destiny2CoreSettings.  # noqa: E501
        :rtype: int
        """
        return self._records_root_node

    @records_root_node.setter
    def records_root_node(self, records_root_node):
        """Sets the records_root_node of this Destiny2CoreSettings.


        :param records_root_node: The records_root_node of this Destiny2CoreSettings.  # noqa: E501
        :type: int
        """

        self._records_root_node = records_root_node

    @property
    def medals_root_node(self):
        """Gets the medals_root_node of this Destiny2CoreSettings.  # noqa: E501


        :return: The medals_root_node of this Destiny2CoreSettings.  # noqa: E501
        :rtype: int
        """
        return self._medals_root_node

    @medals_root_node.setter
    def medals_root_node(self, medals_root_node):
        """Sets the medals_root_node of this Destiny2CoreSettings.


        :param medals_root_node: The medals_root_node of this Destiny2CoreSettings.  # noqa: E501
        :type: int
        """

        self._medals_root_node = medals_root_node

    @property
    def current_rank_progression_hashes(self):
        """Gets the current_rank_progression_hashes of this Destiny2CoreSettings.  # noqa: E501


        :return: The current_rank_progression_hashes of this Destiny2CoreSettings.  # noqa: E501
        :rtype: list[int]
        """
        return self._current_rank_progression_hashes

    @current_rank_progression_hashes.setter
    def current_rank_progression_hashes(self, current_rank_progression_hashes):
        """Sets the current_rank_progression_hashes of this Destiny2CoreSettings.


        :param current_rank_progression_hashes: The current_rank_progression_hashes of this Destiny2CoreSettings.  # noqa: E501
        :type: list[int]
        """

        self._current_rank_progression_hashes = current_rank_progression_hashes

    @property
    def undiscovered_collectible_image(self):
        """Gets the undiscovered_collectible_image of this Destiny2CoreSettings.  # noqa: E501


        :return: The undiscovered_collectible_image of this Destiny2CoreSettings.  # noqa: E501
        :rtype: str
        """
        return self._undiscovered_collectible_image

    @undiscovered_collectible_image.setter
    def undiscovered_collectible_image(self, undiscovered_collectible_image):
        """Sets the undiscovered_collectible_image of this Destiny2CoreSettings.


        :param undiscovered_collectible_image: The undiscovered_collectible_image of this Destiny2CoreSettings.  # noqa: E501
        :type: str
        """

        self._undiscovered_collectible_image = undiscovered_collectible_image

    @property
    def ammo_type_heavy_icon(self):
        """Gets the ammo_type_heavy_icon of this Destiny2CoreSettings.  # noqa: E501


        :return: The ammo_type_heavy_icon of this Destiny2CoreSettings.  # noqa: E501
        :rtype: str
        """
        return self._ammo_type_heavy_icon

    @ammo_type_heavy_icon.setter
    def ammo_type_heavy_icon(self, ammo_type_heavy_icon):
        """Sets the ammo_type_heavy_icon of this Destiny2CoreSettings.


        :param ammo_type_heavy_icon: The ammo_type_heavy_icon of this Destiny2CoreSettings.  # noqa: E501
        :type: str
        """

        self._ammo_type_heavy_icon = ammo_type_heavy_icon

    @property
    def ammo_type_special_icon(self):
        """Gets the ammo_type_special_icon of this Destiny2CoreSettings.  # noqa: E501


        :return: The ammo_type_special_icon of this Destiny2CoreSettings.  # noqa: E501
        :rtype: str
        """
        return self._ammo_type_special_icon

    @ammo_type_special_icon.setter
    def ammo_type_special_icon(self, ammo_type_special_icon):
        """Sets the ammo_type_special_icon of this Destiny2CoreSettings.


        :param ammo_type_special_icon: The ammo_type_special_icon of this Destiny2CoreSettings.  # noqa: E501
        :type: str
        """

        self._ammo_type_special_icon = ammo_type_special_icon

    @property
    def ammo_type_primary_icon(self):
        """Gets the ammo_type_primary_icon of this Destiny2CoreSettings.  # noqa: E501


        :return: The ammo_type_primary_icon of this Destiny2CoreSettings.  # noqa: E501
        :rtype: str
        """
        return self._ammo_type_primary_icon

    @ammo_type_primary_icon.setter
    def ammo_type_primary_icon(self, ammo_type_primary_icon):
        """Sets the ammo_type_primary_icon of this Destiny2CoreSettings.


        :param ammo_type_primary_icon: The ammo_type_primary_icon of this Destiny2CoreSettings.  # noqa: E501
        :type: str
        """

        self._ammo_type_primary_icon = ammo_type_primary_icon

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
        if not isinstance(other, Destiny2CoreSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
