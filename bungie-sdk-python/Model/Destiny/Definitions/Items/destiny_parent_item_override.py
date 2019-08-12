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


class DestinyParentItemOverride(object):
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
        'additional_equip_requirements_display_strings': 'list[str]',
        'pip_icon': 'str'
    }

    attribute_map = {
        'additional_equip_requirements_display_strings': 'additionalEquipRequirementsDisplayStrings',
        'pip_icon': 'pipIcon'
    }

    def __init__(self, additional_equip_requirements_display_strings=None, pip_icon=None):  # noqa: E501
        """DestinyParentItemOverride - a model defined in OpenAPI"""  # noqa: E501

        self._additional_equip_requirements_display_strings = None
        self._pip_icon = None
        self.discriminator = None

        if additional_equip_requirements_display_strings is not None:
            self.additional_equip_requirements_display_strings = additional_equip_requirements_display_strings
        if pip_icon is not None:
            self.pip_icon = pip_icon

    @property
    def additional_equip_requirements_display_strings(self):
        """Gets the additional_equip_requirements_display_strings of this DestinyParentItemOverride.  # noqa: E501


        :return: The additional_equip_requirements_display_strings of this DestinyParentItemOverride.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_equip_requirements_display_strings

    @additional_equip_requirements_display_strings.setter
    def additional_equip_requirements_display_strings(self, additional_equip_requirements_display_strings):
        """Sets the additional_equip_requirements_display_strings of this DestinyParentItemOverride.


        :param additional_equip_requirements_display_strings: The additional_equip_requirements_display_strings of this DestinyParentItemOverride.  # noqa: E501
        :type: list[str]
        """

        self._additional_equip_requirements_display_strings = additional_equip_requirements_display_strings

    @property
    def pip_icon(self):
        """Gets the pip_icon of this DestinyParentItemOverride.  # noqa: E501


        :return: The pip_icon of this DestinyParentItemOverride.  # noqa: E501
        :rtype: str
        """
        return self._pip_icon

    @pip_icon.setter
    def pip_icon(self, pip_icon):
        """Sets the pip_icon of this DestinyParentItemOverride.


        :param pip_icon: The pip_icon of this DestinyParentItemOverride.  # noqa: E501
        :type: str
        """

        self._pip_icon = pip_icon

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
        if not isinstance(other, DestinyParentItemOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
