---
type: simulink-block
title: 'Cumulative Product'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Math Operations'
documentation_page: 'cumulativeproduct'
documentation_source_path: 'ref/cumulativeproduct.html'
language: en
---

# Cumulative Product

## Ports

### Input

### **In** — Input signal vector | matrix

Specify the input signal as a vector or a matrix.

This port is unnamed until you set the **Reset port** parameter to any
value other than `None`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

### **Rst** — Reset port scalar

The optional reset port, **Rst**, accepts scalar values, which can be
any built-in Simulink® numeric data type including `boolean`.
The rate of the input to the **Rst** port must be the
same or slower than that of the input data signal. The sample time of
the input to the **Rst** port must be a positive
integer multiple of the input sample time.

For more information on this port, see Resetting Running Product.

#### Dependencies

This port is unnamed until you set the **Reset
port** parameter to any value other than
`None`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — Cumulative product vector | matrix

Cumulative product of the signal, returned as a vector or a
matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Multiply input along** — Dimension to multiply input along `Channels (running product)` (default) | `Columns` | `Rows`

Specify the dimension along which to compute the cumulative product.
You can set this parameter to one of these options:

- `Channels (running
  product)`
- `Columns`
- `Rows`

For more information, see the following sections:

- Computing Running Product Along Channels of Input
- Multiplying Along Columns
- Multiplying Along Rows

### **Input processing** — Input processing `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block should process the input when computing the
running product along the channels of the input. You can set this
parameter to one of the following options:

- `Columns as channels (frame based)`
  — The block treats each column of the input as a separate
  channel.
- `Elements as channels (sample based)`
  — The block treats each element of the input as a
  separate channel.

For more information, see Computing Running Product Along Channels of Input.

#### Dependencies

To enable this parameter, set the **Multiply input
along** parameter to `Channels (running
product)`.

### **Reset port** — Reset type `None` (default) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

Specify the reset event that causes the block to reset the product
along channels. You can set this parameter to one of these options:

- `None`
- `Rising edge`
- `Falling edge`
- `Either edge`
- `Non-zero sample`

For more information on these options, see Resetting Running Product.

#### Dependencies

To enable this parameter, set the **Multiply input
along** parameter to `Channels (running
product)`.

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

For more details, see rounding
mode.

### **Saturate on integer overflow** — Saturate on integer overflow `off` (default) | `on`

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Intermediate product** — Intermediate product `Inherit: Same as input` (default) | `fixdt([],16,0)`

Specify the intermediate product data type. As shown in Fixed-Point Data Types, the output of the multiplier is
cast to the intermediate product data type before the next element of
the input is multiplied into it. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Product
output** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Product output** — Product output `Inherit: Same as input` (default) | `fixdt([],16,0)`

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

### **Accumulator** — Accumulator `Inherit: Same as input` (default) | `Inherit: Same as product output` | `fixdt([],16,0)`

Specify the accumulator data type. See Fixed-Point Data Types for
illustrations depicting the use of the accumulator data type in this
block. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- A rule that inherits a data type, for example,
  `Inherit: Same as product
  output`
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Accumulator** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Output** — Output `Inherit: Same as input` (default) | `Inherit: Same as product output` | `fixdt([],16,0)`

Specify the output data type. See Fixed-Point Data Types for
illustrations depicting the use of the output data type in this block.
You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- A rule that inherits a data type, for example,
  `Inherit: Same as product
  output`
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

If both inputs are unsigned, all data types including the output data
type is unsigned. If one of the inputs is signed, internal and output
data types are signed.

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Output** parameter.

See Control Data Types of Signals (Simulink) for more
information.

### **Output Minimum** — Minimum `[]` (default)

Specify the minimum value that the block must output. The default value is
`[]` (unspecified). Simulink uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Output Maximum** — Maximum `[]` (default)

Specify the maximum value that the block must output. The default value is
`[]` (unspecified). Simulink uses this value to perform:

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
| **Variable-Size Signals** | `no` |
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

Cumulative product of channel, column, or row elements

The Cumulative Product block computes the cumulative product along the
specified dimension of the input or across time (running product).
