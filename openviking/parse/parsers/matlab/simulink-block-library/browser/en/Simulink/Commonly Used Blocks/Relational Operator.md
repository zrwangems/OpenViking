---
type: simulink-block
title: 'Relational Operator'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'relationaloperator'
language: en
---

# Relational Operator

Perform specified relational operation on inputs

## Libraries

Simulink / Commonly Used Blocks Simulink / Logic and Bit Operations HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Logic and Bit Operations

## Description

The Relational Operator block performs the specified relational operation on
the input. The value you choose for the **Relational operator**
parameter determines whether the block accepts one or two input signals.

### Two-Input Mode

By default, the Relational Operator block compares two inputs using the
**Relational operator** parameter that you specify. The first
input corresponds to the top input port and the second input to the bottom input
port. (See Identify Port Location on Rotated or Flipped Block
for a description of the port order for various block orientations.)

You can specify one of the following operations in two-input mode:

| Operation | Description |
| --- | --- |
| `==` | True if the first input is equal to the second input |
| `~=` | True if the first input is not equal to the second input |
| `<` | True if the first input is less than the second input |
| `<=` | True if the first input is less than or equal to the second input |
| `>=` | True if the first input is greater than or equal to the second input |
| `>` | True if the first input is greater than the second input |

You can specify inputs as scalars, arrays, or a combination of a scalar and an array.

| For... | The output is... |
| --- | --- |
| Scalar inputs | A scalar |
| Array inputs | An array of the same dimensions, where each element is the result of an element-by-element comparison of the input arrays |
| Mixed scalar and array inputs | An array, where each element is the result of a comparison between the scalar and the corresponding array element |

If the relational operation can be efficiently and accurately represented on the
hardware board, this efficient representation is used. Otherwise, both operands are
cast to a common type using overflow saturation and the specified rounding
mode.

You can specify the output data type using the **Output data type**
parameter. The output equals `1` for true and `0`
for false.

**Tip**

Select an output data type that represents zero exactly. Data types that satisfy this condition include signed and unsigned integers and any floating-point data type.

### One-Input Mode

When you select one of the following operations
for **Relational operator**, the block switches to one-input mode.

| Operation | Description |
| --- | --- |
| `isInf` | True if the input is `Inf` |
| `isNaN` | True if the input is `NaN` |
| `isFinite` | True if the input is finite |

For an input that is not floating point, the block produces the following output.

| Data Type | Operation | Block Output |
| --- | --- | --- |
| - Fixed point - Boolean - Built-in integer | `isInf` | False |
| `isNaN` | False |
| `isFinite` | True |

### Rules for Data Type Propagation

The following rules apply for data type propagation when your block has one or more input ports with unspecified data types.

| When the block is in... | And... | The block uses... |
| --- | --- | --- |
| Two-input mode | Both input ports have unspecified data types | `double` as the default data type for both inputs |
| One input port has an unspecified data type | The data type from the specified input port as the default data type of the other port |
| One-input mode | The input port has an unspecified data type | `double` as the default data type for the input |

## Ports

### Input

### **Port\_1** — First input signal scalar | vector | matrix

First input signal, specified as a scalar, vector, or matrix.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — Second input signal scalar | vector | matrix

Second input signal, specified as a scalar, vector, or matrix.

#### Dependencies

To enable this port, set the **Relational operator** to
`==`, `~=`,
`<`,
`<=`,
`>=`, or
`>`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal, consisting of zeros and ones, with the same dimensions
as the input. You control the output data type with the **Output
data type** parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Relational operator** — Relational operator `<=` (default) | `~=` | `==` | `<` | `>=` | `>` | `isInf` | `isNaN` | `isFinite`

Specify the operation for comparing two inputs or determining the
signal type of one input.

- `==` — True if the first input is
  equal to the second input
- `~=` — True if the first input is not
  equal to the second input
- `<` — True if the first input is
  less than the second input
- `<=` — True if the first input is
  less than or equal to the second input
- `>=` — True if the first input is
  greater than or equal to the second input
- `>` — True if the first input is
  greater than the second input
- `isInf` — True if the input is
  `Inf`
- `isNaN` — True if the input is
  `NaN`
- `isFinite` — True if the input is
  finite

`==` and `~=`
support complex numbers for simulation and code generation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operator` |
| **Type:** character vector |
| **Values:** `'==' | '~=' | '<' | '<=' | '>=' | '>' | 'isInf' | 'isNaN' | 'isFinite'` |
| **Default:** `'<='` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `ZeroCross` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

### Data Type

### **Require all inputs to have the same data type** — Require all inputs to have same data type `off` (default) | `on`

To require that all block inputs have the same data type, select this
check box. When you clear this check box, the inputs can have different
data types.

#### Dependencies

This check box is not available when you set **Relational operator**
to `isInf`,
`isNaN`, or
`isFinite` because, in those modes, the
block only has one input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Values:** `'off' | 'on` |
| **Default:** `'off'` |

