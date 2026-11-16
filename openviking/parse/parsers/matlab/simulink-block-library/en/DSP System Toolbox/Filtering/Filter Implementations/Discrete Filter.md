---
type: simulink-block
title: 'Discrete Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'discretefilter'
documentation_source_path: '../simulink/slref/discretefilter.html'
language: en
---

# Discrete Filter

## Ports

### Input

### **u** — Input signal scalar | vector | matrix

Input signal to filter, specified as a scalar, vector, or
matrix.

When you set the **Input
processing** parameter to `Columns as channels
(frame based)`, the block supports variable-size input
signals, that is, you can change the frame size (number of rows) of the
signal during simulation but the number of channels (columns) must
remain constant. *(since R2024a)*

#### Dependencies

The name of this port depends on the source you specify for the
numerator coefficients, denominator coefficients and initial states.
When you set **Numerator**,
**Denominator**, and **Initial
states** to `Dialog`, there is
only one input port, and the port is unlabeled. When you set
**Numerator**,
**Denominator**, or **Initial
states** to `Input port`, this
port is labeled **u**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Num** — Numerator coefficients scalar | vector

Numerator coefficients of the discrete filter, specified as descending powers of
*z*. Use a row vector to specify the coefficients
for a single numerator polynomial.

#### Dependencies

To enable this port, set **Numerator Source** to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Den** — Denominator coefficients scalar | vector

Denominator coefficients of the discrete filter, specified as
descending powers of *z*. Use a row vector to specify
the coefficients for a single denominator polynomial.

#### Dependencies

To enable this port, set **Denominator Source**
to `Input port`.

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

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **x0** — Initial states scalar | vector | matrix

Initial states, specified as a scalar, vector, or matrix. For more information about
specifying states, see Specifying Initial States.

#### Dependencies

To enable this port, set the **Filter structure**
to `Direct form II` or `Direct
form II transposed`, and set **Initial
states** to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **Port\_1** — Filtered output signal scalar | vector | matrix

Filtered output signal. The output dimensions equal the input dimensions, except when
you specify a matrix of filter taps for the **Numerator
coefficients** parameter. When you do so, the output
dimensions depend on the number of different sets of filter taps you
specify.

When you set **Sample time** to
`-1`, sample time of the output signal is same as the
sample time of the input signal **u**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## Parameters

### Main

### **Filter structure** — Filter structure `Direct form II` (default) | `Direct form I transposed` | `Direct form I` | `Direct form II transposed`

Specify the discrete IIR filter structure.

#### Dependencies

To use any filter structure other than `Direct form
II`, you must have an available DSP System Toolbox license.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FilterStructure` |
| **Type:** character vector |
| **Values:** `'Direct form II' | 'Direct form I transposed' | 'Direct form I' | 'Direct form II transposed'` |
| **Default:** `'Direct form II'` |

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

Specify the numerator coefficients of the discrete filter as descending powers of
*z*. Use a row vector to specify the coefficients
for a single numerator polynomial. To specify coefficients for multiple
filters, specify a matrix of coefficients, where each row represents a
different set of filter taps. To implement multiple filters,
**Filter structure** must be `Direct
form II`, **Input processing** must be
`Elements as channels (sample based)`, and
the input must be a scalar.

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

### **Denominator Value** — Denominator coefficients `[1 0.5]` (default) | vector

Specify the denominator coefficients of the discrete filter as
descending powers of *z*. Use a row vector to specify
the coefficients for a single denominator polynomial.

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
| **Values:** scalar | vector |
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

Specify the initial filter states as a scalar, vector, or matrix. To learn how to
specify initial states, see Specifying Initial States.

#### Dependencies

To enable this parameter, set the **Filter
structure** to `Direct form
II` or `Direct form II
transposed`, and set **Initial states
Source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStates` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

Alternatively, use
`IC`.

### **Initial states on numerator side** — Initial numerator states `0` (default) | scalar | vector | matrix

Specify the initial numerator filter states as a scalar, vector, or
matrix. To learn how to specify initial states, see Specifying Initial States.

#### Dependencies

To enable this port, set the **Filter structure**
to `Direct form I` or `Direct
form I transposed`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStates` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

### **Initial states on denominator side** — Initial denominator states `0` (default) | scalar | vector | matrix

Specify the initial denominator filter states as a scalar, vector, or
matrix. To learn how to specify initial states, see Specifying Initial States.

#### Dependencies

To enable this port, set the **Filter structure**
to `Direct form I` or `Direct
form I transposed`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialDenominatorStates` |
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

Specify whether the block performs sample- or frame-based processing.

- `Elements as channels (sample based)`
  — Process each element of the input as an independent
  channel.
- `Columns as channels (frame based)`
  — Process each column of the input as an independent
  channel.

#### Dependencies

Frame-based processing requires a DSP System Toolbox license.

