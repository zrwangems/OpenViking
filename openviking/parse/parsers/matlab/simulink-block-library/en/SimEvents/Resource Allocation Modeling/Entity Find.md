---
type: simulink-block
title: 'Entity Find'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Resource Allocation Modeling'
documentation_page: 'entityfind'
documentation_source_path: 'ref/entityfind.html'
language: en
---

# Entity Find

## Ports

### Input

### **Port\_1** — Input entities to trigger finding entities scalar | vector | matrix

Input port for entities to trigger the event of finding entities using a specific
resource.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_1** — Output found entity scalar | vector | matrix

Output entity port for entities that are found by the block.

#### Dependencies

To enable this port, select the **Extract found entities**
checkbox.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_f** — Number of entities found scalar

Number of entities that are found by the block.

#### Dependencies

To enable this port, click the **Statistics** tab and select
the box labeled **Number of entities found, f**.

**Data Types:** `double`

### **Port\_d** — Number of entities that have departed the block scalar

Number of entities that have departed the block.

#### Dependencies

To enable this port, click the **Statistics** tab and select
the box labeled **Number of entities departed, d**.

**Data Types:** `double`

### **Port\_n** — Number of found entities that have not yet departed the block scalar

Number of found entities that have not yet departed the block.

#### Dependencies

To enable this port, click the **Statistics** tab and select
the box labeled **Number of found entities in block, n**.

**Data Types:** `double`

### **Port\_w** — Average wait time for found entities in the block scalar

Average wait time for found entities in the block.

#### Dependencies

To enable this port, click the **Statistics** tab and select
the box labeled **Average wait, w**.

**Data Types:** `double`

### **Port\_l** — Average length of the found entity queue scalar

Outputs the average length of the found entity queue.

#### Dependencies

To enable this port, click the **Statistics** tab and select
the box labeled **Average queue length, l**.

**Data Types:** `double`

### **Port\_ex** — Number of entities extracted scalar

Number of entities that are extracted out of this block.

#### Dependencies

To enable this port, click the **Statistics** tab and select
the box labeled **Number of entities extracted, ex**.

**Data Types:** `double`

## Parameters

### Main

### **Resource** — Specify the name of the reference resource the entities use `Resource1` (default) | character vector

Name of the reference resource that is used by the entities to be found by the
block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ResourceName` |
| **Type**: character vector |
| **Values**: resource name |
| **Default**: `'Resource1'` |

### **Extract found entities** — Extract and reroute found entities `off` (default) | `on`

Extract and output the entities that are found in the search.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EnableOutput` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Additional filtering condition** — Add optional filtering condition `off` (default) | `on`

Enable the option to define additional matching conditions for finding entities.
If selected, a MATLAB editor appears where you can define additional matching
conditions.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntityFilter` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Matching condition** — Define the matching condition `match = true;` (default)

Use MATLAB code to define additional matching conditions for finding entities. The
block searches for entities such that the value of the boolean variable
`match` becomes `true`. For instance,
when

```
match = isequal(trigger.Attribute1, entity.Attribute1);
```

the
block finds entities that have the same Attribute1 value with the trigger entity,
because only their equality sets the `match` as
`true`.

While authoring additional matching conditions, you can use these
variables.

- `trigger` — Use to access the trigger entity
  attributes.
- `entity` — Use to access the attributes of the entity that is
  being found.
- `match` — Use as a Boolean value to be returned by the
  matching condition. The value of `match` is initialized as
  `false`.

#### Dependencies

This check box appears if the **Additional filtering
condition** check box in the **Main** tab is
selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MatchingCondition` |
| **Type**: character vector |
| **Values**: MATLAB code |
| **Default**: `'% match = isequal(trigger.Attribute1, entity.Attribute1);match = true;'` |

### Event Actions

### **Event actions** — Specify the event action `OnFound` (default) | `Entry` | `Exit` | `Blocked`

