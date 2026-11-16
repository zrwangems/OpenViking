---
type: simulink-block
title: 'Downsample'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'downsample'
documentation_source_path: '../dsp/ref/downsample.html'
language: en
---

# Downsample

## Ports

### Input

### **in** — Data input column vector | matrix | *N*-D array

Input data for which you want to decrease the sample rate, specified
as a column vector or a matrix.

When you set the **Input processing** parameter to
`Elements as channels (sample based)`, the
input can be an *N*-D array.

The block supports variable-size input signals when you set
**Input processing** to `Columns as
channels (frame based)` and **Rate
options** to `Enforce single-rate
processing`, so the frame length (number of rows) and
the number of channels (columns) can change during simulation. When the
block accepts variable-size input signals, they can be of arbitrary
frame length, that is, the input frame length does not have to be a
multiple of the downsampling factor. When you specify fixed-size
signals, the frame length can be arbitrary under certain conditions. For
more details, see Frame-Based Processing and
Sample-Based Processing.

This port is unnamed until you
set **Downsample factor source** to `Input
port`. *(since R2023a)*

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **M** — Downsample factor positive integer

*Since R2023a*

Specify the downsample factor *M* as a positive
integer.

#### Dependency

To enable this port, set the **Downsample factor
source** parameter to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Downsampled output column vector | matrix

Downsampled output with a sampling rate that is 1/*M*
times the input sampling rate, returned as a column vector or a
matrix.

When you set **Rate options** to:

- `Enforce single-rate processing`
  –– The block maintains the input sample rate and downsamples
  the signal by decreasing the output frame size by a factor
  of *M*.

  The output has an upper bound size of
  `ceil`(*P*/*M*)-by-*Q*
  for an input of size
  *P*-by-*Q*.
- `Allow multirate processing` ––
  The block downsamples the signal such that the output sample
  rate is *M* times slower than the input
  sample rate.

  The output frame size is the same as the input frame
  size.

For more details, see Frame-Based Processing and
Sample-Based Processing.

The output is a variable-size signal when any of these conditions are met:

- The input is a variable-size signal.
- The input is a fixed-size signal and the **Allow
  arbitrary frame length for fixed-size input
  signals** parameter is selected.
- Downsample factor is
  input through the port **M** *(since R2023a)*

When the output is a variable-size signal, the block maintains the
phase across consecutive frames of data. For more details, see Phase Continuity.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Downsample factor source** — Source of downsample factor `Dialog parameter` (default) | `Input port`

*Since R2023a*

Specify the downsample factor through one of these options:

- `Dialog parameter` –– The block
  enables the **Downsample factor, M** parameter
  in the block dialog box.
- `Input port` –– The block enables the
  input port **M** through which you specify the
  downsample factor.

### **Downsample factor, M** — Downsampling factor `2` (default) | positive integer

Specify the integer factor *M* by which to decrease the
input sample rate.

#### Dependency

To enable this parameter, set
**Downsample factor source** to `Dialog
parameter`. *(since R2023a)*

### **Sample offset (0 to M−1)** — Sample offset `0` (default) | integer

The **Sample offset (0 to M−1)** parameter delays the
output samples by an integer number of sample periods, *D*,
where 0 ≤ *D* ≤ (*M*–1), so that you can
select any of the *M* possible output phases. For example,
when you downsample the sequence 1, 2, 3, ... by a factor of 4, you can
select from four phases.

| Input Sequence | Sample Offset, *D* | Output Sequence (*M* = 4) |
| --- | --- | --- |
| `1,2,3,...` | 0 | `1,5,9,13,17,21,25,29,...` |
| `1,2,3,...` | 1 | `0,2,6,10,14,18,22,26,...` |
| `1,2,3,...` | 2 | `0,3,7,11,15,19,23,27,...` |
| `1,2,3,...` | 3 | `0,4,8,12,16,20,24,28,...` |

The initial zero in the last three output sequences in the table is a
result of the **Initial conditions** parameter being set to
its default value of 0. See Latency for more
information on the **Initial conditions** parameter.

When you input the downsample factor
through the input port **M**, the **Sample offset
(0 to M−1)** parameter is not enabled in the block dialog box.
In this case, the sample offset *D* is automatically set to
0. *(since R2023a)*

#### Dependency

To enable this parameter, set
**Downsample factor source** to `Dialog
parameter`. *(since R2023a)*

### **Input processing** — Method to process input `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify the method for input processing:

- `Columns as channels (frame based)` ––
  When you set the **Input processing** parameter to
  `Columns as channels (frame based)`,
  the block treats each of the *Q* input columns as
  an individual channel containing
  *Pi* sequential time
  samples. The block downsamples each channel independently by
  discarding *M*–1 rows of the input matrix following
  each row that it outputs.

  For more information, see What Is Frame-Based Processing?.
- `Elements as channels (sample based)` ––
  When you set the **Input processing** parameter to
  `Elements as channels (sample based)`,
  the input can be a *Q*-D array. The
  Downsample block treats each element of the input
  as a separate channel, and resamples each channel of the input over
  time. The block downsamples the input array by discarding
  *M*–1 samples following each sample that it
  passes through to the output. The input and output sizes of the
  Downsample block are identical.

  For more information, see What Is Sample-Based Processing?.

#### Dependency

To enable this parameter, set
**Downsample factor source** to `Dialog
parameter`. *(since R2023a)*

When you set
**Downsample factor source** to `Input
port`, the **Input processing**
parameter is automatically set to `Columns as channels
(frame based)`. *(since R2023a)*

### **Rate options** — Enforce single-rate or allow multirate processing `Enforce single-rate processing` (default) | `Allow multirate processing`

