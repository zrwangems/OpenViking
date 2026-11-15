---
type: simulink-block
title: 'Bit Clear'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitclear'
language: en
---

# Bit Clear

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

The input signal is the specified bit of the stored integer.

**Data Types:** `single` | `double` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

The output consists of the specified bit set to zero.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Index of bit** — Index of bit 0 (default) | scalar | vector

Index of bit where bit 0 is the least significant bit.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `iBit` |
| **Type**: character vector |
| **Values**: scalar | vector |
| **Default**: `'0'` |

## Libraries

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `fixed point` | `integer` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Bit operations are not recommended for use with Boolean signals. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Set specified bit of stored integer to zero

The Bit Clear block sets the specified bit, given by its index, of the
stored integer to zero. Scaling is ignored.

You can specify the bit to be set to zero with the **Index of
bit** parameter, where bit zero is the least significant bit.
