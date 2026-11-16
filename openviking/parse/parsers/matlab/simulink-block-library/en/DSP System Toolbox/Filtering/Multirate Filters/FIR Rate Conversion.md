---
type: simulink-block
title: 'FIR Rate Conversion'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'firrateconversion'
documentation_source_path: 'ref/firrateconversion.html'
language: en
---

# FIR Rate Conversion

## Ports

### Input

### **Port\_1(In1)** — Input signal vector | matrix

Specify the input signal as a vector or a matrix of size
*P*-by-*Q*. The input columns
represent the *Q* independent channels.

The block supports variable-size input signals (frame length changes during simulation)
when you set **Rate options** to `Enforce
single-rate processing`. When the block accepts
variable-size input signals, they can be of arbitrary frame length, that
is, the input frame length does not have to be a multiple of the
decimation factor. For fixed-size signals, the frame length can be
arbitrary under certain conditions. For more details, see Frame-Based Processing.

When the block input is fixed point, all internal data types are
signed fixed point.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1(Out1)** — Rate converted signal vector | matrix

Rate converted signal, returned as a vector or a matrix.

When you set the **Rate options** parameter to:

- `Enforce single-rate processing`
  –– The block maintains the input sample rate and resamples
  the signal by changing the output frame size by a factor of
  *L*/*M*.

  The output has an upper bound size of
  `ceil`(*LP*/*M*)-by-*Q*
  for an input of size
  *P*-by-*Q*.
- `Allow multirate processing` ––
  The block decimates the signal such that the output signal
  sample rate is *L*/*M*
  times the input sample rate.

  The output frame size is the same as the input frame size,
  *Fo* =
  (*L*/*M*)×*Fi*

  All blocks connected to the output operate at
  *Fo*, and
  all blocks connected to the input operate at
  *Fi*.

  For more details, see Frame-Based Processing.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Coefficient source** — Mode of operation **Auto** (default) | **Dialog parameters** | **Filter object**

The FIR Rate Conversion block can operate in three different modes. Select
the mode in the **Coefficient source** group box.

- **Dialog parameters** — Enter information
  about the filter, such as FIR filter coefficients in the block
  dialog box.
- **Filter object** — Specify the filter
  using a `dsp.FIRRateConverter`
  System object™.
- **Auto** (default) — The block determines
  the filter coefficients.

The settings in the FIR Rate Conversion block dialog box
change based on the mode selected.

### Main Tab

### **Interpolation factor** — Interpolation factor `3` (default) | positive integer

Specify the interpolation factor, *L*, as a positive
integer. The block upsamples the signal by this value before filtering
it.

#### Dependencies

To enable this parameter, set **Coefficient
source** to either **Dialog
parameters** or **Auto**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **FIR filter coefficients** — FIR filter coefficients `designMultirateFIR(3,2)` (default) | vector

Specify the FIR filter coefficients in descending powers of
*z*. By default, the block uses the
`designMultirateFIR(3,2)` function to compute the
filter coefficients.

#### Dependencies

To enable this parameter, set **Coefficient
source** to **Dialog
parameters**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**Complex Number Support:** Yes

### **Decimation factor** — Decimation factor `2` (default) | positive integer

Specify the decimation factor, *M*, as a positive
integer. The block downsamples the signal by this value after filtering
it.

#### Dependencies

To enable this parameter, set **Coefficient
source** to either **Dialog
parameters** or **Auto**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Rate options** — Enforce single-rate or allow multirate processing `Enforce single-rate processing` (default) | `Allow multirate processing`

Specify whether to enforce single-rate processing or allow multirate processing.

- `Enforce single-rate processing`
  –– The output frame size
  *Po* is
  *L*/*M* times the
  input frame size
  *Pi*, where
  *L* is the interpolation factor and
  *M* is the decimation factor.

  *Po* =
  (*L*/*M*)×*Pi*

  The output signal rate in Simulink® equals the input signal rate.

  *Fo* =
  *Fi*
- `Allow multirate processing` ––
  The output frame size equals the input frame size.

  *Po* =
  *Pi*

  The output signal rate in Simulink is *L*/*M*
  times the input signal rate.

  *Fo* =
  (*L*/*M*)×*Fi*

  All blocks connected to the output operate at
  *Fo*, and
  all blocks connected to the input operate at
  *Fi*.

### **Filter object** — Filter object `FRC` (default) | `dsp.FIRRateConverter` System object

Specify the multirate filter object that you want the block to
implement. The specified filter object must be a `dsp.FIRRateConverter`
System object.

