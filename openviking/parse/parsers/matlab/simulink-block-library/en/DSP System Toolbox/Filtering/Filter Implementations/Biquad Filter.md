---
type: simulink-block
title: 'Biquad Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'biquadfilter'
documentation_source_path: 'ref/biquadfilter.html'
language: en
---

# Biquad Filter

## Ports

### Input

### **In** — Data input vector | matrix

Data input to the block, specified as a vector or a matrix. This block supports
variable-size input signals, enabling you to change the input frame size (number of rows)
during simulation. However, the number of channels (number of columns) must remain
constant.

If the input is fixed-point, it must be signed fixed-point with binary point
scaling.

This port is unnamed unless you set the **Coefficient source** to
`Input port(s)`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**Complex Number Support:** Yes

### **Num** — Numerator coefficients matrix

Numerator coefficients of the biquad filter, specified as a 3-by-*N*
matrix, where *N* is the number of biquad filter sections.

If **Num** is fixed-point, it must be signed fixed-point with binary
point scaling.

#### Dependencies

This port appears only when you set the **Coefficient source** to
`Input port(s)`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

### **Den** — Denominator coefficients matrix

Denominator coefficients of the biquad filter, specified as a 2-by-*N*
matrix, where *N* is the number of biquad filter sections.

If **Den** is fixed-point, it must be signed fixed-point with binary
point scaling.

#### Dependencies

This port appears only when you set the **Coefficient source** to
`Input port(s)`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

### **g** — Scale values row vector

Scale values of the biquad filter, specified as a 1-by-(*N*+1) vector,
where *N* is the number of biquad filter sections.

If **g** is fixed-point, it must be signed fixed-point with binary
point scaling.

#### Dependencies

This port appears only when you set the **Coefficient source** to
`Input port(s)`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### Output

### **Out** — Filtered output vector | matrix

Filtered output, returned as a vector or a matrix.

The output dimensions always equal the dimensions of the input signal.

If **Out** is fixed-point, it must be signed fixed-point with binary
point scaling.

This port is unnamed unless you set the **Coefficient source** to
`Input port(s)`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Coefficient source** — Mode of operation `Dialog parameters` (default) | `Input port(s)` | `Filter object`

The Biquad Filter block can operate in
three different modes:

- `Dialog parameters` — Enter information about the
  filter, such as structure and coefficients, in the block mask.
- `Input port(s)` — Enter information about the filter
  structure in the block mask using the **Filter structure** parameter. The
  filter coefficients come into the block through additional input ports that appear on the
  block icon:

  - `Num` — Specify numerator coefficients.
  - `Den` — Specify denominator coefficients.
  - `g` — Specify scale values.

  The block assumes the first denominator coefficient of each section to be 1. This
  configuration applies when **Coefficient source** is set to
  `Input port(s)` and **Scale values mode** is
  set to `Specify via input port (g)`.
- `Filter object` — Specify the filter using a `dsp.BiquadFilter`
  System
  object™.

### **Filter** — Name of filter object `BQF` (default) | `dsp.BiquadFilter System object` name

Specify the name of the discrete-time filter that you want the block to implement. You
must specify the filter as a `dsp.BiquadFilter`
System object.

You can define the System object in the block mask or in a MATLAB® workspace variable.

For information on creating System objects, see Define Basic System Objects.

#### Dependencies

This parameter is visible only when **Coefficient source** is set to
`Filter object`.

### **Filter structure** — Filter structure `Direct form II transposed` (default) | `Direct form I` | `Direct form I transposed` | `Direct form II`

Specify the filter structure.

#### Dependencies

This parameter is visible only when **Coefficient source** is set to
`Dialog parameters` or `Input
port(s)`.

### **SOS Matrix (Mx6)** — SOS matrix `[1 0.3 0.4 1 0.1 0.2]` (default) | *M*-by-6 matrix

Specify an *M*-by-6 matrix, where *M* is the number of
sections in the second-order section filter. Each row of the SOS matrix contains the
numerator and denominator coefficients (*bik* and
*aik*) of the corresponding section in the
filter.

[b01b11b21a01a11a21b02b12b22a02a12a22⋮⋮⋮⋮⋮⋮b0Mb1Mb2Ma0Ma1Ma2M]

The leading denominator coefficients [a01
a02 ... a0N] are treated as 1s, regardless of
their actual values. No scaling is applied to the SOS matrix when **a0** is
not 1.

The `ss2sos` and `tf2sos` functions convert a state-space or transfer function description of your
filter into the second-order section description used by this block.

#### Dependencies

This parameter is visible only when **Coefficient source** is set to
`Dialog parameters`.

