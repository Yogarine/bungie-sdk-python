# bungie-sdk-python.TrendingApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trending_categories**](TrendingApi.md#get_trending_categories) | **GET** /Trending/Categories/ | 
[**get_trending_category**](TrendingApi.md#get_trending_category) | **GET** /Trending/Categories/{categoryId}/{pageNumber}/ | 
[**get_trending_entry_detail**](TrendingApi.md#get_trending_entry_detail) | **GET** /Trending/Details/{trendingEntryType}/{identifier}/ | 


# **get_trending_categories**
> InlineResponse20061 get_trending_categories()



Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

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
api_instance = bungie-sdk-python.TrendingApi(bungie-sdk-python.ApiClient(configuration))

try:
    api_response = api_instance.get_trending_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrendingApi->get_trending_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trending_category**
> InlineResponse20062 get_trending_category(category_id, page_number)



Returns paginated lists of trending items for a category.

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
api_instance = bungie-sdk-python.TrendingApi(bungie-sdk-python.ApiClient(configuration))
category_id = 'category_id_example' # str | The ID of the category for whom you want additional results.
page_number = 56 # int | The page # of results to return.

try:
    api_response = api_instance.get_trending_category(category_id, page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrendingApi->get_trending_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The ID of the category for whom you want additional results. | 
 **page_number** | **int**| The page # of results to return. | 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trending_entry_detail**
> InlineResponse20063 get_trending_entry_detail(identifier, trending_entry_type)



Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

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
api_instance = bungie-sdk-python.TrendingApi(bungie-sdk-python.ApiClient(configuration))
identifier = 'identifier_example' # str | The identifier for the entity to be returned.
trending_entry_type = 56 # int | The type of entity to be returned.

try:
    api_response = api_instance.get_trending_entry_detail(identifier, trending_entry_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrendingApi->get_trending_entry_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The identifier for the entity to be returned. | 
 **trending_entry_type** | **int**| The type of entity to be returned. | 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

