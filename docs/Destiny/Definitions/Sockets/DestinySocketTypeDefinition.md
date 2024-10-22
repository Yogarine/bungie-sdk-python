# DestinySocketTypeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_properties** | [**DestinyDisplayPropertiesDefinition**](DestinyDisplayPropertiesDefinition.md) | There are fields for this display data, but they appear to be unpopulated as of now. I am not sure where in the UI these would show if they even were populated, but I will continue to return this data in case it becomes useful. | [optional] 
**insert_action** | [**DestinyInsertPlugActionDefinition**](DestinyInsertPlugActionDefinition.md) | Defines what happens when a plug is inserted into sockets of this type. | [optional] 
**plug_whitelist** | [**list[DestinyPlugWhitelistEntryDefinition]**](DestinyPlugWhitelistEntryDefinition.md) | A list of Plug \&quot;Categories\&quot; that are allowed to be plugged into sockets of this type.  These should be compared against a given plug item&#39;s DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item&#39;s category.  If the plug&#39;s category matches any whitelisted plug, or if the whitelist is empty, it is allowed to be inserted. | [optional] 
**socket_category_hash** | **int** |  | [optional] 
**visibility** | **int** | Sometimes a socket isn&#39;t visible. These are some of the conditions under which sockets of this type are not visible. Unfortunately, the truth of visibility is much, much more complex. Best to rely on the live data for whether the socket is visible and enabled. | [optional] 
**always_randomize_sockets** | **bool** |  | [optional] 
**is_preview_enabled** | **bool** |  | [optional] 
**hide_duplicate_reusable_plugs** | **bool** |  | [optional] 
**overrides_ui_appearance** | **bool** | This property indicates if the socket type determines whether Emblem icons and nameplates should be overridden by the inserted plug item&#39;s icon and nameplate. | [optional] 
**avoid_duplicates_on_initialization** | **bool** |  | [optional] 
**currency_scalars** | [**list[DestinySocketTypeScalarMaterialRequirementEntry]**](DestinySocketTypeScalarMaterialRequirementEntry.md) |  | [optional] 
**hash** | **int** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