### **Scale values** — Scale values `1` (default) | scalar | vector

Specify scale values to be used between SOS sections. You can specify a real-valued
scalar or a vector of length *M*+1:

- When you enter a scalar, the value specifies the gain value before the first section
  of the second-order filter. The rest of the gain values default to 1.
- When you enter a vector of *M*+1 values, each value specifies a
  separate section of the filter. For example, the first element is the first gain value, the
  second element is the second gain value, and so on.

Select the **Optimize unity scale values** check box to optimize your
simulation when one or more scale values equal 1. Selecting this option removes the unity
gains so that the values are treated like Simulink lines or wires. In some fixed-point cases
when there are unity scale values, selecting this parameter also omits certain casts. Refer
to the Fixed-Point Data Types section for more
information.

#### Dependencies

This parameter is visible only when **Coefficient source** is set to
`Dialog parameters`.

### **Initial conditions** — Initial conditions `0` (default) | scalar | vector

Specify the initial conditions of the filter states when **Filter
structure** is set to `Direct form II` or
`Direct form II transposed`.

**Direct form II**

**Direct form II transposed**

The Biquad Filter block initializes the internal filter states to zero by
default. To specify nonzero initial states for the filter delays, use the **Initial
conditions** parameter.

To determine the number of initial conditions you must specify and how to specify them,
see the following table on valid initial conditions.

**Valid Initial Conditions**

| Initial Condition | Description |
| --- | --- |
| Scalar | The block initializes all delay elements in the filter to the scalar value. |
| Vector or matrix   (for applying different delay elements to each channel) | Each vector or matrix element specifies a unique initial condition for a corresponding delay element in a corresponding channel. *M* is the number of sections, and *N* is the number of input channels:  - The vector length must equal the number of delay elements in the filter,   2*M*. - The matrix must have the same number of rows as the number of delay elements in   the filter 2*M**N*. The matrix must also have one   column for each channel of the input signal. |

#### Dependencies

This parameter is only visible when **Coefficient source** is set to
`Dialog parameters` or `Input port(s)`
and the **Filter structure** is set to `Direct form
II` or `Direct form II transposed`.

### **Initial conditions on zeros side** — Initial conditions on zeros side `0` (default) | scalar | vector

Specify the initial conditions for the filter states on the side of the filter structure
with the zeros (*b0*,
*b1*, *b2*,
…). This parameter applies only when **Filter structure** is set to
`Direct form I` or `Direct form I
transposed`.

**Direct form I**

**Direct form I transposed**

The Biquad Filter block initializes the internal filter states to zero by
default. To specify nonzero initial states for the filter delays, use the **Initial
conditions on zeros side** parameter.

To determine the number of initial conditions you must specify and how to specify them,
see the following table on valid initial conditions.

**Valid Initial Conditions**

| Initial Condition | Description |
| --- | --- |
| Scalar | The block initializes all delay elements in the filter to the scalar value. |
| Vector or matrix   (for applying different delay elements to each channel) | Each vector or matrix element specifies a unique initial condition for a corresponding delay element in a corresponding channel. Where *M* is the number of sections and *N* is the number of input channels:  - The vector length must equal the number of delay elements in the filter,   2*M*. - The matrix must have the same number of rows as the number of delay elements in   the filter 2*M**N*. The matrix must also have one   column for each channel of the input signal. |

#### Dependencies

This parameter is visible only when **Coefficient source** is set to
`Dialog parameters` or `Input port(s)`
and the **Filter structure** is set to `Direct form
I` or `Direct form I transposed`.

### **Initial conditions on poles side** — Initial conditions on poles side `0` (default) | scalar | vector

Specify the initial conditions for the filter states on the side of the filter structure
with the poles (*a1*,
*a2*, ...). This parameter applies only when
**Filter structure** is set to `Direct form I` or
`Direct form I transposed`.

**Direct form I**

**Direct form I transposed**

The Biquad Filter block initializes the internal filter states to zero by
default. To specify nonzero initial states for the filter delays, use the **Initial
conditions on poles side** parameter.

To determine the number of initial conditions you must specify and how to specify them,
see the following table on valid initial conditions.

**Valid Initial Conditions**

| Initial Condition | Description |
| --- | --- |
| Scalar | The block initializes all delay elements in the filter to the scalar value. |
| Vector or matrix   (for applying different delay elements to each channel) | Each vector or matrix element specifies a unique initial condition for a corresponding delay element in a corresponding channel. Where *M* is the number of sections and *N* is the number of input channels:  - The vector length must equal the number of delay elements in the filter,   2*M*. - The matrix must have the same number of rows as the number of delay elements in   the filter 2*M**N*. The matrix must also have one   column for each channel of the input signal. |

