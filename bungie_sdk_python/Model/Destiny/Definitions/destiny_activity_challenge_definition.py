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


class DestinyActivityChallengeDefinition(object):
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
        'objective_hash': 'int',
        'dummy_rewards': 'list[DestinyItemQuantity]'
    }

    attribute_map = {
        'objective_hash': 'objectiveHash',
        'dummy_rewards': 'dummyRewards'
    }

    def __init__(self, objective_hash=None, dummy_rewards=None):  # noqa: E501
        """DestinyActivityChallengeDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._objective_hash = None
        self._dummy_rewards = None
        self.discriminator = None

        if objective_hash is not None:
            self.objective_hash = objective_hash
        if dummy_rewards is not None:
            self.dummy_rewards = dummy_rewards

    @property
    def objective_hash(self):
        """Gets the objective_hash of this DestinyActivityChallengeDefinition.  # noqa: E501

        The hash for the Objective that matches this challenge. Use it to look up the DestinyObjectiveDefinition.  # noqa: E501

        :return: The objective_hash of this DestinyActivityChallengeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._objective_hash

    @objective_hash.setter
    def objective_hash(self, objective_hash):
        """Sets the objective_hash of this DestinyActivityChallengeDefinition.

        The hash for the Objective that matches this challenge. Use it to look up the DestinyObjectiveDefinition.  # noqa: E501

        :param objective_hash: The objective_hash of this DestinyActivityChallengeDefinition.  # noqa: E501
        :type: int
        """

        self._objective_hash = objective_hash

    @property
    def dummy_rewards(self):
        """Gets the dummy_rewards of this DestinyActivityChallengeDefinition.  # noqa: E501

        The rewards as they're represented in the UI. Note that they generally link to \"dummy\" items that give a summary of rewards rather than direct, real items themselves.  If the quantity is 0, don't show the quantity.  # noqa: E501

        :return: The dummy_rewards of this DestinyActivityChallengeDefinition.  # noqa: E501
        :rtype: list[DestinyItemQuantity]
        """
        return self._dummy_rewards

    @dummy_rewards.setter
    def dummy_rewards(self, dummy_rewards):
        """Sets the dummy_rewards of this DestinyActivityChallengeDefinition.

        The rewards as they're represented in the UI. Note that they generally link to \"dummy\" items that give a summary of rewards rather than direct, real items themselves.  If the quantity is 0, don't show the quantity.  # noqa: E501

        :param dummy_rewards: The dummy_rewards of this DestinyActivityChallengeDefinition.  # noqa: E501
        :type: list[DestinyItemQuantity]
        """

        self._dummy_rewards = dummy_rewards

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
        if not isinstance(other, DestinyActivityChallengeDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other