# bungie-sdk-python.AppApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_api_usage**](AppApi.md#get_application_api_usage) | **GET** /App/ApiUsage/{applicationId}/ | 
[**get_bungie_applications**](AppApi.md#get_bungie_applications) | **GET** /App/FirstParty/ | 


# **get_application_api_usage**
> InlineResponse200 get_application_api_usage(application_id, end=end, start=start)



Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie-sdk-python
from bungie-sdk-python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie-sdk-python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie-sdk-python.AppApi(bungie-sdk-python.ApiClient(configuration))
application_id = 56 # int | ID of the application to get usage statistics.
end = '2013-10-20T19:20:30+01:00' # datetime | End time for query. Goes to now if not specified. (optional)
start = '2013-10-20T19:20:30+01:00' # datetime | Start time for query. Goes to 24 hours ago if not specified. (optional)

try:
    api_response = api_instance.get_application_api_usage(application_id, end=end, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_application_api_usage: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie-sdk-python
from bungie-sdk-python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie-sdk-python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie-sdk-python.AppApi(bungie-sdk-python.ApiClient(configuration))
application_id = 56 # int | ID of the application to get usage statistics.
end = '2013-10-20T19:20:30+01:00' # datetime | End time for query. Goes to now if not specified. (optional)
start = '2013-10-20T19:20:30+01:00' # datetime | Start time for query. Goes to 24 hours ago if not specified. (optional)

try:
    api_response = api_instance.get_application_api_usage(application_id, end=end, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_application_api_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| ID of the application to get usage statistics. | 
 **end** | **datetime**| End time for query. Goes to now if not specified. | [optional] 
 **start** | **datetime**| Start time for query. Goes to 24 hours ago if not specified. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bungie_applications**
> InlineResponse2001 get_bungie_applications()



Get list of applications created by Bungie.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie-sdk-python
from bungie-sdk-python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie-sdk-python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie-sdk-python.AppApi(bungie-sdk-python.ApiClient(configuration))

try:
    api_response = api_instance.get_bungie_applications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_bungie_applications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

