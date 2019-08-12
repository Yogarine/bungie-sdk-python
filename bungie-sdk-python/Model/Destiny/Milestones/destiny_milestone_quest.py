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


class DestinyMilestoneQuest(object):
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
        'quest_item_hash': 'int',
        'status': 'DestinyQuestStatus',
        'activity': 'DestinyMilestoneActivity',
        'challenges': 'list[DestinyChallengeStatus]'
    }

    attribute_map = {
        'quest_item_hash': 'questItemHash',
        'status': 'status',
        'activity': 'activity',
        'challenges': 'challenges'
    }

    def __init__(self, quest_item_hash=None, status=None, activity=None, challenges=None):  # noqa: E501
        """DestinyMilestoneQuest - a model defined in OpenAPI"""  # noqa: E501

        self._quest_item_hash = None
        self._status = None
        self._activity = None
        self._challenges = None
        self.discriminator = None

        if quest_item_hash is not None:
            self.quest_item_hash = quest_item_hash
        if status is not None:
            self.status = status
        if activity is not None:
            self.activity = activity
        if challenges is not None:
            self.challenges = challenges

    @property
    def quest_item_hash(self):
        """Gets the quest_item_hash of this DestinyMilestoneQuest.  # noqa: E501

        Quests are defined as Items in content. As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest. It will have pointers to all of the steps in the quest, and display information for the quest (title, description, icon etc) Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData property, and themselves are Items with their own renderable data.  # noqa: E501

        :return: The quest_item_hash of this DestinyMilestoneQuest.  # noqa: E501
        :rtype: int
        """
        return self._quest_item_hash

    @quest_item_hash.setter
    def quest_item_hash(self, quest_item_hash):
        """Sets the quest_item_hash of this DestinyMilestoneQuest.

        Quests are defined as Items in content. As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest. It will have pointers to all of the steps in the quest, and display information for the quest (title, description, icon etc) Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData property, and themselves are Items with their own renderable data.  # noqa: E501

        :param quest_item_hash: The quest_item_hash of this DestinyMilestoneQuest.  # noqa: E501
        :type: int
        """

        self._quest_item_hash = quest_item_hash

    @property
    def status(self):
        """Gets the status of this DestinyMilestoneQuest.  # noqa: E501

        The current status of the quest for the character making the request.  # noqa: E501

        :return: The status of this DestinyMilestoneQuest.  # noqa: E501
        :rtype: DestinyQuestStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DestinyMilestoneQuest.

        The current status of the quest for the character making the request.  # noqa: E501

        :param status: The status of this DestinyMilestoneQuest.  # noqa: E501
        :type: DestinyQuestStatus
        """

        self._status = status

    @property
    def activity(self):
        """Gets the activity of this DestinyMilestoneQuest.  # noqa: E501

        *IF* the Milestone has an active Activity that can give you greater details about what you need to do, it will be returned here. Remember to associate this with the DestinyMilestoneDefinition's activities to get details about the activity, including what specific quest it is related to if you have multiple quests to choose from.  # noqa: E501

        :return: The activity of this DestinyMilestoneQuest.  # noqa: E501
        :rtype: DestinyMilestoneActivity
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this DestinyMilestoneQuest.

        *IF* the Milestone has an active Activity that can give you greater details about what you need to do, it will be returned here. Remember to associate this with the DestinyMilestoneDefinition's activities to get details about the activity, including what specific quest it is related to if you have multiple quests to choose from.  # noqa: E501

        :param activity: The activity of this DestinyMilestoneQuest.  # noqa: E501
        :type: DestinyMilestoneActivity
        """

        self._activity = activity

    @property
    def challenges(self):
        """Gets the challenges of this DestinyMilestoneQuest.  # noqa: E501

        The activities referred to by this quest can have many associated challenges. They are all contained here, with activityHashes so that you can associate them with the specific activity variants in which they can be found. In retrospect, I probably should have put these under the specific Activity Variants, but it's too late to change it now. Theoretically, a quest without Activities can still have Challenges, which is why this is on a higher level than activity/variants, but it probably should have been in both places. That may come as a later revision.  # noqa: E501

        :return: The challenges of this DestinyMilestoneQuest.  # noqa: E501
        :rtype: list[DestinyChallengeStatus]
        """
        return self._challenges

    @challenges.setter
    def challenges(self, challenges):
        """Sets the challenges of this DestinyMilestoneQuest.

        The activities referred to by this quest can have many associated challenges. They are all contained here, with activityHashes so that you can associate them with the specific activity variants in which they can be found. In retrospect, I probably should have put these under the specific Activity Variants, but it's too late to change it now. Theoretically, a quest without Activities can still have Challenges, which is why this is on a higher level than activity/variants, but it probably should have been in both places. That may come as a later revision.  # noqa: E501

        :param challenges: The challenges of this DestinyMilestoneQuest.  # noqa: E501
        :type: list[DestinyChallengeStatus]
        """

        self._challenges = challenges

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
        if not isinstance(other, DestinyMilestoneQuest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
