# DestinyLocationReleaseDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_properties** | [**DestinyDisplayPropertiesDefinition**](DestinyDisplayPropertiesDefinition.md) | Sadly, these don&#39;t appear to be populated anymore (ever?) | [optional] 
**small_transparent_icon** | **str** |  | [optional] 
**map_icon** | **str** |  | [optional] 
**large_transparent_icon** | **str** |  | [optional] 
**spawn_point** | **int** | If we had map information, this spawnPoint would be interesting. But sadly, we don&#39;t have that info. | [optional] 
**destination_hash** | **int** | The Destination being pointed to by this location. | [optional] 
**activity_hash** | **int** | The Activity being pointed to by this location. | [optional] 
**activity_graph_hash** | **int** | The Activity Graph being pointed to by this location. | [optional] 
**activity_graph_node_hash** | **int** | The Activity Graph Node being pointed to by this location. (Remember that Activity Graph Node hashes are only unique within an Activity Graph: so use the combination to find the node being spoken of) | [optional] 
**activity_bubble_name** | **int** | The Activity Bubble within the Destination. Look this up in the DestinyDestinationDefinition&#39;s bubbles and bubbleSettings properties. | [optional] 
**activity_path_bundle** | **int** | If we had map information, this would tell us something cool about the path this location wants you to take. I wish we had map information. | [optional] 
**activity_path_destination** | **int** | If we had map information, this would tell us about path information related to destination on the map. Sad. Maybe you can do something cool with it. Go to town man. | [optional] 
**nav_point_type** | **int** | The type of Nav Point that this represents. See the enumeration for more info. | [optional] 
**world_position** | **list[int]** | Looks like it should be the position on the map, but sadly it does not look populated... yet? | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


