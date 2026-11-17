---
type: simulink-block
title: 'Logical Operator'
family: 'libsb2sl'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'LOG'
documentation_page: 'logicaloperator'
documentation_source_path: '../simulink/slref/logicaloperator.html'
language: en
---

# Logical Operator

## Ports
```yaml
ports:
- name: Port_1
  summary: First input signal scalar | vector | matrix
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_2
  summary: Second input signal scalar | vector | matrix
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_N
  summary: Nth input signal scalar | vector | matrix
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Output signal scalar | vector | matrix
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **Port\_1** — First input signal scalar | vector | matrix

First input signal, specified as a scalar, vector, or matrix.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — Second input signal scalar | vector | matrix

Second input signal, specified as a scalar, vector, or matrix.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_N** — Nth input signal scalar | vector | matrix

Nth input signal, specified as a scalar, vector, or matrix.

#### Dependencies

To enable additional input ports, use the **Number of
input ports** parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal, consisting of zeros and ones, with the same dimensions
as the input. You control the output data type with the
**Require all inputs and output to have the same data
type** and **Output data type**
parameters.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Operator
  summary: Logical operator AND (default) | OR | NAND | NOR | XOR | NXOR | NOT
  group: Main
  block_parameter: Operator
  type: character vector
  values: '''AND'' | ''OR'' | ''NAND'' | ''NOR'' | ''XOR'' | ''NXOR'' | ''NOT'''
  default: '''AND'''
- name: Number of input ports
  summary: Number of inputs 2 (default) | positive integer
  group: Main
  block_parameter: Inputs
  type: character vector
  values: positive integer
  default: '''2'''
- name: Icon shape
  summary: Icon shape rectangular (default) | distinctive
  group: Main
  block_parameter: IconShape
  type: character vector
  values: '''rectangular'' | ''distinctive'''
  default: '''rectangular'''
- name: Sample time (-1 for inherited)
  summary: Interval between samples -1 (default) | scalar | vector
  group: Main
  block_parameter: SampleTime
  values: '"-1" (default) | scalar or vector in quotes'
- name: Require all inputs and output to have the same data type
  summary: Require all ports to have same data type off (default) | on
  group: Data Type
  block_parameter: AllPortsSameDT
  type: character vector
  values: '''off'' | ''on'
  default: '''off'''
- name: Output data type
  summary: 'Output data type boolean (default) | Inherit: Logical (see Configuration Parameters: Optimization) | Inherit:
    Inherit via back propagation | fixdt(1,16) | <data type expression>'
  group: Data Type
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Logical (see Configuration Parameters: Optimization)'' | ''boolean'' | ''fixdt(1,16)'' | ''<data type
    expression>'''
  default: '''boolean'''
- name: Mode
  summary: Category of data to specify Built in (default) | Inherit | Fixed point | Expression
  group: Data Type
- name: Data type override
  summary: Specify data type override mode for this signal Inherit | Off
  group: Data Type
- name: Signedness
  summary: Signedness of fixed-point data Signed (default) | Unsigned
  group: Data Type
- name: Word length
  summary: Bit size of the word that holds the quantized integer 16 (default) | integer from 0 to 32
  group: Data Type
- name: Scaling
  summary: Method of scaling Integer (default)
  group: Data Type
```

### Main

### **Operator** — Logical operator `AND` (default) | `OR` | `NAND` | `NOR` | `XOR` | `NXOR` | `NOT`

Select the logical operator to apply to block inputs.

- `AND` — TRUE if all inputs are
  TRUE
- `OR` — TRUE if at least one input is
  TRUE
- `NAND` — TRUE if at least one input
  is FALSE
- `NOR` — TRUE when no inputs are
  TRUE
- `XOR` — TRUE if an odd number of
  inputs are TRUE
- `NXOR` — TRUE if an even number of
  inputs are TRUE
