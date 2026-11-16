---
type: simulink-block
title: 'Coulomb and Viscous Friction'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'coulombandviscousfriction'
documentation_source_path: '../simulink/slref/coulombandviscousfriction.html'
language: en
---

# Coulomb and Viscous Friction

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

The input signal to the model of Coulomb and viscous friction.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

The output signal calculated by applying the friction models to the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

To edit the parameters for the Coulomb and Viscous Friction block,
double-click the block icon.

### **Coulomb friction value** — Static friction offset `[1320]` (default) | real values

Specify the offset that applies to all input values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `offset` |
| **Type**: character vector |
| **Value**: real values |
| **Default**: `'[1 3 2 0]'` |

### **Coefficient of viscous friction** — Dynamic friction coefficient `1` (default) | real values

Specify the signal gain for nonzero input values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `gain` |
| **Type**: character vector |
| **Value**: real values |
| **Default**: `'1'` |

## Libraries

Simulink / Discontinuities HDL Coder / Discontinuities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

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

**Restrictions**

HDL code generation does not support complex input.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Model discontinuity at zero, with linear gain elsewhere

The Coulomb and Viscous Friction block models Coulomb (static) and viscous (dynamic)
friction. The block models a discontinuity at zero and a linear gain otherwise.

The block output matches the MATLAB® result for:

```
y = sign(x) .* (Gain .* abs(x) + Offset)
```

where `y` is the output, `x` is
the input, `Gain` is the signal gain for nonzero
input values, and `Offset` is the Coulomb friction.

The block accepts one input and generates one output. The input can be a scalar, vector, or matrix with real and complex elements.

- For a scalar input, `Gain` and `Offset` can
  have dimensions that differ from the input. The output is a scalar,
  vector, or matrix depending on the dimensions of `Gain` and `Offset`.
- For a vector or matrix input, `Gain` and `Offset` must be scalar or have the same dimensions as the input. The output is a vector or matrix of the same dimensions as the input.
