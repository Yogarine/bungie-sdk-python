# PostSearchResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_posts** | [**list[PostResponse]**](PostResponse.md) |  | [optional] 
**authors** | [**list[GeneralUser]**](GeneralUser.md) |  | [optional] 
**groups** | [**list[GroupResponse]**](GroupResponse.md) |  | [optional] 
**searched_tags** | [**list[TagResponse]**](TagResponse.md) |  | [optional] 
**polls** | [**list[PollResponse]**](PollResponse.md) |  | [optional] 
**recruitment_details** | [**list[ForumRecruitmentDetail]**](ForumRecruitmentDetail.md) |  | [optional] 
**available_pages** | **int** |  | [optional] 
**results** | [**list[PostResponse]**](PostResponse.md) |  | [optional] 
**total_results** | **int** |  | [optional] 
**has_more** | **bool** |  | [optional] 
**query** | [**PagedQuery**](PagedQuery.md) |  | [optional] 
**replacement_continuation_token** | **str** |  | [optional] 
**use_total_results** | **bool** | If useTotalResults is true, then totalResults represents an accurate count.  If False, it does not, and may be estimated/only the size of the current page.  Either way, you should probably always only trust hasMore.  This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


