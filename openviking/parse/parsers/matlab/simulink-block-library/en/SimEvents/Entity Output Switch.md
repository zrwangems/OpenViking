---
type: simulink-block
title: 'Entity Output Switch'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entityoutputswitch'
documentation_source_path: 'ref/entityoutputswitch.html'
language: en
---

# Entity Output Switch

## Ports
```yaml
ports:
- name: Port_1
  summary: Input entity scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: control
  summary: Incoming control entity scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Output entity scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_2
  summary: Output entity scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
```

### Input

### **Port\_1** — Input entity scalar | vector | matrix

Input entity port for entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **control** — Incoming control entity scalar

Input control port for the incoming control entity that determines the output port
for the entities departing from the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output entity scalar | vector | matrix

Output entity port for entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — Output entity scalar | vector | matrix

Output entity port for entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
## Parameters
```yaml
parameters:
- name: Number of output ports
  summary: Specify the number of output ports 2 (default) | scalar
  group: ''
  block_parameter: NumberOutputPorts
  type: character vector
  values: '''2'' | scalar'
  default: '''2'''
- name: Switching criterion
  summary: Choose the switching criterion First port that is not blocked (default) | Round robin | From control port | From
    attribute | Equiprobable
  group: ''
  block_parameter: SwitchingCriterion
  type: character vector
  values: '''First port that is not blocked'' | ''Round robin'' | ''From control port'' | ''From attribute'' | ''Equiprobable'''
  default: '''First port that is not blocked'''
- name: Initial port selection
  summary: Specify the output port at the start of the simulation 1 (default) | scalar
  group: ''
  block_parameter: InitialPortSelection
  type: character vector
  values: '''1'' | scalar'
  default: '''1'''
- name: Switch Attribute name
  summary: Specify the attribute that determines the output port Attribute1 (default) | character vector
  group: ''
  block_parameter: SwitchAttributeName
  type: character vector
  values: '''Attribute1'' | character vector'
  default: '''Attribute1'''
- name: Seed
  summary: Specify the seed 34567 (default) | scalar
  group: ''
  block_parameter: Seed
  type: character vector
  values: '''34567'' | scalar'
  default: '''34567'''
```

### **Number of output ports** — Specify the number of output ports 2 (default) | scalar

Number of output ports for entity departure.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberOutputPorts` |
| **Type**: character vector |
| **Values**: `'2'` | scalar |
| **Default**: `'2'` |

### **Switching criterion** — Choose the switching criterion `First port that is not blocked` (default) | `Round robin` | `From control port` | `From attribute` | `Equiprobable`

Choose the criterion for switching between output ports.

- To output the entity to the first unblocked port, select `First port
  that is not blocked`.

  Assume an example where entities arriving at the Entity Output
  Switch block depart through the first entity output port that is not
  blocked, as long as at least one entity output port is not blocked. An everyday
  example of this approach is a single queue of people waiting for service by one of
  several bank tellers, cashiers, call center representatives, etc. Each person in the
  queue wants to advance as soon as possible to the first available service provider
  without preferring one over another.
- To output entities in a round robin fashion among the output ports, select
  `Round robin`.
- Select `From control port` to let the control port
  determine the selected port for entity departure. A control port will appear to
  input an anonymous entity carrying data with a value greater than
  `0` and smaller than or equal to the number of output ports to
  determine the active port.
- To specify an attribute that determines the output port, select
  `From attribute`. The attribute value is greater than
  `0` and smaller than or equal to the number of output ports to
  determine the active port.

  Consider the situation in which parcels are sorted among several delivery
  vehicles based on the locations of the specified recipients. If each parcel is an
  entity, then you can attach data to each entity to indicate the location of its
  recipient.
- To randomly select an output port for entity departure, select
  `Equiprobable`. Set the **Seed** to
  generate a random number and to determine the active output port.

**Note**

The block rounds a double precision value to the nearest integer less than or
equal to its value as port selection. For instance, the value `0.3`
is rounded of to `0` which is not a valid value for port
selection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SwitchingCriterion` |
| **Type**: character vector |
| **Values**: `'First port that is not blocked'` | `'Round robin'` | `'From control port'` | `'From attribute'` | `'Equiprobable'` |
| **Default**: `'First port that is not blocked'` |

### **Initial port selection** — Specify the output port at the start of the simulation 1 (default) | scalar

Select the initial port for the entity departure.

#### Dependencies

This parameter is visible when **Switching criterion** is set to
`Round robin` or `From control
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialPortSelection` |
| **Type**: character vector |
| **Values**: `'1'` | scalar |
| **Default**: `'1'` |

### **Switch Attribute name** — Specify the attribute that determines the output port `Attribute1` (default) | character vector

Specify the attribute name used to switch the output port.

#### Dependencies

This parameter is visible when **Switching criterion** is set to
`From attribute`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SwitchAttributeName` |
| **Type**: character vector |
| **Values**: `'Attribute1'` | character vector |
| **Default**: `'Attribute1'` |

### **Seed** — Specify the seed `34567` (default) | scalar

Specify the seed for the random number generator to determine the output
port.

#### Dependencies

This parameter is visible when **Switching criterion** is set to
`Equiprobable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Seed` |
| **Type**: character vector |
| **Values**: `'34567'` | scalar |
| **Default**: `'34567'` |
## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Output entities

The Entity Output Switch block allows you to select an output port for the
departure of an entity among multiple entity output ports. The selected port can change during
the simulation and you can choose the criterion for switching between output ports.

Here are some scenarios in which you might use an output switch:

- Entities advance to one of several queues based on efficiency or fairness concerns.
  For example, airplanes advance to one of several runways depending on queue length, or
  customers advance to the first available cashier out of several cashiers.

  Comparing different approaches to efficiency or fairness, by testing different rules
  to determine the selected output port of the output switch, might be part of your goal in
  simulating the system. For an example, see Route Vehicles Using an Entity Output Switch Block.
- Entities advance to a specific destination based on their characteristics. For
  example, parcels advance to one of several delivery vehicles based on the locations of the
  specified recipients.
- Entities use an alternate route in case the preferred route is blocked. For example, a
  communications network drops a packet if the route to the transmitter is blocked and the
  simulation gathers statistics about dropped packets.

Alternatively, you can use the Entity Gate block to control the flow of
entities on a specific entity path. For more information, see Using Entity Priority to Sequence Departures.

### Limitations

The total number of entity output ports must be less than 128. To model more than 128
ports, use multiple Entity Output Switch blocks either in parallel or in
series.
