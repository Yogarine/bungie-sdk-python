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


class DestinyHistoricalStatsWithMerged(object):
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
        'results': 'dict(str, DestinyHistoricalStatsByPeriod)',
        'merged': 'DestinyHistoricalStatsByPeriod'
    }

    attribute_map = {
        'results': 'results',
        'merged': 'merged'
    }

    def __init__(self, results=None, merged=None):  # noqa: E501
        """DestinyHistoricalStatsWithMerged - a model defined in OpenAPI"""  # noqa: E501

        self._results = None
        self._merged = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if merged is not None:
            self.merged = merged

    @property
    def results(self):
        """Gets the results of this DestinyHistoricalStatsWithMerged.  # noqa: E501


        :return: The results of this DestinyHistoricalStatsWithMerged.  # noqa: E501
        :rtype: dict(str, DestinyHistoricalStatsByPeriod)
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this DestinyHistoricalStatsWithMerged.


        :param results: The results of this DestinyHistoricalStatsWithMerged.  # noqa: E501
        :type: dict(str, DestinyHistoricalStatsByPeriod)
        """

        self._results = results

    @property
    def merged(self):
        """Gets the merged of this DestinyHistoricalStatsWithMerged.  # noqa: E501


        :return: The merged of this DestinyHistoricalStatsWithMerged.  # noqa: E501
        :rtype: DestinyHistoricalStatsByPeriod
        """
        return self._merged

    @merged.setter
    def merged(self, merged):
        """Sets the merged of this DestinyHistoricalStatsWithMerged.


        :param merged: The merged of this DestinyHistoricalStatsWithMerged.  # noqa: E501
        :type: DestinyHistoricalStatsByPeriod
        """

        self._merged = merged

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
        if not isinstance(other, DestinyHistoricalStatsWithMerged):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
