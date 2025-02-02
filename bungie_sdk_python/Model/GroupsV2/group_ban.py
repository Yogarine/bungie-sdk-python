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


class GroupBan(object):
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
        'group_id': 'int',
        'last_modified_by': 'UserInfoCard',
        'created_by': 'UserInfoCard',
        'date_banned': 'datetime',
        'date_expires': 'datetime',
        'comment': 'str',
        'bungie_net_user_info': 'UserInfoCard',
        'destiny_user_info': 'UserInfoCard'
    }

    attribute_map = {
        'group_id': 'groupId',
        'last_modified_by': 'lastModifiedBy',
        'created_by': 'createdBy',
        'date_banned': 'dateBanned',
        'date_expires': 'dateExpires',
        'comment': 'comment',
        'bungie_net_user_info': 'bungieNetUserInfo',
        'destiny_user_info': 'destinyUserInfo'
    }

    def __init__(self, group_id=None, last_modified_by=None, created_by=None, date_banned=None, date_expires=None, comment=None, bungie_net_user_info=None, destiny_user_info=None):  # noqa: E501
        """GroupBan - a model defined in OpenAPI"""  # noqa: E501

        self._group_id = None
        self._last_modified_by = None
        self._created_by = None
        self._date_banned = None
        self._date_expires = None
        self._comment = None
        self._bungie_net_user_info = None
        self._destiny_user_info = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if created_by is not None:
            self.created_by = created_by
        if date_banned is not None:
            self.date_banned = date_banned
        if date_expires is not None:
            self.date_expires = date_expires
        if comment is not None:
            self.comment = comment
        if bungie_net_user_info is not None:
            self.bungie_net_user_info = bungie_net_user_info
        if destiny_user_info is not None:
            self.destiny_user_info = destiny_user_info

    @property
    def group_id(self):
        """Gets the group_id of this GroupBan.  # noqa: E501


        :return: The group_id of this GroupBan.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupBan.


        :param group_id: The group_id of this GroupBan.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this GroupBan.  # noqa: E501


        :return: The last_modified_by of this GroupBan.  # noqa: E501
        :rtype: UserInfoCard
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this GroupBan.


        :param last_modified_by: The last_modified_by of this GroupBan.  # noqa: E501
        :type: UserInfoCard
        """

        self._last_modified_by = last_modified_by

    @property
    def created_by(self):
        """Gets the created_by of this GroupBan.  # noqa: E501


        :return: The created_by of this GroupBan.  # noqa: E501
        :rtype: UserInfoCard
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GroupBan.


        :param created_by: The created_by of this GroupBan.  # noqa: E501
        :type: UserInfoCard
        """

        self._created_by = created_by

    @property
    def date_banned(self):
        """Gets the date_banned of this GroupBan.  # noqa: E501


        :return: The date_banned of this GroupBan.  # noqa: E501
        :rtype: datetime
        """
        return self._date_banned

    @date_banned.setter
    def date_banned(self, date_banned):
        """Sets the date_banned of this GroupBan.


        :param date_banned: The date_banned of this GroupBan.  # noqa: E501
        :type: datetime
        """

        self._date_banned = date_banned

    @property
    def date_expires(self):
        """Gets the date_expires of this GroupBan.  # noqa: E501


        :return: The date_expires of this GroupBan.  # noqa: E501
        :rtype: datetime
        """
        return self._date_expires

    @date_expires.setter
    def date_expires(self, date_expires):
        """Sets the date_expires of this GroupBan.


        :param date_expires: The date_expires of this GroupBan.  # noqa: E501
        :type: datetime
        """

        self._date_expires = date_expires

    @property
    def comment(self):
        """Gets the comment of this GroupBan.  # noqa: E501


        :return: The comment of this GroupBan.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this GroupBan.


        :param comment: The comment of this GroupBan.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def bungie_net_user_info(self):
        """Gets the bungie_net_user_info of this GroupBan.  # noqa: E501


        :return: The bungie_net_user_info of this GroupBan.  # noqa: E501
        :rtype: UserInfoCard
        """
        return self._bungie_net_user_info

    @bungie_net_user_info.setter
    def bungie_net_user_info(self, bungie_net_user_info):
        """Sets the bungie_net_user_info of this GroupBan.


        :param bungie_net_user_info: The bungie_net_user_info of this GroupBan.  # noqa: E501
        :type: UserInfoCard
        """

        self._bungie_net_user_info = bungie_net_user_info

    @property
    def destiny_user_info(self):
        """Gets the destiny_user_info of this GroupBan.  # noqa: E501


        :return: The destiny_user_info of this GroupBan.  # noqa: E501
        :rtype: UserInfoCard
        """
        return self._destiny_user_info

    @destiny_user_info.setter
    def destiny_user_info(self, destiny_user_info):
        """Sets the destiny_user_info of this GroupBan.


        :param destiny_user_info: The destiny_user_info of this GroupBan.  # noqa: E501
        :type: UserInfoCard
        """

        self._destiny_user_info = destiny_user_info

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
        if not isinstance(other, GroupBan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
