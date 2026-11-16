---
type: simulink-block
title: 'Entity Multicast'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entitymulticast'
documentation_source_path: 'ref/entitymulticast.html'
language: en
---

# Entity Multicast

## Ports

### Input

### **Port\_1** — Input entity scalar | vector | matrix

Input entity port for entities entering the block.

**Note**

Event actions are not supported with string entity data
type

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`
### Output

### **send** — Broadcast entities scalar | vector | matrix

Output broadcasted entities.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

## Parameters

### **Multicast tag** — Specify the tag with which to broadcast the entities `A` (default) | character vector

Specify the tag with which to broadcast the entities. For example if the
default tag `A` is used, each Entity Queue block with
**Entity arrival source** specified as
`Multicast` and the **Multicast
tag** is set as `A` receives a copy.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MulticastTag` |
| **Type**: character vector |
| **Values**: `'A'` | character vector |
| **Default**: `'A'` |

## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Send multicast entities

The Entity Multicast block broadcasts entities. An entity that arrives
at the block is cloned into copies and sent with a **Multicast tag**.
Each Entity Queue block with
**Entity arrival source** specified as
`Multicast` with the same **Multicast
tag** receives copies. For more information, see Overview of Queues and Servers in Discrete-Event Simulation.
