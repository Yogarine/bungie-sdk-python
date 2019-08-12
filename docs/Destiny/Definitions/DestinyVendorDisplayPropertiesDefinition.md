# DestinyVendorDisplayPropertiesDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**large_icon** | **str** | I regret calling this a \&quot;large icon\&quot;. It&#39;s more like a medium-sized image with a picture of the vendor&#39;s mug on it, trying their best to look cool. Not what one would call an icon. | [optional] 
**subtitle** | **str** |  | [optional] 
**original_icon** | **str** | If we replaced the icon with something more glitzy, this is the original icon that the vendor had according to the game&#39;s content. It may be more lame and/or have less razzle-dazzle. But who am I to tell you which icon to use. | [optional] 
**requirements_display** | [**list[DestinyVendorRequirementDisplayEntryDefinition]**](DestinyVendorRequirementDisplayEntryDefinition.md) | Vendors, in addition to expected display property data, may also show some \&quot;common requirements\&quot; as statically defined definition data. This might be when a vendor accepts a single type of currency, or when the currency is unique to the vendor and the designers wanted to show that currency when you interact with the vendor. | [optional] 
**small_transparent_icon** | **str** | This is the icon used in parts of the game UI such as the vendor&#39;s waypoint. | [optional] 
**map_icon** | **str** | This is the icon used in the map overview, when the vendor is located on the map. | [optional] 
**large_transparent_icon** | **str** | This is apparently the \&quot;Watermark\&quot;. I am not certain offhand where this is actually used in the Game UI, but some people may find it useful. | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**icon** | **str** | Note that \&quot;icon\&quot; is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition&#39;s icon was a big picture of a book.  But usually, it will be a small square image that you can use as... well, an icon.  They are currently represented as 96px x 96px images. | [optional] 
**high_res_icon** | **str** | If this item has a high-res icon (at least for now, many things won&#39;t), then the path to that icon will be here. | [optional] 
**has_icon** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


