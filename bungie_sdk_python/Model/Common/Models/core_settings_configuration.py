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


class CoreSettingsConfiguration(object):
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
        'environment': 'str',
        'systems': 'dict(str, CoreSystem)',
        'ignore_reasons': 'list[CoreSetting]',
        'forum_categories': 'list[CoreSetting]',
        'group_avatars': 'list[CoreSetting]',
        'destiny_membership_types': 'list[CoreSetting]',
        'recruitment_platform_tags': 'list[CoreSetting]',
        'recruitment_misc_tags': 'list[CoreSetting]',
        'recruitment_activities': 'list[CoreSetting]',
        'user_content_locales': 'list[CoreSetting]',
        'system_content_locales': 'list[CoreSetting]',
        'clan_banner_decals': 'list[CoreSetting]',
        'clan_banner_decal_colors': 'list[CoreSetting]',
        'clan_banner_gonfalons': 'list[CoreSetting]',
        'clan_banner_gonfalon_colors': 'list[CoreSetting]',
        'clan_banner_gonfalon_details': 'list[CoreSetting]',
        'clan_banner_gonfalon_detail_colors': 'list[CoreSetting]',
        'clan_banner_standards': 'list[CoreSetting]',
        'destiny2_core_settings': 'Destiny2CoreSettings',
        'email_settings': 'EmailSettings'
    }

    attribute_map = {
        'environment': 'environment',
        'systems': 'systems',
        'ignore_reasons': 'ignoreReasons',
        'forum_categories': 'forumCategories',
        'group_avatars': 'groupAvatars',
        'destiny_membership_types': 'destinyMembershipTypes',
        'recruitment_platform_tags': 'recruitmentPlatformTags',
        'recruitment_misc_tags': 'recruitmentMiscTags',
        'recruitment_activities': 'recruitmentActivities',
        'user_content_locales': 'userContentLocales',
        'system_content_locales': 'systemContentLocales',
        'clan_banner_decals': 'clanBannerDecals',
        'clan_banner_decal_colors': 'clanBannerDecalColors',
        'clan_banner_gonfalons': 'clanBannerGonfalons',
        'clan_banner_gonfalon_colors': 'clanBannerGonfalonColors',
        'clan_banner_gonfalon_details': 'clanBannerGonfalonDetails',
        'clan_banner_gonfalon_detail_colors': 'clanBannerGonfalonDetailColors',
        'clan_banner_standards': 'clanBannerStandards',
        'destiny2_core_settings': 'destiny2CoreSettings',
        'email_settings': 'emailSettings'
    }

    def __init__(self, environment=None, systems=None, ignore_reasons=None, forum_categories=None, group_avatars=None, destiny_membership_types=None, recruitment_platform_tags=None, recruitment_misc_tags=None, recruitment_activities=None, user_content_locales=None, system_content_locales=None, clan_banner_decals=None, clan_banner_decal_colors=None, clan_banner_gonfalons=None, clan_banner_gonfalon_colors=None, clan_banner_gonfalon_details=None, clan_banner_gonfalon_detail_colors=None, clan_banner_standards=None, destiny2_core_settings=None, email_settings=None):  # noqa: E501
        """CoreSettingsConfiguration - a model defined in OpenAPI"""  # noqa: E501

        self._environment = None
        self._systems = None
        self._ignore_reasons = None
        self._forum_categories = None
        self._group_avatars = None
        self._destiny_membership_types = None
        self._recruitment_platform_tags = None
        self._recruitment_misc_tags = None
        self._recruitment_activities = None
        self._user_content_locales = None
        self._system_content_locales = None
        self._clan_banner_decals = None
        self._clan_banner_decal_colors = None
        self._clan_banner_gonfalons = None
        self._clan_banner_gonfalon_colors = None
        self._clan_banner_gonfalon_details = None
        self._clan_banner_gonfalon_detail_colors = None
        self._clan_banner_standards = None
        self._destiny2_core_settings = None
        self._email_settings = None
        self.discriminator = None

        if environment is not None:
            self.environment = environment
        if systems is not None:
            self.systems = systems
        if ignore_reasons is not None:
            self.ignore_reasons = ignore_reasons
        if forum_categories is not None:
            self.forum_categories = forum_categories
        if group_avatars is not None:
            self.group_avatars = group_avatars
        if destiny_membership_types is not None:
            self.destiny_membership_types = destiny_membership_types
        if recruitment_platform_tags is not None:
            self.recruitment_platform_tags = recruitment_platform_tags
        if recruitment_misc_tags is not None:
            self.recruitment_misc_tags = recruitment_misc_tags
        if recruitment_activities is not None:
            self.recruitment_activities = recruitment_activities
        if user_content_locales is not None:
            self.user_content_locales = user_content_locales
        if system_content_locales is not None:
            self.system_content_locales = system_content_locales
        if clan_banner_decals is not None:
            self.clan_banner_decals = clan_banner_decals
        if clan_banner_decal_colors is not None:
            self.clan_banner_decal_colors = clan_banner_decal_colors
        if clan_banner_gonfalons is not None:
            self.clan_banner_gonfalons = clan_banner_gonfalons
        if clan_banner_gonfalon_colors is not None:
            self.clan_banner_gonfalon_colors = clan_banner_gonfalon_colors
        if clan_banner_gonfalon_details is not None:
            self.clan_banner_gonfalon_details = clan_banner_gonfalon_details
        if clan_banner_gonfalon_detail_colors is not None:
            self.clan_banner_gonfalon_detail_colors = clan_banner_gonfalon_detail_colors
        if clan_banner_standards is not None:
            self.clan_banner_standards = clan_banner_standards
        if destiny2_core_settings is not None:
            self.destiny2_core_settings = destiny2_core_settings
        if email_settings is not None:
            self.email_settings = email_settings

    @property
    def environment(self):
        """Gets the environment of this CoreSettingsConfiguration.  # noqa: E501


        :return: The environment of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this CoreSettingsConfiguration.


        :param environment: The environment of this CoreSettingsConfiguration.  # noqa: E501
        :type: str
        """

        self._environment = environment

    @property
    def systems(self):
        """Gets the systems of this CoreSettingsConfiguration.  # noqa: E501


        :return: The systems of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: dict(str, CoreSystem)
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this CoreSettingsConfiguration.


        :param systems: The systems of this CoreSettingsConfiguration.  # noqa: E501
        :type: dict(str, CoreSystem)
        """

        self._systems = systems

    @property
    def ignore_reasons(self):
        """Gets the ignore_reasons of this CoreSettingsConfiguration.  # noqa: E501


        :return: The ignore_reasons of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._ignore_reasons

    @ignore_reasons.setter
    def ignore_reasons(self, ignore_reasons):
        """Sets the ignore_reasons of this CoreSettingsConfiguration.


        :param ignore_reasons: The ignore_reasons of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._ignore_reasons = ignore_reasons

    @property
    def forum_categories(self):
        """Gets the forum_categories of this CoreSettingsConfiguration.  # noqa: E501


        :return: The forum_categories of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._forum_categories

    @forum_categories.setter
    def forum_categories(self, forum_categories):
        """Sets the forum_categories of this CoreSettingsConfiguration.


        :param forum_categories: The forum_categories of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._forum_categories = forum_categories

    @property
    def group_avatars(self):
        """Gets the group_avatars of this CoreSettingsConfiguration.  # noqa: E501


        :return: The group_avatars of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._group_avatars

    @group_avatars.setter
    def group_avatars(self, group_avatars):
        """Sets the group_avatars of this CoreSettingsConfiguration.


        :param group_avatars: The group_avatars of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._group_avatars = group_avatars

    @property
    def destiny_membership_types(self):
        """Gets the destiny_membership_types of this CoreSettingsConfiguration.  # noqa: E501


        :return: The destiny_membership_types of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._destiny_membership_types

    @destiny_membership_types.setter
    def destiny_membership_types(self, destiny_membership_types):
        """Sets the destiny_membership_types of this CoreSettingsConfiguration.


        :param destiny_membership_types: The destiny_membership_types of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._destiny_membership_types = destiny_membership_types

    @property
    def recruitment_platform_tags(self):
        """Gets the recruitment_platform_tags of this CoreSettingsConfiguration.  # noqa: E501


        :return: The recruitment_platform_tags of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._recruitment_platform_tags

    @recruitment_platform_tags.setter
    def recruitment_platform_tags(self, recruitment_platform_tags):
        """Sets the recruitment_platform_tags of this CoreSettingsConfiguration.


        :param recruitment_platform_tags: The recruitment_platform_tags of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._recruitment_platform_tags = recruitment_platform_tags

    @property
    def recruitment_misc_tags(self):
        """Gets the recruitment_misc_tags of this CoreSettingsConfiguration.  # noqa: E501


        :return: The recruitment_misc_tags of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._recruitment_misc_tags

    @recruitment_misc_tags.setter
    def recruitment_misc_tags(self, recruitment_misc_tags):
        """Sets the recruitment_misc_tags of this CoreSettingsConfiguration.


        :param recruitment_misc_tags: The recruitment_misc_tags of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._recruitment_misc_tags = recruitment_misc_tags

    @property
    def recruitment_activities(self):
        """Gets the recruitment_activities of this CoreSettingsConfiguration.  # noqa: E501


        :return: The recruitment_activities of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._recruitment_activities

    @recruitment_activities.setter
    def recruitment_activities(self, recruitment_activities):
        """Sets the recruitment_activities of this CoreSettingsConfiguration.


        :param recruitment_activities: The recruitment_activities of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._recruitment_activities = recruitment_activities

    @property
    def user_content_locales(self):
        """Gets the user_content_locales of this CoreSettingsConfiguration.  # noqa: E501


        :return: The user_content_locales of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._user_content_locales

    @user_content_locales.setter
    def user_content_locales(self, user_content_locales):
        """Sets the user_content_locales of this CoreSettingsConfiguration.


        :param user_content_locales: The user_content_locales of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._user_content_locales = user_content_locales

    @property
    def system_content_locales(self):
        """Gets the system_content_locales of this CoreSettingsConfiguration.  # noqa: E501


        :return: The system_content_locales of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._system_content_locales

    @system_content_locales.setter
    def system_content_locales(self, system_content_locales):
        """Sets the system_content_locales of this CoreSettingsConfiguration.


        :param system_content_locales: The system_content_locales of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._system_content_locales = system_content_locales

    @property
    def clan_banner_decals(self):
        """Gets the clan_banner_decals of this CoreSettingsConfiguration.  # noqa: E501


        :return: The clan_banner_decals of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._clan_banner_decals

    @clan_banner_decals.setter
    def clan_banner_decals(self, clan_banner_decals):
        """Sets the clan_banner_decals of this CoreSettingsConfiguration.


        :param clan_banner_decals: The clan_banner_decals of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._clan_banner_decals = clan_banner_decals

    @property
    def clan_banner_decal_colors(self):
        """Gets the clan_banner_decal_colors of this CoreSettingsConfiguration.  # noqa: E501


        :return: The clan_banner_decal_colors of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._clan_banner_decal_colors

    @clan_banner_decal_colors.setter
    def clan_banner_decal_colors(self, clan_banner_decal_colors):
        """Sets the clan_banner_decal_colors of this CoreSettingsConfiguration.


        :param clan_banner_decal_colors: The clan_banner_decal_colors of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._clan_banner_decal_colors = clan_banner_decal_colors

    @property
    def clan_banner_gonfalons(self):
        """Gets the clan_banner_gonfalons of this CoreSettingsConfiguration.  # noqa: E501


        :return: The clan_banner_gonfalons of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._clan_banner_gonfalons

    @clan_banner_gonfalons.setter
    def clan_banner_gonfalons(self, clan_banner_gonfalons):
        """Sets the clan_banner_gonfalons of this CoreSettingsConfiguration.


        :param clan_banner_gonfalons: The clan_banner_gonfalons of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._clan_banner_gonfalons = clan_banner_gonfalons

    @property
    def clan_banner_gonfalon_colors(self):
        """Gets the clan_banner_gonfalon_colors of this CoreSettingsConfiguration.  # noqa: E501


        :return: The clan_banner_gonfalon_colors of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._clan_banner_gonfalon_colors

    @clan_banner_gonfalon_colors.setter
    def clan_banner_gonfalon_colors(self, clan_banner_gonfalon_colors):
        """Sets the clan_banner_gonfalon_colors of this CoreSettingsConfiguration.


        :param clan_banner_gonfalon_colors: The clan_banner_gonfalon_colors of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._clan_banner_gonfalon_colors = clan_banner_gonfalon_colors

    @property
    def clan_banner_gonfalon_details(self):
        """Gets the clan_banner_gonfalon_details of this CoreSettingsConfiguration.  # noqa: E501


        :return: The clan_banner_gonfalon_details of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._clan_banner_gonfalon_details

    @clan_banner_gonfalon_details.setter
    def clan_banner_gonfalon_details(self, clan_banner_gonfalon_details):
        """Sets the clan_banner_gonfalon_details of this CoreSettingsConfiguration.


        :param clan_banner_gonfalon_details: The clan_banner_gonfalon_details of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._clan_banner_gonfalon_details = clan_banner_gonfalon_details

    @property
    def clan_banner_gonfalon_detail_colors(self):
        """Gets the clan_banner_gonfalon_detail_colors of this CoreSettingsConfiguration.  # noqa: E501


        :return: The clan_banner_gonfalon_detail_colors of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._clan_banner_gonfalon_detail_colors

    @clan_banner_gonfalon_detail_colors.setter
    def clan_banner_gonfalon_detail_colors(self, clan_banner_gonfalon_detail_colors):
        """Sets the clan_banner_gonfalon_detail_colors of this CoreSettingsConfiguration.


        :param clan_banner_gonfalon_detail_colors: The clan_banner_gonfalon_detail_colors of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._clan_banner_gonfalon_detail_colors = clan_banner_gonfalon_detail_colors

    @property
    def clan_banner_standards(self):
        """Gets the clan_banner_standards of this CoreSettingsConfiguration.  # noqa: E501


        :return: The clan_banner_standards of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: list[CoreSetting]
        """
        return self._clan_banner_standards

    @clan_banner_standards.setter
    def clan_banner_standards(self, clan_banner_standards):
        """Sets the clan_banner_standards of this CoreSettingsConfiguration.


        :param clan_banner_standards: The clan_banner_standards of this CoreSettingsConfiguration.  # noqa: E501
        :type: list[CoreSetting]
        """

        self._clan_banner_standards = clan_banner_standards

    @property
    def destiny2_core_settings(self):
        """Gets the destiny2_core_settings of this CoreSettingsConfiguration.  # noqa: E501


        :return: The destiny2_core_settings of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: Destiny2CoreSettings
        """
        return self._destiny2_core_settings

    @destiny2_core_settings.setter
    def destiny2_core_settings(self, destiny2_core_settings):
        """Sets the destiny2_core_settings of this CoreSettingsConfiguration.


        :param destiny2_core_settings: The destiny2_core_settings of this CoreSettingsConfiguration.  # noqa: E501
        :type: Destiny2CoreSettings
        """

        self._destiny2_core_settings = destiny2_core_settings

    @property
    def email_settings(self):
        """Gets the email_settings of this CoreSettingsConfiguration.  # noqa: E501


        :return: The email_settings of this CoreSettingsConfiguration.  # noqa: E501
        :rtype: EmailSettings
        """
        return self._email_settings

    @email_settings.setter
    def email_settings(self, email_settings):
        """Sets the email_settings of this CoreSettingsConfiguration.


        :param email_settings: The email_settings of this CoreSettingsConfiguration.  # noqa: E501
        :type: EmailSettings
        """

        self._email_settings = email_settings

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
        if not isinstance(other, CoreSettingsConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
