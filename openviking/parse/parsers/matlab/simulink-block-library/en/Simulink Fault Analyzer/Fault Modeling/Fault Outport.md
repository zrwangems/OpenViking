---
type: simulink-block
title: 'Fault Outport'
family: 'fault-analyzer'
product_id: 'fault-analyzer'
product_name: 'Simulink Fault Analyzer'
documentation_release: R2025b
official_category: 'Fault Modeling'
documentation_page: 'faultoutport'
documentation_source_path: 'ref/faultoutport.html'
language: en
---

# Fault Outport

## Ports

### Input

### **Port\_1** — Output fault behavior scalar | vector | matrix

Output from behavior to model, specified as a scalar, vector, or matrix. Connect
to this block to represent the introduced behavior in another model.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumeration` | `bus`

## Parameters

Not documented in R2025b.

## Libraries

Simulink Fault Analyzer / Fault Port Blocks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Output signals from fault behaviors

Fault Outport blocks link signals from a model of a fault behavior to an
external model. You can use these blocks to output signal data to Simulink® and System Composer™ models.

Use these blocks only in Fault
Subsystem blocks. Each Fault Subsystem block can contain only one
Fault Outport block.