Specify the method by which the block adjusts the rate at the output port
to accommodate the reduced number of samples. The block performs single-rate
or multirate processing depending on whether you set the **Input
processing** parameter to `Elements as channels
(sample based)` (sample-based processing mode) or
`Columns as channels (frame based)`
(frame-based processing mode).

- `Elements as channels (sample
  based)`

  - `Enforce single-rate
    processing`

    The block forces the output sample rate to match the input
    sample rate (*Tso* =
    *Tsi*) by
    repeating every
    *Mth* input
    sample *M* times at the output. In this
    mode, the block behaves like the Sample and Hold block with
    a repeating trigger event of period
    *MTsi*.
  - `Allow multirate
    processing`

    The sample period of the output is *M*
    times longer than the input sample period
    (*Tso* =
    *MTsi*).

  For more details, see Sample-Based Processing
- `Columns as channels (frame
  based)`

  - `Enforce single rate
    processing`

    The block generates the output at the slower (downsampled)
    rate using a proportionally smaller frame
    *size* than the input. The output has
    an upper bound size of
    `ceil`(*P*/*M*),
    where *P* is the input frame length and
    *M* is the downsample factor. The input
    and output frame rates are equal. For more details, see
    Frame-Based Processing. For an example, see Downsample Signal in Single-Rate Frame-Based Processing Mode.
  - `Allow multirate
    processing`

    The block generates the output at the slower (downsampled)
    rate by using a proportionally longer frame
    *period* at the output port than at
    the input port. For downsampling by a factor of
    *M*, the output frame period is
    *M* times longer than the input frame
    period (*Tfo* =
    *MTfi*), but
    the input and output frame sizes are equal. For more
    details, see Frame-Based Processing. For an example, see Downsample Signal In Multirate Frame-Based Processing Mode.

#### Dependency

To enable this parameter, set
**Downsample factor source** to `Dialog
parameter`. *(since R2023a)*

When you set
**Downsample factor source** to `Input
port`, the **Rate options** parameter
is automatically set to `Enforce single-rate
processing`. *(since R2023a)*

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals on (default) | off

Specify whether fixed-size input signals (size does not change during
simulation) can have an arbitrary frame length, where the frame length does
not have to be a multiple of the downsampling factor. The block uses this
parameter setting only for fixed-size input signals and ignores this
parameter if the input has a variable size.

When the input signal is a variable-size signal, the signal can have an
arbitrary frame length, that is, the frame length does not have to be a
multiple of the decimation factor.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the frame
  length of the signal does not have to be a multiple of the
  downsampling factor. If the input is not a multiple of the
  downsampling factor, then the output is generally a
  variable-size signal. Therefore, to support an arbitrary input
  size, the block must also support variable-size operations,
  which you can enable by selecting the **Allow arbitrary
  frame length for fixed-size input signals**
  parameter.
- Clear the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the input
  frame length must be a multiple of the downsampling
  factor.

#### Dependency

To enable this parameter, set:

- **Downsample
  factor source** to `Dialog
  parameter`. *(since R2023a)*
- **Input processing** to
  `Columns as channels (frame
  based)`.
- **Rate options** to `Enforce
  single-rate processing`.

### **Initial conditions** — Initial value `0` (default) | real scalar | array

The initial block value for cases of nonzero latency. You can specify a
scalar or an array of the same size as the input.

#### Dependencies

This parameter does not appear when **Input
processing** is set to `Columns as channels
(frame based)` and **Rate options** is
set to `Enforce single-rate processing`.

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

It is good practice to follow the Downsample block with a unit delay. Doing so
prevents the code generator from inserting an extra bypass register in the HDL
code.

See also Multirate Model Requirements for HDL Code Generation (HDL Coder).

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

**Restrictions**

- **Input processing** set to `Columns
  as channels (frame based)` is not supported.
- For **Input processing** set to
  `Elements as channels (sample based)`,
  select `Allow multirate processing`. With
  this setting, if **Sample offset** is set to 0,
  **Initial conditions**  has
  no
  effect on generated code.

## Version History

**Introduced before R2006a**

### R2023a: Tune downsample factor through input port

You can now specify the downsample factor through an input port when the
Downsample block operates in the single-rate frame-based
processing mode. When you specify the downsample factor through the input port, you
can change the factor during simulation.

### R2022b: Support for arbitrary input frame length and variable input frame sizes

Starting in R2022b, this block supports input signals with arbitrary frame lengths
when the:

- Input signal is a fixed-size signal (signal dimensions do not change
  during simulation) and the block allows for multirate processing
- Input signal is a fixed-size signal, block enforces single-rate
  processing, and you select the **Allow arbitrary frame length
  for fixed-size input signals** parameter (if
  enabled)
- Input signal is a variable-size signal (signal dimensions change
  during simulation)

When this block supports an arbitrary frame length input signal, the input frame
length does not have to be a multiple of the downsampling factor.

For more details, see Frame-Based Processing and Sample-Based Processing.

## Description

Resample input at lower rate by deleting samples

The Downsample block decreases the sampling rate of the input by
deleting samples. When the block performs frame-based processing, it resamples the data
in each column of the
*Pi*-by-*Q* input matrix
independently. When the block performs sample-based processing, it treats each element
of the input as a separate channel and resamples each channel of the input array across
time. The resample rate is *M* times lower than the input sample rate,
where *M* is the value of the downsample factor. The
Downsample block resamples the input by discarding
*M*–1 consecutive samples following each sample that is
output.

This block supports triggered subsystems when you set the **Rate
options** parameter to `Enforce single-rate
processing`.
