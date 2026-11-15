---
type: simulink-block
title: 'Queue'
family: messages-events
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'queue'
language: en
---

# Queue

## Ports

### Input

### **Port\_1** — Input entity or message scalar | vector | matrix

Input entity or message that carries scalar, bus, or vector data to
enter the queue.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_1** — Output entity or message scalar | vector | matrix

Output port that allows entities or messages at the head of the queue
to depart when a downstream block is ready to accept them.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — Number of entities that have departed the block scalar

Number of entities that have departed the block.

#### Dependencies

To enable this port, in the **Statistics** tab,
select the **Number of entities departed, d** check
box.

**Data Types:** `double`

### **Port\_n** — Number of entities that have not yet departed the block scalar

Number of entities that have not yet departed the block.

#### Dependencies

To enable this port, in the **Statistics** tab,
select the **Number of entities in block, n** check
box.

**Data Types:** `double`

### **Port\_w** — Average wait time for entities in the block scalar

Average wait time for entities in the block.

#### Dependencies

To enable this port, in the **Statistics** tab,
select the **Average wait, w** check box.

**Data Types:** `double`

### **Port\_l** — Average length of the entity queue scalar

**Port\_l** outputs the average length of the entity
queue.

#### Dependencies

To enable this port, in the **Statistics** tab,
select the **Average queue length, l** check
box.

**Data Types:** `double`

### **Port\_ex** — Number of entities extracted scalar

Number of entities that are pulled out of this block.

#### Dependencies

To enable this port, in the **Statistics** tab,
select the **Number of entities extracted, ex**
check box.

**Data Types:** `double`

## Parameters

### **Overwrite the oldest element if queue is full** — Specify queue overwriting policy on (default for Simulink®) | off (default for SimEvents®)

Select this check box to choose between two queue overwriting
policies.

- If you select the check box, an incoming message overwrites the
  oldest if the queue is full.

  This mode represents a simple message buffer that you can use to
  generate asynchronous communication between Simulink components and production code.
- If you clear the check box, the block does not accept new messages
  if the queue is full.

  In this mode, you can manipulate entity data using event actions
  and visualize statistics.

  To customize actions when entities or messages enter, exit, or are
  blocked, enter MATLAB® code in the `Entry action`,
  `Exit action`, or `Blocked
  action` field of the **Event actions**
  tab. For more information, see Events and Event Actions (SimEvents).

  For an example, see Manage Entities Using Event Actions (SimEvents).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QueueOverwriting` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` (for Simulink) and `'off'` (for SimEvents) |

### **Capacity** — Specify the capacity of the queue 25 (default) | scalar

Specify the capacity of the queue.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Capacity` |
| **Type**: character vector |
| **Values**: `'25'` | scalar |
| **Default**: `'25'` |

### **Queue type** — Choose the queue type `FIFO` (default) | `LIFO` | `Priority`

Choose the queue type.

- `FIFO` — first-in-first-out
- `LIFO` — last-in-first-out
- `Priority` — store elements in order of
  priority, see Serve High-Priority Customers by Sorting Entities Based on Priority (SimEvents).
  `Priority` can be selected when you
  clear the **Overwrite the oldest element if queue is
  full** check box.

  **Note**

  Priority queue does not support `fixed
  point` data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QueueType` |
| **Type**: character vector |
| **Values**: `'FIFO'` | `'LIFO'` | `'Priority'` |
| **Default**: `'FIFO'` |

### **Multicast tag** — Specify the tag when accepting entities broadcast via multicast sources `A` (default) | character vector

Specify the tag when accepting entities broadcast via multicast sources.
The Entity Multicast block requires SimEvents license.

#### Dependencies

This parameter is visible when you clear the **Overwrite the
oldest element if queue is full** check box, and set
**Entity arrival source** to
`Multicast`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MulticastTag` |
| **Type**: character vector |
| **Values**: `'A'` | character vector |
| **Default**: `'A'` |

### **Priority source** — Specify which attribute of the entity determines its priority character vector | `entitySys.priority`

Specify the priority source either as a custom entity attribute that you
created, or the `entitySys.priority` attribute,
specifically.

For example, assume that you added two new attributes named
`height` and `width` for an entity in
the Entity Type tab of a Entity Generator block. These
attributes appear as options, in the form of character vectors, for the
**Priority source** parameter. The value of the
parameters determine the entity priority.

**Note**

If you do not replace the default text prompt, PriorityAttribute, with
a priority source, then the model generates an error during
compilation.

#### Dependencies

This parameter is visible when you clear the **Overwrite the
oldest element if queue is full** check box, and set
**Queue type** to
`Priority`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PrioritySource` |
| **Type**: character vector |
| **Values**: `'entity'` | `'entitySys.priority'` | character vector |

### **Sorting direction** — Choose the direction of sorting based on priority `Ascending` (default) | `Descending`

Choose the direction of sorting based on priority.

