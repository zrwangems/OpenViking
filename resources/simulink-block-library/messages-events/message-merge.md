---
type: simulink-block
title: 'Message Merge'
family: messages-events
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'messagemerge'
---

# Message Merge

Combine message paths

## Libraries

Simulink / Messages & Events

## Description

The Message Merge block graphically combines multiple message lines into a
single message line. Merging message lines does not change the messages themselves. You can
specify the number of message lines to merge.

Use this block when you want to merge multiple incoming messages and output to a single
destination such as a queue or a message storage block.

**Note**

Message Merge block is not supported for code generation in AUTOSAR
mode.

## Ports

### Input

### **Port\_1** — Input message line to merge scalar | vector | matrix

Input message port for messages entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — Input message line to merge scalar | vector | matrix

Input message port for messages entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port** — Output message line scalar | vector | matrix

Output message port for messages exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## Parameters

### **Number of input ports** — Specify the number message lines to combine `2` (default) | scalar

Determines the number of message input ports to be combined.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberInputPorts` |
| **Type**: character vector |
| **Values**: `'2'` | scalar |
| **Default**: `'2'` |

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

## Version History

**Introduced in R2021a**
