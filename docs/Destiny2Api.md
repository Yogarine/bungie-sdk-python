# bungie-sdk-python.Destiny2Api

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**awa_get_action_token**](Destiny2Api.md#awa_get_action_token) | **GET** /Destiny2/Awa/GetActionToken/{correlationId}/ | 
[**awa_initialize_request**](Destiny2Api.md#awa_initialize_request) | **POST** /Destiny2/Awa/Initialize/ | 
[**awa_provide_authorization_result**](Destiny2Api.md#awa_provide_authorization_result) | **POST** /Destiny2/Awa/AwaProvideAuthorizationResult/ | 
[**equip_item**](Destiny2Api.md#equip_item) | **POST** /Destiny2/Actions/Items/EquipItem/ | 
[**equip_items**](Destiny2Api.md#equip_items) | **POST** /Destiny2/Actions/Items/EquipItems/ | 
[**get_activity_history**](Destiny2Api.md#get_activity_history) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/ | 
[**get_character**](Destiny2Api.md#get_character) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/ | 
[**get_clan_aggregate_stats**](Destiny2Api.md#get_clan_aggregate_stats) | **GET** /Destiny2/Stats/AggregateClanStats/{groupId}/ | 
[**get_clan_leaderboards**](Destiny2Api.md#get_clan_leaderboards) | **GET** /Destiny2/Stats/Leaderboards/Clans/{groupId}/ | 
[**get_clan_weekly_reward_state**](Destiny2Api.md#get_clan_weekly_reward_state) | **GET** /Destiny2/Clan/{groupId}/WeeklyRewardState/ | 
[**get_collectible_node_details**](Destiny2Api.md#get_collectible_node_details) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Collectibles/{collectiblePresentationNodeHash}/ | 
[**get_destiny_aggregate_activity_stats**](Destiny2Api.md#get_destiny_aggregate_activity_stats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/ | 
[**get_destiny_entity_definition**](Destiny2Api.md#get_destiny_entity_definition) | **GET** /Destiny2/Manifest/{entityType}/{hashIdentifier}/ | 
[**get_destiny_manifest**](Destiny2Api.md#get_destiny_manifest) | **GET** /Destiny2/Manifest/ | 
[**get_historical_stats**](Destiny2Api.md#get_historical_stats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/ | 
[**get_historical_stats_definition**](Destiny2Api.md#get_historical_stats_definition) | **GET** /Destiny2/Stats/Definition/ | 
[**get_historical_stats_for_account**](Destiny2Api.md#get_historical_stats_for_account) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/ | 
[**get_item**](Destiny2Api.md#get_item) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Item/{itemInstanceId}/ | 
[**get_leaderboards**](Destiny2Api.md#get_leaderboards) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/ | 
[**get_leaderboards_for_character**](Destiny2Api.md#get_leaderboards_for_character) | **GET** /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/ | 
[**get_linked_profiles**](Destiny2Api.md#get_linked_profiles) | **GET** /Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/ | 
[**get_post_game_carnage_report**](Destiny2Api.md#get_post_game_carnage_report) | **GET** /Destiny2/Stats/PostGameCarnageReport/{activityId}/ | 
[**get_profile**](Destiny2Api.md#get_profile) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/ | 
[**get_public_milestone_content**](Destiny2Api.md#get_public_milestone_content) | **GET** /Destiny2/Milestones/{milestoneHash}/Content/ | 
[**get_public_milestones**](Destiny2Api.md#get_public_milestones) | **GET** /Destiny2/Milestones/ | 
[**get_public_vendors**](Destiny2Api.md#get_public_vendors) | **GET** /Destiny2//Vendors/ | 
[**get_unique_weapon_history**](Destiny2Api.md#get_unique_weapon_history) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/ | 
[**get_vendor**](Destiny2Api.md#get_vendor) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/ | 
[**get_vendors**](Destiny2Api.md#get_vendors) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/ | 
[**insert_socket_plug**](Destiny2Api.md#insert_socket_plug) | **POST** /Destiny2/Actions/Items/InsertSocketPlug/ | 
[**pull_from_postmaster**](Destiny2Api.md#pull_from_postmaster) | **POST** /Destiny2/Actions/Items/PullFromPostmaster/ | 
[**report_offensive_post_game_carnage_report_player**](Destiny2Api.md#report_offensive_post_game_carnage_report_player) | **POST** /Destiny2/Stats/PostGameCarnageReport/{activityId}/Report/ | 
[**search_destiny_entities**](Destiny2Api.md#search_destiny_entities) | **GET** /Destiny2/Armory/Search/{type}/{searchTerm}/ | 
[**search_destiny_player**](Destiny2Api.md#search_destiny_player) | **GET** /Destiny2/SearchDestinyPlayer/{membershipType}/{displayName}/ | 
[**set_item_lock_state**](Destiny2Api.md#set_item_lock_state) | **POST** /Destiny2/Actions/Items/SetLockState/ | 
[**transfer_item**](Destiny2Api.md#transfer_item) | **POST** /Destiny2/Actions/Items/TransferItem/ | 


# **awa_get_action_token**
> InlineResponse20058 awa_get_action_token(correlation_id)



Returns the action token if user approves the request.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
correlation_id = 'correlation_id_example' # str | The identifier for the advanced write action request.

try:
    api_response = api_instance.awa_get_action_token(correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->awa_get_action_token: %s\n" % e)
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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
correlation_id = 'correlation_id_example' # str | The identifier for the advanced write action request.

try:
    api_response = api_instance.awa_get_action_token(correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->awa_get_action_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **correlation_id** | **str**| The identifier for the advanced write action request. | 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **awa_initialize_request**
> InlineResponse20057 awa_initialize_request(awa_permission_requested)



Initialize a request to perform an advanced write action.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
awa_permission_requested = bungie-sdk-python.AwaPermissionRequested() # Destiny.Advanced.AwaPermissionRequested | 

try:
    api_response = api_instance.awa_initialize_request(awa_permission_requested)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->awa_initialize_request: %s\n" % e)
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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
awa_permission_requested = bungie-sdk-python.AwaPermissionRequested() # Destiny.Advanced.AwaPermissionRequested | 

try:
    api_response = api_instance.awa_initialize_request(awa_permission_requested)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->awa_initialize_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **awa_permission_requested** | [**Destiny.Advanced.AwaPermissionRequested**](AwaPermissionRequested.md)|  | 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **awa_provide_authorization_result**
> InlineResponse20022 awa_provide_authorization_result(awa_user_response)



Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
awa_user_response = bungie-sdk-python.AwaUserResponse() # Destiny.Advanced.AwaUserResponse | 

try:
    api_response = api_instance.awa_provide_authorization_result(awa_user_response)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->awa_provide_authorization_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **awa_user_response** | [**Destiny.Advanced.AwaUserResponse**](AwaUserResponse.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **equip_item**
> InlineResponse20022 equip_item(destiny_item_action_request)



Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_item_action_request = bungie-sdk-python.DestinyItemActionRequest() # Destiny.Requests.Actions.DestinyItemActionRequest | 

try:
    api_response = api_instance.equip_item(destiny_item_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->equip_item: %s\n" % e)
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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_item_action_request = bungie-sdk-python.DestinyItemActionRequest() # Destiny.Requests.Actions.DestinyItemActionRequest | 

try:
    api_response = api_instance.equip_item(destiny_item_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->equip_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_item_action_request** | [**Destiny.Requests.Actions.DestinyItemActionRequest**](DestinyItemActionRequest.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **equip_items**
> InlineResponse20043 equip_items(destiny_item_set_action_request)



Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_item_set_action_request = bungie-sdk-python.DestinyItemSetActionRequest() # Destiny.Requests.Actions.DestinyItemSetActionRequest | 

try:
    api_response = api_instance.equip_items(destiny_item_set_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->equip_items: %s\n" % e)
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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_item_set_action_request = bungie-sdk-python.DestinyItemSetActionRequest() # Destiny.Requests.Actions.DestinyItemSetActionRequest | 

try:
    api_response = api_instance.equip_items(destiny_item_set_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->equip_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_item_set_action_request** | [**Destiny.Requests.Actions.DestinyItemSetActionRequest**](DestinyItemSetActionRequest.md)|  | 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_history**
> InlineResponse20052 get_activity_history(character_id, destiny_membership_id, membership_type, count=count, mode=mode, page=page)



Gets activity history stats for indicated character.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
character_id = 56 # int | The id of the character to retrieve.
destiny_membership_id = 56 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.
count = 56 # int | Number of rows to return (optional)
mode = 56 # int | A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation. (optional)
page = 56 # int | Page number to return, starting with 0. (optional)

try:
    api_response = api_instance.get_activity_history(character_id, destiny_membership_id, membership_type, count=count, mode=mode, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_activity_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The id of the character to retrieve. | 
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **count** | **int**| Number of rows to return | [optional] 
 **mode** | **int**| A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation. | [optional] 
 **page** | **int**| Page number to return, starting with 0. | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character**
> InlineResponse20036 get_character(character_id, destiny_membership_id, membership_type, components=components)



Returns character information for the supplied character.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
character_id = 56 # int | ID of the character.
destiny_membership_id = 56 # int | Destiny membership ID.
membership_type = 56 # int | A valid non-BungieNet membership type.
components = [56] # list[int] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. (optional)

try:
    api_response = api_instance.get_character(character_id, destiny_membership_id, membership_type, components=components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| ID of the character. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **components** | [**list[int]**](int.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_aggregate_stats**
> InlineResponse20048 get_clan_aggregate_stats(group_id, modes=modes)



Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID of the clan whose leaderboards you wish to fetch.
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)

try:
    api_response = api_instance.get_clan_aggregate_stats(group_id, modes=modes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_clan_aggregate_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the clan whose leaderboards you wish to fetch. | 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_leaderboards**
> InlineResponse20047 get_clan_leaderboards(group_id, maxtop=maxtop, modes=modes, statid=statid)



Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | Group ID of the clan whose leaderboards you wish to fetch.
maxtop = 56 # int | Maximum number of top players to return. Use a large number to get entire leaderboard. (optional)
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
statid = 'statid_example' # str | ID of stat to return rather than returning all Leaderboard stats. (optional)

try:
    api_response = api_instance.get_clan_leaderboards(group_id, maxtop=maxtop, modes=modes, statid=statid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_clan_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the clan whose leaderboards you wish to fetch. | 
 **maxtop** | **int**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **str**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_weekly_reward_state**
> InlineResponse20037 get_clan_weekly_reward_state(group_id)



Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
group_id = 56 # int | A valid group id of clan.

try:
    api_response = api_instance.get_clan_weekly_reward_state(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_clan_weekly_reward_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| A valid group id of clan. | 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collectible_node_details**
> InlineResponse20042 get_collectible_node_details(character_id, collectible_presentation_node_hash, destiny_membership_id, membership_type, components=components)



Given a Presentation Node that has Collectibles as direct descendants, this will return item details about those descendants in the context of the requesting character.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
character_id = 56 # int | The Destiny Character ID of the character for whom we're getting collectible detail info.
collectible_presentation_node_hash = 56 # int | The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node.
destiny_membership_id = 56 # int | Destiny membership ID of another user. You may be denied.
membership_type = 56 # int | A valid non-BungieNet membership type.
components = [56] # list[int] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. (optional)

try:
    api_response = api_instance.get_collectible_node_details(character_id, collectible_presentation_node_hash, destiny_membership_id, membership_type, components=components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_collectible_node_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The Destiny Character ID of the character for whom we&#39;re getting collectible detail info. | 
 **collectible_presentation_node_hash** | **int**| The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node. | 
 **destiny_membership_id** | **int**| Destiny membership ID of another user. You may be denied. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **components** | [**list[int]**](int.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destiny_aggregate_activity_stats**
> InlineResponse20054 get_destiny_aggregate_activity_stats(character_id, destiny_membership_id, membership_type)



Gets all activities the character has participated in together with aggregate statistics for those activities.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
character_id = 56 # int | The specific character whose activities should be returned.
destiny_membership_id = 56 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.

try:
    api_response = api_instance.get_destiny_aggregate_activity_stats(character_id, destiny_membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_destiny_aggregate_activity_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The specific character whose activities should be returned. | 
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destiny_entity_definition**
> InlineResponse20032 get_destiny_entity_definition(entity_type, hash_identifier)



Returns the static definition of an entity of the given Type and hash identifier. Examine the API Documentation for the Type Names of entities that have their own definitions. Note that the return type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested entity type if it can be found. Please don't use this as a chatty alternative to the Manifest database if you require large sets of data, but for simple and one-off accesses this should be handy.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
entity_type = 'entity_type_example' # str | The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation.
hash_identifier = 56 # int | The hash identifier for the specific Entity you want returned.

try:
    api_response = api_instance.get_destiny_entity_definition(entity_type, hash_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_destiny_entity_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of entity for whom you would like results. These correspond to the entity&#39;s definition contract name. For instance, if you are looking for items, this property should be &#39;DestinyInventoryItemDefinition&#39;. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation. | 
 **hash_identifier** | **int**| The hash identifier for the specific Entity you want returned. | 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destiny_manifest**
> InlineResponse20031 get_destiny_manifest()



Returns the current version of the manifest as a json object.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))

try:
    api_response = api_instance.get_destiny_manifest()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_destiny_manifest: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_stats**
> InlineResponse20050 get_historical_stats(character_id, destiny_membership_id, membership_type, dayend=dayend, daystart=daystart, groups=groups, modes=modes, period_type=period_type)



Gets historical stats for indicated character.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
character_id = 56 # int | The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters.
destiny_membership_id = 56 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.
dayend = '2013-10-20T19:20:30+01:00' # datetime | Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request. (optional)
daystart = '2013-10-20T19:20:30+01:00' # datetime | First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request. (optional)
groups = [56] # list[int] | Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals (optional)
modes = [56] # list[int] | Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
period_type = 56 # int | Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity (optional)

try:
    api_response = api_instance.get_historical_stats(character_id, destiny_membership_id, membership_type, dayend=dayend, daystart=daystart, groups=groups, modes=modes, period_type=period_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_historical_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters. | 
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **dayend** | **datetime**| Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request. | [optional] 
 **daystart** | **datetime**| First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request. | [optional] 
 **groups** | [**list[int]**](int.md)| Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals | [optional] 
 **modes** | [**list[int]**](int.md)| Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **period_type** | **int**| Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_stats_definition**
> InlineResponse20046 get_historical_stats_definition()



Gets historical stats definitions.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))

try:
    api_response = api_instance.get_historical_stats_definition()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_historical_stats_definition: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_stats_for_account**
> InlineResponse20051 get_historical_stats_for_account(destiny_membership_id, membership_type, groups=groups)



Gets aggregate historical stats organized around each character for a given account.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_membership_id = 56 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.
groups = [56] # list[int] | Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals. (optional)

try:
    api_response = api_instance.get_historical_stats_for_account(destiny_membership_id, membership_type, groups=groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_historical_stats_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **groups** | [**list[int]**](int.md)| Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals. | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item**
> InlineResponse20038 get_item(destiny_membership_id, item_instance_id, membership_type, components=components)



Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_membership_id = 56 # int | The membership ID of the destiny profile.
item_instance_id = 56 # int | The Instance ID of the destiny item.
membership_type = 56 # int | A valid non-BungieNet membership type.
components = [56] # list[int] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. (optional)

try:
    api_response = api_instance.get_item(destiny_membership_id, item_instance_id, membership_type, components=components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_membership_id** | **int**| The membership ID of the destiny profile. | 
 **item_instance_id** | **int**| The Instance ID of the destiny item. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **components** | [**list[int]**](int.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaderboards**
> InlineResponse20047 get_leaderboards(destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)



Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_membership_id = 56 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.
maxtop = 56 # int | Maximum number of top players to return. Use a large number to get entire leaderboard. (optional)
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
statid = 'statid_example' # str | ID of stat to return rather than returning all Leaderboard stats. (optional)

try:
    api_response = api_instance.get_leaderboards(destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **maxtop** | **int**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **str**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaderboards_for_character**
> InlineResponse20047 get_leaderboards_for_character(character_id, destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)



Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
character_id = 56 # int | The specific character to build the leaderboard around for the provided Destiny Membership.
destiny_membership_id = 56 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.
maxtop = 56 # int | Maximum number of top players to return. Use a large number to get entire leaderboard. (optional)
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
statid = 'statid_example' # str | ID of stat to return rather than returning all Leaderboard stats. (optional)

try:
    api_response = api_instance.get_leaderboards_for_character(character_id, destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_leaderboards_for_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The specific character to build the leaderboard around for the provided Destiny Membership. | 
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **maxtop** | **int**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **str**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_profiles**
> InlineResponse20034 get_linked_profiles(membership_id, membership_type, get_all_memberships=get_all_memberships)



Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
membership_id = 56 # int | The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don't pass us a PSN membership ID and the XBox membership type, it's not going to work!
membership_type = 56 # int | The type for the membership whose linked Destiny accounts you want returned.
get_all_memberships = True # bool | (optional) if set to 'true', all memberships regardless of whether they're obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what. (optional)

try:
    api_response = api_instance.get_linked_profiles(membership_id, membership_type, get_all_memberships=get_all_memberships)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_linked_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **int**| The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don&#39;t pass us a PSN membership ID and the XBox membership type, it&#39;s not going to work! | 
 **membership_type** | **int**| The type for the membership whose linked Destiny accounts you want returned. | 
 **get_all_memberships** | **bool**| (optional) if set to &#39;true&#39;, all memberships regardless of whether they&#39;re obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what. | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_game_carnage_report**
> InlineResponse20045 get_post_game_carnage_report(activity_id)



Gets the available post game carnage report for the activity ID.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
activity_id = 56 # int | The ID of the activity whose PGCR is requested.

try:
    api_response = api_instance.get_post_game_carnage_report(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_post_game_carnage_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| The ID of the activity whose PGCR is requested. | 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> InlineResponse20035 get_profile(destiny_membership_id, membership_type, components=components)



Returns Destiny Profile information for the supplied membership.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_membership_id = 56 # int | Destiny membership ID.
membership_type = 56 # int | A valid non-BungieNet membership type.
components = [56] # list[int] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. (optional)

try:
    api_response = api_instance.get_profile(destiny_membership_id, membership_type, components=components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **components** | [**list[int]**](int.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_milestone_content**
> InlineResponse20055 get_public_milestone_content(milestone_hash)



Gets custom localized content for the milestone of the given hash, if it exists.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
milestone_hash = 56 # int | The identifier for the milestone to be returned.

try:
    api_response = api_instance.get_public_milestone_content(milestone_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_public_milestone_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_hash** | **int**| The identifier for the milestone to be returned. | 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_milestones**
> InlineResponse20056 get_public_milestones()



Gets public information about currently available Milestones.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))

try:
    api_response = api_instance.get_public_milestones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_public_milestones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_vendors**
> InlineResponse20041 get_public_vendors(components=components)



Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor's available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: 'It's a long story...'

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
components = [56] # list[int] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. (optional)

try:
    api_response = api_instance.get_public_vendors(components=components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_public_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **components** | [**list[int]**](int.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unique_weapon_history**
> InlineResponse20053 get_unique_weapon_history(character_id, destiny_membership_id, membership_type)



Gets details about unique weapon usage, including all exotic weapons.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
character_id = 56 # int | The id of the character to retrieve.
destiny_membership_id = 56 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.

try:
    api_response = api_instance.get_unique_weapon_history(character_id, destiny_membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_unique_weapon_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The id of the character to retrieve. | 
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor**
> InlineResponse20040 get_vendor(character_id, destiny_membership_id, membership_type, vendor_hash, components=components)



Get the details of a specific Vendor.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
character_id = 56 # int | The Destiny Character ID of the character for whom we're getting vendor info.
destiny_membership_id = 56 # int | Destiny membership ID of another user. You may be denied.
membership_type = 56 # int | A valid non-BungieNet membership type.
vendor_hash = 56 # int | The Hash identifier of the Vendor to be returned.
components = [56] # list[int] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. (optional)

try:
    api_response = api_instance.get_vendor(character_id, destiny_membership_id, membership_type, vendor_hash, components=components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The Destiny Character ID of the character for whom we&#39;re getting vendor info. | 
 **destiny_membership_id** | **int**| Destiny membership ID of another user. You may be denied. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **vendor_hash** | **int**| The Hash identifier of the Vendor to be returned. | 
 **components** | [**list[int]**](int.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendors**
> InlineResponse20039 get_vendors(character_id, destiny_membership_id, membership_type, components=components)



Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have rotating/dynamic inventories. Use their definitions as-is for those.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
character_id = 56 # int | The Destiny Character ID of the character for whom we're getting vendor info.
destiny_membership_id = 56 # int | Destiny membership ID of another user. You may be denied.
membership_type = 56 # int | A valid non-BungieNet membership type.
components = [56] # list[int] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. (optional)

try:
    api_response = api_instance.get_vendors(character_id, destiny_membership_id, membership_type, components=components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->get_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The Destiny Character ID of the character for whom we&#39;re getting vendor info. | 
 **destiny_membership_id** | **int**| Destiny membership ID of another user. You may be denied. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **components** | [**list[int]**](int.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_socket_plug**
> InlineResponse20044 insert_socket_plug(destiny_insert_plugs_action_request)



Insert a plug into a socketed item. I know how it sounds, but I assure you it's much more G-rated than you might be guessing. We haven't decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for 'InsertPlugs' from the account owner.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_insert_plugs_action_request = bungie-sdk-python.DestinyInsertPlugsActionRequest() # Destiny.Requests.Actions.DestinyInsertPlugsActionRequest | 

try:
    api_response = api_instance.insert_socket_plug(destiny_insert_plugs_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->insert_socket_plug: %s\n" % e)
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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_insert_plugs_action_request = bungie-sdk-python.DestinyInsertPlugsActionRequest() # Destiny.Requests.Actions.DestinyInsertPlugsActionRequest | 

try:
    api_response = api_instance.insert_socket_plug(destiny_insert_plugs_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->insert_socket_plug: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_insert_plugs_action_request** | [**Destiny.Requests.Actions.DestinyInsertPlugsActionRequest**](DestinyInsertPlugsActionRequest.md)|  | 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_from_postmaster**
> InlineResponse20022 pull_from_postmaster(destiny_postmaster_transfer_request)



Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_postmaster_transfer_request = bungie-sdk-python.DestinyPostmasterTransferRequest() # Destiny.Requests.Actions.DestinyPostmasterTransferRequest | 

try:
    api_response = api_instance.pull_from_postmaster(destiny_postmaster_transfer_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->pull_from_postmaster: %s\n" % e)
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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_postmaster_transfer_request = bungie-sdk-python.DestinyPostmasterTransferRequest() # Destiny.Requests.Actions.DestinyPostmasterTransferRequest | 

try:
    api_response = api_instance.pull_from_postmaster(destiny_postmaster_transfer_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->pull_from_postmaster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_postmaster_transfer_request** | [**Destiny.Requests.Actions.DestinyPostmasterTransferRequest**](DestinyPostmasterTransferRequest.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_offensive_post_game_carnage_report_player**
> InlineResponse20022 report_offensive_post_game_carnage_report_player(activity_id, destiny_report_offense_pgcr_request)



Report a player that you met in an activity that was engaging in ToS-violating activities. Both you and the offending player must have played in the activityId passed in. Please use this judiciously and only when you have strong suspicions of violation, pretty please.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
activity_id = 56 # int | The ID of the activity where you ran into the brigand that you're reporting.
destiny_report_offense_pgcr_request = bungie-sdk-python.DestinyReportOffensePgcrRequest() # Destiny.Reporting.Requests.DestinyReportOffensePgcrRequest | 

try:
    api_response = api_instance.report_offensive_post_game_carnage_report_player(activity_id, destiny_report_offense_pgcr_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->report_offensive_post_game_carnage_report_player: %s\n" % e)
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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
activity_id = 56 # int | The ID of the activity where you ran into the brigand that you're reporting.
destiny_report_offense_pgcr_request = bungie-sdk-python.DestinyReportOffensePgcrRequest() # Destiny.Reporting.Requests.DestinyReportOffensePgcrRequest | 

try:
    api_response = api_instance.report_offensive_post_game_carnage_report_player(activity_id, destiny_report_offense_pgcr_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->report_offensive_post_game_carnage_report_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| The ID of the activity where you ran into the brigand that you&#39;re reporting. | 
 **destiny_report_offense_pgcr_request** | [**Destiny.Reporting.Requests.DestinyReportOffensePgcrRequest**](DestinyReportOffensePgcrRequest.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_destiny_entities**
> InlineResponse20049 search_destiny_entities(search_term, type, page=page)



Gets a page list of Destiny items.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
search_term = 'search_term_example' # str | The string to use when searching for Destiny entities.
type = 'type_example' # str | The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'.
page = 56 # int | Page number to return, starting with 0. (optional)

try:
    api_response = api_instance.search_destiny_entities(search_term, type, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->search_destiny_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| The string to use when searching for Destiny entities. | 
 **type** | **str**| The type of entity for whom you would like results. These correspond to the entity&#39;s definition contract name. For instance, if you are looking for items, this property should be &#39;DestinyInventoryItemDefinition&#39;. | 
 **page** | **int**| Page number to return, starting with 0. | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_destiny_player**
> InlineResponse20033 search_destiny_player(display_name, membership_type)



Returns a list of Destiny memberships given a full Gamertag or PSN ID.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
display_name = 'display_name_example' # str | The full gamertag or PSN id of the player. Spaces and case are ignored.
membership_type = 56 # int | A valid non-BungieNet membership type, or All.

try:
    api_response = api_instance.search_destiny_player(display_name, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->search_destiny_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_name** | **str**| The full gamertag or PSN id of the player. Spaces and case are ignored. | 
 **membership_type** | **int**| A valid non-BungieNet membership type, or All. | 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_item_lock_state**
> InlineResponse20022 set_item_lock_state(destiny_item_state_request)



Set the Lock State for an instanced item. You must have a valid Destiny Account.

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_item_state_request = bungie-sdk-python.DestinyItemStateRequest() # Destiny.Requests.Actions.DestinyItemStateRequest | 

try:
    api_response = api_instance.set_item_lock_state(destiny_item_state_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->set_item_lock_state: %s\n" % e)
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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_item_state_request = bungie-sdk-python.DestinyItemStateRequest() # Destiny.Requests.Actions.DestinyItemStateRequest | 

try:
    api_response = api_instance.set_item_lock_state(destiny_item_state_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->set_item_lock_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_item_state_request** | [**Destiny.Requests.Actions.DestinyItemStateRequest**](DestinyItemStateRequest.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_item**
> InlineResponse20022 transfer_item(destiny_item_transfer_request)



Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item. itshappening.gif

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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_item_transfer_request = bungie-sdk-python.DestinyItemTransferRequest() # Destiny.Requests.DestinyItemTransferRequest | 

try:
    api_response = api_instance.transfer_item(destiny_item_transfer_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->transfer_item: %s\n" % e)
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
api_instance = bungie-sdk-python.Destiny2Api(bungie-sdk-python.ApiClient(configuration))
destiny_item_transfer_request = bungie-sdk-python.DestinyItemTransferRequest() # Destiny.Requests.DestinyItemTransferRequest | 

try:
    api_response = api_instance.transfer_item(destiny_item_transfer_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Destiny2Api->transfer_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_item_transfer_request** | [**Destiny.Requests.DestinyItemTransferRequest**](DestinyItemTransferRequest.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

