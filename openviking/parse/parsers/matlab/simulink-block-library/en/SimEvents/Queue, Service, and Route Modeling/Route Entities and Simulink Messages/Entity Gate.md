---
type: simulink-block
title: 'Entity Gate'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Queue, Service, and Route Modeling / Route Entities and Simulink Messages'
documentation_page: 'entitygate'
documentation_source_path: 'ref/entitygate.html'
language: en
---

# Entity Gate

## Ports

### Input

### **Port\_1** — Input entity scalar | vector | matrix

Input entity that carries scalar, bus, or vector data to enter the
gate.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

### **control** — Incoming control entity scalar

Input control port to accept the entity that determines the state of
the gate.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Exiting entity scalar

Output entity port for entities leaving the gate.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

## Parameters

### **Operating mode** — Select the mode of operation `Enable gate` (default) | `Release gate` | `Selection gate`

Select the mode of operation of this gate. With the **Operating
mode** parameter set to:

- `Enable gate`, this block represents
  a gate that opens whenever the control port receives an
  anonymous entity with a positive value, and closes whenever it
  has zero or a negative value. By definition, an open gate
  permits entity arrivals as long as the entities are able to
  immediately advance to the next block, while a closed gate
  forbids entity arrivals. The anonymous entity that is received
  at the control port has a numerical value of type double. Since
  the gate receives an anonymous entity with a positive value and
  opens, an enabled gate remains open until it receives an entity
  with zero or a negative value and closes.
- `Release gate`, this block permits
  the arrival of one pending entity for each anonymous entity or
  message that arrives on the control port. At all other times,
  the entity input port of the block is unavailable. By
  definition, the opening of the gate permits one pending entity
  to arrive if the entity is able to immediately advance to the
  next block.
- `Selection gate`, this block permits
  the arrival of pending entities whenever the anonymous entity
  value from the control port matches the attributes of the
  pending entities. Otherwise it prevents the arrival of pending
  entities.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OperatingMode` |
| **Type**: character vector |
| **Values**: `'Enable gate'` | `'Release gate'` `'Selection gate'` |
| **Default**: `'Enable gate'` |

### **Matching attribute** — Specify name of the attribute that matches the value from the control port `Attribute1` (default) | character vector

Name of the attribute to match the value from the control port.

#### Dependencies

This parameter is visible when you set **Operating
mode** to `Selection Gate`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MatchingAttributeName` |
| **Type**: character vector |
| **Values**: `'Attribute1'` | character vector |
| **Default**: `'Attribute1'` |

### **Initial value from the control port** — Specify initial value from the control port to match the matching attribute `NaN` (default) | scalar

Specify the initial value to match the matching attribute which opens the
gate.

#### Dependencies

This parameter is visible when you set **Operating
mode** to `Selection Gate`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialValueOfMatchingAttribute` |
| **Type**: character vector |
| **Values**: `'NaN'` | scalar |
| **Default**: `'NaN'` |

### **Open gate at simulation start** — Opening the gate at the start `off` (default) | `on`

Select this option to open the gate at the start of the
simulation.

Unselected check boxoff
:   Gate is closed at the start of the simulation.

Selected check boxon
:   Gate is open at the start of the simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OpenGateAtSimulationStar` |
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

Gate entities

The Entity Gate block controls when pending entities can advance in the
model.

The **Operating mode** parameter specifies how the pending entities
advance through the gate.

- `Enable gate` — opens and allows entities to advance
  whenever the control port receives an anonymous entity with a positive value,
  and closes whenever it has zero or a negative value. For more information, see
  Use Queue Event Actions to Model a Storage Tank.
- `Release gate` — allows one pending entity to advance
  for each anonymous entity or message that arrives on the control port. At all
  other times, the entity input port of the block is unavailable.
- `Selection gate` — allows entities to advance whenever
  the anonymous entity value from the control port matches the attributes of the
  pending entities.

Use the Entity Gate block to control the flow of entities on the entity
path. Use the Entity Output Switch block to select an
output port for the departure of an entity among multiple entity output ports. For more
information, see Route Vehicles Using an Entity Output Switch Block.
