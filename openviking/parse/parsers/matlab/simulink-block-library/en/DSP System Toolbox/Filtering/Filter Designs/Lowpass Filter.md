---
type: simulink-block
title: 'Lowpass Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'lowpassfilter'
documentation_source_path: 'ref/lowpassfilter.html'
language: en
---

# Lowpass Filter

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal to filter column vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Filtered signal vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Input signal to filter column vector | matrix

Input signal, specified as a real- or complex-valued column vector or
matrix. If the input signal is a matrix, each column of the matrix is
treated as an independent channel. The number of rows in the input
signal denotes the channel length.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Filtered signal vector | matrix

Filtered signal, returned as a vector or matrix. The output has the
same size, data type, and complexity characteristics as the
input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Filter type
  summary: FIR or IIR filter FIR (default) | IIR
  group: Main
- name: Design minimum order filter
  summary: Design filter with minimum order on (default) | off
  group: Main
- name: Filter order
  summary: Order of lowpass filter 50 (default) | positive integer
  group: Main
- name: Passband edge frequency (Hz)
  summary: Passband edge frequency 8e3 (default) | real positive scalar
  group: Main
- name: Stopband edge frequency (Hz)
  summary: Stopband edge frequency 12e3 (default) | real positive scalar
  group: Main
- name: Maximum passband ripple (dB)
  summary: Maximum passband ripple 0.1 (default) | real positive scalar
  group: Main
- name: Minimum stopband attenuation (dB)
  summary: Minimum stopband attenuation 80 (default) | real positive scalar
  group: Main
- name: Sample rate mode
  summary: Mode to specify the input sample rate Use normalized frequency (0 to 1) (default) | Specify on dialog | Inherit
    from input port
  group: Main
- name: Input sample rate (Hz)
  summary: Input sample rate 44100 (default) | scalar
  group: Main
- name: View Filter Response
  summary: Open Filter Visualization Tool button
  group: Main
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: Main
- name: Rounding mode
  summary: Rounding method Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types
- name: Coefficients
  summary: Coefficient data type fixdt(1,16) (default) | fixdt(1,16,0) | <data type expression>
  group: Data Types
```

### Main

### **Filter type** — FIR or IIR filter `FIR` (default) | `IIR`

Specify whether the block implements an FIR lowpass filter or an IIR
lowpass filter.

### **Design minimum order filter** — Design filter with minimum order `on` (default) | `off`

When you select this check box, the block designs a filter with the
minimum order and the specified passband, stopband frequency, passband
ripple, and stopband attenuation.

When you clear this check box, you can specify the **Filter
order** as a positive integer.

### **Filter order** — Order of lowpass filter `50` (default) | positive integer

Specify the filter order of the lowpass filter as a positive
integer.

#### Dependencies

To enable this parameter, clear the **Design minimum order
filter** check box.

### **Passband edge frequency (Hz)** — Passband edge frequency `8e3` (default) | real positive scalar

Specify the passband edge frequency of the lowpass filter as a real
positive scalar in Hz or in normalized
frequency units *(since R2023a)*.

If you set the **Sample
rate mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` ––
  The value of the passband edge frequency is in Hz and must
  be less than half the value of the input sample rate.
- `Use normalized frequency (0 to
  1)` –– The value of the passband edge
  frequency is in normalized frequency units. The value must
  be a positive scalar less than
  `1.0`.

*(since R2023a)*

### **Stopband edge frequency (Hz)** — Stopband edge frequency `12e3` (default) | real positive scalar

Specify the stopband edge frequency of the lowpass filter as a real
positive scalar in Hz or in normalized
frequency units *(since R2023a)*.

