---
type: simulink-block
title: 'Discrete Transfer Fcn'
family: 'simulink-extras'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Additional Discrete'
documentation_page: 'discretetransferfcn'
documentation_source_path: '../simulink/slref/discretetransferfcn.html'
language: en
---

# Discrete Transfer Fcn

## Ports

### Input

### **u** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix.

When you set the **Input
processing** parameter to `Columns as channels
(frame based)`, the block supports variable-size input
signals, that is, you can change the frame size (number of rows) of the
signal during simulation but the number of channels (columns) must
remain constant. *(since R2024a)*

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Num** — Numerator coefficients scalar | vector | matrix

Coefficients of the numerator polynomial specified as a vector or matrix in descending
powers of *z*. Use a row vector to specify the
coefficients for a single numerator polynomial. Use a matrix to specify
coefficients for multiple filters to be applied to the same input. Each
matrix row represents a set of filter taps. The order of the denominator
must be greater than or equal to the order of the numerator.

#### Dependencies

To enable this port, set **Numerator Source** to
`Input port`.

Numerator and denominator coefficients must have the same
complexity. They can have different word lengths and fraction
lengths.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Den** — Denominator coefficients scalar | vector | matrix

Coefficients of the denominator polynomial, specified as a vector in descending powers
of *z*. Use a row vector to specify the coefficients
for a single denominator polynomial. Use a matrix to specify
coefficients for multiple filters to apply to the same input. Each
matrix row represents a set of filter taps. The order of the denominator
must be greater than or equal to the order of the numerator. The leading
denominator coefficient cannot be `0`.

#### Dependencies

To enable this port, set **Denominator Source**
to `Input port`.

Numerator and denominator coefficients must have the same
complexity. They can have different word lengths and fraction
lengths.

To set **Denominator Source** to `Input
port`, select the **Optimize by skipping divide
by leading denominator coefficient (a0)** parameter.
The block ignores the leading denominator coefficient value a0 and
replaces it with 1.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **External reset** — External reset signal scalar

External reset signal, specified as a scalar. When the specified
trigger event occurs, the block resets the states to their initial conditions.

**Tip**

The icon for this port changes based on the value of the
**External reset** parameter.

#### Dependencies

To enable this port, set **External reset** to
`Rising`,
`Falling`,
`Either`,
`Level`, or `Level
hold`.

#### Limitations

The reset signal must be a scalar of type single, double, Boolean, or integer.
Fixed-point data types, except for `ufix1`, are not
supported.

**Data Types:** `single` | `double` | `Boolean` | `int8` | `int16` | `int32` | `fixed point`

### **x0** — Initial states scalar | vector | matrix

Initial states, specified as a scalar, vector, or matrix. For more information about
specifying states, see Specifying Initial States. States are complex when
either the input or the coefficients are complex.

#### Dependencies

To enable this port, set **Initial states
Source** to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal specified as a scalar, vector, or matrix.

When you set **Sample time** to
`-1`, sample time of the output signal is same as the
sample time of the input signal **u**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## Parameters

### Main

### **Numerator Source** — Source of numerator coefficients `Dialog` (default) | `Input port`

Specify the source of the numerator coefficients as
`Dialog` or `Input
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumeratorSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Numerator Value** — Numerator coefficients `[1]` (default) | scalar | vector | matrix

Numerator coefficients of the discrete transfer function. To specify the coefficients,
set the **Source** to
`Dialog`. Then, enter the coefficients in
**Value** as descending powers of
*z*. Use a row vector to specify the coefficients
for a single numerator polynomial. Use a matrix to specify coefficients
for multiple filters to be applied to the same input. Each matrix row
represents a set of filter taps.

#### Dependencies

To enable this parameter, set the **Numerator
Source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Numerator` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[1]'` |

### **Denominator Source** — Source of denominator coefficients `Dialog` (default) | `Input port`

Specify the source of the denominator coefficients as
`Dialog` or `Input
port`.

To set **Denominator Source** to `Input port`,
select the **Optimize by skipping divide by leading denominator
coefficient (a0)** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenominatorSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Denominator Value** — Denominator coefficients `[1 0.5]` (default) | scalar | vector | matrix

Denominator coefficients of the discrete transfer function. To specify the coefficients,
set the **Source** to
`Dialog`. Then, enter the coefficients in
**Value** as descending powers of
*z*. Use a row vector to specify the coefficients
for a single denominator polynomial. Use a matrix to specify
coefficients for multiple filters to apply to the same input. Each
matrix row represents a set of filter taps.

When you select the **Optimize by skipping divide by leading
denominator coefficient (a0)** parameter, an error occurs
if you specify the denominator coefficients in the block dialog box and
*a0* ≠ 1.

#### Dependencies

To enable this parameter, set the **Denominator
Source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Denominator` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[1 0.5]'` |

### **Initial states Source** — Source of initial states `Dialog` (default) | `Input port`

