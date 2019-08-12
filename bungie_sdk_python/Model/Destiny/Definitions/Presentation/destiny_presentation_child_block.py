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


class DestinyPresentationChildBlock(object):
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
        'presentation_node_type': 'int',
        'parent_presentation_node_hashes': 'list[int]',
        'display_style': 'int'
    }

    attribute_map = {
        'presentation_node_type': 'presentationNodeType',
        'parent_presentation_node_hashes': 'parentPresentationNodeHashes',
        'display_style': 'displayStyle'
    }

    def __init__(self, presentation_node_type=None, parent_presentation_node_hashes=None, display_style=None):  # noqa: E501
        """DestinyPresentationChildBlock - a model defined in OpenAPI"""  # noqa: E501

        self._presentation_node_type = None
        self._parent_presentation_node_hashes = None
        self._display_style = None
        self.discriminator = None

        if presentation_node_type is not None:
            self.presentation_node_type = presentation_node_type
        if parent_presentation_node_hashes is not None:
            self.parent_presentation_node_hashes = parent_presentation_node_hashes
        if display_style is not None:
            self.display_style = display_style

    @property
    def presentation_node_type(self):
        """Gets the presentation_node_type of this DestinyPresentationChildBlock.  # noqa: E501


        :return: The presentation_node_type of this DestinyPresentationChildBlock.  # noqa: E501
        :rtype: int
        """
        return self._presentation_node_type

    @presentation_node_type.setter
    def presentation_node_type(self, presentation_node_type):
        """Sets the presentation_node_type of this DestinyPresentationChildBlock.


        :param presentation_node_type: The presentation_node_type of this DestinyPresentationChildBlock.  # noqa: E501
        :type: int
        """

        self._presentation_node_type = presentation_node_type

    @property
    def parent_presentation_node_hashes(self):
        """Gets the parent_presentation_node_hashes of this DestinyPresentationChildBlock.  # noqa: E501


        :return: The parent_presentation_node_hashes of this DestinyPresentationChildBlock.  # noqa: E501
        :rtype: list[int]
        """
        return self._parent_presentation_node_hashes

    @parent_presentation_node_hashes.setter
    def parent_presentation_node_hashes(self, parent_presentation_node_hashes):
        """Sets the parent_presentation_node_hashes of this DestinyPresentationChildBlock.


        :param parent_presentation_node_hashes: The parent_presentation_node_hashes of this DestinyPresentationChildBlock.  # noqa: E501
        :type: list[int]
        """

        self._parent_presentation_node_hashes = parent_presentation_node_hashes

    @property
    def display_style(self):
        """Gets the display_style of this DestinyPresentationChildBlock.  # noqa: E501


        :return: The display_style of this DestinyPresentationChildBlock.  # noqa: E501
        :rtype: int
        """
        return self._display_style

    @display_style.setter
    def display_style(self, display_style):
        """Sets the display_style of this DestinyPresentationChildBlock.


        :param display_style: The display_style of this DestinyPresentationChildBlock.  # noqa: E501
        :type: int
        """

        self._display_style = display_style

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
        if not isinstance(other, DestinyPresentationChildBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other