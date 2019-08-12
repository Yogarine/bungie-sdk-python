# GroupResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**GroupV2**](GroupV2.md) |  | [optional] 
**founder** | [**GroupMember**](GroupMember.md) |  | [optional] 
**allied_ids** | **list[int]** |  | [optional] 
**parent_group** | [**GroupV2**](GroupV2.md) |  | [optional] 
**alliance_status** | **int** |  | [optional] 
**group_join_invite_count** | **int** |  | [optional] 
**current_user_member_map** | [**dict(str, GroupMember)**](GroupMember.md) | This property will be populated if the authenticated user is a member of the group. Note that because of account linking, a user can sometimes be part of a clan more than once. As such, this returns the highest member type available. | [optional] 
**current_user_potential_member_map** | [**dict(str, GroupPotentialMember)**](GroupPotentialMember.md) | This property will be populated if the authenticated user is an applicant or has an outstanding invitation to join. Note that because of account linking, a user can sometimes be part of a clan more than once. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


