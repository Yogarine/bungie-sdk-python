# EmailOptInDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique identifier for this opt-in category. | [optional] 
**value** | **int** | The flag value for this opt-in category. For historical reasons, this is defined as a flags enum. | [optional] 
**set_by_default** | **bool** | If true, this opt-in setting should be set by default in situations where accounts are created without explicit choices about what they&#39;re opting into. | [optional] 
**dependent_subscriptions** | [**list[EmailSubscriptionDefinition]**](EmailSubscriptionDefinition.md) | Information about the dependent subscriptions for this opt-in. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


