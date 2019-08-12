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


class DestinyEntitySearchResultItem(object):
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
        'hash': 'int',
        'entity_type': 'str',
        'display_properties': 'DestinyDisplayPropertiesDefinition',
        'weight': 'float'
    }

    attribute_map = {
        'hash': 'hash',
        'entity_type': 'entityType',
        'display_properties': 'displayProperties',
        'weight': 'weight'
    }

    def __init__(self, hash=None, entity_type=None, display_properties=None, weight=None):  # noqa: E501
        """DestinyEntitySearchResultItem - a model defined in OpenAPI"""  # noqa: E501

        self._hash = None
        self._entity_type = None
        self._display_properties = None
        self._weight = None
        self.discriminator = None

        if hash is not None:
            self.hash = hash
        if entity_type is not None:
            self.entity_type = entity_type
        if display_properties is not None:
            self.display_properties = display_properties
        if weight is not None:
            self.weight = weight

    @property
    def hash(self):
        """Gets the hash of this DestinyEntitySearchResultItem.  # noqa: E501

        The hash identifier of the entity. You will use this to look up the DestinyDefinition relevant for the entity found.  # noqa: E501

        :return: The hash of this DestinyEntitySearchResultItem.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyEntitySearchResultItem.

        The hash identifier of the entity. You will use this to look up the DestinyDefinition relevant for the entity found.  # noqa: E501

        :param hash: The hash of this DestinyEntitySearchResultItem.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def entity_type(self):
        """Gets the entity_type of this DestinyEntitySearchResultItem.  # noqa: E501

        The type of entity, returned as a string matching the DestinyDefinition's contract class name. You'll have to have your own mapping from class names to actually looking up those definitions in the manifest databases.  # noqa: E501

        :return: The entity_type of this DestinyEntitySearchResultItem.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this DestinyEntitySearchResultItem.

        The type of entity, returned as a string matching the DestinyDefinition's contract class name. You'll have to have your own mapping from class names to actually looking up those definitions in the manifest databases.  # noqa: E501

        :param entity_type: The entity_type of this DestinyEntitySearchResultItem.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyEntitySearchResultItem.  # noqa: E501

        Basic display properties on the entity, so you don't have to look up the definition to show basic results for the item.  # noqa: E501

        :return: The display_properties of this DestinyEntitySearchResultItem.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyEntitySearchResultItem.

        Basic display properties on the entity, so you don't have to look up the definition to show basic results for the item.  # noqa: E501

        :param display_properties: The display_properties of this DestinyEntitySearchResultItem.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def weight(self):
        """Gets the weight of this DestinyEntitySearchResultItem.  # noqa: E501

        The ranking value for sorting that we calculated using our relevance formula. This will hopefully get better with time and iteration.  # noqa: E501

        :return: The weight of this DestinyEntitySearchResultItem.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this DestinyEntitySearchResultItem.

        The ranking value for sorting that we calculated using our relevance formula. This will hopefully get better with time and iteration.  # noqa: E501

        :param weight: The weight of this DestinyEntitySearchResultItem.  # noqa: E501
        :type: float
        """

        self._weight = weight

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
        if not isinstance(other, DestinyEntitySearchResultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
