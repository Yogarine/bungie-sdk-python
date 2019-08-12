# EmailViewDefinitionSetting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The identifier for this UI Setting, which can be used to relate it to custom strings or other data as desired. | [optional] 
**localization** | [**dict(str, EMailSettingLocalization)**](EMailSettingLocalization.md) | A dictionary of localized text for the EMail setting, keyed by the locale. | [optional] 
**set_by_default** | **bool** | If true, this setting should be set by default if the user hasn&#39;t chosen whether it&#39;s set or cleared yet. | [optional] 
**opt_in_aggregate_value** | **int** | The OptInFlags value to set or clear if this setting is set or cleared in the UI. It is the aggregate of all underlying opt-in flags related to this setting. | [optional] 
**subscriptions** | [**list[EmailSubscriptionDefinition]**](EmailSubscriptionDefinition.md) | The subscriptions to show as children of this setting, if any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


