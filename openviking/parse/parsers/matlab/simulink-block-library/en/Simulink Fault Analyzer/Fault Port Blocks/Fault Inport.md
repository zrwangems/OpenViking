---
type: simulink-block
title: 'Fault Inport'
family: 'fault-analyzer'
product_id: 'fault-analyzer'
product_name: 'Simulink Fault Analyzer'
documentation_release: R2025b
official_category: 'Fault Port Blocks'
documentation_page: 'faultinport'
documentation_source_path: 'ref/faultinport.html'
language: en
---

# Fault Inport

## Ports

### Output

### **Port\_1** — Input from assigned fault signal scalar | vector | matrix

Input from assigned fault signal to behavior, specified as a scalar, vector, or
matrix. This port represents the intercepted signal in your model.

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

Capture inlet signal for fault behaviors

Fault Inport blocks link signals from an external model to the model of a
fault behavior. The block retrieves data directly from the signal that contains the associated
fault. You can use these blocks to capture signal data from Simulink® and System Composer™ models.

Use these blocks only in Fault
Subsystem blocks. Each Fault Subsystem block can contain only one
Fault Inport block.
