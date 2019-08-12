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


class FireteamApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_active_private_clan_fireteam_count(self, group_id, **kwargs):  # noqa: E501
        """get_active_private_clan_fireteam_count  # noqa: E501

        Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_active_private_clan_fireteam_count(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int group_id: The group id of the clan. (required)
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_active_private_clan_fireteam_count_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_active_private_clan_fireteam_count_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def get_active_private_clan_fireteam_count_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """get_active_private_clan_fireteam_count  # noqa: E501

        Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_active_private_clan_fireteam_count_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int group_id: The group id of the clan. (required)
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_active_private_clan_fireteam_count" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in local_var_params or
                local_var_params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_active_private_clan_fireteam_count`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/Fireteam/Clan/{groupId}/ActiveCount/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20022',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_available_clan_fireteams(self, activity_type, date_range, group_id, page, platform, public_only, slot_filter, **kwargs):  # noqa: E501
        """get_available_clan_fireteams  # noqa: E501

        Gets a listing of all of this clan's fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_clan_fireteams(activity_type, date_range, group_id, page, platform, public_only, slot_filter, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int activity_type: The activity type to filter by. (required)
        :param int date_range: The date range to grab available fireteams. (required)
        :param int group_id: The group id of the clan. (required)
        :param int page: Zero based page (required)
        :param int platform: The platform filter. (required)
        :param int public_only: Determines public/private filtering. (required)
        :param int slot_filter: Filters based on available slots (required)
        :param str lang_filter: An optional language filter.
        :return: InlineResponse20064
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_available_clan_fireteams_with_http_info(activity_type, date_range, group_id, page, platform, public_only, slot_filter, **kwargs)  # noqa: E501
        else:
            (data) = self.get_available_clan_fireteams_with_http_info(activity_type, date_range, group_id, page, platform, public_only, slot_filter, **kwargs)  # noqa: E501
            return data

    def get_available_clan_fireteams_with_http_info(self, activity_type, date_range, group_id, page, platform, public_only, slot_filter, **kwargs):  # noqa: E501
        """get_available_clan_fireteams  # noqa: E501

        Gets a listing of all of this clan's fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_clan_fireteams_with_http_info(activity_type, date_range, group_id, page, platform, public_only, slot_filter, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int activity_type: The activity type to filter by. (required)
        :param int date_range: The date range to grab available fireteams. (required)
        :param int group_id: The group id of the clan. (required)
        :param int page: Zero based page (required)
        :param int platform: The platform filter. (required)
        :param int public_only: Determines public/private filtering. (required)
        :param int slot_filter: Filters based on available slots (required)
        :param str lang_filter: An optional language filter.
        :return: InlineResponse20064
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['activity_type', 'date_range', 'group_id', 'page', 'platform', 'public_only', 'slot_filter', 'lang_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_clan_fireteams" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'activity_type' is set
        if ('activity_type' not in local_var_params or
                local_var_params['activity_type'] is None):
            raise ValueError("Missing the required parameter `activity_type` when calling `get_available_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'date_range' is set
        if ('date_range' not in local_var_params or
                local_var_params['date_range'] is None):
            raise ValueError("Missing the required parameter `date_range` when calling `get_available_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'group_id' is set
        if ('group_id' not in local_var_params or
                local_var_params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_available_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in local_var_params or
                local_var_params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_available_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'platform' is set
        if ('platform' not in local_var_params or
                local_var_params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `get_available_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'public_only' is set
        if ('public_only' not in local_var_params or
                local_var_params['public_only'] is None):
            raise ValueError("Missing the required parameter `public_only` when calling `get_available_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'slot_filter' is set
        if ('slot_filter' not in local_var_params or
                local_var_params['slot_filter'] is None):
            raise ValueError("Missing the required parameter `slot_filter` when calling `get_available_clan_fireteams`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activity_type' in local_var_params:
            path_params['activityType'] = local_var_params['activity_type']  # noqa: E501
        if 'date_range' in local_var_params:
            path_params['dateRange'] = local_var_params['date_range']  # noqa: E501
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501
        if 'page' in local_var_params:
            path_params['page'] = local_var_params['page']  # noqa: E501
        if 'platform' in local_var_params:
            path_params['platform'] = local_var_params['platform']  # noqa: E501
        if 'public_only' in local_var_params:
            path_params['publicOnly'] = local_var_params['public_only']  # noqa: E501
        if 'slot_filter' in local_var_params:
            path_params['slotFilter'] = local_var_params['slot_filter']  # noqa: E501

        query_params = []
        if 'lang_filter' in local_var_params:
            query_params.append(('langFilter', local_var_params['lang_filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/Fireteam/Clan/{groupId}/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{publicOnly}/{page}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20064',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_clan_fireteam(self, fireteam_id, group_id, **kwargs):  # noqa: E501
        """get_clan_fireteam  # noqa: E501

        Gets a specific clan fireteam.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_clan_fireteam(fireteam_id, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int fireteam_id: The unique id of the fireteam. (required)
        :param int group_id: The group id of the clan. (required)
        :return: InlineResponse20066
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_clan_fireteam_with_http_info(fireteam_id, group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_clan_fireteam_with_http_info(fireteam_id, group_id, **kwargs)  # noqa: E501
            return data

    def get_clan_fireteam_with_http_info(self, fireteam_id, group_id, **kwargs):  # noqa: E501
        """get_clan_fireteam  # noqa: E501

        Gets a specific clan fireteam.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_clan_fireteam_with_http_info(fireteam_id, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int fireteam_id: The unique id of the fireteam. (required)
        :param int group_id: The group id of the clan. (required)
        :return: InlineResponse20066
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['fireteam_id', 'group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_clan_fireteam" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'fireteam_id' is set
        if ('fireteam_id' not in local_var_params or
                local_var_params['fireteam_id'] is None):
            raise ValueError("Missing the required parameter `fireteam_id` when calling `get_clan_fireteam`")  # noqa: E501
        # verify the required parameter 'group_id' is set
        if ('group_id' not in local_var_params or
                local_var_params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_clan_fireteam`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fireteam_id' in local_var_params:
            path_params['fireteamId'] = local_var_params['fireteam_id']  # noqa: E501
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/Fireteam/Clan/{groupId}/Summary/{fireteamId}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20066',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_my_clan_fireteams(self, group_id, include_closed, page, platform, **kwargs):  # noqa: E501
        """get_my_clan_fireteams  # noqa: E501

        Gets a listing of all clan fireteams that caller is an applicant, a member, or an alternate of.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_my_clan_fireteams(group_id, include_closed, page, platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int group_id: The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true). (required)
        :param bool include_closed: If true, return fireteams that have been closed. (required)
        :param int page: Deprecated parameter, ignored. (required)
        :param int platform: The platform filter. (required)
        :param bool group_filter: If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.
        :param str lang_filter: An optional language filter.
        :return: InlineResponse20065
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_my_clan_fireteams_with_http_info(group_id, include_closed, page, platform, **kwargs)  # noqa: E501
        else:
            (data) = self.get_my_clan_fireteams_with_http_info(group_id, include_closed, page, platform, **kwargs)  # noqa: E501
            return data

    def get_my_clan_fireteams_with_http_info(self, group_id, include_closed, page, platform, **kwargs):  # noqa: E501
        """get_my_clan_fireteams  # noqa: E501

        Gets a listing of all clan fireteams that caller is an applicant, a member, or an alternate of.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_my_clan_fireteams_with_http_info(group_id, include_closed, page, platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int group_id: The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true). (required)
        :param bool include_closed: If true, return fireteams that have been closed. (required)
        :param int page: Deprecated parameter, ignored. (required)
        :param int platform: The platform filter. (required)
        :param bool group_filter: If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.
        :param str lang_filter: An optional language filter.
        :return: InlineResponse20065
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['group_id', 'include_closed', 'page', 'platform', 'group_filter', 'lang_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_my_clan_fireteams" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in local_var_params or
                local_var_params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_my_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'include_closed' is set
        if ('include_closed' not in local_var_params or
                local_var_params['include_closed'] is None):
            raise ValueError("Missing the required parameter `include_closed` when calling `get_my_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in local_var_params or
                local_var_params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_my_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'platform' is set
        if ('platform' not in local_var_params or
                local_var_params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `get_my_clan_fireteams`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501
        if 'include_closed' in local_var_params:
            path_params['includeClosed'] = local_var_params['include_closed']  # noqa: E501
        if 'page' in local_var_params:
            path_params['page'] = local_var_params['page']  # noqa: E501
        if 'platform' in local_var_params:
            path_params['platform'] = local_var_params['platform']  # noqa: E501

        query_params = []
        if 'group_filter' in local_var_params:
            query_params.append(('groupFilter', local_var_params['group_filter']))  # noqa: E501
        if 'lang_filter' in local_var_params:
            query_params.append(('langFilter', local_var_params['lang_filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/Fireteam/Clan/{groupId}/My/{platform}/{includeClosed}/{page}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20065',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_public_available_clan_fireteams(self, activity_type, date_range, page, platform, slot_filter, **kwargs):  # noqa: E501
        """search_public_available_clan_fireteams  # noqa: E501

        Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_public_available_clan_fireteams(activity_type, date_range, page, platform, slot_filter, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int activity_type: The activity type to filter by. (required)
        :param int date_range: The date range to grab available fireteams. (required)
        :param int page: Zero based page (required)
        :param int platform: The platform filter. (required)
        :param int slot_filter: Filters based on available slots (required)
        :param str lang_filter: An optional language filter.
        :return: InlineResponse20064
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_public_available_clan_fireteams_with_http_info(activity_type, date_range, page, platform, slot_filter, **kwargs)  # noqa: E501
        else:
            (data) = self.search_public_available_clan_fireteams_with_http_info(activity_type, date_range, page, platform, slot_filter, **kwargs)  # noqa: E501
            return data

    def search_public_available_clan_fireteams_with_http_info(self, activity_type, date_range, page, platform, slot_filter, **kwargs):  # noqa: E501
        """search_public_available_clan_fireteams  # noqa: E501

        Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_public_available_clan_fireteams_with_http_info(activity_type, date_range, page, platform, slot_filter, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int activity_type: The activity type to filter by. (required)
        :param int date_range: The date range to grab available fireteams. (required)
        :param int page: Zero based page (required)
        :param int platform: The platform filter. (required)
        :param int slot_filter: Filters based on available slots (required)
        :param str lang_filter: An optional language filter.
        :return: InlineResponse20064
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['activity_type', 'date_range', 'page', 'platform', 'slot_filter', 'lang_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_public_available_clan_fireteams" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'activity_type' is set
        if ('activity_type' not in local_var_params or
                local_var_params['activity_type'] is None):
            raise ValueError("Missing the required parameter `activity_type` when calling `search_public_available_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'date_range' is set
        if ('date_range' not in local_var_params or
                local_var_params['date_range'] is None):
            raise ValueError("Missing the required parameter `date_range` when calling `search_public_available_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in local_var_params or
                local_var_params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `search_public_available_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'platform' is set
        if ('platform' not in local_var_params or
                local_var_params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `search_public_available_clan_fireteams`")  # noqa: E501
        # verify the required parameter 'slot_filter' is set
        if ('slot_filter' not in local_var_params or
                local_var_params['slot_filter'] is None):
            raise ValueError("Missing the required parameter `slot_filter` when calling `search_public_available_clan_fireteams`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activity_type' in local_var_params:
            path_params['activityType'] = local_var_params['activity_type']  # noqa: E501
        if 'date_range' in local_var_params:
            path_params['dateRange'] = local_var_params['date_range']  # noqa: E501
        if 'page' in local_var_params:
            path_params['page'] = local_var_params['page']  # noqa: E501
        if 'platform' in local_var_params:
            path_params['platform'] = local_var_params['platform']  # noqa: E501
        if 'slot_filter' in local_var_params:
            path_params['slotFilter'] = local_var_params['slot_filter']  # noqa: E501

        query_params = []
        if 'lang_filter' in local_var_params:
            query_params.append(('langFilter', local_var_params['lang_filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/Fireteam/Search/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{page}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20064',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)