If you set the **Sample
rate mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` ––
  The value of the stopband edge frequency is in Hz and must
  be less than half the value of the input sample rate.
- `Use normalized frequency (0 to
  1)` –– The value of the stopband edge
  frequency is in normalized frequency units. The value must
  be a positive scalar less than
  `1.0`.

*(since R2023a)*

#### Dependencies

To enable this parameter, select the **Design minimum
order filter** check box.

### **Maximum passband ripple (dB)** — Maximum passband ripple `0.1` (default) | real positive scalar

Specify the maximum ripple of the filter response in the passband as a
real positive scalar in dB.

### **Minimum stopband attenuation (dB)** — Minimum stopband attenuation `80` (default) | real positive scalar

Specify the minimum attenuation in the stopband as a real positive
scalar in dB.

### **Sample rate mode** — Mode to specify the input sample rate `Use normalized frequency (0 to 1)` (default) | `Specify on dialog` | `Inherit from input port`

*Since R2023a*

Specify the input sample rate using one of these options:

- `Use normalized frequency (0 to
  1)` –– Specify the passband edge and the
  stopband edge frequencies in normalized frequency units (0
  to 1).
- `Specify on dialog` –– Specify
  the input sample rate in the block dialog box using the
  **Input sample rate (Hz)**
  parameter.
- `Inherit from input port` –– The
  block inherits the sample rate from the input signal.

### **Input sample rate (Hz)** — Input sample rate `44100` (default) | scalar

Specify the input sample rate as a scalar in Hz.

#### Dependencies

To enable this parameter,
set the **Sample rate mode** parameter to
`Specify on dialog`. *(since R2023a)*

### **View Filter Response** — Open Filter Visualization Tool `button`

Opens the Filter Visualization Tool (`fvtool`) and displays the
magnitude and phase response of the Lowpass Filter. The
response is based on the block dialog box parameters. Changes made to
these parameters update FVTool.

To update the magnitude response while FVTool is running, modify the
dialog box parameters and click **Apply**.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Type of simulation to run:

- `Interpreted execution`
  (default)

  Simulate model using the MATLAB® interpreter. This option shortens startup time
  but has slower simulation speed than `Code
  generation`.
- `Code generation`

  Simulate model using generated C code. The first time you
  run a simulation, Simulink® generates C code for the block. The C code is
  reused for subsequent simulations, as long as the model does
  not change. This option requires additional startup time but
  provides faster simulation speed than
  `Interpreted execution`.

### Data Types

### **Rounding mode** — Rounding method `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Rounding method for the output fixed-point operations.

### **Coefficients** — Coefficient data type `fixdt(1,16)` (default) | `fixdt(1,16,0)` | `<data type expression>`

Fixed-point data type of the coefficients, specified as one of the
following:

- `fixdt(1,16)` — Signed
  fixed-point data type of word length `16`,
  with binary point scaling. The block determines the fraction
  length automatically from the coefficient values in such a
  way that the coefficients occupy maximum representable range
  without overflowing.
- `fixdt(1,16,0)` — Signed
  fixed-point data type of word length `16`
  and fraction length `0`. You can change the
  fraction length to any other integer value.
- `<data type expression>`
  — Specify the data type using an expression that
  evaluates to a data type object, for example, numeric type
  (`fixdt`(`[
  ]`,`16`,
  `15`)). Specify the sign mode of this data
  type as `[ ]` or
  `true`.
- `Refresh Data Type` — Refresh to
  the default data type.

Click the **Show data type assistant**
button  to display the data type assistant,
which helps you set the data type. For more information, see Specify Data Types Using Data Type Assistant (Simulink).
## Libraries

DSP System Toolbox / Filtering / Filter Designs

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

The Lowpass Filter block supports ARM
Cortex code generation. To learn more about ARM
Cortex code generation, see Code Generation for ARM Cortex-M and ARM Cortex-A Processors.

The Lowpass Filter block also supports SIMD code generation using Intel AVX2
code replacement library under these conditions:

- **Filter type** is set to
  `FIR`.
- Input signal has a data type of `single` or
  `double`.

The SIMD technology significantly improves the performance of the generated code.
For more information, see SIMD Code Generation. To
generate SIMD code from this block, see Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks.

## Version History

**Introduced in R2015b**

### R2023a: Support for normalized frequencies

When you set the **Sample rate mode** parameter to
`Use normalized frequency (0 to 1)`, you can specify
the passband and stopband edge frequencies in normalized frequency units (0 to
1).

## Description

Design FIR or IIR lowpass filter

The Lowpass Filter block independently filters each channel of the
input signal over time using the filter design specified by the block parameters. You
can control whether the block implements an IIR or FIR lowpass filter using the
**Filter type** parameter. You can specify the passband and
stopband edge frequencies in Hz or in normalized frequency
units *(since R2023a)*.

This block supports ARM®
Cortex® code generation. Under certain conditions, this block also supports SIMD
code generation. For details, see Code Generation.
