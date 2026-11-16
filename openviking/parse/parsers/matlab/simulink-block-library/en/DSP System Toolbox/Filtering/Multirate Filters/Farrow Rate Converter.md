---
type: simulink-block
title: 'Farrow Rate Converter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'farrowrateconverter'
documentation_source_path: 'ref/farrowrateconverter.html'
language: en
---

# Farrow Rate Converter

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Specify the input signal as a real or a complex-valued scalar, vector,
or a matrix signal.

The block treats each column of the input signal as a separate channel. If the input is
a two-dimensional signal, the first dimension represents the channel
length (or frame size) and the second dimension represents the number of
channels. If the input is a one-dimensional signal, then the block
interprets it as a single-channel signal.

When you input a variable-size signal (frame length changes during simulation), the
frame length of the signal can be arbitrary, that is, the input frame
length does not have to be a multiple of the decimation factor. When you
input a fixed-size signal (frame length does not change during
simulation), the frame length can be arbitrary only when you select the
**Allow arbitrary frame length for fixed-size input
signals** parameter.

To determine the decimation factor, click the **View Info** button in
the block dialog.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Rate converted signal scalar | vector | matrix

The Farrow Rate Converter block outputs a signal that has the same data
type and complexity as the input signal.

The output signal dimensions depend on the input signal dimensions, the overall
interpolation and decimation factors of the Farrow Rate
Converter block, and whether you select the **Allow
arbitrary frame length for fixed-size input signals**
parameter. You can determine the overall interpolation factor
*L* and the decimator factor *M*
by clicking the **View Info** button in the block
dialog box.

This table provides more details on the dimensions of the output signal when you input a
fixed-size input signal.

**Fixed-Size Input Signal**

| Input Signal | Output Signal Dimensions |
| --- | --- |
| *P*-by-1 column vector, where *P* is a multiple of the decimation factor *M* | (*LP*/*M*)-by-1, where *L* is the interpolation factor |
| *P*-by-1 column vector, where *P* is not a multiple of the decimation factor *M* | `ceil`(*LP*/*M*)-by-1 when you select **Allow arbitrary frame length for fixed-size input signals**.  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. |
| *P*-by-*Q* matrix, where *P* is a multiple of the decimation factor *M* | (*LP*/*M*)-by-*Q* |
| *P*-by-*Q* matrix, where *P* is not a multiple of the decimation factor *M* | `ceil`(*LP*/*M*)-by-*Q* when you select **Allow arbitrary frame length for fixed-size input signals**.  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. |

This table gives more details on the dimensions of the output signal when you input a
variable-size input signal. When you input a variable-size signal (frame
length changes during simulation), the **Allow
arbitrary frame length for fixed-size input signals**
appears on the block dialog box but does not have any impact on the
input frame length. You can input a variable-size signal of any frame
length even if you do not select the **Allow
arbitrary frame length for fixed-size input signals**
parameter.

**Variable-Size Input Signal**

