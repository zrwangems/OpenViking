---
type: simulink-block
title: 'Pad'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'pad'
documentation_source_path: 'ref/pad.html'
language: en
---

# Pad

## Ports

### Input

### **Input 1** — Data input scalar | vector | matrix | *N*-D array

Specify the input as a scalar, vector, matrix, or an
*N*-D array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
**Complex Number Support:** Yes
### Output

### **Output 1** — Padded or truncated output scalar | vector | matrix | *N*-D array

Output of the Pad block. The size and dimension of the
output depends on whether the block has padded or truncated the input
along the specified dimension. The data type and complexity of the
output matches that of the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
**Complex Number Support:** Yes

## Parameters

### **Pad over** — Dimension over which to pad or truncate `Columns` (default) | `Rows` | `Columns and rows` | `None` | `Specified dimensions`

Specify the dimensions over which to pad or truncate:

- `Columns`
- `Rows`
- `Columns and rows`
- `None`
- `Specified dimensions`

### **Dimensions to pad** — Specify dimension over which to pad or truncate `1` (default) | scalar | vector

Specify the one-based dimension(s) over which to pad or truncate. The
value for this parameter can be a scalar or a vector. For example, specify
`1` to pad columns. Specify `[1 2]` to
pad columns and rows. Specify `[1 3 5]` to pad the first,
third, and fifth dimensions.

#### Dependencies

This parameter appears only when you set **Pad over**
to `Specified dimensions`.

### **Pad value source** — Source of pad value `Specify via dialog` (default) | `Input port`

Choose how you specify the pad value. The pad value can come from the
dialog or from an input port:

- If you select `Specify via dialog`, the
  **Pad value** parameter appears.
- If you select `Input port`, the
  `PVal` port appears on the block icon.

### **Pad value** — Pad value `0` (default) | scalar

Specify the constant scalar value with which to pad the input.

**Tunable:** Yes

#### Dependencies

This parameter appears only when you set **Pad value
source** to `Specify via
dialog`.

### **Output column mode** — Mode of specifying column length `User-specified` | `Next power of two`

Choose how you specify the column length of the output:

- If you select `User-specified`, the
  **Column size** parameter appears.
- If you select `Next power of two`,
  the block pads the output columns until their length is the next
  highest power of two. If the column length is already a power of
  two, the block does not pad the columns.

#### Dependencies

This parameter appears only when you set **Pad over**
to `Columns` or `Columns and
rows`.

### **Column size** — Column length of output `1` | scalar

Specify the column length of the output. If the specified column length is
longer than the input column length, the block pads the columns. If the
specified column length is shorter than the input column length, the block
truncates the columns.

#### Dependencies

This parameter appears only when you set **Output column
mode** to `User-specified`.

### **Output row mode** — Mode of specifying row length `User-specified` (default) | `Next power of two`

Choose how you specify the row length of the output:

- If you select `User-specified`, the
  **Row size** parameter appears.
- If you select `Next power of two`,
  the block pads the output rows until their length is the next
  highest power of two. If the row length is already a power of
  two, the block does not pad the rows.

#### Dependencies

This parameter appears only when you set **Pad over**
to `Rows` or `Columns and
rows`.

### **Row size** — Row length of output `1` | scalar

Specify the row length of the output. If the specified row length is
longer than the input row length, the block pads the rows. If the specified
row length is shorter than the input row length, the block truncates the
rows.

#### Dependencies

This parameter appears only when you set **Output row
mode** to `User-specified`.

### **Specify** — Specify output size or pad size `Output size` (default) | `Pad size`

Choose whether you want to control the output length of the specified
dimensions by specifying the output size or the pad size.

#### Dependencies

This parameter appears only when you set **Pad over**
to `Specified dimensions`.

### **Output size mode** — Mode of specifying output length `User-specified` | `Next power of two`

Choose how you specify the output length of the specified dimensions:

- If you select `User-specified`, the
  **Output size** parameter appears.
- If you select `Next power of two`,
  the block pads the specified dimensions until their length is
  the next highest power of two. If the dimension length is
  already a power of two, the block does not pad in that
  dimension.

