---
type: simulink-block
title: 'Fault Data Inport'
family: 'fault-analyzer'
product_id: 'fault-analyzer'
product_name: 'Simulink Fault Analyzer'
documentation_release: R2025b
official_category: 'Fault Port Blocks'
documentation_page: 'faultdatainport'
documentation_source_path: 'ref/faultdatainport.html'
language: en
---

# Fault Data Inport

## Ports
```yaml
ports:
- name: Port_1
  summary: Data from model signal scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | string | fixed
    point | enumeration | bus
```

### Output

### **Port\_1** — Data from model signal scalar | vector | matrix

The Fault Data Inport block outputs real-valued scalar, vector, or
matrix data. Map this block to a block or component output signal in the model. The
model must contain the fault assigned to the behavior. The signal that you map to the
block determines the output data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumeration` | `bus`
## Parameters
```yaml
parameters: []
```

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

**Introduced in R2024b**

## Description

Import Simulink model data into fault behavior

Fault Data Inport blocks retrieve signal data from a model and feed the
data to behaviors that you assign to the faults. You can use these blocks to capture signal
data from Simulink® and System Composer™ models.

Use these blocks only in the top-level of a Fault
Subsystem block.

For more information, see Access Data from Model Outputs in Fault Behaviors.
