---
type: simulink-block
title: 'FIR Decimation'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'firdecimation'
documentation_source_path: 'ref/firdecimation.html'
language: en
---

# FIR Decimation

## Ports

### Input

### **In** — Data input vector | matrix

Specify the data input as a vector or a matrix of size
*P*-by-*Q*. The columns in the
input signal represent *Q* independent channels.

The block supports variable-size input signals (frame length changes during simulation)
when you set **Input processing** to
`Columns as channels (frame based)` and
**Rate options** to `Enforce
single-rate processing`. When the block accepts
variable-size input signals, they can be of arbitrary frame length, that
is, the input frame length does not have to be a multiple of the
decimation factor. When you specify fixed-size signals, the frame length
can be arbitrary under certain conditions. For more details, see Frame-Based Processing and Sample-Based Processing.

This port is unnamed until you set **Coefficient
source** to **Input port**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

### **Num** — Numerator coefficients vector

Specify the numerator coefficients of the FIR filter as a
vector.

The transfer function *H*(*z*) of
the FIR filter is given by:

H(z)=b0+b1z−1+...+bNz−N,

You can generate the FIR filter coefficient vector, **b** =
[*b0*,
*b1*, …,
*bN*], using one of
the DSP System Toolbox™ filter design functions such as `designMultirateFIR`,
`firnyquist`, `firgr`, or `firceqrip`.

To act as an effective anti-aliasing filter, the coefficients usually
correspond to a lowpass filter with a normalized cutoff frequency no
greater than 1/*M*, where *M* is the decimation factor.
To design such a filter, use the `designMultirateFIR`
function.

Coefficient values obtained through **Num** are tunable, that is, they
can change during simulation, while their properties must remain
constant.

The data type of the **Num** input must match the
data type of the **In** input.

#### Dependencies

The **Num** input port appears when you set
**Coefficient source** as **Input
port**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Out** — Decimator output vector | matrix

Output of the FIR Decimator block, returned as a vector or a
matrix.

When you set **Rate options** to:

- `Enforce single-rate processing`
  –– The block maintains the input sample rate and decimates
  the signal by decreasing the output frame size by a factor
  of *M*.

  The output has an upper bound size of
  `ceil`(*P*/*M*)-by-*Q*
  for an input of size
  *P*-by-*Q*.
- `Allow multirate processing` ––
  The block decimates the signal such that the output sample
  rate is *M* times slower than the input
  sample rate.

  The output frame size is the same as the input frame
  size.

For more details, see Frame-Based Processing and Sample-Based Processing.

This port is unnamed until you set **Coefficient
source** to **Input port**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

#### Coefficient source

### **Coefficient source** — FIR filter coefficient source **Auto** (default) | **Dialog parameters** | **Input port** | **Filter object**

Specify the FIR filter coefficient source as one of the following:

- **Dialog parameters** –– Specify the filter
  coefficients through the **FIR filter
  coefficients** parameter in the block dialog
  box.
- **Input port** –– Specify the filter
  coefficients through the **Num** input
  port.
- **Filter object** –– Specify the filter using
  a `dsp.FIRDecimator`
  System object™.
- **Auto** –– When you select
  **Auto**, the block designs an FIR
  decimator using the decimation factor that you specify in
  **Decimation factor**. The `designMultirateFIR`
  function designs the filter and returns the coefficients used by
  the block.

  For more information on the filter design, see Orfanidis [2].

#### Main Tab

### **FIR filter coefficients** — Lowpass FIR filter coefficients `designMultirateFIR(1,2)` (default) | vector

Specify the lowpass FIR filter coefficients, in descending powers of
*z*, as a vector. By default,
`designMultirateFIR(1,2)` computes the filter
coefficients.

The transfer function *H*(*z*) of the
FIR filter is given by:

H(z)=b0+b1z−1+...+bNz−N,

You can generate the FIR filter coefficient vector, **b** =
[*b0*,
*b1*, …,
*bN*], using one of the
DSP System Toolbox filter design functions such as `designMultirateFIR`, `firnyquist`, `firgr`, or `firceqrip`.

