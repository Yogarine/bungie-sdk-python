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


class DestinyPerkReference(object):
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
        'perk_hash': 'int',
        'icon_path': 'str',
        'is_active': 'bool',
        'visible': 'bool'
    }

    attribute_map = {
        'perk_hash': 'perkHash',
        'icon_path': 'iconPath',
        'is_active': 'isActive',
        'visible': 'visible'
    }

    def __init__(self, perk_hash=None, icon_path=None, is_active=None, visible=None):  # noqa: E501
        """DestinyPerkReference - a model defined in OpenAPI"""  # noqa: E501

        self._perk_hash = None
        self._icon_path = None
        self._is_active = None
        self._visible = None
        self.discriminator = None

        if perk_hash is not None:
            self.perk_hash = perk_hash
        if icon_path is not None:
            self.icon_path = icon_path
        if is_active is not None:
            self.is_active = is_active
        if visible is not None:
            self.visible = visible

    @property
    def perk_hash(self):
        """Gets the perk_hash of this DestinyPerkReference.  # noqa: E501

        The hash identifier for the perk, which can be used to look up DestinySandboxPerkDefinition if it exists. Be warned, perks frequently do not have user-viewable information. You should examine whether you actually found a name/description in the perk's definition before you show it to the user.  # noqa: E501

        :return: The perk_hash of this DestinyPerkReference.  # noqa: E501
        :rtype: int
        """
        return self._perk_hash

    @perk_hash.setter
    def perk_hash(self, perk_hash):
        """Sets the perk_hash of this DestinyPerkReference.

        The hash identifier for the perk, which can be used to look up DestinySandboxPerkDefinition if it exists. Be warned, perks frequently do not have user-viewable information. You should examine whether you actually found a name/description in the perk's definition before you show it to the user.  # noqa: E501

        :param perk_hash: The perk_hash of this DestinyPerkReference.  # noqa: E501
        :type: int
        """

        self._perk_hash = perk_hash

    @property
    def icon_path(self):
        """Gets the icon_path of this DestinyPerkReference.  # noqa: E501

        The icon for the perk.  # noqa: E501

        :return: The icon_path of this DestinyPerkReference.  # noqa: E501
        :rtype: str
        """
        return self._icon_path

    @icon_path.setter
    def icon_path(self, icon_path):
        """Sets the icon_path of this DestinyPerkReference.

        The icon for the perk.  # noqa: E501

        :param icon_path: The icon_path of this DestinyPerkReference.  # noqa: E501
        :type: str
        """

        self._icon_path = icon_path

    @property
    def is_active(self):
        """Gets the is_active of this DestinyPerkReference.  # noqa: E501

        Whether this perk is currently active. (We may return perks that you have not actually activated yet: these represent perks that you should show in the item's tooltip, but that the user has not yet activated.)  # noqa: E501

        :return: The is_active of this DestinyPerkReference.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this DestinyPerkReference.

        Whether this perk is currently active. (We may return perks that you have not actually activated yet: these represent perks that you should show in the item's tooltip, but that the user has not yet activated.)  # noqa: E501

        :param is_active: The is_active of this DestinyPerkReference.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def visible(self):
        """Gets the visible of this DestinyPerkReference.  # noqa: E501

        Some perks provide benefits, but aren't visible in the UI. This value will let you know if this is perk should be shown in your UI.  # noqa: E501

        :return: The visible of this DestinyPerkReference.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this DestinyPerkReference.

        Some perks provide benefits, but aren't visible in the UI. This value will let you know if this is perk should be shown in your UI.  # noqa: E501

        :param visible: The visible of this DestinyPerkReference.  # noqa: E501
        :type: bool
        """

        self._visible = visible

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
        if not isinstance(other, DestinyPerkReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
