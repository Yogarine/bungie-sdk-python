# bungie-sdk-python.GroupV2Api

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abdicate_foundership**](GroupV2Api.md#abdicate_foundership) | **POST** /GroupV2/{groupId}/Admin/AbdicateFoundership/{membershipType}/{founderIdNew}/ | 
[**add_optional_conversation**](GroupV2Api.md#add_optional_conversation) | **POST** /GroupV2/{groupId}/OptionalConversations/Add/ | 
[**approve_all_pending**](GroupV2Api.md#approve_all_pending) | **POST** /GroupV2/{groupId}/Members/ApproveAll/ | 
[**approve_pending**](GroupV2Api.md#approve_pending) | **POST** /GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/ | 
[**approve_pending_for_list**](GroupV2Api.md#approve_pending_for_list) | **POST** /GroupV2/{groupId}/Members/ApproveList/ | 
[**ban_member**](GroupV2Api.md#ban_member) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Ban/ | 
[**deny_all_pending**](GroupV2Api.md#deny_all_pending) | **POST** /GroupV2/{groupId}/Members/DenyAll/ | 
[**deny_pending_for_list**](GroupV2Api.md#deny_pending_for_list) | **POST** /GroupV2/{groupId}/Members/DenyList/ | 
[**edit_clan_banner**](GroupV2Api.md#edit_clan_banner) | **POST** /GroupV2/{groupId}/EditClanBanner/ | 
[**edit_founder_options**](GroupV2Api.md#edit_founder_options) | **POST** /GroupV2/{groupId}/EditFounderOptions/ | 
[**edit_group**](GroupV2Api.md#edit_group) | **POST** /GroupV2/{groupId}/Edit/ | 
[**edit_group_membership**](GroupV2Api.md#edit_group_membership) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/SetMembershipType/{memberType}/ | 
[**edit_optional_conversation**](GroupV2Api.md#edit_optional_conversation) | **POST** /GroupV2/{groupId}/OptionalConversations/Edit/{conversationId}/ | 
[**get_admins_and_founder_of_group**](GroupV2Api.md#get_admins_and_founder_of_group) | **GET** /GroupV2/{groupId}/AdminsAndFounder/ | 
[**get_available_avatars**](GroupV2Api.md#get_available_avatars) | **GET** /GroupV2/GetAvailableAvatars/ | 
[**get_available_themes**](GroupV2Api.md#get_available_themes) | **GET** /GroupV2/GetAvailableThemes/ | 
[**get_banned_members_of_group**](GroupV2Api.md#get_banned_members_of_group) | **GET** /GroupV2/{groupId}/Banned/ | 
[**get_group**](GroupV2Api.md#get_group) | **GET** /GroupV2/{groupId}/ | 
[**get_group_by_name**](GroupV2Api.md#get_group_by_name) | **GET** /GroupV2/Name/{groupName}/{groupType}/ | 
[**get_group_by_name_v2**](GroupV2Api.md#get_group_by_name_v2) | **POST** /GroupV2/NameV2/ | 
[**get_group_optional_conversations**](GroupV2Api.md#get_group_optional_conversations) | **GET** /GroupV2/{groupId}/OptionalConversations/ | 
[**get_groups_for_member**](GroupV2Api.md#get_groups_for_member) | **GET** /GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/ | 
[**get_invited_individuals**](GroupV2Api.md#get_invited_individuals) | **GET** /GroupV2/{groupId}/Members/InvitedIndividuals/ | 
[**get_members_of_group**](GroupV2Api.md#get_members_of_group) | **GET** /GroupV2/{groupId}/Members/ | 
[**get_pending_memberships**](GroupV2Api.md#get_pending_memberships) | **GET** /GroupV2/{groupId}/Members/Pending/ | 
[**get_potential_groups_for_member**](GroupV2Api.md#get_potential_groups_for_member) | **GET** /GroupV2/User/Potential/{membershipType}/{membershipId}/{filter}/{groupType}/ | 
[**get_recommended_groups**](GroupV2Api.md#get_recommended_groups) | **POST** /GroupV2/Recommended/{groupType}/{createDateRange}/ | 
[**get_user_clan_invite_setting**](GroupV2Api.md#get_user_clan_invite_setting) | **GET** /GroupV2/GetUserClanInviteSetting/{mType}/ | 
[**group_search**](GroupV2Api.md#group_search) | **POST** /GroupV2/Search/ | 
[**individual_group_invite**](GroupV2Api.md#individual_group_invite) | **POST** /GroupV2/{groupId}/Members/IndividualInvite/{membershipType}/{membershipId}/ | 
[**individual_group_invite_cancel**](GroupV2Api.md#individual_group_invite_cancel) | **POST** /GroupV2/{groupId}/Members/IndividualInviteCancel/{membershipType}/{membershipId}/ | 
[**kick_member**](GroupV2Api.md#kick_member) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Kick/ | 
[**recover_group_for_founder**](GroupV2Api.md#recover_group_for_founder) | **GET** /GroupV2/Recover/{membershipType}/{membershipId}/{groupType}/ | 
[**unban_member**](GroupV2Api.md#unban_member) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Unban/ | 


# **abdicate_foundership**
> InlineResponse20017 abdicate_foundership(founder_id_new, group_id, membership_type)



An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
founder_id_new = 56 # int | The new founder for this group. Must already be a group admin.
group_id = 56 # int | The target group id.
membership_type = 56 # int | Membership type of the provided founderIdNew.

try:
    api_response = api_instance.abdicate_foundership(founder_id_new, group_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->abdicate_foundership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **founder_id_new** | **int**| The new founder for this group. Must already be a group admin. | 
 **group_id** | **int**| The target group id. | 
 **membership_type** | **int**| Membership type of the provided founderIdNew. | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_optional_conversation**
> InlineResponse20012 add_optional_conversation(group_id, group_optional_conversation_add_request)



Add a new optional conversation/chat channel. Requires admin permissions to the group.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID of the group to edit.
group_optional_conversation_add_request = bungie-sdk-python.GroupOptionalConversationAddRequest() # GroupsV2.GroupOptionalConversationAddRequest | 

try:
    api_response = api_instance.add_optional_conversation(group_id, group_optional_conversation_add_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->add_optional_conversation: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID of the group to edit.
group_optional_conversation_add_request = bungie-sdk-python.GroupOptionalConversationAddRequest() # GroupsV2.GroupOptionalConversationAddRequest | 

try:
    api_response = api_instance.add_optional_conversation(group_id, group_optional_conversation_add_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->add_optional_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the group to edit. | 
 **group_optional_conversation_add_request** | [**GroupsV2.GroupOptionalConversationAddRequest**](GroupOptionalConversationAddRequest.md)|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_all_pending**
> InlineResponse20027 approve_all_pending(group_id, group_application_request)



Approve all of the pending users for the given group.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group.
group_application_request = bungie-sdk-python.GroupApplicationRequest() # GroupsV2.GroupApplicationRequest | 

try:
    api_response = api_instance.approve_all_pending(group_id, group_application_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->approve_all_pending: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group.
group_application_request = bungie-sdk-python.GroupApplicationRequest() # GroupsV2.GroupApplicationRequest | 

try:
    api_response = api_instance.approve_all_pending(group_id, group_application_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->approve_all_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 
 **group_application_request** | [**GroupsV2.GroupApplicationRequest**](GroupApplicationRequest.md)|  | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_pending**
> InlineResponse20017 approve_pending(group_id, membership_id, membership_type, group_application_request)



Approve the given membershipId to join the group/clan as long as they have applied.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group.
membership_id = 56 # int | The membership id being approved.
membership_type = 56 # int | Membership type of the supplied membership ID.
group_application_request = bungie-sdk-python.GroupApplicationRequest() # GroupsV2.GroupApplicationRequest | 

try:
    api_response = api_instance.approve_pending(group_id, membership_id, membership_type, group_application_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->approve_pending: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group.
membership_id = 56 # int | The membership id being approved.
membership_type = 56 # int | Membership type of the supplied membership ID.
group_application_request = bungie-sdk-python.GroupApplicationRequest() # GroupsV2.GroupApplicationRequest | 

try:
    api_response = api_instance.approve_pending(group_id, membership_id, membership_type, group_application_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->approve_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 
 **membership_id** | **int**| The membership id being approved. | 
 **membership_type** | **int**| Membership type of the supplied membership ID. | 
 **group_application_request** | [**GroupsV2.GroupApplicationRequest**](GroupApplicationRequest.md)|  | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_pending_for_list**
> InlineResponse20027 approve_pending_for_list(group_id, group_application_list_request)



Approve all of the pending users for the given group.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group.
group_application_list_request = bungie-sdk-python.GroupApplicationListRequest() # GroupsV2.GroupApplicationListRequest | 

try:
    api_response = api_instance.approve_pending_for_list(group_id, group_application_list_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->approve_pending_for_list: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group.
group_application_list_request = bungie-sdk-python.GroupApplicationListRequest() # GroupsV2.GroupApplicationListRequest | 

try:
    api_response = api_instance.approve_pending_for_list(group_id, group_application_list_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->approve_pending_for_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 
 **group_application_list_request** | [**GroupsV2.GroupApplicationListRequest**](GroupApplicationListRequest.md)|  | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ban_member**
> InlineResponse20022 ban_member(group_id, membership_id, membership_type, group_ban_request)



Bans the requested member from the requested group for the specified period of time.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID that has the member to ban.
membership_id = 56 # int | Membership ID of the member to ban from the group.
membership_type = 56 # int | Membership type of the provided membership ID.
group_ban_request = bungie-sdk-python.GroupBanRequest() # GroupsV2.GroupBanRequest | 

try:
    api_response = api_instance.ban_member(group_id, membership_id, membership_type, group_ban_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->ban_member: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID that has the member to ban.
membership_id = 56 # int | Membership ID of the member to ban from the group.
membership_type = 56 # int | Membership type of the provided membership ID.
group_ban_request = bungie-sdk-python.GroupBanRequest() # GroupsV2.GroupBanRequest | 

try:
    api_response = api_instance.ban_member(group_id, membership_id, membership_type, group_ban_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->ban_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID that has the member to ban. | 
 **membership_id** | **int**| Membership ID of the member to ban from the group. | 
 **membership_type** | **int**| Membership type of the provided membership ID. | 
 **group_ban_request** | [**GroupsV2.GroupBanRequest**](GroupBanRequest.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deny_all_pending**
> InlineResponse20027 deny_all_pending(group_id, group_application_request)



Deny all of the pending users for the given group.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group.
group_application_request = bungie-sdk-python.GroupApplicationRequest() # GroupsV2.GroupApplicationRequest | 

try:
    api_response = api_instance.deny_all_pending(group_id, group_application_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->deny_all_pending: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group.
group_application_request = bungie-sdk-python.GroupApplicationRequest() # GroupsV2.GroupApplicationRequest | 

try:
    api_response = api_instance.deny_all_pending(group_id, group_application_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->deny_all_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 
 **group_application_request** | [**GroupsV2.GroupApplicationRequest**](GroupApplicationRequest.md)|  | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deny_pending_for_list**
> InlineResponse20027 deny_pending_for_list(group_id, group_application_list_request)



Deny all of the pending users for the given group that match the passed-in .

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group.
group_application_list_request = bungie-sdk-python.GroupApplicationListRequest() # GroupsV2.GroupApplicationListRequest | 

try:
    api_response = api_instance.deny_pending_for_list(group_id, group_application_list_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->deny_pending_for_list: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group.
group_application_list_request = bungie-sdk-python.GroupApplicationListRequest() # GroupsV2.GroupApplicationListRequest | 

try:
    api_response = api_instance.deny_pending_for_list(group_id, group_application_list_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->deny_pending_for_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 
 **group_application_list_request** | [**GroupsV2.GroupApplicationListRequest**](GroupApplicationListRequest.md)|  | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_clan_banner**
> InlineResponse20022 edit_clan_banner(group_id, clan_banner)



Edit an existing group's clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID of the group to edit.
clan_banner = bungie-sdk-python.ClanBanner() # GroupsV2.ClanBanner | 

try:
    api_response = api_instance.edit_clan_banner(group_id, clan_banner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->edit_clan_banner: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID of the group to edit.
clan_banner = bungie-sdk-python.ClanBanner() # GroupsV2.ClanBanner | 

try:
    api_response = api_instance.edit_clan_banner(group_id, clan_banner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->edit_clan_banner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the group to edit. | 
 **clan_banner** | [**GroupsV2.ClanBanner**](ClanBanner.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_founder_options**
> InlineResponse20022 edit_founder_options(group_id, group_options_edit_action)



Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID of the group to edit.
group_options_edit_action = bungie-sdk-python.GroupOptionsEditAction() # GroupsV2.GroupOptionsEditAction | 

try:
    api_response = api_instance.edit_founder_options(group_id, group_options_edit_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->edit_founder_options: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID of the group to edit.
group_options_edit_action = bungie-sdk-python.GroupOptionsEditAction() # GroupsV2.GroupOptionsEditAction | 

try:
    api_response = api_instance.edit_founder_options(group_id, group_options_edit_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->edit_founder_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the group to edit. | 
 **group_options_edit_action** | [**GroupsV2.GroupOptionsEditAction**](GroupOptionsEditAction.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_group**
> InlineResponse20022 edit_group(group_id, group_edit_action)



Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID of the group to edit.
group_edit_action = bungie-sdk-python.GroupEditAction() # GroupsV2.GroupEditAction | 

try:
    api_response = api_instance.edit_group(group_id, group_edit_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->edit_group: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID of the group to edit.
group_edit_action = bungie-sdk-python.GroupEditAction() # GroupsV2.GroupEditAction | 

try:
    api_response = api_instance.edit_group(group_id, group_edit_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->edit_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the group to edit. | 
 **group_edit_action** | [**GroupsV2.GroupEditAction**](GroupEditAction.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_group_membership**
> InlineResponse20022 edit_group_membership(group_id, membership_id, membership_type, member_type)



Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group to which the member belongs.
membership_id = 56 # int | Membership ID to modify.
membership_type = 56 # int | Membership type of the provide membership ID.
member_type = 56 # int | New membertype for the specified member.

try:
    api_response = api_instance.edit_group_membership(group_id, membership_id, membership_type, member_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->edit_group_membership: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group to which the member belongs.
membership_id = 56 # int | Membership ID to modify.
membership_type = 56 # int | Membership type of the provide membership ID.
member_type = 56 # int | New membertype for the specified member.

try:
    api_response = api_instance.edit_group_membership(group_id, membership_id, membership_type, member_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->edit_group_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group to which the member belongs. | 
 **membership_id** | **int**| Membership ID to modify. | 
 **membership_type** | **int**| Membership type of the provide membership ID. | 
 **member_type** | **int**| New membertype for the specified member. | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_optional_conversation**
> InlineResponse20012 edit_optional_conversation(conversation_id, group_id, group_optional_conversation_edit_request)



Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
conversation_id = 56 # int | Conversation Id of the channel being edited.
group_id = 56 # int | Group ID of the group to edit.
group_optional_conversation_edit_request = bungie-sdk-python.GroupOptionalConversationEditRequest() # GroupsV2.GroupOptionalConversationEditRequest | 

try:
    api_response = api_instance.edit_optional_conversation(conversation_id, group_id, group_optional_conversation_edit_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->edit_optional_conversation: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
conversation_id = 56 # int | Conversation Id of the channel being edited.
group_id = 56 # int | Group ID of the group to edit.
group_optional_conversation_edit_request = bungie-sdk-python.GroupOptionalConversationEditRequest() # GroupsV2.GroupOptionalConversationEditRequest | 

try:
    api_response = api_instance.edit_optional_conversation(conversation_id, group_id, group_optional_conversation_edit_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->edit_optional_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **int**| Conversation Id of the channel being edited. | 
 **group_id** | **int**| Group ID of the group to edit. | 
 **group_optional_conversation_edit_request** | [**GroupsV2.GroupOptionalConversationEditRequest**](GroupOptionalConversationEditRequest.md)|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admins_and_founder_of_group**
> InlineResponse20023 get_admins_and_founder_of_group(currentpage, group_id)



Get the list of members in a given group who are of admin level or higher.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 items per page.
group_id = 56 # int | The ID of the group.

try:
    api_response = api_instance.get_admins_and_founder_of_group(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_admins_and_founder_of_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentpage** | **int**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **group_id** | **int**| The ID of the group. | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_avatars**
> InlineResponse20015 get_available_avatars()



Returns a list of all available group avatars for the signed-in user.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))

try:
    api_response = api_instance.get_available_avatars()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_available_avatars: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_themes**
> InlineResponse20016 get_available_themes()



Returns a list of all available group themes.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))

try:
    api_response = api_instance.get_available_themes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_available_themes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_banned_members_of_group**
> InlineResponse20025 get_banned_members_of_group(currentpage, group_id)



Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 entries.
group_id = 56 # int | Group ID whose banned members you are fetching

try:
    api_response = api_instance.get_banned_members_of_group(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_banned_members_of_group: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 entries.
group_id = 56 # int | Group ID whose banned members you are fetching

try:
    api_response = api_instance.get_banned_members_of_group(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_banned_members_of_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentpage** | **int**| Page number (starting with 1). Each page has a fixed size of 50 entries. | 
 **group_id** | **int**| Group ID whose banned members you are fetching | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> InlineResponse20020 get_group(group_id)



Get information about a specific group of the given ID.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Requested group's id.

try:
    api_response = api_instance.get_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Requested group&#39;s id. | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_by_name**
> InlineResponse20020 get_group_by_name(group_name, group_type)



Get information about a specific group with the given name and type.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_name = 'group_name_example' # str | Exact name of the group to find.
group_type = 56 # int | Type of group to find.

try:
    api_response = api_instance.get_group_by_name(group_name, group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_group_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Exact name of the group to find. | 
 **group_type** | **int**| Type of group to find. | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_by_name_v2**
> InlineResponse20020 get_group_by_name_v2(group_name_search_request)



Get information about a specific group with the given name and type. The POST version.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_name_search_request = bungie-sdk-python.GroupNameSearchRequest() # GroupsV2.GroupNameSearchRequest | 

try:
    api_response = api_instance.get_group_by_name_v2(group_name_search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_group_by_name_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name_search_request** | [**GroupsV2.GroupNameSearchRequest**](GroupNameSearchRequest.md)|  | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_optional_conversations**
> InlineResponse20021 get_group_optional_conversations(group_id)



Gets a list of available optional conversation channels and their settings.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Requested group's id.

try:
    api_response = api_instance.get_group_optional_conversations(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_group_optional_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Requested group&#39;s id. | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_for_member**
> InlineResponse20028 get_groups_for_member(filter, group_type, membership_id, membership_type)



Get information about the groups that a given member has joined.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
filter = 56 # int | Filter apply to list of joined groups.
group_type = 56 # int | Type of group the supplied member founded.
membership_id = 56 # int | Membership ID to for which to find founded groups.
membership_type = 56 # int | Membership type of the supplied membership ID.

try:
    api_response = api_instance.get_groups_for_member(filter, group_type, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_groups_for_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **int**| Filter apply to list of joined groups. | 
 **group_type** | **int**| Type of group the supplied member founded. | 
 **membership_id** | **int**| Membership ID to for which to find founded groups. | 
 **membership_type** | **int**| Membership type of the supplied membership ID. | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invited_individuals**
> InlineResponse20026 get_invited_individuals(currentpage, group_id)



Get the list of users who have been invited into the group.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 items per page.
group_id = 56 # int | ID of the group.

try:
    api_response = api_instance.get_invited_individuals(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_invited_individuals: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 items per page.
group_id = 56 # int | ID of the group.

try:
    api_response = api_instance.get_invited_individuals(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_invited_individuals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentpage** | **int**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **group_id** | **int**| ID of the group. | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_of_group**
> InlineResponse20023 get_members_of_group(currentpage, group_id, member_type=member_type, name_search=name_search)



Get the list of members in a given group.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 items per page.
group_id = 56 # int | The ID of the group.
member_type = 56 # int | Filter out other member types. Use None for all members. (optional)
name_search = 'name_search_example' # str | The name fragment upon which a search should be executed for members with matching display or unique names. (optional)

try:
    api_response = api_instance.get_members_of_group(currentpage, group_id, member_type=member_type, name_search=name_search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_members_of_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentpage** | **int**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **group_id** | **int**| The ID of the group. | 
 **member_type** | **int**| Filter out other member types. Use None for all members. | [optional] 
 **name_search** | **str**| The name fragment upon which a search should be executed for members with matching display or unique names. | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_memberships**
> InlineResponse20026 get_pending_memberships(currentpage, group_id)



Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 items per page.
group_id = 56 # int | ID of the group.

try:
    api_response = api_instance.get_pending_memberships(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_pending_memberships: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 items per page.
group_id = 56 # int | ID of the group.

try:
    api_response = api_instance.get_pending_memberships(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_pending_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentpage** | **int**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **group_id** | **int**| ID of the group. | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_potential_groups_for_member**
> InlineResponse20029 get_potential_groups_for_member(filter, group_type, membership_id, membership_type)



Get information about the groups that a given member has applied to or been invited to.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
filter = 56 # int | Filter apply to list of potential joined groups.
group_type = 56 # int | Type of group the supplied member applied.
membership_id = 56 # int | Membership ID to for which to find applied groups.
membership_type = 56 # int | Membership type of the supplied membership ID.

try:
    api_response = api_instance.get_potential_groups_for_member(filter, group_type, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_potential_groups_for_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **int**| Filter apply to list of potential joined groups. | 
 **group_type** | **int**| Type of group the supplied member applied. | 
 **membership_id** | **int**| Membership ID to for which to find applied groups. | 
 **membership_type** | **int**| Membership type of the supplied membership ID. | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_groups**
> InlineResponse20018 get_recommended_groups(create_date_range, group_type)



Gets groups recommended for you based on the groups to whom those you follow belong.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
create_date_range = 56 # int | Requested range in which to pull recommended groups
group_type = 56 # int | Type of groups requested

try:
    api_response = api_instance.get_recommended_groups(create_date_range, group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_recommended_groups: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
create_date_range = 56 # int | Requested range in which to pull recommended groups
group_type = 56 # int | Type of groups requested

try:
    api_response = api_instance.get_recommended_groups(create_date_range, group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_recommended_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_date_range** | **int**| Requested range in which to pull recommended groups | 
 **group_type** | **int**| Type of groups requested | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_clan_invite_setting**
> InlineResponse20017 get_user_clan_invite_setting(m_type)



Gets the state of the user's clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
m_type = 56 # int | The Destiny membership type of the account we wish to access settings.

try:
    api_response = api_instance.get_user_clan_invite_setting(m_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_user_clan_invite_setting: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
m_type = 56 # int | The Destiny membership type of the account we wish to access settings.

try:
    api_response = api_instance.get_user_clan_invite_setting(m_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->get_user_clan_invite_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **m_type** | **int**| The Destiny membership type of the account we wish to access settings. | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_search**
> InlineResponse20019 group_search(group_query)



Search for Groups.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_query = bungie-sdk-python.GroupQuery() # GroupsV2.GroupQuery | 

try:
    api_response = api_instance.group_search(group_query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_query** | [**GroupsV2.GroupQuery**](GroupQuery.md)|  | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **individual_group_invite**
> InlineResponse20030 individual_group_invite(group_id, membership_id, membership_type, group_application_request)



Invite a user to join this group.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group you would like to join.
membership_id = 56 # int | Membership id of the account being invited.
membership_type = 56 # int | MembershipType of the account being invited.
group_application_request = bungie-sdk-python.GroupApplicationRequest() # GroupsV2.GroupApplicationRequest | 

try:
    api_response = api_instance.individual_group_invite(group_id, membership_id, membership_type, group_application_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->individual_group_invite: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group you would like to join.
membership_id = 56 # int | Membership id of the account being invited.
membership_type = 56 # int | MembershipType of the account being invited.
group_application_request = bungie-sdk-python.GroupApplicationRequest() # GroupsV2.GroupApplicationRequest | 

try:
    api_response = api_instance.individual_group_invite(group_id, membership_id, membership_type, group_application_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->individual_group_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group you would like to join. | 
 **membership_id** | **int**| Membership id of the account being invited. | 
 **membership_type** | **int**| MembershipType of the account being invited. | 
 **group_application_request** | [**GroupsV2.GroupApplicationRequest**](GroupApplicationRequest.md)|  | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **individual_group_invite_cancel**
> InlineResponse20030 individual_group_invite_cancel(group_id, membership_id, membership_type)



Cancels a pending invitation to join a group.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group you would like to join.
membership_id = 56 # int | Membership id of the account being cancelled.
membership_type = 56 # int | MembershipType of the account being cancelled.

try:
    api_response = api_instance.individual_group_invite_cancel(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->individual_group_invite_cancel: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | ID of the group you would like to join.
membership_id = 56 # int | Membership id of the account being cancelled.
membership_type = 56 # int | MembershipType of the account being cancelled.

try:
    api_response = api_instance.individual_group_invite_cancel(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->individual_group_invite_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group you would like to join. | 
 **membership_id** | **int**| Membership id of the account being cancelled. | 
 **membership_type** | **int**| MembershipType of the account being cancelled. | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kick_member**
> InlineResponse20024 kick_member(group_id, membership_id, membership_type)



Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID to kick the user from.
membership_id = 56 # int | Membership ID to kick.
membership_type = 56 # int | Membership type of the provided membership ID.

try:
    api_response = api_instance.kick_member(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->kick_member: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID to kick the user from.
membership_id = 56 # int | Membership ID to kick.
membership_type = 56 # int | Membership type of the provided membership ID.

try:
    api_response = api_instance.kick_member(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->kick_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID to kick the user from. | 
 **membership_id** | **int**| Membership ID to kick. | 
 **membership_type** | **int**| Membership type of the provided membership ID. | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_group_for_founder**
> InlineResponse20028 recover_group_for_founder(group_type, membership_id, membership_type)



Allows a founder to manually recover a group they can see in game but not on bungie.net

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_type = 56 # int | Type of group the supplied member founded.
membership_id = 56 # int | Membership ID to for which to find founded groups.
membership_type = 56 # int | Membership type of the supplied membership ID.

try:
    api_response = api_instance.recover_group_for_founder(group_type, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->recover_group_for_founder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_type** | **int**| Type of group the supplied member founded. | 
 **membership_id** | **int**| Membership ID to for which to find founded groups. | 
 **membership_type** | **int**| Membership type of the supplied membership ID. | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unban_member**
> InlineResponse20022 unban_member(group_id, membership_id, membership_type)



Unbans the requested member, allowing them to re-apply for membership.

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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | 
membership_id = 56 # int | Membership ID of the member to unban from the group
membership_type = 56 # int | Membership type of the provided membership ID.

try:
    api_response = api_instance.unban_member(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->unban_member: %s\n" % e)
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
api_instance = bungie-sdk-python.GroupV2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | 
membership_id = 56 # int | Membership ID of the member to unban from the group
membership_type = 56 # int | Membership type of the provided membership ID.

try:
    api_response = api_instance.unban_member(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->unban_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **membership_id** | **int**| Membership ID of the member to unban from the group | 
 **membership_type** | **int**| Membership type of the provided membership ID. | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