Specify the source of the initial states as
`Dialog` or `Input
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStatesSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Initial states Value** — Initial filter states `0` (default) | scalar | vector | matrix

Specify the initial filter states as a scalar, vector, or matrix. To
learn how to specify initial states, see Specifying Initial States.

#### Dependencies

To enable this parameter, set **Initial states
Source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStates` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

### **External reset** — External state reset `None` (default) | `Rising` | `Falling` | `Either` | `Level` | `Level hold`

Specify the trigger event to use to reset the states to the initial conditions.

| Reset Mode | Behavior |
| --- | --- |
| `None` | No reset |
| `Rising` | Reset on a rising edge |
| `Falling` | Reset on a falling edge |
| `Either` | Reset on either a rising or falling edge |
| `Level` | Reset in either of these cases:  - When the reset signal is nonzero at the current time   step - When the reset signal value changes from nonzero at the   previous time step to zero at the current time step |
| `Level hold` | Reset when the reset signal is nonzero at the current time step |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ExternalReset` |
| **Type**: character vector |
| **Values**: `'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **Default**: `'None'` |

### **Input processing** — Sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based
processing.

- `Elements as channels (sample based)`
  — Process each element of the input as an independent
  channel.
- `Columns as channels (frame based)`
  — Process each column of the input as an independent
  channel.

  **Note**

  Frame-based processing requires a DSP System Toolbox license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputProcessing` |
| **Type:** character vector |
| **Values:** `'Elements as channels (sample based)' | 'Columns as channels (frame based)'` |
| **Default:** `'Elements as channels (sample based)'` |

### **Optimize by skipping divide by leading denominator coefficient (a0)** — Skip divide by a0 `off` (default) | `on`

When you select this check box, the block does not divide by
*a0* either in
simulation or in the generated code. This parameter optimizes your code.
An error occurs if you specify the denominator coefficients in the block
dialog box and *a0* ≠ 1.

If you specify the denominator coefficients from the input port
**Den**, you must select the **Optimize by
skipping divide by leading denominator coefficient (a0)**
parameter. When you select this checkbox, the block ignores the leading
denominator coefficient *a0* and
replaces it with 1.

When you clear this check box, the block is fully tunable during simulation. It divides
by *a0* in both simulation and
code generation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a0EqualsOne` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

### **View Filter Response** — View filter response button

Click this button to open the Filter Visualization Tool (`fvtool` (DSP System Toolbox)) and display the filter response of the filter
defined in the block dialog box.

#### Dependencies

To enable this parameter, set the **Numerator Source** and
**Denominator Source** parameters to
`Dialog`.

This parameter appears only if you have a valid DSP System Toolbox license.

### Data Types

### **State** — State data type `Inherit: Same as input` (default) | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the state data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as input'` |

### **Numerator coefficients** — Numerator coefficient data type `Inherit: Inherit via internal rule` (default) | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the numerator coefficient data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `NumCoefDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Numerator coefficient minimum** — Minimum value of numerator coefficients `[]` (default) | scalar

Specify the minimum value that a numerator coefficient can have. The
default value is `[]` (unspecified). Simulink® software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumCoefMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Numerator coefficient maximum** — Maximum value of numerator coefficients `[]` (default) | scalar

Specify the maximum value that a numerator coefficient can have. The
default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumCoefMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Numerator product output** — Numerator product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the product output data type for the numerator coefficients.
You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumProductDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Numerator accumulator** — Numerator accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the accumulator data type for the numerator coefficients. You
can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumAccumDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Denominator coefficients** — Denominator coefficient data type `Inherit: Inherit via internal rule` (default) | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the denominator coefficient data type. You can set it
to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenCoefDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Denominator coefficient minimum** — Minimum value of denominator coefficients `[]` (default) | scalar

Specify the minimum value that a denominator coefficient can have. The
default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenCoefMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Denominator coefficient maximum** — Maximum value of denominator coefficients `[]` (default) | scalar

Specify the maximum value that a denominator coefficient can have. The
default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenCoefMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Denominator product output** — Denominator product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the product output data type for the denominator coefficients.
You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenProductDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Denominator accumulator** — Denominator accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the accumulator data type for the denominator coefficients.
You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenAccumDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Output** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Output minimum** — Minimum value of output `[]` (default) | scalar

Specify the minimum value that the block can output. The default value
is `[]` (unspecified). Simulink uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Output maximum** — Maximum value of output `[]` (default) | scalar

Specify the maximum value that the block can output. The default value
is `[]` (unspecified). Simulink uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

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

### State Attributes

### **State name** — Unique name for block state `''` (default) | alphanumeric string

Use this parameter to assign a unique name to the block state. The default is `' '`. When this field is blank, no name is assigned. When using this parameter, remember these considerations:

- A valid identifier starts with an alphabetic or underscore character, followed by alphanumeric or underscore characters.
- The state name applies only to the selected block.

This parameter enables **State name must resolve to Simulink signal object** when you click **Apply**.

