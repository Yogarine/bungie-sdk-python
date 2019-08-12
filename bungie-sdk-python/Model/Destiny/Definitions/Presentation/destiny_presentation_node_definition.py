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


class DestinyPresentationNodeDefinition(object):
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
        'original_icon': 'str',
        'root_view_icon': 'str',
        'node_type': 'int',
        'scope': 'int',
        'objective_hash': 'int',
        'completion_record_hash': 'int',
        'children': 'DestinyPresentationNodeChildrenBlock',
        'display_style': 'int',
        'screen_style': 'int',
        'requirements': 'DestinyPresentationNodeRequirementsBlock',
        'disable_child_subscreen_navigation': 'bool',
        'parent_node_hashes': 'list[int]',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'original_icon': 'originalIcon',
        'root_view_icon': 'rootViewIcon',
        'node_type': 'nodeType',
        'scope': 'scope',
        'objective_hash': 'objectiveHash',
        'completion_record_hash': 'completionRecordHash',
        'children': 'children',
        'display_style': 'displayStyle',
        'screen_style': 'screenStyle',
        'requirements': 'requirements',
        'disable_child_subscreen_navigation': 'disableChildSubscreenNavigation',
        'parent_node_hashes': 'parentNodeHashes',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, original_icon=None, root_view_icon=None, node_type=None, scope=None, objective_hash=None, completion_record_hash=None, children=None, display_style=None, screen_style=None, requirements=None, disable_child_subscreen_navigation=None, parent_node_hashes=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyPresentationNodeDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._display_properties = None
        self._original_icon = None
        self._root_view_icon = None
        self._node_type = None
        self._scope = None
        self._objective_hash = None
        self._completion_record_hash = None
        self._children = None
        self._display_style = None
        self._screen_style = None
        self._requirements = None
        self._disable_child_subscreen_navigation = None
        self._parent_node_hashes = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
            self.display_properties = display_properties
        if original_icon is not None:
            self.original_icon = original_icon
        if root_view_icon is not None:
            self.root_view_icon = root_view_icon
        if node_type is not None:
            self.node_type = node_type
        if scope is not None:
            self.scope = scope
        self.objective_hash = objective_hash
        self.completion_record_hash = completion_record_hash
        if children is not None:
            self.children = children
        if display_style is not None:
            self.display_style = display_style
        if screen_style is not None:
            self.screen_style = screen_style
        if requirements is not None:
            self.requirements = requirements
        if disable_child_subscreen_navigation is not None:
            self.disable_child_subscreen_navigation = disable_child_subscreen_navigation
        if parent_node_hashes is not None:
            self.parent_node_hashes = parent_node_hashes
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyPresentationNodeDefinition.  # noqa: E501


        :return: The display_properties of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyPresentationNodeDefinition.


        :param display_properties: The display_properties of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def original_icon(self):
        """Gets the original_icon of this DestinyPresentationNodeDefinition.  # noqa: E501

        The original icon for this presentation node, before we futzed with it.  # noqa: E501

        :return: The original_icon of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._original_icon

    @original_icon.setter
    def original_icon(self, original_icon):
        """Sets the original_icon of this DestinyPresentationNodeDefinition.

        The original icon for this presentation node, before we futzed with it.  # noqa: E501

        :param original_icon: The original_icon of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: str
        """

        self._original_icon = original_icon

    @property
    def root_view_icon(self):
        """Gets the root_view_icon of this DestinyPresentationNodeDefinition.  # noqa: E501

        Some presentation nodes are meant to be explicitly shown on the \"root\" or \"entry\" screens for the feature to which they are related. You should use this icon when showing them on such a view, if you have a similar \"entry point\" view in your UI. If you don't have a UI, then I guess it doesn't matter either way does it?  # noqa: E501

        :return: The root_view_icon of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._root_view_icon

    @root_view_icon.setter
    def root_view_icon(self, root_view_icon):
        """Sets the root_view_icon of this DestinyPresentationNodeDefinition.

        Some presentation nodes are meant to be explicitly shown on the \"root\" or \"entry\" screens for the feature to which they are related. You should use this icon when showing them on such a view, if you have a similar \"entry point\" view in your UI. If you don't have a UI, then I guess it doesn't matter either way does it?  # noqa: E501

        :param root_view_icon: The root_view_icon of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: str
        """

        self._root_view_icon = root_view_icon

    @property
    def node_type(self):
        """Gets the node_type of this DestinyPresentationNodeDefinition.  # noqa: E501


        :return: The node_type of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this DestinyPresentationNodeDefinition.


        :param node_type: The node_type of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: int
        """

        self._node_type = node_type

    @property
    def scope(self):
        """Gets the scope of this DestinyPresentationNodeDefinition.  # noqa: E501

        Indicates whether this presentation node's state is determined on a per-character or on an account-wide basis.  # noqa: E501

        :return: The scope of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this DestinyPresentationNodeDefinition.

        Indicates whether this presentation node's state is determined on a per-character or on an account-wide basis.  # noqa: E501

        :param scope: The scope of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: int
        """

        self._scope = scope

    @property
    def objective_hash(self):
        """Gets the objective_hash of this DestinyPresentationNodeDefinition.  # noqa: E501

        If this presentation node shows a related objective (for instance, if it tracks the progress of its children), the objective being tracked is indicated here.  # noqa: E501

        :return: The objective_hash of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._objective_hash

    @objective_hash.setter
    def objective_hash(self, objective_hash):
        """Sets the objective_hash of this DestinyPresentationNodeDefinition.

        If this presentation node shows a related objective (for instance, if it tracks the progress of its children), the objective being tracked is indicated here.  # noqa: E501

        :param objective_hash: The objective_hash of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: int
        """

        self._objective_hash = objective_hash

    @property
    def completion_record_hash(self):
        """Gets the completion_record_hash of this DestinyPresentationNodeDefinition.  # noqa: E501

        If this presentation node has an associated \"Record\" that you can accomplish for completing its children, this is the identifier of that Record.  # noqa: E501

        :return: The completion_record_hash of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._completion_record_hash

    @completion_record_hash.setter
    def completion_record_hash(self, completion_record_hash):
        """Sets the completion_record_hash of this DestinyPresentationNodeDefinition.

        If this presentation node has an associated \"Record\" that you can accomplish for completing its children, this is the identifier of that Record.  # noqa: E501

        :param completion_record_hash: The completion_record_hash of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: int
        """

        self._completion_record_hash = completion_record_hash

    @property
    def children(self):
        """Gets the children of this DestinyPresentationNodeDefinition.  # noqa: E501

        The child entities contained by this presentation node.  # noqa: E501

        :return: The children of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: DestinyPresentationNodeChildrenBlock
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this DestinyPresentationNodeDefinition.

        The child entities contained by this presentation node.  # noqa: E501

        :param children: The children of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: DestinyPresentationNodeChildrenBlock
        """

        self._children = children

    @property
    def display_style(self):
        """Gets the display_style of this DestinyPresentationNodeDefinition.  # noqa: E501

        A hint for how to display this presentation node when it's shown in a list.  # noqa: E501

        :return: The display_style of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._display_style

    @display_style.setter
    def display_style(self, display_style):
        """Sets the display_style of this DestinyPresentationNodeDefinition.

        A hint for how to display this presentation node when it's shown in a list.  # noqa: E501

        :param display_style: The display_style of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: int
        """

        self._display_style = display_style

    @property
    def screen_style(self):
        """Gets the screen_style of this DestinyPresentationNodeDefinition.  # noqa: E501

        A hint for how to display this presentation node when it's shown in its own detail screen.  # noqa: E501

        :return: The screen_style of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._screen_style

    @screen_style.setter
    def screen_style(self, screen_style):
        """Sets the screen_style of this DestinyPresentationNodeDefinition.

        A hint for how to display this presentation node when it's shown in its own detail screen.  # noqa: E501

        :param screen_style: The screen_style of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: int
        """

        self._screen_style = screen_style

    @property
    def requirements(self):
        """Gets the requirements of this DestinyPresentationNodeDefinition.  # noqa: E501

        The requirements for being able to interact with this presentation node and its children.  # noqa: E501

        :return: The requirements of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: DestinyPresentationNodeRequirementsBlock
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this DestinyPresentationNodeDefinition.

        The requirements for being able to interact with this presentation node and its children.  # noqa: E501

        :param requirements: The requirements of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: DestinyPresentationNodeRequirementsBlock
        """

        self._requirements = requirements

    @property
    def disable_child_subscreen_navigation(self):
        """Gets the disable_child_subscreen_navigation of this DestinyPresentationNodeDefinition.  # noqa: E501

        If this presentation node has children, but the game doesn't let you inspect the details of those children, that is indicated here.  # noqa: E501

        :return: The disable_child_subscreen_navigation of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._disable_child_subscreen_navigation

    @disable_child_subscreen_navigation.setter
    def disable_child_subscreen_navigation(self, disable_child_subscreen_navigation):
        """Sets the disable_child_subscreen_navigation of this DestinyPresentationNodeDefinition.

        If this presentation node has children, but the game doesn't let you inspect the details of those children, that is indicated here.  # noqa: E501

        :param disable_child_subscreen_navigation: The disable_child_subscreen_navigation of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: bool
        """

        self._disable_child_subscreen_navigation = disable_child_subscreen_navigation

    @property
    def parent_node_hashes(self):
        """Gets the parent_node_hashes of this DestinyPresentationNodeDefinition.  # noqa: E501

        A quick reference to presentation nodes that have this node as a child. (presentation nodes can be parented under multiple parents)  # noqa: E501

        :return: The parent_node_hashes of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._parent_node_hashes

    @parent_node_hashes.setter
    def parent_node_hashes(self, parent_node_hashes):
        """Sets the parent_node_hashes of this DestinyPresentationNodeDefinition.

        A quick reference to presentation nodes that have this node as a child. (presentation nodes can be parented under multiple parents)  # noqa: E501

        :param parent_node_hashes: The parent_node_hashes of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: list[int]
        """

        self._parent_node_hashes = parent_node_hashes

    @property
    def hash(self):
        """Gets the hash of this DestinyPresentationNodeDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyPresentationNodeDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyPresentationNodeDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyPresentationNodeDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyPresentationNodeDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyPresentationNodeDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyPresentationNodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyPresentationNodeDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyPresentationNodeDefinition.  # noqa: E501
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
        if not isinstance(other, DestinyPresentationNodeDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other