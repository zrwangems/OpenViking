---
type: simulink-block
title: 'Complex to Magnitude-Angle'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Complex Numbers'
documentation_page: 'complextomagnitudeangle'
documentation_source_path: '../dsphdl/ref/complextomagnitudeangle.html'
language: en
---

# Complex to Magnitude-Angle

## Ports

### Input

### **data** — Complex input signal scalar | vector

Complex input signal, specified as a scalar, a column vector representing samples
in time, or a row vector representing channels. Using vector input increases data
throughput while using more hardware resources. The block implements the conversion
logic in parallel for each element of the vector. The input vector can contain up to
64 elements.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid input data scalar

Control signal that indicates if the input data is valid. When
**valid** is `1` (`true`), the
block captures values from the input **data** port. When
**valid** is `0` (`false`), the
block ignores the values from the input **data** port.

**Data Types:** `Boolean`
### Output

### **Magnitude** — Magnitude of the input signal scalar | vector

Magnitude of the input signal, returned as a scalar, a column vector representing
samples in time, or a row vector representing channels. The dimensions of this port
match the dimensions of the input **data** port.

#### Dependencies

To enable this port, set the **Output format** parameter to
`Magnitude and Angle` or `Magnitude`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **Angle** — Angle of the input signal scalar | vector

Angle of the input signal, returned as a scalar, a column vector representing
samples in time, or a row vector representing channels. The dimensions of this port
match the dimensions of the input **data** port.

#### Dependencies

To enable this port, set the **Output format** parameter to
`Magnitude and Angle` or `Angle`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **valid** — Indicates valid output data scalar

Control signal that indicates if the data from the output
**data** port is valid. When **valid** is
`1` (`true`), the block returns valid data from
the **Magnitude** and/or **Angle** ports. When
**valid** is `0` (`false`), the
values from the **Magnitude** and/or **Angle** ports
are not valid.

**Data Types:** `Boolean`

## Parameters

### **Number of iterations source** — Source of number of iterations `Auto` (default) | `Property`

- To set the number of iterations to input *WL* − 1, select
  `Auto`. If the input is of data type `double` or
  `single`, the number of iterations is set to 16, by
  default.
- To specify the number of iterations by using **Number of
  iterations** parameter, select `Property`.

### **Number of iterations** — Number of CORDIC iterations positive integer

The number of iterations must be less than or equal to input *WL* −
1. The latency of the block depends on the number of iterations performed. For
information about latency, see Latency.

#### Dependencies

To enable this parameter, set **Number of iterations source** to
`Property`.

### **Output format** — Output signal format `Magnitude and Angle` (default) | `Magnitude` | `Angle`

Use this parameter to specify which output ports are enabled.

- To enable the **Magnitude** and **Angle**
  output ports, select `Magnitude and Angle` (default).
- To enable the **Magnitude** output port and disable the
  **Angle** output port, select
  `Magnitude`.
- To enable the **Angle** output port and disable the
  **Magnitude** output port, select `Angle`.

### **Angle format** — Output angle format `Normalized` (default) | `Radians`

- To return the **Angle** output as a fixed-point value that
  normalizes the angles in the range [–1,1], select `Normalized`. For
  more information see Normalized Angle Format.
- To return the **Angle** output as a fixed-point value in the
  range [-π, π], select `Radians`. When using this block to implement
  the `atan2` function, set this parameter to
  `Radians`.

### **Scale output** — Scales output `on` (default) | `off`

Select this parameter to multiply the **Angle** output by the
inverse of the CORDIC gain factor. The block implements this gain factor with either CSD
logic or a multiplier, according to the **Scaling method** parameter.

**Note**

If you clear this parameter and apply the CORDIC gain elsewhere in your design,
you must exclude the π/4 term. Because the quadrant mapping algorithm replaces the
first CORDIC iteration by mapping inputs onto the angle range [0, π/4], the initial
rotation does not contribute a gain term. The gain factor is the product of
`cos(atan(2-n))`, for
*n* from 1 to **Number of iterations** – 1.

#### Dependencies

To enable this parameter, set the **Output format** parameter to
`Magnitude and Angle` or `Magnitude`.

### **Scaling method** — Implementation of CORDIC gain scaling `Shift-Add` (default) | `Multipliers`

When you set this parameter to `Shift-Add`, the block
implements the CORDIC gain scaling by using a shift-and-add architecture for the
multiply operation. This implementation uses no multiplier resources and may increase
the length of the critical path in your design. When you select
`Multipliers`, the block implements the CORDIC gain scaling
with a multiplier and increases the latency of the block by four
cycles.

#### Dependencies

To enable this parameter, select the **Scale output**
parameter.

## Libraries

DSP HDL Toolbox / Math Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration option that affect HDL implementation and
synthesized logic.

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

## Version History

**Introduced in R2014b**

### R2022a: Moved to DSP HDL Toolbox from DSP System Toolbox

Before R2022a, this block was named Complex to Magnitude-Angle HDL
Optimized and was included in the DSP System Toolbox™
**DSP System Toolbox HDL Support** library.

### R2022a: Option to use multiplier for scale factor

In previous releases, the block implemented the CORDIC gain for hardware by using
shift-and-add logic. To use a multiplier, set the **Scaling method**
parameter to `Multipliers`. To use shift-and-add logic, set this
parameter to `Shift-Add`.

### R2021b: High-throughput interface

The block accepts and returns a column vector of elements that represent samples in
time. The input vector can contain up to 64 samples.

## Description

Compute magnitude and phase angle of complex signal using CORDIC algorithm

The Complex to Magnitude-Angle block computes the magnitude and phase angle
of a complex signal and provides hardware-friendly control signals. To achieve an efficient
HDL implementation, the block uses a pipelined Coordinate Rotation Digital Computer (CORDIC)
algorithm.

You can use this block to implement operations such as `atan2` in hardware.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
