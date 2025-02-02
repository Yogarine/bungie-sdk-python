# DestinyPublicMilestone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**milestone_hash** | **int** | The hash identifier for the milestone. Use it to look up the DestinyMilestoneDefinition for static data about the Milestone. | [optional] 
**available_quests** | [**list[DestinyPublicMilestoneQuest]**](DestinyPublicMilestoneQuest.md) | A milestone not need have even a single quest, but if there are active quests they will be returned here. | [optional] 
**activities** | [**list[DestinyPublicMilestoneChallengeActivity]**](DestinyPublicMilestoneChallengeActivity.md) |  | [optional] 
**vendor_hashes** | **list[int]** | Sometimes milestones - or activities active in milestones - will have relevant vendors. These are the vendors that are currently relevant.  Deprecated, already, for the sake of the new \&quot;vendors\&quot; property that has more data. What was I thinking. | [optional] 
**vendors** | [**list[DestinyPublicMilestoneVendor]**](DestinyPublicMilestoneVendor.md) | This is why we can&#39;t have nice things. This is the ordered list of vendors to be shown that relate to this milestone, potentially along with other interesting data. | [optional] 
**start_date** | **datetime** | If known, this is the date when the Milestone started/became active. | [optional] 
**end_date** | **datetime** | If known, this is the date when the Milestone will expire/recycle/end. | [optional] 
**order** | **int** | Used for ordering milestones in a display to match how we order them in BNet. May pull from static data, or possibly in the future from dynamic information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


