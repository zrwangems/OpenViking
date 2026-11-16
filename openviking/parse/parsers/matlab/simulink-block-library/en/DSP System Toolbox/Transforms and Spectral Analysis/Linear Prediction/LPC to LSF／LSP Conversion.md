---
type: simulink-block
title: 'LPC to LSF/LSP Conversion'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms and Spectral Analysis / Linear Prediction'
documentation_page: 'lpctolsflspconversion'
documentation_source_path: 'ref/lpctolsflspconversion.html'
language: en
---

# LPC to LSF/LSP Conversion

## Ports

### Input

### **A** — Linear prediction coefficients column vector | unoriented vector | matrix

Specify the input linear prediction coefficients as a column vector, unoriented vector,
or a matrix. Each channel of the input must have at least two
samples.

The input LPCs for each channel, 1, *a1*,
*a*2, ...,
*a**m*, must be the denominator of the transfer function of a
stable all-pole filter with the form given in the first equation of
Requirements for Valid Outputs. A
length-*M*+1 input channel yields a
length-*M* output channel.

**Data Types:** `single` | `double`
### Output

### **LSP** — Line spectral pairs column vector | unoriented vector | matrix

Line spectral pairs, returned as a column vector, unoriented vector,
or a matrix.

**Data Types:** `single` | `double`

### **LSFn** — Line spectral frequencies normalized in range (0 0.5) column vector | unoriented vector | matrix

Line spectral frequencies normalized in range (0 0.5), returned as a
column vector, unoriented vector, or a matrix.

**Data Types:** `single` | `double`

### **LSFr** — Line spectral frequencies in range (0 π) column vector | unoriented vector | matrix

Line spectral frequencies in range (0 π), returned as a column vector,
unoriented vector, or a matrix.

**Data Types:** `single` | `double`

### **Status** — Validity status of output scalar | row vector

Validity status of the output, returned as a scalar or a row vector of Boolean values.

- `1` indicates that the output of the
  corresponding channel is valid.
- `0` indicates that the output of the
  corresponding channel is invalid.

#### Dependencies

To enable this port, select the **Show output validity
status** parameter.

**Data Types:** `Boolean`

## Parameters

### **Output** — Conversion output `LSP in range (-1 1)` (default) | `LSF normalized in range (0 0.5)` | `LSF in range (0 pi)`

Specify whether the block converts the input linear prediction polynomial
coefficients (LPCs) to line spectral pairs (LSPs) or line spectral
frequencies (LSFs). You can set this parameter to one of these options:

- `LSP in range (-1 1)` — The
  block outputs LSP values in decreasing order, equal to the
  cosine of the LSF values between 0 and *π*
  radians. The block does not output the guaranteed LSP values, −1
  and 1.
- `LSF in radians (0 pi)` — The
  block outputs the LSF values between 0 and *π*
  radians in increasing order. The block does not output the
  guaranteed LSF values, 0 and *π*.
- `LSF normalized in range (0 0.5)`
  — The block outputs normalized LSF values in increasing
  order, computed by dividing the LSF values between 0 and
  *π* radians by 2*π*. The
  block does not output the guaranteed normalized LSF values, 0
  and 0.5.

### **Root finding coarse grid points** — Number of search steps `64` (default) | positive integer greater than 1

Specify the number of search steps *n* as a positive
integer greater than 1. The block divides the interval (−1, 1) into
*n* subintervals of equal length, and looks for roots
(LSP values) in each subinterval. You must pick *n* large
enough or the block output might be invalid as described in Requirements for Valid Outputs. To learn how the block uses
this parameter to compute the output, see LSF and LSP Computation Method: Chebyshev Polynomial Method for Root Finding. Also see Adjusting Output Computation Time and Accuracy with Root Finding Parameters.

**Tunable:** Yes

### **Root finding bisection refinement** — Number of bisections `4` (default) | nonnegative integer

Specify the number of bisections *k* as a nonnegative integer. Specify
the value *k*, where each LSP output is within 1/(n⋅2k) of the actual LSP value, where *n* is the
value of the **Root finding coarse grid points** parameter.
To learn how the block uses this parameter to compute the output, see LSF and LSP Computation Method: Chebyshev Polynomial Method for Root Finding. You can also see Adjusting Output Computation Time and Accuracy with Root Finding Parameters. Tunable (Simulink).

### **Show output validity status** — Show status of output validity `off` (default) | `on`

Select this parameter to show the validity status of output. When you
select this parameter, the block enables the output port
**Status**. The **Status** port
outputs a scalar or a row vector with one Boolean element per channel.

- `1` indicates that the output of the
  corresponding channel is valid.
- `0` indicates that the output of the
  corresponding channel is invalid.

The LSF and LSP outputs are invalid when the block fails to find all the
LSF or LSP values or when the input LPCs are unstable. For details, see
Requirements for Valid Outputs.

### **If current output is invalid, overwrite with previous output** — Overwrite invalid outputs with previous output `off` (default) | `on`

When you select this check box, the block overwrites invalid outputs with the previous
output. Selecting this parameter activates other parameters for taking care
of initial overwrite values (when the very first output of the block is
invalid). For more information, see Parameters for Handling Invalid Inputs and Outputs.

### **When first output is invalid, overwrite with user-defined values** — Overwrite invalid first output with user-defined values `off` (default) | `on`

When the first input is unstable, you can overwrite the invalid first
output with:

- The default values by clearing this check box
- The values you specify by selecting this check box

The default initial overwrite values are the LSF or LSP representations of an allpass
filter. The vector that the block uses to overwrite the invalid first output
is stored as an internal state. For more information, see Parameters for Handling Invalid Inputs and Outputs.

#### Dependencies

To enable this parameter, select the **If current output is
invalid, overwrite with previous output** parameter.

### **User-defined LSP/LSF values for overwriting invalid first output** — User-defined LSP/LSF values vector (default) | matrix

Specify a vector of LSP/LSF values for overwriting an invalid first output if you
selected the **When first output is invalid, overwrite with
user-defined values** parameter. For multichannel inputs,
provide a matrix with the same number of channels as the input, or one
vector that the block applies to every channel. The vector or matrix of
LSP/LSF values you specify must have the same dimension, size, and frame
status as the other outputs.

#### Dependencies

To enable this parameter, select the **When first output is
invalid, overwrite with user-defined values**
parameter.

### **If first input value is not 1** — Action to take if first input value is not 1 `Ignore` (default) | `Normalize` | `Normalize and warn` | `Error`

Specify the action to take if the first coefficient of an input is not
`1`. Set this parameter to one of the following:

- `Ignore` –– The block treats the
  first coefficient as a 1.
- `Normalize` –– The block divides the
  input LPCs by the value of the first coefficient before
  computing the output.
- `Normalize and warn` ––- The block
  normalizes the input LPCs and displays a warning message.
- `Error` –– The block stops the
  simulation and displays an error message at the MATLAB® command line.

For more information, see Parameters for Handling Invalid Inputs and Outputs.

## Libraries

DSP System Toolbox / Estimation / Linear Prediction

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Convert linear prediction coefficients to line spectral pairs or line spectral frequencies

The LPC to LSF/LSP Conversion block converts linear prediction coefficients
(LPCs) to line spectral pairs (LSPs) or line spectral frequencies (LSFs). When
converting LPCs to LSFs, the block outputs match those of the
`poly2lsf` function.
