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


class DestinyProfileRecordsComponent(object):
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
        'score': 'int',
        'tracked_record_hash': 'int',
        'records': 'dict(str, DestinyRecordComponent)'
    }

    attribute_map = {
        'score': 'score',
        'tracked_record_hash': 'trackedRecordHash',
        'records': 'records'
    }

    def __init__(self, score=None, tracked_record_hash=None, records=None):  # noqa: E501
        """DestinyProfileRecordsComponent - a model defined in OpenAPI"""  # noqa: E501

        self._score = None
        self._tracked_record_hash = None
        self._records = None
        self.discriminator = None

        if score is not None:
            self.score = score
        self.tracked_record_hash = tracked_record_hash
        if records is not None:
            self.records = records

    @property
    def score(self):
        """Gets the score of this DestinyProfileRecordsComponent.  # noqa: E501

        Your \"Triumphs\" score.  # noqa: E501

        :return: The score of this DestinyProfileRecordsComponent.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this DestinyProfileRecordsComponent.

        Your \"Triumphs\" score.  # noqa: E501

        :param score: The score of this DestinyProfileRecordsComponent.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def tracked_record_hash(self):
        """Gets the tracked_record_hash of this DestinyProfileRecordsComponent.  # noqa: E501

        If this profile is tracking a record, this is the hash identifier of the record it is tracking.  # noqa: E501

        :return: The tracked_record_hash of this DestinyProfileRecordsComponent.  # noqa: E501
        :rtype: int
        """
        return self._tracked_record_hash

    @tracked_record_hash.setter
    def tracked_record_hash(self, tracked_record_hash):
        """Sets the tracked_record_hash of this DestinyProfileRecordsComponent.

        If this profile is tracking a record, this is the hash identifier of the record it is tracking.  # noqa: E501

        :param tracked_record_hash: The tracked_record_hash of this DestinyProfileRecordsComponent.  # noqa: E501
        :type: int
        """

        self._tracked_record_hash = tracked_record_hash

    @property
    def records(self):
        """Gets the records of this DestinyProfileRecordsComponent.  # noqa: E501


        :return: The records of this DestinyProfileRecordsComponent.  # noqa: E501
        :rtype: dict(str, DestinyRecordComponent)
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this DestinyProfileRecordsComponent.


        :param records: The records of this DestinyProfileRecordsComponent.  # noqa: E501
        :type: dict(str, DestinyRecordComponent)
        """

        self._records = records

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
        if not isinstance(other, DestinyProfileRecordsComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
