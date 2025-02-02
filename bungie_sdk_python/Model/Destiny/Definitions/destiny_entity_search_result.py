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


class DestinyEntitySearchResult(object):
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
        'suggested_words': 'list[str]',
        'results': 'SearchResultOfDestinyEntitySearchResultItem'
    }

    attribute_map = {
        'suggested_words': 'suggestedWords',
        'results': 'results'
    }

    def __init__(self, suggested_words=None, results=None):  # noqa: E501
        """DestinyEntitySearchResult - a model defined in OpenAPI"""  # noqa: E501

        self._suggested_words = None
        self._results = None
        self.discriminator = None

        if suggested_words is not None:
            self.suggested_words = suggested_words
        if results is not None:
            self.results = results

    @property
    def suggested_words(self):
        """Gets the suggested_words of this DestinyEntitySearchResult.  # noqa: E501

        A list of suggested words that might make for better search results, based on the text searched for.  # noqa: E501

        :return: The suggested_words of this DestinyEntitySearchResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._suggested_words

    @suggested_words.setter
    def suggested_words(self, suggested_words):
        """Sets the suggested_words of this DestinyEntitySearchResult.

        A list of suggested words that might make for better search results, based on the text searched for.  # noqa: E501

        :param suggested_words: The suggested_words of this DestinyEntitySearchResult.  # noqa: E501
        :type: list[str]
        """

        self._suggested_words = suggested_words

    @property
    def results(self):
        """Gets the results of this DestinyEntitySearchResult.  # noqa: E501

        The items found that are matches/near matches for the searched-for term, sorted by something vaguely resembling \"relevance\". Hopefully this will get better in the future.  # noqa: E501

        :return: The results of this DestinyEntitySearchResult.  # noqa: E501
        :rtype: SearchResultOfDestinyEntitySearchResultItem
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this DestinyEntitySearchResult.

        The items found that are matches/near matches for the searched-for term, sorted by something vaguely resembling \"relevance\". Hopefully this will get better in the future.  # noqa: E501

        :param results: The results of this DestinyEntitySearchResult.  # noqa: E501
        :type: SearchResultOfDestinyEntitySearchResultItem
        """

        self._results = results

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
        if not isinstance(other, DestinyEntitySearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
