# DestinyActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_hash** | **int** | The hash identifier of the Activity. Use this to look up the DestinyActivityDefinition of the activity. | [optional] 
**is_new** | **bool** | If true, then the activity should have a \&quot;new\&quot; indicator in the Director UI. | [optional] 
**can_lead** | **bool** | If true, the user is allowed to lead a Fireteam into this activity. | [optional] 
**can_join** | **bool** | If true, the user is allowed to join with another Fireteam in this activity. | [optional] 
**is_completed** | **bool** | If true, we both have the ability to know that the user has completed this activity and they have completed it. Unfortunately, we can&#39;t necessarily know this for all activities. As such, this should probably only be used if you already know in advance which specific activities you wish to check. | [optional] 
**is_visible** | **bool** | If true, the user should be able to see this activity. | [optional] 
**display_level** | **int** | The difficulty level of the activity, if applicable. | [optional] 
**recommended_light** | **int** | The recommended light level for the activity, if applicable. | [optional] 
**difficulty_tier** | **int** | A DestinyActivityDifficultyTier enum value indicating the difficulty of the activity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


