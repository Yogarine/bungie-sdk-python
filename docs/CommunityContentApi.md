# bungie_sdk_python.CommunityContentApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_community_content**](CommunityContentApi.md#get_community_content) | **GET** /CommunityContent/Get/{sort}/{mediaFilter}/{page}/ | 
[**get_community_live_statuses**](CommunityContentApi.md#get_community_live_statuses) | **GET** /CommunityContent/Live/All/{partnershipType}/{sort}/{page}/ | 
[**get_community_live_statuses_for_clanmates**](CommunityContentApi.md#get_community_live_statuses_for_clanmates) | **GET** /CommunityContent/Live/Clan/{partnershipType}/{sort}/{page}/ | 
[**get_community_live_statuses_for_friends**](CommunityContentApi.md#get_community_live_statuses_for_friends) | **GET** /CommunityContent/Live/Friends/{partnershipType}/{sort}/{page}/ | 
[**get_featured_community_live_statuses**](CommunityContentApi.md#get_featured_community_live_statuses) | **GET** /CommunityContent/Live/Featured/{partnershipType}/{sort}/{page}/ | 
[**get_streaming_status_for_member**](CommunityContentApi.md#get_streaming_status_for_member) | **GET** /CommunityContent/Live/Users/{partnershipType}/{membershipType}/{membershipId}/ | 


# **get_community_content**
> InlineResponse20011 get_community_content(media_filter, page, sort)



Returns community content.

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
api_instance = bungie_sdk_python.CommunityContentApi(bungie_sdk_python.ApiClient(configuration))
media_filter = 56 # int | The type of media to get
page = 56 # int | Zero based page
sort = 56 # int | The sort mode.

try:
    api_response = api_instance.get_community_content(media_filter, page, sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->get_community_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_filter** | **int**| The type of media to get | 
 **page** | **int**| Zero based page | 
 **sort** | **int**| The sort mode. | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_community_live_statuses**
> InlineResponse20059 get_community_live_statuses(page, partnership_type, sort, mode_hash=mode_hash, stream_locale=stream_locale)



Returns info about community members who are live streaming.

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
api_instance = bungie_sdk_python.CommunityContentApi(bungie_sdk_python.ApiClient(configuration))
page = 56 # int | Zero based page.
partnership_type = 56 # int | The type of partnership for which the status should be returned.
sort = 56 # int | The sort mode.
mode_hash = 56 # int | The hash of the Activity Mode for which streams should be retrieved. Don't pass it in or pass 0 to not filter by mode. (optional)
stream_locale = 'stream_locale_example' # str | The locale for streams you'd like to see. Don't pass this to fall back on your BNet locale. Pass 'ALL' to not filter by locale. (optional)

try:
    api_response = api_instance.get_community_live_statuses(page, partnership_type, sort, mode_hash=mode_hash, stream_locale=stream_locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->get_community_live_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero based page. | 
 **partnership_type** | **int**| The type of partnership for which the status should be returned. | 
 **sort** | **int**| The sort mode. | 
 **mode_hash** | **int**| The hash of the Activity Mode for which streams should be retrieved. Don&#39;t pass it in or pass 0 to not filter by mode. | [optional] 
 **stream_locale** | **str**| The locale for streams you&#39;d like to see. Don&#39;t pass this to fall back on your BNet locale. Pass &#39;ALL&#39; to not filter by locale. | [optional] 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_community_live_statuses_for_clanmates**
> InlineResponse20059 get_community_live_statuses_for_clanmates(page, partnership_type, sort)



Returns info about community members who are live streaming in your clans.

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
api_instance = bungie_sdk_python.CommunityContentApi(bungie_sdk_python.ApiClient(configuration))
page = 56 # int | Zero based page.
partnership_type = 56 # int | The type of partnership for which the status should be returned.
sort = 56 # int | The sort mode.

try:
    api_response = api_instance.get_community_live_statuses_for_clanmates(page, partnership_type, sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->get_community_live_statuses_for_clanmates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero based page. | 
 **partnership_type** | **int**| The type of partnership for which the status should be returned. | 
 **sort** | **int**| The sort mode. | 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_community_live_statuses_for_friends**
> InlineResponse20059 get_community_live_statuses_for_friends(page, partnership_type, sort)



Returns info about community members who are live streaming among your friends.

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
api_instance = bungie_sdk_python.CommunityContentApi(bungie_sdk_python.ApiClient(configuration))
page = 56 # int | Zero based page.
partnership_type = 56 # int | The type of partnership for which the status should be returned.
sort = 56 # int | The sort mode.

try:
    api_response = api_instance.get_community_live_statuses_for_friends(page, partnership_type, sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->get_community_live_statuses_for_friends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero based page. | 
 **partnership_type** | **int**| The type of partnership for which the status should be returned. | 
 **sort** | **int**| The sort mode. | 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featured_community_live_statuses**
> InlineResponse20059 get_featured_community_live_statuses(page, partnership_type, sort, stream_locale=stream_locale)



Returns info about Featured live streams.

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
api_instance = bungie_sdk_python.CommunityContentApi(bungie_sdk_python.ApiClient(configuration))
page = 56 # int | Zero based page.
partnership_type = 56 # int | The type of partnership for which the status should be returned.
sort = 56 # int | The sort mode.
stream_locale = 'stream_locale_example' # str | The locale for streams you'd like to see. Don't pass this to fall back on your BNet locale. Pass 'ALL' to not filter by locale. (optional)

try:
    api_response = api_instance.get_featured_community_live_statuses(page, partnership_type, sort, stream_locale=stream_locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->get_featured_community_live_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero based page. | 
 **partnership_type** | **int**| The type of partnership for which the status should be returned. | 
 **sort** | **int**| The sort mode. | 
 **stream_locale** | **str**| The locale for streams you&#39;d like to see. Don&#39;t pass this to fall back on your BNet locale. Pass &#39;ALL&#39; to not filter by locale. | [optional] 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streaming_status_for_member**
> InlineResponse20060 get_streaming_status_for_member(membership_id, membership_type, partnership_type)



Gets the Live Streaming status of a particular Account and Membership Type.

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
api_instance = bungie_sdk_python.CommunityContentApi(bungie_sdk_python.ApiClient(configuration))
membership_id = 56 # int | The membershipId related to that type.
membership_type = 56 # int | The type of account for which info will be extracted.
partnership_type = 56 # int | The type of partnership for which info will be extracted.

try:
    api_response = api_instance.get_streaming_status_for_member(membership_id, membership_type, partnership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->get_streaming_status_for_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **int**| The membershipId related to that type. | 
 **membership_type** | **int**| The type of account for which info will be extracted. | 
 **partnership_type** | **int**| The type of partnership for which info will be extracted. | 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