Specify the behavior of the entity on certain events. For example, the
**Entry** action is called when the entity enters the block. To
customize actions when entities enter, exit, or are found or blocked, enter
MATLAB code in the `Entry action`, `Exit
action`, `On found action`, or `Blocked
action` field of the **Event actions** tab. For more
information about event actions, see Events and Event Actions. For an example, see Manage Entities Using Event Actions

#### Dependencies

`On found action` appears only if the **Extract found
entities** check box is not selected.

`Entry action`, `Exit action`, and
`Blocked action` appear only if the **Extract found
entities** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntryAction, ExitAction, BlockedAction` |
| **Type**: character vector |
| **Values**: MATLAB code |
| **Default**: `''` |

### Statistics

### **Number of entities found, f** — Outputs the number of entities that are found `off` (default) | `on`

Number of entities that are found by the block during simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesDeparted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities departed, d** — Outputs the number of entities that have departed the block `off` (default) | `on`

Number of entities that have departed the block.

#### Dependencies

This check box appears if the **Extract found entities** check
box in the **Main** tab is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesDeparted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of found entities in block, n** — Outputs the number of found entities that are yet to depart `off` (default) | `on`

Number of found entities that are yet to depart.

#### Dependencies

This check box appears if the **Extract found entities** check
box in the **Main** tab is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesInBlock` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Average wait, w** — Outputs the average wait time `off` (default) | `on`

Sum of the wait times for entities departing the block divided by their total
number. *Wait time* is the duration between the Entity
Find block entry and exit of an entity. For more information, see Interpret SimEvents Models Using Statistical Analysis.

#### Dependencies

This check box appears if the **Extract found entities** check
box in the **Main** tab is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageWait` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Average queue length, l** — Outputs the average length of the entity queue `off` (default) | `on`

Accumulated time-weighted average queue size. The block computes this value by:

1. Multiplying the size of the queue by its duration to calculate time-weighted
   queue size
2. Summing up all time-weighted queue sizes and averaging them over total
   time

For more information, see Interpret SimEvents Models Using Statistical Analysis.

#### Dependencies

This check box appears if the **Extract found entities** check
box in the **Main** tab is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageStoreSize` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities extracted, ex** — Number of entities extracted from this block `off` (default) | `on`

Outputs the number of extracted entities.

#### Dependencies

This check box appears if the **Extract found entities** check
box in the **Main** tab is selected.

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

**Introduced in R2018b**

## Description

Find entities

The Entity Find block finds entities that use a specific resource. The
block receives a trigger entity from its input port. Upon receiving the trigger entity, it
initiates a search across all blocks in a model for entities with a specific resource. You can
further filter the search for finding entities by adding additional filtering conditions. The
block can manipulate the found entities in these ways.

- Search entities that satisfy a specific condition across blocks in a model to find and
  examine them.
- Extract found entities from the model without modifying them.
- Change the attributes of the found entities at their location in the model without
  extraction.

  In this case, to customize actions when the entity is found, in the **Event
  actions** tab, in the `On found action` field enter
  MATLAB® code.
- Extract and change entity attributes. The extracted entities are queued in the block
  and rerouted through its output port.

  In this case, to customize actions when entities enter, exit, or are blocked, enter
  MATLAB code in the `Entry action`, `Exit action`,
  or `Blocked action` field of the **Event actions** tab.
  For more information, see Write Event Actions for Legacy Models.

The block can extract entities from Entity Server, Entity
Queue, Entity Store, Resource Acquirer, Entity
Replicator, Conveyor System, Entity Selector,
MATLAB Discrete-Event System, and Discrete-Event Chart
blocks.

When an entity is extracted, pending events and statistics are updated accordingly. For
instance, if an entity is extracted by an Entity Find block from an
Entity Server block during the service period, the rest of the service is
canceled and the output of the statistics are updated.

**Note**

The block can find only one entity type that you specify in the model and it cannot find
or extract entities across model reference boundaries.

For more information about common workflows involving Entity Find block,
see Find and Extract Entities in SimEvents Models.
