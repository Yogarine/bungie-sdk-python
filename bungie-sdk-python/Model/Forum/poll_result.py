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


class PollResult(object):
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
        'answer_text': 'str',
        'answer_slot': 'int',
        'last_vote_date': 'datetime',
        'votes': 'int',
        'requesting_user_voted': 'bool'
    }

    attribute_map = {
        'answer_text': 'answerText',
        'answer_slot': 'answerSlot',
        'last_vote_date': 'lastVoteDate',
        'votes': 'votes',
        'requesting_user_voted': 'requestingUserVoted'
    }

    def __init__(self, answer_text=None, answer_slot=None, last_vote_date=None, votes=None, requesting_user_voted=None):  # noqa: E501
        """PollResult - a model defined in OpenAPI"""  # noqa: E501

        self._answer_text = None
        self._answer_slot = None
        self._last_vote_date = None
        self._votes = None
        self._requesting_user_voted = None
        self.discriminator = None

        if answer_text is not None:
            self.answer_text = answer_text
        if answer_slot is not None:
            self.answer_slot = answer_slot
        if last_vote_date is not None:
            self.last_vote_date = last_vote_date
        if votes is not None:
            self.votes = votes
        if requesting_user_voted is not None:
            self.requesting_user_voted = requesting_user_voted

    @property
    def answer_text(self):
        """Gets the answer_text of this PollResult.  # noqa: E501


        :return: The answer_text of this PollResult.  # noqa: E501
        :rtype: str
        """
        return self._answer_text

    @answer_text.setter
    def answer_text(self, answer_text):
        """Sets the answer_text of this PollResult.


        :param answer_text: The answer_text of this PollResult.  # noqa: E501
        :type: str
        """

        self._answer_text = answer_text

    @property
    def answer_slot(self):
        """Gets the answer_slot of this PollResult.  # noqa: E501


        :return: The answer_slot of this PollResult.  # noqa: E501
        :rtype: int
        """
        return self._answer_slot

    @answer_slot.setter
    def answer_slot(self, answer_slot):
        """Sets the answer_slot of this PollResult.


        :param answer_slot: The answer_slot of this PollResult.  # noqa: E501
        :type: int
        """

        self._answer_slot = answer_slot

    @property
    def last_vote_date(self):
        """Gets the last_vote_date of this PollResult.  # noqa: E501


        :return: The last_vote_date of this PollResult.  # noqa: E501
        :rtype: datetime
        """
        return self._last_vote_date

    @last_vote_date.setter
    def last_vote_date(self, last_vote_date):
        """Sets the last_vote_date of this PollResult.


        :param last_vote_date: The last_vote_date of this PollResult.  # noqa: E501
        :type: datetime
        """

        self._last_vote_date = last_vote_date

    @property
    def votes(self):
        """Gets the votes of this PollResult.  # noqa: E501


        :return: The votes of this PollResult.  # noqa: E501
        :rtype: int
        """
        return self._votes

    @votes.setter
    def votes(self, votes):
        """Sets the votes of this PollResult.


        :param votes: The votes of this PollResult.  # noqa: E501
        :type: int
        """

        self._votes = votes

    @property
    def requesting_user_voted(self):
        """Gets the requesting_user_voted of this PollResult.  # noqa: E501


        :return: The requesting_user_voted of this PollResult.  # noqa: E501
        :rtype: bool
        """
        return self._requesting_user_voted

    @requesting_user_voted.setter
    def requesting_user_voted(self, requesting_user_voted):
        """Sets the requesting_user_voted of this PollResult.


        :param requesting_user_voted: The requesting_user_voted of this PollResult.  # noqa: E501
        :type: bool
        """

        self._requesting_user_voted = requesting_user_voted

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
        if not isinstance(other, PollResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
