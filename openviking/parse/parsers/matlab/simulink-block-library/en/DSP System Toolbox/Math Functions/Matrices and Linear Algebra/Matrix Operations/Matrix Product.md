---
type: simulink-block
title: 'Matrix Product'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'matrixproduct'
documentation_source_path: 'ref/matrixproduct.html'
language: en
---

# Matrix Product

## Ports
```yaml
ports:
- name: Input
  summary: Input vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Output
  summary: Matrix product output vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### Input

### **Input** — Input vector | matrix

Specify the input as a vector or a matrix of size
*M*-by-*N*.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output** — Matrix product output vector | matrix

Output of the Matrix Product block, returned as a
vector or a matrix. For more information on how the block computes the
output, see the description for the **Multiply over**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Multiply over
  summary: Dimension over which to multiply Columns (default) | Rows | Entire input
  group: Main Tab
- name: Rounding mode
  summary: Rounding mode Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Saturate on integer overflow off (default) | on
  group: Data Types Tab
- name: Intermediate product
  summary: 'Intermediate product data type Inherit: Same as input (default) | fixdt([],16,0)'
  group: Data Types Tab
- name: Product output
  summary: 'Product output data type Inherit: Inherit via internal rule (default) | Inherit: Same as input | fixdt([],16,0)'
  group: Data Types Tab
- name: Accumulator
  summary: 'Accumulator data type Inherit: Inherit via internal rule (default) | Inherit: Same as input | Inherit: Same as
    product output | fixdt([],16,0)'
  group: Data Types Tab
- name: Output
  summary: 'Output data type Inherit: Same as product output (default) | Inherit: Same as input | fixdt([],16,0)'
  group: Data Types Tab
- name: Output Minimum
  summary: Output minimum [] (default) | scalar
  group: Data Types Tab
- name: Output Maximum
  summary: Output maximum [] (default) | scalar
  group: Data Types Tab
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types Tab
```

### Main Tab

### **Multiply over** — Dimension over which to multiply `Columns` (default) | `Rows` | `Entire input`

Specify the dimension over which to multiply as one of these:

- `Columns` –– The block multiplies
  down the elements of each column and outputs the resulting
  1-by-*N* matrix. The block treats a
  length-*M* unoriented vector input as
  an *M*-by-1 matrix.

  [u11u12u13u21u22u23u31u32u33]⇓[y1y2y3]=[(∏i=13ui1)(∏i=13ui2)(∏i=13ui3)]
- `Rows` –– The block multiplies
  across the elements of each row and outputs the resulting
  *M*-by-1 matrix. The block treats a
  length-*N* unoriented vector input as a
  1-by-*N* matrix.

  [u11u12u13u21u22u23u31u32u33]⇒[y1y2y3]=[(∏j=13u1j)(∏j=13u2j)(∏j=13u3j)]
- `Entire input` –– The block
  multiplies all the elements of the input together and
  outputs the resulting scalar.

  [u11u12u13u21u22u23u31u32u33]⇒y=(∏i=13∏j=13uij)

### Data Types Tab

**Note**

Floating-point inheritance takes precedence over the data type settings
defined on this pane. When inputs are floating point, the block ignores these
settings, and all internal data types are floating point.

### **Rounding mode** — Rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations as one of the following:

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

For more details, see Rounding
Modes.

### **Saturate on integer overflow** — Saturate on integer overflow `off` (default) | `on`

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Intermediate product** — Intermediate product data type `Inherit: Same as input` (default) | `fixdt([],16,0)`

Specify the intermediate product data type. As shown in Fixed-Point Data Types, the block casts the output of the
multiplier to the intermediate product data type before multiplying the
next element of the input into it. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Product
output** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

Specify the product output data type. See Fixed-Point Data Types and Multiplication Data Types for
illustrations depicting the use of the product output data type in this
block. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`. For more information on this rule, see
  Inherit via Internal Rule.
- A rule that inherits a data type, for example,
  `Inherit: Same as input`.
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Product
output** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

Specify the accumulator data type. See Fixed-Point Data Types for illustrations depicting the use
of the accumulator data type in this block. You can set this parameter
to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`. For more information on this rule, see
  Inherit via Internal Rule.
- A rule that inherits a data type, for example,
  `Inherit: Same as input`.
- A rule that inherits a data type, for example,
  `Inherit: Same as product
  output`.
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Accumulator** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Output** — Output data type `Inherit: Same as product output` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

Specify the output data type. See Fixed-Point Data Types for illustrations depicting the use
of the output data type in this block. You can set this parameter
to:

- A rule that inherits a data type, for example,
  `Inherit: Same as product
  output`
- A rule that inherits a data type, for example,
  `Inherit: Same as input`.
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Output** parameter.

See Control Data Types of Signals (Simulink) for more
information.

### **Output Minimum** — Output minimum `[]` (default) | scalar

Specify the minimum value that the block should output. The default
value is `[]` (unspecified). Simulink® uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Output Maximum** — Output maximum `[]` (default) | scalar

Specify the maximum value that the block should output. The default
value is `[]` (unspecified). Simulink uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

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

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Multiply matrix elements along rows, columns, or entire input

The Matrix Product block multiplies the elements of an
*M*-by-*N* input matrix along its rows, columns,
or over all its elements.
