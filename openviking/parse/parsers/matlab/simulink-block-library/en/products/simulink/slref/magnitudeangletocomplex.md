---
type: simulink-block
title: 'Magnitude-Angle to Complex'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Math Operations'
documentation_page: 'magnitudeangletocomplex'
documentation_source_path: 'slref/magnitudeangletocomplex.html'
language: en
---

# Magnitude-Angle to Complex

## Ports

### Input

### **|u|** — Magnitude scalar | vector | matrix

Magnitude, specified as a real-valued scalar, vector, or matrix.

#### Dependencies

- To enable this port, set **Input** to
  `Magnitude and angle`.

#### Limitations

- If one input has a floating-point data type, the other
  input must use the same data type. For example, both signals
  must be `double` or
  `single`.
- Fixed-point data types are supported only when you set the
  **Approximation method** to
  `CORDIC`. When one input has a
  fixed-point data type, the other input must also have a
  fixed-point data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **∠u** — Radian phase angle scalar | vector | matrix

Radian phase angle, specified as a real-valued scalar, vector, or
matrix. To compute the CORDIC approximation, the input angle must be
between:

- [–2π, 2π) rad, for signed fixed-point types
- [0, 2π) rad, for unsigned fixed-point types

For more information, see Effect of Out-of-Range Input on CORDIC Approximations.

#### Dependencies

- To enable this port, set **Input** to
  `Magnitude and angle`.

#### Limitations

- If one input has a floating-point data type, the other
  input must use the same data type. For example, both signals
  must be `double` or
  `single`.
- Fixed-point data types are supported only when you set the
  **Approximation method** to
  `CORDIC`. If one input has a
  fixed-point data type, the other input must also have a
  fixed-point data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_1** — Magnitude or radian phase angle scalar | vector | matrix

Magnitude, or radian phase angle, specified as a real-valued scalar,
vector, or matrix.

- When you set **Input** to
  `Magnitude`, you specify the
  magnitude at the input port, and the angle on the dialog
  box.
- When you set **Input** to
  `Angle`, you specify the angle at
  the input port, and the magnitude on the dialog box.

#### Dependencies

To enable this port, set **Input** to
`Magnitude` or
`Angle`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Complex signal scalar | vector | matrix

Complex signal, formed from the magnitude and phase angle you
specify.

If the block input is an array, the output is an array of complex
signals. The elements of a magnitude input vector map to the magnitudes
of the corresponding complex output elements. Similarly, the elements of
an angle input vector map to the angles of the corresponding complex
output elements. If one input is a scalar, it maps to the corresponding
component (magnitude or angle) of all the complex output signals.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Input** — Type of input `Magnitude` (default) | `Angle` | `Magnitude and angle`

Specify the kind of input: a magnitude input, an angle input, or
both.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Input` |
| **Type:** character vector |
| **Values:** `'Magnitude' | 'Angle' | 'Magnitude and angle'` |
| **Default:** `'Magnitude and angle'` |

### **Angle** — Phase angle of output `0` (default) | real-valued scalar, vector, or matrix

Constant phase angle of the output signal, in rad. To compute the CORDIC approximation,
the input angle must be between:

- [–2π, 2π) rad, for signed fixed-point types
- [0, 2π) rad, for unsigned fixed-point types

For more information, see Effect of Out-of-Range Input on CORDIC Approximations.

#### Dependencies

To enable this parameter, set **Input** to
`Magnitude`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConstantPart` |
| **Type:** character vector |
| **Values:** constant scalar |
| **Default:** `'0'` |

### **Magnitude** — Magnitude of output `0` (default) | real-valued scalar, vector, or matrix

Constant magnitude of the output signal, specified as a real-valued
scalar, vector, or matrix.

#### Dependencies

To enable this parameter, set **Input** to
`Angle`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConstantPart` |
| **Type:** character vector |
| **Values:**real-valued scalar, vector, or matrix |
| **Default:** `'0'` |

### **Approximation method** — CORDIC or none `None` (default) | `CORDIC`

Specify the type of approximation for computing output.

| Approximation Method | Data Types Supported | When to Use This Method |
| --- | --- | --- |
| `None` (default) | Floating point | You want to use the default Taylor series algorithm. |
| `CORDIC` | Floating point and fixed point | You want a fast, approximate calculation. |

When you use the CORDIC approximation, follow these guidelines for the input angle:

- For signed fixed-point types, the input angle must fall within the range [–2π, 2π) rad.
- For unsigned fixed-point types, the input angle must fall within the range [0, 2π) rad.

The block uses the following data type propagation rules:

| Data Type of Magnitude Input | Approximation Method | Data Type of Complex Output |
| --- | --- | --- |
| Floating point | `None` or `CORDIC` | Same as input |
| Signed, fixed point | `CORDIC` | `fixdt`(1, *`WL`* + 2, *`FL`*)  where *`WL`* and *`FL`* are the word length and fraction length of the magnitude |
| Unsigned, fixed point | `CORDIC` | `fixdt`(1, *`WL`* + 3, *`FL`*)  where *`WL`* and *`FL`* are the word length and fraction length of the magnitude |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApproximationMethod` |
| **Type:** character vector |
| **Values:** `'None' | 'CORDIC'` |
| **Default:** `'None'` |

