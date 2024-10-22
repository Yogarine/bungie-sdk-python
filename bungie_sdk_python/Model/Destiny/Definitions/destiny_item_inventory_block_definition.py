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


class DestinyItemInventoryBlockDefinition(object):
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
        'stack_unique_label': 'str',
        'max_stack_size': 'int',
        'bucket_type_hash': 'int',
        'recovery_bucket_type_hash': 'int',
        'tier_type_hash': 'int',
        'is_instance_item': 'bool',
        'tier_type_name': 'str',
        'tier_type': 'int',
        'expiration_tooltip': 'str',
        'expired_in_activity_message': 'str',
        'expired_in_orbit_message': 'str',
        'suppress_expiration_when_objectives_complete': 'bool'
    }

    attribute_map = {
        'stack_unique_label': 'stackUniqueLabel',
        'max_stack_size': 'maxStackSize',
        'bucket_type_hash': 'bucketTypeHash',
        'recovery_bucket_type_hash': 'recoveryBucketTypeHash',
        'tier_type_hash': 'tierTypeHash',
        'is_instance_item': 'isInstanceItem',
        'tier_type_name': 'tierTypeName',
        'tier_type': 'tierType',
        'expiration_tooltip': 'expirationTooltip',
        'expired_in_activity_message': 'expiredInActivityMessage',
        'expired_in_orbit_message': 'expiredInOrbitMessage',
        'suppress_expiration_when_objectives_complete': 'suppressExpirationWhenObjectivesComplete'
    }

    def __init__(self, stack_unique_label=None, max_stack_size=None, bucket_type_hash=None, recovery_bucket_type_hash=None, tier_type_hash=None, is_instance_item=None, tier_type_name=None, tier_type=None, expiration_tooltip=None, expired_in_activity_message=None, expired_in_orbit_message=None, suppress_expiration_when_objectives_complete=None):  # noqa: E501
        """DestinyItemInventoryBlockDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._stack_unique_label = None
        self._max_stack_size = None
        self._bucket_type_hash = None
        self._recovery_bucket_type_hash = None
        self._tier_type_hash = None
        self._is_instance_item = None
        self._tier_type_name = None
        self._tier_type = None
        self._expiration_tooltip = None
        self._expired_in_activity_message = None
        self._expired_in_orbit_message = None
        self._suppress_expiration_when_objectives_complete = None
        self.discriminator = None

        if stack_unique_label is not None:
            self.stack_unique_label = stack_unique_label
        if max_stack_size is not None:
            self.max_stack_size = max_stack_size
        if bucket_type_hash is not None:
            self.bucket_type_hash = bucket_type_hash
        if recovery_bucket_type_hash is not None:
            self.recovery_bucket_type_hash = recovery_bucket_type_hash
        if tier_type_hash is not None:
            self.tier_type_hash = tier_type_hash
        if is_instance_item is not None:
            self.is_instance_item = is_instance_item
        if tier_type_name is not None:
            self.tier_type_name = tier_type_name
        if tier_type is not None:
            self.tier_type = tier_type
        if expiration_tooltip is not None:
            self.expiration_tooltip = expiration_tooltip
        if expired_in_activity_message is not None:
            self.expired_in_activity_message = expired_in_activity_message
        if expired_in_orbit_message is not None:
            self.expired_in_orbit_message = expired_in_orbit_message
        if suppress_expiration_when_objectives_complete is not None:
            self.suppress_expiration_when_objectives_complete = suppress_expiration_when_objectives_complete

    @property
    def stack_unique_label(self):
        """Gets the stack_unique_label of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        If this string is populated, you can't have more than one stack with this label in a given inventory. Note that this is different from the equipping block's unique label, which is used for equipping uniqueness.  # noqa: E501

        :return: The stack_unique_label of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: str
        """
        return self._stack_unique_label

    @stack_unique_label.setter
    def stack_unique_label(self, stack_unique_label):
        """Sets the stack_unique_label of this DestinyItemInventoryBlockDefinition.

        If this string is populated, you can't have more than one stack with this label in a given inventory. Note that this is different from the equipping block's unique label, which is used for equipping uniqueness.  # noqa: E501

        :param stack_unique_label: The stack_unique_label of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: str
        """

        self._stack_unique_label = stack_unique_label

    @property
    def max_stack_size(self):
        """Gets the max_stack_size of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        The maximum quantity of this item that can exist in a stack.  # noqa: E501

        :return: The max_stack_size of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._max_stack_size

    @max_stack_size.setter
    def max_stack_size(self, max_stack_size):
        """Sets the max_stack_size of this DestinyItemInventoryBlockDefinition.

        The maximum quantity of this item that can exist in a stack.  # noqa: E501

        :param max_stack_size: The max_stack_size of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: int
        """

        self._max_stack_size = max_stack_size

    @property
    def bucket_type_hash(self):
        """Gets the bucket_type_hash of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        The hash identifier for the DestinyInventoryBucketDefinition to which this item belongs. I should have named this \"bucketHash\", but too many things refer to it now. Sigh.  # noqa: E501

        :return: The bucket_type_hash of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._bucket_type_hash

    @bucket_type_hash.setter
    def bucket_type_hash(self, bucket_type_hash):
        """Sets the bucket_type_hash of this DestinyItemInventoryBlockDefinition.

        The hash identifier for the DestinyInventoryBucketDefinition to which this item belongs. I should have named this \"bucketHash\", but too many things refer to it now. Sigh.  # noqa: E501

        :param bucket_type_hash: The bucket_type_hash of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: int
        """

        self._bucket_type_hash = bucket_type_hash

    @property
    def recovery_bucket_type_hash(self):
        """Gets the recovery_bucket_type_hash of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        If the item is picked up by the lost loot queue, this is the hash identifier for the DestinyInventoryBucketDefinition into which it will be placed. Again, I should have named this recoveryBucketHash instead.  # noqa: E501

        :return: The recovery_bucket_type_hash of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._recovery_bucket_type_hash

    @recovery_bucket_type_hash.setter
    def recovery_bucket_type_hash(self, recovery_bucket_type_hash):
        """Sets the recovery_bucket_type_hash of this DestinyItemInventoryBlockDefinition.

        If the item is picked up by the lost loot queue, this is the hash identifier for the DestinyInventoryBucketDefinition into which it will be placed. Again, I should have named this recoveryBucketHash instead.  # noqa: E501

        :param recovery_bucket_type_hash: The recovery_bucket_type_hash of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: int
        """

        self._recovery_bucket_type_hash = recovery_bucket_type_hash

    @property
    def tier_type_hash(self):
        """Gets the tier_type_hash of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        The hash identifier for the Tier Type of the item, use to look up its DestinyItemTierTypeDefinition if you need to show localized data for the item's tier.  # noqa: E501

        :return: The tier_type_hash of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._tier_type_hash

    @tier_type_hash.setter
    def tier_type_hash(self, tier_type_hash):
        """Sets the tier_type_hash of this DestinyItemInventoryBlockDefinition.

        The hash identifier for the Tier Type of the item, use to look up its DestinyItemTierTypeDefinition if you need to show localized data for the item's tier.  # noqa: E501

        :param tier_type_hash: The tier_type_hash of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: int
        """

        self._tier_type_hash = tier_type_hash

    @property
    def is_instance_item(self):
        """Gets the is_instance_item of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        If TRUE, this item is instanced. Otherwise, it is a generic item that merely has a quantity in a stack (like Glimmer).  # noqa: E501

        :return: The is_instance_item of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_instance_item

    @is_instance_item.setter
    def is_instance_item(self, is_instance_item):
        """Sets the is_instance_item of this DestinyItemInventoryBlockDefinition.

        If TRUE, this item is instanced. Otherwise, it is a generic item that merely has a quantity in a stack (like Glimmer).  # noqa: E501

        :param is_instance_item: The is_instance_item of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: bool
        """

        self._is_instance_item = is_instance_item

    @property
    def tier_type_name(self):
        """Gets the tier_type_name of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        The localized name of the tier type, which is a useful shortcut so you don't have to look up the definition every time. However, it's mostly a holdover from days before we had a DestinyItemTierTypeDefinition to refer to.  # noqa: E501

        :return: The tier_type_name of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: str
        """
        return self._tier_type_name

    @tier_type_name.setter
    def tier_type_name(self, tier_type_name):
        """Sets the tier_type_name of this DestinyItemInventoryBlockDefinition.

        The localized name of the tier type, which is a useful shortcut so you don't have to look up the definition every time. However, it's mostly a holdover from days before we had a DestinyItemTierTypeDefinition to refer to.  # noqa: E501

        :param tier_type_name: The tier_type_name of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: str
        """

        self._tier_type_name = tier_type_name

    @property
    def tier_type(self):
        """Gets the tier_type of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        The enumeration matching the tier type of the item to known values, again for convenience sake.  # noqa: E501

        :return: The tier_type of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._tier_type

    @tier_type.setter
    def tier_type(self, tier_type):
        """Sets the tier_type of this DestinyItemInventoryBlockDefinition.

        The enumeration matching the tier type of the item to known values, again for convenience sake.  # noqa: E501

        :param tier_type: The tier_type of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: int
        """

        self._tier_type = tier_type

    @property
    def expiration_tooltip(self):
        """Gets the expiration_tooltip of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        The tooltip message to show, if any, when the item expires.  # noqa: E501

        :return: The expiration_tooltip of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: str
        """
        return self._expiration_tooltip

    @expiration_tooltip.setter
    def expiration_tooltip(self, expiration_tooltip):
        """Sets the expiration_tooltip of this DestinyItemInventoryBlockDefinition.

        The tooltip message to show, if any, when the item expires.  # noqa: E501

        :param expiration_tooltip: The expiration_tooltip of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: str
        """

        self._expiration_tooltip = expiration_tooltip

    @property
    def expired_in_activity_message(self):
        """Gets the expired_in_activity_message of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        If the item expires while playing in an activity, we show a different message.  # noqa: E501

        :return: The expired_in_activity_message of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: str
        """
        return self._expired_in_activity_message

    @expired_in_activity_message.setter
    def expired_in_activity_message(self, expired_in_activity_message):
        """Sets the expired_in_activity_message of this DestinyItemInventoryBlockDefinition.

        If the item expires while playing in an activity, we show a different message.  # noqa: E501

        :param expired_in_activity_message: The expired_in_activity_message of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: str
        """

        self._expired_in_activity_message = expired_in_activity_message

    @property
    def expired_in_orbit_message(self):
        """Gets the expired_in_orbit_message of this DestinyItemInventoryBlockDefinition.  # noqa: E501

        If the item expires in orbit, we show a... more different message. (\"Consummate V's, consummate!\")  # noqa: E501

        :return: The expired_in_orbit_message of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: str
        """
        return self._expired_in_orbit_message

    @expired_in_orbit_message.setter
    def expired_in_orbit_message(self, expired_in_orbit_message):
        """Sets the expired_in_orbit_message of this DestinyItemInventoryBlockDefinition.

        If the item expires in orbit, we show a... more different message. (\"Consummate V's, consummate!\")  # noqa: E501

        :param expired_in_orbit_message: The expired_in_orbit_message of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: str
        """

        self._expired_in_orbit_message = expired_in_orbit_message

    @property
    def suppress_expiration_when_objectives_complete(self):
        """Gets the suppress_expiration_when_objectives_complete of this DestinyItemInventoryBlockDefinition.  # noqa: E501


        :return: The suppress_expiration_when_objectives_complete of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_expiration_when_objectives_complete

    @suppress_expiration_when_objectives_complete.setter
    def suppress_expiration_when_objectives_complete(self, suppress_expiration_when_objectives_complete):
        """Sets the suppress_expiration_when_objectives_complete of this DestinyItemInventoryBlockDefinition.


        :param suppress_expiration_when_objectives_complete: The suppress_expiration_when_objectives_complete of this DestinyItemInventoryBlockDefinition.  # noqa: E501
        :type: bool
        """

        self._suppress_expiration_when_objectives_complete = suppress_expiration_when_objectives_complete

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
        if not isinstance(other, DestinyItemInventoryBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