To act as an effective anti-aliasing filter, the coefficients usually
correspond to a lowpass filter with a normalized cutoff frequency no greater
than 1/*M*, where *M* is the decimation factor. To
design such a filter, use the `designMultirateFIR`
function.

The block internally initializes all filter states to zero.

#### Dependencies

This parameter appears only when you set the **Coefficient
source** to **Dialog parameters**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**Complex Number Support:** Yes

### **Decimation factor** — Decimation factor `2` (default) | positive scalar

Specify the integer factor *M*. The block decreases the
sample rate of the input sequence by this factor.

#### Dependencies

This parameter appears only when you set the **Coefficient
source** to **Dialog parameters**,
**Input port**, or
**Auto**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Filter structure** — FIR filter structure `Direct form` (default) | `Direct form transposed`

Specify the FIR filter structure as either `Direct
form` or `Direct form
transposed`.

#### Dependencies

This parameter appears only when you set the **Coefficient
source** to **Dialog parameters**,
**Input port**, or
**Auto**.

### **Filter object** — Filter object `dsp.FIRDecimator`

Specify the name of the multirate filter object that you want the block to
implement. You must specify the filter as a `dsp.FIRDecimator`
System object.

You can define the System object directly in the block dialog box. Alternatively, you can
define the object in a MATLAB® workspace variable and specify the variable in the block
dialog box.

For information on creating System objects, see Define Basic System Objects.

#### Dependencies

This parameter appears only when you set the **Coefficient
source** to **Filter object**.

### **Input processing** — Method to process input signals `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block should process the input. You can set this parameter
to one of the following options:

- `Columns as channels (frame based)`
  — When you select this option, the block treats each column
  of the input as a separate channel.
- `Elements as channels (sample based)`
  — When you select this option, the block treats each element
  of the input as a separate channel.

### **Rate options** — Method by which block decimates input `Enforce single-rate processing` (default) | `Allow multirate processing`

Specify the method by which the block should decimate the input. You can
select one of the following options:

- `Enforce single-rate processing`
  — When you select this option, the block maintains the
  input sample rate and decimates the signal by decreasing the
  output frame size by a factor of *M*. To select
  this option, you must set the **Input
  processing** parameter to `Columns as
  channels (frame based)`.

  When you set the **Rate options** parameter
  to `Enforce single-rate processing`,
  you can use the FIR Decimation block inside
  triggered subsystems.
- `Allow multirate processing` —
  When you select this option, the block decimates the signal such
  that the output sample rate is *M* times slower
  than the input sample rate.

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals off (default) | on

Specify whether fixed-size input signals (whose size does not change during simulation)
can have an arbitrary frame length, where the frame length does not have to
be a multiple of the decimation factor. The block uses this parameter
setting only for fixed-size input signals and ignores this parameter if the
input has a variable-size.

When the input signal is a variable-size signal, the signal can have arbitrary frame
length, that is, the frame length does not have to be a multiple of the
decimation factor.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the frame
  length of the signal does not have to be a multiple of the
  decimation factor. If the input is not a multiple of the
  decimation factor, then the output is generally a variable-size
  signal. Therefore, to support arbitrary input size, the block
  must also support variable-size operations, which you can enable
  by selecting the **Allow arbitrary frame length for
  fixed-size input signals** parameter.
- Clear the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the input
  frame length must be a multiple of the decimation factor.

#### Dependency

To enable this parameter, set **Input processing** to
`Columns as channels (frame based)` and
**Rate options** to `Enforce
single-rate processing`.

### **Output buffer initial conditions** — Initial conditions `0` (default) | scalar | matrix

When you set the FIR Decimation block to the frame-based
processing mode, the block can exhibit one-frame latency. In the case of
one-frame latency, this parameter specifies the output of the block until
the first filtered input sample is available. Specify this parameter as a
scalar value to be applied to all signal channels, or as a matrix containing
one value for each channel.

Cases of one-frame latency can occur when the input frame size is greater
than one, and you set the **Input processing** and
**Rate options** parameters of the FIR
Decimation block as follows:

- **Input processing** set to `Columns
  as channels (frame based)`
- **Rate options** set to `Allow
  multirate processing`

For more information on latency in the FIR Decimation
block, see Latency.

#### Dependencies

This parameter appears only when you configure the block to perform
multirate processing by setting **Rate options** to
`Allow multirate processing`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**Complex Number Support:** Yes

### **View Filter Response** — View filter response button

Click on this button to open the Filter Visualization Tool (`fvtool`) and display the filter response of the filter
defined in the block dialog box.

#### Data Types Tab

### **Rounding mode** — Rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding
mode for fixed-point operations. The default is
`Floor`. The filter coefficients do not obey
this parameter and always round to
`Nearest`.

**Note**

The **Rounding mode** and **Saturate on
integer overflow** settings have no effect on numerical
results when all the following conditions exist:

- **Product output** is
  `Inherit: Inherit via internal
  rule`
- **Accumulator** is `Inherit:
  Inherit via internal rule`
- **Output** is `Inherit: Same
  as accumulator`

With these data type settings, the block is effectively operating in
the full-precision mode.

### **Saturate on integer overflow** — Saturate on integer overflow `off` (default) | `on`

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps the
result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

**Note**

The **Rounding mode** and **Saturate on
integer overflow** parameters have no effect on numeric
results when all these conditions are met:

- **Product output** data type is
  `Inherit: Inherit via internal
  rule`.
- **Accumulator** data type is
  `Inherit: Inherit via internal
  rule`.

With these data type settings, the block operates in full-precision
mode.

### **Coefficients Data Type** — Coefficients data type `Inherit: Same word length as input` (default) | `fixdt(1,16)` | `fixdt(1,16,0)`

Specify the coefficients data type. See Fixed-Point Data Types and Multiplication Data Types for
illustrations depicting the use of the coefficients data type in this block.

You can set this parameter to one of the following:

- `Inherit: Same word length as
  input`
- `fixdt(1,16,0)` or
  `fixdt(1,16)` –– Specify a data type
  object.

Click the **Show data type assistant** button
Double greater than symbols to display the **Data Type
Assistant**, which helps you set the
**Coefficients** parameter.

See Specify Data Types Using Data Type Assistant (Simulink)
for more information.

#### Dependencies

This parameter appears only when you set **Coefficient
source** to `Dialog parameters`,
`Filter object`, or
`Auto`.

When **Coefficient source** is set to
`Filter object`,
**Coefficients** parameter is automatically set to
`Same word length as input`.

### **Coefficients Minimum** — Minimum value of filter coefficients `[]` (default) | scalar

Specify the minimum value of the filter coefficients. The default value is
`[]` (unspecified). Simulink® software uses this value to perform automatic scaling of
fixed-point data types.

#### Dependencies

This parameter appears only when you set **Coefficient
source** to `Dialog parameters` or
`Auto`.

### **Coefficients Maximum** — Maximum value of filter coefficients `[]` (default) | scalar

Specify the maximum value of the filter coefficients. The default value is
`[]` (unspecified). Simulink software uses this value to perform automatic scaling of
fixed-point data types.

#### Dependencies

This parameter appears only when you set **Coefficient
source** to `Dialog parameters` or
`Auto`.

### **Product output Data Type** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt(1,16,0)`

Specify the product output data type. See Fixed-Point Data Types and Multiplication Data Types for
illustrations depicting the use of the product output data type in this
block.

You can set this parameter to one of the following:

- `Inherit: Inherit via internal
  rule`

  For more information on this rule, see Inherit via Internal Rule.
- `Inherit: Same as input`
- `fixdt(1,16,0)` –– Specify a data type
  object.

Click the **Show data type assistant** button
Double greater than symbols to display the **Data Type
Assistant**, which helps you set the **Product
output** parameter.

See Specify Data Types Using Data Type Assistant (Simulink)
for more information.

#### Dependencies

When **Coefficient source** is set to
`Filter object`, **Product
output** parameter is automatically set to `Full
precision`.

### **Accumulator Data Type** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

Specify the accumulator data type. See Fixed-Point Data Types for
illustrations depicting the use of the accumulator data type in this block.

You can set this parameter to one of the following:

- `Inherit: Inherit via internal rule`.

  For more information on this rule, see Inherit via Internal Rule.
- `Inherit: Same as input`
- `Inherit: Same as product output`
- `fixdt(1,16,0)` –– Specify a data type
  object.

Click the **Show data type assistant** button
Double greater than symbols to display the **Data Type
Assistant**, which helps you set the
**Accumulator** parameter.

See Specify Data Types Using Data Type Assistant (Simulink)
for more information.

#### Dependencies

When **Coefficient source** is set to
`Filter object`,
**Accumulator** parameter is automatically set to
`Full precision`.

### **Output Data Type** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

Specify the output data type. See Fixed-Point Data Types for
illustrations depicting the use of the output data type in this block.

You can set it to one of the following:

- `Inherit: Same as accumulator`
- `Inherit: Same as input`
- `Inherit: Same as product output`
- `fixdt(1,16,0)` –– Specify a data type
  object.

Click the **Show data type assistant** button
Double greater than symbols to display the **Data Type
Assistant**, which helps you set the
**Output** parameter.

See Control Data Types of Signals (Simulink) for more information.

#### Dependencies

When **Coefficient source** is set to
`Filter object`,
**Output** parameter is automatically set to
`Same as accumulator`.

### **Output Minimum** — Minimum value of block output `[]` (default) | scalar

Specify the minimum value that the block should output. The default value
is `[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

#### Dependencies

This parameter appears only when you set **Coefficient
source** to `Dialog parameters`,
`Input port`, or
`Auto`.

### **Output Maximum** — Maximum value of block output `[]` (default) | scalar

Specify the maximum value that the block should output. The default value
is `[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

#### Dependencies

This parameter appears only when you set **Coefficient
source** to `Dialog parameters`,
`Input port`, or
`Auto`.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.

## Libraries

DSP System Toolbox / Filtering / Multirate Filters DSP System Toolbox HDL Support / Filtering

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

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

**Generate SIMD code using Intel® AVX2 code replacement library**

**Note**

Requires Embedded Coder® license

The FIR Decimation block supports SIMD code generation using Intel AVX2 code replacement library under these conditions:

- **Filter structure** is set to `Direct
  form`.
- **Input processing** is set to `Columns
  as channels (frame based)`.
- **Rate options** is set to `Enforce
  single-rate processing`.
- Clear the **Allow arbitrary frame length for fixed-size input
  signals** parameter.
- Input signal is real-valued with real filter coefficients.
- Input signal is complex-valued with real or complex filter
  coefficients.
- Input signal has a data type of `single` or
  `double`.

To generate SIMD code from this block using this workflow, see Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks.

**Generate SIMD code by
leveraging target hardware instruction set extensions** *(since R2023a)*

**Note**

Requires Simulink
Coder™ or Embedded Coder license

You can generate SIMD code for the FIR Decimation block on all Intel platforms, ARM®
Cortex®-A processors, and Apple silicon processors by using the model configuration parameter
**Leverage target hardware instruction set extensions** under
these conditions:

- You set **Filter structure** to `Direct
  form` for the FIR Decimation
  block
- You set **Input processing** to `Columns
  as channels (frame based)`
- Input signal is real-valued with real filter coefficients
- Input signal is complex-valued with real or complex filter
  coefficients.
- Data type of the input signal is `single`
  (ARM
  Cortex-A processors)
- Data type of the input signal is `single` or
  `double` (Intel platforms)

In addition, configure your model appropriately. In the
**Modeling** tab of the Simulink model window, click **Model Settings** and configure
these parameters under **Code Generation**.

- In the **Optimization** pane:

  - Provide a specific instruction set in the
    **Leverage target hardware instruction set
    extensions** parameter.
  - Select the **Optimize reductions**
    parameter.
  - Under **Optimization levels**, set
    **Level** to
    `Maximum` and
    **Priority** to `Maximize
    execution speed`.
- In the **Interface** pane, under **Software
  environment**, clear **non-finite
  numbers**.

To generate SIMD code from this block using this workflow, see Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Intel Platforms, Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon, and Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for ARM Cortex-A Processors.

For computationally intensive operations on supported blocks, SIMD intrinsics can
significantly improve the performance of the generated code on Intel platforms. For
more details, see Optimize Code for Reduction Operations by Using SIMD (Simulink Coder).

For more information on SIMD code generation in DSP System Toolbox, see SIMD Code Generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**Note**

For a FIR decimation filter with hardware-friendly control signals and
simulation of HDL latency in Simulink, or for complex data with complex coefficients, use the FIR
Decimator (DSP HDL Toolbox) block instead of this block.

**HDL Architecture**

The block has `HDLDataPath` as a default
architecture. This architecture provides additional configuration options that
affect HDL implementation and synthesized logic.

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
| **AdderChainArchitecture** | Select the adder architecture to generate linear chain or tree structure of adders to compute sum of elements. The default is `tree`. For more information, see HDL Code Generation section in Sum (Simulink). |
| **AdderOutputPipeline** | Number of output pipeline stages to insert in the generated code for addition operation. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Enumerated | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes | Yes | Yes |

**Optimizations**

The block participates in these HDL optimizations to optimize the speed, and
area.

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

- You must set **Initial conditions** to zero. HDL code
  generation is not supported for nonzero initial states.
- When you select **Dialog parameters**, the following
  fixed-point options are not supported for HDL code generation:

  - `Slope and Bias scaling`
- Programmable coefficients are not supported.
- Frame-based input filters are not supported for:

  - Resettable and enabled subsystems
  - Complex input signals with complex coefficients. You can use
    either complex input signals and real coefficients, or complex
    coefficients and real input signals.
  - Sharing and streaming optimizations

To configure the FIR Decimation block for a frame-based input,
use the following block settings:

|  |  |
| --- | --- |
| **Frame-based input** | HDL Coder supports the use of vector inputs to FIR Decimation blocks, where each element of the vector represents a sample in time. You can use an input vector of up to 512 samples. The frame-based implementation supports fixed-point input and output data types, and uses full-precision internal data types. The output is a column vector of reduced size, corresponding to your decimation factor. You can use real input signals with real coefficients, complex input signals with real coefficients, or real input signals with complex coefficients.  1. Connect a column vector signal to the FIR    Decimation block input port. 2. Specify **Input processing** as    `Columns as channels (frame    based)`. 3. Set **Rate options** to    `Enforce single-rate    processing`. |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024b: Generate SIMD code for Apple silicon processors

In R2024b, if you have Embedded Coder, you can generate SIMD code for the FIR Decimation
block for Apple silicon processors by using the model configuration parameter
**Leverage target hardware instruction set extensions**. For
more information, see Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon.

### R2024a: Generate SIMD code for ARM Cortex-A processors

In R2024a, if you have Embedded Coder, you can generate SIMD code for the FIR Decimation
block for ARM
Cortex-A processors by using the model configuration parameter
**Leverage target hardware instruction set extensions**.

### R2023b: Generate SIMD Code for Complex Signals

In R2023b, if you have Embedded Coder, you can generate SIMD code for the FIR Decimation
block when the input signal is complex-valued by using the model configuration
parameter **Leverage target hardware instruction set
extensions**.

### R2023a: Generate SIMD code for FIR Decimation block on all Intel platforms

In R2023a, if you have Embedded Coder, you can generate SIMD code for the FIR Decimation
block on all Intel platforms by using the model configuration parameter
**Leverage target hardware instruction set extensions**.
Previously, you had to use a code replacement library to generate SIMD code. For
more details, see Code Generation.

### R2022b: Support for arbitrary input frame length

Starting in R2022b, this block supports input signals with arbitrary frame lengths when the:

- Input signal is a fixed-size signal (frame length does not change
  during simulation) and the block allows for multirate processing
- Input signal is a fixed-size signal, the block enforces single-rate
  processing, and you select the **Allow arbitrary frame length
  for fixed-size input signals** parameter
- Input signal is a variable-size signal (frame length changes during
  simulation)

When this block supports an arbitrary frame length input signal, the input frame
length does not have to be a multiple of the decimation factor.

For more details, see Frame-Based Processing and Sample-Based Processing.

## Description

Perform polyphase FIR decimation

The FIR Decimation block performs an efficient polyphase decimation using an
integer downsampling factor *M* along the first dimension.

Conceptually, the FIR decimator (as shown in the schematic) consists of an
anti-aliasing FIR filter followed by a downsampler. To design an FIR anti-aliasing
filter, use the `designMultirateFIR` function.

The FIR filter filters the data in each channel of the input using a direct-form FIR filter.
The downsampler that follows downsamples each channel of filtered data by taking every
*M*-th sample and discarding the *M* – 1 samples that follow. *M* is the value of the
decimation factor that you specify. The resulting discrete-time signal has a sample rate
that is 1/*M* times the original sample rate.

FIR decimator contains an anti-aliasing FIR filter followed by a downsampler.

Note that the actual block algorithm implements a direct-form FIR polyphase structure, an
efficient equivalent of the combined system depicted in the diagram. For more details,
see Algorithms.

Under specific conditions, this block also supports SIMD code generation. For details,
see Code Generation.
