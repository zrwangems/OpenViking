---
type: simulink-block
title: 'Array-Vector Subtract'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'arrayvectorsubtract'
documentation_source_path: 'ref/arrayvectorsubtract.html'
language: en
---

# Array-Vector Subtract

## Ports

### Input

### **A** — Input array scalar | vector | matrix | *N*-D array

Specify the input array as a scalar, vector, matrix, or an
*N*-D array.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

### **V** — Vector to subtract vector

Specify the vector *V* to subtract as a vector of
length equal to the length of the specified dimension in input
*A*.

#### Dependencies

To enable this parameter, set the **Vector (V)
source** parameter to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output** — Output scalar | vector | matrix | *N*-D array

The output of the Array-Vector Subtract block, returned
as a scalar, vector, matrix, or an *N*-D array. The
output always has the same size, data type, and complexity as the input
signal.

For more information on how the block computes the output, see Algorithms.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Subtract along dimension** — Dimension along which to subtract `1` (default) | positive integer

Specify the dimension along which to subtract the elements of vector
*V* from the input array *A* as a
positive integer. The value of this parameter must be less than or equal
to the number of dimensions of input *A*.

### **Vector (V) source** — Source of vector *V* `Input port` (default) | `Dialog parameter`

Specify the source of the vector *V* as one of these:

- `Input port` –– Use the input
  port **V** to specify the vector.
- `Dialog parameter` –– Use the
  **Vector (V)** dialog parameter to
  specify the vector.

### **Vector (V)** — Vector to subtract `[0.5 0.25]` (default) | vector

Specify the vector *V* to subtract as a vector of
length equal to the length of the specified dimension in input
*A*.

#### Dependencies

To enable this parameter, set the **Vector (V)
source** parameter to `Dialog
parameter`.

### Data Types Tab

**Note**

Floating-point inheritance takes precedence over the data type settings
defined on this tab. When inputs are floating point, the block ignores these
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

**Note**

The **Rounding mode** and **Saturate on
integer overflow** settings have no effect on numerical
results when both of these conditions are met:

- **Accumulator** is
  `Inherit: Inherit via internal
  rule`
- **Output** is `Inherit:
  Same as accumulator`

With these data type settings, the block is
effectively operating in full precision mode.

### **Saturate on integer overflow** — Saturate on integer overflow `off` (default) | `on`

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Vector (V)** — Vector data type `Inherit: Same word length as input` (default) | `fixdt([],16,0)`

Use this parameter to specify the word and fraction lengths for the
elements of the vector, *V*. You can set this parameter
to:

- A rule that inherits a data type, for example,
  `Inherit: Same word length as
  input`.
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`.

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Accumulator** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

#### Dependencies

The **Vector (V)** parameter on the
**Data Types** tab is only visible when
you select `Dialog parameter` for the
**Vector (V) source** parameter on the
**Main** tab in the block dialog box.
When the vector comes in through the block's input port, the data
type and scaling of its elements are inherited from the driving
block.

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `fixdt([],16,0)`

Specify the accumulator data type. See Fixed-Point Data Types for
illustrations depicting the use of the accumulator data type in this
block. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`. For more information on this rule, see
  Inherit via Internal Rule.
- A rule that inherits a data type, for example,
  `Inherit: Same as first
  input`.
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`.

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Accumulator** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as first input` | `fixdt([],16,0)`

Specify the output data type. See Fixed-Point Data Types for
illustrations depicting the use of the output data type in this block.
You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Same as
  accumulator`
- A rule that inherits a data type, for example,
  `Inherit: Same as first
  input`.
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`.

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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2007b**

## Description

Subtract vector from array along specified dimension

The Array-Vector Subtract block subtracts the values in the input vector
*V* from the values in the specified dimension of the
*N*-dimensional input array *A*. The
Array-Vector Subtract block subtracts each element of
*V* from the corresponding element along the specified dimension of
*A*.

For more information on how the block computes the output, see Algorithms.
