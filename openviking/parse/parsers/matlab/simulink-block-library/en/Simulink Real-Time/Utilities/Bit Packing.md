---
type: simulink-block
title: 'Bit Packing'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'bitpacking'
documentation_source_path: 'io_ref/bitpacking.html'
language: en
---

# Bit Packing

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Bit Patterns
  summary: Packed data bit pattern {[0:31]} (default)
  group: ''
  block_parameter: BitPatterns
- name: Output port (packed) data type
  summary: Packed data type uint32 (default) | double | single | int8 | uint8 | int16 | uint16 | int32 | boolean
  group: ''
  block_parameter: PackDataType
- name: Output port (packed) dimensions
  summary: Packed data dimensions [1] (default)
  group: ''
  block_parameter: PackDataSize
```

### **Bit Patterns** — Packed data bit pattern {[0:31]} (default)

Specify bit patterns. The data type entered in the control must be a MATLAB® cell array vector. The number of elements in the cell array define the
number of input ports shown by this block instance. The cell array elements must be of
type double array and define the position of each bit of the incoming value (data typed
input port) in the outgoing double value (data frame). From a data type perspective
(input ports), the block behaves like a Simulink® Sink block. The data types of the input ports are inherited from the
driving blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BitPatterns` |

### **Output port (packed) data type** — Packed data type `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

From the list, select an output port (packed) data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PackDataType` |

### **Output port (packed) dimensions** — Packed data dimensions [1] (default)

Specify the dimensions the output port (packed). Enter this value as a vector.
Specify the size of the port by using a format compatible with the MATLAB
`size` command.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PackDataSize` |
## Libraries

Simulink Real-Time / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006a**

## Description

Construct data frames

The Bit Packing block constructs data frames. Its output port is typically
connected to an input port of a Send block or Digital Output block. The block has one output
port. This port can be a vector of arbitrary size. It represents the data frame entity
constructed by the signals entering the block at its input ports. The number of input ports
depends on the setting in the block dialog box.
