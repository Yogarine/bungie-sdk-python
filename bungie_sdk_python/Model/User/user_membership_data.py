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


class UserMembershipData(object):
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
        'destiny_memberships': 'list[UserInfoCard]',
        'bungie_net_user': 'GeneralUser'
    }

    attribute_map = {
        'destiny_memberships': 'destinyMemberships',
        'bungie_net_user': 'bungieNetUser'
    }

    def __init__(self, destiny_memberships=None, bungie_net_user=None):  # noqa: E501
        """UserMembershipData - a model defined in OpenAPI"""  # noqa: E501

        self._destiny_memberships = None
        self._bungie_net_user = None
        self.discriminator = None

        if destiny_memberships is not None:
            self.destiny_memberships = destiny_memberships
        if bungie_net_user is not None:
            self.bungie_net_user = bungie_net_user

    @property
    def destiny_memberships(self):
        """Gets the destiny_memberships of this UserMembershipData.  # noqa: E501

        this allows you to see destiny memberships that are visible and linked to this account (regardless of whether or not they have characters on the world server)  # noqa: E501

        :return: The destiny_memberships of this UserMembershipData.  # noqa: E501
        :rtype: list[UserInfoCard]
        """
        return self._destiny_memberships

    @destiny_memberships.setter
    def destiny_memberships(self, destiny_memberships):
        """Sets the destiny_memberships of this UserMembershipData.

        this allows you to see destiny memberships that are visible and linked to this account (regardless of whether or not they have characters on the world server)  # noqa: E501

        :param destiny_memberships: The destiny_memberships of this UserMembershipData.  # noqa: E501
        :type: list[UserInfoCard]
        """

        self._destiny_memberships = destiny_memberships

    @property
    def bungie_net_user(self):
        """Gets the bungie_net_user of this UserMembershipData.  # noqa: E501


        :return: The bungie_net_user of this UserMembershipData.  # noqa: E501
        :rtype: GeneralUser
        """
        return self._bungie_net_user

    @bungie_net_user.setter
    def bungie_net_user(self, bungie_net_user):
        """Sets the bungie_net_user of this UserMembershipData.


        :param bungie_net_user: The bungie_net_user of this UserMembershipData.  # noqa: E501
        :type: GeneralUser
        """

        self._bungie_net_user = bungie_net_user

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
        if not isinstance(other, UserMembershipData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
