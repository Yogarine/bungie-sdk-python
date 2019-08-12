# TrendingEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **float** | The weighted score of this trending item. | [optional] 
**is_featured** | **bool** |  | [optional] 
**identifier** | **str** | We don&#39;t know whether the identifier will be a string, a uint, or a long... so we&#39;re going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type. | [optional] 
**entity_type** | **int** | An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item. | [optional] 
**display_name** | **str** | The localized \&quot;display name/article title/&#39;primary localized identifier&#39;\&quot; of the entity. | [optional] 
**tagline** | **str** | If the entity has a localized tagline/subtitle/motto/whatever, that is found here. | [optional] 
**image** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**link** | **str** |  | [optional] 
**webm_video** | **str** | If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo | [optional] 
**mp4_video** | **str** | If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo | [optional] 
**feature_image** | **str** | If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don&#39;t use it all the time. | [optional] 
**items** | [**list[TrendingEntry]**](TrendingEntry.md) | If the item is of entityType TrendingEntryType.Container, it may have items - also Trending Entries - contained within it. This is the ordered list of those to display under the Container&#39;s header. | [optional] 
**creation_date** | **datetime** | If the entry has a date at which it was created, this is that date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


