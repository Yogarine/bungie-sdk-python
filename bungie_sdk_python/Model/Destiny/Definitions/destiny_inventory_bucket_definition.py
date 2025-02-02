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


class DestinyInventoryBucketDefinition(object):
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
        'scope': 'int',
        'category': 'int',
        'bucket_order': 'int',
        'item_count': 'int',
        'location': 'int',
        'has_transfer_destination': 'bool',
        'enabled': 'bool',
        'fifo': 'bool',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'scope': 'scope',
        'category': 'category',
        'bucket_order': 'bucketOrder',
        'item_count': 'itemCount',
        'location': 'location',
        'has_transfer_destination': 'hasTransferDestination',
        'enabled': 'enabled',
        'fifo': 'fifo',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, scope=None, category=None, bucket_order=None, item_count=None, location=None, has_transfer_destination=None, enabled=None, fifo=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyInventoryBucketDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._display_properties = None
        self._scope = None
        self._category = None
        self._bucket_order = None
        self._item_count = None
        self._location = None
        self._has_transfer_destination = None
        self._enabled = None
        self._fifo = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
            self.display_properties = display_properties
        if scope is not None:
            self.scope = scope
        if category is not None:
            self.category = category
        if bucket_order is not None:
            self.bucket_order = bucket_order
        if item_count is not None:
            self.item_count = item_count
        if location is not None:
            self.location = location
        if has_transfer_destination is not None:
            self.has_transfer_destination = has_transfer_destination
        if enabled is not None:
            self.enabled = enabled
        if fifo is not None:
            self.fifo = fifo
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyInventoryBucketDefinition.  # noqa: E501


        :return: The display_properties of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyInventoryBucketDefinition.


        :param display_properties: The display_properties of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def scope(self):
        """Gets the scope of this DestinyInventoryBucketDefinition.  # noqa: E501

        Where the bucket is found. 0 = Character, 1 = Account  # noqa: E501

        :return: The scope of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this DestinyInventoryBucketDefinition.

        Where the bucket is found. 0 = Character, 1 = Account  # noqa: E501

        :param scope: The scope of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: int
        """

        self._scope = scope

    @property
    def category(self):
        """Gets the category of this DestinyInventoryBucketDefinition.  # noqa: E501

        An enum value for what items can be found in the bucket. See the BucketCategory enum for more details.  # noqa: E501

        :return: The category of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this DestinyInventoryBucketDefinition.

        An enum value for what items can be found in the bucket. See the BucketCategory enum for more details.  # noqa: E501

        :param category: The category of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: int
        """

        self._category = category

    @property
    def bucket_order(self):
        """Gets the bucket_order of this DestinyInventoryBucketDefinition.  # noqa: E501

        Use this property to provide a quick-and-dirty recommended ordering for buckets in the UI. Most UIs will likely want to forsake this for something more custom and manual.  # noqa: E501

        :return: The bucket_order of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: int
        """
        return self._bucket_order

    @bucket_order.setter
    def bucket_order(self, bucket_order):
        """Sets the bucket_order of this DestinyInventoryBucketDefinition.

        Use this property to provide a quick-and-dirty recommended ordering for buckets in the UI. Most UIs will likely want to forsake this for something more custom and manual.  # noqa: E501

        :param bucket_order: The bucket_order of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: int
        """

        self._bucket_order = bucket_order

    @property
    def item_count(self):
        """Gets the item_count of this DestinyInventoryBucketDefinition.  # noqa: E501

        The maximum # of item \"slots\" in a bucket. A slot is a given combination of item + quantity.  For instance, a Weapon will always take up a single slot, and always have a quantity of 1. But a material could take up only a single slot with hundreds of quantity.  # noqa: E501

        :return: The item_count of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this DestinyInventoryBucketDefinition.

        The maximum # of item \"slots\" in a bucket. A slot is a given combination of item + quantity.  For instance, a Weapon will always take up a single slot, and always have a quantity of 1. But a material could take up only a single slot with hundreds of quantity.  # noqa: E501

        :param item_count: The item_count of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: int
        """

        self._item_count = item_count

    @property
    def location(self):
        """Gets the location of this DestinyInventoryBucketDefinition.  # noqa: E501

        Sometimes, inventory buckets represent conceptual \"locations\" in the game that might not be expected. This value indicates the conceptual location of the bucket, regardless of where it is actually contained on the character/account.   See ItemLocation for details.   Note that location includes the Vault and the Postmaster (both of whom being just inventory buckets with additional actions that can be performed on them through a Vendor)  # noqa: E501

        :return: The location of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: int
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DestinyInventoryBucketDefinition.

        Sometimes, inventory buckets represent conceptual \"locations\" in the game that might not be expected. This value indicates the conceptual location of the bucket, regardless of where it is actually contained on the character/account.   See ItemLocation for details.   Note that location includes the Vault and the Postmaster (both of whom being just inventory buckets with additional actions that can be performed on them through a Vendor)  # noqa: E501

        :param location: The location of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: int
        """

        self._location = location

    @property
    def has_transfer_destination(self):
        """Gets the has_transfer_destination of this DestinyInventoryBucketDefinition.  # noqa: E501

        If TRUE, there is at least one Vendor that can transfer items to/from this bucket. See the DestinyVendorDefinition's acceptedItems property for more information on how transferring works.  # noqa: E501

        :return: The has_transfer_destination of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._has_transfer_destination

    @has_transfer_destination.setter
    def has_transfer_destination(self, has_transfer_destination):
        """Sets the has_transfer_destination of this DestinyInventoryBucketDefinition.

        If TRUE, there is at least one Vendor that can transfer items to/from this bucket. See the DestinyVendorDefinition's acceptedItems property for more information on how transferring works.  # noqa: E501

        :param has_transfer_destination: The has_transfer_destination of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: bool
        """

        self._has_transfer_destination = has_transfer_destination

    @property
    def enabled(self):
        """Gets the enabled of this DestinyInventoryBucketDefinition.  # noqa: E501

        If True, this bucket is enabled. Disabled buckets may include buckets that were included for test purposes, or that were going to be used but then were abandoned but never removed from content *cough*.  # noqa: E501

        :return: The enabled of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DestinyInventoryBucketDefinition.

        If True, this bucket is enabled. Disabled buckets may include buckets that were included for test purposes, or that were going to be used but then were abandoned but never removed from content *cough*.  # noqa: E501

        :param enabled: The enabled of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def fifo(self):
        """Gets the fifo of this DestinyInventoryBucketDefinition.  # noqa: E501

        if a FIFO bucket fills up, it will delete the oldest item from said bucket when a new item tries to be added to it. If this is FALSE, the bucket will not allow new items to be placed in it until room is made by the user manually deleting items from it. You can see an example of this with the Postmaster's bucket.  # noqa: E501

        :return: The fifo of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._fifo

    @fifo.setter
    def fifo(self, fifo):
        """Sets the fifo of this DestinyInventoryBucketDefinition.

        if a FIFO bucket fills up, it will delete the oldest item from said bucket when a new item tries to be added to it. If this is FALSE, the bucket will not allow new items to be placed in it until room is made by the user manually deleting items from it. You can see an example of this with the Postmaster's bucket.  # noqa: E501

        :param fifo: The fifo of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: bool
        """

        self._fifo = fifo

    @property
    def hash(self):
        """Gets the hash of this DestinyInventoryBucketDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyInventoryBucketDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyInventoryBucketDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyInventoryBucketDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyInventoryBucketDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyInventoryBucketDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyInventoryBucketDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyInventoryBucketDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyInventoryBucketDefinition.  # noqa: E501
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
        if not isinstance(other, DestinyInventoryBucketDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
