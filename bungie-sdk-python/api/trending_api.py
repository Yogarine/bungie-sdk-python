# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.  # noqa: E501

    OpenAPI spec version: 2.3.6
    Contact: support@bungie.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bungie-sdk-python.api_client import ApiClient


class TrendingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_trending_categories(self, **kwargs):  # noqa: E501
        """get_trending_categories  # noqa: E501

        Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trending_categories(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20061
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_trending_categories_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_trending_categories_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_trending_categories_with_http_info(self, **kwargs):  # noqa: E501
        """get_trending_categories  # noqa: E501

        Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trending_categories_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20061
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trending_categories" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/Trending/Categories/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20061',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_trending_category(self, category_id, page_number, **kwargs):  # noqa: E501
        """get_trending_category  # noqa: E501

        Returns paginated lists of trending items for a category.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trending_category(category_id, page_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str category_id: The ID of the category for whom you want additional results. (required)
        :param int page_number: The page # of results to return. (required)
        :return: InlineResponse20062
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_trending_category_with_http_info(category_id, page_number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_trending_category_with_http_info(category_id, page_number, **kwargs)  # noqa: E501
            return data

    def get_trending_category_with_http_info(self, category_id, page_number, **kwargs):  # noqa: E501
        """get_trending_category  # noqa: E501

        Returns paginated lists of trending items for a category.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trending_category_with_http_info(category_id, page_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str category_id: The ID of the category for whom you want additional results. (required)
        :param int page_number: The page # of results to return. (required)
        :return: InlineResponse20062
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['category_id', 'page_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trending_category" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in local_var_params or
                local_var_params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_trending_category`")  # noqa: E501
        # verify the required parameter 'page_number' is set
        if ('page_number' not in local_var_params or
                local_var_params['page_number'] is None):
            raise ValueError("Missing the required parameter `page_number` when calling `get_trending_category`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'category_id' in local_var_params:
            path_params['categoryId'] = local_var_params['category_id']  # noqa: E501
        if 'page_number' in local_var_params:
            path_params['pageNumber'] = local_var_params['page_number']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/Trending/Categories/{categoryId}/{pageNumber}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20062',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_trending_entry_detail(self, identifier, trending_entry_type, **kwargs):  # noqa: E501
        """get_trending_entry_detail  # noqa: E501

        Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trending_entry_detail(identifier, trending_entry_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: The identifier for the entity to be returned. (required)
        :param int trending_entry_type: The type of entity to be returned. (required)
        :return: InlineResponse20063
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_trending_entry_detail_with_http_info(identifier, trending_entry_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_trending_entry_detail_with_http_info(identifier, trending_entry_type, **kwargs)  # noqa: E501
            return data

    def get_trending_entry_detail_with_http_info(self, identifier, trending_entry_type, **kwargs):  # noqa: E501
        """get_trending_entry_detail  # noqa: E501

        Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trending_entry_detail_with_http_info(identifier, trending_entry_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: The identifier for the entity to be returned. (required)
        :param int trending_entry_type: The type of entity to be returned. (required)
        :return: InlineResponse20063
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['identifier', 'trending_entry_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trending_entry_detail" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in local_var_params or
                local_var_params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_trending_entry_detail`")  # noqa: E501
        # verify the required parameter 'trending_entry_type' is set
        if ('trending_entry_type' not in local_var_params or
                local_var_params['trending_entry_type'] is None):
            raise ValueError("Missing the required parameter `trending_entry_type` when calling `get_trending_entry_detail`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']  # noqa: E501
        if 'trending_entry_type' in local_var_params:
            path_params['trendingEntryType'] = local_var_params['trending_entry_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/Trending/Details/{trendingEntryType}/{identifier}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20063',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
