---
type: simulink-block
title: 'Entity Batch Splitter'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Resource Allocation Modeling'
documentation_page: 'entitybatchsplitter'
documentation_source_path: 'ref/entitybatchsplitter.html'
language: en
---

# Entity Batch Splitter

## Ports

### Input

### **port\_1** — Input batch entity scalar | vector | matrix

Input entity port for entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **port\_1** — Output entity scalar | vector | matrix

Output entity port for entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **port\_a** — Number of entities arrived scalar

Number of entities that have arrived at the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities arrived,
a**.

**Data Types:** `double`

### **port\_d** — Number of entities that have departed the block scalar

Number of entities that have departed the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities departed,
d**.

**Data Types:** `double`

### **port\_rem** — Number of entities remaining in the block scalar

Number of entities still in the block that have yet to depart.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities remaining to
depart, rem**.

**Data Types:** `double`

### **port\_pe** — Pending entity in block off (default) | on

Selecting this check box outputs the value `1` for a
pending entity in the block, and `0` otherwise.

#### Dependencies

To enable this port, select the **Statistics** > **Pending entity in block, pe**.

**Data Types:** `double`

## Parameters

### **Event actions** — Specify the event action `Entry` (default) | `Unbatch` | `Exit` | `Blocked`

Specify the behavior of the entity on certain events. For example, the
**Entry** action is called when the entity enters the
block. To customize actions when entities enter, exit, or are unbatched or
blocked, enter MATLAB code in the `Entry action`, `Exit
action`, `Unbatch action`, or `Blocked
action` field of the **Event actions** tab.
For more information about event actions, see Events and Event Actions. For an example, see Manage Entities Using Event Actions

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntryAction, UnbatchAction, ExitAction, BlockedAction` |
| **Type**: character vector |
| **Values**: MATLAB code |
| **Default**: `''` |

### **Number of entities arrived, a** — Outputs the number of entities that have arrived at the block `off` (default) | `on`

Number of entities that have arrived at the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberOfEntitiesArrived` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities departed, d** — Outputs the number of entities that have departed the block `off` (default) | `on`

Selecting this check box outputs the number of entities that have exited
the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberOfEntitiesDeparted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities remaining to depart, rem** — Outputs the number of entities that remain in the block `off` (default) | `on`

Outputs the number of entities still in the block that have yet to
depart.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberOfEntitiesWaitingToDepart` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Pending entity in block, pe** — Pending entities `off` (default) | `on`

Indicates whether an entity that is yet to depart is present in the block.
The value is `1` for a pending entity, and
`0` otherwise.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PendingEntity` |
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

**Introduced in R2016b**

## Description

Split batch entities

The Entity Batch Splitter block splits a batched entity into its
individual entities and outputs each entity through the output port. A batched entity is
the output of the Entity Batch Creator block.

To customize actions when entities enter, exit, and are blocked or unbatched, enter
MATLAB® code in the `Entry action`, `Exit
action`, `Blocked action`, or `Unbatch
action` field of the **Event actions** tab.
