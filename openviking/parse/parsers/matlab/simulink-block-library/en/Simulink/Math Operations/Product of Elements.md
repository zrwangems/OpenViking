---
type: simulink-block
title: 'Product of Elements'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'productofelements'
documentation_source_path: 'slref/productofelements.html'
language: en
---

# Product of Elements

## Ports
```yaml
ports:
- name: Port_1
  summary: First input to multiply or divide scalar | vector | matrix | N-D array
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_N
  summary: Nth input to multiply or divide scalar | vector | matrix | N-D array
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: X
  summary: Input signal to multiply scalar | vector | matrix | N-D array
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: ÷
  summary: Input signal to divide or invert scalar | vector | matrix | N-D array
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Output computed by multiplying, dividing, or inverting inputs scalar | vector | matrix | N-D array
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **Port\_1** — First input to multiply or divide scalar | vector | matrix | N-D array

First input to multiply or divide, provided as a scalar, vector,
matrix, or N-D array.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_N** — Nth input to multiply or divide scalar | vector | matrix | N-D array

Nth input to multiply or divide, provided as a scalar, vector, matrix,
or N-D array.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **X** — Input signal to multiply scalar | vector | matrix | N-D array

Input signal to be multiplied with other inputs.

#### Dependencies

To enable one or more **X** ports, specify one or
more `*` characters for the **Number of
inputs** parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **÷** — Input signal to divide or invert scalar | vector | matrix | N-D array

Input signal for division or inversion operations.

#### Dependencies

To enable one or more **÷** ports, specify one or
more `/` characters for the **Number of
inputs** parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output computed by multiplying, dividing, or inverting inputs scalar | vector | matrix | N-D array

Output computed by multiplying, dividing, or inverting inputs.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Number of inputs
  summary: Control number of inputs and type of operation * (default) | positive integer scalar | * or / for each input port
  group: Main
  block_parameter: Inputs
  type: character vector
  values: '''2'' | ''*'' | '''' | ''*/'' | ''*/*'' | ...'
  default: '''*'''
- name: Multiplication
  summary: Element-wise (.\*) or Matrix (\*) multiplication Element-wise(.*) (default) | Matrix(*)
  group: Main
  block_parameter: Multiplication
  type: character vector
  values: '''Element-wise(.*)'' | ''Matrix(*)'''
  default: '''Element-wise(.*)'''
- name: Apply over
  summary: How to apply function along specified dimensions All dimensions (default) | Specified dimension
  group: Main
  block_parameter: CollapseMode
  type: character vector
  values: '''All dimensions'' | ''Specified dimension'''
  default: '''All dimensions'''
- name: Dimension
  summary: Dimension along which to multiply 1 (default) | positive integer
  group: Main
  block_parameter: CollapseDim
  type: character vector
  values: '''1'' | ''2'' | ...'
  default: '''1'''
- name: Sample time (-1 for inherited)
  summary: Interval between samples -1 (default) | scalar | vector
  group: Main
  block_parameter: SampleTime
  values: '"-1" (default) | scalar or vector in quotes'
- name: Require all inputs to have the same data type
  summary: Require that all inputs have the same data type off (default) | on
  group: Signal Attributes
  block_parameter: InputSameDT
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output minimum
  summary: Minimum output value for range checking [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMin
  values: '''[]'' (default) | scalar in quotes'
- name: Output maximum
  summary: Maximum output value for range checking [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMax
  values: '''[]'' (default) | scalar in quotes'
- name: Output data type
  summary: 'Specify the output data type Inherit: Inherit via internal rule (default) | Inherit: Inherit via back propagation
    | Inherit: Same as first input | double | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16)
    | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Signal Attributes
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule | ''Inherit: Same as first input'' | ''Inherit: Inherit via back propagation''
    | ''double'' | ''single'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64''
    | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Option to prevent fixed-point tools from overriding Output data type off (default) | on
  group: Signal Attributes
  block_parameter: LockScale
  values: '''off'' (default) | ''on'''
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest |
    Zero
  group: Signal Attributes
  block_parameter: RndMeth
  type: character vector
  values: '''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
  default: '''Floor'''
- name: Saturate on integer overflow
  summary: Method of overflow action off (default) | on
  group: Signal Attributes
  block_parameter: SaturateOnIntegerOverflow
  values: '''off'' (default) | ''on'''
- name: Mode
  summary: Select data type mode Inherit (default) | Built in | Fixed Point
  group: Signal Attributes
- name: Data type override
  summary: Specify data type override mode for this signal Inherit | Off
  group: Signal Attributes
- name: Signedness
  summary: Specify signed or unsigned Signed (default) | Unsigned
  group: Signal Attributes
- name: Word length
  summary: Bit size of the word that holds the quantized integer 16 (default) | integer from 0 to 32
  group: Signal Attributes
- name: Fraction length
  summary: Specify fraction length for fixed-point data type 0 (default) | scalar integer
  group: Signal Attributes
- name: Scaling
  summary: Method for scaling fixed-point data Best precision (default) | Binary point | Slope and bias
  group: Signal Attributes
- name: Slope
  summary: Specify slope for the fixed-point data type 2^0 (default) | positive, real-valued scalar
  group: Signal Attributes
- name: Bias
  summary: Specify bias for the fixed-point data type 0 (default) | real-valued scalar
  group: Signal Attributes
```

