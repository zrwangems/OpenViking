---
type: simulink-block
title: 'Sort'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'sort'
documentation_source_path: 'ref/sort.html'
language: en
---

# Sort

## Ports
```yaml
ports:
- name: Port_1
  summary: Data input vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Val
  summary: Sorted data vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Idx
  summary: Index of the sorted data vector | matrix
  direction: output
  data_types: uint32
```

### Input

### **Port\_1** — Data input vector | matrix

The block accepts real-valued or complex-valued multichannel inputs.
The input data type must be double precision, single precision, integer,
or fixed point, with power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Val** — Sorted data vector | matrix

The block sorts the data along each channel and outputs the sorted
data through this port. The size, data type, and complexity of the
sorted data matches that of the input data. The block sorts complex
inputs according to their magnitude.

#### Dependencies

To enable this port, set the **Mode** parameter
to `Value and index` or
`Value`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **Idx** — Index of the sorted data vector | matrix

The output at this port contains the indices of the sorted
data.

#### Dependencies

To enable this port, set the **Mode** parameter
to `Value and index` or
`Index`.

**Data Types:** `uint32`
## Parameters
```yaml
parameters:
- name: Mode
  summary: Specify whether block returns values, indices, or both Value and Index (default) | Value | Index
  group: Main Tab
- name: Sort order
  summary: Order of sorting Ascending (default) | Descending
  group: Main Tab
- name: Sort algorithm
  summary: Sort method Quick sort (default) | Insertion sort
  group: Main Tab
- name: Rounding mode
  summary: Method of rounding operation Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Method of overflow action off (default) | on
  group: Data Types Tab
- name: Product output
  summary: 'Product output data type Inherit: Same as input (default) | fixdt([],16,0)'
  group: Data Types Tab
- name: Accumulator
  summary: 'Accumulator data type Inherit: Same as product output (default) | Inherit: Same as input | fixdt([],16,0)'
  group: Data Types Tab
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types Tab
```

### Main Tab

### **Mode** — Specify whether block returns values, indices, or both `Value and Index` (default) | `Value` | `Index`

When the **Mode** parameter is set to:

- `Value` — The block sorts
  the elements in each channel of the
  *M*-by-*N* input
  matrix in an ascending or descending order, based on what
  you specify in the **Sort order**
  parameter. The output at each sample time,
  *Val*, is an
  *M*-by-*N* matrix that
  contains the sorted columns of the input.

  The block sorts complex inputs according to their
  magnitude.
- `Index` — The block sorts
  the elements in each channel of the
  *M*-by-*N* input
  matrix, and outputs the index array, *I*.
  Each element in *I* is an integer of type
  `uint32` that indexes the sorted value
  in the corresponding column of the input.
- `Value and index` — The
  block outputs the sorted values of the input data,
  *Val*, and the corresponding indices in
  the index array, *I*.

### **Sort order** — Order of sorting `Ascending` (default) | `Descending`

Specify to sort the input data in either ascending or descending
order.

### **Sort algorithm** — Sort method `Quick sort` (default) | `Insertion sort`

The quick sort algorithm uses a recursive sort method and is faster at
sorting more than 32 elements. The insertion sort algorithm uses a
nonrecursive method and is faster at sorting fewer than 32 elements.
When you generate code, to avoid recursive function calls, use the
insertion sort algorithm.

### Data Types Tab

**Note**

To use these parameters, the data input must be complex and fixed point. For
all other inputs, the parameters on the **Data Types** tab are
ignored. Complex inputs are sorted by their magnitude, which is the sum of the
squares of the real and imaginary components of the input. The results of the
squares of the real and imaginary parts are stored in the **Product
output** data type. The result of the sum of the squares is stored
in the **Accumulator** data type. The parameters on the
**Data Types** tab are ignored for all other inputs.

### **Rounding mode** — Method of rounding operation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more
details, see rounding
mode.

### **Saturate on integer overflow** — Method of overflow action off (default) | on

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Product output** — Product output data type `Inherit: Same as input` (default) | `fixdt([],16,0)`

The squares of the real and imaginary parts of the complex input are
stored in the **Product output** data type.

You can set this parameter to:

- `Inherit: Same as input` — The
  product output data type is the same as the input data
  type.
- `fixdt([],16,0)` — The product
  output data type is an autosigned, binary-point, scaled,
  fixed-point data type with a word length of 16 bits and a
  fraction length of 0.

Alternatively, you can set the **Product output**
data type by using the **Data Type Assistant**. To use
the assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Accumulator** — Accumulator data type `Inherit: Same as product output` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

The result of the sum of the squares of the real and imaginary parts
of the complex input are stored in the **Accumulator**
data type.

You can set this parameter to:

- `Inherit: Same as product output`
  — The accumulator data type is the same as the product
  output data type.
- `Inherit: Same as input` — The
  accumulator data type is the same as the input data type.
- `fixdt([],16,0)` — The
  accumulator data type is an autosigned, binary-point, scaled,
  fixed-point data type with a word length of 16 bits and a
  fraction length of 0.

Alternatively, you can set the **Accumulator** data
type by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types off (default) | on

Select this parameter to prevent the fixed-point tools from overriding
the data types you specify on the block.
## Libraries

DSP System Toolbox / Statistics

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

Sort input elements by value

The Sort block ranks the values of the input elements along each
channel (column) in an `Ascending` or a
`Descending` order, based on the **Sort
order** you specify. Complex inputs are sorted by their magnitude, which is
the sum of the squares of the real and imaginary components of the input. You can choose
the **Sort algorithm** to be either `Quick
sort` or `Insertion sort`. The quick sort
algorithm uses a recursive sort method and is faster at sorting more than 32 elements.
The insertion sort algorithm uses a nonrecursive method and is faster at sorting fewer
than 32 elements. When you generate code, use the insertion sort algorithm to avoid
recursive function calls.

The **Mode** parameter specifies the block's mode of operation, which
you can set to `Value`, `Index`, or
`Value and Index`.
