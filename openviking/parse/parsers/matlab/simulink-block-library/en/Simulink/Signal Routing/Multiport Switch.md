---
type: simulink-block
title: 'Multiport Switch'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'multiportswitch'
documentation_source_path: 'slref/multiportswitch.html'
language: en
---

# Multiport Switch

## Ports

### Input

### **Port\_1** — Control signal scalar

The control signal can be of any data type that Simulink® supports, including fixed-point and enumerated types. When
the control input is not an integer value, the block truncates the value
to an integer by rounding to zero.

For information on control signals of enumerated type, see Guidelines on Setting Parameters for Enumerated Control Port.

For information on how the block handles the out-of-range condition,
see How the Block Handles an Out-of-Range Control Input.

#### Limitations

- If the control signal is numeric, the control signal
  cannot be complex.
- If the control signal is an enumerated signal, the block
  uses the value of the underlying integer to select a data
  port.
- If the underlying integer does not correspond to a data
  port, an error occurs.
- If the control input is a floating point value that
  exceeds the datatype range of integers, the Multiport
  Switch block issues a runtime error. This range
  includes `Inf` and
  `NaN`.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

### **1** — First data input scalar | vector | matrix | N-D array

First data input, specified as a scalar, vector, matrix, or N-D array.
All input data signals can be of any data type that Simulink supports.

- If all the data inputs are scalar, the output is scalar
- If at least one of the data inputs is a vector, the block
  output is a vector. In this case, the block expands any scalar
  inputs to vectors.
- If any two nonscalar signals have a different number of
  dimensions or different dimension lengths, select the
  **Allow different data input sizes** check
  box. For more information, see Use Data Inputs That Have Different Dimensions
- If any data signal is of an enumerated type, all others must
  be of the same enumerated type.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

### **2** — Second data input scalar | vector | matrix | N-D array

Second data input, specified as a scalar, vector, matrix, or N-D
array. All input data signals can be of any data type that Simulink supports.

- If all the data inputs are scalar, the output is scalar
- If at least one of the data inputs is a vector, the block
  output is a vector. In this case, the block expands any scalar
  inputs to vectors.
- If any two nonscalar signals have a different number of
  dimensions or different dimension lengths, select the
  **Allow different data input sizes** check
  box. For more information, see Use Data Inputs That Have Different Dimensions
- If any data signal is of an enumerated type, all others must
  be of the same enumerated type.

#### Dependencies

To enable this port, set **Number of data ports**
to an integer greater than 1.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

### **N** — Nth data input scalar | vector | matrix | N-D array

Nth data input, specified as a scalar, vector, matrix, or N-D array.
All input data signals can be of any data type that Simulink supports.

- If all the data inputs are scalar, the output is scalar
- If at least one of the data inputs is a vector, the block
  output is a vector. In this case, the block expands any scalar
  inputs to vectors.
- If any two nonscalar signals have a different number of
  dimensions or different dimension lengths, select the
  **Allow different data input sizes** check
  box. For more information, see Use Data Inputs That Have Different Dimensions
- If any data signal is of an enumerated type, all others must
  be of the same enumerated type.

#### Dependencies

To enable the *N*th input port, set **Number of data
ports** to an integer value greater than or equal to
*N*.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

### **\*** — Data port for out-of-range inputs scalar | vector | matrix | N-D array

Input data port for out-of-range control signal inputs, specified as a
scalar, vector, matrix, or N-D array. All input data signals can be of
any data type that Simulink supports. If any data signal is of an enumerated type, all
others must be of the same enumerated type. If any two signals have a
different number of dimensions or different dimension lengths, select
the **Allow different data input sizes** check box. For
more information, see Use Data Inputs That Have Different Dimensions.

#### Dependencies

To create an additional data port for out-of-range control signal
inputs, set **Data port for default case** to
`Additional data port`. When you set
**Data port for default case** to
`Last data port`, the block uses the
last data port for output when the control signal value does not
match any data port indices.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Selected data input, based on control signal value scalar | vector | matrix | N-D array

The block outputs one of the data inputs, selected according to the control signal
value. The output has the same dimensions as the corresponding data
input. The output data type is the data type of the input port that
requires the largest memory space. When you select the **Allow
different data input sizes** check box, the output of the
block is a variable size signal.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `string` | `image`

## Parameters

### Main

### **Data port order** — Type of ordering for data input ports `One-based contiguous` | `Zero-based contiguous` | `Specify indices`

Specify the type of ordering for your data input ports.

- `Zero-based contiguous` — Block uses
  zero-based indexing for ordering contiguous data ports. This is
  the default value of the Index Vector
  block.
