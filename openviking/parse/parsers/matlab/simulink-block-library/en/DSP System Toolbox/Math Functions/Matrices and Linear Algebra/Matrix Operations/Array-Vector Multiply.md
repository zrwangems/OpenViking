---
type: simulink-block
title: 'Array-Vector Multiply'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'arrayvectormultiply'
documentation_source_path: 'ref/arrayvectormultiply.html'
language: en
---

# Array-Vector Multiply

## Ports
```yaml
ports:
- name: A
  summary: Array input vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: V
  summary: Vector input vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: Multiplied output vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### Input

### **A** — Array input vector | matrix

Specify the array input as a vector or a matrix.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

### **V** — Vector input vector

Specify the vector input as a vector.

#### Dependencies

This port appears only when you set the **Vector (V) source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Multiplied output vector | matrix

Output of the Array-Vector Multiply block, returned as a vector or
a matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Multiply along dimension
  summary: Dimension along which to multiply input array 2 (default) | positive integer
  group: Main Tab
- name: Vector (V) source
  summary: Source of vector Input port (default) | Dialog parameter
  group: Main Tab
- name: Vector (V)
  summary: Vector parameter [0.5 0.25] (default) | vector
  group: Main Tab
- name: Rounding mode
  summary: Method of rounding operation Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Method of overflow action off (default) | on
  group: Data Types Tab
- name: Vector (V)
  summary: 'Word and fraction lengths for elements of vector Inherit: Same word length as input (default) | fixdt(1,16,0)
    | <data type expression>'
  group: Data Types Tab
- name: Vector (V) Minimum
  summary: Minimum value for elements of vector [] (unspecified) (default) | scalar
  group: Data Types Tab
- name: Vector (V) Maximum
  summary: Maximum value for elements of vector [] (unspecified) (default) | scalar
  group: Data Types Tab
- name: Product output
  summary: 'Product output data type Inherit: Inherit via internal rule (default) | Inherit: Same as first input | fixdt([],16,0)
    | <data type expression>'
  group: Data Types Tab
- name: Accumulator
  summary: 'Accumulator data type Inherit: Inherit via internal rule (default) | Inherit: Same as first input | Inherit: Same
    as product output | fixdt([],16,0) | <data type expression>'
  group: Data Types Tab
- name: Output
  summary: 'Output data type Inherit: Same as product output (default) | Inherit: Same as first input | Inherit: Same as first
    input | fixdt([],16,0) | <data type expression>'
  group: Data Types Tab
- name: Output Minimum
  summary: Minimum value of block output [] (unspecified) (default) | scalar
  group: Data Types Tab
- name: Output Maximum
  summary: Maximum value of block output [] (unspecified) (default) | scalar
  group: Data Types Tab
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types Tab
```

### Main Tab

### **Multiply along dimension** — Dimension along which to multiply input array `2` (default) | positive integer

Specify the dimension along which to multiply the input array *A*
by the elements of vector *V* as a positive integer.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Vector (V) source** — Source of vector `Input port` (default) | `Dialog parameter`

Set the source of the vector *V* to one of these options.

- `Input port` — Vector comes from the input
  port.
- `Dialog parameter` — Vector comes from the
  dialog parameter **Vector (V)**.

### **Vector (V)** — Vector parameter `[0.5 0.25]` (default) | vector

Specify the vector *V*.

#### Dependencies

This parameter appears only when you set the **Vector (V)
source** parameter to `Dialog parameter`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

### Data Types Tab

**Note**

Floating-point inheritance takes precedence over the data type settings defined on the
**Data Types** tab. When inputs are floating point, the block
ignores these settings and all internal data types are floating point.

### **Rounding mode** — Method of rounding operation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Set the rounding mode for fixed-point operations to one of these options.

- `Ceiling`
- `Convergent`
- `Floor`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

For details, see rounding mode.

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

When you select this parameter, the block saturates the result of its fixed-point
operations. When you clear this parameter, the block wraps the result of its
fixed-point operations. For details on `saturate` and
`wrap`, see overflow mode for
fixed-point operations.

### **Vector (V)** — Word and fraction lengths for elements of vector `Inherit: Same word length as input` (default) | `fixdt(1,16,0)` | `<data type expression>`

Use this parameter to specify the word and fraction lengths for the elements of
the vector, *V*. Select this parameter as one of these
options.

- `Inherit: Same word length as input` —
  Inherits the data type so it is the same as that of the input array
  *A*.
- `fixdt(1,16,0)` — Specifies a signed,
  binary-point, scaled, fixed-point data type with a word length of 16 bits and a
  fraction length of 0.
- `<data type expression>` — Lets you specify
  an expression that evaluates to a valid data type.

Alternatively, you can set the **Vector (V)** data type by using
the **Data Type Assistant**. To use the assistant, click the
**Show data type assistant** button .

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

**Note**

When the vector comes in through the input port of the block, the data type and
scaling of its elements are inherited from the driving block.

#### Dependencies

This parameter appears only when you set the **Vector (V)
source** parameter on the **Main** tab to
`Dialog parameter`.

