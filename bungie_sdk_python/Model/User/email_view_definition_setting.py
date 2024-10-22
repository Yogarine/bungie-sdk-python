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


class EmailViewDefinitionSetting(object):
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
        'localization': 'dict(str, EMailSettingLocalization)',
        'set_by_default': 'bool',
        'opt_in_aggregate_value': 'int',
        'subscriptions': 'list[EmailSubscriptionDefinition]'
    }

    attribute_map = {
        'name': 'name',
        'localization': 'localization',
        'set_by_default': 'setByDefault',
        'opt_in_aggregate_value': 'optInAggregateValue',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, name=None, localization=None, set_by_default=None, opt_in_aggregate_value=None, subscriptions=None):  # noqa: E501
        """EmailViewDefinitionSetting - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._localization = None
        self._set_by_default = None
        self._opt_in_aggregate_value = None
        self._subscriptions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if localization is not None:
            self.localization = localization
        if set_by_default is not None:
            self.set_by_default = set_by_default
        if opt_in_aggregate_value is not None:
            self.opt_in_aggregate_value = opt_in_aggregate_value
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def name(self):
        """Gets the name of this EmailViewDefinitionSetting.  # noqa: E501

        The identifier for this UI Setting, which can be used to relate it to custom strings or other data as desired.  # noqa: E501

        :return: The name of this EmailViewDefinitionSetting.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailViewDefinitionSetting.

        The identifier for this UI Setting, which can be used to relate it to custom strings or other data as desired.  # noqa: E501

        :param name: The name of this EmailViewDefinitionSetting.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def localization(self):
        """Gets the localization of this EmailViewDefinitionSetting.  # noqa: E501

        A dictionary of localized text for the EMail setting, keyed by the locale.  # noqa: E501

        :return: The localization of this EmailViewDefinitionSetting.  # noqa: E501
        :rtype: dict(str, EMailSettingLocalization)
        """
        return self._localization

    @localization.setter
    def localization(self, localization):
        """Sets the localization of this EmailViewDefinitionSetting.

        A dictionary of localized text for the EMail setting, keyed by the locale.  # noqa: E501

        :param localization: The localization of this EmailViewDefinitionSetting.  # noqa: E501
        :type: dict(str, EMailSettingLocalization)
        """

        self._localization = localization

    @property
    def set_by_default(self):
        """Gets the set_by_default of this EmailViewDefinitionSetting.  # noqa: E501

        If true, this setting should be set by default if the user hasn't chosen whether it's set or cleared yet.  # noqa: E501

        :return: The set_by_default of this EmailViewDefinitionSetting.  # noqa: E501
        :rtype: bool
        """
        return self._set_by_default

    @set_by_default.setter
    def set_by_default(self, set_by_default):
        """Sets the set_by_default of this EmailViewDefinitionSetting.

        If true, this setting should be set by default if the user hasn't chosen whether it's set or cleared yet.  # noqa: E501

        :param set_by_default: The set_by_default of this EmailViewDefinitionSetting.  # noqa: E501
        :type: bool
        """

        self._set_by_default = set_by_default

    @property
    def opt_in_aggregate_value(self):
        """Gets the opt_in_aggregate_value of this EmailViewDefinitionSetting.  # noqa: E501

        The OptInFlags value to set or clear if this setting is set or cleared in the UI. It is the aggregate of all underlying opt-in flags related to this setting.  # noqa: E501

        :return: The opt_in_aggregate_value of this EmailViewDefinitionSetting.  # noqa: E501
        :rtype: int
        """
        return self._opt_in_aggregate_value

    @opt_in_aggregate_value.setter
    def opt_in_aggregate_value(self, opt_in_aggregate_value):
        """Sets the opt_in_aggregate_value of this EmailViewDefinitionSetting.

        The OptInFlags value to set or clear if this setting is set or cleared in the UI. It is the aggregate of all underlying opt-in flags related to this setting.  # noqa: E501

        :param opt_in_aggregate_value: The opt_in_aggregate_value of this EmailViewDefinitionSetting.  # noqa: E501
        :type: int
        """

        self._opt_in_aggregate_value = opt_in_aggregate_value

    @property
    def subscriptions(self):
        """Gets the subscriptions of this EmailViewDefinitionSetting.  # noqa: E501

        The subscriptions to show as children of this setting, if any.  # noqa: E501

        :return: The subscriptions of this EmailViewDefinitionSetting.  # noqa: E501
        :rtype: list[EmailSubscriptionDefinition]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this EmailViewDefinitionSetting.

        The subscriptions to show as children of this setting, if any.  # noqa: E501

        :param subscriptions: The subscriptions of this EmailViewDefinitionSetting.  # noqa: E501
        :type: list[EmailSubscriptionDefinition]
        """

        self._subscriptions = subscriptions

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
        if not isinstance(other, EmailViewDefinitionSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
