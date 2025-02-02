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


class GroupPotentialMembership(object):
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
        'member': 'GroupPotentialMember',
        'group': 'GroupV2'
    }

    attribute_map = {
        'member': 'member',
        'group': 'group'
    }

    def __init__(self, member=None, group=None):  # noqa: E501
        """GroupPotentialMembership - a model defined in OpenAPI"""  # noqa: E501

        self._member = None
        self._group = None
        self.discriminator = None

        if member is not None:
            self.member = member
        if group is not None:
            self.group = group

    @property
    def member(self):
        """Gets the member of this GroupPotentialMembership.  # noqa: E501


        :return: The member of this GroupPotentialMembership.  # noqa: E501
        :rtype: GroupPotentialMember
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this GroupPotentialMembership.


        :param member: The member of this GroupPotentialMembership.  # noqa: E501
        :type: GroupPotentialMember
        """

        self._member = member

    @property
    def group(self):
        """Gets the group of this GroupPotentialMembership.  # noqa: E501


        :return: The group of this GroupPotentialMembership.  # noqa: E501
        :rtype: GroupV2
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this GroupPotentialMembership.


        :param group: The group of this GroupPotentialMembership.  # noqa: E501
        :type: GroupV2
        """

        self._group = group

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
        if not isinstance(other, GroupPotentialMembership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
