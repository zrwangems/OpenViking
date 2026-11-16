---
type: simulink-block
title: 'Entity Input Switch'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entityinputswitch'
documentation_source_path: 'ref/entityinputswitch.html'
language: en
---

# Entity Input Switch

## Ports

### Input

### **Port\_1** — Input entity scalar | vector | matrix

Input entity port for entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — Input entity scalar | vector | matrix

Input entity port for entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **control** — Incoming control entity scalar

Input control port for the incoming control entity that determines the
input port for the entities arriving at the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **Port\_1** — Output entity scalar | vector | matrix

Output entity port for entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## Parameters

### **Number of input ports** — Specify the number of input ports `2` (default) | scalar

Determines how many entity input ports the block has.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberInputPorts` |
| **Type**: character vector |
| **Values**: `'2'` | scalar |
| **Default**: `'2'` |

### **Active port selection** — Specify the active input port `All` (default) | `Switch`

Specify the active input port to allow arrival of entities at all ports or
one port at a time. Select `All` to combine entity
paths and allow arrival of entities at all ports. Select
`Switch` to allow arrival of an entity at only
one port at a time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ActivePortSelection` |
| **Type**: character vector |
| **Values**: `'All'` | `'Switch'` |
| **Default**: `'All'` |

### **Switching criterion** — Specify input port switch criterion `Round robin` (default) | `From control port` | `Equiprobable`

Select the criterion for switching between input ports.

- Select `Round robin` to select ports in a
  round robin fashion. Set the initial port in the **Initial
  port selection**.
- Select `From control port` to let the
  control port determine the selected port. A control port will appear
  to input an anonymous entity carrying data with a value greater than
  `0`, and smaller than or equal to the number of
  input ports to determine the active port.
- Select `Equiprobable` to let the block
  randomly select any port with equal probability. Set the
  **Seed** to generate a random number and to
  determine the active input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SwitchingCriterion` |
| **Type**: character vector |
| **Values**: `'Round robin'` | `'From control port'` | `'Equiprobable'` |
| **Default**: `'Round robin'` |

### **Initial port selection** — Specify the initial input port for entity entry `1` (default) | scalar

Specify initially which port allows arrival of an entity.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialPortSelection` |
| **Type**: character vector |
| **Values**: `'1'` | scalar |
| **Default**: `'1'` |

### **Seed** — Specify the seed for the random number generator to determine the input port `23453` (default) | scalar

Specify the seed for the random number generator to determine the input
port.

#### Dependencies

This parameter is visible when **Switching
criterion** is set to
`Equiprobable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Seed` |
| **Type**: character vector |
| **Values**: `'23453'` | scalar |
| **Default**: `'23453'` |

## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Switch input entities

A typical scenario in which you might use an input switch is when multiple sources of
entities feed into a single queue, where the sequencing follows specific rules. For
example, users of terminals in a time-shared computer submit jobs to a queue that feeds
into the central processing unit, where an algorithm regulates access to the queue so as
to prevent unfair domination by any one user.

**Note**

If you want to merge message or entity paths and generate code for your component
interface, use the Simulink®
Message
Merge block. Message Merge block's behavior is the same
as the Entity Output Switch block with **Active port
selection** parameter set to `All`.

For an example, see Generate Entities When Events Occur.

### Combine Entity Paths

You can merge multiple paths into a single path using the Entity Input
Switch block with the **Active port selection**
parameter set to `All`. Merging entity paths does not
change the entities themselves, just as merging lanes on a road does not change the
vehicles that travel on it. In particular, the Entity Input Switch
block does not create aggregates or batches.

Here are some scenarios in which you might combine entity paths:

- Attaching different data — Multiple entity generator blocks create
  entities having different values for a particular attribute. The entities
  then follow a merged path but might be treated differently later based on
  their individual attribute values.
- Merging queues — Multiple queues merge into a single queue.
- Connecting a feedback path — A feedback path enters the same queue
  as an ordinary path.

### Sequence Simultaneous Pending Arrivals

The Entity Input Switch block does not experience any collisions,
even if multiple entities attempt to arrive at the same time. The categories of
behavior are as follows:

- If the entity output port is not blocked when the entities attempt to
  arrive, then the sequence of arrivals depends on the sequence of departure
  events from blocks that precede the Entity Input Switch
  block.

  Even if the departure time is the same for multiple entities, the sequence
  might affect the system's behavior. For example, if the entities advance to
  a queue, the departure sequence determines their positions in the
  queue.
- If pending entities are waiting to advance to the Entity Input
  Switch block when its entity output port changes from blocked to
  unblocked, then the entity input ports are notified of the change
  sequentially. The change from blocked to unblocked means that an entity can
  advance to the Entity Input Switch block.

  If at least two entities are waiting to advance to the Entity Input
  Switch block via distinct entity input ports, then the
  notification sequence is important because the first port to be notified of
  the change is the first to advance an entity to the Entity Input
  Switch block.

### Select Arrival Path

The Entity Input Switch block allows arrival of entities at its
ports. The selected entity input port can change during the simulation.

You can also select the criterion for switching between input ports.

- Select `Round robin` to select ports in a round
  robin fashion.
- Select `From control port` to let the control
  port determine the selected port.
- Select `Equiprobable` to let the block randomly
  select any port with equal probability.

### Limitations

The total number of entity input ports must be less than 128. To model more than
128 ports, use multiple Entity Input Switch blocks either in parallel
or in series.
