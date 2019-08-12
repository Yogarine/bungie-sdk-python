# bungie_sdk_python.UserApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_themes**](UserApi.md#get_available_themes) | **GET** /User/GetAvailableThemes/ | 
[**get_bungie_net_user_by_id**](UserApi.md#get_bungie_net_user_by_id) | **GET** /User/GetBungieNetUserById/{id}/ | 
[**get_membership_data_by_id**](UserApi.md#get_membership_data_by_id) | **GET** /User/GetMembershipsById/{membershipId}/{membershipType}/ | 
[**get_membership_data_for_current_user**](UserApi.md#get_membership_data_for_current_user) | **GET** /User/GetMembershipsForCurrentUser/ | 
[**get_partnerships**](UserApi.md#get_partnerships) | **GET** /User/{membershipId}/Partnerships/ | 
[**search_users**](UserApi.md#search_users) | **GET** /User/SearchUsers/ | 


# **get_available_themes**
> InlineResponse2004 get_available_themes()



Returns a list of all available user themes.

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
api_instance = bungie_sdk_python.UserApi(bungie_sdk_python.ApiClient(configuration))

try:
    api_response = api_instance.get_available_themes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_available_themes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bungie_net_user_by_id**
> InlineResponse2002 get_bungie_net_user_by_id(id)



Loads a bungienet user by membership id.

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
api_instance = bungie_sdk_python.UserApi(bungie_sdk_python.ApiClient(configuration))
id = 56 # int | The requested Bungie.net membership id.

try:
    api_response = api_instance.get_bungie_net_user_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_bungie_net_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The requested Bungie.net membership id. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership_data_by_id**
> InlineResponse2005 get_membership_data_by_id(membership_id, membership_type)



Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

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
api_instance = bungie_sdk_python.UserApi(bungie_sdk_python.ApiClient(configuration))
membership_id = 56 # int | The membership ID of the target user.
membership_type = 56 # int | Type of the supplied membership ID.

try:
    api_response = api_instance.get_membership_data_by_id(membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_membership_data_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **int**| The membership ID of the target user. | 
 **membership_type** | **int**| Type of the supplied membership ID. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership_data_for_current_user**
> InlineResponse2005 get_membership_data_for_current_user()



Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

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
api_instance = bungie_sdk_python.UserApi(bungie_sdk_python.ApiClient(configuration))

try:
    api_response = api_instance.get_membership_data_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_membership_data_for_current_user: %s\n" % e)
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
api_instance = bungie_sdk_python.UserApi(bungie_sdk_python.ApiClient(configuration))

try:
    api_response = api_instance.get_membership_data_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_membership_data_for_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partnerships**
> InlineResponse2006 get_partnerships(membership_id)



Returns a user's linked Partnerships.

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
api_instance = bungie_sdk_python.UserApi(bungie_sdk_python.ApiClient(configuration))
membership_id = 56 # int | The ID of the member for whom partnerships should be returned.

try:
    api_response = api_instance.get_partnerships(membership_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_partnerships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **int**| The ID of the member for whom partnerships should be returned. | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> InlineResponse2003 search_users(q=q)



Returns a list of possible users based on the search string

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
api_instance = bungie_sdk_python.UserApi(bungie_sdk_python.ApiClient(configuration))
q = 'q_example' # str | The search string. (optional)

try:
    api_response = api_instance.search_users(q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The search string. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