### **Output data type** — Output data type `boolean` (default) | `Inherit: Logical (see Configuration Parameters: Optimization)` | `Inherit: Inherit via back propagation` | `fixdt(1,16)` | `<data type expression>`

Specify the output data type. When you select:

- `boolean` — The block output has data type
  `boolean`.
- `Inherit: Logical (see Configuration Parameters:
  Optimization)` — The block uses the **Implement logic
  signals as Boolean data** configuration parameter to specify the
  output data type (see Implement logic signals as Boolean data (vs. double)).

  **Note**

  This option supports models created before the `boolean`
  option was available. Use one of the other options, preferably
  `boolean`, for new models.
- `Inherit: Inherit via back propagation` — The block
  inherits a data type. When you select this option, the output data type and
  scaling matches that of the next downstream block.
- `fixdt(1,16)` — The block output has the specified
  fixed-point data type `fixdt(1,16)`.

  **Tip**

  The **Data Type Assistant** helps you set data
  attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.
- `<data type expression>` — The block output has
  the data type you specify as a data type expression, for example,
  `Simulink.NumericType`.

  **Tip**

  To enter a built-in data type (`double`,
  `single`, `int8`,
  `uint8`, `int16`,
  `uint16`, `int32`, or
  `uint32`), enclose the expression in single quotes. For
  example, enter `'double'` instead of
  `double`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Logical (see Configuration Parameters: Optimization)'` | `'boolean'` | `'fixdt(1,16)'` | `'<data type expression>'` |
| **Default:** `'boolean'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Simplest` (default) | `Convergent` | `Floor` | `Nearest` | `Round` | `Ceiling` | `Zero`

Specify the rounding mode for fixed-point operations. You can
select:

`Ceiling`
:   Rounds positive and negative numbers toward positive
    infinity. Equivalent to the MATLAB®
    `ceil` function.

`Convergent`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds to the nearest even integer. Equivalent to
    the Fixed-Point Designer™
    `convergent` function.

`Floor`
:   Rounds positive and negative numbers toward negative
    infinity. Equivalent to the MATLAB
    `floor` function.

`Nearest`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds toward positive infinity. Equivalent to the
    Fixed-Point Designer
    `nearest` function.

`Round`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds positive numbers toward positive infinity and
    rounds negative numbers toward negative infinity. Equivalent
    to the Fixed-Point Designer
    `round` function.

`Simplest`
:   Chooses between rounding toward floor and rounding toward
    zero to generate rounding code that is as efficient as
    possible.

`Zero`
:   Rounds number toward zero. Equivalent to the MATLAB
    `fix` function.

For more information, see Rounding Modes (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Simplest'` |

### **Mode** — Category of data to specify `Built in` (default) | `Inherit` | `Fixed point` | `Expression`

Select the category of data to specify.

- `Built in` — Specifies built-in data types. Selecting
  `Built in` enables
  `boolean`.
- `Inherit` — Specifies inheritance rules for data
  types. Selecting `Inherit` enables `Logical
  (see Configuration Parameters: Optimization)`.
- `Fixed point` — Specifies fixed-point data
  types.
- `Expression` — Specifies expressions that evaluate to
  data types.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink inherits the data
  type override setting from its context, that is, from the block,
  `Simulink.Signal` object or Stateflow® chart in Simulink® that is using the signal.
- When you select `Off`, Simulink ignores the data type
  override setting of its context and uses the fixed-point data type specified for
  the signal.

For more information, see Specify Data Types Using Data Type Assistant in the
Simulink documentation.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`.

#### Tips

The ability to turn off data type override for an individual data type provides
greater control over the data types in your model when you apply data type override.
For example, you can use this option to ensure that data types meet the requirements
of downstream blocks regardless of the data type override setting.

### **Signedness** — Signedness of fixed-point data `Signed` (default) | `Unsigned`

Specify whether you want the fixed-point data as signed or unsigned.
Signed data can represent positive and negative values, but unsigned
data represents positive values only. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Scaling** — Method of scaling `Integer` (default)

Specify the method for scaling your fixed-point data to avoid overflow conditions and
minimize quantization errors. Specifying `Integer` has the same
result as specifying a binary point location and setting the fraction length to
`0`.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button and set **Mode** to
`Fixed point`.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |

**Complex Data Support**

The `~=` and `==` operators are supported for simulation
and code generation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
