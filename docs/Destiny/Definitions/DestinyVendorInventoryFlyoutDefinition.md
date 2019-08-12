# DestinyVendorInventoryFlyoutDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locked_description** | **str** | If the flyout is locked, this is the reason why. | [optional] 
**display_properties** | [**DestinyDisplayPropertiesDefinition**](DestinyDisplayPropertiesDefinition.md) | The title and other common properties of the flyout. | [optional] 
**buckets** | [**list[DestinyVendorInventoryFlyoutBucketDefinition]**](DestinyVendorInventoryFlyoutBucketDefinition.md) | A list of inventory buckets and other metadata to show on the screen. | [optional] 
**flyout_id** | **int** | An identifier for the flyout, in case anything else needs to refer to them. | [optional] 
**suppress_newness** | **bool** | If this is true, don&#39;t show any of the glistening \&quot;this is a new item\&quot; UI elements, like we show on the inventory items themselves in in-game UI. | [optional] 
**equipment_slot_hash** | **int** | If this flyout is meant to show you the contents of the player&#39;s equipment slot, this is the slot to show. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


