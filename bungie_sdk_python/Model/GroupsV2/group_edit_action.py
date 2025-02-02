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


class GroupEditAction(object):
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
        'name': 'str',
        'about': 'str',
        'motto': 'str',
        'theme': 'str',
        'avatar_image_index': 'int',
        'tags': 'str',
        'is_public': 'bool',
        'membership_option': 'int',
        'is_public_topic_admin_only': 'bool',
        'allow_chat': 'bool',
        'chat_security': 'int',
        'callsign': 'str',
        'locale': 'str',
        'homepage': 'int',
        'enable_invitation_messaging_for_admins': 'bool',
        'default_publicity': 'int'
    }

    attribute_map = {
        'name': 'name',
        'about': 'about',
        'motto': 'motto',
        'theme': 'theme',
        'avatar_image_index': 'avatarImageIndex',
        'tags': 'tags',
        'is_public': 'isPublic',
        'membership_option': 'membershipOption',
        'is_public_topic_admin_only': 'isPublicTopicAdminOnly',
        'allow_chat': 'allowChat',
        'chat_security': 'chatSecurity',
        'callsign': 'callsign',
        'locale': 'locale',
        'homepage': 'homepage',
        'enable_invitation_messaging_for_admins': 'enableInvitationMessagingForAdmins',
        'default_publicity': 'defaultPublicity'
    }

    def __init__(self, name=None, about=None, motto=None, theme=None, avatar_image_index=None, tags=None, is_public=None, membership_option=None, is_public_topic_admin_only=None, allow_chat=None, chat_security=None, callsign=None, locale=None, homepage=None, enable_invitation_messaging_for_admins=None, default_publicity=None):  # noqa: E501
        """GroupEditAction - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._about = None
        self._motto = None
        self._theme = None
        self._avatar_image_index = None
        self._tags = None
        self._is_public = None
        self._membership_option = None
        self._is_public_topic_admin_only = None
        self._allow_chat = None
        self._chat_security = None
        self._callsign = None
        self._locale = None
        self._homepage = None
        self._enable_invitation_messaging_for_admins = None
        self._default_publicity = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if about is not None:
            self.about = about
        if motto is not None:
            self.motto = motto
        if theme is not None:
            self.theme = theme
        self.avatar_image_index = avatar_image_index
        if tags is not None:
            self.tags = tags
        self.is_public = is_public
        self.membership_option = membership_option
        self.is_public_topic_admin_only = is_public_topic_admin_only
        self.allow_chat = allow_chat
        self.chat_security = chat_security
        if callsign is not None:
            self.callsign = callsign
        if locale is not None:
            self.locale = locale
        self.homepage = homepage
        self.enable_invitation_messaging_for_admins = enable_invitation_messaging_for_admins
        self.default_publicity = default_publicity

    @property
    def name(self):
        """Gets the name of this GroupEditAction.  # noqa: E501


        :return: The name of this GroupEditAction.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupEditAction.


        :param name: The name of this GroupEditAction.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def about(self):
        """Gets the about of this GroupEditAction.  # noqa: E501


        :return: The about of this GroupEditAction.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this GroupEditAction.


        :param about: The about of this GroupEditAction.  # noqa: E501
        :type: str
        """

        self._about = about

    @property
    def motto(self):
        """Gets the motto of this GroupEditAction.  # noqa: E501


        :return: The motto of this GroupEditAction.  # noqa: E501
        :rtype: str
        """
        return self._motto

    @motto.setter
    def motto(self, motto):
        """Sets the motto of this GroupEditAction.


        :param motto: The motto of this GroupEditAction.  # noqa: E501
        :type: str
        """

        self._motto = motto

    @property
    def theme(self):
        """Gets the theme of this GroupEditAction.  # noqa: E501


        :return: The theme of this GroupEditAction.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this GroupEditAction.


        :param theme: The theme of this GroupEditAction.  # noqa: E501
        :type: str
        """

        self._theme = theme

    @property
    def avatar_image_index(self):
        """Gets the avatar_image_index of this GroupEditAction.  # noqa: E501


        :return: The avatar_image_index of this GroupEditAction.  # noqa: E501
        :rtype: int
        """
        return self._avatar_image_index

    @avatar_image_index.setter
    def avatar_image_index(self, avatar_image_index):
        """Sets the avatar_image_index of this GroupEditAction.


        :param avatar_image_index: The avatar_image_index of this GroupEditAction.  # noqa: E501
        :type: int
        """

        self._avatar_image_index = avatar_image_index

    @property
    def tags(self):
        """Gets the tags of this GroupEditAction.  # noqa: E501


        :return: The tags of this GroupEditAction.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GroupEditAction.


        :param tags: The tags of this GroupEditAction.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def is_public(self):
        """Gets the is_public of this GroupEditAction.  # noqa: E501


        :return: The is_public of this GroupEditAction.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this GroupEditAction.


        :param is_public: The is_public of this GroupEditAction.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def membership_option(self):
        """Gets the membership_option of this GroupEditAction.  # noqa: E501


        :return: The membership_option of this GroupEditAction.  # noqa: E501
        :rtype: int
        """
        return self._membership_option

    @membership_option.setter
    def membership_option(self, membership_option):
        """Sets the membership_option of this GroupEditAction.


        :param membership_option: The membership_option of this GroupEditAction.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if membership_option not in allowed_values:
            raise ValueError(
                "Invalid value for `membership_option` ({0}), must be one of {1}"  # noqa: E501
                .format(membership_option, allowed_values)
            )

        self._membership_option = membership_option

    @property
    def is_public_topic_admin_only(self):
        """Gets the is_public_topic_admin_only of this GroupEditAction.  # noqa: E501


        :return: The is_public_topic_admin_only of this GroupEditAction.  # noqa: E501
        :rtype: bool
        """
        return self._is_public_topic_admin_only

    @is_public_topic_admin_only.setter
    def is_public_topic_admin_only(self, is_public_topic_admin_only):
        """Sets the is_public_topic_admin_only of this GroupEditAction.


        :param is_public_topic_admin_only: The is_public_topic_admin_only of this GroupEditAction.  # noqa: E501
        :type: bool
        """

        self._is_public_topic_admin_only = is_public_topic_admin_only

    @property
    def allow_chat(self):
        """Gets the allow_chat of this GroupEditAction.  # noqa: E501


        :return: The allow_chat of this GroupEditAction.  # noqa: E501
        :rtype: bool
        """
        return self._allow_chat

    @allow_chat.setter
    def allow_chat(self, allow_chat):
        """Sets the allow_chat of this GroupEditAction.


        :param allow_chat: The allow_chat of this GroupEditAction.  # noqa: E501
        :type: bool
        """

        self._allow_chat = allow_chat

    @property
    def chat_security(self):
        """Gets the chat_security of this GroupEditAction.  # noqa: E501


        :return: The chat_security of this GroupEditAction.  # noqa: E501
        :rtype: int
        """
        return self._chat_security

    @chat_security.setter
    def chat_security(self, chat_security):
        """Sets the chat_security of this GroupEditAction.


        :param chat_security: The chat_security of this GroupEditAction.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if chat_security not in allowed_values:
            raise ValueError(
                "Invalid value for `chat_security` ({0}), must be one of {1}"  # noqa: E501
                .format(chat_security, allowed_values)
            )

        self._chat_security = chat_security

    @property
    def callsign(self):
        """Gets the callsign of this GroupEditAction.  # noqa: E501


        :return: The callsign of this GroupEditAction.  # noqa: E501
        :rtype: str
        """
        return self._callsign

    @callsign.setter
    def callsign(self, callsign):
        """Sets the callsign of this GroupEditAction.


        :param callsign: The callsign of this GroupEditAction.  # noqa: E501
        :type: str
        """

        self._callsign = callsign

    @property
    def locale(self):
        """Gets the locale of this GroupEditAction.  # noqa: E501


        :return: The locale of this GroupEditAction.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this GroupEditAction.


        :param locale: The locale of this GroupEditAction.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def homepage(self):
        """Gets the homepage of this GroupEditAction.  # noqa: E501


        :return: The homepage of this GroupEditAction.  # noqa: E501
        :rtype: int
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this GroupEditAction.


        :param homepage: The homepage of this GroupEditAction.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if homepage not in allowed_values:
            raise ValueError(
                "Invalid value for `homepage` ({0}), must be one of {1}"  # noqa: E501
                .format(homepage, allowed_values)
            )

        self._homepage = homepage

    @property
    def enable_invitation_messaging_for_admins(self):
        """Gets the enable_invitation_messaging_for_admins of this GroupEditAction.  # noqa: E501


        :return: The enable_invitation_messaging_for_admins of this GroupEditAction.  # noqa: E501
        :rtype: bool
        """
        return self._enable_invitation_messaging_for_admins

    @enable_invitation_messaging_for_admins.setter
    def enable_invitation_messaging_for_admins(self, enable_invitation_messaging_for_admins):
        """Sets the enable_invitation_messaging_for_admins of this GroupEditAction.


        :param enable_invitation_messaging_for_admins: The enable_invitation_messaging_for_admins of this GroupEditAction.  # noqa: E501
        :type: bool
        """

        self._enable_invitation_messaging_for_admins = enable_invitation_messaging_for_admins

    @property
    def default_publicity(self):
        """Gets the default_publicity of this GroupEditAction.  # noqa: E501


        :return: The default_publicity of this GroupEditAction.  # noqa: E501
        :rtype: int
        """
        return self._default_publicity

    @default_publicity.setter
    def default_publicity(self, default_publicity):
        """Sets the default_publicity of this GroupEditAction.


        :param default_publicity: The default_publicity of this GroupEditAction.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if default_publicity not in allowed_values:
            raise ValueError(
                "Invalid value for `default_publicity` ({0}), must be one of {1}"  # noqa: E501
                .format(default_publicity, allowed_values)
            )

        self._default_publicity = default_publicity

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
        if not isinstance(other, GroupEditAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