You can define the System object in the block mask or in a MATLAB® workspace variable.

For information on creating System objects, see Define Basic System Objects.

#### Dependencies

This parameter appears when **Coefficient
source** is set to **Filter
object**.

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals off (default) | on

Specify whether fixed-size input signals (whose size does not change during simulation)
can have an arbitrary frame length, where the frame length does not have
to be a multiple of the decimation factor. The block uses this parameter
setting only for fixed-size input signals and ignores this parameter if
the input has a variable-size.

When the input signal is a variable-size signal, the signal can have
arbitrary frame length, that is, the frame length does not have to be a
multiple of the decimation factor.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the frame
  length of the signal does not have to be a multiple of the
  decimation factor. If the input is not a multiple of the
  decimation factor, then the output is generally a
  variable-size signal. Therefore, to support arbitrary input
  size, the block must also support variable-size operations,
  which you can enable by selecting the **Allow
  arbitrary frame length for fixed-size input
  signals** parameter.
- Clear the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the input
  frame length must be a multiple of the decimation
  factor.

#### Dependency

To enable this parameter, set **Rate options** to
`Enforce single-rate
processing`.

### **View Filter Response** — Visualize filter response button

Select this parameter to open the Filter Visualization Tool, `fvtool`, and display the magnitude response of the FIR
filter. The response is based on the parameters selected in the block
dialog box. Changes made to these parameters update
`fvtool`.

To update the magnitude response while `fvtool` is
running, modify the block parameters and click
**Apply**.

To view the magnitude response and phase response simultaneously,
click the **Magnitude and Phase responses** button on
the toolbar.

### Data Types Tab

When **Coefficient source** is set to **Filter object**,
the fixed-point settings of the filter object specified on the **Main
tab** are displayed on the **Data Types
tab**. You cannot change these settings directly on the block dialog
box. To change the fixed-point settings, you must edit the filter object.

For more information on System objects, see the What Are System Objects?.

When **Coefficient source** is set to **Auto**, the block
chooses the filter coefficients automatically. For more information on the filter
design algorithm that the block uses, see Specify FIR Filter Coefficients.

### **Rounding mode** — Rounding method `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations as:

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

For more details, see Rounding
Modes.

The filter coefficients do not obey this parameter and always round to
`Nearest`.

**Note**

The **Rounding mode** and **Saturate on
integer overflow** parameters have no effect on
numerical results when all these conditions are met:

- **Product output** data type is
  `Inherit: Inherit via internal
  rule`.
- **Accumulator** data type is
  `Inherit: Inherit via internal
  rule`.
- **Output** data type is
  `Inherit: Same as
  accumulator`.

With these data-type settings, the block operates in a
full-precision mode.

#### Dependencies

To enable this parameter, set **Coefficient
source** to either **Dialog
parameters** or **Auto**.

### **Saturate on integer overflow** — Overflow handling method off (default) | on

Select this parameter to saturate the result of the fixed-point
operation. Clear this parameter to wrap the result of the fixed-point
operation. For details on *saturate* and
*wrap*, see Overflow
Handling for fixed-point operations.

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

With these data-type settings, the block operates in a
full-precision mode.

#### Dependencies

This parameter is editable only when **Coefficient
source** is set to either **Dialog
parameters** or **Auto**.

### **Coefficients** — Coefficients data type `Inherit: Same word length as input` (default) | `fixdt(1,16)` | `fixdt(1,16,0)`

**Coefficients** specifies the data type of the
filter coefficients.

- `Inherit: Same word length as input`
  –– The block inherits the word length of the coefficients from
  the fixed-point input. The fraction length is determined based
  on the coefficient values in order to obtain the best possible
  precision.
- `fixdt(1,16)` –– The coefficients
  data type is a signed, binary-point, scaled, fixed-point data
  type with a word length of 16 bits.
- `fixdt(1,16,0)` –– The coefficients
  data type is a signed, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Coefficients** data
type by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button .

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

For a diagrammatic representation of how this block uses the filter coefficients data
type, see Fixed-Point Data Types.

#### Dependencies

This parameter is editable only when **Coefficient
source** is set to either **Dialog
parameters** or **Auto**.

### **Coefficients Minimum** — Minimum value of filter coefficients `[]` (default) | scalar

Specify the minimum value of the filter coefficients. Simulink uses this minimum value to perform automatic scaling of
fixed-point data types.

### **Coefficients Maximum** — Maximum value of filter coefficients `[]` (default) | scalar

