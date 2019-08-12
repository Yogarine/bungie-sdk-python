# DestinyVendorCategoryEntryDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_index** | **int** | The index of the category in the original category definitions for the vendor. | [optional] 
**category_id** | **str** | The string identifier of the category. | [optional] 
**sort_value** | **int** | Used in sorting items in vendors... but there&#39;s a lot more to it. Just go with the order provided in the itemIndexes property on the DestinyVendorCategoryComponent instead, it should be more reliable than trying to recalculate it yourself. | [optional] 
**category_hash** | **int** | The hashed identifier for the category. | [optional] 
**quantity_available** | **int** | The amount of items that will be available when this category is shown. | [optional] 
**show_unavailable_items** | **bool** | If items aren&#39;t up for sale in this category, should we still show them (greyed out)? | [optional] 
**hide_if_no_currency** | **bool** | If you don&#39;t have the currency required to buy items from this category, should the items be hidden? | [optional] 
**hide_from_regular_purchase** | **bool** | True if this category doesn&#39;t allow purchases. | [optional] 
**buy_string_override** | **str** | The localized string for making purchases from this category, if it is different from the vendor&#39;s string for purchasing. | [optional] 
**disabled_description** | **str** | If the category is disabled, this is the localized description to show. | [optional] 
**display_title** | **str** | The localized title of the category. | [optional] 
**overlay** | [**DestinyVendorCategoryOverlayDefinition**](DestinyVendorCategoryOverlayDefinition.md) | If this category has an overlay prompt that should appear, this contains the details of that prompt. | [optional] 
**vendor_item_indexes** | **list[int]** | A shortcut for the vendor item indexes sold under this category. Saves us from some expensive reorganization at runtime. | [optional] 
**is_preview** | **bool** | Sometimes a category isn&#39;t actually used to sell items, but rather to preview them. This implies different UI (and manual placement of the category in the UI) in the game, and special treatment. | [optional] 
**is_display_only** | **bool** | If true, this category only displays items: you can&#39;t purchase anything in them. | [optional] 
**reset_interval_minutes_override** | **int** |  | [optional] 
**reset_offset_minutes_override** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


