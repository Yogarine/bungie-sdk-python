# DestinyVendorInteractionDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interaction_index** | **int** | The position of this interaction in its parent array. Note that this is NOT content agnostic, and should not be used as such. | [optional] 
**replies** | [**list[DestinyVendorInteractionReplyDefinition]**](DestinyVendorInteractionReplyDefinition.md) | The potential replies that the user can make to the interaction. | [optional] 
**vendor_category_index** | **int** | If &gt;&#x3D; 0, this is the category of sale items to show along with this interaction dialog. | [optional] 
**questline_item_hash** | **int** | If this interaction dialog is about a quest, this is the questline related to the interaction. You can use this to show the quest overview, or even the character&#39;s status with the quest if you use it to find the character&#39;s current Quest Step by checking their inventory against this questlineItemHash&#39;s DestinyInventoryItemDefinition.setData. | [optional] 
**sack_interaction_list** | [**list[DestinyVendorInteractionSackEntryDefinition]**](DestinyVendorInteractionSackEntryDefinition.md) | If this interaction is meant to show you sacks, this is the list of types of sacks to be shown. If empty, the interaction is not meant to show sacks. | [optional] 
**ui_interaction_type** | **int** | A UI hint for the behavior of the interaction screen. This is useful to determine what type of interaction is occurring, such as a prompt to receive a rank up reward or a prompt to choose a reward for completing a quest. The hash isn&#39;t as useful as the Enum in retrospect, well what can you do. Try using interactionType instead. | [optional] 
**interaction_type** | **int** | The enumerated version of the possible UI hints for vendor interactions, which is a little easier to grok than the hash found in uiInteractionType. | [optional] 
**reward_block_label** | **str** | If this interaction is displaying rewards, this is the text to use for the header of the reward-displaying section of the interaction. | [optional] 
**reward_vendor_category_index** | **int** | If the vendor&#39;s reward list is sourced from one of his categories, this is the index into the category array of items to show. | [optional] 
**flavor_line_one** | **str** | If the vendor interaction has flavor text, this is some of it. | [optional] 
**flavor_line_two** | **str** | If the vendor interaction has flavor text, this is the rest of it. | [optional] 
**header_display_properties** | [**DestinyDisplayPropertiesDefinition**](DestinyDisplayPropertiesDefinition.md) | The header for the interaction dialog. | [optional] 
**instructions** | **str** | The localized text telling the player what to do when they see this dialog. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


