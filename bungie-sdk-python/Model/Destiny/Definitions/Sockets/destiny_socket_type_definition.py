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


class DestinySocketTypeDefinition(object):
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
        'insert_action': 'DestinyInsertPlugActionDefinition',
        'plug_whitelist': 'list[DestinyPlugWhitelistEntryDefinition]',
        'socket_category_hash': 'int',
        'visibility': 'int',
        'always_randomize_sockets': 'bool',
        'is_preview_enabled': 'bool',
        'hide_duplicate_reusable_plugs': 'bool',
        'overrides_ui_appearance': 'bool',
        'avoid_duplicates_on_initialization': 'bool',
        'currency_scalars': 'list[DestinySocketTypeScalarMaterialRequirementEntry]',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'insert_action': 'insertAction',
        'plug_whitelist': 'plugWhitelist',
        'socket_category_hash': 'socketCategoryHash',
        'visibility': 'visibility',
        'always_randomize_sockets': 'alwaysRandomizeSockets',
        'is_preview_enabled': 'isPreviewEnabled',
        'hide_duplicate_reusable_plugs': 'hideDuplicateReusablePlugs',
        'overrides_ui_appearance': 'overridesUiAppearance',
        'avoid_duplicates_on_initialization': 'avoidDuplicatesOnInitialization',
        'currency_scalars': 'currencyScalars',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, insert_action=None, plug_whitelist=None, socket_category_hash=None, visibility=None, always_randomize_sockets=None, is_preview_enabled=None, hide_duplicate_reusable_plugs=None, overrides_ui_appearance=None, avoid_duplicates_on_initialization=None, currency_scalars=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinySocketTypeDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._display_properties = None
        self._insert_action = None
        self._plug_whitelist = None
        self._socket_category_hash = None
        self._visibility = None
        self._always_randomize_sockets = None
        self._is_preview_enabled = None
        self._hide_duplicate_reusable_plugs = None
        self._overrides_ui_appearance = None
        self._avoid_duplicates_on_initialization = None
        self._currency_scalars = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
            self.display_properties = display_properties
        if insert_action is not None:
            self.insert_action = insert_action
        if plug_whitelist is not None:
            self.plug_whitelist = plug_whitelist
        if socket_category_hash is not None:
            self.socket_category_hash = socket_category_hash
        if visibility is not None:
            self.visibility = visibility
        if always_randomize_sockets is not None:
            self.always_randomize_sockets = always_randomize_sockets
        if is_preview_enabled is not None:
            self.is_preview_enabled = is_preview_enabled
        if hide_duplicate_reusable_plugs is not None:
            self.hide_duplicate_reusable_plugs = hide_duplicate_reusable_plugs
        if overrides_ui_appearance is not None:
            self.overrides_ui_appearance = overrides_ui_appearance
        if avoid_duplicates_on_initialization is not None:
            self.avoid_duplicates_on_initialization = avoid_duplicates_on_initialization
        if currency_scalars is not None:
            self.currency_scalars = currency_scalars
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinySocketTypeDefinition.  # noqa: E501

        There are fields for this display data, but they appear to be unpopulated as of now. I am not sure where in the UI these would show if they even were populated, but I will continue to return this data in case it becomes useful.  # noqa: E501

        :return: The display_properties of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinySocketTypeDefinition.

        There are fields for this display data, but they appear to be unpopulated as of now. I am not sure where in the UI these would show if they even were populated, but I will continue to return this data in case it becomes useful.  # noqa: E501

        :param display_properties: The display_properties of this DestinySocketTypeDefinition.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def insert_action(self):
        """Gets the insert_action of this DestinySocketTypeDefinition.  # noqa: E501

        Defines what happens when a plug is inserted into sockets of this type.  # noqa: E501

        :return: The insert_action of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: DestinyInsertPlugActionDefinition
        """
        return self._insert_action

    @insert_action.setter
    def insert_action(self, insert_action):
        """Sets the insert_action of this DestinySocketTypeDefinition.

        Defines what happens when a plug is inserted into sockets of this type.  # noqa: E501

        :param insert_action: The insert_action of this DestinySocketTypeDefinition.  # noqa: E501
        :type: DestinyInsertPlugActionDefinition
        """

        self._insert_action = insert_action

    @property
    def plug_whitelist(self):
        """Gets the plug_whitelist of this DestinySocketTypeDefinition.  # noqa: E501

        A list of Plug \"Categories\" that are allowed to be plugged into sockets of this type.  These should be compared against a given plug item's DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item's category.  If the plug's category matches any whitelisted plug, or if the whitelist is empty, it is allowed to be inserted.  # noqa: E501

        :return: The plug_whitelist of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: list[DestinyPlugWhitelistEntryDefinition]
        """
        return self._plug_whitelist

    @plug_whitelist.setter
    def plug_whitelist(self, plug_whitelist):
        """Sets the plug_whitelist of this DestinySocketTypeDefinition.

        A list of Plug \"Categories\" that are allowed to be plugged into sockets of this type.  These should be compared against a given plug item's DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item's category.  If the plug's category matches any whitelisted plug, or if the whitelist is empty, it is allowed to be inserted.  # noqa: E501

        :param plug_whitelist: The plug_whitelist of this DestinySocketTypeDefinition.  # noqa: E501
        :type: list[DestinyPlugWhitelistEntryDefinition]
        """

        self._plug_whitelist = plug_whitelist

    @property
    def socket_category_hash(self):
        """Gets the socket_category_hash of this DestinySocketTypeDefinition.  # noqa: E501


        :return: The socket_category_hash of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._socket_category_hash

    @socket_category_hash.setter
    def socket_category_hash(self, socket_category_hash):
        """Sets the socket_category_hash of this DestinySocketTypeDefinition.


        :param socket_category_hash: The socket_category_hash of this DestinySocketTypeDefinition.  # noqa: E501
        :type: int
        """

        self._socket_category_hash = socket_category_hash

    @property
    def visibility(self):
        """Gets the visibility of this DestinySocketTypeDefinition.  # noqa: E501

        Sometimes a socket isn't visible. These are some of the conditions under which sockets of this type are not visible. Unfortunately, the truth of visibility is much, much more complex. Best to rely on the live data for whether the socket is visible and enabled.  # noqa: E501

        :return: The visibility of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this DestinySocketTypeDefinition.

        Sometimes a socket isn't visible. These are some of the conditions under which sockets of this type are not visible. Unfortunately, the truth of visibility is much, much more complex. Best to rely on the live data for whether the socket is visible and enabled.  # noqa: E501

        :param visibility: The visibility of this DestinySocketTypeDefinition.  # noqa: E501
        :type: int
        """

        self._visibility = visibility

    @property
    def always_randomize_sockets(self):
        """Gets the always_randomize_sockets of this DestinySocketTypeDefinition.  # noqa: E501


        :return: The always_randomize_sockets of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._always_randomize_sockets

    @always_randomize_sockets.setter
    def always_randomize_sockets(self, always_randomize_sockets):
        """Sets the always_randomize_sockets of this DestinySocketTypeDefinition.


        :param always_randomize_sockets: The always_randomize_sockets of this DestinySocketTypeDefinition.  # noqa: E501
        :type: bool
        """

        self._always_randomize_sockets = always_randomize_sockets

    @property
    def is_preview_enabled(self):
        """Gets the is_preview_enabled of this DestinySocketTypeDefinition.  # noqa: E501


        :return: The is_preview_enabled of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_preview_enabled

    @is_preview_enabled.setter
    def is_preview_enabled(self, is_preview_enabled):
        """Sets the is_preview_enabled of this DestinySocketTypeDefinition.


        :param is_preview_enabled: The is_preview_enabled of this DestinySocketTypeDefinition.  # noqa: E501
        :type: bool
        """

        self._is_preview_enabled = is_preview_enabled

    @property
    def hide_duplicate_reusable_plugs(self):
        """Gets the hide_duplicate_reusable_plugs of this DestinySocketTypeDefinition.  # noqa: E501


        :return: The hide_duplicate_reusable_plugs of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._hide_duplicate_reusable_plugs

    @hide_duplicate_reusable_plugs.setter
    def hide_duplicate_reusable_plugs(self, hide_duplicate_reusable_plugs):
        """Sets the hide_duplicate_reusable_plugs of this DestinySocketTypeDefinition.


        :param hide_duplicate_reusable_plugs: The hide_duplicate_reusable_plugs of this DestinySocketTypeDefinition.  # noqa: E501
        :type: bool
        """

        self._hide_duplicate_reusable_plugs = hide_duplicate_reusable_plugs

    @property
    def overrides_ui_appearance(self):
        """Gets the overrides_ui_appearance of this DestinySocketTypeDefinition.  # noqa: E501

        This property indicates if the socket type determines whether Emblem icons and nameplates should be overridden by the inserted plug item's icon and nameplate.  # noqa: E501

        :return: The overrides_ui_appearance of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._overrides_ui_appearance

    @overrides_ui_appearance.setter
    def overrides_ui_appearance(self, overrides_ui_appearance):
        """Sets the overrides_ui_appearance of this DestinySocketTypeDefinition.

        This property indicates if the socket type determines whether Emblem icons and nameplates should be overridden by the inserted plug item's icon and nameplate.  # noqa: E501

        :param overrides_ui_appearance: The overrides_ui_appearance of this DestinySocketTypeDefinition.  # noqa: E501
        :type: bool
        """

        self._overrides_ui_appearance = overrides_ui_appearance

    @property
    def avoid_duplicates_on_initialization(self):
        """Gets the avoid_duplicates_on_initialization of this DestinySocketTypeDefinition.  # noqa: E501


        :return: The avoid_duplicates_on_initialization of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._avoid_duplicates_on_initialization

    @avoid_duplicates_on_initialization.setter
    def avoid_duplicates_on_initialization(self, avoid_duplicates_on_initialization):
        """Sets the avoid_duplicates_on_initialization of this DestinySocketTypeDefinition.


        :param avoid_duplicates_on_initialization: The avoid_duplicates_on_initialization of this DestinySocketTypeDefinition.  # noqa: E501
        :type: bool
        """

        self._avoid_duplicates_on_initialization = avoid_duplicates_on_initialization

    @property
    def currency_scalars(self):
        """Gets the currency_scalars of this DestinySocketTypeDefinition.  # noqa: E501


        :return: The currency_scalars of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: list[DestinySocketTypeScalarMaterialRequirementEntry]
        """
        return self._currency_scalars

    @currency_scalars.setter
    def currency_scalars(self, currency_scalars):
        """Sets the currency_scalars of this DestinySocketTypeDefinition.


        :param currency_scalars: The currency_scalars of this DestinySocketTypeDefinition.  # noqa: E501
        :type: list[DestinySocketTypeScalarMaterialRequirementEntry]
        """

        self._currency_scalars = currency_scalars

    @property
    def hash(self):
        """Gets the hash of this DestinySocketTypeDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinySocketTypeDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinySocketTypeDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinySocketTypeDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinySocketTypeDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinySocketTypeDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinySocketTypeDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinySocketTypeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinySocketTypeDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinySocketTypeDefinition.  # noqa: E501
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
        if not isinstance(other, DestinySocketTypeDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
