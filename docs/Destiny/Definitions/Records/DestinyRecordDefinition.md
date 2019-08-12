# DestinyRecordDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_properties** | [**DestinyDisplayPropertiesDefinition**](DestinyDisplayPropertiesDefinition.md) |  | [optional] 
**scope** | **int** | Indicates whether this Record&#39;s state is determined on a per-character or on an account-wide basis. | [optional] 
**presentation_info** | [**DestinyPresentationChildBlock**](DestinyPresentationChildBlock.md) |  | [optional] 
**lore_hash** | **int** |  | [optional] 
**objective_hashes** | **list[int]** |  | [optional] 
**record_value_style** | **int** |  | [optional] 
**title_info** | [**DestinyRecordTitleBlock**](DestinyRecordTitleBlock.md) |  | [optional] 
**completion_info** | [**DestinyRecordCompletionBlock**](DestinyRecordCompletionBlock.md) |  | [optional] 
**state_info** | [**SchemaRecordStateBlock**](SchemaRecordStateBlock.md) |  | [optional] 
**requirements** | [**DestinyPresentationNodeRequirementsBlock**](DestinyPresentationNodeRequirementsBlock.md) |  | [optional] 
**expiration_info** | [**DestinyRecordExpirationBlock**](DestinyRecordExpirationBlock.md) |  | [optional] 
**reward_items** | [**list[DestinyItemQuantity]**](DestinyItemQuantity.md) | If there is any publicly available information about rewards earned for achieving this record, this is the list of those items.   However, note that some records intentionally have \&quot;hidden\&quot; rewards. These will not be returned in this list. | [optional] 
**hash** | **int** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


