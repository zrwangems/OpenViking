---
type: simulink-block
title: 'Resource Acquirer'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'resourceacquirer'
documentation_source_path: 'ref/resourceacquirer.html'
language: en
---

# Resource Acquirer

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

### **Port\_w** — Average wait time for entities in the block scalar

Average wait time for entities in the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Average wait,
w**.

**Data Types:** `double`

### **Port\_ex** — Number of entities extracted scalar

Number of entities that are pulled out of this block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities extracted,
ex**.

**Data Types:** `double`

## Parameters

### **Maximum number of waiting entities** — Maximum number of entities that can wait for a resource `1` (default) | `scalar`

Enter the maximum number of entities that can wait for a resource.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberWaitingEntities` |
| **Type**: character vector |
| **Values**: `'1'` | scalar |
| **Default**: `'1'` |

### **Event actions** — Specify the behavior of the entity on certain events `Entry` (default) | `Exit` | `Blocked`

Define the behavior in the **Event actions**. For
example, the **Entry** action is called when an entity
enters the block.

**Note**

If an event action changes an entity, related block behavior such
as resorting a priority queue, and rescheduling of any events, will
occur after the event action has fully finished and returned.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntryAction, ExitAction, BlockedAction` |
| **Type**: character vector |
| **Values**: MATLAB code |
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

### **Average wait, w** — Outputs the average wait time `off` (default) | `on`

Sum of the wait times for entities departing the block divided by their
total number. *Wait time* is the duration between the
entity's entry into and exit from the Resource Acquirer
block. For more information, see Interpret SimEvents Models Using Statistical Analysis.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageWait` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities extracted, ex** — Number of entities extracted from this block `off` (default) | `on`

Outputs the number of extracted entities which are pulled out from this
block by the Entity Find block. When an entity is extracted,
its resource acquisition from the Resource Pool block is
canceled and **Number of entities departed, d**,
**Number of entities in block, n**, and
**Average wait, w** statistics are updated accordingly.
For more information about finding and extracting entities, see Find and Extract Entities in SimEvents Models.

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

Acquire entity resources

The Resource Acquirer block acquires for and assigns them to input
entities. You can specify which resource amounts and type the block acquires.

An entity does not depart the Resource Acquirer block until the entity
acquires all of the requested resources. For example, if an entity requests
`5` resources and there are `2` resources
available in a Resource Pool block, then the entity
waits until all the requested resources are available before exiting. Similarly, if an
entity requests `2` resources from one type and `3`
resources from another type, the entity waits until all of the resources from both types
are available.

Initialize a Resource Pool block with a specified
amount of available resources. Then:

- Use one or more Resource Acquirer blocks to reserve those
  resources.

  The priority order of Resource Acquirer blocks is determined at
  the beginning of a simulation and cannot be customized. The entity in the higher
  priority Resource Acquirer block always acquires the resource
  first.

  Two entities acquiring the same resource

  For example, suppose only `1` resource is available in the
  Resource Pool block and Resource Acquirer1 is higher priority
  than Resource Acquirer2. If Entity1 and Entity2 want to acquire the resource at
  the same time, Entity1 always acquires the resource. Even if the resource
  becomes available again and there are two entities Entity1 and Entity2 waiting
  in the ResourceAcquirer1 and ResourceAcquirer2, Entity1 again acquires the
  resource.
- Use a Resource Releaser block to
  return resources to the Resource Pool block for future
  use.

The visibility of the resources is determined by the **Resource
visibility** parameter of the Resource Pool blocks in the
model.

To customize actions when entities enter, exit, or are blocked, enter MATLAB® code in the `Entry action`, `Exit
action`, or `Blocked action` field of the **Event
actions** tab.

### Available Resources

Use the **Available Resources** controls to:

- Select the resources from the resources defined in all the Resource
  Pool blocks in the model.
- Add the resources to the **Selected Resources** table,
  where you can configure resource acquisition details.

The list displays all the available resources in the model. (If there are no
resources, the **Available Attributes** list is empty.)

If the resource list is long, you can type the resource name in the text box to
filter the list.

Use the buttons in the **Available Resources** section to help
build the resources table. The buttons perform these actions.

| Button | Action |
| --- | --- |
| Button with a green circular arrow symbol | Refresh the **Available Resources** list. The list updates with any upstream model changes you make while the block dialog box is open. |
| Button with a blue arrow pointing right | Add the selected resources to the **Selected Resources** table. |
| Button with a blue arrow pointing left | Move the selected resource from the **Selected Resources** table to the **Available Resources** list.  **Note**  If the selected resource is one you added manually, this button appears dimmed. |

The message area below the available resources list displays additional messages
about the resources, as they apply.

| Message | Meaning |
| --- | --- |
| `> Resource already selected` | You have already added the resource to the **Selected Resources** table. You cannot add the resource to the table again. |

### Selected Resources

Use the controls under **Selected Resources** to build and manage
the list of resources to attach to the entity. Each resource appears as a row in a
table.

Using these controls, you can:

- Add a resource manually.
- Modify a resource that you added to the table from the **Available
  Resources** list to attach to the entity.

The buttons under **Selected Resources** perform these
actions:

| Button | Action | Notes |
| --- | --- | --- |
| Button with a green plus symbol | Add a template resource to the table. | Rename the resource and specify its properties. |
| Button with two identical paper symbols overlapping | Add a copy of the selected resource to the table to use as the basis of a new resource. | Rename the copy. Two resources cannot have the same name. |
| Button with a red cross symbol | Remove the selected resource from the **Selected Resources** table. | When you delete a resource this way, no confirmation appears and you cannot undo the operation. |
| Button with a blue arrow pointing upward | Move up the selected resource in order in the **Selected Resources** table. | N/A |
| Button with a blue arrow pointing downward. | Move the selected resource down in order in the **Selected Resources** table. | N/A |

**Note**

If you delete a row and apply the change, the deletion can affect signal
output ports corresponding to other attributes. For example, if the block has a
signal output port **A2** and you delete the attribute with a
port marked **A1**, the block relabels **A2**
as **A1**. Verify that any signal that connects to the
relabeled port is still connected as you expect.

| Property | Specify | Use |
| --- | --- | --- |
| **Name** | The name of the resource. Each resource must have a unique name. | Double-click the existing name, and then type the new name. |
| **Amount Source** | Whether the resource amount, that an entity requests, comes from the dialog box or an attribute. | Select `Dialog` or `Attribute`. If you select `Attribute`, the source of the resource amount comes from the attribute of the entity. This option allows each entity to acquire varying amounts of resources. For more information, see Set Resource Amount with Attributes. |
| **Amount** | The value to assign to the resource (when the resource comes from the dialog box). | Double-click the value, and then type the value you want to assign.  This value is the number of resources acquired per entity. For example, if **Amount** is `3`, each entity that arrives at the Resource Acquire block must wait to acquire 3 resources before departing the block.  Granularity of the resources to be acquired matches the granularity of the resources in the Resource Pool block. |