| Input Signal | Output Signal Dimensions |
| --- | --- |
| *P*-by-*Q* | `ceil`(*LP*/*M*)-by-*Q* |

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Sample rate of input signal (Hz)** — Sample rate of input signal in Hz `48e3` (default) | positive scalar

Specify the sample rate of the input signal as a positive scalar in
Hz. The input sample rate must be greater than the bandwidth of
interest.

### **Sample rate of output signal (Hz)** — Sample rate of output signal in Hz `96e3` (default) | positive scalar in Hz

Specify the sample rate of the output signal as a positive scalar in
Hz. The output sample rate must be higher or lower than the input sample
rate.

### **Tolerance for output sample rate** — Maximum tolerance for output sample rate `0` (default) | positive scalar

Specify the maximum tolerance for the output sample rate as a positive scalar in the
range [`0``0.5`].

The actual output sample rate varies but is within the specified range. For example, if
you set the **Tolerance for output sample rate** to
0.01, then the actual output sample rate is in the range given by sample
rate of output signal ± 1%. This flexibility allows for a
simpler filter design.

### **Filter Specification method** — Method for specifying filter coefficients `Polynomial order` (default) | `Coefficients`

Specify the method the block uses to determine the polynomial interpolator coefficients
as one of the following:

- `Polynomial order` —
  Specify the order of the Lagrange interpolation filter
  polynomial through the **Polynomial order**
  parameter.
- `Coefficients` — Specify
  the polynomial coefficients directly through the
  **Coefficients** parameter.

### **Coefficients** — Filter polynomial coefficients `[-1 1; 1 0]` (default) | real-valued square matrix

Specify the filter polynomial coefficients as a real-valued square
matrix.

#### Dependencies

To enable this parameter, set **Filter specification method** to
`Coefficients`.

### **Polynomial order** — Order of Lagrange-interpolation-filter polynomial `3` (default) | positive integer less than or equal to 4

Specify the order of the Lagrange-interpolation-filter polynomial as
`1`, `2`, `3`, or
`4`.

#### Dependencies

To enable this parameter, set **Filter specification method** to
`Polynomial order`.

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals on (default) | off

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

### **View Filter Response** — View filter response button

Opens the FVTool and displays the magnitude/phase response of the Farrow Rate
Converter. The response is based on the block parameters.
FVTool updates when you change the parameters.

To update the magnitude response while FVTool is running, modify the parameters in the
dialog box and click **Apply**.

### **View Info** — View info button

Click this button for the block to display the following information about the Farrow
filter system:

- `Filter Structure`
- `Interpolation Factor`
- `Decimation Factor`
- `Filter Length`
- `Stable`
- `Linear Phase`

This button brings the functionality of the `info` method into the
Simulink® environment.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

### Data Types Tab

### **Rounding mode** — Rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Specify the rounding mode for fixed-point operations as one of the following:

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

For more details, see rounding
mode.

### **Saturate on integer overflow** — Method of overflow action off (default) | on

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Coefficients** — Data type of filter coefficients `fixdt(1,16)` (default) | `fixdt(1,16,0)`

Specify the data type of the filter coefficients as a signed fixed-point object. The
default `fixdt(1,16)` corresponds to a signed
fixed-point type object with 16-bit coefficients. For maximum precision,
the block determines the fraction length based on the coefficient
values.

### **Fractional Delay** — Data type of fractional delay `fixdt(0,8)` (default) | `fixdt(0,16)`

Specify the data type of the fractional delay as an unsigned fixed-point object. The
default `fixdt(0,8)` corresponds to an unsigned
fixed-point data type object with 8-bit word length. For maximum
precision, the block computes the fractional length based on the
fractional delay values.

### **Multiplicand** — Data type of multiplicand `fixdt(1,16,13)` (default) | `fixdt(1,16,0)`

Specify the multiplicand data type as a signed fixed-point object. The
default `fixdt(1,16,13)` corresponds to a
signed fixed-point multiplicand data type with 16-bit word length and
13-bit fraction length.

### **Output** — Data type of output `Inherit: Same word length as input` (default) | `Inherit: Same as accumulator` | `fixdt(1,16)` | `fixdt(1,16,0)`

Specify the word length and fraction length of the output data type as
one of the following:

- `Inherit: Same word length as
  input` (default) — Output word
  length and fraction lengths are the same as the
  input.
- `Inherit: Same as accumulator`
  — Output word length and fraction lengths are the
  same as the accumulator.
- `fixdt(1,16)` — Signed
  fixed-point data type with 16-bit word length. For maximum
  precision, the block computes the fraction length based on
  the input range and preserves the dynamic range of the
  input.
- `fixdt(1,16,0)` — Signed
  fixed-point data type with 16-bit word length and zero
  fraction length.

### **Output Minimum** — Minimum value that the block can output `[]` (default) | scalar

Specify the minimum value that the block can output. Simulink software uses this minimum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum value that the block can output `[]` (default) | scalar

Specify the maximum value that the block can output. Simulink software uses this maximum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.

## Libraries

DSP System Toolbox / Signal Operations DSP System Toolbox / Filtering / Multirate Filters

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

## Version History

**Introduced in R2015b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2022b: Support for arbitrary input frame length

Starting in R2022b, this block supports input signals with arbitrary frame lengths when the:

- Input signal is a fixed-size signal (frame length does not change
  during simulation) and you select the **Allow arbitrary frame
  length for fixed-size input signals** parameter
- Input signal is a variable-size signal (frame length changes during
  simulation)

When this block supports an arbitrary frame length input signal, the input frame
length does not have to be a multiple of the decimation factor.

## Description

Polynomial sample-rate converter with arbitrary conversion factor

The Farrow Rate Converter block converts the sample rate of an input signal
using polynomial-fit sample-rate conversion. Polynomial-based filters are efficient at
implementing fractional sample rate conversion. Farrow structures are implementations of
polynomial-based filters. This block uses a Farrow structure to implement arbitrary
rate-change factors efficiently. The rate-change factors can be irrational.
