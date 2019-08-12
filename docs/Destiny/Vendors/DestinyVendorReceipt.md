# DestinyVendorReceipt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_paid** | [**list[DestinyItemQuantity]**](DestinyItemQuantity.md) | The amount paid for the item, in terms of items that were consumed in the purchase and their quantity. | [optional] 
**item_received** | [**DestinyItemQuantity**](DestinyItemQuantity.md) | The item that was received, and its quantity. | [optional] 
**license_unlock_hash** | **int** | The unlock flag used to determine whether you still have the purchased item. | [optional] 
**purchased_by_character_id** | **int** | The ID of the character who made the purchase. | [optional] 
**refund_policy** | **int** | Whether you can get a refund, and what happens in order for the refund to be received. See the DestinyVendorItemRefundPolicy enum for details. | [optional] 
**sequence_number** | **int** | The identifier of this receipt. | [optional] 
**time_to_expiration** | **int** | The seconds since epoch at which this receipt is rendered invalid. | [optional] 
**expires_on** | **datetime** | The date at which this receipt is rendered invalid. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


