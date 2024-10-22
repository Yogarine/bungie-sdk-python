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


class DestinyTalentNode(object):
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
        'node_index': 'int',
        'node_hash': 'int',
        'state': 'int',
        'is_activated': 'bool',
        'step_index': 'int',
        'materials_to_upgrade': 'list[DestinyMaterialRequirement]',
        'activation_grid_level': 'int',
        'progress_percent': 'float',
        'hidden': 'bool',
        'node_stats_block': 'DestinyTalentNodeStatBlock'
    }

    attribute_map = {
        'node_index': 'nodeIndex',
        'node_hash': 'nodeHash',
        'state': 'state',
        'is_activated': 'isActivated',
        'step_index': 'stepIndex',
        'materials_to_upgrade': 'materialsToUpgrade',
        'activation_grid_level': 'activationGridLevel',
        'progress_percent': 'progressPercent',
        'hidden': 'hidden',
        'node_stats_block': 'nodeStatsBlock'
    }

    def __init__(self, node_index=None, node_hash=None, state=None, is_activated=None, step_index=None, materials_to_upgrade=None, activation_grid_level=None, progress_percent=None, hidden=None, node_stats_block=None):  # noqa: E501
        """DestinyTalentNode - a model defined in OpenAPI"""  # noqa: E501

        self._node_index = None
        self._node_hash = None
        self._state = None
        self._is_activated = None
        self._step_index = None
        self._materials_to_upgrade = None
        self._activation_grid_level = None
        self._progress_percent = None
        self._hidden = None
        self._node_stats_block = None
        self.discriminator = None

        if node_index is not None:
            self.node_index = node_index
        if node_hash is not None:
            self.node_hash = node_hash
        if state is not None:
            self.state = state
        if is_activated is not None:
            self.is_activated = is_activated
        if step_index is not None:
            self.step_index = step_index
        if materials_to_upgrade is not None:
            self.materials_to_upgrade = materials_to_upgrade
        if activation_grid_level is not None:
            self.activation_grid_level = activation_grid_level
        if progress_percent is not None:
            self.progress_percent = progress_percent
        if hidden is not None:
            self.hidden = hidden
        if node_stats_block is not None:
            self.node_stats_block = node_stats_block

    @property
    def node_index(self):
        """Gets the node_index of this DestinyTalentNode.  # noqa: E501

        The index of the Talent Node being referred to (an index into DestinyTalentGridDefinition.nodes[]). CONTENT VERSION DEPENDENT.  # noqa: E501

        :return: The node_index of this DestinyTalentNode.  # noqa: E501
        :rtype: int
        """
        return self._node_index

    @node_index.setter
    def node_index(self, node_index):
        """Sets the node_index of this DestinyTalentNode.

        The index of the Talent Node being referred to (an index into DestinyTalentGridDefinition.nodes[]). CONTENT VERSION DEPENDENT.  # noqa: E501

        :param node_index: The node_index of this DestinyTalentNode.  # noqa: E501
        :type: int
        """

        self._node_index = node_index

    @property
    def node_hash(self):
        """Gets the node_hash of this DestinyTalentNode.  # noqa: E501

        The hash of the Talent Node being referred to (in DestinyTalentGridDefinition.nodes). Deceptively CONTENT VERSION DEPENDENT. We have no guarantee of the hash's immutability between content versions.  # noqa: E501

        :return: The node_hash of this DestinyTalentNode.  # noqa: E501
        :rtype: int
        """
        return self._node_hash

    @node_hash.setter
    def node_hash(self, node_hash):
        """Sets the node_hash of this DestinyTalentNode.

        The hash of the Talent Node being referred to (in DestinyTalentGridDefinition.nodes). Deceptively CONTENT VERSION DEPENDENT. We have no guarantee of the hash's immutability between content versions.  # noqa: E501

        :param node_hash: The node_hash of this DestinyTalentNode.  # noqa: E501
        :type: int
        """

        self._node_hash = node_hash

    @property
    def state(self):
        """Gets the state of this DestinyTalentNode.  # noqa: E501

        An DestinyTalentNodeState enum value indicating the node's state: whether it can be activated or swapped, and why not if neither can be performed.  # noqa: E501

        :return: The state of this DestinyTalentNode.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DestinyTalentNode.

        An DestinyTalentNodeState enum value indicating the node's state: whether it can be activated or swapped, and why not if neither can be performed.  # noqa: E501

        :param state: The state of this DestinyTalentNode.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def is_activated(self):
        """Gets the is_activated of this DestinyTalentNode.  # noqa: E501

        If true, the node is activated: it's current step then provides its benefits.  # noqa: E501

        :return: The is_activated of this DestinyTalentNode.  # noqa: E501
        :rtype: bool
        """
        return self._is_activated

    @is_activated.setter
    def is_activated(self, is_activated):
        """Sets the is_activated of this DestinyTalentNode.

        If true, the node is activated: it's current step then provides its benefits.  # noqa: E501

        :param is_activated: The is_activated of this DestinyTalentNode.  # noqa: E501
        :type: bool
        """

        self._is_activated = is_activated

    @property
    def step_index(self):
        """Gets the step_index of this DestinyTalentNode.  # noqa: E501

        The currently relevant Step for the node. It is this step that has rendering data for the node and the benefits that are provided if the node is activated. (the actual rules for benefits provided are extremely complicated in theory, but with how Talent Grids are being used in Destiny 2 you don't have to worry about a lot of those old Destiny 1 rules.) This is an index into: DestinyTalentGridDefinition.nodes[nodeIndex].steps[stepIndex]  # noqa: E501

        :return: The step_index of this DestinyTalentNode.  # noqa: E501
        :rtype: int
        """
        return self._step_index

    @step_index.setter
    def step_index(self, step_index):
        """Sets the step_index of this DestinyTalentNode.

        The currently relevant Step for the node. It is this step that has rendering data for the node and the benefits that are provided if the node is activated. (the actual rules for benefits provided are extremely complicated in theory, but with how Talent Grids are being used in Destiny 2 you don't have to worry about a lot of those old Destiny 1 rules.) This is an index into: DestinyTalentGridDefinition.nodes[nodeIndex].steps[stepIndex]  # noqa: E501

        :param step_index: The step_index of this DestinyTalentNode.  # noqa: E501
        :type: int
        """

        self._step_index = step_index

    @property
    def materials_to_upgrade(self):
        """Gets the materials_to_upgrade of this DestinyTalentNode.  # noqa: E501

        If the node has material requirements to be activated, this is the list of those requirements.  # noqa: E501

        :return: The materials_to_upgrade of this DestinyTalentNode.  # noqa: E501
        :rtype: list[DestinyMaterialRequirement]
        """
        return self._materials_to_upgrade

    @materials_to_upgrade.setter
    def materials_to_upgrade(self, materials_to_upgrade):
        """Sets the materials_to_upgrade of this DestinyTalentNode.

        If the node has material requirements to be activated, this is the list of those requirements.  # noqa: E501

        :param materials_to_upgrade: The materials_to_upgrade of this DestinyTalentNode.  # noqa: E501
        :type: list[DestinyMaterialRequirement]
        """

        self._materials_to_upgrade = materials_to_upgrade

    @property
    def activation_grid_level(self):
        """Gets the activation_grid_level of this DestinyTalentNode.  # noqa: E501

        The progression level required on the Talent Grid in order to be able to activate this talent node. Talent Grids have their own Progression - similar to Character Level, but in this case it is experience related to the item itself.  # noqa: E501

        :return: The activation_grid_level of this DestinyTalentNode.  # noqa: E501
        :rtype: int
        """
        return self._activation_grid_level

    @activation_grid_level.setter
    def activation_grid_level(self, activation_grid_level):
        """Sets the activation_grid_level of this DestinyTalentNode.

        The progression level required on the Talent Grid in order to be able to activate this talent node. Talent Grids have their own Progression - similar to Character Level, but in this case it is experience related to the item itself.  # noqa: E501

        :param activation_grid_level: The activation_grid_level of this DestinyTalentNode.  # noqa: E501
        :type: int
        """

        self._activation_grid_level = activation_grid_level

    @property
    def progress_percent(self):
        """Gets the progress_percent of this DestinyTalentNode.  # noqa: E501

        If you want to show a progress bar or circle for how close this talent node is to being activate-able, this is the percentage to show. It follows the node's underlying rules about when the progress bar should first show up, and when it should be filled.  # noqa: E501

        :return: The progress_percent of this DestinyTalentNode.  # noqa: E501
        :rtype: float
        """
        return self._progress_percent

    @progress_percent.setter
    def progress_percent(self, progress_percent):
        """Sets the progress_percent of this DestinyTalentNode.

        If you want to show a progress bar or circle for how close this talent node is to being activate-able, this is the percentage to show. It follows the node's underlying rules about when the progress bar should first show up, and when it should be filled.  # noqa: E501

        :param progress_percent: The progress_percent of this DestinyTalentNode.  # noqa: E501
        :type: float
        """

        self._progress_percent = progress_percent

    @property
    def hidden(self):
        """Gets the hidden of this DestinyTalentNode.  # noqa: E501

        Whether or not the talent node is actually visible in the game's UI. Whether you want to show it in your own UI is up to you! I'm not gonna tell you who to sock it to.  # noqa: E501

        :return: The hidden of this DestinyTalentNode.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this DestinyTalentNode.

        Whether or not the talent node is actually visible in the game's UI. Whether you want to show it in your own UI is up to you! I'm not gonna tell you who to sock it to.  # noqa: E501

        :param hidden: The hidden of this DestinyTalentNode.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def node_stats_block(self):
        """Gets the node_stats_block of this DestinyTalentNode.  # noqa: E501

        This property has some history. A talent grid can provide stats on both the item it's related to and the character equipping the item. This returns data about those stat bonuses.  # noqa: E501

        :return: The node_stats_block of this DestinyTalentNode.  # noqa: E501
        :rtype: DestinyTalentNodeStatBlock
        """
        return self._node_stats_block

    @node_stats_block.setter
    def node_stats_block(self, node_stats_block):
        """Sets the node_stats_block of this DestinyTalentNode.

        This property has some history. A talent grid can provide stats on both the item it's related to and the character equipping the item. This returns data about those stat bonuses.  # noqa: E501

        :param node_stats_block: The node_stats_block of this DestinyTalentNode.  # noqa: E501
        :type: DestinyTalentNodeStatBlock
        """

        self._node_stats_block = node_stats_block

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
        if not isinstance(other, DestinyTalentNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
