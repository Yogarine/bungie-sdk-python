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


class PostSearchResponse(object):
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
        'related_posts': 'list[PostResponse]',
        'authors': 'list[GeneralUser]',
        'groups': 'list[GroupResponse]',
        'searched_tags': 'list[TagResponse]',
        'polls': 'list[PollResponse]',
        'recruitment_details': 'list[ForumRecruitmentDetail]',
        'available_pages': 'int',
        'results': 'list[PostResponse]',
        'total_results': 'int',
        'has_more': 'bool',
        'query': 'PagedQuery',
        'replacement_continuation_token': 'str',
        'use_total_results': 'bool'
    }

    attribute_map = {
        'related_posts': 'relatedPosts',
        'authors': 'authors',
        'groups': 'groups',
        'searched_tags': 'searchedTags',
        'polls': 'polls',
        'recruitment_details': 'recruitmentDetails',
        'available_pages': 'availablePages',
        'results': 'results',
        'total_results': 'totalResults',
        'has_more': 'hasMore',
        'query': 'query',
        'replacement_continuation_token': 'replacementContinuationToken',
        'use_total_results': 'useTotalResults'
    }

    def __init__(self, related_posts=None, authors=None, groups=None, searched_tags=None, polls=None, recruitment_details=None, available_pages=None, results=None, total_results=None, has_more=None, query=None, replacement_continuation_token=None, use_total_results=None):  # noqa: E501
        """PostSearchResponse - a model defined in OpenAPI"""  # noqa: E501

        self._related_posts = None
        self._authors = None
        self._groups = None
        self._searched_tags = None
        self._polls = None
        self._recruitment_details = None
        self._available_pages = None
        self._results = None
        self._total_results = None
        self._has_more = None
        self._query = None
        self._replacement_continuation_token = None
        self._use_total_results = None
        self.discriminator = None

        if related_posts is not None:
            self.related_posts = related_posts
        if authors is not None:
            self.authors = authors
        if groups is not None:
            self.groups = groups
        if searched_tags is not None:
            self.searched_tags = searched_tags
        if polls is not None:
            self.polls = polls
        if recruitment_details is not None:
            self.recruitment_details = recruitment_details
        self.available_pages = available_pages
        if results is not None:
            self.results = results
        if total_results is not None:
            self.total_results = total_results
        if has_more is not None:
            self.has_more = has_more
        if query is not None:
            self.query = query
        if replacement_continuation_token is not None:
            self.replacement_continuation_token = replacement_continuation_token
        if use_total_results is not None:
            self.use_total_results = use_total_results

    @property
    def related_posts(self):
        """Gets the related_posts of this PostSearchResponse.  # noqa: E501


        :return: The related_posts of this PostSearchResponse.  # noqa: E501
        :rtype: list[PostResponse]
        """
        return self._related_posts

    @related_posts.setter
    def related_posts(self, related_posts):
        """Sets the related_posts of this PostSearchResponse.


        :param related_posts: The related_posts of this PostSearchResponse.  # noqa: E501
        :type: list[PostResponse]
        """

        self._related_posts = related_posts

    @property
    def authors(self):
        """Gets the authors of this PostSearchResponse.  # noqa: E501


        :return: The authors of this PostSearchResponse.  # noqa: E501
        :rtype: list[GeneralUser]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this PostSearchResponse.


        :param authors: The authors of this PostSearchResponse.  # noqa: E501
        :type: list[GeneralUser]
        """

        self._authors = authors

    @property
    def groups(self):
        """Gets the groups of this PostSearchResponse.  # noqa: E501


        :return: The groups of this PostSearchResponse.  # noqa: E501
        :rtype: list[GroupResponse]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this PostSearchResponse.


        :param groups: The groups of this PostSearchResponse.  # noqa: E501
        :type: list[GroupResponse]
        """

        self._groups = groups

    @property
    def searched_tags(self):
        """Gets the searched_tags of this PostSearchResponse.  # noqa: E501


        :return: The searched_tags of this PostSearchResponse.  # noqa: E501
        :rtype: list[TagResponse]
        """
        return self._searched_tags

    @searched_tags.setter
    def searched_tags(self, searched_tags):
        """Sets the searched_tags of this PostSearchResponse.


        :param searched_tags: The searched_tags of this PostSearchResponse.  # noqa: E501
        :type: list[TagResponse]
        """

        self._searched_tags = searched_tags

    @property
    def polls(self):
        """Gets the polls of this PostSearchResponse.  # noqa: E501


        :return: The polls of this PostSearchResponse.  # noqa: E501
        :rtype: list[PollResponse]
        """
        return self._polls

    @polls.setter
    def polls(self, polls):
        """Sets the polls of this PostSearchResponse.


        :param polls: The polls of this PostSearchResponse.  # noqa: E501
        :type: list[PollResponse]
        """

        self._polls = polls

    @property
    def recruitment_details(self):
        """Gets the recruitment_details of this PostSearchResponse.  # noqa: E501


        :return: The recruitment_details of this PostSearchResponse.  # noqa: E501
        :rtype: list[ForumRecruitmentDetail]
        """
        return self._recruitment_details

    @recruitment_details.setter
    def recruitment_details(self, recruitment_details):
        """Sets the recruitment_details of this PostSearchResponse.


        :param recruitment_details: The recruitment_details of this PostSearchResponse.  # noqa: E501
        :type: list[ForumRecruitmentDetail]
        """

        self._recruitment_details = recruitment_details

    @property
    def available_pages(self):
        """Gets the available_pages of this PostSearchResponse.  # noqa: E501


        :return: The available_pages of this PostSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._available_pages

    @available_pages.setter
    def available_pages(self, available_pages):
        """Sets the available_pages of this PostSearchResponse.


        :param available_pages: The available_pages of this PostSearchResponse.  # noqa: E501
        :type: int
        """

        self._available_pages = available_pages

    @property
    def results(self):
        """Gets the results of this PostSearchResponse.  # noqa: E501


        :return: The results of this PostSearchResponse.  # noqa: E501
        :rtype: list[PostResponse]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PostSearchResponse.


        :param results: The results of this PostSearchResponse.  # noqa: E501
        :type: list[PostResponse]
        """

        self._results = results

    @property
    def total_results(self):
        """Gets the total_results of this PostSearchResponse.  # noqa: E501


        :return: The total_results of this PostSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this PostSearchResponse.


        :param total_results: The total_results of this PostSearchResponse.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

    @property
    def has_more(self):
        """Gets the has_more of this PostSearchResponse.  # noqa: E501


        :return: The has_more of this PostSearchResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this PostSearchResponse.


        :param has_more: The has_more of this PostSearchResponse.  # noqa: E501
        :type: bool
        """

        self._has_more = has_more

    @property
    def query(self):
        """Gets the query of this PostSearchResponse.  # noqa: E501


        :return: The query of this PostSearchResponse.  # noqa: E501
        :rtype: PagedQuery
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this PostSearchResponse.


        :param query: The query of this PostSearchResponse.  # noqa: E501
        :type: PagedQuery
        """

        self._query = query

    @property
    def replacement_continuation_token(self):
        """Gets the replacement_continuation_token of this PostSearchResponse.  # noqa: E501


        :return: The replacement_continuation_token of this PostSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._replacement_continuation_token

    @replacement_continuation_token.setter
    def replacement_continuation_token(self, replacement_continuation_token):
        """Sets the replacement_continuation_token of this PostSearchResponse.


        :param replacement_continuation_token: The replacement_continuation_token of this PostSearchResponse.  # noqa: E501
        :type: str
        """

        self._replacement_continuation_token = replacement_continuation_token

    @property
    def use_total_results(self):
        """Gets the use_total_results of this PostSearchResponse.  # noqa: E501

        If useTotalResults is true, then totalResults represents an accurate count.  If False, it does not, and may be estimated/only the size of the current page.  Either way, you should probably always only trust hasMore.  This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.  # noqa: E501

        :return: The use_total_results of this PostSearchResponse.  # noqa: E501
        :rtype: bool
        """
        return self._use_total_results

    @use_total_results.setter
    def use_total_results(self, use_total_results):
        """Sets the use_total_results of this PostSearchResponse.

        If useTotalResults is true, then totalResults represents an accurate count.  If False, it does not, and may be estimated/only the size of the current page.  Either way, you should probably always only trust hasMore.  This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.  # noqa: E501

        :param use_total_results: The use_total_results of this PostSearchResponse.  # noqa: E501
        :type: bool
        """

        self._use_total_results = use_total_results

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
        if not isinstance(other, PostSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