For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputProcessing` |
| **Type:** character vector |
| **Values:** `'Columns as channels (frame based)' | 'Elements as channels (sample based)'` |
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

Specify the state data type. You can set this parameter to:

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

Specify the numerator coefficient data type. You can set this
parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in signed integer, for example,
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
| **Block Parameter:** `NumCoefDataTypeStr` |
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
You can set this parameter to:

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
can set this parameter to:

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

Specify the denominator coefficient data type. You can set this
parameter to:

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
You can set this parameter to:

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
You can set this parameter to:

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

Specify the output data type. You can set this parameter to:

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
is `[]` (unspecified). Simulink software uses this value to perform:

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
is `[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Multiplicand data type** — Multiplicand data type `Inherit: Same as input` (default) | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the multiplicand data type. You can set this parameter
to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set the **Filter
structure** to `Direct form I
transposed`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MultiplicandDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as input'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock data type settings of this block against changes by the
Fixed-Point Tool and the Fixed-Point Advisor. For more information,
see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations.
For more information, see Rounding Modes (Fixed-Point Designer).

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

### State Attributes

### **State name** — Assign unique name to each state `' '` (default) | `'position'` | `{'a', 'b', 'c'}` | `a` | ...

Assign a unique name to each state. If this field is blank (`'
'`), no name assignment occurs.

- To assign a name to a single state, enter the name between
  quotes, for example, `'position'`.
- To assign names to multiple states, enter a comma-delimited
  list surrounded by braces, for example, `{'a', 'b',
  'c'}`. Each name must be unique.
- To assign state names with a variable in the MATLAB® workspace, enter the variable without quotes. A
  variable can be a character vector, cell array, or
  structure.

#### Limitations

- The state names apply only to the selected block.
- The number of states must divide evenly among the number
  of state names.
- You can specify fewer names than states, but you cannot
  specify more names than states.

  For example, you can specify two names in a system with
  four states. The first name applies to the first two states
  and the second name to the last two states.

#### Dependencies

To enable this parameter, set **Filter
structure** to `Direct form
II`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateName` |
| **Type:** character vector |
| **Values:** `' '` | user-defined |
| **Default:** `' '` |

### **State name must resolve to Simulink signal object** — Require state name resolve to a signal object `off` (default) | `on`

Select this check box to require that the state name resolves to a
Simulink signal object.

#### Dependencies

To enable this parameter, set **Filter
structure** to `Direct form
II` and specify a value for **State
name**. This parameter appears only if you set the
model configuration parameter **Signal resolution**
to a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateMustResolveToSignalObject` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Libraries

Simulink / Discrete DSP System Toolbox / Filtering / Filter Implementations

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

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block only supports signed fixed-point data types.

The Discrete Filter block accepts and outputs real and complex signals of any
signed numeric data type that Simulink supports. The block supports the same types for the numerator and
denominator coefficients.

Numerator and denominator coefficients must have the same complexity. They can
have different word lengths and fraction lengths.

The following diagrams show the filter structure and the data types used within
the Discrete Filter block for fixed-point signals.

The block omits the dashed divide when you select the **Optimize by
skipping divide by leading denominator coefficient (a0)**
parameter.

## Version History

**Introduced before R2006a**

### R2024b: View filter response

Click the **View Filter Response** button to visualize the
frequency response of the filter that you specify in the block dialog box.

### R2024a: The Discrete Filter block supports variable-size input signals

The Discrete Filter block supports variable-size input signals when
you set the **Input processing** parameter to `Columns
as channels (frame based)`.

When the input is a variable-size signal, you can change the frame size (number of
rows) of the signal during simulation but the number of channels (columns) must
remain constant.

### R2023b: Conditional display of the **Sample time** parameter

The Discrete Filter block no longer displays the **Sample
time** parameter in the block parameters dialog box by default. The
parameter is visible only if you set the sample time to a value other the default
value (`-1`) at the command line or in an existing model. For more
information, see Blocks for Which Sample Time Is Not Recommended.

## Description

Model Infinite Impulse Response (IIR) filters

The Discrete Filter block independently filters each channel of the input
signal with the specified digital IIR filter. You can specify the filter structure as
`Direct form I`, `Direct form I transposed`,
`Direct form II`, or `Direct form II transposed`.
The block implements static filters with fixed coefficients. You can tune the
coefficients of these static filters.

This block filters each channel of the input signal independently
over time. The **Input processing** parameter allows
you to specify how the block treats each element of the input. You
can specify treating input elements as an independent channel (sample-based
processing), or treating each column of the input as an independent
channel (frame-based processing). To perform frame-based processing,
you must have a DSP System Toolbox™ license.

The output dimensions equal the input dimensions, except when you specify a matrix of filter
taps for the **Numerator coefficients** parameter. When you do so, the
output dimensions depend on the number of different sets of filter taps you
specify.

Use the **Numerator coefficients** parameter
to specify the coefficients of the discrete filter numerator polynomial.
Use the **Denominator coefficients** parameter to
specify the coefficients of the denominator polynomial of the function.
The **Denominator coefficients** parameter must be a vector of coefficients.

Specify the coefficients of the numerator and denominator polynomials in ascending powers of
*z-1*. The Discrete
Filter block lets you use polynomials in
*z-1* (the delay operator) to
represent a discrete system. Signal processing engineers typically use this method.
Conversely, the Discrete Transfer Fcn block lets you use
polynomials in *z* to represent a discrete system. Control engineers
typically use this method. When the numerator and denominator polynomials have the same
length, the two methods are identical.

### Specifying Initial States

In **Dialog parameters** and **Input port(s)** modes, the block initializes the internal filter
states to zero by default, which is equivalent to assuming past inputs
and outputs are zero. You can optionally use the **Initial states** parameter to specify nonzero initial states for the filter delays.

To determine the number of initial state values you must specify, and how to specify them,
see the following table on valid initial states and Number of Delay Elements (Filter States). The **Initial
states** parameter can take one of four forms as described in the
following table.

**Valid Initial States**

| Initial state | Examples | Description |
| --- | --- | --- |
| Scalar | `5`  Each delay element for each channel is set to `5`. | The block initializes all delay elements in the filter to the scalar value. |
| Vector   (for applying the same delay elements to each channel) | For a filter with two delay elements: [*d1**d2*]  The delay elements for all channels are d1 and d2. | Each vector element specifies a unique initial condition for a corresponding delay element. The block applies the same vector of initial conditions to each channel of the input signal. The vector length must equal the number of delay elements in the filter (specified in the table Number of Delay Elements (Filter States)). |
| Vector or matrix   (for applying different delay elements to each channel) | For a three-channel input signal and a filter with two delay elements:  [*d*1*d2**D1**D2**d1**d2*] or    [d1D1d1d2D2d2]    - The delay elements for channel 1 are   *d1* and   *d2*. - The delay elements for channel 2 are   *D1* and   *D2*. - The delay elements for channel 3 are   *d1*and   *d2*. | Each vector or matrix element specifies a unique initial condition for a corresponding delay element in a corresponding channel:  - The vector length must be equal to the product of   the number of input channels and the number of delay elements in the   filter (specified in the table Number of Delay Elements (Filter States)). - The matrix must have the same number of rows as the   number of delay elements in the filter (specified in the table Number of Delay Elements (Filter States)), and must have one column for each channel of the input signal. |
| Empty matrix | `[ ]`  Each delay element for each channel is set to `0`. | The empty matrix, `[]`, is equivalent to setting the **Initial conditions** parameter to the scalar value `0`. |

The number of delay elements (filter states) per input channel depends on the filter structure, as indicated in the following table.

**Number of Delay Elements (Filter States)**

| Filter Structure | Number of Delay Elements Per Channel |
| --- | --- |
| `Direct form I   Direct form I transposed` | - `number of zeros - 1` - `number of poles - 1` |
| `Direct form II   Direct form II transposed` | `max(number of zeros, number of poles)-1` |

The following tables describe the valid initial states for different sizes of input and
different number of channels depending on whether you set the  **Input
processing** parameter to frame based or sample based.

**Frame-Based Processing**

| Input | Number of Channels | Valid Initial States (Dialog Box) | Valid Initial States (Input Port) |
| --- | --- | --- | --- |
| - Column vector (*K*-by-1) - Unoriented vector (*K*) | 1 | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) | - Scalar - Column vector (*M*-by-1) |
| - Row vector (1-by-*N*) - Matrix (*K*-by-*N*) | *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-*N*) | - Scalar - Matrix (*M*-by-*N*) |

