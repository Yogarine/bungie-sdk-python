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


class GroupV2(object):
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
        'name': 'str',
        'group_type': 'int',
        'membership_id_created': 'int',
        'creation_date': 'datetime',
        'modification_date': 'datetime',
        'about': 'str',
        'tags': 'list[str]',
        'member_count': 'int',
        'is_public': 'bool',
        'is_public_topic_admin_only': 'bool',
        'motto': 'str',
        'allow_chat': 'bool',
        'is_default_post_public': 'bool',
        'chat_security': 'int',
        'locale': 'str',
        'avatar_image_index': 'int',
        'homepage': 'int',
        'membership_option': 'int',
        'default_publicity': 'int',
        'theme': 'str',
        'banner_path': 'str',
        'avatar_path': 'str',
        'conversation_id': 'int',
        'enable_invitation_messaging_for_admins': 'bool',
        'ban_expire_date': 'datetime',
        'features': 'GroupFeatures',
        'clan_info': 'GroupV2ClanInfoAndInvestment'
    }

    attribute_map = {
        'group_id': 'groupId',
        'name': 'name',
        'group_type': 'groupType',
        'membership_id_created': 'membershipIdCreated',
        'creation_date': 'creationDate',
        'modification_date': 'modificationDate',
        'about': 'about',
        'tags': 'tags',
        'member_count': 'memberCount',
        'is_public': 'isPublic',
        'is_public_topic_admin_only': 'isPublicTopicAdminOnly',
        'motto': 'motto',
        'allow_chat': 'allowChat',
        'is_default_post_public': 'isDefaultPostPublic',
        'chat_security': 'chatSecurity',
        'locale': 'locale',
        'avatar_image_index': 'avatarImageIndex',
        'homepage': 'homepage',
        'membership_option': 'membershipOption',
        'default_publicity': 'defaultPublicity',
        'theme': 'theme',
        'banner_path': 'bannerPath',
        'avatar_path': 'avatarPath',
        'conversation_id': 'conversationId',
        'enable_invitation_messaging_for_admins': 'enableInvitationMessagingForAdmins',
        'ban_expire_date': 'banExpireDate',
        'features': 'features',
        'clan_info': 'clanInfo'
    }

    def __init__(self, group_id=None, name=None, group_type=None, membership_id_created=None, creation_date=None, modification_date=None, about=None, tags=None, member_count=None, is_public=None, is_public_topic_admin_only=None, motto=None, allow_chat=None, is_default_post_public=None, chat_security=None, locale=None, avatar_image_index=None, homepage=None, membership_option=None, default_publicity=None, theme=None, banner_path=None, avatar_path=None, conversation_id=None, enable_invitation_messaging_for_admins=None, ban_expire_date=None, features=None, clan_info=None):  # noqa: E501
        """GroupV2 - a model defined in OpenAPI"""  # noqa: E501

        self._group_id = None
        self._name = None
        self._group_type = None
        self._membership_id_created = None
        self._creation_date = None
        self._modification_date = None
        self._about = None
        self._tags = None
        self._member_count = None
        self._is_public = None
        self._is_public_topic_admin_only = None
        self._motto = None
        self._allow_chat = None
        self._is_default_post_public = None
        self._chat_security = None
        self._locale = None
        self._avatar_image_index = None
        self._homepage = None
        self._membership_option = None
        self._default_publicity = None
        self._theme = None
        self._banner_path = None
        self._avatar_path = None
        self._conversation_id = None
        self._enable_invitation_messaging_for_admins = None
        self._ban_expire_date = None
        self._features = None
        self._clan_info = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if group_type is not None:
            self.group_type = group_type
        if membership_id_created is not None:
            self.membership_id_created = membership_id_created
        if creation_date is not None:
            self.creation_date = creation_date
        if modification_date is not None:
            self.modification_date = modification_date
        if about is not None:
            self.about = about
        if tags is not None:
            self.tags = tags
        if member_count is not None:
            self.member_count = member_count
        if is_public is not None:
            self.is_public = is_public
        if is_public_topic_admin_only is not None:
            self.is_public_topic_admin_only = is_public_topic_admin_only
        if motto is not None:
            self.motto = motto
        if allow_chat is not None:
            self.allow_chat = allow_chat
        if is_default_post_public is not None:
            self.is_default_post_public = is_default_post_public
        if chat_security is not None:
            self.chat_security = chat_security
        if locale is not None:
            self.locale = locale
        if avatar_image_index is not None:
            self.avatar_image_index = avatar_image_index
        if homepage is not None:
            self.homepage = homepage
        if membership_option is not None:
            self.membership_option = membership_option
        if default_publicity is not None:
            self.default_publicity = default_publicity
        if theme is not None:
            self.theme = theme
        if banner_path is not None:
            self.banner_path = banner_path
        if avatar_path is not None:
            self.avatar_path = avatar_path
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if enable_invitation_messaging_for_admins is not None:
            self.enable_invitation_messaging_for_admins = enable_invitation_messaging_for_admins
        self.ban_expire_date = ban_expire_date
        if features is not None:
            self.features = features
        if clan_info is not None:
            self.clan_info = clan_info

    @property
    def group_id(self):
        """Gets the group_id of this GroupV2.  # noqa: E501


        :return: The group_id of this GroupV2.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupV2.


        :param group_id: The group_id of this GroupV2.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this GroupV2.  # noqa: E501


        :return: The name of this GroupV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupV2.


        :param name: The name of this GroupV2.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group_type(self):
        """Gets the group_type of this GroupV2.  # noqa: E501


        :return: The group_type of this GroupV2.  # noqa: E501
        :rtype: int
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this GroupV2.


        :param group_type: The group_type of this GroupV2.  # noqa: E501
        :type: int
        """

        self._group_type = group_type

    @property
    def membership_id_created(self):
        """Gets the membership_id_created of this GroupV2.  # noqa: E501


        :return: The membership_id_created of this GroupV2.  # noqa: E501
        :rtype: int
        """
        return self._membership_id_created

    @membership_id_created.setter
    def membership_id_created(self, membership_id_created):
        """Sets the membership_id_created of this GroupV2.


        :param membership_id_created: The membership_id_created of this GroupV2.  # noqa: E501
        :type: int
        """

        self._membership_id_created = membership_id_created

    @property
    def creation_date(self):
        """Gets the creation_date of this GroupV2.  # noqa: E501


        :return: The creation_date of this GroupV2.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this GroupV2.


        :param creation_date: The creation_date of this GroupV2.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def modification_date(self):
        """Gets the modification_date of this GroupV2.  # noqa: E501


        :return: The modification_date of this GroupV2.  # noqa: E501
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this GroupV2.


        :param modification_date: The modification_date of this GroupV2.  # noqa: E501
        :type: datetime
        """

        self._modification_date = modification_date

    @property
    def about(self):
        """Gets the about of this GroupV2.  # noqa: E501


        :return: The about of this GroupV2.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this GroupV2.


        :param about: The about of this GroupV2.  # noqa: E501
        :type: str
        """

        self._about = about

    @property
    def tags(self):
        """Gets the tags of this GroupV2.  # noqa: E501


        :return: The tags of this GroupV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GroupV2.


        :param tags: The tags of this GroupV2.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def member_count(self):
        """Gets the member_count of this GroupV2.  # noqa: E501


        :return: The member_count of this GroupV2.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this GroupV2.


        :param member_count: The member_count of this GroupV2.  # noqa: E501
        :type: int
        """

        self._member_count = member_count

    @property
    def is_public(self):
        """Gets the is_public of this GroupV2.  # noqa: E501


        :return: The is_public of this GroupV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this GroupV2.


        :param is_public: The is_public of this GroupV2.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def is_public_topic_admin_only(self):
        """Gets the is_public_topic_admin_only of this GroupV2.  # noqa: E501


        :return: The is_public_topic_admin_only of this GroupV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_public_topic_admin_only

    @is_public_topic_admin_only.setter
    def is_public_topic_admin_only(self, is_public_topic_admin_only):
        """Sets the is_public_topic_admin_only of this GroupV2.


        :param is_public_topic_admin_only: The is_public_topic_admin_only of this GroupV2.  # noqa: E501
        :type: bool
        """

        self._is_public_topic_admin_only = is_public_topic_admin_only

    @property
    def motto(self):
        """Gets the motto of this GroupV2.  # noqa: E501


        :return: The motto of this GroupV2.  # noqa: E501
        :rtype: str
        """
        return self._motto

    @motto.setter
    def motto(self, motto):
        """Sets the motto of this GroupV2.


        :param motto: The motto of this GroupV2.  # noqa: E501
        :type: str
        """

        self._motto = motto

    @property
    def allow_chat(self):
        """Gets the allow_chat of this GroupV2.  # noqa: E501


        :return: The allow_chat of this GroupV2.  # noqa: E501
        :rtype: bool
        """
        return self._allow_chat

    @allow_chat.setter
    def allow_chat(self, allow_chat):
        """Sets the allow_chat of this GroupV2.


        :param allow_chat: The allow_chat of this GroupV2.  # noqa: E501
        :type: bool
        """

        self._allow_chat = allow_chat

    @property
    def is_default_post_public(self):
        """Gets the is_default_post_public of this GroupV2.  # noqa: E501


        :return: The is_default_post_public of this GroupV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_default_post_public

    @is_default_post_public.setter
    def is_default_post_public(self, is_default_post_public):
        """Sets the is_default_post_public of this GroupV2.


        :param is_default_post_public: The is_default_post_public of this GroupV2.  # noqa: E501
        :type: bool
        """

        self._is_default_post_public = is_default_post_public

    @property
    def chat_security(self):
        """Gets the chat_security of this GroupV2.  # noqa: E501


        :return: The chat_security of this GroupV2.  # noqa: E501
        :rtype: int
        """
        return self._chat_security

    @chat_security.setter
    def chat_security(self, chat_security):
        """Sets the chat_security of this GroupV2.


        :param chat_security: The chat_security of this GroupV2.  # noqa: E501
        :type: int
        """

        self._chat_security = chat_security

    @property
    def locale(self):
        """Gets the locale of this GroupV2.  # noqa: E501


        :return: The locale of this GroupV2.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this GroupV2.


        :param locale: The locale of this GroupV2.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def avatar_image_index(self):
        """Gets the avatar_image_index of this GroupV2.  # noqa: E501


        :return: The avatar_image_index of this GroupV2.  # noqa: E501
        :rtype: int
        """
        return self._avatar_image_index

    @avatar_image_index.setter
    def avatar_image_index(self, avatar_image_index):
        """Sets the avatar_image_index of this GroupV2.


        :param avatar_image_index: The avatar_image_index of this GroupV2.  # noqa: E501
        :type: int
        """

        self._avatar_image_index = avatar_image_index

    @property
    def homepage(self):
        """Gets the homepage of this GroupV2.  # noqa: E501


        :return: The homepage of this GroupV2.  # noqa: E501
        :rtype: int
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this GroupV2.


        :param homepage: The homepage of this GroupV2.  # noqa: E501
        :type: int
        """

        self._homepage = homepage

    @property
    def membership_option(self):
        """Gets the membership_option of this GroupV2.  # noqa: E501


        :return: The membership_option of this GroupV2.  # noqa: E501
        :rtype: int
        """
        return self._membership_option

    @membership_option.setter
    def membership_option(self, membership_option):
        """Sets the membership_option of this GroupV2.


        :param membership_option: The membership_option of this GroupV2.  # noqa: E501
        :type: int
        """

        self._membership_option = membership_option

    @property
    def default_publicity(self):
        """Gets the default_publicity of this GroupV2.  # noqa: E501


        :return: The default_publicity of this GroupV2.  # noqa: E501
        :rtype: int
        """
        return self._default_publicity

    @default_publicity.setter
    def default_publicity(self, default_publicity):
        """Sets the default_publicity of this GroupV2.


        :param default_publicity: The default_publicity of this GroupV2.  # noqa: E501
        :type: int
        """

        self._default_publicity = default_publicity

    @property
    def theme(self):
        """Gets the theme of this GroupV2.  # noqa: E501


        :return: The theme of this GroupV2.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this GroupV2.


        :param theme: The theme of this GroupV2.  # noqa: E501
        :type: str
        """

        self._theme = theme

    @property
    def banner_path(self):
        """Gets the banner_path of this GroupV2.  # noqa: E501


        :return: The banner_path of this GroupV2.  # noqa: E501
        :rtype: str
        """
        return self._banner_path

    @banner_path.setter
    def banner_path(self, banner_path):
        """Sets the banner_path of this GroupV2.


        :param banner_path: The banner_path of this GroupV2.  # noqa: E501
        :type: str
        """

        self._banner_path = banner_path

    @property
    def avatar_path(self):
        """Gets the avatar_path of this GroupV2.  # noqa: E501


        :return: The avatar_path of this GroupV2.  # noqa: E501
        :rtype: str
        """
        return self._avatar_path

    @avatar_path.setter
    def avatar_path(self, avatar_path):
        """Sets the avatar_path of this GroupV2.


        :param avatar_path: The avatar_path of this GroupV2.  # noqa: E501
        :type: str
        """

        self._avatar_path = avatar_path

    @property
    def conversation_id(self):
        """Gets the conversation_id of this GroupV2.  # noqa: E501


        :return: The conversation_id of this GroupV2.  # noqa: E501
        :rtype: int
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this GroupV2.


        :param conversation_id: The conversation_id of this GroupV2.  # noqa: E501
        :type: int
        """

        self._conversation_id = conversation_id

    @property
    def enable_invitation_messaging_for_admins(self):
        """Gets the enable_invitation_messaging_for_admins of this GroupV2.  # noqa: E501


        :return: The enable_invitation_messaging_for_admins of this GroupV2.  # noqa: E501
        :rtype: bool
        """
        return self._enable_invitation_messaging_for_admins

    @enable_invitation_messaging_for_admins.setter
    def enable_invitation_messaging_for_admins(self, enable_invitation_messaging_for_admins):
        """Sets the enable_invitation_messaging_for_admins of this GroupV2.


        :param enable_invitation_messaging_for_admins: The enable_invitation_messaging_for_admins of this GroupV2.  # noqa: E501
        :type: bool
        """

        self._enable_invitation_messaging_for_admins = enable_invitation_messaging_for_admins

    @property
    def ban_expire_date(self):
        """Gets the ban_expire_date of this GroupV2.  # noqa: E501


        :return: The ban_expire_date of this GroupV2.  # noqa: E501
        :rtype: datetime
        """
        return self._ban_expire_date

    @ban_expire_date.setter
    def ban_expire_date(self, ban_expire_date):
        """Sets the ban_expire_date of this GroupV2.


        :param ban_expire_date: The ban_expire_date of this GroupV2.  # noqa: E501
        :type: datetime
        """

        self._ban_expire_date = ban_expire_date

    @property
    def features(self):
        """Gets the features of this GroupV2.  # noqa: E501


        :return: The features of this GroupV2.  # noqa: E501
        :rtype: GroupFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this GroupV2.


        :param features: The features of this GroupV2.  # noqa: E501
        :type: GroupFeatures
        """

        self._features = features

    @property
    def clan_info(self):
        """Gets the clan_info of this GroupV2.  # noqa: E501


        :return: The clan_info of this GroupV2.  # noqa: E501
        :rtype: GroupV2ClanInfoAndInvestment
        """
        return self._clan_info

    @clan_info.setter
    def clan_info(self, clan_info):
        """Sets the clan_info of this GroupV2.


        :param clan_info: The clan_info of this GroupV2.  # noqa: E501
        :type: GroupV2ClanInfoAndInvestment
        """

        self._clan_info = clan_info

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
        if not isinstance(other, GroupV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
