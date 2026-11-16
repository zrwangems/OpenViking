---
type: simulink-block
title: 'Delay Line'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Buffers'
documentation_page: 'delayline'
documentation_source_path: 'ref/delayline.html'
language: en
---

# Delay Line

## Ports

### Input

### **In** — Input signal vector | matrix

Specify the input signal as a vector or a matrix of size
*Mi*-by-*N*.

This port is unnamed until you select the **Show En\_Out port
for selectively enabling output** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **En\_Out** — Linearize the block output `true` | `false`

Specify whether to linearize the block output.

If the input value to the **En\_Out** port is a
`Boolean`
`1` (or `true`), the block linearizes
the output and the output is valid. This setting allows the block to be
more efficient when the tapped Delay Line output is not required at each
sample time.

Note that when the input value to the **En\_Out** port
is a `Boolean`
`0` (or `false`), the block can give
different results depending on the state of the model. The results can
appear to match valid results or can be invalid, and they cannot be
predicted. You should ignore the block output in all cases when the
input to the **En\_Out** port is
`0`.

#### Dependencies

To enable this port, select the **Show En\_Out port for
selectively enabling output** parameter.

**Data Types:** `Boolean`
### Output

### **Out** — Rebuffered output vector | matrix

Rebuffered output, returned as a vector or a matrix of size
*Mo*-by-*N*.

When *Mo* >
*Mi*, the output frame
overlap is the difference between the output and input frame size,
*Mo*−*Mi*.
When *Mo* <
*Mi*, the output is
underlapped and the Delay Line block discards the first
*Mi*−*Mo*
samples of each input frame so that only the last
*Mo* samples are
buffered into the corresponding output frame. When
*Mo* =
*Mi*, the output data is
identical to the input data, but is delayed by the latency of the block.
Due to the block latency, the outputs are always delayed by one frame,
the entries of which you specify in the **Initial
conditions** parameter.

The output frame period is equal to the input frame period
(*Tfo*=*Tfi*).
The output sample period, *Tso*,
is therefore equal to
*Tfi*/*Mo*,
or equivalently,
*Tsi*(*Mi*/*Mo*)

In the most typical use, each output differs from the preceding output
by only one sample, as illustrated below for scalar input.

Note that the first output of the block in the example above is all
zeros; this is because the **Initial Conditions**
parameter is set to zero.

This port is unnamed until you select the **Show En\_Out port
for selectively enabling output** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## Parameters

### **Delay line size** — Delay line size `64` (default) | positive integer

Specify the number of rows *M*o in
output matrix as a positive integer.

### **Initial conditions** — Initial conditions `0` (default) | scalar | vector | matrix

Specify the value of the block initial output as a scalar, vector, or a
matrix. The Delay Line block buffer is initialized to the
value specified by the **Initial conditions** parameter.
The block outputs this buffer at the first simulation step
(*t*=0).

When the block outputs a vector, the **Initial
conditions** can be a vector of the same size, or a scalar
value to be repeated across all elements of the initial output. When the
block outputs a matrix, the **Initial conditions** can be a
matrix of the same size, a vector (of length equal to the number of matrix
rows) to be repeated across all columns of the initial output, or a scalar
to be repeated across all elements of the initial output.

### **Allow directfeedthrough** — Allow direct feed through `off` (default) | `on`

When you select this check box, the input data is not delayed by an extra
frame before it is available at the output buffer. Instead, the input data
is available immediately at the output port of the block.

### **Show En\_Out port for selectively enabling output** — Show En\_Out port for selectively enabling output `off` (default) | `on`

When you select this check box, the **En\_Out** input port
appears on the block icon. This block uses a circular buffer internally even
though the output is linear. This means that for valid output, data from the
circular buffer has to be linearized. The **En\_Out** port
determines whether or not a valid output needs to be computed based on the
value of its `Boolean` input. If the input value to the
**En\_Out** port is `1`, the block
output is linearized, and thus is valid. Otherwise, the output is not
linearized, and is invalid. This allows the block to be more efficient when
the tapped Delay Line output is not required at each sample time.

Note that when the input value to the **En\_Out** port is
`0`, the block can give different results depending on
the state of the model. The results can appear to match valid results or can
be invalid, and they cannot be predicted. You should ignore the block output
in all cases when the input to the **En\_Out** port is
`0`.

### **Hold previous value when the output is disabled** — Hold previous value when the output is disabled `off` (default) | `on`

Use this parameter to specify the block output at those time steps when
the internal state buffer is not being linearized to output valid
data.

When you do not select this check box, the block memory is free to be used
by other parts of the model, and the signal on the output port is invalid.
When you select this check box, the most recent valid value is held on the
output port, and slightly more memory is used by the block.

#### Dependencies

To enable this parameter, select **Show En\_Out port for
selectively enabling output**.

## Libraries

DSP System Toolbox / Signal Management / Buffers

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
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

Rebuffer sequence of inputs

The Delay Line block rebuffers a sequence of
*Mi*-by-*N* matrix
inputs into a sequence of
*Mo*-by-*N* matrix outputs,
where *Mo* is the output frame size you specify
in the **Delay line size** parameter. Depending on whether
*Mo* is greater than, less than, or
equal to the input frame size, *Mi*, the output
frames can be underlapped or overlapped. The block always performs frame-based
processing and rebuffers each of the *N* input channels
independently.
