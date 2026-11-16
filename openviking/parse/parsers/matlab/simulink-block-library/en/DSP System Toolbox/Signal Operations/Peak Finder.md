---
type: simulink-block
title: 'Peak Finder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'peakfinder'
documentation_source_path: 'ref/peakfinder.html'
language: en
---

# Peak Finder

## Ports

### Input

### **Port\_1** — Data input column vector of at least three rows | matrix with at least three rows

The Peak Finder blocks accepts real-valued vector or
matrix inputs with at least three rows.

**Example:** [`9 6 10 3 5 5 0 12`; `9 6 1 13 4 1 0
12`]'

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### Output

### **Cnt** — Number of peak values scalar | row vector

Number of peak values the block detects in the input signal, returned as a scalar or a
row vector of length equal to the number of channels in the data
input.

**Example:** [`4 3`]

**Data Types:** `uint32`

### **Idx** — Indices of the peak values column vector | matrix

Indices of the peak values in the input signal, returned as a column
vector or matrix. The size of the peak indices output is the same as
that of the input. All nonzero elements represent peak indices.

If you set **Index base** to `Zero`, the block
outputs zero-based extrema indices. If you set **Index
base** to `One`, the block outputs
one-based extrema indices.

**Example:** [`1 2 3 6 0 0 0 0 0 0`; `2 3 6 0 0 0 0 0 0
0`]'

#### Dependencies

To enable this output port, select the **Output peak indices**
parameter.

**Data Types:** `uint32`

### **Val** — Peak values column vector | matrix

Peak values in the input signal, returned as a column vector or
matrix.

**Example:** [`6 10 3 0 0 0 0 0 0 0`; `1 13 0 0 0 0 0 0 0
0`]'

#### Dependencies

To enable this output port, select the **Output peak values**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Pol** — Peak value polarity column vector | matrix

Peak value polarity in input signal, returned as a column vector or a matrix of logical
1s and 0s. If the signal value is a maximum, the block outputs 1 at this
port. If the signal value is a minimum, the block outputs 0 at this
port.

**Example:** [`0 1 0 0 0 0 0 0 0 0`; `0 1 0 0 0 0
0 0 0 0`]'

#### Dependencies

To enable this port, select either **Output peak
indices** or **Output peak values**,
and set the **Peak type(s)** parameter to
`Maxima and Minima`.

**Data Types:** `Boolean`

## Parameters

### **Peak type(s)** — Type of peaks to identify `Maxima and Minima` (default) | `Maxima` | `Minima`

Specify the type of peaks to identify as one of these:

- `Maxima` –– If you select
  **Ignore peaks within threshold of neighboring
  values**, the block identifies the current value as a
  maximum if (*current* – *previous*) > *threshold* and (*current* – *next*) >
  *threshold*. Specify *threshold* in the
  **Threshold** parameter. If you do not select
  **Ignore peaks within threshold of neighboring
  values**, the block identifies a maxima if the current
  value is larger than both its neighboring points.
- `Minima` –– If you select
  **Ignore peaks within threshold of neighboring
  values**, the block identifies the current value as a
  minimum if (*current* – *previous*) < –*threshold* and (*current* – *next*)
  < –*threshold*. If you do not
  select **Ignore peaks within threshold of neighboring
  values**, the block identifies a minima if the current
  value is smaller than both its neighboring points.
- `Maxima and Minima` –– The block
  identifies the maxima and the minima points.

### **Index base** — Index base `Zero` (default) | `One`

Specify the base of the extrema indices as either:

- `Zero` –– The first index starts with
  0. For example, consider an input vector [−1.5, 0.5, 0]. The
  peak value of this vector is 0.5 and the index of this peak
  value is 1.
- `One` –– In this setting, the first
  index starts with 1. The index of the peak value in [−1.5, 0.5,
  0] is 2.

### **Output peak indices** — Enable output of peak indices `off` (default) | `on`

Select this check box if you want the block to output the extrema indices
at the **Idx** port.

### **Output peak values** — Enable output of peak values `off` (default) | `on`

Select this parameter if you want the block to output the extrema values at the
**Val** port.

### **Maximum number of peaks to find** — Maximum number of peak values to identify `10` (default) | integer greater than or equal to 1

Enter the number of extrema to look for in each input signal as an integer
greater than or equal to 1. The block stops searching the input signal for
extrema once the maximum number of extrema has been found.

### **Ignore peaks within threshold of neighboring values** — Ignore peaks below a threshold `off` (default) | `on`

Select this parameter if you want to eliminate the detection of peaks whose amplitudes
are within a specified threshold of neighboring values. This feature allows
the block to ignore noise by focusing on values above the specified
threshold.

When you clear this parameter, the block identifies the current value as a peak if the
current value is larger (or smaller) than both its neighboring points. When
you select this parameter, the block identifies the current value as a
maximum if (*current* – *previous*) > *threshold* and (*current* –
*next*) > *threshold*. The block identifies the current value as a
minimum if (*current* – *previous*) < –*threshold* and (*current* –
*next*) < –*threshold*.

### **Threshold** — Threshold below which peaks are ignored `0` (default) | positive real scalar | vector

Specify the threshold below which peaks are ignored as a real scalar
greater than or equal to 0 or a vector with all elements greater than or
equal to 0. The length of the vector must be equal to the number of
channels.

This property identifies the current input value to be a maximum if (*current* – *previous*) > *threshold* and
(*current* – *next*) > *threshold*. The
current value is a minimum if (*current* –
*previous*) < –*threshold* and (*current* – *next*) <
–*threshold*.

#### Dependencies

To enable this parameter, select the **Ignore peaks within threshold of
neighboring values** parameter.

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

When you select this parameter, the block saturates the result of its
fixed-point operations. When you clear this parameter, the block wraps the
result of its fixed-point operations. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

#### Dependencies

To enable this parameter, select the **Ignore peaks within threshold of
neighboring values** parameter.

## Libraries

DSP System Toolbox / Signal Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
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

Determine whether each value of input signal is local minimum or maximum

The Peak Finder block counts the number of local extrema in each column of a
real-valued input signal. The block outputs the number of local extrema at the
**Cnt** port. You can also configure the block to output the
extrema indices, the extrema values, and a binary value indicating if the extrema are
maxima or minima. To qualify as an extremum, a point has to be larger (or smaller) than
both its neighboring points, so the block does not consider end points when counting
extrema.
