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


class DestinyMilestoneRewardCategoryDefinition(object):
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
        'category_hash': 'int',
        'category_identifier': 'str',
        'display_properties': 'DestinyDisplayPropertiesDefinition',
        'reward_entries': 'dict(str, DestinyMilestoneRewardEntryDefinition)',
        'order': 'int'
    }

    attribute_map = {
        'category_hash': 'categoryHash',
        'category_identifier': 'categoryIdentifier',
        'display_properties': 'displayProperties',
        'reward_entries': 'rewardEntries',
        'order': 'order'
    }

    def __init__(self, category_hash=None, category_identifier=None, display_properties=None, reward_entries=None, order=None):  # noqa: E501
        """DestinyMilestoneRewardCategoryDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._category_hash = None
        self._category_identifier = None
        self._display_properties = None
        self._reward_entries = None
        self._order = None
        self.discriminator = None

        if category_hash is not None:
            self.category_hash = category_hash
        if category_identifier is not None:
            self.category_identifier = category_identifier
        if display_properties is not None:
            self.display_properties = display_properties
        if reward_entries is not None:
            self.reward_entries = reward_entries
        if order is not None:
            self.order = order

    @property
    def category_hash(self):
        """Gets the category_hash of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501

        Identifies the reward category. Only guaranteed unique within this specific component!  # noqa: E501

        :return: The category_hash of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._category_hash

    @category_hash.setter
    def category_hash(self, category_hash):
        """Sets the category_hash of this DestinyMilestoneRewardCategoryDefinition.

        Identifies the reward category. Only guaranteed unique within this specific component!  # noqa: E501

        :param category_hash: The category_hash of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501
        :type: int
        """

        self._category_hash = category_hash

    @property
    def category_identifier(self):
        """Gets the category_identifier of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501

        The string identifier for the category, if you want to use it for some end. Guaranteed unique within the specific component.  # noqa: E501

        :return: The category_identifier of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501
        :rtype: str
        """
        return self._category_identifier

    @category_identifier.setter
    def category_identifier(self, category_identifier):
        """Sets the category_identifier of this DestinyMilestoneRewardCategoryDefinition.

        The string identifier for the category, if you want to use it for some end. Guaranteed unique within the specific component.  # noqa: E501

        :param category_identifier: The category_identifier of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501
        :type: str
        """

        self._category_identifier = category_identifier

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501

        Hopefully this is obvious by now.  # noqa: E501

        :return: The display_properties of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyMilestoneRewardCategoryDefinition.

        Hopefully this is obvious by now.  # noqa: E501

        :param display_properties: The display_properties of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def reward_entries(self):
        """Gets the reward_entries of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501

        If this milestone can provide rewards, this will define the sets of rewards that can be earned, the conditions under which they can be acquired, internal data that we'll use at runtime to determine whether you've already earned or redeemed this set of rewards, and the category that this reward should be placed under.  # noqa: E501

        :return: The reward_entries of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501
        :rtype: dict(str, DestinyMilestoneRewardEntryDefinition)
        """
        return self._reward_entries

    @reward_entries.setter
    def reward_entries(self, reward_entries):
        """Sets the reward_entries of this DestinyMilestoneRewardCategoryDefinition.

        If this milestone can provide rewards, this will define the sets of rewards that can be earned, the conditions under which they can be acquired, internal data that we'll use at runtime to determine whether you've already earned or redeemed this set of rewards, and the category that this reward should be placed under.  # noqa: E501

        :param reward_entries: The reward_entries of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501
        :type: dict(str, DestinyMilestoneRewardEntryDefinition)
        """

        self._reward_entries = reward_entries

    @property
    def order(self):
        """Gets the order of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501

        If you want to use BNet's recommended order for rendering categories programmatically, use this value and compare it to other categories to determine the order in which they should be rendered. I don't feel great about putting this here, I won't lie.  # noqa: E501

        :return: The order of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this DestinyMilestoneRewardCategoryDefinition.

        If you want to use BNet's recommended order for rendering categories programmatically, use this value and compare it to other categories to determine the order in which they should be rendered. I don't feel great about putting this here, I won't lie.  # noqa: E501

        :param order: The order of this DestinyMilestoneRewardCategoryDefinition.  # noqa: E501
        :type: int
        """

        self._order = order

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
        if not isinstance(other, DestinyMilestoneRewardCategoryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
