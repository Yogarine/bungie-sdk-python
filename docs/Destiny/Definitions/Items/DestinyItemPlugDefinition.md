# DestinyItemPlugDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insertion_rules** | [**list[DestinyPlugRuleDefinition]**](DestinyPlugRuleDefinition.md) | The rules around when this plug can be inserted into a socket, aside from the socket&#39;s individual restrictions.  The live data DestinyItemPlugComponent.insertFailIndexes will be an index into this array, so you can pull out the failure strings appropriate for the user. | [optional] 
**plug_category_identifier** | **str** | The string identifier for the plug&#39;s category. Use the socket&#39;s DestinySocketTypeDefinition.plugWhitelist to determine whether this plug can be inserted into the socket. | [optional] 
**plug_category_hash** | **int** | The hash for the plugCategoryIdentifier. You can use this instead if you wish: I put both in the definition for debugging purposes. | [optional] 
**on_action_recreate_self** | **bool** | If you successfully socket the item, this will determine whether or not you get \&quot;refunded\&quot; on the plug. | [optional] 
**insertion_material_requirement_hash** | **int** | If inserting this plug requires materials, this is the hash identifier for looking up the DestinyMaterialRequirementSetDefinition for those requirements. | [optional] 
**preview_item_override_hash** | **int** | In the game, if you&#39;re inspecting a plug item directly, this will be the item shown with the plug attached. Look up the DestinyInventoryItemDefinition for this hash for the item. | [optional] 
**enabled_material_requirement_hash** | **int** | It&#39;s not enough for the plug to be inserted. It has to be enabled as well. For it to be enabled, it may require materials. This is the hash identifier for the DestinyMaterialRequirementSetDefinition for those requirements, if there is one. | [optional] 
**enabled_rules** | [**list[DestinyPlugRuleDefinition]**](DestinyPlugRuleDefinition.md) | The rules around whether the plug, once inserted, is enabled and providing its benefits.  The live data DestinyItemPlugComponent.enableFailIndexes will be an index into this array, so you can pull out the failure strings appropriate for the user. | [optional] 
**ui_plug_label** | **str** | Plugs can have arbitrary, UI-defined identifiers that the UI designers use to determine the style applied to plugs. Unfortunately, we have neither a definitive list of these labels nor advance warning of when new labels might be applied or how that relates to how they get rendered. If you want to, you can refer to known labels to change your own styles: but know that new ones can be created arbitrarily, and we have no way of associating the labels with any specific UI style guidance... you&#39;ll have to piece that together on your end. Or do what we do, and just show plugs more generically, without specialized styles. | [optional] 
**plug_style** | **int** |  | [optional] 
**is_pseudo_plug** | **bool** | If TRUE, the plug doesn&#39;t actually convey any benefit: it only exists to show information in the UI. | [optional] 
**plug_availability** | **int** | Indicates the rules about when this plug can be used. See the PlugAvailabilityMode enumeration for more information! | [optional] 
**alternate_ui_plug_label** | **str** | If the plug meets certain state requirements, it may have an alternative label applied to it. This is the alternative label that will be applied in such a situation. | [optional] 
**alternate_plug_style** | **int** | The alternate plug of the plug: only applies when the item is in states that only the server can know about and control, unfortunately. See AlternateUiPlugLabel for the related label info. | [optional] 
**is_dummy_plug** | **bool** | If TRUE, this plug is used for UI display purposes only, and doesn&#39;t have any interesting effects of its own. | [optional] 
**parent_item_override** | [**DestinyParentItemOverride**](DestinyParentItemOverride.md) | Do you ever get the feeling that a system has become so overburdened by edge cases that it probably should have become some other system entirely? So do I!  In totally unrelated news, Plugs can now override properties of their parent items. This is some of the relevant definition data for those overrides.  If this is populated, it will have the override data to be applied when this plug is applied to an item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


