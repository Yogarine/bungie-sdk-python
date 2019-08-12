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


class EmailSettings(object):
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
        'opt_in_definitions': 'dict(str, EmailOptInDefinition)',
        'subscription_definitions': 'dict(str, EmailSubscriptionDefinition)',
        'views': 'dict(str, EmailViewDefinition)'
    }

    attribute_map = {
        'opt_in_definitions': 'optInDefinitions',
        'subscription_definitions': 'subscriptionDefinitions',
        'views': 'views'
    }

    def __init__(self, opt_in_definitions=None, subscription_definitions=None, views=None):  # noqa: E501
        """EmailSettings - a model defined in OpenAPI"""  # noqa: E501

        self._opt_in_definitions = None
        self._subscription_definitions = None
        self._views = None
        self.discriminator = None

        if opt_in_definitions is not None:
            self.opt_in_definitions = opt_in_definitions
        if subscription_definitions is not None:
            self.subscription_definitions = subscription_definitions
        if views is not None:
            self.views = views

    @property
    def opt_in_definitions(self):
        """Gets the opt_in_definitions of this EmailSettings.  # noqa: E501

        Keyed by the name identifier of the opt-in definition.  # noqa: E501

        :return: The opt_in_definitions of this EmailSettings.  # noqa: E501
        :rtype: dict(str, EmailOptInDefinition)
        """
        return self._opt_in_definitions

    @opt_in_definitions.setter
    def opt_in_definitions(self, opt_in_definitions):
        """Sets the opt_in_definitions of this EmailSettings.

        Keyed by the name identifier of the opt-in definition.  # noqa: E501

        :param opt_in_definitions: The opt_in_definitions of this EmailSettings.  # noqa: E501
        :type: dict(str, EmailOptInDefinition)
        """

        self._opt_in_definitions = opt_in_definitions

    @property
    def subscription_definitions(self):
        """Gets the subscription_definitions of this EmailSettings.  # noqa: E501

        Keyed by the name identifier of the Subscription definition.  # noqa: E501

        :return: The subscription_definitions of this EmailSettings.  # noqa: E501
        :rtype: dict(str, EmailSubscriptionDefinition)
        """
        return self._subscription_definitions

    @subscription_definitions.setter
    def subscription_definitions(self, subscription_definitions):
        """Sets the subscription_definitions of this EmailSettings.

        Keyed by the name identifier of the Subscription definition.  # noqa: E501

        :param subscription_definitions: The subscription_definitions of this EmailSettings.  # noqa: E501
        :type: dict(str, EmailSubscriptionDefinition)
        """

        self._subscription_definitions = subscription_definitions

    @property
    def views(self):
        """Gets the views of this EmailSettings.  # noqa: E501

        Keyed by the name identifier of the View definition.  # noqa: E501

        :return: The views of this EmailSettings.  # noqa: E501
        :rtype: dict(str, EmailViewDefinition)
        """
        return self._views

    @views.setter
    def views(self, views):
        """Sets the views of this EmailSettings.

        Keyed by the name identifier of the View definition.  # noqa: E501

        :param views: The views of this EmailSettings.  # noqa: E501
        :type: dict(str, EmailViewDefinition)
        """

        self._views = views

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
        if not isinstance(other, EmailSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other