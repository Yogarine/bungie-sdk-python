# DestinyItemSocketEntryDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**socket_type_hash** | **int** | All sockets have a type, and this is the hash identifier for this particular type. Use it to look up the DestinySocketTypeDefinition: read there for more information on how socket types affect the behavior of the socket. | [optional] 
**single_initial_item_hash** | **int** | If a valid hash, this is the hash identifier for the DestinyInventoryItemDefinition representing the Plug that will be initially inserted into the item on item creation. Otherwise, this Socket will either start without a plug inserted, or will have one randomly inserted. | [optional] 
**reusable_plug_items** | [**list[DestinyItemSocketEntryPlugItemDefinition]**](DestinyItemSocketEntryPlugItemDefinition.md) | This is a list of pre-determined plugs that can *always* be plugged into this socket, without the character having the plug in their inventory.  If this list is populated, you will not be allowed to plug an arbitrary item in the socket: you will only be able to choose from one of these reusable plugs. | [optional] 
**prevent_initialization_on_vendor_purchase** | **bool** | If this is true, then the socket will not be initialized with a plug if the item is purchased from a Vendor.  Remember that Vendors are much more than conceptual vendors: they include \&quot;Collection Kiosks\&quot; and other entities. See DestinyVendorDefinition for more information. | [optional] 
**hide_perks_in_item_tooltip** | **bool** | If this is true, the perks provided by this socket shouldn&#39;t be shown in the item&#39;s tooltip. This might be useful if it&#39;s providing a hidden bonus, or if the bonus is less important than other benefits on the item. | [optional] 
**plug_sources** | **int** | Indicates where you should go to get plugs for this socket. This will affect how you populate your UI, as well as what plugs are valid for this socket. It&#39;s an alternative to having to check for the existence of certain properties (reusablePlugItems for example) to infer where plugs should come from. | [optional] 
**reusable_plug_set_hash** | **int** | If this socket&#39;s plugs come from a reusable DestinyPlugSetDefinition, this is the identifier for that set. We added this concept to reduce some major duplication that&#39;s going to come from sockets as replacements for what was once implemented as large sets of items and kiosks (like Emotes). | [optional] 
**randomized_plug_items** | [**list[DestinyItemSocketEntryPlugItemRandomizedDefinition]**](DestinyItemSocketEntryPlugItemRandomizedDefinition.md) | As of Forsaken, item sockets can have randomized plugs. If this is populated, the live data will return a subset of plugs from this list that are active and able to be inserted into the socket just like a reusable plug. | [optional] 
**default_visible** | **bool** | If true, then this socket is visible in the item&#39;s \&quot;default\&quot; state. If you have an instance, you should always check the runtime state, as that can override this visibility setting: but if you&#39;re looking at the item on a conceptual level, this property can be useful for hiding data such as legacy sockets - which remain defined on items for infrastructure purposes, but can be confusing for users to see. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


