---
type: simulink-block
title: 'Upsample'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'upsample'
documentation_source_path: 'ref/upsample.html'
language: en
---

# Upsample

## Ports

### Input

### **in** — Input signal scalar | vector | matrix

Specify the input signal as a real or a complex-valued scalar, vector,
or a matrix signal.

When you set **Input processing** to
`Columns as channels (frame based)` and
**Rate options** to `Enforce
single-rate processing`, the input can be a
variable-size signal. When the input is a variable-size signal, the
frame size (number of rows) and the number of channels (columns) of the
signal can change during simulation.

This port is unnamed until you
set **Upsample factor source** to `Input
port`. *(since R2023a)*

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **L** — Upsample factor positive integer ≤ *Lmax*

*Since R2023a*

Specify the upsample factor *L* as a positive integer less than or
equal to the value you specify in the **Maximum upsample factor,
Lmax** parameter.

#### Dependency

To enable this port, set the **Upsample factor
source** parameter to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Upsampled signal scalar | vector | matrix

The Upsample block outputs a signal that has the same data type and
complexity as the input signal. The size of the output depends on the
value of the upsample factor and the option you select in the
**Rate options** parameter.

If you set **Upsample factor, L** to *L* and
**Rate options** to:

- `Enforce single-rate processing`
  –– The block maintains the input sample rate by increasing
  the output frame size by a factor of
  *L*.
- `Allow multirate processing` ––
  The block resamples the signal such that the output sample
  rate is *L* times faster than the input
  sample rate. The output signal has the same frame size as
  the input signal.

When you input the upsample
factor through the input port **L**, the **Rate
options** parameter is automatically set to
`Enforce single-rate processing`. In this
case, the block maintains the input sample rate at the output by
increasing the output frame size by a factor of
*L*. *(since R2023a)*

The output is a variable-size signal when one or both of these
conditions are met:

- Input is a variable-size signal.
- Upsample factor is input through the port
  **L**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Upsample factor source** — Mode of specifying upsample factor `Dialog parameter` (default) | `Input port`

*Since R2023a*

Specify the upsample factor through one of these options:

- `Dialog parameter` –– The block
  enables the **Upsample factor, L** parameter on
  the block dialog box.
- `Input port` –– The block enables the
  input port **L** through which you can specify
  the upsample factor.

### **Upsample factor, L** — Upsample factor `3` (default) | positive integer

Specify the upsample factor *L* by which to increase the input sample
rate as a positive integer.

#### Dependency

To enable this parameter, set
**Upsample factor source** to `Dialog
parameter`. *(since R2023a)*

### **Sample offset (0 to L−1)** — Sample offset `0` (default) | integer in the range [0, *L*−1]

Specify the sample offset *D* as an integer in the range
[0, *L*−1].

Use the **Sample offset (0 to L−1)** parameter to delay the output
samples by a specific number of sample periods. Doing so enables you to
select any of the *L* possible output phases. The value you
specify in the **Sample offset (0 to L−1)** parameter must
be an integer in the range 0≤D<(L−1).

When you input the upsample factor through the
input port **L**, the **Sample offset (0 to
L−1)** parameter is not enabled in the block dialog box. In
this case, the sample offset *D* is automatically set to
0. *(since R2023a)*

#### Dependency

To enable this parameter, set
**Upsample factor source** to `Dialog
parameter`. *(since R2023a)*

### **Maximum upsample factor, Lmax** — Maximum upsample factor `16` (default) | positive integer ≥ 1

*Since R2023a*

Specify the maximum upsample factor *Lmax* as a positive
integer greater than or equal to `1`. The upsample factor
you specify through the input port **L** must be less than
or equal to *Lmax*.

#### Dependency

To enable this parameter, set **Upsample factor
source** to `Input port`.

### **Input processing** — Method to process input signals `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block should process the input. You can set this parameter to one of
these options:

- `Columns as channels (frame based)`
  — When you select this option, the block treats each column
  of the input as a separate channel. In this mode, the block can
  perform single-rate or multirate processing.
