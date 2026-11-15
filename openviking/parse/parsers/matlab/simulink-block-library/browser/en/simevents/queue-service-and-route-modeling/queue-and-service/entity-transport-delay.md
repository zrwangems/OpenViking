---
type: simulink-block
title: 'Entity Transport Delay'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Queue, Service, and Route Modeling / Queue and Service'
documentation_page: 'entitytransportdelay'
documentation_source_path: 'ref/entitytransportdelay.html'
language: en
---

# Entity Transport Delay

## Ports

### Input

### **Port\_1** — Input entity SimEvents entity

SimEvents entity or message. For more information on entities in
SimEvents, see Entities in a SimEvents Model.

This port does not have direct feedthrough.

### **ti** — Instantaneous delay scalar | vector | matrix

Instantaneous delay in the transport of the SimEvents entity. *ti* is
the reciprocal of the speed of the entity. For more information on the
calculation of instantaneous delay, see Variable Transport Delay.

This port has direct feedthrough.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `bus`
### Output

### **Port\_1** — Delayed entity SimEvents entity

SimEvents entity with the instantaneous delay
*ti* applied to
it.

### **n** — Number of delayed entities real scalar

Secondary output signal of the block, which displays the number of
entities processed in a time step.

#### Dependencies

To enable this port, enable the **Output number of entities in block,
n** parameter

**Data Types:** `double`

## Parameters

### **Capacity** — Specify the capacity of the block inf (default) | scalar

Specify capacity to accept entities to be delayed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Capacity` |
| **Type**: character vector |
| **Values**: `'inf'` | real scalar |
| **Default**: `'inf'` |

### **Output number of entities in block, n** — Outputs the number of delayed entities present in the block `off` (default) | `on`

Number of entities present in the block that are being delayed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowNumberEntitiesInBlock` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Libraries

Simulink / Continuous SimEvents

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Introduce a delay in propagation of a SimEvents message

The Entity Transport Delay block delays an entity for a period of time, named *transport delay*. The first input is the entity that is
transported from point A to point B on a constant-length moving surface whose speed
changes over time. The value from the second input is the *instantaneous delay*. The speed of the surface is the reciprocal of
instantaneous delay. The product of instantaneous delay and the speed is 1.

The block calculates the implemented transport delay by the distance-speed-time
relationship, where the surface length (distance) is equal to the integral of the
variable surface speed over the duration of the transport delay (time). For more
information about this calculation, see Variable Transport Delay.

The Entity Transport Delay block connects SimEvents® to Simulink® using the input from a Simulink signal and computing the transport delay as a continuous process, and
applying this delay to an entity in a discrete-event process. For an example that uses
the Entity Transport Delay block, see Modeling Cyber-Physical Systems.
