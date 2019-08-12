# DestinyItemActionBlockDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verb_name** | **str** | Localized text for the verb of the action being performed. | [optional] 
**verb_description** | **str** | Localized text describing the action being performed. | [optional] 
**is_positive** | **bool** | The content has this property, however it&#39;s not entirely clear how it is used. | [optional] 
**overlay_screen_name** | **str** | If the action has an overlay screen associated with it, this is the name of that screen. Unfortunately, we cannot return the screen&#39;s data itself. | [optional] 
**overlay_icon** | **str** | The icon associated with the overlay screen for the action, if any. | [optional] 
**required_cooldown_seconds** | **int** | The number of seconds to delay before allowing this action to be performed again. | [optional] 
**required_items** | [**list[DestinyItemActionRequiredItemDefinition]**](DestinyItemActionRequiredItemDefinition.md) | If the action requires other items to exist or be destroyed, this is the list of those items and requirements. | [optional] 
**progression_rewards** | [**list[DestinyProgressionRewardDefinition]**](DestinyProgressionRewardDefinition.md) | If performing this action earns you Progression, this is the list of progressions and values granted for those progressions by performing this action. | [optional] 
**action_type_label** | **str** | The internal identifier for the action. | [optional] 
**required_location** | **str** | Theoretically, an item could have a localized string for a hint about the location in which the action should be performed. In practice, no items yet have this property. | [optional] 
**required_cooldown_hash** | **int** | The identifier hash for the Cooldown associated with this action. We have not pulled this data yet for you to have more data to use for cooldowns. | [optional] 
**delete_on_action** | **bool** | If true, the item is deleted when the action completes. | [optional] 
**consume_entire_stack** | **bool** | If true, the entire stack is deleted when the action completes. | [optional] 
**use_on_acquire** | **bool** | If true, this action will be performed as soon as you earn this item. Some rewards work this way, providing you a single item to pick up from a reward-granting vendor in-game and then immediately consuming itself to provide you multiple items. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


