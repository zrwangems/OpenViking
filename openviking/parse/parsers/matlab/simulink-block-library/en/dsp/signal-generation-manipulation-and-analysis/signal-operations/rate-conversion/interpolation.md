---
type: simulink-block
title: 'Interpolation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Operations / Rate Conversion'
documentation_page: 'interpolation'
documentation_source_path: 'ref/interpolation.html'
language: en
---

# Interpolation

## Ports

### Input

### **In** — Input signal scalar | vector | matrix | *N*-D array

Input signal, specified as a scalar, vector, matrix, or
*N*-D array.

This port is unnamed until `Source
of interpolation points` is set to `Input
port`.

**Data Types:** `single` | `double`

### **Pts** — Interpolation points scalar | vector | matrix | *N*-D array

Interpolation points, specified as a scalar, vector, matrix, or
*N*-D array.

For more details on the block's behavior when the `Source
of interpolation points` parameter is set to
`Input port`, see How the Block Applies Interpolation Arrays to Inputs.

#### Dependencies

This port is unavailable until `Source of interpolation points` is set to
`Input port`.

**Data Types:** `single` | `double`
### Output

### **Out** — Output signal scalar | vector | matrix | *N*-D array

Output signal, specified as a vector, matrix, or
*N*-D array.

This port is unnamed until `Source
of interpolation points` is set to `Input
port`.

**Data Types:** `single` | `double`

## Parameters

### **Source of interpolation points** — Interpolation point input method `Specify via dialog` (default) | `Input port`

Choose how you want to specify the interpolation points:

- `Specify via dialog` –– The `Interpolation points` parameter becomes
  available. Use this option for static interpolation
  points.
- `Input port` –– The `Pts` port appears on the block. The block uses
  the input to this port as the interpolation points. Use this
  option for time-varying interpolation points.

For more information, see Specifying Static Interpolation Points and Specifying Time-Varying Interpolation Points.

### **Interpolation points** — Interpolation points `[1.1 4.8 2.67 1.6 3.2]'` (default) | scalar | vector | matrix | *N*-D array

The array of points in time at which to interpolate the input signal
(*I*Pts). An entry of 1 in
*I*Pts refers to the first
sample of the input, an entry of 2.5 refers to the sample halfway between
the second and third input sample, and so on. See How the Block Applies Interpolation Arrays to Inputs.

**Tunable:** Yes

#### Dependencies

This parameter becomes available only when the `Source
of interpolation points` is set to `Specify
via dialog`. For more information, see Specifying Static Interpolation Points.

### **Interpolation mode** — Interpolation mode `Linear` (default) | `FIR`

Sets the block to interpolate by either `Linear`
or `FIR` interpolation. For more information, see
Linear Interpolation Mode and
FIR Interpolation Mode.

### **Interpolation filter half-length** — Half length of FIR interpolation filter `3` (default) | positive integer

Specify the half-length of the FIR interpolation filter
(`P`). To perform the interpolation in
`FIR` mode, the block uses the nearest
2×`P` low-rate samples. In most cases,
`P` low-rate samples must appear below and above each
interpolation point. If you interpolate at a low-rate sample point, the
block includes that low-rate sample in the required 2\*`P`
samples and requires only 2\*`P`–1 neighboring low-rate
samples. If an interpolation point does not have the required number of
neighboring low-rate samples, the block interpolates that point using linear
interpolation.

#### Dependencies

This parameter becomes available only when the `Interpolation mode` is set to
`FIR`. For more information, see FIR Interpolation Mode.

### **Interpolation points per input sample** — Interpolation points per sample `3` (default)

Number of points per input sample,  *upsampling
factor* (`L`), at which the block computes a
unique FIR interpolation filter. To perform the FIR interpolation, the block
uses a polyphase structure that has `L` filter arms of
length 2\*`P`.

