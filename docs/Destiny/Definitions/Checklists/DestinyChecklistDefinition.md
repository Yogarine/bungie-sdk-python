# DestinyChecklistDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_properties** | [**DestinyDisplayPropertiesDefinition**](DestinyDisplayPropertiesDefinition.md) |  | [optional] 
**view_action_string** | **str** | A localized string prompting you to view the checklist. | [optional] 
**scope** | **int** | Indicates whether you will find this checklist on the Profile or Character components. | [optional] 
**entries** | [**list[DestinyChecklistEntryDefinition]**](DestinyChecklistEntryDefinition.md) | The individual checklist items. Gotta catch &#39;em all. | [optional] 
**hash** | **int** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


