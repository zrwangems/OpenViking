---
type: simulink-block
title: 'Real-Imag to Complex'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'realimagtocomplex'
documentation_source_path: '../simulink/slref/realimagtocomplex.html'
language: en
---

# Real-Imag to Complex

## Ports
```yaml
ports:
- name: Re
  summary: Real part of complex output scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | bus
- name: Im
  summary: Imaginary part of complex output scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | bus
- name: Port_1
  summary: Real or imaginary part of complex output scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | bus
- name: Port_1
  summary: Complex signal scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Re** — Real part of complex output scalar | vector | matrix

Real value to be converted to complex-valued output signal, specified
as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **Im** — Imaginary part of complex output scalar | vector | matrix

Imaginary value to be converted to complex-valued output signal,
specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **Port\_1** — Real or imaginary part of complex output scalar | vector | matrix

Real or imaginary value to convert to complex output signal, specified
as a finite scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
### Output

### **Port\_1** — Complex signal scalar | vector | matrix

Complex signal, formed from real and imaginary values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Input
  summary: Real, imaginary, or both Real (default) | Imag | Real and imag
  group: ''
  block_parameter: Input
  type: character vector
  values: '''Real and imag'' | ''Real'' | ''Imag'''
  default: '''Real and imag'''
- name: Imag part
  summary: Imaginary part of complex output 0 (default) | finite scalar, vector, or matrix
  group: ''
  block_parameter: ConstantPart
  type: character vector
  values: imaginary value
  default: '''0'''
- name: Real part
  summary: Real part of complex output 0 (default) | finite scalar, vector, or matrix
  group: ''
  block_parameter: ConstantPart
  type: character vector
  values: finite, real-valued scalar, vector, or matrix
  default: '''0'''
- name: Sample time (-1 for inherited)
  summary: Interval between samples -1 (default) | scalar | vector
  group: ''
  block_parameter: SampleTime
  values: '"-1" (default) | scalar or vector in quotes'
```

### **Input** — Real, imaginary, or both `Real` (default) | `Imag` | `Real and imag`

Specify the type of input: a real input, an imaginary input, or both.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Input` |
| **Type:** character vector |
| **Values:** `'Real and imag' | 'Real' | 'Imag'` |
| **Default:** `'Real and imag'` |

### **Imag part** — Imaginary part of complex output `0` (default) | finite scalar, vector, or matrix

Specify the imaginary value to use when converting the input to a
complex-valued output signal.

#### Dependencies

To enable this parameter, set **Input** to
`Real`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConstantPart` |
| **Type:** character vector |
| **Values:** imaginary value |
| **Default:** `'0'` |

### **Real part** — Real part of complex output `0` (default) | finite scalar, vector, or matrix

Specify the constant real value to use when converting the input to a
complex-valued output signal.

#### Dependencies

To enable this parameter, set **Input** to
`Imag`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConstantPart` |
| **Type:** character vector |
| **Values:** finite, real-valued scalar, vector, or matrix |
| **Default:** `'0'` |

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
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
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

Convert real and/or imaginary inputs to complex signal

The Real-Imag to Complex block converts real and/or imaginary inputs to a
complex-valued output signal.

The inputs can both be arrays (vectors or matrices) of equal dimensions, or one input can be an array and the other a scalar. If the block has an array input, the output is a complex array of the same dimensions. The elements of the real input map to the real parts of the corresponding complex output elements. The imaginary input similarly maps to the imaginary parts of the complex output signals. If one input is a scalar, it maps to the corresponding component (real or imaginary) of all the complex output signals.
