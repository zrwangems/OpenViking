---
type: simulink-block
title: 'Data Type Conversion'
family: 'hdlcoder'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'datatypeconversion'
documentation_source_path: '../simulink/slref/datatypeconversion.html'
language: en
---

# Data Type Conversion

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D array. The input can be any
real- or complex-valued signal. If the input is real, the output is
real. If the input is complex, the output is complex. The block converts
the input signal to the **Output data type** you
specify.

When you are converting fixed-point data types, use the
**Input and output to have equal** parameter to
determine whether the conversion happens based on the `Real
World Value (RWV)` or `Stored Integer
(SI)` value of the signal. For more information, see
Convert Fixed-Point Signals.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | N-D array

Output signal, converted to the data type you specify, with the same
dimensions as the input signal.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## Parameters

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

### **Output data type** — Output data type `Inherit: Inherit via back propagation` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified directly, or
expressed as a data type object such as `Simulink.NumericType`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'<data type expression>'` |
| **Default:** `'Inherit: Inherit via back propagation'` |

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

### **Input and output to have equal** — Constraint for converting fixed-point data types `Real World Value (RWV)` (default) | `Stored Integer (SI)`

Specify which type of input and output must be equal, in the context of
fixed-point data representation.

- `Real World Value (RWV)` — Specifies the
  goal of making the `Real World Value (RWV)`
  of the input equal to the `Real World Value
  (RWV)` of the output.
- `Stored Integer (SI)` — Specifies the
  goal of making the `Stored Integer (SI)`
  value of the input equal to the `Stored Integer
  (SI)` value of the output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConvertRealWorld` |
| **Type:** character vector |
| **Values:** `'Real World Value (RWV)' | 'Stored Integer (SI)'` |
| **Default:** `'Real World Value (RWV)'` |

### **Integer rounding mode** — Specify the rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Choose one of these rounding modes.

`Ceiling`
:   Rounds both positive and negative numbers
    toward positive infinity. Equivalent to the
    MATLAB®
    `ceil` function.

`Convergent`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds to the nearest even
    integer. Equivalent to the Fixed-Point Designer™
    `convergent` function.

`Floor`
:   Rounds both positive and negative numbers
    toward negative infinity. Equivalent to the
    MATLAB
    `floor` function.

`Nearest`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds toward positive
    infinity. Equivalent to the Fixed-Point Designer
    `nearest` function.

`Round`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds positive numbers
    toward positive infinity and rounds negative
    numbers toward negative infinity. Equivalent to
    the Fixed-Point Designer
    `round` function.

`Simplest`
:   Automatically chooses between round toward
    floor and round toward zero to generate rounding
    code that is as efficient as possible.

`Zero`
:   Rounds number toward zero. Equivalent to the
    MATLAB
    `fix` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RndMeth` |
| **Type**: character vector |
| **Values**: `'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **Default**: `'Floor'` |

#### See Also

For more information, see Rounding Modes (Fixed-Point Designer).

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

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

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

Simulink / Commonly Used Blocks Simulink / Signal Attributes HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Signal Attributes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
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

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Note**

With the HDL Code Advisor, you can replace Data Type
Conversion blocks that use the `Stored Integer
(SI)` mode and convert between floating-point and
fixed-point data types with Float Typecast blocks.

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |

**Enumeration Data Support**

This block supports code generation for enumerated signals. Use this block to cast a
signal of an enumerated type to any integer type or to cast a signal of any
integer type to an enumerated type.

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Convert input signal to specified data type

The Data Type Conversion block converts an input signal of any Simulink® data type to the data type that you specify.

**Note**

To control the output data type by specifying block parameters,
or to inherit a data type from a downstream block, use the Data Type Conversion block. To inherit a data type from a different
signal in the model, use the Data Type Conversion Inherited block.

### Convert Fixed-Point Signals

When you convert between fixed-point data types, the **Input and output to have
equal** parameter controls block behavior. This parameter does not
change the behavior of the block when:

- The input and output do not have a fixed-point data type.
- The input or output has a fixed-point data type with trivial
  scaling.

For more information about fixed-point numbers, see Fixed-Point Numbers in Simulink (Fixed-Point Designer).

To convert a signal from one data type to another by attempting to preserve the real-world
value of the input signal, select `Real World Value (RWV)`,
the default setting. The block accounts for the limits imposed by the scaling of the
input and output and attempts to generate an output of equal real-world
value.

To change the real-world value of the input signal by performing a scaling reinterpretation
of the stored integer value, select `Stored Integer (SI)`.
Within the limits of the specified data types, the block attempts to preserve the
stored integer value of the signal during conversion. A best practice is to specify
input and output data types using the same word length and signedness. Doing so
ensures that the block changes only the scaling of the signal. Specifying a
different signedness or word length for the input and output could produce
unexpected results such as range loss or unexpected sign extensions. For an example,
see Convert Data Types in Simulink Models.

If you select `Stored Integer (SI)`, the block does not perform a
lower-level bit reinterpretation of a floating-point input signal. For example, if
the input is `single` and has value `5`, the bits
that store the input in memory are given in hexadecimal by the following
command.

```
num2hex(single(5))
```

```
40a00000
```

However, the Data Type Conversion block does
not treat the stored integer value as `40a00000`,
but instead as the real-world value, `5`. After conversion,
the stored integer value of the output is `5`.

### Cast Enumerated Signals

Use a Data Type Conversion block to cast enumerated signals as follows:

1. To cast a signal of enumerated type to a signal of any numeric
   type.

   The underlying integers of all enumerated values input to the
   Data Type Conversion block must be within the range
   of the numeric type. Otherwise, an error occurs during
   simulation.
2. To cast a signal of any integer type to a signal of enumerated
   type.

   The value input to the Data Type Conversion block must
   match the underlying value of an enumerated value. Otherwise, an error
   occurs during simulation.

   You can enable the **Saturate on integer overflow** parameter so that
   Simulink uses the default value of the enumerated type when the
   value input to the block does not match the underlying value of an
   enumerated value. See Type Casting for Enumerations (Simulink Coder).

You cannot use a Data Type Conversion block in these cases:

- To cast a noninteger numeric signal to an enumerated signal.
- To cast a complex signal to an enumerated signal, regardless of the
  data types of the real and imaginary parts of the complex signal.

See Simulink Enumerations for information on working with enumerated types.
