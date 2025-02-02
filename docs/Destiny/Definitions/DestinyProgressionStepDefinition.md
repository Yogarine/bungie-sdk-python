# DestinyProgressionStepDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_name** | **str** | Very rarely, Progressions will have localized text describing the Level of the progression. This will be that localized text, if it exists. Otherwise, the standard appears to be to simply show the level numerically. | [optional] 
**display_effect_type** | **int** | This appears to be, when you \&quot;level up\&quot;, whether a visual effect will display and on what entity. See DestinyProgressionStepDisplayEffect for slightly more info. | [optional] 
**progress_total** | **int** | The total amount of progression points/\&quot;experience\&quot; you will need to initially reach this step. If this is the last step and the progression is repeating indefinitely (DestinyProgressionDefinition.repeatLastStep), this will also be the progress needed to level it up further by repeating this step again. | [optional] 
**reward_items** | [**list[DestinyItemQuantity]**](DestinyItemQuantity.md) | A listing of items rewarded as a result of reaching this level. | [optional] 
**icon** | **str** | If this progression step has a specific icon related to it, this is the icon to show. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


