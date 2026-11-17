---
type: simulink-block
title: 'Multicast Receive Queue'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'multicastreceivequeue'
documentation_source_path: 'ref/multicastreceivequeue.html'
language: en
---

# Multicast Receive Queue

## Ports
```yaml
ports:
- name: receive
  summary: Receive broadcasted entity scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | string | fixed point
- name: Port_1
  summary: Output entity scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | string | fixed point
```

### Input

### **receive** — Receive broadcasted entity scalar | vector | matrix

Input for received entities.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`
### Output

### **Port\_1** — Output entity scalar | vector | matrix

Output entity at the head of the queue to depart when a downstream
block is ready to accept it.

**Note**

Event actions are not supported with string entity data
type

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Receive multicast entities

The Multicast Receive Queue block is identical to an Entity
Queue block with the **Entity arrival source** parameter
set to `Multicast`. For information about parameter
descriptions, see the documentation for the Entity Queue
block.

You specify a **Multicast tag** for receiving entities. Then the
block receives entities with a matching **Multicast tag** broadcast by
the Entity Multicast block. See Overview of Queues and Servers in Discrete-Event Simulation, for more information about using multicast
mode to broadcast entities.
