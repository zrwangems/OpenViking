---
type: simulink-block
title: 'Composite Entity Creator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Resource Allocation Modeling'
documentation_page: 'compositeentitycreator'
documentation_source_path: 'ref/compositeentitycreator.html'
language: en
---

# Composite Entity Creator

## Ports

### Input

### **port\_1** — Input entity scalar | vector | matrix

Input entity port for entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **port\_2** — Input entity scalar | vector | matrix

Input entity port for entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **port\_1** — Output composite entity scalar | vector | matrix

Output entity port for composite entities exiting the clock.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## Parameters

### **Number of input ports** — Specify the number of input ports `2` (default) | scalar

Specify the number of input ports to create the composite entity.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberInputPorts` |
| **Type**: character vector |
| **Values**: `'2'` | scalar |
| **Default**: `'2'` |

### **Entity type name** — Specify the type name of the composite entity `Combined` (default) | character vector

Specify the type name of the composite entity that is created after
combining incoming entities.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntityTypeName` |
| **Type**: character vector |
| **Values**: `'Combined'` | character vector |
| **Default**: `'Combined'` |

### **Bus object** — Specify the output `off` (default) | `on`

Specify whether to output the composite entity as a bus object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BusObject` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Define input entity names** — Specify the names of the input entities used to generate the composite entity `{E1, E2}` (default) | character vector

Names of the entities in the composite entity.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputEntityName` |
| **Type**: character vector |
| **Values**: `'E1|E2'` | character vector |
| **Default**: `'E1|E2'` |

## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Create composite entities

The Composite Entity Creator block creates a composite entity for each
set of entities arriving simultaneously at all input ports. The newly created entity can
include information about the structure, attributes, and timers of the arriving
entities.

You can combine entities from different paths using this block. The combined entity
represents different parts within a larger item, such as the header, payload, and
trailer that are parts of a data packet. Alternatively, you can model resource
allocation by combining an entity that represents a resource with an entity that
represents a part or other item.

The Composite Entity Creator block detects when all necessary component
entities are present and when the composite entity that results from the combining
operation will be able to advance to the next block. You can also configure the
Composite Entity Creator block to make the combining operation
reversible via the Composite Entity Splitter block.
