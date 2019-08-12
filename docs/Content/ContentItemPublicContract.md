# ContentItemPublicContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_id** | **int** |  | [optional] 
**c_type** | **str** |  | [optional] 
**cms_path** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**allow_comments** | **bool** |  | [optional] 
**has_age_gate** | **bool** |  | [optional] 
**minimum_age** | **int** |  | [optional] 
**rating_image_path** | **str** |  | [optional] 
**author** | [**GeneralUser**](GeneralUser.md) |  | [optional] 
**auto_english_property_fallback** | **bool** |  | [optional] 
**properties** | **dict(str, object)** | Firehose content is really a collection of metadata and \&quot;properties\&quot;, which are the potentially-but-not-strictly localizable data that comprises the meat of whatever content is being shown.  As Cole Porter would have crooned, \&quot;Anything Goes\&quot; with Firehose properties. They are most often strings, but they can theoretically be anything. They are JSON encoded, and could be JSON structures, simple strings, numbers etc... The Content Type of the item (cType) will describe the properties, and thus how they ought to be deserialized. | [optional] 
**representations** | [**list[ContentRepresentation]**](ContentRepresentation.md) |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**comment_summary** | [**CommentSummary**](CommentSummary.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


