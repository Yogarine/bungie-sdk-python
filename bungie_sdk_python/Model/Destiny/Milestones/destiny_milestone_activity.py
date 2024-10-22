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


class DestinyMilestoneActivity(object):
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
        'activity_hash': 'int',
        'activity_mode_hash': 'int',
        'activity_mode_type': 'int',
        'modifier_hashes': 'list[int]',
        'variants': 'list[DestinyMilestoneActivityVariant]'
    }

    attribute_map = {
        'activity_hash': 'activityHash',
        'activity_mode_hash': 'activityModeHash',
        'activity_mode_type': 'activityModeType',
        'modifier_hashes': 'modifierHashes',
        'variants': 'variants'
    }

    def __init__(self, activity_hash=None, activity_mode_hash=None, activity_mode_type=None, modifier_hashes=None, variants=None):  # noqa: E501
        """DestinyMilestoneActivity - a model defined in OpenAPI"""  # noqa: E501

        self._activity_hash = None
        self._activity_mode_hash = None
        self._activity_mode_type = None
        self._modifier_hashes = None
        self._variants = None
        self.discriminator = None

        if activity_hash is not None:
            self.activity_hash = activity_hash
        self.activity_mode_hash = activity_mode_hash
        self.activity_mode_type = activity_mode_type
        if modifier_hashes is not None:
            self.modifier_hashes = modifier_hashes
        if variants is not None:
            self.variants = variants

    @property
    def activity_hash(self):
        """Gets the activity_hash of this DestinyMilestoneActivity.  # noqa: E501

        The hash of an arbitrarily chosen variant of this activity. We'll go ahead and call that the \"canonical\" activity, because if you're using this value you should only use it for properties that are common across the variants: things like the name of the activity, it's location, etc... Use this hash to look up the DestinyActivityDefinition of this activity for rendering data.  # noqa: E501

        :return: The activity_hash of this DestinyMilestoneActivity.  # noqa: E501
        :rtype: int
        """
        return self._activity_hash

    @activity_hash.setter
    def activity_hash(self, activity_hash):
        """Sets the activity_hash of this DestinyMilestoneActivity.

        The hash of an arbitrarily chosen variant of this activity. We'll go ahead and call that the \"canonical\" activity, because if you're using this value you should only use it for properties that are common across the variants: things like the name of the activity, it's location, etc... Use this hash to look up the DestinyActivityDefinition of this activity for rendering data.  # noqa: E501

        :param activity_hash: The activity_hash of this DestinyMilestoneActivity.  # noqa: E501
        :type: int
        """

        self._activity_hash = activity_hash

    @property
    def activity_mode_hash(self):
        """Gets the activity_mode_hash of this DestinyMilestoneActivity.  # noqa: E501

        The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.  # noqa: E501

        :return: The activity_mode_hash of this DestinyMilestoneActivity.  # noqa: E501
        :rtype: int
        """
        return self._activity_mode_hash

    @activity_mode_hash.setter
    def activity_mode_hash(self, activity_mode_hash):
        """Sets the activity_mode_hash of this DestinyMilestoneActivity.

        The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.  # noqa: E501

        :param activity_mode_hash: The activity_mode_hash of this DestinyMilestoneActivity.  # noqa: E501
        :type: int
        """

        self._activity_mode_hash = activity_mode_hash

    @property
    def activity_mode_type(self):
        """Gets the activity_mode_type of this DestinyMilestoneActivity.  # noqa: E501

        The enumeration equivalent of the most specific Activity Mode under which this activity is played.  # noqa: E501

        :return: The activity_mode_type of this DestinyMilestoneActivity.  # noqa: E501
        :rtype: int
        """
        return self._activity_mode_type

    @activity_mode_type.setter
    def activity_mode_type(self, activity_mode_type):
        """Sets the activity_mode_type of this DestinyMilestoneActivity.

        The enumeration equivalent of the most specific Activity Mode under which this activity is played.  # noqa: E501

        :param activity_mode_type: The activity_mode_type of this DestinyMilestoneActivity.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]  # noqa: E501
        if activity_mode_type not in allowed_values:
            raise ValueError(
                "Invalid value for `activity_mode_type` ({0}), must be one of {1}"  # noqa: E501
                .format(activity_mode_type, allowed_values)
            )

        self._activity_mode_type = activity_mode_type

    @property
    def modifier_hashes(self):
        """Gets the modifier_hashes of this DestinyMilestoneActivity.  # noqa: E501

        If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data. Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.  # noqa: E501

        :return: The modifier_hashes of this DestinyMilestoneActivity.  # noqa: E501
        :rtype: list[int]
        """
        return self._modifier_hashes

    @modifier_hashes.setter
    def modifier_hashes(self, modifier_hashes):
        """Sets the modifier_hashes of this DestinyMilestoneActivity.

        If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data. Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.  # noqa: E501

        :param modifier_hashes: The modifier_hashes of this DestinyMilestoneActivity.  # noqa: E501
        :type: list[int]
        """

        self._modifier_hashes = modifier_hashes

    @property
    def variants(self):
        """Gets the variants of this DestinyMilestoneActivity.  # noqa: E501

        If you want more than just name/location/etc... you're going to have to dig into and show the variants of the conceptual activity. These will differ in seemingly arbitrary ways, like difficulty level and modifiers applied. Show it in whatever way tickles your fancy.  # noqa: E501

        :return: The variants of this DestinyMilestoneActivity.  # noqa: E501
        :rtype: list[DestinyMilestoneActivityVariant]
        """
        return self._variants

    @variants.setter
    def variants(self, variants):
        """Sets the variants of this DestinyMilestoneActivity.

        If you want more than just name/location/etc... you're going to have to dig into and show the variants of the conceptual activity. These will differ in seemingly arbitrary ways, like difficulty level and modifiers applied. Show it in whatever way tickles your fancy.  # noqa: E501

        :param variants: The variants of this DestinyMilestoneActivity.  # noqa: E501
        :type: list[DestinyMilestoneActivityVariant]
        """

        self._variants = variants

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
        if not isinstance(other, DestinyMilestoneActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