### Main

### **Number of inputs** — Control number of inputs and type of operation `*` (default) | positive integer scalar | `*` or `/` for each input port

Control two properties of the block:

- The number of input ports on the block
- Whether each input is multiplied or divided into the
  output

When you specify:

- **`1` or
  `*` or
  `/`**

  The block has one input port. In element-wise mode, the block
  processes the input as described for the Product of
  Elements block. In matrix mode, if the parameter
  value is `1` or `*`, the block
  outputs the input value. If the value is `/`,
  the input must be a square matrix (including a scalar as a
  degenerate case) and the block outputs the matrix inverse. See
  Element-Wise Mode and Matrix Mode for more
  information.
- **Integer value > 1**

  The block has the number of inputs given by the integer value.
  The inputs are multiplied together in element-wise mode or
  matrix mode, as specified by the **Multiplication** parameter. See Element-Wise Mode and Matrix Mode for more
  information.
- **Unquoted string of two or more
  `*` and `/`
  characters**

  The block has the number of inputs given by the length of the
  character vector. Each input that corresponds to a
  `*` character is multiplied into the
  output. Each input that corresponds to a `/`
  character is divided into the output. The operations occur in
  element-wise mode or matrix mode, as specified by the **Multiplication** parameter. See Element-Wise Mode and Matrix Mode for more
  information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** `'2' | '*' | '**' | '*/' | '*/*' | ...` |
| **Default:** `'*'` |

### **Multiplication** — Element-wise (.\*) or Matrix (\*) multiplication `Element-wise(.*)` (default) | `Matrix(*)`