- `NOT` — TRUE if the input is
  FALSE

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operator` |
| **Type:** character vector |
| **Values:** `'AND' | 'OR' | 'NAND' | 'NOR' | 'XOR' | 'NXOR' | 'NOT'` |
| **Default:** `'AND'` |

### **Number of input ports** — Number of inputs `2` (default) | positive integer

Specify the number of block inputs as a positive integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** positive integer |
| **Default:** `'2'` |

#### Dependencies

This parameter is not available when you set the
**Operator** to
`NOT`.

### **Icon shape** — Icon shape `rectangular` (default) | `distinctive`

Specify the shape of the block icon.

- `rectangular` — Results in a
  rectangular block that displays the name of the selected
  operator.
- `distinctive` — Use the graphic
  symbol for the selected operator as specified by the IEEE standard.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconShape` |
| **Type:** character vector |
| **Values:** `'rectangular' | 'distinctive'` |
| **Default:** `'rectangular'` |

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

### **Require all inputs and output to have the same data type** — Require all ports to have same data type `off` (default) | `on`

To require that all block inputs and the output have the same data
type, select this check box. When you clear this check box, the inputs
and output can have different data types.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AllPortsSameDT` |
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
  `Simulink.Signal` object or Stateflow® chart in Simulink that is using the signal.
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
## Libraries

Simulink / Commonly Used Blocks Simulink / Logic and Bit Operations HDL Coder / Commonly Used Blocks HDL Coder / Logic and Bit Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Perform specified logical operation on input

The Logical Operator block performs the specified logical operation on its
inputs. An input value is true (`1`) if it is nonzero and false
(`0`) if it is zero.

You select the Boolean operation connecting the inputs with the
**Operator** parameter list. If you select
`rectangular` as the **Icon shape**
property, the name of the selected operator displays on the block icon. If you select
`distinctive` as the **Icon shape**
property, the name of the selected operator does not display on the block icon. This
table shows supported operations:

| Operation | Description |
| --- | --- |
| AND | TRUE if all inputs are TRUE |
| OR | TRUE if at least one input is TRUE |
| NAND | TRUE if at least one input is FALSE |
| NOR | TRUE when no inputs are TRUE |
| XOR | TRUE if an odd number of inputs are TRUE |
| NXOR | TRUE if an even number of inputs are TRUE |
| NOT | TRUE if the input is FALSE |

If you select `distinctive` as the **Icon shape**,
the block appearance indicates its function. Simulink® software displays a distinctive shape for the selected operator,
conforming to the IEEE® Standard Graphic Symbols for Logic Functions.

To specify the number of input ports, use the **Number of input ports**
parameter. The output type is specified using the **Output data type**
parameter. An output value is `1` if TRUE and `0` if
FALSE.

**Note**

The output data type should represent zero exactly. Data types that satisfy this condition include signed and unsigned integers, and any floating-point data type.

The size of the output depends on input vector size and the selected operator:

- If the block has more than one input, any nonscalar inputs must have the same dimensions. For example, if any input is a 2-by-2 array, all other nonscalar inputs must also be 2-by-2 arrays.

  Scalar inputs are expanded to have the same dimensions as the nonscalar inputs.

  If the block has more than one input, the output has the same dimensions as the inputs
  (after scalar expansion) and each output element is the result of applying the
  specified logical operation to the corresponding input elements. For example, if
  the specified operation is AND and the inputs are 2-by-2 arrays, the output is a
  2-by-2 array whose top left element is the result of applying AND to the top
  left elements of the inputs, and so on.
- For a single vector input, the block applies the operation (except the NOT operator) to all elements of the vector. The output is always a scalar.
- The NOT operator accepts only one input, which can be a scalar or a vector. If the input is a vector, the output is a vector of the same size containing the logical complements of the input vector elements.

When configured as a multi-input XOR gate, this block performs an addition modulo two
operation as mandated by the IEEE Standard for Logic Elements.
