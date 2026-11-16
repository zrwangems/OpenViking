---
type: simulink-block
title: 'Composite Entity Splitter'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'compositeentitysplitter'
documentation_source_path: 'ref/compositeentitysplitter.html'
language: en
---

# Composite Entity Splitter

## Ports

### Input

### **port\_1** — Input composite entity scalar | vector | matrix

Input entity port for composite entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **port\_1** — Output entity scalar | vector | matrix

Output port for entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **port\_2** — Output entity scalar | vector | matrix

Output port for entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `enumerated` | `bus` | `fixed point`

## Parameters

### **Number of output ports** — Specify the number of output ports `2` (default) | scalar

Specify the number of output ports to output entities.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberOutputPorts` |
| **Type**: character vector |
| **Values**: `'2'` | scalar |
| **Default**: `'2'` |

## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Split composite entities

The Composite Entity Splitter block splits a composite entity into its
individual entities and outputs them through each unblocked entity output port. A
composite entity can be the output of the Composite Entity Creator block, a structured
type or a bus type entity from Entity Generator or Message
Send blocks.
