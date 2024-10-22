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


class DestinyTalentNodeStatBlock(object):
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
        'current_step_stats': 'list[DestinyStat]',
        'next_step_stats': 'list[DestinyStat]'
    }

    attribute_map = {
        'current_step_stats': 'currentStepStats',
        'next_step_stats': 'nextStepStats'
    }

    def __init__(self, current_step_stats=None, next_step_stats=None):  # noqa: E501
        """DestinyTalentNodeStatBlock - a model defined in OpenAPI"""  # noqa: E501

        self._current_step_stats = None
        self._next_step_stats = None
        self.discriminator = None

        if current_step_stats is not None:
            self.current_step_stats = current_step_stats
        if next_step_stats is not None:
            self.next_step_stats = next_step_stats

    @property
    def current_step_stats(self):
        """Gets the current_step_stats of this DestinyTalentNodeStatBlock.  # noqa: E501

        The stat benefits conferred when this talent node is activated for the current Step that is active on the node.  # noqa: E501

        :return: The current_step_stats of this DestinyTalentNodeStatBlock.  # noqa: E501
        :rtype: list[DestinyStat]
        """
        return self._current_step_stats

    @current_step_stats.setter
    def current_step_stats(self, current_step_stats):
        """Sets the current_step_stats of this DestinyTalentNodeStatBlock.

        The stat benefits conferred when this talent node is activated for the current Step that is active on the node.  # noqa: E501

        :param current_step_stats: The current_step_stats of this DestinyTalentNodeStatBlock.  # noqa: E501
        :type: list[DestinyStat]
        """

        self._current_step_stats = current_step_stats

    @property
    def next_step_stats(self):
        """Gets the next_step_stats of this DestinyTalentNodeStatBlock.  # noqa: E501

        This is a holdover from the old days of Destiny 1, when a node could be activated multiple times, conferring multiple steps worth of benefits: you would use this property to show what activating the \"next\" step on the node would provide vs. what the current step is providing. While Nodes are currently not being used this way, the underlying system for this functionality still exists. I hesitate to remove this property while the ability for designers to make such a talent grid still exists. Whether you want to show it is up to you.  # noqa: E501

        :return: The next_step_stats of this DestinyTalentNodeStatBlock.  # noqa: E501
        :rtype: list[DestinyStat]
        """
        return self._next_step_stats

    @next_step_stats.setter
    def next_step_stats(self, next_step_stats):
        """Sets the next_step_stats of this DestinyTalentNodeStatBlock.

        This is a holdover from the old days of Destiny 1, when a node could be activated multiple times, conferring multiple steps worth of benefits: you would use this property to show what activating the \"next\" step on the node would provide vs. what the current step is providing. While Nodes are currently not being used this way, the underlying system for this functionality still exists. I hesitate to remove this property while the ability for designers to make such a talent grid still exists. Whether you want to show it is up to you.  # noqa: E501

        :param next_step_stats: The next_step_stats of this DestinyTalentNodeStatBlock.  # noqa: E501
        :type: list[DestinyStat]
        """

        self._next_step_stats = next_step_stats

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
        if not isinstance(other, DestinyTalentNodeStatBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
