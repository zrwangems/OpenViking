---
type: simulink-block
title: 'Resource Releaser'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'resourcereleaser'
documentation_source_path: 'ref/resourcereleaser.html'
language: en
---

# Resource Releaser

## Ports

### Input

### **Port\_1** — Input entity scalar | vector | matrix

Input entity port for entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_1** — Output entity scalar | vector | matrix

Output entity port for entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — Number of entities that have departed the block scalar

Number of entities that have departed the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities departed,
d**.

**Data Types:** `double`

### **Port\_n** — Number of entities that have not yet departed the block scalar

Number of entities that have not yet departed the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities in block,
n**.

**Data Types:** `double`

### **Port\_ex** — Number of entities extracted scalar

Number of entities that are pulled out of this block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities extracted,
ex**.

**Data Types:** `double`

## Parameters

### **Resource to release** — Select the resources to release `All` (default) | `Selected`

Select the resources to release.

- `All`

  Release the use of all resources for a passing entity.
- `Selected`

  Release selected resources. Selecting this option enables the
  **Available Resources** table.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ResourceToRelease` |
| **Type**: character vector |
| **Values**: `'All'` | `'Selected'` |
| **Default**: `'All'` |

### **Event actions** — Specify the behavior of the entity on certain events `Entry` (default) | `Exit` | `Blocked`

Define the behavior in the **Event actions**. For
example, the **Entry** action is called when an entity
enters the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntryAction, ExitAction, BlockedAction` |
| **Type**: character vector |
| **Values**: MATLAB® code |
| **Default**: `''` |

### **Number of entities departed, d** — Outputs the number of entities that have departed the block `off` (default) | `on`

Selecting this check box outputs the number of entities that have exited
the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesDeparted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities in block, n** — Outputs the number of entities present in the block, which have yet to depart `off` (default) | `on`

Selecting this check box outputs the number of entities present in the
block, which have yet to depart.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesInBlock` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities extracted, ex** — Number of entities extracted from this block `off` (default) | `on`

Number of extracted entities that are pulled out from this block by the
Entity Find block. For more information about finding and
extracting entities, see Find and Extract Entities in SimEvents Models.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumEntitiesExtracted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Release entity resources

The Resource Releaser block releases resources when an entity enters
the block. The block accepts one entity and the entity departs the block immediately
provided it is accepted by the next block or extracted by the Entity Find
block.

You can specify that the block release certain resource types or release all
resources.

### Available Resources

Use the **Available Resources** controls to:

- Select the resources from the resources defined in all the Resource
  Pool blocks in the model.
- Add the resources to the Selected Resources table, where you can modify
  them.

The list displays all the resources in the model. (If there are no resources, the
**Available Resources** list is empty).

If the resource list is long, you can type the resource name in the text box to
filter the list.

Use the buttons in the **Available Resources** section to help
build the resources table. The buttons perform these actions.

| Button | Action |
| --- | --- |
| Button with circular green arrow symbol | Refresh the **Available Resources** list. The list updates with any upstream model changes you make while the block dialog box is open. |
| Button with blue arrow pointing right. | Add the selected resources to the **Selected Resources** table. |
| Button with blue arrow pointing left | Move the selected resource from the **Selected Resources** table to the **Available Resources** list.  If the selected resource is one you added manually, this button appears dimmed. |

The message area below the available resources list displays additional messages
about the resources, as they apply.

| Message | Meaning |
| --- | --- |
| `> Resource already selected` | You have already added the resource to the **Selected Resources** table. You cannot add the resource to the table again. |

### Selected Resources

Use the controls under **Selected Resources** to build and manage
the list of resources to release. Each resource appears as a row in a table.

Using these controls, you can:

- Add a resource manually.
- Modify a resource that you added to the table from the **Available
  Resources** list to release.
- Choose the amount of resources to be released by setting the
  **Amount Source** parameter to
  `Dialog` or
  `Attribute`.

  - `Dialog` — Specify the amount of
    resources to be released under the **Amount**
    column.
  - `Attribute` — Specify the name of the attribute
    that defines the amount of resources to be released.

The buttons under **Selected Resources** perform these
actions.

| Button | Action | Notes |
| --- | --- | --- |
| Button with green plus symbol | Add a template resource to the table. | Rename the resource and specify its properties. |
| Button with identical paper symbols overlapping | Add a copy of the selected resource to the table to use as the basis of a new resource. | Rename the copy. Two resources cannot have the same name. |
| Button with red cross symbol | Remove the selected resource from the **Selected Resources** table. | When you delete a resource this way, no confirmation appears and you cannot undo the operation. |
| Button with blue arrow pointing upward | Move up the selected resource in order in the **Selected Resources** table. | N/A |
| Button with blue arrow pointing downward | Move the selected resource down in order in the **Selected Resources** table. | N/A |

**Note**

If you delete a row and apply the change, the deletion can affect signal
output ports corresponding to other attributes. For example, if the block has a
signal output port **A2** and you delete the attribute with a
port marked **A1**, the block relabels **A2**
as **A1**. Verify that any signal that connects to the
relabeled port is still connected as you expect.

| Property | Specification | Usage |
| --- | --- | --- |
| **Name** | The name of the resource. Each resource must have a unique name. | Double-click the existing name, and then type the new name. |
| **Amount Source** | Whether the resource amount, that an entity requests, comes from the dialog box or an attribute. | Select `Dialog` or `Attribute`. If you select `Attribute`, the source of the resource amount comes from the attribute of the entity. This option allows each entity to acquire varying amounts of resources. For more information, see Set Resource Amount with Attributes. |
| **Amount** | The value to assign to the resource (when the resource comes from the dialog box). | Double-click the value, and then type the value you want to assign.  This value is the number of resources released per entity. For example, if **Amount** is three, each entity that arrives at the Resource Releaser block must wait to release 3 resources before departing the block.  Granularity of the resources to be released matches the granularity of the resources in the Resource Pool block. |
