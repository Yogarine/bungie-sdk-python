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


class DestinyActivityGraphConnectionDefinition(object):
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
        'source_node_hash': 'int',
        'dest_node_hash': 'int'
    }

    attribute_map = {
        'source_node_hash': 'sourceNodeHash',
        'dest_node_hash': 'destNodeHash'
    }

    def __init__(self, source_node_hash=None, dest_node_hash=None):  # noqa: E501
        """DestinyActivityGraphConnectionDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._source_node_hash = None
        self._dest_node_hash = None
        self.discriminator = None

        if source_node_hash is not None:
            self.source_node_hash = source_node_hash
        if dest_node_hash is not None:
            self.dest_node_hash = dest_node_hash

    @property
    def source_node_hash(self):
        """Gets the source_node_hash of this DestinyActivityGraphConnectionDefinition.  # noqa: E501


        :return: The source_node_hash of this DestinyActivityGraphConnectionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._source_node_hash

    @source_node_hash.setter
    def source_node_hash(self, source_node_hash):
        """Sets the source_node_hash of this DestinyActivityGraphConnectionDefinition.


        :param source_node_hash: The source_node_hash of this DestinyActivityGraphConnectionDefinition.  # noqa: E501
        :type: int
        """

        self._source_node_hash = source_node_hash

    @property
    def dest_node_hash(self):
        """Gets the dest_node_hash of this DestinyActivityGraphConnectionDefinition.  # noqa: E501


        :return: The dest_node_hash of this DestinyActivityGraphConnectionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._dest_node_hash

    @dest_node_hash.setter
    def dest_node_hash(self, dest_node_hash):
        """Sets the dest_node_hash of this DestinyActivityGraphConnectionDefinition.


        :param dest_node_hash: The dest_node_hash of this DestinyActivityGraphConnectionDefinition.  # noqa: E501
        :type: int
        """

        self._dest_node_hash = dest_node_hash

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
        if not isinstance(other, DestinyActivityGraphConnectionDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
