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


class DestinyVendorItemDefinition(object):
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
        'vendor_item_index': 'int',
        'item_hash': 'int',
        'quantity': 'int',
        'failure_indexes': 'list[int]',
        'currencies': 'list[DestinyVendorItemQuantity]',
        'refund_policy': 'int',
        'refund_time_limit': 'int',
        'creation_levels': 'list[DestinyItemCreationEntryLevelDefinition]',
        'display_category_index': 'int',
        'category_index': 'int',
        'original_category_index': 'int',
        'minimum_level': 'int',
        'maximum_level': 'int',
        'action': 'DestinyVendorSaleItemActionBlockDefinition',
        'display_category': 'str',
        'inventory_bucket_hash': 'int',
        'visibility_scope': 'int',
        'purchasable_scope': 'int',
        'exclusivity': 'int',
        'is_offer': 'bool',
        'is_crm': 'bool',
        'sort_value': 'int',
        'expiration_tooltip': 'str',
        'redirect_to_sale_indexes': 'list[int]',
        'socket_overrides': 'list[DestinyVendorItemSocketOverride]'
    }

    attribute_map = {
        'vendor_item_index': 'vendorItemIndex',
        'item_hash': 'itemHash',
        'quantity': 'quantity',
        'failure_indexes': 'failureIndexes',
        'currencies': 'currencies',
        'refund_policy': 'refundPolicy',
        'refund_time_limit': 'refundTimeLimit',
        'creation_levels': 'creationLevels',
        'display_category_index': 'displayCategoryIndex',
        'category_index': 'categoryIndex',
        'original_category_index': 'originalCategoryIndex',
        'minimum_level': 'minimumLevel',
        'maximum_level': 'maximumLevel',
        'action': 'action',
        'display_category': 'displayCategory',
        'inventory_bucket_hash': 'inventoryBucketHash',
        'visibility_scope': 'visibilityScope',
        'purchasable_scope': 'purchasableScope',
        'exclusivity': 'exclusivity',
        'is_offer': 'isOffer',
        'is_crm': 'isCrm',
        'sort_value': 'sortValue',
        'expiration_tooltip': 'expirationTooltip',
        'redirect_to_sale_indexes': 'redirectToSaleIndexes',
        'socket_overrides': 'socketOverrides'
    }

    def __init__(self, vendor_item_index=None, item_hash=None, quantity=None, failure_indexes=None, currencies=None, refund_policy=None, refund_time_limit=None, creation_levels=None, display_category_index=None, category_index=None, original_category_index=None, minimum_level=None, maximum_level=None, action=None, display_category=None, inventory_bucket_hash=None, visibility_scope=None, purchasable_scope=None, exclusivity=None, is_offer=None, is_crm=None, sort_value=None, expiration_tooltip=None, redirect_to_sale_indexes=None, socket_overrides=None):  # noqa: E501
        """DestinyVendorItemDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._vendor_item_index = None
        self._item_hash = None
        self._quantity = None
        self._failure_indexes = None
        self._currencies = None
        self._refund_policy = None
        self._refund_time_limit = None
        self._creation_levels = None
        self._display_category_index = None
        self._category_index = None
        self._original_category_index = None
        self._minimum_level = None
        self._maximum_level = None
        self._action = None
        self._display_category = None
        self._inventory_bucket_hash = None
        self._visibility_scope = None
        self._purchasable_scope = None
        self._exclusivity = None
        self._is_offer = None
        self._is_crm = None
        self._sort_value = None
        self._expiration_tooltip = None
        self._redirect_to_sale_indexes = None
        self._socket_overrides = None
        self.discriminator = None

        if vendor_item_index is not None:
            self.vendor_item_index = vendor_item_index
        if item_hash is not None:
            self.item_hash = item_hash
        if quantity is not None:
            self.quantity = quantity
        if failure_indexes is not None:
            self.failure_indexes = failure_indexes
        if currencies is not None:
            self.currencies = currencies
        if refund_policy is not None:
            self.refund_policy = refund_policy
        if refund_time_limit is not None:
            self.refund_time_limit = refund_time_limit
        if creation_levels is not None:
            self.creation_levels = creation_levels
        if display_category_index is not None:
            self.display_category_index = display_category_index
        if category_index is not None:
            self.category_index = category_index
        if original_category_index is not None:
            self.original_category_index = original_category_index
        if minimum_level is not None:
            self.minimum_level = minimum_level
        if maximum_level is not None:
            self.maximum_level = maximum_level
        if action is not None:
            self.action = action
        if display_category is not None:
            self.display_category = display_category
        if inventory_bucket_hash is not None:
            self.inventory_bucket_hash = inventory_bucket_hash
        if visibility_scope is not None:
            self.visibility_scope = visibility_scope
        if purchasable_scope is not None:
            self.purchasable_scope = purchasable_scope
        if exclusivity is not None:
            self.exclusivity = exclusivity
        self.is_offer = is_offer
        self.is_crm = is_crm
        if sort_value is not None:
            self.sort_value = sort_value
        if expiration_tooltip is not None:
            self.expiration_tooltip = expiration_tooltip
        if redirect_to_sale_indexes is not None:
            self.redirect_to_sale_indexes = redirect_to_sale_indexes
        if socket_overrides is not None:
            self.socket_overrides = socket_overrides

    @property
    def vendor_item_index(self):
        """Gets the vendor_item_index of this DestinyVendorItemDefinition.  # noqa: E501

        The index into the DestinyVendorDefinition.saleList. This is what we use to refer to items being sold throughout live and definition data.  # noqa: E501

        :return: The vendor_item_index of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._vendor_item_index

    @vendor_item_index.setter
    def vendor_item_index(self, vendor_item_index):
        """Sets the vendor_item_index of this DestinyVendorItemDefinition.

        The index into the DestinyVendorDefinition.saleList. This is what we use to refer to items being sold throughout live and definition data.  # noqa: E501

        :param vendor_item_index: The vendor_item_index of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._vendor_item_index = vendor_item_index

    @property
    def item_hash(self):
        """Gets the item_hash of this DestinyVendorItemDefinition.  # noqa: E501

        The hash identifier of the item being sold (DestinyInventoryItemDefinition).  Note that a vendor can sell the same item in multiple ways, so don't assume that itemHash is a unique identifier for this entity.  # noqa: E501

        :return: The item_hash of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._item_hash

    @item_hash.setter
    def item_hash(self, item_hash):
        """Sets the item_hash of this DestinyVendorItemDefinition.

        The hash identifier of the item being sold (DestinyInventoryItemDefinition).  Note that a vendor can sell the same item in multiple ways, so don't assume that itemHash is a unique identifier for this entity.  # noqa: E501

        :param item_hash: The item_hash of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._item_hash = item_hash

    @property
    def quantity(self):
        """Gets the quantity of this DestinyVendorItemDefinition.  # noqa: E501

        The amount you will recieve of the item described in itemHash if you make the purchase.  # noqa: E501

        :return: The quantity of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this DestinyVendorItemDefinition.

        The amount you will recieve of the item described in itemHash if you make the purchase.  # noqa: E501

        :param quantity: The quantity of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def failure_indexes(self):
        """Gets the failure_indexes of this DestinyVendorItemDefinition.  # noqa: E501

        An list of indexes into the DestinyVendorDefinition.failureStrings array, indicating the possible failure strings that can be relevant for this item.  # noqa: E501

        :return: The failure_indexes of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._failure_indexes

    @failure_indexes.setter
    def failure_indexes(self, failure_indexes):
        """Sets the failure_indexes of this DestinyVendorItemDefinition.

        An list of indexes into the DestinyVendorDefinition.failureStrings array, indicating the possible failure strings that can be relevant for this item.  # noqa: E501

        :param failure_indexes: The failure_indexes of this DestinyVendorItemDefinition.  # noqa: E501
        :type: list[int]
        """

        self._failure_indexes = failure_indexes

    @property
    def currencies(self):
        """Gets the currencies of this DestinyVendorItemDefinition.  # noqa: E501

        This is a pre-compiled aggregation of item value and priceOverrideList, so that we have one place to check for what the purchaser must pay for the item. Use this instead of trying to piece together the price separately.  The somewhat crappy part about this is that, now that item quantity overrides have dynamic modifiers, this will not necessarily be statically true. If you were using this instead of live data, switch to using live data.  # noqa: E501

        :return: The currencies of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: list[DestinyVendorItemQuantity]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        """Sets the currencies of this DestinyVendorItemDefinition.

        This is a pre-compiled aggregation of item value and priceOverrideList, so that we have one place to check for what the purchaser must pay for the item. Use this instead of trying to piece together the price separately.  The somewhat crappy part about this is that, now that item quantity overrides have dynamic modifiers, this will not necessarily be statically true. If you were using this instead of live data, switch to using live data.  # noqa: E501

        :param currencies: The currencies of this DestinyVendorItemDefinition.  # noqa: E501
        :type: list[DestinyVendorItemQuantity]
        """

        self._currencies = currencies

    @property
    def refund_policy(self):
        """Gets the refund_policy of this DestinyVendorItemDefinition.  # noqa: E501

        If this item can be refunded, this is the policy for what will be refundd, how, and in what time period.  # noqa: E501

        :return: The refund_policy of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._refund_policy

    @refund_policy.setter
    def refund_policy(self, refund_policy):
        """Sets the refund_policy of this DestinyVendorItemDefinition.

        If this item can be refunded, this is the policy for what will be refundd, how, and in what time period.  # noqa: E501

        :param refund_policy: The refund_policy of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._refund_policy = refund_policy

    @property
    def refund_time_limit(self):
        """Gets the refund_time_limit of this DestinyVendorItemDefinition.  # noqa: E501

        The amount of time before refundability of the newly purchased item will expire.  # noqa: E501

        :return: The refund_time_limit of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._refund_time_limit

    @refund_time_limit.setter
    def refund_time_limit(self, refund_time_limit):
        """Sets the refund_time_limit of this DestinyVendorItemDefinition.

        The amount of time before refundability of the newly purchased item will expire.  # noqa: E501

        :param refund_time_limit: The refund_time_limit of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._refund_time_limit = refund_time_limit

    @property
    def creation_levels(self):
        """Gets the creation_levels of this DestinyVendorItemDefinition.  # noqa: E501

        The Default level at which the item will spawn. Almost always driven by an adjusto these days. Ideally should be singular. It's a long story how this ended up as a list, but there is always either going to be 0:1 of these entities.  # noqa: E501

        :return: The creation_levels of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: list[DestinyItemCreationEntryLevelDefinition]
        """
        return self._creation_levels

    @creation_levels.setter
    def creation_levels(self, creation_levels):
        """Sets the creation_levels of this DestinyVendorItemDefinition.

        The Default level at which the item will spawn. Almost always driven by an adjusto these days. Ideally should be singular. It's a long story how this ended up as a list, but there is always either going to be 0:1 of these entities.  # noqa: E501

        :param creation_levels: The creation_levels of this DestinyVendorItemDefinition.  # noqa: E501
        :type: list[DestinyItemCreationEntryLevelDefinition]
        """

        self._creation_levels = creation_levels

    @property
    def display_category_index(self):
        """Gets the display_category_index of this DestinyVendorItemDefinition.  # noqa: E501

        This is an index specifically into the display category, as opposed to the server-side Categories (which do not need to match or pair with each other in any way: server side categories are really just structures for common validation. Display Category will let us more easily categorize items visually)  # noqa: E501

        :return: The display_category_index of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._display_category_index

    @display_category_index.setter
    def display_category_index(self, display_category_index):
        """Sets the display_category_index of this DestinyVendorItemDefinition.

        This is an index specifically into the display category, as opposed to the server-side Categories (which do not need to match or pair with each other in any way: server side categories are really just structures for common validation. Display Category will let us more easily categorize items visually)  # noqa: E501

        :param display_category_index: The display_category_index of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._display_category_index = display_category_index

    @property
    def category_index(self):
        """Gets the category_index of this DestinyVendorItemDefinition.  # noqa: E501

        The index into the DestinyVendorDefinition.categories array, so you can find the category associated with this item.  # noqa: E501

        :return: The category_index of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._category_index

    @category_index.setter
    def category_index(self, category_index):
        """Sets the category_index of this DestinyVendorItemDefinition.

        The index into the DestinyVendorDefinition.categories array, so you can find the category associated with this item.  # noqa: E501

        :param category_index: The category_index of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._category_index = category_index

    @property
    def original_category_index(self):
        """Gets the original_category_index of this DestinyVendorItemDefinition.  # noqa: E501

        Same as above, but for the original category indexes.  # noqa: E501

        :return: The original_category_index of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._original_category_index

    @original_category_index.setter
    def original_category_index(self, original_category_index):
        """Sets the original_category_index of this DestinyVendorItemDefinition.

        Same as above, but for the original category indexes.  # noqa: E501

        :param original_category_index: The original_category_index of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._original_category_index = original_category_index

    @property
    def minimum_level(self):
        """Gets the minimum_level of this DestinyVendorItemDefinition.  # noqa: E501

        The minimum character level at which this item is available for sale.  # noqa: E501

        :return: The minimum_level of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._minimum_level

    @minimum_level.setter
    def minimum_level(self, minimum_level):
        """Sets the minimum_level of this DestinyVendorItemDefinition.

        The minimum character level at which this item is available for sale.  # noqa: E501

        :param minimum_level: The minimum_level of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._minimum_level = minimum_level

    @property
    def maximum_level(self):
        """Gets the maximum_level of this DestinyVendorItemDefinition.  # noqa: E501

        The maximum character level at which this item is available for sale.  # noqa: E501

        :return: The maximum_level of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._maximum_level

    @maximum_level.setter
    def maximum_level(self, maximum_level):
        """Sets the maximum_level of this DestinyVendorItemDefinition.

        The maximum character level at which this item is available for sale.  # noqa: E501

        :param maximum_level: The maximum_level of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._maximum_level = maximum_level

    @property
    def action(self):
        """Gets the action of this DestinyVendorItemDefinition.  # noqa: E501

        The action to be performed when purchasing the item, if it's not just \"buy\".  # noqa: E501

        :return: The action of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: DestinyVendorSaleItemActionBlockDefinition
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this DestinyVendorItemDefinition.

        The action to be performed when purchasing the item, if it's not just \"buy\".  # noqa: E501

        :param action: The action of this DestinyVendorItemDefinition.  # noqa: E501
        :type: DestinyVendorSaleItemActionBlockDefinition
        """

        self._action = action

    @property
    def display_category(self):
        """Gets the display_category of this DestinyVendorItemDefinition.  # noqa: E501

        The string identifier for the category selling this item.  # noqa: E501

        :return: The display_category of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_category

    @display_category.setter
    def display_category(self, display_category):
        """Sets the display_category of this DestinyVendorItemDefinition.

        The string identifier for the category selling this item.  # noqa: E501

        :param display_category: The display_category of this DestinyVendorItemDefinition.  # noqa: E501
        :type: str
        """

        self._display_category = display_category

    @property
    def inventory_bucket_hash(self):
        """Gets the inventory_bucket_hash of this DestinyVendorItemDefinition.  # noqa: E501

        The inventory bucket into which this item will be placed upon purchase.  # noqa: E501

        :return: The inventory_bucket_hash of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._inventory_bucket_hash

    @inventory_bucket_hash.setter
    def inventory_bucket_hash(self, inventory_bucket_hash):
        """Sets the inventory_bucket_hash of this DestinyVendorItemDefinition.

        The inventory bucket into which this item will be placed upon purchase.  # noqa: E501

        :param inventory_bucket_hash: The inventory_bucket_hash of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._inventory_bucket_hash = inventory_bucket_hash

    @property
    def visibility_scope(self):
        """Gets the visibility_scope of this DestinyVendorItemDefinition.  # noqa: E501

        The most restrictive scope that determines whether the item is available in the Vendor's inventory. See DestinyGatingScope's documentation for more information.  This can be determined by Unlock gating, or by whether or not the item has purchase level requirements (minimumLevel and maximumLevel properties).  # noqa: E501

        :return: The visibility_scope of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._visibility_scope

    @visibility_scope.setter
    def visibility_scope(self, visibility_scope):
        """Sets the visibility_scope of this DestinyVendorItemDefinition.

        The most restrictive scope that determines whether the item is available in the Vendor's inventory. See DestinyGatingScope's documentation for more information.  This can be determined by Unlock gating, or by whether or not the item has purchase level requirements (minimumLevel and maximumLevel properties).  # noqa: E501

        :param visibility_scope: The visibility_scope of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._visibility_scope = visibility_scope

    @property
    def purchasable_scope(self):
        """Gets the purchasable_scope of this DestinyVendorItemDefinition.  # noqa: E501

        Similar to visibilityScope, it represents the most restrictive scope that determines whether the item can be purchased. It will at least be as restrictive as visibilityScope, but could be more restrictive if the item has additional purchase requirements beyond whether it is merely visible or not.  See DestinyGatingScope's documentation for more information.  # noqa: E501

        :return: The purchasable_scope of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._purchasable_scope

    @purchasable_scope.setter
    def purchasable_scope(self, purchasable_scope):
        """Sets the purchasable_scope of this DestinyVendorItemDefinition.

        Similar to visibilityScope, it represents the most restrictive scope that determines whether the item can be purchased. It will at least be as restrictive as visibilityScope, but could be more restrictive if the item has additional purchase requirements beyond whether it is merely visible or not.  See DestinyGatingScope's documentation for more information.  # noqa: E501

        :param purchasable_scope: The purchasable_scope of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._purchasable_scope = purchasable_scope

    @property
    def exclusivity(self):
        """Gets the exclusivity of this DestinyVendorItemDefinition.  # noqa: E501

        If this item can only be purchased by a given platform, this indicates the platform to which it is restricted.  # noqa: E501

        :return: The exclusivity of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._exclusivity

    @exclusivity.setter
    def exclusivity(self, exclusivity):
        """Sets the exclusivity of this DestinyVendorItemDefinition.

        If this item can only be purchased by a given platform, this indicates the platform to which it is restricted.  # noqa: E501

        :param exclusivity: The exclusivity of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._exclusivity = exclusivity

    @property
    def is_offer(self):
        """Gets the is_offer of this DestinyVendorItemDefinition.  # noqa: E501

        If this sale can only be performed as the result of an offer check, this is true.  # noqa: E501

        :return: The is_offer of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_offer

    @is_offer.setter
    def is_offer(self, is_offer):
        """Sets the is_offer of this DestinyVendorItemDefinition.

        If this sale can only be performed as the result of an offer check, this is true.  # noqa: E501

        :param is_offer: The is_offer of this DestinyVendorItemDefinition.  # noqa: E501
        :type: bool
        """

        self._is_offer = is_offer

    @property
    def is_crm(self):
        """Gets the is_crm of this DestinyVendorItemDefinition.  # noqa: E501

        If this sale can only be performed as the result of receiving a CRM offer, this is true.  # noqa: E501

        :return: The is_crm of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_crm

    @is_crm.setter
    def is_crm(self, is_crm):
        """Sets the is_crm of this DestinyVendorItemDefinition.

        If this sale can only be performed as the result of receiving a CRM offer, this is true.  # noqa: E501

        :param is_crm: The is_crm of this DestinyVendorItemDefinition.  # noqa: E501
        :type: bool
        """

        self._is_crm = is_crm

    @property
    def sort_value(self):
        """Gets the sort_value of this DestinyVendorItemDefinition.  # noqa: E501

        *if* the category this item is in supports non-default sorting, this value should represent the sorting value to use, pre-processed and ready to go.  # noqa: E501

        :return: The sort_value of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: int
        """
        return self._sort_value

    @sort_value.setter
    def sort_value(self, sort_value):
        """Sets the sort_value of this DestinyVendorItemDefinition.

        *if* the category this item is in supports non-default sorting, this value should represent the sorting value to use, pre-processed and ready to go.  # noqa: E501

        :param sort_value: The sort_value of this DestinyVendorItemDefinition.  # noqa: E501
        :type: int
        """

        self._sort_value = sort_value

    @property
    def expiration_tooltip(self):
        """Gets the expiration_tooltip of this DestinyVendorItemDefinition.  # noqa: E501

        If this item can expire, this is the tooltip message to show with its expiration info.  # noqa: E501

        :return: The expiration_tooltip of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: str
        """
        return self._expiration_tooltip

    @expiration_tooltip.setter
    def expiration_tooltip(self, expiration_tooltip):
        """Sets the expiration_tooltip of this DestinyVendorItemDefinition.

        If this item can expire, this is the tooltip message to show with its expiration info.  # noqa: E501

        :param expiration_tooltip: The expiration_tooltip of this DestinyVendorItemDefinition.  # noqa: E501
        :type: str
        """

        self._expiration_tooltip = expiration_tooltip

    @property
    def redirect_to_sale_indexes(self):
        """Gets the redirect_to_sale_indexes of this DestinyVendorItemDefinition.  # noqa: E501

        If this is populated, the purchase of this item should redirect to purchasing these other items instead.  # noqa: E501

        :return: The redirect_to_sale_indexes of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._redirect_to_sale_indexes

    @redirect_to_sale_indexes.setter
    def redirect_to_sale_indexes(self, redirect_to_sale_indexes):
        """Sets the redirect_to_sale_indexes of this DestinyVendorItemDefinition.

        If this is populated, the purchase of this item should redirect to purchasing these other items instead.  # noqa: E501

        :param redirect_to_sale_indexes: The redirect_to_sale_indexes of this DestinyVendorItemDefinition.  # noqa: E501
        :type: list[int]
        """

        self._redirect_to_sale_indexes = redirect_to_sale_indexes

    @property
    def socket_overrides(self):
        """Gets the socket_overrides of this DestinyVendorItemDefinition.  # noqa: E501


        :return: The socket_overrides of this DestinyVendorItemDefinition.  # noqa: E501
        :rtype: list[DestinyVendorItemSocketOverride]
        """
        return self._socket_overrides

    @socket_overrides.setter
    def socket_overrides(self, socket_overrides):
        """Sets the socket_overrides of this DestinyVendorItemDefinition.


        :param socket_overrides: The socket_overrides of this DestinyVendorItemDefinition.  # noqa: E501
        :type: list[DestinyVendorItemSocketOverride]
        """

        self._socket_overrides = socket_overrides

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
        if not isinstance(other, DestinyVendorItemDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
