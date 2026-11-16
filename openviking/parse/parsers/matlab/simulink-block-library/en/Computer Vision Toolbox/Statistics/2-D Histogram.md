---
type: simulink-block
title: '2-D Histogram'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: '2dhistogram'
documentation_source_path: 'ref/2dhistogram.html'
language: en
---

# 2-D Histogram

## Ports

### Input

### **Port\_1** — Input image vector | matrix | 3-D array

Input image, specified as a vector, matrix, or 3-D array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Rst** — Reset value scalar

Reset value for an input sequence, specified as a scalar. This value dictates the
event that causes the block to reset the running histogram. The sample time of the
**Rst** input must be a positive integer and a multiple of the
input sample time.

#### Dependencies

To enable this port, select the **Running histogram** parameter
and set the **Trigger type** parameter to `Rising
edge`, `Falling edge`, `Either
edge`, or `Non-zero sample`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Histogram output vector | matrix | 3-D array

Histogram output, returned as a vector, matrix, or 3-D array.

If the **Find the histogram over** parameter is set to
`Entire input`, then the output is always a vector. If the
**Find the histogram over** parameter is set to `Each
column`, then the output has the same number of dimension as the
input.

**Data Types:** `single` | `double` | `uint32`

## Parameters

**Main**

### **Lower limit of histogram** — Lower limit of lowest-valued bin `0` (default) | real-valued scalar

Specify a real-valued scalar for the lower boundary,
*Bm*, of the lowest-valued bin.
`NaN` and `inf` are not valid values for
*Bm*.

**Tunable:** Yes

### **Upper limit of histogram** — Upper limit of highest-valued bin `1` (default) | real-valued scalar

Specify a real-valued scalar for the upper boundary,
*Bm*, of the highest-valued bin.
`NaN` and `inf` are not valid values for
*BM*.

**Tunable:** Yes

### **Number of bins** — Number of bins in histogram `256` (default) | real-valued scalar

Specify the number of bins in the histogram.

### **Find the histogram over** — Dimension along which to compute histogram `Entire input` (default) | `Each column`

Specify the dimension of the input image along which the block computes the
histogram values. For any given value, *n*, of the **Number of
bins** parameter, this parameter affects the output of the block as follows.

- `Entire input` — The block computes the
  histogram over the entire input. It outputs an *n*- element
  column vector.
- `Each column` — The block computes the
  histogram over each column of the input.

  - If the input is an *M*-by-*N* matrix,
    the block outputs an *n*-by-*N* matrix. The
    *j*th column of the output matrix contains the histogram
    for the data in the *j*th column of the
    *M*-by-*N* input matrix.
  - If the input is an
    *M*-by-*N*-by-*P* array,
    the block outputs an
    *n*-by-*N*-by-*P* array.
    If the input is a three-channel color image, the value of P is 3, and the
    block computes the histogram for each color channel separately.

### **Normalized** — Normalize histogram output `off` (default) | `on`

Select the **Normalized** parameter to normalize the output
histogram value within a range of [0, 1].

**Note**

Use of this parameter is not supported for fixed-point signals.

### **Running histogram** — Frequency distribution for successive inputs `off` (default) | `on`

Select the **Running histogram** parameter to compute the frequency
distribution of both the past and present data for successive inputs. The block resets
the histogram (by emptying all of the bins) when it detects a reset event at the
optional **Rst** port. There's an additional dimension to the output
size which is equal to
((*Tsim*/*Ts*)+1)
where *Tsim* is the simulation time and
*Ts* is the sample time for block execution.
The output depends on the value of the **Find the histogram over**
parameter.

- `Entire input` — The block computes a running histogram
  for the data in the first dimension of the input. The block outputs an
  *n*-by-1-by-((*Tsim*/*Ts*)+1),
  where *n* is the value of **Number of bins**
  parameter.
- `Each column` — The block computes a running histogram
  for each column of the *M*-by-*N* matrix. The
  block outputs an
  *n*-by-*N*-by-((*Tsim*/*Ts*)+1)
  array, where *n* is the value of the **Number of
  bins** parameter.

**Note**

When the block is used in running mode and the input data type is non-floating
point, the output of the histogram is stored as a `uint32` data type.
The largest number that can be represented by this data type is
`232–1`. If the range of the
`uint32` data type is exceeded, the output data wraps back to
0.

### **Trigger type** — Reset condition of running histogram `None` (default) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

Specify the event that, when detected at the optional **Rst** port,
resets the running histogram. The reset signal and the input data signal must have the
same rate.

Specify the reset event as:

- `None` — Disables the **Rst**
  port
- `Rising edge` — Triggers a reset event when the
  **Rst** input does one of the following:

  - Rises from a negative value to either a positive value or zero
  - Rises from zero to a positive value, where the rise is not a continuation of
    a rise from a negative value to zero
- `Falling edge` — Triggers a reset event when the
  **Rst** input does one of the following:

  - Falls from a positive value to either a negative value or zero
  - Falls from zero to a negative value, where the fall is not a continuation of
    a fall from a positive value to zero
- `Either edge` — Triggers a reset event when the
  **Rst** input is a rising edge or falling edge
- `Non-zero sample` — Triggers a reset event at
  each sample time that the **Rst** input is not zero

#### Dependencies

To enable this parameter, select the **Running histogram**
parameter.

**Data Types**

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

## Libraries

Computer Vision Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or
`memset` functions (string.h) under certain conditions.

## Version History

**Introduced before R2006a**

## Description

Generate histogram from input

The 2-D Histogram block computes the frequencies of the elements in the
input image. The block calculates the histogram values for either the entire input or for each
column of the input image. It sorts all the of input values into bins according to their pixel
values. The histogram value for a given bin represents the frequency of the input values
bracketed by that bin. The block is also capable of computing a running histogram across a
sequence of inputs. The block is also capable of computing a running histogram across a
sequence of inputs.
