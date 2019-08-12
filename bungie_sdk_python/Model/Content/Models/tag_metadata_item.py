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


class TagMetadataItem(object):
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
        'description': 'str',
        'tag_text': 'str',
        'groups': 'list[str]',
        'is_default': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'tag_text': 'tagText',
        'groups': 'groups',
        'is_default': 'isDefault',
        'name': 'name'
    }

    def __init__(self, description=None, tag_text=None, groups=None, is_default=None, name=None):  # noqa: E501
        """TagMetadataItem - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._tag_text = None
        self._groups = None
        self._is_default = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if tag_text is not None:
            self.tag_text = tag_text
        if groups is not None:
            self.groups = groups
        if is_default is not None:
            self.is_default = is_default
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this TagMetadataItem.  # noqa: E501


        :return: The description of this TagMetadataItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TagMetadataItem.


        :param description: The description of this TagMetadataItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tag_text(self):
        """Gets the tag_text of this TagMetadataItem.  # noqa: E501


        :return: The tag_text of this TagMetadataItem.  # noqa: E501
        :rtype: str
        """
        return self._tag_text

    @tag_text.setter
    def tag_text(self, tag_text):
        """Sets the tag_text of this TagMetadataItem.


        :param tag_text: The tag_text of this TagMetadataItem.  # noqa: E501
        :type: str
        """

        self._tag_text = tag_text

    @property
    def groups(self):
        """Gets the groups of this TagMetadataItem.  # noqa: E501


        :return: The groups of this TagMetadataItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this TagMetadataItem.


        :param groups: The groups of this TagMetadataItem.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def is_default(self):
        """Gets the is_default of this TagMetadataItem.  # noqa: E501


        :return: The is_default of this TagMetadataItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this TagMetadataItem.


        :param is_default: The is_default of this TagMetadataItem.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def name(self):
        """Gets the name of this TagMetadataItem.  # noqa: E501


        :return: The name of this TagMetadataItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TagMetadataItem.


        :param name: The name of this TagMetadataItem.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, TagMetadataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other