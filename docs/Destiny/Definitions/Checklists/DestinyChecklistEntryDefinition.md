# DestinyChecklistEntryDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **int** | The identifier for this Checklist entry. Guaranteed unique only within this Checklist Definition, and not globally/for all checklists. | [optional] 
**display_properties** | [**DestinyDisplayPropertiesDefinition**](DestinyDisplayPropertiesDefinition.md) | Even if no other associations exist, we will give you *something* for display properties. In cases where we have no associated entities, it may be as simple as a numerical identifier. | [optional] 
**destination_hash** | **int** |  | [optional] 
**location_hash** | **int** |  | [optional] 
**bubble_hash** | **int** | Note that a Bubble&#39;s hash doesn&#39;t uniquely identify a \&quot;top level\&quot; entity in Destiny. Only the combination of location and bubble can uniquely identify a place in the world of Destiny: so if bubbleHash is populated, locationHash must too be populated for it to have any meaning.  You can use this property if it is populated to look up the DestinyLocationDefinition&#39;s associated .locationReleases[].activityBubbleName property. | [optional] 
**activity_hash** | **int** |  | [optional] 
**item_hash** | **int** |  | [optional] 
**vendor_hash** | **int** |  | [optional] 
**vendor_interaction_index** | **int** |  | [optional] 
**scope** | **int** | The scope at which this specific entry can be computed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


