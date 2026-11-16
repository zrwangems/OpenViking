---
type: simulink-block
title: 'Complex to Real-Imag'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'complextorealimag'
documentation_source_path: '../simulink/slref/complextorealimag.html'
language: en
---

# Complex to Real-Imag

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Complex input signal that the block computes and outputs the real
and/or imaginary part.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal that is the real and/or imaginary part of the input
signal. To choose which part is output, set the
**Output** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### **Output** — Real and/or imaginary output specification `Real and imag` (default) | `Real` | `Imag`

Specify whether the output is the real, imaginary, or both real and
imaginary part of the input signal.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `Output` |
| **Type:** string | character vector |
| **Values:** `'Real and imag'` | `'Real'` | `'Imag'` |
| **Default:** `'Real and imag'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

## Libraries

Simulink / Math Operations HDL Coder / Math Operations

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

**Complex Data Support**

This block supports code generation for complex signals.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Output real and imaginary parts of complex input signal

The Complex to Real-Imag block outputs the real and/or imaginary part
of the input signal, depending on the setting of the **Output**
parameter. The real outputs are of the same data type as the complex input. The input
can be an array (vector or matrix) of complex signals, in which case the output signals
are arrays of the same dimensions. The real array contains the real parts of the
corresponding complex input elements. The imaginary output similarly contains the
imaginary parts of the input elements.
