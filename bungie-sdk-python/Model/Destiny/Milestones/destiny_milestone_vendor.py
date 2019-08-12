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


class DestinyMilestoneVendor(object):
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
        'vendor_hash': 'int',
        'preview_item_hash': 'int'
    }

    attribute_map = {
        'vendor_hash': 'vendorHash',
        'preview_item_hash': 'previewItemHash'
    }

    def __init__(self, vendor_hash=None, preview_item_hash=None):  # noqa: E501
        """DestinyMilestoneVendor - a model defined in OpenAPI"""  # noqa: E501

        self._vendor_hash = None
        self._preview_item_hash = None
        self.discriminator = None

        if vendor_hash is not None:
            self.vendor_hash = vendor_hash
        self.preview_item_hash = preview_item_hash

    @property
    def vendor_hash(self):
        """Gets the vendor_hash of this DestinyMilestoneVendor.  # noqa: E501

        The hash identifier of the Vendor related to this Milestone. You can show useful things from this, such as thier Faction icon or whatever you might care about.  # noqa: E501

        :return: The vendor_hash of this DestinyMilestoneVendor.  # noqa: E501
        :rtype: int
        """
        return self._vendor_hash

    @vendor_hash.setter
    def vendor_hash(self, vendor_hash):
        """Sets the vendor_hash of this DestinyMilestoneVendor.

        The hash identifier of the Vendor related to this Milestone. You can show useful things from this, such as thier Faction icon or whatever you might care about.  # noqa: E501

        :param vendor_hash: The vendor_hash of this DestinyMilestoneVendor.  # noqa: E501
        :type: int
        """

        self._vendor_hash = vendor_hash

    @property
    def preview_item_hash(self):
        """Gets the preview_item_hash of this DestinyMilestoneVendor.  # noqa: E501

        If this vendor is featuring a specific item for this event, this will be the hash identifier of that item. I'm taking bets now on how long we go before this needs to be a list or some other, more complex representation instead and I deprecate this too. I'm going to go with 5 months. Calling it now, 2017-09-14 at 9:46pm PST.  # noqa: E501

        :return: The preview_item_hash of this DestinyMilestoneVendor.  # noqa: E501
        :rtype: int
        """
        return self._preview_item_hash

    @preview_item_hash.setter
    def preview_item_hash(self, preview_item_hash):
        """Sets the preview_item_hash of this DestinyMilestoneVendor.

        If this vendor is featuring a specific item for this event, this will be the hash identifier of that item. I'm taking bets now on how long we go before this needs to be a list or some other, more complex representation instead and I deprecate this too. I'm going to go with 5 months. Calling it now, 2017-09-14 at 9:46pm PST.  # noqa: E501

        :param preview_item_hash: The preview_item_hash of this DestinyMilestoneVendor.  # noqa: E501
        :type: int
        """

        self._preview_item_hash = preview_item_hash

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
        if not isinstance(other, DestinyMilestoneVendor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