For example, if `L`=`4`, the block
constructs a polyphase filter with four arms. The block then interpolates at
points corresponding to 1 +*i*/`L`, 2
+*i*/`L`, 3
+*i*/`L`..., where the integers 1, 2, and 3 represent the low-rate
samples, and *i*=`0,1,2,3`. To interpolate
at a point that does not directly correspond to an arm of the polyphase
filter requires an extra computation. The block first rounds that point down
to the nearest value that does correspond to an arm of the polyphase filter.
To interpolate at the point 2.2, the block rounds 2.2 down to 2, and
computes the FIR interpolation by using the first arm of the polyphase
filter structure. Similarly, to interpolate the point 2.65, the block rounds
the value down to 2.5 and uses the third arm of the polyphase filter
structure.

#### Dependencies

This parameter becomes available only when the `Interpolation mode` is set to
`FIR`. For more information, see FIR Interpolation Mode.

### **Normalized input bandwidth** — Normalized input bandwidth `0.5` (default) | scalar in (0 1]

The bandwidth of the input divided by Fs/2 (half the input sample
frequency), specified as a scalar in the range (0 1].

#### Dependencies

This parameter becomes available only when the `Interpolation mode` is set to
`FIR`. For more information, see FIR Interpolation Mode.

### **Out of range interpolation points** — Error handling for out-of-range points `Clip` (default) | `Clip and warn` | `Error`

Valid values in the interpolation array
*I*Pts range from 1 to the
number of samples in each channel of the input. For instance, given a
length-5 input vector `D`, all entries of
*I*Pts must range from 1 to 5.
*I*Pts cannot contain entries
such as 7 or -9 because there is no 7th or -9th entry in
`D`.

The **Out of range interpolation points** parameter sets
how the block handles interpolation points that are fall outside the valid
range. The parameter has these settings:

- `Clip` — The block replaces any
  out-of-range values in
  *I*Pts with the closest
  value in the valid range (from 1 to the number of input samples),
  and then proceeds with computations by using the clipped version of
  *I*Pts.
- `Clip and warn` — In addition to
  `Clip`, the block issues a warning at
  the MATLAB® command line every time clipping occurs.
- `Error` — When the block
  encounters an out-of-range value in
  *I*Pts, the simulation
  stops, and the block issues an error at the MATLAB command line.

As an example of clipping, suppose the block is set to clip out-of-range
interpolation points and gets these input vector and interpolation
points:

- `D = [11 22 33 44]'`
- `IPts = [10 2.6
  -3]'`

Because *D* has four samples, valid interpolation points
range from 1 to 4. The block clips the interpolation point 10 to 4 and the
point -3 to 1, resulting in the clipped interpolation vector
`IPtsClipped = [4 2.6
1]'`.

## Libraries

DSP System Toolbox / Signal Operations

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

## Version History

**Introduced before R2006a**

## Description

Interpolate values of real input samples

The Interpolation block interpolates discrete, real inputs by using linear or
FIR interpolation. The block accepts a vector, a matrix, or an *N*-D
array. The block outputs a scalar, a vector, a matrix, or an *N*-D
array of the interpolated values.

You must specify the interpolation points, the times at which to interpolate values in
a one-based interpolation array *I*Pts. An entry
of 1 in *I*Pts refers to the first sample of the
input data, an entry of 2.5 refers to the sample halfway between the second and third
input sample, and so on. Depending on the dimensions of the input data,
*I*Pts can be a scalar, a
length-*P* row, or a column vector, a
*P*-by-*N* matrix, or an *N*-D
array where *P* is the size of the first dimension of the
*N*-D array. In most cases, *P* can be any
positive integer. For more information about valid interpolation arrays, refer to the
tables in Pts and Interpolation points.

In most cases, the block applies *I*Pts across
the first dimension of an *N*-D input array or to each input vector.
You can set the block to apply the same interpolation array for all input data, static
interpolation points entered on the block mask, or to use a different interpolation
array for each *N*-D array, matrix, or vector input, time-varying
interpolation points received through the `Pts` input
port.
