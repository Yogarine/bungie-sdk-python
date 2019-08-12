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


class DestinyMilestoneDefinition(object):
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
        'image': 'str',
        'milestone_type': 'int',
        'recruitable': 'bool',
        'friendly_name': 'str',
        'show_in_explorer': 'bool',
        'show_in_milestones': 'bool',
        'explore_prioritizes_activity_image': 'bool',
        'has_predictable_dates': 'bool',
        'quests': 'dict(str, DestinyMilestoneQuestDefinition)',
        'rewards': 'dict(str, DestinyMilestoneRewardCategoryDefinition)',
        'vendors_display_title': 'str',
        'vendors': 'list[DestinyMilestoneVendorDefinition]',
        'values': 'dict(str, DestinyMilestoneValueDefinition)',
        'is_in_game_milestone': 'bool',
        'activities': 'list[DestinyMilestoneChallengeActivityDefinition]',
        'default_order': 'int',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'image': 'image',
        'milestone_type': 'milestoneType',
        'recruitable': 'recruitable',
        'friendly_name': 'friendlyName',
        'show_in_explorer': 'showInExplorer',
        'show_in_milestones': 'showInMilestones',
        'explore_prioritizes_activity_image': 'explorePrioritizesActivityImage',
        'has_predictable_dates': 'hasPredictableDates',
        'quests': 'quests',
        'rewards': 'rewards',
        'vendors_display_title': 'vendorsDisplayTitle',
        'vendors': 'vendors',
        'values': 'values',
        'is_in_game_milestone': 'isInGameMilestone',
        'activities': 'activities',
        'default_order': 'defaultOrder',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, image=None, milestone_type=None, recruitable=None, friendly_name=None, show_in_explorer=None, show_in_milestones=None, explore_prioritizes_activity_image=None, has_predictable_dates=None, quests=None, rewards=None, vendors_display_title=None, vendors=None, values=None, is_in_game_milestone=None, activities=None, default_order=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyMilestoneDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._display_properties = None
        self._image = None
        self._milestone_type = None
        self._recruitable = None
        self._friendly_name = None
        self._show_in_explorer = None
        self._show_in_milestones = None
        self._explore_prioritizes_activity_image = None
        self._has_predictable_dates = None
        self._quests = None
        self._rewards = None
        self._vendors_display_title = None
        self._vendors = None
        self._values = None
        self._is_in_game_milestone = None
        self._activities = None
        self._default_order = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
            self.display_properties = display_properties
        if image is not None:
            self.image = image
        if milestone_type is not None:
            self.milestone_type = milestone_type
        if recruitable is not None:
            self.recruitable = recruitable
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if show_in_explorer is not None:
            self.show_in_explorer = show_in_explorer
        if show_in_milestones is not None:
            self.show_in_milestones = show_in_milestones
        if explore_prioritizes_activity_image is not None:
            self.explore_prioritizes_activity_image = explore_prioritizes_activity_image
        if has_predictable_dates is not None:
            self.has_predictable_dates = has_predictable_dates
        if quests is not None:
            self.quests = quests
        if rewards is not None:
            self.rewards = rewards
        if vendors_display_title is not None:
            self.vendors_display_title = vendors_display_title
        if vendors is not None:
            self.vendors = vendors
        if values is not None:
            self.values = values
        if is_in_game_milestone is not None:
            self.is_in_game_milestone = is_in_game_milestone
        if activities is not None:
            self.activities = activities
        if default_order is not None:
            self.default_order = default_order
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyMilestoneDefinition.  # noqa: E501


        :return: The display_properties of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyMilestoneDefinition.


        :param display_properties: The display_properties of this DestinyMilestoneDefinition.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def image(self):
        """Gets the image of this DestinyMilestoneDefinition.  # noqa: E501

        A custom image someone made just for the milestone. Isn't that special?  # noqa: E501

        :return: The image of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this DestinyMilestoneDefinition.

        A custom image someone made just for the milestone. Isn't that special?  # noqa: E501

        :param image: The image of this DestinyMilestoneDefinition.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def milestone_type(self):
        """Gets the milestone_type of this DestinyMilestoneDefinition.  # noqa: E501

        An enumeration listing one of the possible types of milestones. Check out the DestinyMilestoneType enum for more info!  # noqa: E501

        :return: The milestone_type of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: int
        """
        return self._milestone_type

    @milestone_type.setter
    def milestone_type(self, milestone_type):
        """Sets the milestone_type of this DestinyMilestoneDefinition.

        An enumeration listing one of the possible types of milestones. Check out the DestinyMilestoneType enum for more info!  # noqa: E501

        :param milestone_type: The milestone_type of this DestinyMilestoneDefinition.  # noqa: E501
        :type: int
        """

        self._milestone_type = milestone_type

    @property
    def recruitable(self):
        """Gets the recruitable of this DestinyMilestoneDefinition.  # noqa: E501

        If True, then the Milestone has been integrated with BNet's recruiting feature.  # noqa: E501

        :return: The recruitable of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._recruitable

    @recruitable.setter
    def recruitable(self, recruitable):
        """Sets the recruitable of this DestinyMilestoneDefinition.

        If True, then the Milestone has been integrated with BNet's recruiting feature.  # noqa: E501

        :param recruitable: The recruitable of this DestinyMilestoneDefinition.  # noqa: E501
        :type: bool
        """

        self._recruitable = recruitable

    @property
    def friendly_name(self):
        """Gets the friendly_name of this DestinyMilestoneDefinition.  # noqa: E501

        If the milestone has a friendly identifier for association with other features - such as Recruiting - that identifier can be found here. This is \"friendly\" in that it looks better in a URL than whatever the identifier for the Milestone actually is.  # noqa: E501

        :return: The friendly_name of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this DestinyMilestoneDefinition.

        If the milestone has a friendly identifier for association with other features - such as Recruiting - that identifier can be found here. This is \"friendly\" in that it looks better in a URL than whatever the identifier for the Milestone actually is.  # noqa: E501

        :param friendly_name: The friendly_name of this DestinyMilestoneDefinition.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def show_in_explorer(self):
        """Gets the show_in_explorer of this DestinyMilestoneDefinition.  # noqa: E501

        If TRUE, this entry should be returned in the list of milestones for the \"Explore Destiny\" (i.e. new BNet homepage) features of Bungie.net (as long as the underlying event is active) Note that this is a property specifically used by BNet and the companion app for the \"Live Events\" feature of the front page/welcome view: it's not a reflection of what you see in-game.  # noqa: E501

        :return: The show_in_explorer of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_explorer

    @show_in_explorer.setter
    def show_in_explorer(self, show_in_explorer):
        """Sets the show_in_explorer of this DestinyMilestoneDefinition.

        If TRUE, this entry should be returned in the list of milestones for the \"Explore Destiny\" (i.e. new BNet homepage) features of Bungie.net (as long as the underlying event is active) Note that this is a property specifically used by BNet and the companion app for the \"Live Events\" feature of the front page/welcome view: it's not a reflection of what you see in-game.  # noqa: E501

        :param show_in_explorer: The show_in_explorer of this DestinyMilestoneDefinition.  # noqa: E501
        :type: bool
        """

        self._show_in_explorer = show_in_explorer

    @property
    def show_in_milestones(self):
        """Gets the show_in_milestones of this DestinyMilestoneDefinition.  # noqa: E501

        Determines whether we'll show this Milestone in the user's personal Milestones list.  # noqa: E501

        :return: The show_in_milestones of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_milestones

    @show_in_milestones.setter
    def show_in_milestones(self, show_in_milestones):
        """Sets the show_in_milestones of this DestinyMilestoneDefinition.

        Determines whether we'll show this Milestone in the user's personal Milestones list.  # noqa: E501

        :param show_in_milestones: The show_in_milestones of this DestinyMilestoneDefinition.  # noqa: E501
        :type: bool
        """

        self._show_in_milestones = show_in_milestones

    @property
    def explore_prioritizes_activity_image(self):
        """Gets the explore_prioritizes_activity_image of this DestinyMilestoneDefinition.  # noqa: E501

        If TRUE, \"Explore Destiny\" (the front page of BNet and the companion app) prioritize using the activity image over any overriding Quest or Milestone image provided. This unfortunate hack is brought to you by Trials of The Nine.  # noqa: E501

        :return: The explore_prioritizes_activity_image of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._explore_prioritizes_activity_image

    @explore_prioritizes_activity_image.setter
    def explore_prioritizes_activity_image(self, explore_prioritizes_activity_image):
        """Sets the explore_prioritizes_activity_image of this DestinyMilestoneDefinition.

        If TRUE, \"Explore Destiny\" (the front page of BNet and the companion app) prioritize using the activity image over any overriding Quest or Milestone image provided. This unfortunate hack is brought to you by Trials of The Nine.  # noqa: E501

        :param explore_prioritizes_activity_image: The explore_prioritizes_activity_image of this DestinyMilestoneDefinition.  # noqa: E501
        :type: bool
        """

        self._explore_prioritizes_activity_image = explore_prioritizes_activity_image

    @property
    def has_predictable_dates(self):
        """Gets the has_predictable_dates of this DestinyMilestoneDefinition.  # noqa: E501

        A shortcut for clients - and the server - to understand whether we can predict the start and end dates for this event. In practice, there are multiple ways that an event could have predictable date ranges, but not all events will be able to be predicted via any mechanism (for instance, events that are manually triggered on and off)  # noqa: E501

        :return: The has_predictable_dates of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._has_predictable_dates

    @has_predictable_dates.setter
    def has_predictable_dates(self, has_predictable_dates):
        """Sets the has_predictable_dates of this DestinyMilestoneDefinition.

        A shortcut for clients - and the server - to understand whether we can predict the start and end dates for this event. In practice, there are multiple ways that an event could have predictable date ranges, but not all events will be able to be predicted via any mechanism (for instance, events that are manually triggered on and off)  # noqa: E501

        :param has_predictable_dates: The has_predictable_dates of this DestinyMilestoneDefinition.  # noqa: E501
        :type: bool
        """

        self._has_predictable_dates = has_predictable_dates

    @property
    def quests(self):
        """Gets the quests of this DestinyMilestoneDefinition.  # noqa: E501

        The full set of possible Quests that give the overview of the Milestone event/activity in question. Only one of these can be active at a time for a given Conceptual Milestone, but many of them may be \"available\" for the user to choose from. (for instance, with Milestones you can choose from the three available Quests, but only one can be active at a time) Keyed by the quest item.  As of Forsaken (~September 2018), Quest-style Milestones are being removed for many types of activities. There will likely be further revisions to the Milestone concept in the future.  # noqa: E501

        :return: The quests of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: dict(str, DestinyMilestoneQuestDefinition)
        """
        return self._quests

    @quests.setter
    def quests(self, quests):
        """Sets the quests of this DestinyMilestoneDefinition.

        The full set of possible Quests that give the overview of the Milestone event/activity in question. Only one of these can be active at a time for a given Conceptual Milestone, but many of them may be \"available\" for the user to choose from. (for instance, with Milestones you can choose from the three available Quests, but only one can be active at a time) Keyed by the quest item.  As of Forsaken (~September 2018), Quest-style Milestones are being removed for many types of activities. There will likely be further revisions to the Milestone concept in the future.  # noqa: E501

        :param quests: The quests of this DestinyMilestoneDefinition.  # noqa: E501
        :type: dict(str, DestinyMilestoneQuestDefinition)
        """

        self._quests = quests

    @property
    def rewards(self):
        """Gets the rewards of this DestinyMilestoneDefinition.  # noqa: E501

        If this milestone can provide rewards, this will define the categories into which the individual reward entries are placed.  This is keyed by the Category's hash, which is only guaranteed to be unique within a given Milestone.  # noqa: E501

        :return: The rewards of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: dict(str, DestinyMilestoneRewardCategoryDefinition)
        """
        return self._rewards

    @rewards.setter
    def rewards(self, rewards):
        """Sets the rewards of this DestinyMilestoneDefinition.

        If this milestone can provide rewards, this will define the categories into which the individual reward entries are placed.  This is keyed by the Category's hash, which is only guaranteed to be unique within a given Milestone.  # noqa: E501

        :param rewards: The rewards of this DestinyMilestoneDefinition.  # noqa: E501
        :type: dict(str, DestinyMilestoneRewardCategoryDefinition)
        """

        self._rewards = rewards

    @property
    def vendors_display_title(self):
        """Gets the vendors_display_title of this DestinyMilestoneDefinition.  # noqa: E501

        If you're going to show Vendors for the Milestone, you can use this as a localized \"header\" for the section where you show that vendor data. It'll provide a more context-relevant clue about what the vendor's role is in the Milestone.  # noqa: E501

        :return: The vendors_display_title of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: str
        """
        return self._vendors_display_title

    @vendors_display_title.setter
    def vendors_display_title(self, vendors_display_title):
        """Sets the vendors_display_title of this DestinyMilestoneDefinition.

        If you're going to show Vendors for the Milestone, you can use this as a localized \"header\" for the section where you show that vendor data. It'll provide a more context-relevant clue about what the vendor's role is in the Milestone.  # noqa: E501

        :param vendors_display_title: The vendors_display_title of this DestinyMilestoneDefinition.  # noqa: E501
        :type: str
        """

        self._vendors_display_title = vendors_display_title

    @property
    def vendors(self):
        """Gets the vendors of this DestinyMilestoneDefinition.  # noqa: E501

        Sometimes, milestones will have rewards provided by Vendors. This definition gives the information needed to understand which vendors are relevant, the order in which they should be returned if order matters, and the conditions under which the Vendor is relevant to the user.  # noqa: E501

        :return: The vendors of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: list[DestinyMilestoneVendorDefinition]
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        """Sets the vendors of this DestinyMilestoneDefinition.

        Sometimes, milestones will have rewards provided by Vendors. This definition gives the information needed to understand which vendors are relevant, the order in which they should be returned if order matters, and the conditions under which the Vendor is relevant to the user.  # noqa: E501

        :param vendors: The vendors of this DestinyMilestoneDefinition.  # noqa: E501
        :type: list[DestinyMilestoneVendorDefinition]
        """

        self._vendors = vendors

    @property
    def values(self):
        """Gets the values of this DestinyMilestoneDefinition.  # noqa: E501

        Sometimes, milestones will have arbitrary values associated with them that are of interest to us or to third party developers. This is the collection of those values' definitions, keyed by the identifier of the value and providing useful definition information such as localizable names and descriptions for the value.  # noqa: E501

        :return: The values of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: dict(str, DestinyMilestoneValueDefinition)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this DestinyMilestoneDefinition.

        Sometimes, milestones will have arbitrary values associated with them that are of interest to us or to third party developers. This is the collection of those values' definitions, keyed by the identifier of the value and providing useful definition information such as localizable names and descriptions for the value.  # noqa: E501

        :param values: The values of this DestinyMilestoneDefinition.  # noqa: E501
        :type: dict(str, DestinyMilestoneValueDefinition)
        """

        self._values = values

    @property
    def is_in_game_milestone(self):
        """Gets the is_in_game_milestone of this DestinyMilestoneDefinition.  # noqa: E501

        Some milestones are explicit objectives that you can see and interact with in the game. Some milestones are more conceptual, built by BNet to help advise you on activities and events that happen in-game but that aren't explicitly shown in game as Milestones. If this is TRUE, you can see this as a milestone in the game. If this is FALSE, it's an event or activity you can participate in, but you won't see it as a Milestone in the game's UI.  # noqa: E501

        :return: The is_in_game_milestone of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_game_milestone

    @is_in_game_milestone.setter
    def is_in_game_milestone(self, is_in_game_milestone):
        """Sets the is_in_game_milestone of this DestinyMilestoneDefinition.

        Some milestones are explicit objectives that you can see and interact with in the game. Some milestones are more conceptual, built by BNet to help advise you on activities and events that happen in-game but that aren't explicitly shown in game as Milestones. If this is TRUE, you can see this as a milestone in the game. If this is FALSE, it's an event or activity you can participate in, but you won't see it as a Milestone in the game's UI.  # noqa: E501

        :param is_in_game_milestone: The is_in_game_milestone of this DestinyMilestoneDefinition.  # noqa: E501
        :type: bool
        """

        self._is_in_game_milestone = is_in_game_milestone

    @property
    def activities(self):
        """Gets the activities of this DestinyMilestoneDefinition.  # noqa: E501

        A Milestone can now be represented by one or more activities directly (without a backing Quest), and that activity can have many challenges, modifiers, and related to it.  # noqa: E501

        :return: The activities of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: list[DestinyMilestoneChallengeActivityDefinition]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this DestinyMilestoneDefinition.

        A Milestone can now be represented by one or more activities directly (without a backing Quest), and that activity can have many challenges, modifiers, and related to it.  # noqa: E501

        :param activities: The activities of this DestinyMilestoneDefinition.  # noqa: E501
        :type: list[DestinyMilestoneChallengeActivityDefinition]
        """

        self._activities = activities

    @property
    def default_order(self):
        """Gets the default_order of this DestinyMilestoneDefinition.  # noqa: E501


        :return: The default_order of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: int
        """
        return self._default_order

    @default_order.setter
    def default_order(self, default_order):
        """Sets the default_order of this DestinyMilestoneDefinition.


        :param default_order: The default_order of this DestinyMilestoneDefinition.  # noqa: E501
        :type: int
        """

        self._default_order = default_order

    @property
    def hash(self):
        """Gets the hash of this DestinyMilestoneDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyMilestoneDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyMilestoneDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyMilestoneDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyMilestoneDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyMilestoneDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyMilestoneDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyMilestoneDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyMilestoneDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyMilestoneDefinition.  # noqa: E501
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
        if not isinstance(other, DestinyMilestoneDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
