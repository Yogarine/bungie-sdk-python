# DestinyProfileUserInfoCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_last_played** | **datetime** |  | [optional] 
**applicable_membership_types** | **list[int]** | The list of membership types/Platforms that this Destiny Account can be used on - either its own original platform, or any subservient platforms hooked up to it through Cross Save. | [optional] 
**is_overridden** | **bool** | If this profile is being overridden/obscured by Cross Save, this will be set to true. We will still return the profile for display purposes where users need to know the info: it is up to any given area of the app/site to determine if this profile should still be shown. | [optional] 
**is_cross_save_primary** | **bool** | If true, this account is hooked up as the \&quot;Primary\&quot; cross save account for one or more platforms. | [optional] 
**supplemental_display_name** | **str** | A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc. | [optional] 
**icon_path** | **str** | URL the Icon if available. | [optional] 
**membership_type** | **int** | Type of the membership. | [optional] 
**membership_id** | **int** | Membership ID as they user is known in the Accounts service | [optional] 
**display_name** | **str** | Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