- `One-based contiguous` — Block uses
  one-based indexing for ordering contiguous data ports. This is
  the default value of the Multiport Switch
  block
- `Specify indices` — Block uses
  noncontiguous indexing for ordering data ports.

#### Tips

- When the control port is of enumerated type, select
  `Specify indices`.
- If you select `Zero-based
  contiguous` or `One-based
  contiguous`, verify that the control port
  is not of enumerated type. This configuration is deprecated
  and produces an error. You can run the Upgrade Advisor on
  your model to replace each Multiport Switch
  block of this configuration with a block that explicitly
  specifies data port indices. See Model Upgrades.
- Avoid situations where the block contains unused data
  ports for simulation or code generation. When the control
  port is of fixed-point or built-in data type, verify that
  all data port indices are representable with that type.
  Otherwise, the following block behavior occurs.

  | If the Block Has Unused Data Ports and Data Port Order Is: | The Block Produces: |
  | --- | --- |
  | `Zero-based contiguous` or `One-based contiguous` | A warning |
  | `Specify indices` | An error |

#### Dependencies

Selecting `Zero-based contiguous` or
`One-based contiguous` enables the
**Number of data ports** parameter.

Selecting `Specify indices` enables the
**Data port indices** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataPortOrder` |
| **Type:** character vector |
| **Values:** `'Zero-based contiguous' | 'One-based contiguous' | 'Specify indices'` |
| **Default:** `'One-based contiguous'` (Multiport Switch) | `'Zero-based contiguous'` (Index Vector) |

### **Number of data ports** — Number of data input ports `1` | `3` | integer between 1 and 65535

Specify the number of data input ports to the block. The total number of input ports is
the number you specify, plus one for the control signal input port, and
plus one more if you set **Data port for default case**
to `Additional data port`.

#### Dependencies

To enable this parameter, set **Data port order**
to `Zero-based contiguous` or
`One-based contiguous`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** integer between 1 and 65536 |
| **Default:** `'3'` (Multiport Switch) | `'1'` (Index Vector) |

### **Data port indices** — Array of indices for data ports `{1,2,3}` (default) | array of indices

Specify an array of indices for your data ports. The block icon
changes to match the data port indices you specify.

#### Tips

- To specify an array of indices that correspond to all
  values of an enumerated type, enter
  `enumeration('name of the
  type')`.

  For example, `enumeration('MyColors')` is
  a valid entry if `MyColors` is the name of
  an enumerated type.
- To enter specific values of an enumerated type, use the
  *`type_name.enumerated_name`*
  format. Do not enter the underlying integer value.

  For example, `enumeration({MyColors.Red, MyColors.Green,
  MyColors.Blue})` is a valid entry.
- To indicate that more than one value maps to a data port,
  use brackets.

  For example, the following entries are both valid:

  - `enumeration({MyColors.Red,
    MyColors.Green, [MyColors.Blue,
    MyColors.Yellow]})`
  - `enumeration({[3,5],0,18})`
- If the control port is of fixed-point or built-in data
  type, the values for **Data port indices**
  must be representable with that type. Otherwise, an error
  appears at compile time to alert you to unused data
  ports.
- If the control port is of enumerated data type, the values
  for **Data port indices** must be
  enumerated values of that type.
- If **Data port indices** contains values
  of enumerated type, the control port must be of that data
  type.

#### Dependencies

To enable this parameter, set **Data port order**
to `Specify indices`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataPortIndices` |
| **Type:** character vector |
| **Values:** array of indices |
| **Default:** `'{1,2,3}'` |

### **Data port for default case** — Port to use for out-of-range inputs `Last data port` (default) | `Additional data port`

Specify whether to use the last data port for out-of-range inputs, or to use an
additional port. An asterisk (\*) next to the port name indicates the
port the block uses when the control port value does not match any data
port indices.

- `Last data port` — Block uses the
  last data port for output when the control port value does not
  match any data port indices.
- `Additional data port` — Block uses
  an additional data port for output when the control port value
  does not match any data port indices.

#### Tip

If you set this parameter to `Additional data
port` and **Number of data ports**
is `3`, the number of input ports on the
block is 5. The first input is the control port, the next three
inputs are data ports, and the fifth input is the default port for
out-of-range inputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataPortForDefault` |
| **Type:** character vector |
| **Values:** `'Last data port' | 'Additional data port'` |
| **Default:** `'Last data port'` |

### **Diagnostic for default case** — Diagnostic action when control port value does not match data port indices `Error` (default) | `Warning` | `None`

Specify the diagnostic action to take when the control port value does not match any
data port indices.

- `None` — Produce no response.
- `Warning` — Display a warning and
  continue the simulation.
- `Error` — Terminate the simulation
  and display an error. In this case, the **Data port for
  default case** is used only for code generation and
  not simulation.

For more information, see How the Block Handles an Out-of-Range Control Input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiagnosticForDefault` |
| **Type:** character vector |
| **Values:** `'None' | 'Warning' | 'Error'` |
| **Default:** `'Error'` |

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

### **Require all data port inputs to have the same data type** — Require all inputs to have the same data type `off` (default) | `on`

Select this check box to require that all data input ports have the same data
type. When you clear this check box, the block allows data port inputs to have
different data types.

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

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first data input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Simulink.ImageType(480,640,3)` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select an inherited option, the block behaves as follows:

- `Inherit: Inherit via internal
  rule`—Simulink chooses a data type to balance numerical accuracy,
  performance, and generated code size, while taking into account the
  properties of the embedded target hardware. If you change the embedded
  target settings, the data type selected by the internal rule might
  change. It is not always possible for the software to optimize code
  efficiency and numerical accuracy at the same time. If the internal rule
  doesn’t meet your specific needs for numerical accuracy or performance,
  use one of the following options:

  - Specify the output data type explicitly.
  - Explicitly specify a default data type such as
    `fixdt(1,32,16)` and then use the
    Fixed-Point Tool to propose data types for your model. For more
    information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and then use a Data Type
    Propagation block. Examples of how to use this block
    are available in the Signal Attributes library Data Type
    Propagation Examples block.
- `Inherit: Inherit via back propagation` —
  Uses the data type of the driving block.
- `Inherit: Same as first data input` — Uses
  the data type of the first data input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `Simulink.ImageType(480,640,3)` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock the output data type setting of this block against changes
by the Fixed-Point Tool and the Fixed-Point Advisor. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LockScale` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

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

### **Allow different data input sizes (Results in variable-size output signal)** — Allow input signals with different sizes `off` (default) | `on`

Select this check box to allow input signals with different sizes.

- `On` — Allows input signals with different sizes, and
  propagate the input signal size to the output signal. In this mode, the
  block produces a variable-size output signal.
- `Off` — Requires that all nonscalar data input signals be
  the same size.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `AllowDiffInputSizes` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |

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

Simulink / Signal Routing HDL Coder / Signal Routing

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
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
| **CodingStyle** | Specify whether to generate HDL code with case statements or if-else statements. By default, HDL Coder generates if-else statements. See also CodingStyle (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

**Setting Data Port Indices Using Specify Indices mode**

You can specify the data port indices to the input port using specify indices
mode. To configure the Multiport Switch block with specify indices mode, set the
**Data port order** block parameter to `Specify
indices`. Then, enter the port indices in the **Data
port indices** block parameter. For a model targeted for HDL code
generation, you can use these input data types for the control input in a
specify indices mode:

- Fixed-point and floating-point types
- Signed and unsigned integer types
- Enumerated types
- Vector, matrix, and bus types

**Using an Enumerated Type as Port Index**

You can set **Data port order** to **Specify
indices**, and enter enumeration values for the **Data
port indices**. For example, you can connect the Enumerated
Constant block to the Multiport Switch control
port and use the enumerated types as data port indices.

**Restrictions**

You must avoid using of `NaN` or out of range values at the
control port. It can cause simulation mismatch in the validation model.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Multiport Switch block has runtime error when input has floating point value

The Multiport Switch block now issues a runtime error when the
control signal in the first port has a floating point value that exceeds the
datatype range of integers. This range includes `Inf` and
`NaN`.

## Description

Select output signal based on control signal

The Multiport Switch block determines which of several inputs to the block
passes to the output. The block bases this decision on the value of the first input. The
first input is the control input and the remaining inputs are the data inputs. The value
of the control input determines which data input passes to the output.

The Multiport Switch and Index Vector blocks are alternative
configurations of the same block.

- Multiport Switch — Select output signal based on control signal.
- Index Vector — Switch output between different inputs based on
  value of first input.

The table summarizes how Multiport Switch interprets the control input and
determines the data input that is passed to the output.

| Control Input | Truncation | Setting for Data Port Order | Block Behavior During Simulation | |
| --- | --- | --- | --- | --- |
| Indexing to Select Data Input | Out-of-Range Condition |
| Integer value | None | `Zero-based contiguous` | Zero-based indexing | The control input is less than `0` or greater than the number of data inputs minus one. |
| `One-based contiguous` | One-based indexing | The control input is less than `1` or greater than the number of data inputs. |
| `Specify indices` | Indices you specify | The control input does not correspond to any specified data port index. |
| Not an integer value | The block truncates the value to an integer by rounding to zero. | `Zero-based contiguous` | Zero-based indexing | The truncated control input is less than `0` or greater than the number of data inputs minus one. |
| `One-based contiguous` | One-based indexing | The truncated control input is less than `1` or greater than the number of data inputs. |
| `Specify indices` | Indices you specify | The truncated control input does not correspond to any specified data port index. |

For information on how the block handles the out-of-range condition, see
How the Block Handles an Out-of-Range Control Input.

### Multiport Switch Configured as an Index Vector Block

An Index Vector is a special
configuration of a Multiport Switch block in which you specify one
data input and the control input is zero-based. The block output is the element of
the input vector whose index matches the control input. For example, if the input
vector is `[18 15 17 10]` and the control input is
`3`, the element that matches the index of 3 (zero-based) is
10, and that becomes the output value.

To configure a Multiport Switch block to work as an Index
Vector block, set **Number of data ports** to
`1` and **Data port order** to
`Zero-based contiguous`.

### How the Block Handles an Out-of-Range Control Input

For an input with an integer value less than `intmax(‘int32’)`, the input
is out of range when the value does not match any data port indices. For a control
input that is not an integer value, the input is out of range when the
*truncated* value does not match any data port indices. In
both cases, the block behavior depends on your settings for **Data port for
default case** and **Diagnostic for default
case**.

**Note**

If the control input is larger than `intmax(‘int32’)`, the
block wraps the input value to an integer.

**Behavior for Simulation**

The following behavior applies only to simulation for your model.

| Data Port for Default Case | Diagnostic for Default Case | | |
| --- | --- | --- | --- |
| None | Warning | Error |
| `Last data port` | Use the last data port and do not report any warning or error. | Use the last data port and report a warning. | Report an error and stop simulation. |
| `Additional data port` | Use the additional data port with a `*` label and do not report any warning or error. | Use the additional data port with a `*` label and report a warning. | Report an error and stop simulation. |

**Behavior for Code Generation**

The following behavior applies to code generation for your model.

| Data Port for Default Case | Diagnostic for Default Case | | |
| --- | --- | --- | --- |
| None | Warning | Error |
| `Last data port` | Use the last data port. | Use the last data port. | Use the last data port. |
| `Additional data port` | Use the additional data port with a `*` label. | Use the additional data port with a `*` label. | Use the additional data port with a `*` label. |

### Use Data Inputs That Have Different Dimensions

If two signals have a different number of dimensions or different
dimension lengths, you can use the signals as data inputs to a Multiport Switch block. In the block dialog box, select the parameter **Allow different data input sizes**. In this case, the output of the block is a variable-size signal. If you do not select this parameter, the block generates an error.

For more information about the parameter, see Allow different data input sizes (Results in variable-size output signal). For
more information about variable-size signals, see Variable-Size Signal Basics.

### Rules That Determine the Block Behavior

You specify the number of data inputs with **Number of data ports**.

- If you set **Number of data ports** to
  1, the block behaves as an *index selector* or *index vector* and not as a multiport switch. For more details,
  see Multiport Switch Configured as an Index Vector Block.
- If you set **Number of data ports** to an integer greater than 1, the block behaves as a multiport switch. The block output is the data input that corresponds to the value of the control input. If at least one of the data inputs is a vector, the block output is a vector. In this case, the block expands any scalar inputs to vectors.
- If all the data inputs are scalar, the output is a scalar.

### Guidelines on Setting Parameters for Enumerated Control Port

When the control port on the Multiport Switch block is of enumerated type, follow these guidelines:

| Scenario | What to Do | Rationale |
| --- | --- | --- |
| The enumerated type contains a value that represents invalid, out-of-range, or uninitialized values. | - Set **Data port order** to `Specify indices`. - Set **Data port indices** to use this value for the last data port. - Set **Data port for default case** to `Last data port`. | This block configuration handles invalid values that the enumerated type explicitly represents. |
| The enumerated type contains only valid enumerated values. However, a data input port can get invalid values of enumerated type. | - Set **Data port for default case** to `Additional data port`. | This block configuration handles invalid values that the enumerated type does not explicitly represent. |
| The enumerated type contains only valid enumerated values. Data input ports can never get invalid values of enumerated type. | - Set **Data port for default case** to `Last data port`. - Set **Diagnostic for default case** to `None`. | This block configuration avoids unnecessary diagnostic action. |
| The block does not have a data input port for every value of the enumerated type. | - Set **Data port for default case** to `Additional data port`. | This block configuration handles enumerated values that do not have a data input port, along with invalid values. |
