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


class DestinyLocationDefinition(object):
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
        'location_releases': 'list[DestinyLocationReleaseDefinition]',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'vendor_hash': 'vendorHash',
        'location_releases': 'locationReleases',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, vendor_hash=None, location_releases=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyLocationDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._vendor_hash = None
        self._location_releases = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if vendor_hash is not None:
            self.vendor_hash = vendor_hash
        if location_releases is not None:
            self.location_releases = location_releases
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def vendor_hash(self):
        """Gets the vendor_hash of this DestinyLocationDefinition.  # noqa: E501

        If the location has a Vendor on it, this is the hash identifier for that Vendor. Look them up with DestinyVendorDefinition.  # noqa: E501

        :return: The vendor_hash of this DestinyLocationDefinition.  # noqa: E501
        :rtype: int
        """
        return self._vendor_hash

    @vendor_hash.setter
    def vendor_hash(self, vendor_hash):
        """Sets the vendor_hash of this DestinyLocationDefinition.

        If the location has a Vendor on it, this is the hash identifier for that Vendor. Look them up with DestinyVendorDefinition.  # noqa: E501

        :param vendor_hash: The vendor_hash of this DestinyLocationDefinition.  # noqa: E501
        :type: int
        """

        self._vendor_hash = vendor_hash

    @property
    def location_releases(self):
        """Gets the location_releases of this DestinyLocationDefinition.  # noqa: E501

        A Location may refer to different specific spots in the world based on the world's current state. This is a list of those potential spots, and the data we can use at runtime to determine which one of the spots is the currently valid one.  # noqa: E501

        :return: The location_releases of this DestinyLocationDefinition.  # noqa: E501
        :rtype: list[DestinyLocationReleaseDefinition]
        """
        return self._location_releases

    @location_releases.setter
    def location_releases(self, location_releases):
        """Sets the location_releases of this DestinyLocationDefinition.

        A Location may refer to different specific spots in the world based on the world's current state. This is a list of those potential spots, and the data we can use at runtime to determine which one of the spots is the currently valid one.  # noqa: E501

        :param location_releases: The location_releases of this DestinyLocationDefinition.  # noqa: E501
        :type: list[DestinyLocationReleaseDefinition]
        """

        self._location_releases = location_releases

    @property
    def hash(self):
        """Gets the hash of this DestinyLocationDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyLocationDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyLocationDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyLocationDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyLocationDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyLocationDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyLocationDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyLocationDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyLocationDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyLocationDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyLocationDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyLocationDefinition.  # noqa: E501
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
        if not isinstance(other, DestinyLocationDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other