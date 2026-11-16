---
type: simulink-block
title: 'Differentiator Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'differentiatorfilter'
documentation_source_path: 'ref/differentiatorfilter.html'
language: en
---

# Differentiator Filter

## Ports

### Input

### **Input** — Data input vector | matrix

Specify the data input as a vector or a matrix. If the input signal is
a matrix, each column of the matrix is treated as an independent
channel.

This block supports variable-size input, enabling you to change the
channel length during simulation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output** — Differentiator filter output vector | matrix

Differentiator filter output, returned as a vector or a matrix.

The output port properties, such as data type, complexity, and
dimension are identical to the input port properties.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Design minimum order filter** — Design minimum order filter `on` (default) | `off`

When you select this check box, the block designs a filter with the minimum order and
with the passband ripple that you specify in **Maximum passband
ripple (dB)**. When you clear this check box, specify the
order of the filter in **Filter order**.

### **Filter order** — Order of differentiator filter `31` (default) | odd positive integer

Specify the order of the differentiator filter as an odd positive
integer.

#### Dependencies

To enable this parameter, clear the **Design minimum order
filter** parameter.

### **Maximum passband ripple (dB)** — Maximum passband ripple `0.1` (default) | positive scalar

Specify the maximum ripple of the filter response in the passband as a real positive
scalar in dB.

### **Scale filter coefficients** — Scale filter coefficients `off` (default) | `on`

When you select this check box, the blocks scales the filter coefficients to preserve
the input dynamic range. By default, this check box is not
selected.

### **View Filter Response** — View filter response button (default)

Click this button to open the Filter Visualization Tool
(`fvtool`) and display the magnitude and phase
response of the Differentiator Filter block. The response
is based on the block dialog box parameters. Changes made to these
parameters update FVTool.

To update the magnitude response while FVTool is running, modify the
dialog box parameters and click **Apply**.

### **Simulate using** — Simulate using `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution`
  (default)

  Simulate model using the MATLAB®  interpreter. This option shortens
  startup time and has faster simulation speed
  than `Code
  generation`.
- `Code generation`

  Simulate model using generated C code. The first time you
  run a simulation, Simulink® generates C code for the block. The C code is
  reused for subsequent simulations, as long as the model does
  not change. This option requires additional startup time but
  provides faster subsequent simulations.

### Data Types Tab

### **Rounding mode** — Rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding method for the output fixed-point operations. The rounding methods
are `Ceiling`,
`Convergent`,
`Floor`,
`Nearest`, `Round`,
`Simplest`, and
`Zero`. The default is
`Floor`.

### **Coefficients** — Coefficients `fixdt(1,16)` (default) | `fixdt(1,16,0)` | `<data type expression>`

Specify the fixed-point data type of the coefficients as one of the
following:

- `fixdt(1,16)` — Signed
  fixed-point data type of word length `16`
  with binary point scaling. The block determines the fraction
  length automatically from the coefficient values such that
  the coefficients occupy the maximum representable range
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
which helps you set the stage input parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

The word length of the output is same as the word length of the input.
The fraction length of the output is computed such that the entire
dynamic range of the output can be represented without overflow. For
details on how the block computes the fraction length, see Fixed-Point Precision Rules for Avoiding Overflow in FIR Filters.

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

The Differentiator Filter block supports SIMD code generation using
Intel AVX2 code replacement library when the input signal has a data type of
`single` or `double`.

The SIMD technology significantly improves the performance of the generated code.
For more information, see SIMD Code Generation. To
generate SIMD code from this block, see Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks.

## Version History

**Introduced in R2015b**

## Description

Direct form FIR fullband differentiator filter

The Differentiator Filter block applies a fullband differentiator
filter on the input signal to differentiate all its frequency components. The block uses
an FIR equiripple filter design to design the differentiator filter. The ideal frequency
response of the differentiator is D(ω)=jω for −π≤ω≤π.

You can design the filter with a minimum order or with a specific order.

This block also supports SIMD code generation. For details, see Code Generation.
