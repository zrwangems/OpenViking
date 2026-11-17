---
type: simulink-block
title: 'Byte Unpack'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'byteunpack'
documentation_source_path: 'ref/byteunpack.html'
language: en
---

# Byte Unpack

## Ports
```yaml
ports:
- name: Port_1
  summary: Signal to convert vector
  direction: input
  data_types: uint8
- name: Port_1
  summary: Converted signal data signal of type double (default) | array of signal data
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### Input

### **Port\_1** — Signal to convert vector

Input vector of `uint8`.

**Data Types:** `uint8`
### Output

### **Port\_1** — Converted signal data signal of type `double` (default) | array of signal data

Array of input signals of one or more data types.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## Parameters
```yaml
parameters:
- name: Output port dimensions (cell array)
  summary: Dimensions of block output signals {[1]} (default) | cell array of data dimension specifications
  group: ''
- name: Output port data types (cell array)
  summary: Data types of block output signals {'double'} (default) | cell array of Simulink data types
  group: ''
- name: Byte Alignment
  summary: Byte boundary for data type alignment 1 (default) | 2 | 4 | 8
  group: ''
```

### **Output port dimensions (cell array)** — Dimensions of block output signals {[1]} (default) | cell array of data dimension specifications

Specify the dimensions of the output signals that the block outputs in a cell
array. Each element in the array specifies the dimension that the MATLAB®
`size` function returns for the
corresponding signal. Specify dimensions that align with data converted by the
corresponding Byte Pack (Embedded Coder) block in the model.

For example, assume the corresponding Byte Pack block specifies these input
port data types:

```
 {'uint32','uint32','uint16','double','uint8','double','single'}
```

To specify scalar and matrix output, you might set the **Output port
dimensions (cell array)** parameter to:

```
 {1,1,[2,4],[4,4],[2,2],1,[3,3]}
```

To apply the same dimension across the output signals, you can specify one
dimension value.

### **Output port data types (cell array)** — Data types of block output signals {'double'} (default) | cell array of Simulink data types

Specify the Simulink data types of the individual input signals received by the
corresponding Byte Pack block in the model in a cell array.

For example, if the corresponding Byte Pack block specifies these input port
data types, specify the same cell array for this parameter.

```
 {'uint32','uint32','uint16','double','uint8','double','single'}
```

To apply the same data type to each output signal, you need to specify the data
type only once.

### **Byte Alignment** — Byte boundary for data type alignment 1 (default) | 2 | 4 | 8

Specify how to align the data types of output data to form the
`uint8` vector input in bytes. Specify the alignment value
that matches the value specified for the corresponding Byte Pack (Embedded Coder) block in the model.

For example, if the corresponding Byte Pack block sets the byte alignment to 2,
set this parameter to 2.
## Libraries

Motor Control Blockset / Signal Management C2000 Microcontroller Blockset / Target Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2024a**

## Description

Convert uint8 vector to input signals

The Byte Unpack block receives a `uint8` vector and converts the vector
to output signals of different Simulink® data types based on content of the input vector. You can use block parameters
to specify dimensions and data types of the output signals and the alignment of the data in
the individual vectors that the block outputs. Because the UDP protocol transmits data in
`uint8` format, you can use this block to reformat data that is
received as a UDP packet for use in a model by connecting the input of this block to the
output of a UDP Send (Embedded Coder) block.
