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


class DestinyItemPreviewBlockDefinition(object):
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
        'screen_style': 'str',
        'preview_vendor_hash': 'int',
        'preview_action_string': 'str',
        'derived_item_categories': 'list[DestinyDerivedItemCategoryDefinition]'
    }

    attribute_map = {
        'screen_style': 'screenStyle',
        'preview_vendor_hash': 'previewVendorHash',
        'preview_action_string': 'previewActionString',
        'derived_item_categories': 'derivedItemCategories'
    }

    def __init__(self, screen_style=None, preview_vendor_hash=None, preview_action_string=None, derived_item_categories=None):  # noqa: E501
        """DestinyItemPreviewBlockDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._screen_style = None
        self._preview_vendor_hash = None
        self._preview_action_string = None
        self._derived_item_categories = None
        self.discriminator = None

        if screen_style is not None:
            self.screen_style = screen_style
        if preview_vendor_hash is not None:
            self.preview_vendor_hash = preview_vendor_hash
        if preview_action_string is not None:
            self.preview_action_string = preview_action_string
        if derived_item_categories is not None:
            self.derived_item_categories = derived_item_categories

    @property
    def screen_style(self):
        """Gets the screen_style of this DestinyItemPreviewBlockDefinition.  # noqa: E501

        A string that the game UI uses as a hint for which detail screen to show for the item. You, too, can leverage this for your own custom screen detail views. Note, however, that these are arbitrarily defined by designers: there's no guarantees of a fixed, known number of these - so fall back to something reasonable if you don't recognize it.  # noqa: E501

        :return: The screen_style of this DestinyItemPreviewBlockDefinition.  # noqa: E501
        :rtype: str
        """
        return self._screen_style

    @screen_style.setter
    def screen_style(self, screen_style):
        """Sets the screen_style of this DestinyItemPreviewBlockDefinition.

        A string that the game UI uses as a hint for which detail screen to show for the item. You, too, can leverage this for your own custom screen detail views. Note, however, that these are arbitrarily defined by designers: there's no guarantees of a fixed, known number of these - so fall back to something reasonable if you don't recognize it.  # noqa: E501

        :param screen_style: The screen_style of this DestinyItemPreviewBlockDefinition.  # noqa: E501
        :type: str
        """

        self._screen_style = screen_style

    @property
    def preview_vendor_hash(self):
        """Gets the preview_vendor_hash of this DestinyItemPreviewBlockDefinition.  # noqa: E501

        If the preview data is derived from a fake \"Preview\" Vendor, this will be the hash identifier for the DestinyVendorDefinition of that fake vendor.  # noqa: E501

        :return: The preview_vendor_hash of this DestinyItemPreviewBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._preview_vendor_hash

    @preview_vendor_hash.setter
    def preview_vendor_hash(self, preview_vendor_hash):
        """Sets the preview_vendor_hash of this DestinyItemPreviewBlockDefinition.

        If the preview data is derived from a fake \"Preview\" Vendor, this will be the hash identifier for the DestinyVendorDefinition of that fake vendor.  # noqa: E501

        :param preview_vendor_hash: The preview_vendor_hash of this DestinyItemPreviewBlockDefinition.  # noqa: E501
        :type: int
        """

        self._preview_vendor_hash = preview_vendor_hash

    @property
    def preview_action_string(self):
        """Gets the preview_action_string of this DestinyItemPreviewBlockDefinition.  # noqa: E501

        If the preview has an associated action (like \"Open\"), this will be the localized string for that action.  # noqa: E501

        :return: The preview_action_string of this DestinyItemPreviewBlockDefinition.  # noqa: E501
        :rtype: str
        """
        return self._preview_action_string

    @preview_action_string.setter
    def preview_action_string(self, preview_action_string):
        """Sets the preview_action_string of this DestinyItemPreviewBlockDefinition.

        If the preview has an associated action (like \"Open\"), this will be the localized string for that action.  # noqa: E501

        :param preview_action_string: The preview_action_string of this DestinyItemPreviewBlockDefinition.  # noqa: E501
        :type: str
        """

        self._preview_action_string = preview_action_string

    @property
    def derived_item_categories(self):
        """Gets the derived_item_categories of this DestinyItemPreviewBlockDefinition.  # noqa: E501

        This is a list of the items being previewed, categorized in the same way as they are in the preview UI.  # noqa: E501

        :return: The derived_item_categories of this DestinyItemPreviewBlockDefinition.  # noqa: E501
        :rtype: list[DestinyDerivedItemCategoryDefinition]
        """
        return self._derived_item_categories

    @derived_item_categories.setter
    def derived_item_categories(self, derived_item_categories):
        """Sets the derived_item_categories of this DestinyItemPreviewBlockDefinition.

        This is a list of the items being previewed, categorized in the same way as they are in the preview UI.  # noqa: E501

        :param derived_item_categories: The derived_item_categories of this DestinyItemPreviewBlockDefinition.  # noqa: E501
        :type: list[DestinyDerivedItemCategoryDefinition]
        """

        self._derived_item_categories = derived_item_categories

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
        if not isinstance(other, DestinyItemPreviewBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