Specify the maximum value of the filter coefficients. Simulink uses this maximum value to perform automatic scaling of
fixed-point data types.

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt(1,16,0)`

**Product output** specifies the data type of the output of a product
operation in the FIR Rate Conversion block.

- `Inherit: Inherit via internal rule`
  — The block inherits the product output data type based
  on an internal rule. For more information on this rule, see
  Inherit via Internal Rule.
- `Inherit: Same as input` — The
  block specifies the product output data type to be the same as
  the input data type.
- `fixdt(1,16,0)` — The block
  specifies a signed, binary-point, scaled, fixed-point data type
  with a word length of 16 bits and a fraction length of 0.

Alternatively, you can set the **Product output**
data type by using the **Data Type Assistant**. To use
the assistant, click the **Show data type assistant**
button .

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

For a diagrammatic representation of how this block uses the product output data type,
see Fixed-Point Data Types.

#### Dependencies

This parameter is editable only when **Coefficient
source** is set to either **Dialog
parameters** or **Auto**.

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

**Accumulator** specifies the data type of the output of an
accumulation operation in the FIR Rate Conversion block.
For illustrations on how this block uses the accumulator data type, see
Fixed-Point Data Types.

- `Inherit: Inherit via internal rule`
  — The block inherits the accumulator data type based on
  an internal rule. For more information on this rule, see Inherit via Internal Rule.
- `Inherit: Same as input` — The
  block specifies the accumulator data type to be the same as the
  input data type.
- `Inherit: Same as product output`
  — The block specifies the accumulator data type to be the
  same as the product output data type.
- `fixdt(1,16,0)` — The block
  specifies a signed, binary-point, scaled, fixed-point data type
  with a word length of 16 bits and a fraction length of 0.

Alternatively, you can set the **Accumulator** data
type by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant** button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

This parameter is editable only when **Coefficient
source** is set to either **Dialog
parameters** or **Auto**.

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

**Output** specifies the data type of the output of the FIR Rate
Conversion block.

- `Inherit: Same as input` — The
  block specifies the output data type to be the same as the input
  data type.
- `Inherit: Same as product output`
  — The block specifies the output data type to be the same
  as the product output data type.
- `Inherit: Same as accumulator`
  — The block specifies the output data type to be the same
  as the accumulator data type.
- `fixdt(1,16,0)` — The block
  specifies a signed, binary-point, scaled, fixed-point data type
  with a word length of 16 bits and a fraction length of 0.

Alternatively, you can set the **Output** data type
by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button .

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

For a diagrammatic representation of how this block uses the output data type, see Fixed-Point Data Types.

#### Dependencies

This parameter is editable only when **Coefficient
source** is set to either **Dialog
parameters** or **Auto**.

### **Output Minimum** — Minimum value the block can output `[]` (default) | scalar

Specify the minimum value the block can output. Simulink uses this minimum value to perform:

- Simulation range checking. For more information, see Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum value block can output `[]` (default) | scalar

Specify the maximum value the block can output. Simulink uses this maximum value to perform:

- Simulation range checking. For more information, see Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding
the data types you specify on the block dialog box.

#### Dependencies

This parameter appears only when **Coefficient
source** is set to either **Dialog
parameters** or **Auto**.

## Libraries

DSP System Toolbox / Filtering / Multirate Filters

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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

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

For more details, see Frame-Based Processing.

## Description

Perform polyphase FIR sample rate conversion

The FIR Rate Conversion block performs an efficient polyphase sample rate conversion using a
rational factor *L*/*M* along the first dimension. The
block treats each column of the input as a separate channel and resamples the data in
each channel independently over time.

Conceptually, the rate converter combines an FIR interpolator followed by an FIR decimator.
The following schematic contains an upsampler, a combined anti-imaging and anti-aliasing
FIR filter, and a downsampler. To design an FIR filter which acts as a combined
anti-imaging and anti-aliasing FIR filter, use the `designMultirateFIR` function.

The rate converter does the following:

1. Upsamples the input to a higher rate by inserting
   *L*−`1` zeros between input
   samples.
2. Passes the upsampled data through an FIR filter.
3. Downsamples the filtered data to a lower rate by discarding
   *M*-`1` consecutive samples following each
   sample that the block retains.

FIR rate converter contains an upsampler followed by an anti-imaging, anti-aliasing FIR filter, followed by a downsampler.

Note that the actual block algorithm implements a polyphase structure, an efficient
equivalent of the combined system depicted in the diagram. For more details, see Algorithms.
