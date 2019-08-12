# bungie_sdk_python.ForumApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_core_topics_paged**](ForumApi.md#get_core_topics_paged) | **GET** /Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/ | 
[**get_forum_tag_suggestions**](ForumApi.md#get_forum_tag_suggestions) | **GET** /Forum/GetForumTagSuggestions/ | 
[**get_poll**](ForumApi.md#get_poll) | **GET** /Forum/Poll/{topicId}/ | 
[**get_post_and_parent**](ForumApi.md#get_post_and_parent) | **GET** /Forum/GetPostAndParent/{childPostId}/ | 
[**get_post_and_parent_awaiting_approval**](ForumApi.md#get_post_and_parent_awaiting_approval) | **GET** /Forum/GetPostAndParentAwaitingApproval/{childPostId}/ | 
[**get_posts_threaded_paged**](ForumApi.md#get_posts_threaded_paged) | **GET** /Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/ | 
[**get_posts_threaded_paged_from_child**](ForumApi.md#get_posts_threaded_paged_from_child) | **GET** /Forum/GetPostsThreadedPagedFromChild/{childPostId}/{page}/{pageSize}/{replySize}/{rootThreadMode}/{sortMode}/ | 
[**get_recruitment_thread_summaries**](ForumApi.md#get_recruitment_thread_summaries) | **POST** /Forum/Recruit/Summaries/ | 
[**get_topic_for_content**](ForumApi.md#get_topic_for_content) | **GET** /Forum/GetTopicForContent/{contentId}/ | 
[**get_topics_paged**](ForumApi.md#get_topics_paged) | **GET** /Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/ | 


# **get_core_topics_paged**
> InlineResponse20011 get_core_topics_paged(category_filter, page, quick_date, sort, locales=locales)



Gets a listing of all topics marked as part of the core group.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_sdk_python.ForumApi(bungie_sdk_python.ApiClient(configuration))
category_filter = 56 # int | The category filter.
page = 56 # int | Zero base page
quick_date = 56 # int | The date filter.
sort = 56 # int | The sort mode.
locales = 'locales_example' # str | Comma seperated list of locales posts must match to return in the result list. Default 'en' (optional)

try:
    api_response = api_instance.get_core_topics_paged(category_filter, page, quick_date, sort, locales=locales)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->get_core_topics_paged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_filter** | **int**| The category filter. | 
 **page** | **int**| Zero base page | 
 **quick_date** | **int**| The date filter. | 
 **sort** | **int**| The sort mode. | 
 **locales** | **str**| Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39; | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forum_tag_suggestions**
> InlineResponse20013 get_forum_tag_suggestions(partialtag=partialtag)



Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_sdk_python.ForumApi(bungie_sdk_python.ApiClient(configuration))
partialtag = 'partialtag_example' # str | The partial tag input to generate suggestions from. (optional)

try:
    api_response = api_instance.get_forum_tag_suggestions(partialtag=partialtag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->get_forum_tag_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partialtag** | **str**| The partial tag input to generate suggestions from. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poll**
> InlineResponse20011 get_poll(topic_id)



Gets the specified forum poll.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_sdk_python.ForumApi(bungie_sdk_python.ApiClient(configuration))
topic_id = 56 # int | The post id of the topic that has the poll.

try:
    api_response = api_instance.get_poll(topic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->get_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **int**| The post id of the topic that has the poll. | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_and_parent**
> InlineResponse20011 get_post_and_parent(child_post_id, showbanned=showbanned)



Returns the post specified and its immediate parent.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_sdk_python.ForumApi(bungie_sdk_python.ApiClient(configuration))
child_post_id = 56 # int | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try:
    api_response = api_instance.get_post_and_parent(child_post_id, showbanned=showbanned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->get_post_and_parent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_post_id** | **int**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_and_parent_awaiting_approval**
> InlineResponse20011 get_post_and_parent_awaiting_approval(child_post_id, showbanned=showbanned)



Returns the post specified and its immediate parent of posts that are awaiting approval.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_sdk_python.ForumApi(bungie_sdk_python.ApiClient(configuration))
child_post_id = 56 # int | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try:
    api_response = api_instance.get_post_and_parent_awaiting_approval(child_post_id, showbanned=showbanned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->get_post_and_parent_awaiting_approval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_post_id** | **int**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_posts_threaded_paged**
> InlineResponse20011 get_posts_threaded_paged(get_parent_post, page, page_size, parent_post_id, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)



Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_sdk_python.ForumApi(bungie_sdk_python.ApiClient(configuration))
get_parent_post = True # bool | 
page = 56 # int | 
page_size = 56 # int | 
parent_post_id = 56 # int | 
reply_size = 56 # int | 
root_thread_mode = True # bool | 
sort_mode = 56 # int | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try:
    api_response = api_instance.get_posts_threaded_paged(get_parent_post, page, page_size, parent_post_id, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->get_posts_threaded_paged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_parent_post** | **bool**|  | 
 **page** | **int**|  | 
 **page_size** | **int**|  | 
 **parent_post_id** | **int**|  | 
 **reply_size** | **int**|  | 
 **root_thread_mode** | **bool**|  | 
 **sort_mode** | **int**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_posts_threaded_paged_from_child**
> InlineResponse20011 get_posts_threaded_paged_from_child(child_post_id, page, page_size, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)



Returns a thread of posts starting at the topicId of the input childPostId, optionally returning replies to those posts as well as the original parent.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_sdk_python.ForumApi(bungie_sdk_python.ApiClient(configuration))
child_post_id = 56 # int | 
page = 56 # int | 
page_size = 56 # int | 
reply_size = 56 # int | 
root_thread_mode = True # bool | 
sort_mode = 56 # int | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try:
    api_response = api_instance.get_posts_threaded_paged_from_child(child_post_id, page, page_size, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->get_posts_threaded_paged_from_child: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_post_id** | **int**|  | 
 **page** | **int**|  | 
 **page_size** | **int**|  | 
 **reply_size** | **int**|  | 
 **root_thread_mode** | **bool**|  | 
 **sort_mode** | **int**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recruitment_thread_summaries**
> InlineResponse20014 get_recruitment_thread_summaries(request_body)



Allows the caller to get a list of to 25 recruitment thread summary information objects.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_sdk_python.ForumApi(bungie_sdk_python.ApiClient(configuration))
request_body = NULL # list[int] | 

try:
    api_response = api_instance.get_recruitment_thread_summaries(request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->get_recruitment_thread_summaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[int]**](list.md)|  | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_for_content**
> InlineResponse20012 get_topic_for_content(content_id)



Gets the post Id for the given content item's comments, if it exists.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_sdk_python.ForumApi(bungie_sdk_python.ApiClient(configuration))
content_id = 56 # int | 

try:
    api_response = api_instance.get_topic_for_content(content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->get_topic_for_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **int**|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topics_paged**
> InlineResponse20011 get_topics_paged(category_filter, group, page, page_size, quick_date, sort, locales=locales, tagstring=tagstring)



Get topics from any forum.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_sdk_python.ForumApi(bungie_sdk_python.ApiClient(configuration))
category_filter = 56 # int | A category filter
group = 56 # int | The group, if any.
page = 56 # int | Zero paged page number
page_size = 56 # int | Unused
quick_date = 56 # int | A date filter.
sort = 56 # int | The sort mode.
locales = 'locales_example' # str | Comma seperated list of locales posts must match to return in the result list. Default 'en' (optional)
tagstring = 'tagstring_example' # str | The tags to search, if any. (optional)

try:
    api_response = api_instance.get_topics_paged(category_filter, group, page, page_size, quick_date, sort, locales=locales, tagstring=tagstring)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->get_topics_paged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_filter** | **int**| A category filter | 
 **group** | **int**| The group, if any. | 
 **page** | **int**| Zero paged page number | 
 **page_size** | **int**| Unused | 
 **quick_date** | **int**| A date filter. | 
 **sort** | **int**| The sort mode. | 
 **locales** | **str**| Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39; | [optional] 
 **tagstring** | **str**| The tags to search, if any. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