#### Dependencies

This parameter is visible only when **Coefficient source** is set to
`Dialog parameters` or `Input port(s)`
and the **Filter structure** is set to `Direct form
I` or `Direct form I transposed`.

### **Scale values mode** — Mode to specify scale values `Specify via input port (g)` (default) | `Assume all are unity and optimize`

Choose how to specify the scale values to use between filter sections. When you select
`Specify via input port (g)`, you enter the scale values as a 2-D
vector at port **g**. When you select `Assume all are unity and
optimize`, all scale values are removed and treated like Simulink lines or
wires.

#### Dependencies

This parameter is visible only when **Coefficient source** is set to
`Input port(s)`.

### **Action when the a0 values of the SOS matrix are not one** — Action when a0 values of SOS matrix are not one `Warning` (default) | `None` | `Error`

Specify the action the block should perform when the SOS matrix
*a0j* values do not equal one. The action can be
`Warning`, `Error`, or
`None`.

When you choose `None`, the leading coefficients
*a0j* are treated as 1's, regardless of their
actual values. No scaling is applied on the SOS matrix when **a0** is not
1.

#### Dependencies

This parameter is visible only when **Coefficient source** is set to
`Dialog parameters`.

### **Optimize unity scale values** — Optimize unity scale values `on` (default) | `off`

Select this check box to optimize your simulation when one or more scale values equal 1.
Selecting this option removes the unity gains so that the values are treated like Simulink
lines or wires. In some fixed-point cases when there are unity scale values, selecting this
parameter also omits certain casts. See the Fixed-Point Data Types section for more
information.

#### Dependencies

This parameter is visible only when **Coefficient source** is set to
`Dialog parameters`.

### **Input processing** — Input processing `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block should process the input. If the input is an
*M*-by-*N* matrix, you can set this parameter to:

- `Columns as channels (frame based)` (default) — The
  block treats each column as a separate channel. In this mode, the block creates
  *M* instances of the same filter, each with its own independent state
  buffer. Each of the *M* filters process *N* input samples
  at every Simulink time step.
- `Elements as channels (sample based)` — The block
  treats each element as a separate channel. In this mode, the block creates
  *M**N* instances of the same filter, each with its own
  independent state buffer. Each filter processes one input sample at every Simulink time step.

### **View Filter Response** — View filter response button

This button opens the Filter Visualization Tool (FVTool) and displays the filter response of the filter specified in the
dialog.

**Note**

When you make changes to the filter parameters on the block dialog, you must click the
**Apply** button before using the **View Filter
Response** button.

### Data Types Tab

**Note**

This tab appears only when you set **Coefficient source** to either
`Dialog parameters` or `Input port(s)`. When
the **Coefficient source** is set to `Filter object`,
the data types specified in the filter object properties are used by the block.

### **Rounding mode** — Rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations.

For more details, see rounding mode. The filter
coefficients do not obey this parameter; instead, they always round to
`Nearest`.

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

When you select this parameter, the block saturates the result of its fixed-point
operation. When you clear this parameter, the block wraps the result of its fixed-point
operation. For details on `saturate` and `wrap`, see overflow mode for fixed-point operations.

The filter coefficients are always saturated and do not obey this parameter.

### **Section input** — Section input data type `Same as input` (default) | `Binary point scaling`

Choose how you specify the word and fraction lengths of the fixed-point data type going
into each section of a biquadratic filter. See the Fixed-Point Data Types section for illustrations
depicting the use of the section input data type in this block. When you select:

- `Same as input` — Word length and fraction length
  characteristics of the **Section input** data type match those of the
  input to the block.
- `Binary point scaling` — Enter the word and fraction
  lengths of the section input, in bits.

### **Section output** — Section output data type `Same as section input` (default) | `Binary point scaling`

Choose how you specify the word and fraction lengths of the fixed-point data type coming
out of each section of a biquadratic filter. See the Fixed-Point Data Types section for illustrations
depicting the use of the section output data type in this block. When you select:

- `Same as section input` — Word length and fraction
  length characteristics of the **Section output** data type match with
  those of the input to the block.
- `Binary point scaling` — Enter the word and fraction
  lengths of the section output, in bits.

### **Multiplicand** — Multiplicand data type `Same as output` (default) | `Binary point scaling`

Choose how you specify the word and fraction lengths of the multiplicand data type of a
`Direct form I transposed` filter structure. See the Fixed-Point Data Types section for illustrations
depicting the use of the multiplicand data type in this block.

