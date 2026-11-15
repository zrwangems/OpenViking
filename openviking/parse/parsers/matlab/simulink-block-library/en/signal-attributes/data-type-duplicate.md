---
type: simulink-block
title: 'Data Type Duplicate'
family: signal-attributes
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'datatypeduplicate'
language: en
---

# Data Type Duplicate

## Ports

### Input

### **Port\_1** — First input signal scalar | vector | matrix | N-D array

First input signal, specified as a scalar, vector, matrix, or N-D array. If all signals
do not have the same data type, the block returns an error
message.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `string` | `Boolean` | `fixed point` | `enumerated`

### **Port\_N** — Nth input signal scalar | vector | matrix | N-D array

Nth input signal, specified as a scalar, vector, matrix, or N-D array. If all signals do
not have the same data type, the block returns an error message.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `string` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### **Number of input ports** — Number of block inputs `2` (default) | real-valued positive integer

Specify the number of inputs to this block as a real-valued positive
integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumInputPorts` |
| **Type:** character vector |
| **Values:** real-valued positive integer |
| **Default:** `'2'` |

## Libraries

Simulink / Signal Attributes HDL Coder / Signal Attributes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block can be used to force inputs to have same data
type in subsystems that generate code, but is not included in the hardware
implementation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Force all inputs to same data type

The Data Type Duplicate block forces all inputs to have the same data type.
Other attributes of input signals, such as dimension, complexity, and sample time, are
independent.

You can use the Data Type Duplicate block to check for consistency of data
types among blocks. If all signals do not have the same data type, the block returns an
error message.

The Data Type Duplicate block is typically used such that one signal to the
block controls the data type for all other blocks. The other blocks are set to inherit
their data types via backpropagation.

The block can also be useful in a user created library. These library blocks can be placed
in any model, and the data type for all library blocks are configured according to the
usage in the model. To create a library block with more complex data type rules than
duplication, use the Data Type Propagation block.
