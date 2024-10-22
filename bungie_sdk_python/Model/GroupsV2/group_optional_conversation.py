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


class GroupOptionalConversation(object):
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
        'conversation_id': 'int',
        'chat_enabled': 'bool',
        'chat_name': 'str',
        'chat_security': 'int'
    }

    attribute_map = {
        'group_id': 'groupId',
        'conversation_id': 'conversationId',
        'chat_enabled': 'chatEnabled',
        'chat_name': 'chatName',
        'chat_security': 'chatSecurity'
    }

    def __init__(self, group_id=None, conversation_id=None, chat_enabled=None, chat_name=None, chat_security=None):  # noqa: E501
        """GroupOptionalConversation - a model defined in OpenAPI"""  # noqa: E501

        self._group_id = None
        self._conversation_id = None
        self._chat_enabled = None
        self._chat_name = None
        self._chat_security = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if chat_enabled is not None:
            self.chat_enabled = chat_enabled
        if chat_name is not None:
            self.chat_name = chat_name
        if chat_security is not None:
            self.chat_security = chat_security

    @property
    def group_id(self):
        """Gets the group_id of this GroupOptionalConversation.  # noqa: E501


        :return: The group_id of this GroupOptionalConversation.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupOptionalConversation.


        :param group_id: The group_id of this GroupOptionalConversation.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def conversation_id(self):
        """Gets the conversation_id of this GroupOptionalConversation.  # noqa: E501


        :return: The conversation_id of this GroupOptionalConversation.  # noqa: E501
        :rtype: int
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this GroupOptionalConversation.


        :param conversation_id: The conversation_id of this GroupOptionalConversation.  # noqa: E501
        :type: int
        """

        self._conversation_id = conversation_id

    @property
    def chat_enabled(self):
        """Gets the chat_enabled of this GroupOptionalConversation.  # noqa: E501


        :return: The chat_enabled of this GroupOptionalConversation.  # noqa: E501
        :rtype: bool
        """
        return self._chat_enabled

    @chat_enabled.setter
    def chat_enabled(self, chat_enabled):
        """Sets the chat_enabled of this GroupOptionalConversation.


        :param chat_enabled: The chat_enabled of this GroupOptionalConversation.  # noqa: E501
        :type: bool
        """

        self._chat_enabled = chat_enabled

    @property
    def chat_name(self):
        """Gets the chat_name of this GroupOptionalConversation.  # noqa: E501


        :return: The chat_name of this GroupOptionalConversation.  # noqa: E501
        :rtype: str
        """
        return self._chat_name

    @chat_name.setter
    def chat_name(self, chat_name):
        """Sets the chat_name of this GroupOptionalConversation.


        :param chat_name: The chat_name of this GroupOptionalConversation.  # noqa: E501
        :type: str
        """

        self._chat_name = chat_name

    @property
    def chat_security(self):
        """Gets the chat_security of this GroupOptionalConversation.  # noqa: E501


        :return: The chat_security of this GroupOptionalConversation.  # noqa: E501
        :rtype: int
        """
        return self._chat_security

    @chat_security.setter
    def chat_security(self, chat_security):
        """Sets the chat_security of this GroupOptionalConversation.


        :param chat_security: The chat_security of this GroupOptionalConversation.  # noqa: E501
        :type: int
        """

        self._chat_security = chat_security

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
        if not isinstance(other, GroupOptionalConversation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
