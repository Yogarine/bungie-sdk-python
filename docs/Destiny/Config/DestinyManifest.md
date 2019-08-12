# DestinyManifest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**mobile_asset_content_path** | **str** |  | [optional] 
**mobile_gear_asset_data_bases** | [**list[GearAssetDataBaseDefinition]**](GearAssetDataBaseDefinition.md) |  | [optional] 
**mobile_world_content_paths** | **dict(str, str)** |  | [optional] 
**json_world_content_paths** | **dict(str, str)** |  | [optional] 
**mobile_clan_banner_database_path** | **str** |  | [optional] 
**mobile_gear_cdn** | **dict(str, str)** |  | [optional] 
**icon_image_pyramid_info** | [**list[ImagePyramidEntry]**](ImagePyramidEntry.md) | Information about the \&quot;Image Pyramid\&quot; for Destiny icons. Where possible, we create smaller versions of Destiny icons. These are found as subfolders under the location of the \&quot;original/full size\&quot; Destiny images, with the same file name and extension as the original image itself. (this lets us avoid sending largely redundant path info with every entity, at the expense of the smaller versions of the image being less discoverable) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


