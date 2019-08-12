# bungie_sdk_python.FireteamApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_private_clan_fireteam_count**](FireteamApi.md#get_active_private_clan_fireteam_count) | **GET** /Fireteam/Clan/{groupId}/ActiveCount/ | 
[**get_available_clan_fireteams**](FireteamApi.md#get_available_clan_fireteams) | **GET** /Fireteam/Clan/{groupId}/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{publicOnly}/{page}/ | 
[**get_clan_fireteam**](FireteamApi.md#get_clan_fireteam) | **GET** /Fireteam/Clan/{groupId}/Summary/{fireteamId}/ | 
[**get_my_clan_fireteams**](FireteamApi.md#get_my_clan_fireteams) | **GET** /Fireteam/Clan/{groupId}/My/{platform}/{includeClosed}/{page}/ | 
[**search_public_available_clan_fireteams**](FireteamApi.md#search_public_available_clan_fireteams) | **GET** /Fireteam/Search/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{page}/ | 


# **get_active_private_clan_fireteam_count**
> InlineResponse20022 get_active_private_clan_fireteam_count(group_id)



Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

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
api_instance = bungie_sdk_python.FireteamApi(bungie_sdk_python.ApiClient(configuration))
group_id = 56 # int | The group id of the clan.

try:
    api_response = api_instance.get_active_private_clan_fireteam_count(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FireteamApi->get_active_private_clan_fireteam_count: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_sdk_python.FireteamApi(bungie_sdk_python.ApiClient(configuration))
group_id = 56 # int | The group id of the clan.

try:
    api_response = api_instance.get_active_private_clan_fireteam_count(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FireteamApi->get_active_private_clan_fireteam_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The group id of the clan. | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_clan_fireteams**
> InlineResponse20064 get_available_clan_fireteams(activity_type, date_range, group_id, page, platform, public_only, slot_filter, lang_filter=lang_filter)



Gets a listing of all of this clan's fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.

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
api_instance = bungie_sdk_python.FireteamApi(bungie_sdk_python.ApiClient(configuration))
activity_type = 56 # int | The activity type to filter by.
date_range = 56 # int | The date range to grab available fireteams.
group_id = 56 # int | The group id of the clan.
page = 56 # int | Zero based page
platform = 56 # int | The platform filter.
public_only = 56 # int | Determines public/private filtering.
slot_filter = 56 # int | Filters based on available slots
lang_filter = 'lang_filter_example' # str | An optional language filter. (optional)

try:
    api_response = api_instance.get_available_clan_fireteams(activity_type, date_range, group_id, page, platform, public_only, slot_filter, lang_filter=lang_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FireteamApi->get_available_clan_fireteams: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_sdk_python.FireteamApi(bungie_sdk_python.ApiClient(configuration))
activity_type = 56 # int | The activity type to filter by.
date_range = 56 # int | The date range to grab available fireteams.
group_id = 56 # int | The group id of the clan.
page = 56 # int | Zero based page
platform = 56 # int | The platform filter.
public_only = 56 # int | Determines public/private filtering.
slot_filter = 56 # int | Filters based on available slots
lang_filter = 'lang_filter_example' # str | An optional language filter. (optional)

try:
    api_response = api_instance.get_available_clan_fireteams(activity_type, date_range, group_id, page, platform, public_only, slot_filter, lang_filter=lang_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FireteamApi->get_available_clan_fireteams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_type** | **int**| The activity type to filter by. | 
 **date_range** | **int**| The date range to grab available fireteams. | 
 **group_id** | **int**| The group id of the clan. | 
 **page** | **int**| Zero based page | 
 **platform** | **int**| The platform filter. | 
 **public_only** | **int**| Determines public/private filtering. | 
 **slot_filter** | **int**| Filters based on available slots | 
 **lang_filter** | **str**| An optional language filter. | [optional] 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_fireteam**
> InlineResponse20066 get_clan_fireteam(fireteam_id, group_id)



Gets a specific clan fireteam.

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
api_instance = bungie_sdk_python.FireteamApi(bungie_sdk_python.ApiClient(configuration))
fireteam_id = 56 # int | The unique id of the fireteam.
group_id = 56 # int | The group id of the clan.

try:
    api_response = api_instance.get_clan_fireteam(fireteam_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FireteamApi->get_clan_fireteam: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_sdk_python.FireteamApi(bungie_sdk_python.ApiClient(configuration))
fireteam_id = 56 # int | The unique id of the fireteam.
group_id = 56 # int | The group id of the clan.

try:
    api_response = api_instance.get_clan_fireteam(fireteam_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FireteamApi->get_clan_fireteam: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fireteam_id** | **int**| The unique id of the fireteam. | 
 **group_id** | **int**| The group id of the clan. | 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_clan_fireteams**
> InlineResponse20065 get_my_clan_fireteams(group_id, include_closed, page, platform, group_filter=group_filter, lang_filter=lang_filter)



Gets a listing of all clan fireteams that caller is an applicant, a member, or an alternate of.

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
api_instance = bungie_sdk_python.FireteamApi(bungie_sdk_python.ApiClient(configuration))
group_id = 56 # int | The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).
include_closed = True # bool | If true, return fireteams that have been closed.
page = 56 # int | Deprecated parameter, ignored.
platform = 56 # int | The platform filter.
group_filter = True # bool | If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams. (optional)
lang_filter = 'lang_filter_example' # str | An optional language filter. (optional)

try:
    api_response = api_instance.get_my_clan_fireteams(group_id, include_closed, page, platform, group_filter=group_filter, lang_filter=lang_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FireteamApi->get_my_clan_fireteams: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_sdk_python.FireteamApi(bungie_sdk_python.ApiClient(configuration))
group_id = 56 # int | The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).
include_closed = True # bool | If true, return fireteams that have been closed.
page = 56 # int | Deprecated parameter, ignored.
platform = 56 # int | The platform filter.
group_filter = True # bool | If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams. (optional)
lang_filter = 'lang_filter_example' # str | An optional language filter. (optional)

try:
    api_response = api_instance.get_my_clan_fireteams(group_id, include_closed, page, platform, group_filter=group_filter, lang_filter=lang_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FireteamApi->get_my_clan_fireteams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true). | 
 **include_closed** | **bool**| If true, return fireteams that have been closed. | 
 **page** | **int**| Deprecated parameter, ignored. | 
 **platform** | **int**| The platform filter. | 
 **group_filter** | **bool**| If true, filter by clan. Otherwise, ignore the clan and show all of the user&#39;s fireteams. | [optional] 
 **lang_filter** | **str**| An optional language filter. | [optional] 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_public_available_clan_fireteams**
> InlineResponse20064 search_public_available_clan_fireteams(activity_type, date_range, page, platform, slot_filter, lang_filter=lang_filter)



Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.

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
api_instance = bungie_sdk_python.FireteamApi(bungie_sdk_python.ApiClient(configuration))
activity_type = 56 # int | The activity type to filter by.
date_range = 56 # int | The date range to grab available fireteams.
page = 56 # int | Zero based page
platform = 56 # int | The platform filter.
slot_filter = 56 # int | Filters based on available slots
lang_filter = 'lang_filter_example' # str | An optional language filter. (optional)

try:
    api_response = api_instance.search_public_available_clan_fireteams(activity_type, date_range, page, platform, slot_filter, lang_filter=lang_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FireteamApi->search_public_available_clan_fireteams: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_sdk_python
from bungie_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_sdk_python.FireteamApi(bungie_sdk_python.ApiClient(configuration))
activity_type = 56 # int | The activity type to filter by.
date_range = 56 # int | The date range to grab available fireteams.
page = 56 # int | Zero based page
platform = 56 # int | The platform filter.
slot_filter = 56 # int | Filters based on available slots
lang_filter = 'lang_filter_example' # str | An optional language filter. (optional)

try:
    api_response = api_instance.search_public_available_clan_fireteams(activity_type, date_range, page, platform, slot_filter, lang_filter=lang_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FireteamApi->search_public_available_clan_fireteams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_type** | **int**| The activity type to filter by. | 
 **date_range** | **int**| The date range to grab available fireteams. | 
 **page** | **int**| Zero based page | 
 **platform** | **int**| The platform filter. | 
 **slot_filter** | **int**| Filters based on available slots | 
 **lang_filter** | **str**| An optional language filter. | [optional] 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