When you select:

- `Same as output` — Word length and fraction length
  characteristics of the **Multiplicand** data type match with those of the
  output of the block.
- `Binary point scaling` — Enter the word length and the
  fraction length of the multiplicand, in bits.

#### Dependencies

This parameter is visible only when the **Filter structure** parameter
is set to `Direct form I transposed`.

### **Coefficients** — Coefficients data type `Same word length as input` (default) | `Specify word length` | `Binary point scaling`

Choose how you specify the word and fraction lengths of the filter coefficients
(numerator, denominator, and scale value) when **Coefficient source** is set
to `Dialog parameters`. See the Fixed-Point Data Types section for illustrations
depicting the use of the coefficient data types in this block. When you select:

- `Same word length as input` — Word length of the
  filter coefficients matches that of the input to the block. In this mode, the block
  automatically sets the fraction length of the coefficients to the binary point-only scaling
  that provides the best precision possible given the value and word length of the
  coefficients.
- `Specify word length` — Enter the word length of the
  coefficients, in bits. In this mode, the block automatically sets the fraction length of
  the coefficients to the binary point-only scaling that provides the best precision possible
  given the value and word length of the coefficients.
- `Binary point scaling` — Enter the word length and the
  fraction length of the coefficients, in bits. If applicable, enter separate fraction
  lengths for the numerator and denominator coefficients.

The filter coefficients do not obey the **Rounding mode** and the
**Overflow mode** parameters; instead, they are always saturated and
rounded to `Nearest`.

#### Dependencies

This parameter is visible only when **Coefficient source** is set to
`Dialog parameters`.

### **Product output** — Product output data type `Same as input` (default) | `Inherit via internal rule` | `Binary point scaling`

Specify how to designate the product output word and fraction lengths. See Multiplication Data Types and the Fixed-Point Data Types section for illustrations
depicting the use of the product output data type in this block. When you select:

- `Same as input` — Product output word length and
  fraction length characteristics match those of the input to the block.
- `Inherit via internal rule` — Product output word
  length and fraction lengths are computed based on full-precision rules. These rules prevent
  quantization from occurring within the block. Bits are added, as needed, so that no
  roundoff or overflow occurs. For more details, see Inherit via Internal Rule.
- `Binary point scaling` — Enter the word length and the
  fraction length of the product output, in bits. If applicable, enter separate fraction
  lengths for the numerator and denominator product output data type.

### **Accumulator** — Accumulator data type `Same as product output` (default) | `Same as input` | `Binary point scaling`

Specify how to designate the accumulator word and fraction lengths. See Multiplication Data Types and the Fixed-Point Data Types section for illustrations
depicting the use of the accumulator data type in this block. When you select:

- `Same as input` — Accumulator word and fraction length
  characteristics match those of the input to the block.
- `Same as product output` — Accumulator word and
  fraction length characteristics match those of the product output.
- `Binary point scaling` — Enter the word length and the
  fraction length of the accumulator, in bits. If applicable, enter separate fraction lengths
  for the numerator and denominator accumulator data type.

### **States** — States data type `Same as accumulator` (default) | `Same as input` | `Binary point scaling`

Specify how to designate the state word and fraction lengths when **Coefficient
source** is set to `Dialog parameters`. See the Fixed-Point Data Types section for illustrations
depicting the use of the state data type in this block.

When you select:

- `Same as input` — State word and fraction length
  characteristics match those of the input to the block.
- `Same as accumulator` — State word and fraction length
  characteristics match those of the accumulator.
- `Binary point scaling` — Enter the word length and the
  fraction length of the state, in bits. If applicable, enter separate fraction lengths for
  the numerator and denominator state data type.

#### Dependencies

This parameter is visible only when **Filter structure** is set to
`Direct form II` or `Direct form II
transposed`.

### **Output** — Output data type `Same as accumulator` (default) | `Same as input` | `Binary point scaling`

Choose how you specify the output word length and fraction length. See the Fixed-Point Data Types section for illustrations
depicting the use of the output data type in this block. When you select:

- `Same as input` — Output word and fraction length
  characteristics match those of the input to the block.
- `Same as accumulator` — Output word and fraction
  length characteristics match those of the accumulator.
- `Binary point scaling` — Enter the word length and the
  fraction length of the output, in bits.

### **Lock data type settings against changes by the fixed-point tools** — Lock data type settings `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify on the block mask.

## Libraries

DSP System Toolbox / Filtering / Filter Implementations DSP System Toolbox HDL Support / Filtering

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**Note**