- `Elements as channels (sample based)`
  — When you select this option, the block treats each element
  of the input as a separate channel. In this mode, the block always
  performs multirate processing.

#### Dependency

To enable this parameter, set
**Upsample factor source** to `Dialog
parameter`. *(since R2023a)*

When you set **Upsample
factor source** to `Input port`,
the **Input processing** parameter is automatically set
to `Columns as channels (frame based)`. *(since R2023a)*

### **Rate options** — Method to upsample input `Enforce single-rate processing` (default) | `Allow multirate processing`

Specify the method that the block uses to upsample the input. You can
select one of the following options:

- `Enforce single-rate processing` —
  When you select this option, the block maintains the input sample
  rate by increasing the output frame size by a factor of
  *L*. To select this option, you must set the
  **Input processing** parameter to
  `Columns as channels (frame
  based)`.
- `Allow multirate processing` —
  When you select this option, the block resamples the signal such
  that the output sample rate is *L* times faster
  than the input sample rate.

#### Dependency

To enable this parameter, set
**Upsample factor source** to `Dialog
parameter`. *(since R2023a)*

When you set **Upsample
factor source** to `Input port`,
the **Rate options** parameter is automatically set to
`Enforce single-rate processing`. *(since R2023a)*

### **Initial conditions** — Initial conditions `0` (default) | scalar | vector | matrix

Specify the value with which the block is initialized for cases of nonzero
latency as a scalar, vector, or a matrix. The scalar value appears in the
output as the sample *D*+1. If this parameter is set to a
vector or a matrix, the size of this parameter should be the same as that of
the input. This parameter appears only when you configure the block to
perform multirate processing.

#### Dependencies

To enable this parameter, set **Rate options** to `Allow
multirate processing`.

## Libraries

DSP System Toolbox / Signal Operations DSP System Toolbox HDL Support / Signal Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**Best Practices**

Consider whether your model can use the Repeat block instead of the
Upsample block. The Repeat block uses fewer
hardware resources, so as a best practice use the Upsample block
only when your algorithm requires zero-padding upsampling.

See also Multirate Model Requirements for HDL Code Generation (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

- **Input processing** set to `Columns as
  channels (frame based)` is not supported.
- **Upsample factor source** set to `Input
  port` is not supported.

**Complex Data Support**

This block supports code generation for complex signals.

## Version History

**Introduced before R2006a**

### R2025a: Support for clock-rate pipelining during HDL code generation

Starting in R2025a, when you use the clock-rate pipelining optimization, the Upsample block does not act as a barrier to the optimization. As a
result, clock-rate pipelining optimizes multirate designs more effectively by
reducing the large amount of latency and unbalanced delays that could have
previously occurred. For example, in previous releases, a multirate design with
feedback loops might generate delay balancing errors when you enabled clock-rate
pipelining. In R2025a, these designs do not generate delay balancing errors.

### R2023a: Tune upsample factor through input port

You can now specify the upsample factor through an input port when the
Upsample block operates in the single-rate frame-based processing
mode. When you specify the upsample factor through the input port, you can change
the factor during simulation.

### R2022b: Support for variable-size input signal

Starting in R2022b, when you set **Input processing** to
`Columns as channels (frame based)` and **Rate
options** to `Enforce single-rate processing`,
the input can be a variable-size signal. That is, the frame size (number of rows)
and the number of channels (columns) of the signal can change during
simulation.

When the input is a variable-size signal, the output is also a variable-size
signal.

## Description

Resample input at higher rate by inserting zeros

The Upsample block resamples each channel of the
*M*i-by-*N* input at a rate
*L* times higher than the input sample rate by inserting
*L*−1 zeros between consecutive samples. Specify the integer
*L* in the **Upsample factor, L** parameter or
through the input port **L**.

You can use this block inside triggered subsystems when you set the **Rate
options** parameter to `Enforce single-rate
processing`.