**Sample-Based Processing**

| Input | Number of Channels | Valid Initial States (Dialog Box) | Valid Initial States (Input Port) |
| --- | --- | --- | --- |
| - Unoriented scalar | 1 | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) |
| - Row vector (1-by-*N*) - Column vector (*N*-by–1) - Unoriented vector (*N*) | *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-*N*) | - Scalar |
| - Matrix (*K*-by-*N*) | *K* × *N* | - Scalar - Column vector (*M*-by-1) - Row vector (1-by-*M*) - Matrix (*M*-by-(*K*×*N*)) | - Scalar |

When the **Initial states** is a scalar, the block initializes all filter
states to the same scalar value. Enter `0` to initialize all states
to zero. When the **Initial states** is a vector or a matrix, each
vector or matrix element specifies a unique initial state. This unique state
corresponds to a delay element in a corresponding channel:

- The vector length must equal the number of delay elements in the
  filter, `M = max(number of zeros, number of
  poles)`.
- The matrix must have the same number of rows as the number of delay
  elements in the filter, `M = max(number of zeros, number of
  poles)`. The matrix must also have one column for each
  channel of the input signal.

The relationship between the initial filter output
*y1*, the initial input
*u1*, and the initial state
[*x1*,
*x2*] is given by the following
equation.

y1=b1[(u1−a2x1−a3x2)a1]+b2x1+b3x2

where,

- *b1*,
  *b2*, and
  *b3* are the numerator
  coefficients of the discrete filter.
- *a1*,
  *a2*, and
  *a3* are the denominator
  coefficients of the discrete filter.