### **Number of iterations** — Number of iterations for CORDIC algorithm `11` (default) | positive integer, less than or equal to word length of fixed-point input

Number of iterations to perform the CORDIC algorithm. The range of
possible values depends on the data type of the input:

| Data Type of Block Inputs | Value You Can Specify |
| --- | --- |
| Floating point | A positive integer |
| Fixed point | A positive integer that does not exceed the word length of the magnitude input or the word length of the phase angle input, whichever value is smaller |

#### Dependencies

To enable this parameter, set **Approximation
method** to `CORDIC`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfIterations` |
| **Type:** character vector |
| **Values:** positive integer, less than or equal to word length of fixed-point input |
| **Default:** `'11'` |

### **Scale output by reciprocal of gain factor** — Scale real and imaginary parts of complex output `on` (default) | `off`

Select this check box to scale the real and imaginary parts of the complex
output by a factor of `(1/CORDIC gain)`. This value depends
on the number of iterations you specify. As the number of iterations goes
up, the value approaches 1.647.

This check box is selected by default, which leads to a more numerically
accurate result for the complex output, `X + iY`. However,
scaling the output adds two extra multiplication operations, one for
`X` and one for `Y`.

#### Dependencies

To enable this parameter, set **Approximation
method** to `CORDIC`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleReciprocalGainFactor` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

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

Simulink / Math Operations HDL Coder / HDL Floating Point Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
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

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

**HDL Block Properties**

**General**

| HDL Property | Description |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `MAX`, `Min`, `CUSTOM`, or `ZERO` latency for fixed-point and floating-point types. The default is `MAX`. See also LatencyStrategy (HDL Coder). |
| **CustomLatency** | When **LatencyStrategy** is set to `CUSTOM`, use this property to specify a custom latency value between `ZERO` and `MAX` for fixed-point types. See also LatencyStrategy (HDL Coder). |

**Native Floating Point**

| HDL Property | Description |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **InputRangeReduction** | Specify whether your input range is bounded or unbounded. If your input range is unbounded, enable this property for HDL Coder to insert additional logic to reduce the range of inputs to `[-pi, pi]`. The default is `on`. See also InputRangeReduction (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |

**Fixed-Point Support**

You can generate code for Magnitude-Angle to Complex block with fixed-point
data types as input. To generate the code with fixed-point data types for the
block, set **Input** to `Magnitude and
angle` and the **Approximation method** to
`CORDIC`. When using the CORDIC approximation
method, the block adds additional cycles of latency as given in table
below.

| Architecture | Parameter | Additional cycles of latency |
| --- | --- | --- |
| `Pol2CartCordic` | **Number of iterations**  **Scale output by reciprocal of gain factor** | When **Scale output by reciprocal of gain factor** parameter is `off`,  *Max Latency* = **Number of iterations** + 1.  When **Scale output by reciprocal of gain factor** parameter is `on`,  *Max Latency* = **Number of iterations** + 6. |

**Restrictions**

Fixed-point data types are not supported when you set
**Input** to `Magnitude` or
`Angle`.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

The Magnitude-Angle to Complex block supports fixed-point and base integer data
types when you set **Approximation method** to
`CORDIC`.

## Version History

**Introduced before R2006a**

### R2024a: Generate HDL code with fixed-point data types

Starting in R2024a, you can generate HDL code for Magnitude-Angle to Complex block
that uses fixed-point data types as inputs. To generate code with fixed-point data
types, set the **Input** block parameter to `Magnitude
and angle` and the **Approximation method**
parameter to `CORDIC`. When using the CORDIC approximation
method, you can also enable **Scale output by reciprocal of gain
factor** to scale the real and imaginary parts of the complex output by
a gain factor.

## Description

Convert magnitude and/or a phase angle signal to complex signal

### Supported Operations

The Magnitude-Angle to Complex block converts magnitude and phase angle
inputs to a complex output. The angle input must be in rad.

When there are two block inputs, the block supports these combinations of input
dimensions:

- Two inputs of equal dimensions
- One scalar input and the other an n-dimensional array

If the block input is an array, the output is an array of complex signals. The elements of a magnitude input vector map to the magnitudes of the corresponding complex output elements. Similarly, the elements of an angle input vector map to the angles of the corresponding complex output elements. If one input is a scalar, it maps to the corresponding component (magnitude or angle) of all the complex output signals.

### Effect of Out-of-Range Input on CORDIC Approximations

If you use the CORDIC approximation method [1],
the block input for phase angle has these restrictions:

- For signed fixed-point types, the input angle must fall within the range
  [–2π, 2π) rad.
- For unsigned fixed-point types, the input angle must fall within the range
  [0, 2π) rad.

This table summarizes the effects of an out-of-range input:

| Block Usage | Effect of Out-of-Range Input |
| --- | --- |
| Simulation modes | An error appears. |
| Generated code | Undefined behavior occurs. |

When you use the CORDIC approximation, ensure that you use an in-range input for the
Magnitude-Angle to Complex block. Avoid relying on undefined
behavior for generated code or accelerator modes.