- `Ascending` — Elements with smaller
  priority values appear in front of the queue.
- `Descending` — Elements with greater
  priority values appear in front of the queue.

#### Dependencies

This parameter is visible when you clear the **Overwrite the
oldest element if queue is full** check box, and set
**Queue type** to
`Priority`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SortingDirection` |
| **Type**: character vector |
| **Values**: `'Ascending'` | `'Descending'` |
| **Default**: `'Ascending'` |

### **Entity arrival source** — Choose the source of arrival for the entities `Input port` (default) | `Multicast`

Choose the source of arrival for the entities.

- `Input port` — Input port is source of
  messages or entities.
- `Multicast` — Entity
  Multicast block is source of entities. The Entity
  Multicast block requires SimEvents license.

#### Dependencies

This parameter is visible when you clear the **Overwrite the
oldest element if queue is full** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntityArrivalSource` |
| **Type**: character vector |
| **Values**: `'Input port'` | `'Multicast'` |
| **Default**: `'Input port'` |

### **Event action** — Specify the behavior of the entity in certain events `Entry` (default) | `Exit` | `Blocked`

Specify the behavior of the entity in certain events. Define the behavior
in the **Event action** parameter. The
**Entry** and the **Exit** actions are
called just after the entity entry and just before entity exit. The
**Blocked** action is called after an entity is
blocked. For more information, see Events and Event Actions (SimEvents).

**Note**

If an event action changes an entity, related block behavior such
as resorting a priority queue, and rescheduling of any events, will
occur after the event action has fully finished and returned.

**Note**

Event actions do not support `fixed point` data
type.

#### Dependencies

Event actions are visible when you clear the **Overwrite the
oldest element if queue is full** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntryAction, ExitAction, BlockedAction` |
| **Type**: character vector |
| **Values**: MATLAB code |
| **Default**: `''` |

### **Number of entities departed, d** — Outputs the number of entities that have departed the block `off` (default) | `on`

Number of entities that have departed the block.

#### Dependencies

**Number of entities departed, d** is visible when
you clear the **Overwrite the oldest element if queue is
full** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesDeparted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities in block, n** — Outputs the number of entities present in the block, that are yet to depart `off` (default) | `on`

Number of entities present in the block, but which are yet to
depart.

#### Dependencies

**Number of entities in block, n** is visible when
you clear the **Overwrite the oldest element if queue is
full** check box.

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
Entity Queue block entry and exit of an entity. For more
information, see Interpret SimEvents Models Using Statistical Analysis (SimEvents).

#### Dependencies

**Average wait, w** is visible when you clear the
**Overwrite the oldest element if queue is full**
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageWait` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Average queue length, l** — Outputs the average length of the entity queue `off` (default) | `on`

Accumulated time-weighted average queue size. The block computes this
value by:

1. Multiplying the size of the queue by its duration to calculate
   time-weighted queue size
2. Summing up all time-weighted queue sizes and averaging them
   over total time

For more information, see Interpret SimEvents Models Using Statistical Analysis (SimEvents).

#### Dependencies

**Average queue length, l** is visible when you clear
the **Overwrite the oldest element if queue is full**
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageQueueLength` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities extracted, ex** — Number of entities extracted from this block `off` (default) | `on`

Outputs the number of extracted entities which are pulled out from this
block by the Entity Find block. The Entity
Find block requires a SimEvents license. If the extracted entity is the first entity in the
queue, the next entity is set as the pending entity to leave the block. If
an entity attribute defines the priority in a priority queue and it is
modified by the Entity Find block, the queue is sorted again.
When an entity is extracted, **Number of entities departed,
d**, **Number of entities in block, n**,
**Average wait, w**, and **Average queue
length, l** statistics are updated accordingly. For more
information about finding and extracting entities, see Find and Extract Entities in SimEvents Models (SimEvents).

#### Dependencies

**Number of entities extracted, ex** is visible when
you clear the **Overwrite the oldest element if queue is
full** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumEntitiesExtracted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Libraries

Simulink / Messages & Events SimEvents

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Code generation is not supported for event actions and statistics.

When you generate code for a model that contains a message queue and has
multitasking enabled, enable concurrent tasking behavior if that model will be
deployed to a multitasking environment. Otherwise, the generated code has the
potential for data corruption. You enable concurrent tasking behavior by selecting
Allow tasks to execute concurrently on target.

## Version History

**Introduced in R2016a**

## Description

Enqueue messages and entities

This block stores entities or messages in a queue, based on their order of arrival or
priority. Each element at the head of the queue departs when the downstream block is
ready to accept it.

You can specify the capacity of the queue, and the policy when the queue is full. The
block supports three different message or queue sorting policies, first-in-first out
(FIFO), last-in-first out (LIFO), and priority. The priority queue can be used only when
the **Overwrite the oldest element if queue is full** check box is
cleared.