### **Vector (V) Minimum** — Minimum value for elements of vector `[]` (unspecified) (default) | scalar

Specify the minimum value for the elements of vector *V*. The
default value is `[]` (unspecified). Simulink® uses this value to perform:

- Parameter range checking. For more information, see Specify Minimum and Maximum Values for Block Parameters (Simulink).
- Automatic scaling of fixed-point data types.

#### Dependencies

This parameter appears only when you set the **Vector (V)
source** parameter on the **Main** tab to
`Dialog parameter`.

### **Vector (V) Maximum** — Maximum value for elements of vector `[]` (unspecified) (default) | scalar

Specify the maximum value for the element of vector *V*. The
default value is `[]` (unspecified). Simulink uses this value to perform:

- Parameter range checking. For more information, see Specify Minimum and Maximum Values for Block Parameters (Simulink).
- Automatic scaling of fixed-point data types.

#### Dependencies

This parameter appears only when you set the **Vector (V)
source** parameter on the **Main** tab to
`Dialog parameter`.

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `fixdt([],16,0)` | `<data type expression>`

Specify the data type of the output of a product operation in the
Array-Vector Multiply block. For illustrations depicting the use of
the product output data type in this block, see Fixed-Point Data Types and Multiplication Data Types. Set this parameter to one of these
options.

- `Inherit: Inherit via internal rule` —
  Inherits the data type based on an internal rule. For more information on this
  rule, see Inherit via Internal Rule.
- `Inherit: Same as first input` — Inherits the
  data type so it is the same as that of the input array
  *A*.
- `fixdt([],16,0)` — Lets you specify the
  fixed-point attributes of the data type.
- `<data type expression>` — Lets you specify
  an expression that evaluates to a valid data type.

Alternatively, you can set the **Product output** data type by
using the **Data Type Assistant**. To use the assistant, click the
**Show data type assistant** button .

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `Inherit: Same as product output` | `fixdt([],16,0)` | `<data type expression>`

Specify the data type of the output of an accumulation operation in the
Array-Vector Multiply block. For illustrations depicting the use of
the accumulator data type in this block, see Fixed-Point Data Types. Set this parameter
to one of these options.

- `Inherit: Inherit via internal rule` —
  Inherits the data type based on an internal rule. For more information on this
  rule, see Inherit via Internal Rule.
- `Inherit: Same as first input` — Inherits the
  data type so it is the same as that of the input array
  *A*.
- `Inherit: Same as product output` — Inherits
  the data type so it is the same as the product output data type.
- `fixdt([],16,0)` — Lets you specify the
  fixed-point attributes of the data type.
- `<data type expression>` — Lets you specify
  an expression that evaluates to a valid data type.

Alternatively, you can set the **Accumulator** data type by using
the **Data Type Assistant**. To use the assistant, click the
**Show data type assistant** button .

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output** — Output data type `Inherit: Same as product output` (default) | `Inherit: Same as first input` | `Inherit: Same as first input` | `fixdt([],16,0)` | `<data type expression>`

Specify the output data type. For illustrations depicting the use of the output
data type in this block, see Fixed-Point Data Types. Set this parameter
to one of these options.

- `Inherit: Same as first input` — Inherits the
  data type so it is the same as that of the input array
  *A*.
- `Inherit: Same as product output` — Inherits
  the data type so it is the same as the product output data type.
- `fixdt([],16,0)` — Lets you specify the
  fixed-point attributes of the data type.
- `<data type expression>` — Lets you specify
  an expression that evaluates to a valid data type.

For more information, see Control Data Types of Signals (Simulink).

Alternatively, you can set the **Output** data type by using the
**Data Type Assistant**. To use the assistant, click the
**Show data type assistant** button .

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output Minimum** — Minimum value of block output `[]` (unspecified) (default) | scalar

Specify the minimum value that the block outputs. The default value is
`[]` (unspecified). Simulink uses this value to perform:

- Simulation range checking. For more information, see Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum value of block output `[]` (unspecified) (default) | scalar

Specify the maximum value that the block should output. The default value is
`[]` (unspecified). Simulink uses this value to perform:

- Simulation range checking. For more information, see Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.
## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2007b**

## Description

Multiply array by vector along specified dimension

The Array-Vector Multiply block multiplies the values in the specified
dimension of the *N*-dimensional input array *A* by the
values in the input vector *V*.

The length of the input *V* must be the same as the length of the
specified dimension of *A*. The Array-Vector Multiply block
multiplies each element of *V* by the corresponding element along that
dimension of *A*.

Consider a 3-dimensional
*M*-by-*N*-by-*P* input array
*A(i,j,k)* and an *N*-by-1 input vector
*V*. When the **Multiply along dimension** parameter is
set to `2`, the output of the block *Y(i,j,k)* is

Y(i,j,k)=A(i,j,k)\*V(j)

where

1≤i≤M1≤j≤N1≤k≤P

The output of the Array-Vector Multiply block is the same size as the input
array *A*. This block accepts real and complex floating-point and fixed-point
inputs.
