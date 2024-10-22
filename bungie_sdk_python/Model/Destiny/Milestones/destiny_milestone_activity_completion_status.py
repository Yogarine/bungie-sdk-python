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


class DestinyMilestoneActivityCompletionStatus(object):
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
        'completed': 'bool',
        'phases': 'list[DestinyMilestoneActivityPhase]'
    }

    attribute_map = {
        'completed': 'completed',
        'phases': 'phases'
    }

    def __init__(self, completed=None, phases=None):  # noqa: E501
        """DestinyMilestoneActivityCompletionStatus - a model defined in OpenAPI"""  # noqa: E501

        self._completed = None
        self._phases = None
        self.discriminator = None

        if completed is not None:
            self.completed = completed
        if phases is not None:
            self.phases = phases

    @property
    def completed(self):
        """Gets the completed of this DestinyMilestoneActivityCompletionStatus.  # noqa: E501

        If the activity has been \"completed\", that information will be returned here.  # noqa: E501

        :return: The completed of this DestinyMilestoneActivityCompletionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this DestinyMilestoneActivityCompletionStatus.

        If the activity has been \"completed\", that information will be returned here.  # noqa: E501

        :param completed: The completed of this DestinyMilestoneActivityCompletionStatus.  # noqa: E501
        :type: bool
        """

        self._completed = completed

    @property
    def phases(self):
        """Gets the phases of this DestinyMilestoneActivityCompletionStatus.  # noqa: E501

        If the Activity has discrete \"phases\" that we can track, that info will be here. Otherwise, this value will be NULL. Note that this is a list and not a dictionary: the order implies the ascending order of phases or progression in this activity.  # noqa: E501

        :return: The phases of this DestinyMilestoneActivityCompletionStatus.  # noqa: E501
        :rtype: list[DestinyMilestoneActivityPhase]
        """
        return self._phases

    @phases.setter
    def phases(self, phases):
        """Sets the phases of this DestinyMilestoneActivityCompletionStatus.

        If the Activity has discrete \"phases\" that we can track, that info will be here. Otherwise, this value will be NULL. Note that this is a list and not a dictionary: the order implies the ascending order of phases or progression in this activity.  # noqa: E501

        :param phases: The phases of this DestinyMilestoneActivityCompletionStatus.  # noqa: E501
        :type: list[DestinyMilestoneActivityPhase]
        """

        self._phases = phases

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
        if not isinstance(other, DestinyMilestoneActivityCompletionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
