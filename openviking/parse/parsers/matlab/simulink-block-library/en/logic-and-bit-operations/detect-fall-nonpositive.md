---
type: simulink-block
title: 'Detect Fall Nonpositive'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'detectfallnonpositive'
language: en
---

# Detect Fall Nonpositive

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal that detects a falling edge, specified as a scalar,
vector, or matrix.

- The output is true (equal to `1`) when
  the input signal is less than or equal to zero, and its
  previous value was greater than zero.
- The output is false (equal to `0`) when
  the input signal is greater than zero, or if it is
  nonpositive, its previous value was also nonpositive.

**Data Types:** `uint8` | `Boolean`

## Parameters

### **Initial condition** — Initial condition of Boolean expression `U/z <= 0` 0 (default) | scalar | vector | matrix

Set the initial condition of the Boolean expression `U/z <=
0`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vinit` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

### **Input processing** — Specify sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing:

- `Columns as channels (frame based)` — Treat
  each column of the input as a separate channel (frame-based processing).

  **Note**

  Frame-based processing requires a DSP System Toolbox™ license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).
- `Elements as channels (sample based)` — Treat
  each element of the input as a separate channel (sample-based
  processing).

Use **Input processing** to specify whether the block performs
sample- or frame-based processing. For more information about these two processing
modes, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputProcessing` |
| **Type**: character vector |
| **Values**: `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **Default**: `'Elements as channels (sample based)'` |

### **Output data type** — Output data type `boolean` (default) | `uint8`

Specify the output data type as `boolean` or
`uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'boolean' | 'uint8'` |
| **Default:** `'boolean'` |

## Libraries

Simulink / Logic and Bit Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or
`memset` functions (`string.h`) under
certain conditions.

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

Detect falling edge when signal value decreases to nonpositive value, and its previous value was strictly positive

The Detect Fall Nonpositive block determines if the input is less than
or equal to zero, and its previous value was greater than zero.

- The output is true (equal to `1`) when the input signal is
  less than or equal to zero, and its previous value was greater than zero.
- The output is false (equal to `0`) when the input signal is
  greater than zero, or if it is nonpositive, its previous value was also
  nonpositive.

This block supports only discrete sample times.
