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


class ContentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_content_by_id(self, id, locale, **kwargs):  # noqa: E501
        """get_content_by_id  # noqa: E501

        Returns a content item referenced by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_by_id(id, locale, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str locale: (required)
        :param bool head: false
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_content_by_id_with_http_info(id, locale, **kwargs)  # noqa: E501
        else:
            (data) = self.get_content_by_id_with_http_info(id, locale, **kwargs)  # noqa: E501
            return data

    def get_content_by_id_with_http_info(self, id, locale, **kwargs):  # noqa: E501
        """get_content_by_id  # noqa: E501

        Returns a content item referenced by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_by_id_with_http_info(id, locale, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str locale: (required)
        :param bool head: false
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'locale', 'head']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_content_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_content_by_id`")  # noqa: E501
        # verify the required parameter 'locale' is set
        if ('locale' not in local_var_params or
                local_var_params['locale'] is None):
            raise ValueError("Missing the required parameter `locale` when calling `get_content_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'locale' in local_var_params:
            path_params['locale'] = local_var_params['locale']  # noqa: E501

        query_params = []
        if 'head' in local_var_params:
            query_params.append(('head', local_var_params['head']))  # noqa: E501

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
            '/Content/GetContentById/{id}/{locale}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_content_by_tag_and_type(self, locale, tag, type, **kwargs):  # noqa: E501
        """get_content_by_tag_and_type  # noqa: E501

        Returns the newest item that matches a given tag and Content Type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_by_tag_and_type(locale, tag, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locale: (required)
        :param str tag: (required)
        :param str type: (required)
        :param bool head: Not used.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_content_by_tag_and_type_with_http_info(locale, tag, type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_content_by_tag_and_type_with_http_info(locale, tag, type, **kwargs)  # noqa: E501
            return data

    def get_content_by_tag_and_type_with_http_info(self, locale, tag, type, **kwargs):  # noqa: E501
        """get_content_by_tag_and_type  # noqa: E501

        Returns the newest item that matches a given tag and Content Type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_by_tag_and_type_with_http_info(locale, tag, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locale: (required)
        :param str tag: (required)
        :param str type: (required)
        :param bool head: Not used.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['locale', 'tag', 'type', 'head']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_content_by_tag_and_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'locale' is set
        if ('locale' not in local_var_params or
                local_var_params['locale'] is None):
            raise ValueError("Missing the required parameter `locale` when calling `get_content_by_tag_and_type`")  # noqa: E501
        # verify the required parameter 'tag' is set
        if ('tag' not in local_var_params or
                local_var_params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `get_content_by_tag_and_type`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_content_by_tag_and_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'locale' in local_var_params:
            path_params['locale'] = local_var_params['locale']  # noqa: E501
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']  # noqa: E501
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']  # noqa: E501

        query_params = []
        if 'head' in local_var_params:
            query_params.append(('head', local_var_params['head']))  # noqa: E501

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
            '/Content/GetContentByTagAndType/{tag}/{type}/{locale}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_content_type(self, type, **kwargs):  # noqa: E501
        """get_content_type  # noqa: E501

        Gets an object describing a particular variant of content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_type(type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: (required)
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_content_type_with_http_info(type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_content_type_with_http_info(type, **kwargs)  # noqa: E501
            return data

    def get_content_type_with_http_info(self, type, **kwargs):  # noqa: E501
        """get_content_type  # noqa: E501

        Gets an object describing a particular variant of content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_type_with_http_info(type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: (required)
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_content_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_content_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']  # noqa: E501

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
            '/Content/GetContentType/{type}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_content_by_tag_and_type(self, locale, tag, type, **kwargs):  # noqa: E501
        """search_content_by_tag_and_type  # noqa: E501

        Searches for Content Items that match the given Tag and Content Type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_content_by_tag_and_type(locale, tag, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locale: (required)
        :param str tag: (required)
        :param str type: (required)
        :param int currentpage: Page number for the search results starting with page 1.
        :param bool head: Not used.
        :param int itemsperpage: Not used.
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_content_by_tag_and_type_with_http_info(locale, tag, type, **kwargs)  # noqa: E501
        else:
            (data) = self.search_content_by_tag_and_type_with_http_info(locale, tag, type, **kwargs)  # noqa: E501
            return data

    def search_content_by_tag_and_type_with_http_info(self, locale, tag, type, **kwargs):  # noqa: E501
        """search_content_by_tag_and_type  # noqa: E501

        Searches for Content Items that match the given Tag and Content Type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_content_by_tag_and_type_with_http_info(locale, tag, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locale: (required)
        :param str tag: (required)
        :param str type: (required)
        :param int currentpage: Page number for the search results starting with page 1.
        :param bool head: Not used.
        :param int itemsperpage: Not used.
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['locale', 'tag', 'type', 'currentpage', 'head', 'itemsperpage']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_content_by_tag_and_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'locale' is set
        if ('locale' not in local_var_params or
                local_var_params['locale'] is None):
            raise ValueError("Missing the required parameter `locale` when calling `search_content_by_tag_and_type`")  # noqa: E501
        # verify the required parameter 'tag' is set
        if ('tag' not in local_var_params or
                local_var_params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `search_content_by_tag_and_type`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `search_content_by_tag_and_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'locale' in local_var_params:
            path_params['locale'] = local_var_params['locale']  # noqa: E501
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']  # noqa: E501
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']  # noqa: E501

        query_params = []
        if 'currentpage' in local_var_params:
            query_params.append(('currentpage', local_var_params['currentpage']))  # noqa: E501
        if 'head' in local_var_params:
            query_params.append(('head', local_var_params['head']))  # noqa: E501
        if 'itemsperpage' in local_var_params:
            query_params.append(('itemsperpage', local_var_params['itemsperpage']))  # noqa: E501

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
            '/Content/SearchContentByTagAndType/{tag}/{type}/{locale}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_content_with_text(self, locale, **kwargs):  # noqa: E501
        """search_content_with_text  # noqa: E501

        Gets content based on querystring information passed in. Provides basic search and text search capabilities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_content_with_text(locale, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locale: (required)
        :param str ctype: Content type tag: Help, News, etc. Supply multiple ctypes separated by space.
        :param int currentpage: Page number for the search results, starting with page 1.
        :param bool head: Not used.
        :param str searchtext: Word or phrase for the search.
        :param str source: For analytics, hint at the part of the app that triggered the search. Optional.
        :param str tag: Tag used on the content to be searched.
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_content_with_text_with_http_info(locale, **kwargs)  # noqa: E501
        else:
            (data) = self.search_content_with_text_with_http_info(locale, **kwargs)  # noqa: E501
            return data

    def search_content_with_text_with_http_info(self, locale, **kwargs):  # noqa: E501
        """search_content_with_text  # noqa: E501

        Gets content based on querystring information passed in. Provides basic search and text search capabilities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_content_with_text_with_http_info(locale, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locale: (required)
        :param str ctype: Content type tag: Help, News, etc. Supply multiple ctypes separated by space.
        :param int currentpage: Page number for the search results, starting with page 1.
        :param bool head: Not used.
        :param str searchtext: Word or phrase for the search.
        :param str source: For analytics, hint at the part of the app that triggered the search. Optional.
        :param str tag: Tag used on the content to be searched.
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['locale', 'ctype', 'currentpage', 'head', 'searchtext', 'source', 'tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_content_with_text" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'locale' is set
        if ('locale' not in local_var_params or
                local_var_params['locale'] is None):
            raise ValueError("Missing the required parameter `locale` when calling `search_content_with_text`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'locale' in local_var_params:
            path_params['locale'] = local_var_params['locale']  # noqa: E501

        query_params = []
        if 'ctype' in local_var_params:
            query_params.append(('ctype', local_var_params['ctype']))  # noqa: E501
        if 'currentpage' in local_var_params:
            query_params.append(('currentpage', local_var_params['currentpage']))  # noqa: E501
        if 'head' in local_var_params:
            query_params.append(('head', local_var_params['head']))  # noqa: E501
        if 'searchtext' in local_var_params:
            query_params.append(('searchtext', local_var_params['searchtext']))  # noqa: E501
        if 'source' in local_var_params:
            query_params.append(('source', local_var_params['source']))  # noqa: E501
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))  # noqa: E501

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
            '/Content/Search/{locale}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_help_articles(self, searchtext, size, **kwargs):  # noqa: E501
        """search_help_articles  # noqa: E501

        Search for Help Articles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_help_articles(searchtext, size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str searchtext: (required)
        :param str size: (required)
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_help_articles_with_http_info(searchtext, size, **kwargs)  # noqa: E501
        else:
            (data) = self.search_help_articles_with_http_info(searchtext, size, **kwargs)  # noqa: E501
            return data

    def search_help_articles_with_http_info(self, searchtext, size, **kwargs):  # noqa: E501
        """search_help_articles  # noqa: E501

        Search for Help Articles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_help_articles_with_http_info(searchtext, size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str searchtext: (required)
        :param str size: (required)
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['searchtext', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_help_articles" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'searchtext' is set
        if ('searchtext' not in local_var_params or
                local_var_params['searchtext'] is None):
            raise ValueError("Missing the required parameter `searchtext` when calling `search_help_articles`")  # noqa: E501
        # verify the required parameter 'size' is set
        if ('size' not in local_var_params or
                local_var_params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `search_help_articles`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'searchtext' in local_var_params:
            path_params['searchtext'] = local_var_params['searchtext']  # noqa: E501
        if 'size' in local_var_params:
            path_params['size'] = local_var_params['size']  # noqa: E501

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
            '/Content/SearchHelpArticles/{searchtext}/{size}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
