# bungie_sdk_python.ContentApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_by_id**](ContentApi.md#get_content_by_id) | **GET** /Content/GetContentById/{id}/{locale}/ | 
[**get_content_by_tag_and_type**](ContentApi.md#get_content_by_tag_and_type) | **GET** /Content/GetContentByTagAndType/{tag}/{type}/{locale}/ | 
[**get_content_type**](ContentApi.md#get_content_type) | **GET** /Content/GetContentType/{type}/ | 
[**search_content_by_tag_and_type**](ContentApi.md#search_content_by_tag_and_type) | **GET** /Content/SearchContentByTagAndType/{tag}/{type}/{locale}/ | 
[**search_content_with_text**](ContentApi.md#search_content_with_text) | **GET** /Content/Search/{locale}/ | 
[**search_help_articles**](ContentApi.md#search_help_articles) | **GET** /Content/SearchHelpArticles/{searchtext}/{size} | 


# **get_content_by_id**
> InlineResponse2008 get_content_by_id(id, locale, head=head)



Returns a content item referenced by id

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
api_instance = bungie_sdk_python.ContentApi(bungie_sdk_python.ApiClient(configuration))
id = 56 # int | 
locale = 'locale_example' # str | 
head = True # bool | false (optional)

try:
    api_response = api_instance.get_content_by_id(id, locale, head=head)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->get_content_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **locale** | **str**|  | 
 **head** | **bool**| false | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_by_tag_and_type**
> InlineResponse2008 get_content_by_tag_and_type(locale, tag, type, head=head)



Returns the newest item that matches a given tag and Content Type.

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
api_instance = bungie_sdk_python.ContentApi(bungie_sdk_python.ApiClient(configuration))
locale = 'locale_example' # str | 
tag = 'tag_example' # str | 
type = 'type_example' # str | 
head = True # bool | Not used. (optional)

try:
    api_response = api_instance.get_content_by_tag_and_type(locale, tag, type, head=head)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->get_content_by_tag_and_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**|  | 
 **tag** | **str**|  | 
 **type** | **str**|  | 
 **head** | **bool**| Not used. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_type**
> InlineResponse2007 get_content_type(type)



Gets an object describing a particular variant of content.

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
api_instance = bungie_sdk_python.ContentApi(bungie_sdk_python.ApiClient(configuration))
type = 'type_example' # str | 

try:
    api_response = api_instance.get_content_type(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->get_content_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_content_by_tag_and_type**
> InlineResponse2009 search_content_by_tag_and_type(locale, tag, type, currentpage=currentpage, head=head, itemsperpage=itemsperpage)



Searches for Content Items that match the given Tag and Content Type.

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
api_instance = bungie_sdk_python.ContentApi(bungie_sdk_python.ApiClient(configuration))
locale = 'locale_example' # str | 
tag = 'tag_example' # str | 
type = 'type_example' # str | 
currentpage = 56 # int | Page number for the search results starting with page 1. (optional)
head = True # bool | Not used. (optional)
itemsperpage = 56 # int | Not used. (optional)

try:
    api_response = api_instance.search_content_by_tag_and_type(locale, tag, type, currentpage=currentpage, head=head, itemsperpage=itemsperpage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->search_content_by_tag_and_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**|  | 
 **tag** | **str**|  | 
 **type** | **str**|  | 
 **currentpage** | **int**| Page number for the search results starting with page 1. | [optional] 
 **head** | **bool**| Not used. | [optional] 
 **itemsperpage** | **int**| Not used. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_content_with_text**
> InlineResponse2009 search_content_with_text(locale, ctype=ctype, currentpage=currentpage, head=head, searchtext=searchtext, source=source, tag=tag)



Gets content based on querystring information passed in. Provides basic search and text search capabilities.

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
api_instance = bungie_sdk_python.ContentApi(bungie_sdk_python.ApiClient(configuration))
locale = 'locale_example' # str | 
ctype = 'ctype_example' # str | Content type tag: Help, News, etc. Supply multiple ctypes separated by space. (optional)
currentpage = 56 # int | Page number for the search results, starting with page 1. (optional)
head = True # bool | Not used. (optional)
searchtext = 'searchtext_example' # str | Word or phrase for the search. (optional)
source = 'source_example' # str | For analytics, hint at the part of the app that triggered the search. Optional. (optional)
tag = 'tag_example' # str | Tag used on the content to be searched. (optional)

try:
    api_response = api_instance.search_content_with_text(locale, ctype=ctype, currentpage=currentpage, head=head, searchtext=searchtext, source=source, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->search_content_with_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**|  | 
 **ctype** | **str**| Content type tag: Help, News, etc. Supply multiple ctypes separated by space. | [optional] 
 **currentpage** | **int**| Page number for the search results, starting with page 1. | [optional] 
 **head** | **bool**| Not used. | [optional] 
 **searchtext** | **str**| Word or phrase for the search. | [optional] 
 **source** | **str**| For analytics, hint at the part of the app that triggered the search. Optional. | [optional] 
 **tag** | **str**| Tag used on the content to be searched. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_help_articles**
> InlineResponse20010 search_help_articles(searchtext, size)



Search for Help Articles.

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
api_instance = bungie_sdk_python.ContentApi(bungie_sdk_python.ApiClient(configuration))
searchtext = 'searchtext_example' # str | 
size = 'size_example' # str | 

try:
    api_response = api_instance.search_help_articles(searchtext, size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->search_help_articles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchtext** | **str**|  | 
 **size** | **str**|  | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

