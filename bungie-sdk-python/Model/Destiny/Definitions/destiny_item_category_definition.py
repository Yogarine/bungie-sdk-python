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


class DestinyItemCategoryDefinition(object):
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
        'visible': 'bool',
        'deprecated': 'bool',
        'short_title': 'str',
        'item_type_regex': 'str',
        'plug_category_identifier': 'str',
        'item_type_regex_not': 'str',
        'origin_bucket_identifier': 'str',
        'grant_destiny_item_type': 'int',
        'grant_destiny_sub_type': 'int',
        'grant_destiny_class': 'int',
        'grouped_category_hashes': 'list[int]',
        'parent_category_hashes': 'list[int]',
        'group_category_only': 'bool',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'visible': 'visible',
        'deprecated': 'deprecated',
        'short_title': 'shortTitle',
        'item_type_regex': 'itemTypeRegex',
        'plug_category_identifier': 'plugCategoryIdentifier',
        'item_type_regex_not': 'itemTypeRegexNot',
        'origin_bucket_identifier': 'originBucketIdentifier',
        'grant_destiny_item_type': 'grantDestinyItemType',
        'grant_destiny_sub_type': 'grantDestinySubType',
        'grant_destiny_class': 'grantDestinyClass',
        'grouped_category_hashes': 'groupedCategoryHashes',
        'parent_category_hashes': 'parentCategoryHashes',
        'group_category_only': 'groupCategoryOnly',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, visible=None, deprecated=None, short_title=None, item_type_regex=None, plug_category_identifier=None, item_type_regex_not=None, origin_bucket_identifier=None, grant_destiny_item_type=None, grant_destiny_sub_type=None, grant_destiny_class=None, grouped_category_hashes=None, parent_category_hashes=None, group_category_only=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyItemCategoryDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._display_properties = None
        self._visible = None
        self._deprecated = None
        self._short_title = None
        self._item_type_regex = None
        self._plug_category_identifier = None
        self._item_type_regex_not = None
        self._origin_bucket_identifier = None
        self._grant_destiny_item_type = None
        self._grant_destiny_sub_type = None
        self._grant_destiny_class = None
        self._grouped_category_hashes = None
        self._parent_category_hashes = None
        self._group_category_only = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
            self.display_properties = display_properties
        if visible is not None:
            self.visible = visible
        if deprecated is not None:
            self.deprecated = deprecated
        if short_title is not None:
            self.short_title = short_title
        if item_type_regex is not None:
            self.item_type_regex = item_type_regex
        if plug_category_identifier is not None:
            self.plug_category_identifier = plug_category_identifier
        if item_type_regex_not is not None:
            self.item_type_regex_not = item_type_regex_not
        if origin_bucket_identifier is not None:
            self.origin_bucket_identifier = origin_bucket_identifier
        if grant_destiny_item_type is not None:
            self.grant_destiny_item_type = grant_destiny_item_type
        if grant_destiny_sub_type is not None:
            self.grant_destiny_sub_type = grant_destiny_sub_type
        if grant_destiny_class is not None:
            self.grant_destiny_class = grant_destiny_class
        if grouped_category_hashes is not None:
            self.grouped_category_hashes = grouped_category_hashes
        if parent_category_hashes is not None:
            self.parent_category_hashes = parent_category_hashes
        if group_category_only is not None:
            self.group_category_only = group_category_only
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyItemCategoryDefinition.  # noqa: E501


        :return: The display_properties of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyItemCategoryDefinition.


        :param display_properties: The display_properties of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def visible(self):
        """Gets the visible of this DestinyItemCategoryDefinition.  # noqa: E501

        If True, this category should be visible in UI. Sometimes we make categories that we don't think are interesting externally. It's up to you if you want to skip on showing them.  # noqa: E501

        :return: The visible of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this DestinyItemCategoryDefinition.

        If True, this category should be visible in UI. Sometimes we make categories that we don't think are interesting externally. It's up to you if you want to skip on showing them.  # noqa: E501

        :param visible: The visible of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def deprecated(self):
        """Gets the deprecated of this DestinyItemCategoryDefinition.  # noqa: E501

        If True, this category has been deprecated: it may have no items left, or there may be only legacy items that remain in it which are no longer relevant to the game.  # noqa: E501

        :return: The deprecated of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this DestinyItemCategoryDefinition.

        If True, this category has been deprecated: it may have no items left, or there may be only legacy items that remain in it which are no longer relevant to the game.  # noqa: E501

        :param deprecated: The deprecated of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def short_title(self):
        """Gets the short_title of this DestinyItemCategoryDefinition.  # noqa: E501

        A shortened version of the title. The reason why we have this is because the Armory in German had titles that were too long to display in our UI, so these were localized abbreviated versions of those categories. The property still exists today, even though the Armory doesn't exist for D2... yet.  # noqa: E501

        :return: The short_title of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: str
        """
        return self._short_title

    @short_title.setter
    def short_title(self, short_title):
        """Sets the short_title of this DestinyItemCategoryDefinition.

        A shortened version of the title. The reason why we have this is because the Armory in German had titles that were too long to display in our UI, so these were localized abbreviated versions of those categories. The property still exists today, even though the Armory doesn't exist for D2... yet.  # noqa: E501

        :param short_title: The short_title of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: str
        """

        self._short_title = short_title

    @property
    def item_type_regex(self):
        """Gets the item_type_regex of this DestinyItemCategoryDefinition.  # noqa: E501

        The janky regular expression we used against the item type to try and discern whether the item belongs to this category.  # noqa: E501

        :return: The item_type_regex of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: str
        """
        return self._item_type_regex

    @item_type_regex.setter
    def item_type_regex(self, item_type_regex):
        """Sets the item_type_regex of this DestinyItemCategoryDefinition.

        The janky regular expression we used against the item type to try and discern whether the item belongs to this category.  # noqa: E501

        :param item_type_regex: The item_type_regex of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: str
        """

        self._item_type_regex = item_type_regex

    @property
    def plug_category_identifier(self):
        """Gets the plug_category_identifier of this DestinyItemCategoryDefinition.  # noqa: E501

        If the item is a plug, this is the identifier we expect to find associated with it if it is in this category.  # noqa: E501

        :return: The plug_category_identifier of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: str
        """
        return self._plug_category_identifier

    @plug_category_identifier.setter
    def plug_category_identifier(self, plug_category_identifier):
        """Sets the plug_category_identifier of this DestinyItemCategoryDefinition.

        If the item is a plug, this is the identifier we expect to find associated with it if it is in this category.  # noqa: E501

        :param plug_category_identifier: The plug_category_identifier of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: str
        """

        self._plug_category_identifier = plug_category_identifier

    @property
    def item_type_regex_not(self):
        """Gets the item_type_regex_not of this DestinyItemCategoryDefinition.  # noqa: E501

        If the item type matches this janky regex, it does *not* belong to this category.  # noqa: E501

        :return: The item_type_regex_not of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: str
        """
        return self._item_type_regex_not

    @item_type_regex_not.setter
    def item_type_regex_not(self, item_type_regex_not):
        """Sets the item_type_regex_not of this DestinyItemCategoryDefinition.

        If the item type matches this janky regex, it does *not* belong to this category.  # noqa: E501

        :param item_type_regex_not: The item_type_regex_not of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: str
        """

        self._item_type_regex_not = item_type_regex_not

    @property
    def origin_bucket_identifier(self):
        """Gets the origin_bucket_identifier of this DestinyItemCategoryDefinition.  # noqa: E501

        If the item belongs to this bucket, it does belong to this category.  # noqa: E501

        :return: The origin_bucket_identifier of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: str
        """
        return self._origin_bucket_identifier

    @origin_bucket_identifier.setter
    def origin_bucket_identifier(self, origin_bucket_identifier):
        """Sets the origin_bucket_identifier of this DestinyItemCategoryDefinition.

        If the item belongs to this bucket, it does belong to this category.  # noqa: E501

        :param origin_bucket_identifier: The origin_bucket_identifier of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: str
        """

        self._origin_bucket_identifier = origin_bucket_identifier

    @property
    def grant_destiny_item_type(self):
        """Gets the grant_destiny_item_type of this DestinyItemCategoryDefinition.  # noqa: E501

        If an item belongs to this category, it will also receive this item type. This is now how DestinyItemType is populated for items: it used to be an even jankier process, but that's a story that requires more alcohol.  # noqa: E501

        :return: The grant_destiny_item_type of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._grant_destiny_item_type

    @grant_destiny_item_type.setter
    def grant_destiny_item_type(self, grant_destiny_item_type):
        """Sets the grant_destiny_item_type of this DestinyItemCategoryDefinition.

        If an item belongs to this category, it will also receive this item type. This is now how DestinyItemType is populated for items: it used to be an even jankier process, but that's a story that requires more alcohol.  # noqa: E501

        :param grant_destiny_item_type: The grant_destiny_item_type of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: int
        """

        self._grant_destiny_item_type = grant_destiny_item_type

    @property
    def grant_destiny_sub_type(self):
        """Gets the grant_destiny_sub_type of this DestinyItemCategoryDefinition.  # noqa: E501

        If an item belongs to this category, it will also receive this subtype enum value.  I know what you're thinking - what if it belongs to multiple categories that provide sub-types?  The last one processed wins, as is the case with all of these \"grant\" enums. Now you can see one reason why we moved away from these enums... but they're so convenient when they work, aren't they?  # noqa: E501

        :return: The grant_destiny_sub_type of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._grant_destiny_sub_type

    @grant_destiny_sub_type.setter
    def grant_destiny_sub_type(self, grant_destiny_sub_type):
        """Sets the grant_destiny_sub_type of this DestinyItemCategoryDefinition.

        If an item belongs to this category, it will also receive this subtype enum value.  I know what you're thinking - what if it belongs to multiple categories that provide sub-types?  The last one processed wins, as is the case with all of these \"grant\" enums. Now you can see one reason why we moved away from these enums... but they're so convenient when they work, aren't they?  # noqa: E501

        :param grant_destiny_sub_type: The grant_destiny_sub_type of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: int
        """

        self._grant_destiny_sub_type = grant_destiny_sub_type

    @property
    def grant_destiny_class(self):
        """Gets the grant_destiny_class of this DestinyItemCategoryDefinition.  # noqa: E501

        If an item belongs to this category, it will also get this class restriction enum value.  See the other \"grant\"-prefixed properties on this definition for my color commentary.  # noqa: E501

        :return: The grant_destiny_class of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._grant_destiny_class

    @grant_destiny_class.setter
    def grant_destiny_class(self, grant_destiny_class):
        """Sets the grant_destiny_class of this DestinyItemCategoryDefinition.

        If an item belongs to this category, it will also get this class restriction enum value.  See the other \"grant\"-prefixed properties on this definition for my color commentary.  # noqa: E501

        :param grant_destiny_class: The grant_destiny_class of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: int
        """

        self._grant_destiny_class = grant_destiny_class

    @property
    def grouped_category_hashes(self):
        """Gets the grouped_category_hashes of this DestinyItemCategoryDefinition.  # noqa: E501

        If this category is a \"parent\" category of other categories, those children will have their hashes listed in rendering order here, and can be looked up using these hashes against DestinyItemCategoryDefinition.  In this way, you can build up a visual hierarchy of item categories. That's what we did, and you can do it too. I believe in you. Yes, you, Carl.  (I hope someone named Carl reads this someday)  # noqa: E501

        :return: The grouped_category_hashes of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._grouped_category_hashes

    @grouped_category_hashes.setter
    def grouped_category_hashes(self, grouped_category_hashes):
        """Sets the grouped_category_hashes of this DestinyItemCategoryDefinition.

        If this category is a \"parent\" category of other categories, those children will have their hashes listed in rendering order here, and can be looked up using these hashes against DestinyItemCategoryDefinition.  In this way, you can build up a visual hierarchy of item categories. That's what we did, and you can do it too. I believe in you. Yes, you, Carl.  (I hope someone named Carl reads this someday)  # noqa: E501

        :param grouped_category_hashes: The grouped_category_hashes of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: list[int]
        """

        self._grouped_category_hashes = grouped_category_hashes

    @property
    def parent_category_hashes(self):
        """Gets the parent_category_hashes of this DestinyItemCategoryDefinition.  # noqa: E501

        All item category hashes of \"parent\" categories: categories that contain this as a child through the hierarchy of groupedCategoryHashes. It's a bit redundant, but having this child-centric list speeds up some calculations.  # noqa: E501

        :return: The parent_category_hashes of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._parent_category_hashes

    @parent_category_hashes.setter
    def parent_category_hashes(self, parent_category_hashes):
        """Sets the parent_category_hashes of this DestinyItemCategoryDefinition.

        All item category hashes of \"parent\" categories: categories that contain this as a child through the hierarchy of groupedCategoryHashes. It's a bit redundant, but having this child-centric list speeds up some calculations.  # noqa: E501

        :param parent_category_hashes: The parent_category_hashes of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: list[int]
        """

        self._parent_category_hashes = parent_category_hashes

    @property
    def group_category_only(self):
        """Gets the group_category_only of this DestinyItemCategoryDefinition.  # noqa: E501

        If true, this category is only used for grouping, and should not be evaluated with its own checks. Rather, the item only has this category if it has one of its child categories.  # noqa: E501

        :return: The group_category_only of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._group_category_only

    @group_category_only.setter
    def group_category_only(self, group_category_only):
        """Sets the group_category_only of this DestinyItemCategoryDefinition.

        If true, this category is only used for grouping, and should not be evaluated with its own checks. Rather, the item only has this category if it has one of its child categories.  # noqa: E501

        :param group_category_only: The group_category_only of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: bool
        """

        self._group_category_only = group_category_only

    @property
    def hash(self):
        """Gets the hash of this DestinyItemCategoryDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyItemCategoryDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyItemCategoryDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyItemCategoryDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyItemCategoryDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyItemCategoryDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyItemCategoryDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyItemCategoryDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyItemCategoryDefinition.  # noqa: E501
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
        if not isinstance(other, DestinyItemCategoryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other