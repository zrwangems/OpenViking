---
type: simulink-block
title: 'Entity Batch Creator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Queue, Service, and Route Modeling / Events'
documentation_page: 'entitybatchcreator'
documentation_source_path: 'ref/entitybatchcreator.html'
language: en
---

# Entity Batch Creator

## Ports

### Input

### **Port\_1** — Input entity scalar | vector | matrix

Input entity port for entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_1** — Output batch entity scalar | vector | matrix

Output entity port for batch entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_a** — Number of entities arrived scalar

Number of entities that have arrived at the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities arrived,
a**.

**Data Types:** `double`

### **Port\_d** — Number of entities that have departed the block scalar

Number of entities that have departed the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities departed,
d**.

**Data Types:** `double`

### **Port\_rem** — Number of entities remaining for the next batch scalar

Number of entities that remain for the next batch.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities remaining
for the next batch, rem**.

**Data Types:** `double`

### **Port\_pe** — Pending entity in block off (default) | on

Selecting this check box outputs `1` for a pending
entity in the block, and `0` otherwise.

#### Dependencies

To enable this port, select the **Statistics** > **Pending entity in block, pe**.

**Data Types:** `double`

## Parameters

### **Number of entities in batch** — Number of entities in one batch `4` (default) | scalar

Specify the number of entities in a batch.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberOfEntitiesInBatch` |
| **Type**: character vector |
| **Values**: `'4'` | scalar |
| **Default**: `'4'` |

### **Entity type name** — Name of the batched entity that is created after combining incoming entities `Batch` (default) | character vector

Specify the name of the batched entity that is created after combining
incoming entities.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntityTypeName` |
| **Type**: character vector |
| **Values**: `'Batch'` | character vector |
| **Default**: `'Batch'` |

### **Bus object** — Specify whether to output the batched entity as a bus object off (default) | on

Specify whether to output the batched entity as a bus object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BusObject` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Input entity name** — Specify names to be attached to the input entities `batch` (default) | character vector

Specify names to be attached to the input entities, which can be used for
referencing these entities in the batched entity.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputEntityName` |
| **Type**: character vector |
| **Values**: `'batch'` | character vector |
| **Default**: `'batch'` |

### **Event actions** — Specify the event action `Entry` (default) | `Batch generate` | `Exit` | `Blocked`

Specify the behavior of the entity on certain events. For example, the
**Entry** action is called when the entity enters the
block. To customize actions when entities enter, exit, or are batched or
blocked, enter MATLAB code in the `Entry action`, `Exit
action`, `Batch generate action`, or
`Blocked action` field of the **Event
actions** tab. For more information about event actions, see
Events and Event Actions. For an example, see Manage Entities Using Event Actions

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntryAction, BatchGenerateAction, ExitAction, BlockedAction` |
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

### **Number of entities departed, d** — Outputs the number of entities departed the block `off` (default) | `on`

Number of entities that have departed the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberOfEntitiesDeparted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities remaining for next batch, rem** — Outputs the number of entities remaining for the next batch `off` (default) | `on`

Outputs the number of entities still in the block for the next batch of
entities.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberOfEntitiesRequiredForNextBatch` |
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

Create batch of entities

The Entity Batch Creator receives the expected number of entities and
creates a batch entity that contains all these entities. The batched entity is an array
of entities. Any acquired resources have to be released using a Resource Releaser block before batching
an input entity.

To customize actions when entities enter, exit, or are batched or blocked, enter
MATLAB® code in the `Entry action`, `Exit
action`, `Batch generate action`, or `Blocked
action` field of the **Event actions** tab. For more
information about event actions, see Events and Event Actions.

You can write MATLAB code to manipulate the attributes of the batched entity. For example, to
access attributes after an entity batch is generated, select `Batch generate
action` and use the code.

```
entity.batch
```

If
the number of entities in a batch is `4`, then
`entity.batch` is a
`4`-by-`1` structure array. To manipulate
`Attribute1` of the third entity in the batch enter the
code.

```
entity.batch(3).Attribute1
```

You can reference batched entity attributes in event actions. You cannot reference
them in:

- Priority queues — Do not set **Priority source**
  parameter to `PriorityAttribute`.
- Entity Server block — Do not set **Service time
  source** parameter to `Attribute`.
- Output Switch block — Do not set **Switching
  criterion** parameter to `From
  attribute`.

To output the batch as a bus object, select the **Bus object**
parameter. Consider creating a bus object for the batched entity when:

- Sending or receiving a batched entity to or from a MATLAB
  Discrete-Event System block.
- Sending or receiving a batched entity to or from a Discrete-Event
  Chart block.
- When passing full entity data to a Simulink Function
  block.
- When converting a batched entity to a signal using the Message
  Receive block.