Specify whether the block performs `Element-wise(.*)` or
`Matrix(*)` multiplication.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Multiplication` |
| **Type:** character vector |
| **Values:** `'Element-wise(.*)' | 'Matrix(*)'` |
| **Default:** `'Element-wise(.*)'` |

### **Apply over** — How to apply function along specified dimensions `All dimensions` (default) | `Specified dimension`

Specify how to apply the function along specified dimensions.

- `All dimensions` — Apply function for
  all input values for all dimensions.

  For example, in this model,
  **Multiplication** is set to
  `Element-wise(.*)`, and
  **Apply over** is set to `All
  dimensions`. The block returns the product of
  all values from all dimensions.

  2D matrix with Constant block value [1 2 3;7 6 4] as input to Product block configured for all dimensions

  When you select `All dimensions` and
  select the configuration parameter **Use algorithms optimized for row-major array
  layout**, Simulink® enables row-major algorithms for simulation. To
  generate row-major code, set configuration parameter **Array layout** (Simulink Coder)
  to `Row-major`, and select
  **Use algorithms optimized for row-major array
  layout**. The column-major and row-major algorithms
  differ only in the multiplication order. In some cases, due to
  operation function order on the same data set, you might
  experience minor numeric differences in the outputs of
  column-major and row-major algorithms.
- `Specified dimensions` — Apply
  function for all input values for specified dimension.

#### Dependencies

To enable this parameter, set **Number of
inputs** to `*` and
**Multiplication** to `Element-wise
(.*)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CollapseMode` |
| **Type:** character vector |
| **Values:** `'All dimensions' | 'Specified dimension'` |
| **Default:** `'All dimensions'` |

### **Dimension** — Dimension along which to multiply `1` (default) | positive integer

Specify the dimension along which to multiply, as a
positive integer. For example, for a 2-D matrix, `1`
applies the function to each column, and `2` applies
the function to each row.

For example, in this model,
**Multiplication** is set to
`Element-wise(.*)`,
**Apply over** is set to
`Specified dimension`,
and **Dimension** is set to
`2`. The block returns the
product of all values from each row.

2D matrix with Constant block value [1 2 3;7 6 4] as input to Product block configured for dimension 2

#### Dependencies

To enable this parameter:

- Set **Number of inputs** to
  `*`
- Set **Multiplication** to
  `Element-wise
  (.*)`
- Set **Apply over** to
  `Specified
  dimension`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CollapseDim` |
| **Type:** character vector |
| **Values:** `'1' | '2' | ...` |
| **Default:** `'1'` |

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

### Signal Attributes

### **Require all inputs to have the same data type** — Require that all inputs have the same data type `off` (default) | `on`

Specify if input signals must all have the same data type. If you enable
this parameter, then an error occurs during simulation if the input
signal types are different.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Lower value of the output range that the software checks.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Upper value of the output range that the software checks.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`. For more information, see
Control Data Types of Signals.

When you select an inherited option, the block behaves as follows:

- `Inherit: Inherit via internal rule`
  — Simulink chooses a data type to balance numerical
  accuracy, performance, and generated code size, while taking
  into account the properties of the embedded target hardware.
  If you change the embedded target settings, the data type
  selected by the internal rule might change. For example, if
  the block multiplies an input of type
  `int8` by a gain of
  `int16` and
  `ASIC/FPGA` is specified as
  the targeted hardware type, the output data type is
  `sfix24`. If
  `Unspecified (assume 32-bit
  Generic)`, in other words, a generic
  32-bit microprocessor, is specified as the target hardware,
  the output data type is `int32`. If none of
  the word lengths provided by the target microprocessor can
  accommodate the output range, Simulink software displays an error in the Diagnostic
  Viewer.

  It is not always possible for the software to optimize code
  efficiency and numerical accuracy at the same time. If the
  internal rule doesn’t meet your specific needs for numerical
  accuracy or performance, use one of the following options:

  - Specify the output data type
    explicitly.
  - Use the simple choice of
    `Inherit: Same as
    input`.
  - Explicitly specify a default data type such
    as `fixdt(1,32,16)` and then use
    the Fixed-Point Tool to propose data types for
    your model. For more information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and then use a Data Type
    Propagation block. Examples of how to use
    this block are available in the Signal Attributes
    library Data Type Propagation
    Examples block.
- `Inherit: Inherit via back
  propagation` — Use data type of the
  driving block.
- `Inherit: Same as first input` — Use
  data type of first input signal.

#### Dependencies

When input is a floating-point data type smaller than single
precision, the `Inherit: Inherit via internal
rule` output data type depends on the setting
of the Inherit floating-point output type smaller than single precision configuration parameter. Data types are smaller than single
precision when the number of bits needed to encode the data type is
less than the 32 bits needed to encode the single-precision data
type. For example, `half` and
`int16` are smaller than single
precision.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding mode for fixed-point operations. You can select:

`Ceiling`
:   Rounds positive and negative numbers toward positive infinity. Equivalent
    to the MATLAB®
    `ceil` function.

`Convergent`
:   Rounds number to the nearest representable value. If a tie occurs, rounds
    to the nearest even integer. Equivalent to the Fixed-Point Designer™
    `convergent` function.

`Floor`
:   Rounds positive and negative numbers toward negative infinity. Equivalent
    to the MATLAB
    `floor` function.

`Nearest`
:   Rounds number to the nearest representable value. If a tie occurs, rounds
    toward positive infinity. Equivalent to the Fixed-Point Designer
    `nearest` function.

`Round`
:   Rounds number to the nearest representable value. If a tie occurs, rounds
    positive numbers toward positive infinity and rounds negative numbers toward
    negative infinity. Equivalent to the Fixed-Point Designer
    `round` function.

`Simplest`
:   Chooses between rounding toward floor and rounding toward zero to generate
    rounding code that is as efficient as possible.

`Zero`
:   Rounds number toward zero. Equivalent to the MATLAB
    `fix` function.

For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB rounding function into the mask field.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |

### **Mode** — Select data type mode `Inherit` (default) | `Built in` | `Fixed Point`

Select the category of data to specify.

- `Inherit` — Inheritance rules for data types.
  Selecting `Inherit` enables a second menu/text box to the right
  where you can select the inheritance mode.
- `Built in` — Built-in data types. Selecting
  `Built in` enables a second menu/text box to the right
  where you can select a built-in data type.
- `Fixed point` — Fixed-point data types. Selecting
  `Fixed point` enables additional parameters that
  you can use to specify a fixed-point data type.
- `Expression` — Expressions that evaluate to data
  types. Selecting `Expression` enables a second menu/text box to
  the right, where you can enter the expression.

For more information, see Specify Data Types Using Data Type Assistant.

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

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned. Signed data can represent
positive and negative values, but unsigned data represents positive values only.

- `Signed`, specifies the fixed-point data as
  signed.
- `Unsigned`, specifies the fixed-point data as
  unsigned.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set the **Mode** to `Fixed