For more information, see C Data Code Interface Configuration for Model Interface Elements (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateName` |
| **Type:** character vector |
| **Values:** unique name |
| **Default:** `''` |

### **State name must resolve to Simulink signal object** — Require state name resolve to a signal object `off` (default) | `on`

Select this check box to require that the state name resolves to a Simulink signal object.

#### Dependencies

To enable this parameter, specify a value for **State name**. This parameter appears only if you set the model configuration parameter **Signal resolution** to a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateMustResolveToSignalObject` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Libraries

Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `integera` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block only supports signed fixed-point data types. | |

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
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |

**Restrictions**

- Double data types are not supported for this block. Use single
  data types instead.
- Frame, matrix, and vector input data types are not
  supported.
- The leading denominator coefficient (a0) must be 1 or -1.
- Setting the data type as `Inherit: Inherit via internal
  rule` is not supported.

The Discrete Transfer Fcn block is excluded from the following optimizations:

- Resource sharing
- Distributed pipelining

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block only supports signed fixed-point data types.

## Version History

**Introduced before R2006a**

### R2024b: View filter response

Click the **View Filter Response** button to visualize the frequency
response of the filter that you specify in the block dialog box.

### R2024a: The Discrete Transfer Fcn block supports variable-size input signals

The Discrete Transfer Fcn block supports variable-size input
signals when you set the **Input processing** parameter to
`Columns as channels (frame based)`.

When the input is a variable-size signal, you can change the frame size (number of
rows) of the signal during simulation but the number of channels (columns) must
remain constant.

### R2023b: Conditional display of the **Sample time** parameter

The Discrete Transfer Fcn block no longer displays the **Sample
time** parameter in the block parameters dialog box by default. The
parameter is visible only if you set the sample time to a value other the default
value (`-1`) at the command line or in an existing model. For more
information, see Blocks for Which Sample Time Is Not Recommended.

## Description

Implement discrete transfer function

The Discrete Transfer Fcn block implements the *z*-transform
transfer function as follows:

H(z)=num(z)den(z)=num0zm+num1zm−1+...+nummden0zn+den1zn−1+...+denn

where m+1 and n+1 are the number of numerator and denominator coefficients,
respectively. *num* and *den* contain the coefficients
of the numerator and denominator in descending powers of *z*.
*num* can be a vector or matrix, while *den* must
be a vector. The order of the denominator must be greater than or equal to the order of
the numerator.

Specify the coefficients of the numerator and denominator polynomials in descending powers
of *z*. This block lets you use polynomials in *z* to
represent a discrete system, a method that control engineers typically use. Conversely,
the Discrete Filter block lets you use polynomials in
*z-1* (the delay operator) to
represent a discrete system, a method that signal processing engineers typically use.
The two methods are identical when the numerator and denominator polynomials have the
same length.

The Discrete Transfer Fcn block applies the *z*-transform
transfer function to each independent channel of the input. The **Input
processing** parameter allows you to specify whether the block treats each
column of the input as an individual channel (frame-based processing) or each element of
the input as an individual channel (sample-based processing). To perform frame-based
processing, you must have a DSP System Toolbox™ license.

### Specifying Initial States

Use the **Initial states** parameter to specify the initial filter states.
The initial states you specify are the initial conditions of the unit delay blocks
that are used in the filter digram implementing the discrete transfer
function.

To determine the number of initial states you must specify and how to specify
them, use the following tables.

**Frame-Based Processing**

| Input | Number of Channels | Valid Initial States (Dialog Box) | Valid Initial States (Input Port) |
| --- | --- | --- | --- |
| - Column vector (*K*-by-1) - Unoriented vector (*K*) | 1 | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) | - Scalar - Column vector (*M*-by-1) |
| - Row vector (1-by-*N*) - Matrix (*K*-by-*N*) | *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-*N*) | - Scalar - Matrix (*M*-by-*N*) |

**Sample-Based Processing**

| Input | Number of Channels | Valid Initial States (Dialog Box) | Valid Initial States (Input Port) |
| --- | --- | --- | --- |
| - Scalar | 1 | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) |
| - Row vector (1-by-*N*) - Column vector (*N*-by-1) - Unoriented vector (*N*) | *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-*N*) | - Scalar |
| - Matrix (*K*-by-*N*) | *K* × *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-(*K*×*N*)) | - Scalar |

When the **Initial states** is a scalar, the block initializes all filter
states to the same scalar value. To initialize all states to zero, enter
`0`. When the **Initial states** is a vector
or a matrix, each vector or matrix element specifies a unique initial state for a
corresponding delay element in a corresponding channel:

- The vector length must equal the number of delay elements in the
  filter, `M = max(number of zeros, number of
  poles)`.
- The matrix must have the same number of rows as the number of delay
  elements in the filter, `M = max(number of zeros, number of
  poles)`. The matrix must also have one column for each
  channel of the input signal.

The following example shows the relationship between the initial filter output and the
initial input and state. Given an initial input
*u1*, the first output
*y1* is related to the initial state
[*x1*,
*x2*] and initial input by as
follows:

y1=4x1x2=1/2(u1−3x1)
