---
type: simulink-block
title: '2-D DCT'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: '2ddct'
documentation_source_path: 'ref/2ddct.html'
language: en
---

# 2-D DCT

## Ports
```yaml
ports:
- name: Port_1
  summary: Input data matrix | vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Output data matrix | vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **Port\_1** — Input data matrix | vector

Input data, specified as a numeric matrix or a vector. The size of the input data
must be power of 2.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output data matrix | vector

Output data containing the DCT coefficients, returned as a matrix or vector. The
size and the datatype of the output is same as that of the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Sine and cosine computation
  summary: Specify how the block computes the sine and cosine terms Table lookup (default) | Trigonometric fcn
  group: ''
- name: Rounding mode
  summary: Rounding mode for fixed-point representation Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest
    | Zero
  group: ''
- name: Saturate on integer overflow
  summary: Specify overflow mode off (default) | on
  group: ''
- name: Sine Table
  summary: 'Data type of sine table Inherit: Same word length as input (default) | fixdt(1,16) | <data type expression>'
  group: ''
- name: Product output
  summary: 'Data type of product output Inherit: Inherit via internal rule (default) | Inherit: Same as input | fixdt(1,16,0)
    | <data type expression>'
  group: ''
- name: Accumulator
  summary: 'Data type of accumulator Inherit: Inherit via internal rule (default) | Inherit: Same as input | Inherit: Same
    as product output | fixdt(1,16,0) | <data type expression>'
  group: ''
- name: Output
  summary: 'Data type of output Inherit: Inherit via internal rule (default) | Inherit: Same as input | fixdt(1,16,0) | <data
    type expression>'
  group: ''
- name: Lock data type settings against change by the fixed-point tools
  summary: Data type override off (default) | on
  group: ''
```

**Main Tab**

### **Sine and cosine computation** — Specify how the block computes the sine and cosine terms `Table lookup` (default) | `Trigonometric fcn`

Use this parameter to specify how the block computes the sine and cosine terms in
the DCT algorithm.

- If you select `Trigonometric fcn`, the block computes
  the sine and cosine values during the simulation.
- If you select `Table lookup`, the block computes and
  stores the trigonometric values before the simulation starts. In this case, the
  block requires extra memory. `Table lookup` is the
  default.

**Data Types Tab**

#### Fixed-point operational parameters

### **Rounding mode** — Rounding mode for fixed-point representation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Use this parameter to specify the rounding mode for the block to use when the
specified data type and scaling cannot exactly represent the result of a fixed-point
calculation. See Rounding Modes for more information on the
available values.

**Note**

The sine table values do not obey this parameter; they always round to
`Nearest`.

### **Saturate on integer overflow** — Specify overflow mode off (default) | on

When you select this parameter, the block saturates the result of its fixed-point
operation. When you clear this parameter, the block wraps the result of its fixed-point
operation.

For details on saturate and wrap, see Overflow Handling for fixed-point operations.

**Note**

The sine table values do not obey this parameter; instead, they are always
saturated.

#### Fixed-point data types

### **Sine Table** — Data type of sine table `Inherit: Same word length as input` (default) | `fixdt(1,16)` | `<data type expression>`

Use this parameter to specify the word length of the values of the sine table. The
fraction length of the sine table values always equals the word length minus one.

The sine table values do not obey the **Rounding mode** and
**Saturate on integer overflow** parameters; instead, they are always
saturated and rounded to `Nearest`.

### **Product output** — Data type of product output `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt(1,16,0)` | `<data type expression>`

Use this parameter to specify the product output data type. See Fixed-Point Data Types
and Multiplication Data Types for illustrations
depicting the use of the product output data type in this block.

### **Accumulator** — Data type of accumulator `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)` | `<data type expression>`

Use this parameter to specify the accumulator data type. See Fixed-Point Data Types
for illustrations depicting the use of the accumulator data type in this block.

### **Output** — Data type of output `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt(1,16,0)` | `<data type expression>`

Use this parameter to specify the output data type. See Fixed-Point Data Types
for illustrations depicting the use of the output data type in this block. When you set
this parameter to

- `Inherit: Inherit via internal rule`, the block
  calculates the output word length and fraction length automatically. The internal
  rule first calculates an ideal output word length and fraction length using the
  following equations:

  WLideal output=WLinput+floor(log2(DCT length−1))+1

  FLideal output=FLinput

  Using these ideal results, the internal rule then selects word lengths and
  fraction lengths that are appropriate for your hardware. For more information, see
  Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Data type override off (default) | on

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify on the block mask. For more information, see `fxptdlg` (Fixed-Point Designer), a reference page on the Fixed-Point Tool.
## Libraries

Computer Vision Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Compute 2-D discrete cosine transform (DCT)

The 2-D DCT block calculates the two-dimensional discrete cosine transform of an image.
Suppose *f*(*x*,*y*) is the input image of dimension *M*-by-*N*, the equation for the 2-D DCT is

F(m,n)=2MNC(m)C(n)∑x=0M−1∑y=0N−1f(x,y)cos(2x+1)mπ2Mcos(2y+1)nπ2N

where C(m)=C(n)=1/2 for m,n=0 and C(m),C(n)=1 otherwise.

The number of rows and columns of the input image must be power of 2. You can also use
this block to compute 1-D DCT of a vector.