point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Binary point`.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Slope** — Specify slope for the fixed-point data type `2^0` (default) | positive, real-valued scalar

Specify slope for the fixed-point data type. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### **Bias** — Specify bias for the fixed-point data type `0` (default) | real-valued scalar

Specify bias for the fixed-point data type as any real number. For more
information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.
## Libraries

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

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

HDL Coder supports `Tree` architectures for Product
or Product of Elements blocks that have a single vector input with multiple
elements.

| Architecture | Description |
| --- | --- |
| `Linear` (default) | Generates a linear chain of adders to compute the sum of products. |
| `Tree` | Generates a tree structure of adders to compute the sum of products. |

**HDL Block Properties**

If you use the block in matrix multiplication mode, you can specify the
**DotProductStrategy**. This setting determines whether you want to
implement the matrix multiplication by using a tree of adders and multipliers, or use the
Multiply-Accumulate block implementation. The default is `Fully
Parallel`.

**Note**

The **DotProductStrategy** must be set to `Fully
Parallel` when you use the `Native Floating Point`
mode.

For more information, see DotProductStrategy (HDL Coder).

See also Design Considerations for Matrices and Vectors (HDL Coder).

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |

**Complex Data Support**

The default (linear) implementation supports complex data.

Complex division is not supported. For block
implementations of the Product block in divide mode or reciprocal mode, see
HDL Code Generation on the
Divide block reference page.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Copy or invert one scalar input, or collapse one nonscalar input

The Product of Elements block inputs one scalar, vector, or matrix. You
can use the block to:

- Copy a scalar input unchanged
- Invert a scalar input (divide 1 by it)
- Collapse a vector or matrix to a scalar by multiplying together all elements
  or taking successive inverses of the elements
- Collapse a matrix to a vector using one of these options:

  - Multiply together the elements of each row or column
  - Take successive inverses of the elements of each row or
    column

The Product of Elements block is functionally a Product block that has two preset
parameter values:

- **Multiplication**:
  `Element-wise(.*)`
- **Number of inputs**: `*`

Setting nondefault values for either of those parameters can change a Product
of Elements block to be functionally equivalent to a Product block or a Divide block.
