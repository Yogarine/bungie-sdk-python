# DestinyActivityModeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_properties** | [**DestinyDisplayPropertiesDefinition**](DestinyDisplayPropertiesDefinition.md) |  | [optional] 
**pgcr_image** | **str** | If this activity mode has a related PGCR image, this will be the path to said image. | [optional] 
**mode_type** | **int** | The Enumeration value for this Activity Mode. Pass this identifier into Stats endpoints to get aggregate stats for this mode. | [optional] 
**activity_mode_category** | **int** | The type of play being performed in broad terms (PVP, PVE) | [optional] 
**is_team_based** | **bool** | If True, this mode has oppositional teams fighting against each other rather than \&quot;Free-For-All\&quot; or Co-operative modes of play.  Note that Aggregate modes are never marked as team based, even if they happen to be team based at the moment. At any time, an aggregate whose subordinates are only team based could be changed so that one or more aren&#39;t team based, and then this boolean won&#39;t make much sense (the aggregation would become \&quot;sometimes team based\&quot;). Let&#39;s not deal with that right now. | [optional] 
**is_aggregate_mode** | **bool** | If true, this mode is an aggregation of other, more specific modes rather than being a mode in itself. This includes modes that group Features/Events rather than Gameplay, such as Trials of The Nine: Trials of the Nine being an Event that is interesting to see aggregate data for, but when you play the activities within Trials of the Nine they are more specific activity modes such as Clash. | [optional] 
**parent_hashes** | **list[int]** | The hash identifiers of the DestinyActivityModeDefinitions that represent all of the \&quot;parent\&quot; modes for this mode. For instance, the Nightfall Mode is also a member of AllStrikes and AllPvE. | [optional] 
**friendly_name** | **str** | A Friendly identifier you can use for referring to this Activity Mode. We really only used this in our URLs, so... you know, take that for whatever it&#39;s worth. | [optional] 
**activity_mode_mappings** | **dict(str, int)** | If this exists, the mode has specific Activities (referred to by the Key) that should instead map to other Activity Modes when they are played. This was useful in D1 for Private Matches, where we wanted to have Private Matches as an activity mode while still referring to the specific mode being played. | [optional] 
**display** | **bool** | If FALSE, we want to ignore this type when we&#39;re showing activity modes in BNet UI. It will still be returned in case 3rd parties want to use it for any purpose. | [optional] 
**order** | **int** | The relative ordering of activity modes. | [optional] 
**hash** | **int** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


