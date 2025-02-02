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


class DestinyPublicMilestoneChallengeActivity(object):
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
        'challenge_objective_hashes': 'list[int]',
        'modifier_hashes': 'list[int]',
        'loadout_requirement_index': 'int',
        'phase_hashes': 'list[int]',
        'boolean_activity_options': 'dict(str, bool)'
    }

    attribute_map = {
        'activity_hash': 'activityHash',
        'challenge_objective_hashes': 'challengeObjectiveHashes',
        'modifier_hashes': 'modifierHashes',
        'loadout_requirement_index': 'loadoutRequirementIndex',
        'phase_hashes': 'phaseHashes',
        'boolean_activity_options': 'booleanActivityOptions'
    }

    def __init__(self, activity_hash=None, challenge_objective_hashes=None, modifier_hashes=None, loadout_requirement_index=None, phase_hashes=None, boolean_activity_options=None):  # noqa: E501
        """DestinyPublicMilestoneChallengeActivity - a model defined in OpenAPI"""  # noqa: E501

        self._activity_hash = None
        self._challenge_objective_hashes = None
        self._modifier_hashes = None
        self._loadout_requirement_index = None
        self._phase_hashes = None
        self._boolean_activity_options = None
        self.discriminator = None

        if activity_hash is not None:
            self.activity_hash = activity_hash
        if challenge_objective_hashes is not None:
            self.challenge_objective_hashes = challenge_objective_hashes
        if modifier_hashes is not None:
            self.modifier_hashes = modifier_hashes
        self.loadout_requirement_index = loadout_requirement_index
        if phase_hashes is not None:
            self.phase_hashes = phase_hashes
        if boolean_activity_options is not None:
            self.boolean_activity_options = boolean_activity_options

    @property
    def activity_hash(self):
        """Gets the activity_hash of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501


        :return: The activity_hash of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :rtype: int
        """
        return self._activity_hash

    @activity_hash.setter
    def activity_hash(self, activity_hash):
        """Sets the activity_hash of this DestinyPublicMilestoneChallengeActivity.


        :param activity_hash: The activity_hash of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :type: int
        """

        self._activity_hash = activity_hash

    @property
    def challenge_objective_hashes(self):
        """Gets the challenge_objective_hashes of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501


        :return: The challenge_objective_hashes of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :rtype: list[int]
        """
        return self._challenge_objective_hashes

    @challenge_objective_hashes.setter
    def challenge_objective_hashes(self, challenge_objective_hashes):
        """Sets the challenge_objective_hashes of this DestinyPublicMilestoneChallengeActivity.


        :param challenge_objective_hashes: The challenge_objective_hashes of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :type: list[int]
        """

        self._challenge_objective_hashes = challenge_objective_hashes

    @property
    def modifier_hashes(self):
        """Gets the modifier_hashes of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501

        If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data.  Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.  # noqa: E501

        :return: The modifier_hashes of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :rtype: list[int]
        """
        return self._modifier_hashes

    @modifier_hashes.setter
    def modifier_hashes(self, modifier_hashes):
        """Sets the modifier_hashes of this DestinyPublicMilestoneChallengeActivity.

        If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data.  Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.  # noqa: E501

        :param modifier_hashes: The modifier_hashes of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :type: list[int]
        """

        self._modifier_hashes = modifier_hashes

    @property
    def loadout_requirement_index(self):
        """Gets the loadout_requirement_index of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501

        If returned, this is the index into the DestinyActivityDefinition's \"loadouts\" property, indicating the currently active loadout requirements.  # noqa: E501

        :return: The loadout_requirement_index of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :rtype: int
        """
        return self._loadout_requirement_index

    @loadout_requirement_index.setter
    def loadout_requirement_index(self, loadout_requirement_index):
        """Sets the loadout_requirement_index of this DestinyPublicMilestoneChallengeActivity.

        If returned, this is the index into the DestinyActivityDefinition's \"loadouts\" property, indicating the currently active loadout requirements.  # noqa: E501

        :param loadout_requirement_index: The loadout_requirement_index of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :type: int
        """

        self._loadout_requirement_index = loadout_requirement_index

    @property
    def phase_hashes(self):
        """Gets the phase_hashes of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501

        The ordered list of phases for this activity, if any. Note that we have no human readable info for phases, nor any entities to relate them to: relating these hashes to something human readable is up to you unfortunately.  # noqa: E501

        :return: The phase_hashes of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :rtype: list[int]
        """
        return self._phase_hashes

    @phase_hashes.setter
    def phase_hashes(self, phase_hashes):
        """Sets the phase_hashes of this DestinyPublicMilestoneChallengeActivity.

        The ordered list of phases for this activity, if any. Note that we have no human readable info for phases, nor any entities to relate them to: relating these hashes to something human readable is up to you unfortunately.  # noqa: E501

        :param phase_hashes: The phase_hashes of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :type: list[int]
        """

        self._phase_hashes = phase_hashes

    @property
    def boolean_activity_options(self):
        """Gets the boolean_activity_options of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501

        The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique).  As a concrete example of this data, the hashes you get for Raids will correspond to the currently active \"Challenge Mode\".  We have no human readable information for this data, so it's up to you if you want to associate it with such info to show it.  # noqa: E501

        :return: The boolean_activity_options of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._boolean_activity_options

    @boolean_activity_options.setter
    def boolean_activity_options(self, boolean_activity_options):
        """Sets the boolean_activity_options of this DestinyPublicMilestoneChallengeActivity.

        The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique).  As a concrete example of this data, the hashes you get for Raids will correspond to the currently active \"Challenge Mode\".  We have no human readable information for this data, so it's up to you if you want to associate it with such info to show it.  # noqa: E501

        :param boolean_activity_options: The boolean_activity_options of this DestinyPublicMilestoneChallengeActivity.  # noqa: E501
        :type: dict(str, bool)
        """

        self._boolean_activity_options = boolean_activity_options

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
        if not isinstance(other, DestinyPublicMilestoneChallengeActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