For an HDL-optimized biquad filter architecture with hardware-friendly control signals,
use the Biquad Filter (DSP HDL Toolbox)
block. The DSP HDL Toolbox™ block simulates the latency of the HDL algorithm in Simulink. The DSP HDL Toolbox block generates a direct form II or direct form II transposed pipelined
add-multiply operation that fits into the DSP block on an FPGA. It provides an optional
pipelined feedback architecture that uses more multipliers but reduces the critical path and
achieves higher clock rates. The DSP HDL Toolbox block does not support programmable coefficients. To perform multichannel
filtering, put the DSP HDL Toolbox
Biquad Filter block into a For Each subsystem.

**HDL Architecture**

The block has `HDLDataPath` as a default architecture. This
architecture provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Block Properties**

| HDL Block Properties | Description |
| --- | --- |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **FlattenFilter** | Remove hierarchy of Filter subsystem from generated HDL code. The default is `auto`. See FlattenHierarchy (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming (HDL Coder). |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **MultiplerArchitecture** | Select the multipler architecture as `linear` or `shiftadd`. The default is `linear`. For more information, see HDL Code Generation section in Product, Matrix Multiply (Simulink). |
| **MultiplierInputPipeline** | Specify the number of pipeline stages to add at filter multiplier inputs. See also MultiplierInputPipeline (HDL Coder). |
| **MultiplierOutputPipeline** | Specify the number of pipeline stages to add at filter multiplier outputs. See also MultiplierOutputPipeline (HDL Coder). |
| **SectionOutputPipeline** | Specify the number of pipeline stages to add for section outputs. The default is `0`. |
| **AdderOutputPipeline** | Number of output pipeline stages to insert in the generated code for addition operation. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Enumerated | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes | Yes | Yes |

**Block Parameter Configuration**

These block parameter configurations are incompatible with HDL code generation.

| Block Parameter | Limitations |
| --- | --- |
| **Input processing** | Parameter value `Columns as channels (frame based)` is not supported. |

**Optimizations**

The block participates in these HDL optimizations to optimize the speed, and area.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* optimization creates patterns or combination of blocks with registers that can improve the achievable clock frequency and reduce the area usage on the FPGA boards by inserting pipeline registers to the blocks in your design. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**Limitations and Considerations**

The block has these limitations:

- Frame input is not supported for HDL code generation. For frame-based input, use the
  Biquad Filter (DSP HDL Toolbox)
  block.
- You must set **Initial conditions** to `0`. HDL code
  generation is not supported for nonzero initial states.
- You must select **Optimize unity scale values**.

To configure the Biquad Filter block as a programmable filter or a
multichannel filter, use the following block settings:

| Filter Case | Considerations |
| --- | --- |
| **Programmable Filter** | HDL Coder supports programmable filters for Biquad Filter blocks.  1. On the filter block mask, set **Coefficient source** to    **Input port(s)**. 2. Connect vector signals to the **Num** and **Den**    coefficient ports. You must use one Biquad Filter block for each    second-order section in your filter. For a filter with *M* second-order    sections, use a series of *M*    Biquad Filter blocks, each with an input **Num** that is    a 3-by-1 vector and an input **Den** that is a 2-by-1 vector. |
| **Multichannel Filter** | HDL Coder supports the use of vector inputs to Biquad Filter blocks.  1. Connect a vector signal to the Biquad Filter block input    port. 2. Specify **Input processing** as `Elements as channels    (sample based)`. 3. To reduce area by sharing the filter kernel between channels, set the    **StreamingFactor** parameter of the block to the number of    channels. |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2008b**

## Description

Model biquadratic IIR (SOS) filters

The Biquad Filter block independently filters each channel of the input
signal with the specified biquadratic infinite impulse response (IIR) filter. When you specify
the filter coefficients in the dialog box, the block implements static filters with fixed
coefficients. When you provide the filter coefficients through an input port, you can tune the
coefficients during simulation.

The Biquad Filter block supports the Simulink® state logging feature. See State (Simulink) for more information.

**Note**

Both the Biquad Filter and the Second-Order Section
Filter blocks implement a cascade of second-order section filters in Simulink. However, they differ in a few aspects such as the filter tunability and support
for fixed-point signals.

If the input signal is of `single` or `double` data type,
use the Second-Order Section Filter block because it has several advantages over
the Biquad Filter block. If the input signal is of built-in integer or
fixed-point arithmetic, use the Biquad Filter block. You can customize the
Biquad Filter block for fixed-point arithmetic operations.

For more information on key differences between the two blocks, see Difference Between Biquad Filter and Second-Order Section Filter Blocks.
