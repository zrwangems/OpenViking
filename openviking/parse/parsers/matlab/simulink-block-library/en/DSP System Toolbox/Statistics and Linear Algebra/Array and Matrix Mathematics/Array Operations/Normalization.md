---
type: simulink-block
title: 'Normalization'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Array and Matrix Mathematics / Array Operations'
documentation_page: 'normalization'
documentation_source_path: 'ref/normalization.html'
language: en
---

# Normalization

## Ports

### Input

### **Input** — Input signal scalar | vector | matrix | *N*-D array

Specify the input signal as a scalar, vector, matrix, or an *N*-D
array. You can specify both fixed- and floating-point signals in the
`Squared 2-norm` mode but only
floating-point signals in the `2-norm` mode.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output** — Normalization output scalar | vector | matrix | *N*-D array

Normalized output, returned as a scalar, vector, matrix, or an
*N*-D array. The output always has the same size,
data type, and complexity as the input signal.

For more information on how the block normalizes the signal, see Algorithms.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Norm** — Normalization type `Squared 2-norm` (default) | `2-norm`

Specify the type of normalization to perform as one of these:

- `Squared 2-norm` –– Supports both
  floating-point and fixed-point signals.
- `2-norm` –– Supports only
  floating-point signals.

### **Normalization bias** — Normalization bias `1e-10` (default) | nonnegative scalar

Specify the normalization bias as a nonnegative scalar. This is the real value
*b* which the block adds in the denominator to
avoid division by zero.

**Tunable:** Yes

### **Normalize over** — Dimension over which to normalize `Each column` (default) | `Each row` | `Specified dimension`

Specify the dimension over which to normalize as one of these:

- `Each column`
- `Each row`
- `Specified dimension` –– Use the
  **Dimension** parameter to specify the
  dimension.

### **Dimension** — Specify dimension `1` (default) | positive integer

Specify the one-based value of the dimension over which to normalize
as a positive integer. The value of this parameter cannot exceed the
number of dimensions in the input signal.

#### Dependencies

To enable this parameter, set the **Normalize
over** parameter to `Specified
dimension`.

### Data Types Tab

**Note**

The parameters on this tab are applicable only to fixed-point signals when the
block is in squared 2-norm mode. See Fixed-Point Data Types for a diagram of how the product output,
accumulator, and output data types are used in this case.

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

### **Product output** — Product output data type `Inherit: Same as input` (default) | `fixdt([],16,0)`

Specify the product output data type. See Fixed-Point Data Types and Multiplication Data Types for
illustrations depicting the use of the product output data type in this
block. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Product
output** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Accumulator** — Accumulator data type `Inherit: Same as product output` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

Specify the accumulator data type. See Fixed-Point Data Types for
illustrations depicting the use of the accumulator data type in this
block. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Same as product
  output`
- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Accumulator** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Output** — Output data type `Inherit: Same as product output` (default) | `Inherit: Same as input` | `Inherit: Same as accumulator` | `fixdt([],16,0)`

Specify the output data type. See Fixed-Point Data Types for
illustrations depicting the use of the output data type in this block.
You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Same as product
  output`
- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- A rule that inherits a data type, for example,
  `Inherit: Same as
  accumulator`
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Output** parameter.

See Control Data Types of Signals (Simulink) for more
information.

### **Output Minimum** — Output Minimum `[]` (default) | scalar

Specify the minimum value that the block should output. The default
value is `[]` (unspecified). Simulink® software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Output Maximum** — Output Maximum `[]` (default) | scalar

Specify the maximum value that the block should output. The default
value is `[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.

## Libraries

DSP System Toolbox / Math Functions / Math Operations

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

**Introduced before R2006a**

## Description

Perform vector normalization along rows, columns, or specified dimension

The Normalization block independently normalizes each row, column, or
vector of the specified dimension of the input using the `Squared
2-norm` or the `2-norm` methods.

For more information on how the block normalizes the signal, see Algorithms.