#### Dependencies

This parameter appears only when you set **Pad over**
to `Specified dimensions` and the
**Specify** parameter to `Output
size`.

### **Output size** — Output length along specified dimension `1` | scalar | vector

Specify the output length of the specified dimension(s). This parameter
must be a scalar or a vector with the same number of elements as the
**Dimensions to pad** parameter. Each element in the
**Output size** vector gives the output length for the
corresponding dimension in the **Dimensions to pad**
vector. If the specified length is longer than the input length for a given
dimension, the block pads that dimension. If the specified length is shorter
than the input length for a given dimension, the block truncates that
dimension.

#### Dependencies

This parameter appears only when you set **Pad over**
to `Specified dimensions` and the
**Specify** parameter to `Output
size`.

### **Pad size at beginning** — Specify number of values to add to beginning of input signal `0` | scalar | vector

Specify how many values to add to the beginning of the input signal along
the specified dimension(s). This parameter must be a scalar or a vector with
the same number of elements as the **Dimensions to pad**
parameter. Each element in the **Pad size at beginning**
parameter gives the pad length at the beginning of the corresponding
dimension in the **Dimensions to pad** parameter. Values of
this parameter must be nonnegative integers.

#### Dependencies

This parameter appears only when you set **Pad over**
to `Specified dimensions` and the
**Specify** parameter to `Pad
size`.

### **Pad size at end** — Specify number of values to add to end of input signal `0` | scalar | vector

Specify how many values to add to the end of the input signal along the
specified dimension(s). This parameter must be a scalar or a vector with the
same number of elements as the **Dimensions to pad**
parameter. Each element in the **Pad size at end**
parameter gives the pad length at the end of the corresponding dimension in
the **Dimensions to pad** parameter. Values of this
parameter must be nonnegative integers.

#### Dependencies

This parameter appears only when you set **Pad over**
to `Specified dimensions` and the
**Specify** parameter to `Pad
size`.

### **Pad signal at** — Specify where to pad or truncate signal `End` (default) | `Beginning` | `Beginning and end`

Specify whether to pad or truncate the signal at the
`Beginning`, `End`, or
`Beginning and end` of the specified
dimension(s). When you select `Beginning and end`,
half the pad length is added to the beginning of the signal and the other
half is added to the end of the signal. For an odd pad length, the extra
value is added to the end of the signal. When you specify to truncate the
signal in this mode, an equal number of values are truncated from the
beginning and the end of the signal. In the case of an odd truncation
length, the extra value is removed from the end of the signal.

#### Dependencies

This parameter appears only when you set **Pad over**
to `Columns`, `Rows`,
and `Columns and rows`.

### **Action when truncation occurs** — Action to take when truncation occurs `None` | `Warning` | `Error`

Specify the action the block takes when it truncates the input.

- `None` –– The block does not notify
  when the input is truncated.
- `Warning` –– The block displays a
  warning when the input is truncated.
- `Error` –– The block displays an
  error message and terminates the simulation when the input is
  truncated.

#### Dependencies

This parameter appears only when you set **Pad over**
to `Columns`, `Rows`,
and `Columns and rows`.

## Libraries

DSP System Toolbox / Signal Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `fixed point` | `integer` | `single` |
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

Pad or truncate specified dimension(s)

The Pad block extends or crops the dimensions of an input signal by padding or
truncating along its columns, rows, columns and rows, or along any other dimension(s)
that you specify. The block truncates the input when you specify output dimensions that
are shorter than the corresponding input dimensions. If the input and output lengths are
the same, the block acts as a pass-through.

You can enter the pad value in the block mask or via an input port. You can enter
output sizes in the block mask, or have the block pad the specified dimensions until
their length is the next highest power of two. The **Pad signal at**
parameter controls whether the block pads or truncates the input signal dimensions at
the beginning, end, or both. For odd pad or truncation lengths, the extra pad or
truncation value is applied at the end of the signal. When the block is in the
`Specified dimensions` mode, you can specify either the
output size or the pad size.

You can configure the block to warn or error when an input signal is truncated using
the **Action when truncation occurs** parameter.
