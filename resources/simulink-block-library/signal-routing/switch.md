---
type: simulink-block
title: 'Switch'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'switch'
---

# Switch

Switch output between first input and third input based on value of second input

## Libraries

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

## Description

### Types of Block Inputs

The Switch block passes through the first input or the third input
based on the value of the second input. The first and third inputs are called
*data inputs*. The second input is called the
*control input*. Specify the condition under which the
block passes the first input by using the **Criteria for passing first
input** and **Threshold** parameters.

To immediately back propagate a known output data type to the first and third
input ports, set the **Output data type** parameter to
`Inherit: Inherit via internal rule` and select the
**Require all data port inputs to have the same data type**
check box.

**Tip**

For back propagation `Inherit: Inherit via internal rule`, the
**Require all data port inputs to have the same data
type** parameter must be selected. Otherwise, the block does not
automatically back propagate the output data type to the first and third output
ports.

### Limitations on Data Inputs

The sizes of the two data inputs can be different if you select **Allow
different data input sizes**. However, this block does not support
variable-size input signals. Therefore, the size of each input cannot change during
simulation.

If the data inputs to the Switch block are buses, the element names
of both buses must be the same. Using the same element names ensures that the output
bus has the same element names no matter which input bus the block selects. To
ensure that your model meets this requirement, use a bus object to define the buses
and set the **Element name mismatch** diagnostic to
`error`. For more information, see Model Configuration Parameters: Connectivity Diagnostics.

### Block Icon Appearance

The block icon helps you identify **Criteria for passing first
input** and **Threshold** without having to open the
block dialog box.

For information about port order for various block orientations, see Identify Port Location on Rotated or Flipped Block.

### Block Behavior for Boolean Control Input

When the control input is a `Boolean` signal, use one of these
combinations of criteria and threshold value:

- `u2 >= Threshold`, where the threshold value
  equals `1`
- `u2 > Threshold`, where the threshold value
  equals `0`
- `u2 ~=0`

Otherwise, the Switch block ignores the threshold and uses the
Boolean input for signal routing. For a control input of `1`, the
block passes the first input, and for a control input of `0`, the
block passes the third input. In this case, the block icon changes after compile
time and uses `T` and `F` to label the first and
third inputs, respectively.

### Data Type Support

The control input can be of any data type that Simulink® supports, including fixed-point and enumerated types. The control
input cannot be complex. If the control input is enumerated, the
**Threshold** parameter must be a value of the same enumerated
type.

The data inputs can be of any data type that Simulink supports. If either data input is of an enumerated type, the other
must be of the same enumerated type.

When the output is of enumerated type, both data inputs should use the same
enumerated type as the output.

For more information, see Data Types Supported by Simulink.

## Ports

### Input

### **Port\_1** — First data input signal scalar | vector

First of two data inputs. The block propagates either the first or second data input to
the output. The block selects which input to pass based on the control
input. Specify the condition for the control input to pass the first
input using the **Criteria for passing first input**
and **Threshold** parameters.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_2** — Control input signal scalar | vector

Control signal the block uses to determine whether to pass the first
or second data input to the output. If the control input meets the
condition set in the **Criteria for passing first
input** parameter, then the block passes the first data
input. Otherwise, the block passes the second data input.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_3** — Second data input signal scalar | vector

Second of two data inputs. The block propagates either the first or second data input to
the output. The block selects which input to pass based on the control
input. Specify the condition for the control input to pass the first or
second input using the **Criteria for passing first
input** and **Threshold**
parameters.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal propagated from either the first or second input signal, based on the
control signal value.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### Main

### **Criteria for passing first input** — Selection criteria to pass first data input `u2 > Threshold` (default) | `u2 >= Threshold` | `u2 ~= 0`

Select the condition under which the block passes the first data
input. If the control input meets the condition set in the
**Criteria for passing first input** parameter, the
block passes the first input. Otherwise, the block passes the second
data input signal from input `Port_3`.

`u2 >= Threshold`
:   Checks whether the control input is greater than or
    equal to the threshold value.

`u2 > Threshold`
:   Checks whether the control input is greater than the
    threshold value.

`u2 ~= 0`
:   Checks whether the control input is nonzero.

    **Note**

    The Switch block does not support
    `u2 ~= 0` mode for
    enumerated data types.

#### Tip

When the control input is a Boolean signal, use one of these
combinations of condition and threshold value:

- `u2 >= Threshold`, where the
  threshold value equals 1
- `u2 > Threshold`, where the
  threshold value equals 0
- `u2 ~= 0`

Otherwise, the Switch block ignores threshold
values and uses the Boolean value for signal routing. For a value of
1, the block passes the first input, and for a value of 0, the block
passes the third input. A warning message that describes this
behavior also appears in the MATLAB® Command Window.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Criteria` |
| **Type:** character vector |
| **Value:** `'u2 >= Threshold'` | `'u2 > Threshold'` | `'u2 ~= 0'` |
| **Default:** `'u2 > Threshold'` |

### **Threshold** — Threshold used in criteria `0` (default) | `scalar`

Assign the threshold used in the **Criteria for passing first
input** that determines which input the block passes to the
output. **Threshold** must be greater than
**Output minimum** and less than **Output
maximum**.

To specify a nonscalar threshold, use brackets. For example, the
following entries are valid:

- `[1 4 8 12]`
- `[MyColors.Red, MyColors.Blue]`

#### Dependencies

Setting **Criteria for passing first input** to `u2 ~=
0` disables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Threshold` |
| **Type:** character vector |
| **Value:** scalar |
| **Default:** `'0'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector | string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

### Signal Attributes

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

### **Require all data port inputs to have the same data type** — Require data ports to have the same data type `off` (default) | `on`

Require all data inputs to have the same data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Value: `'off'` | `'on'`** |
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

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Enum: <class name>` | `<data type expression>` | `Simulink.ImageType(480,640,3)`

Specify the output data type.

`Inherit: Inherit via internal rule`
:   Uses the following rules to determine the output data
    type.

    | Data Type of First Input Port | Output Data Type |
    | --- | --- |
    | Has a larger positive range than the third input port | Inherited from the first input port |
    | Has the same positive range as the third input port | Inherited from the third input port |
    | Has a smaller positive range than the third input port |
    | Is a Boolean value and third input port is `uint8` |
    | Is `uint8` and third input port is a Boolean value |
    | Is a Boolean value and other is `int8` | Set to a Boolean value |
    | Is `uint8` and other is a Boolean value |

    | Data Types of Two Input Ports | Output Data Type |
    | --- | --- |
    | Has one input type as a Boolean value and another as `uint8` | Set to data type of the third data port |
    | Has one input as a Boolean value and another as `int8` | Set to a Boolean value |

`Inherit: Inherit via back propagation`
:   Adopts the data type from the output block.

`Inherit: Inherit same as first input`
:   Uses data type of the first data input port.

`double`
:   Specifies output data type is
    `double`.

`single`
:   Specifies output data type is
    `single`.

`half`
:   Specifies output data type is
    `half`.

`int8`
:   Specifies output data type is
    `int8`.

`uint8`
:   Specifies output data type is
    `uint8`.

`int16`
:   Specifies output data type is
    `int16`.

`uint16`
:   Specifies output data type is
    `uint16`.

`int32`
:   Specifies output data type is
    `int32`.

`uint32`
:   Specifies output data type is
    `uint32`.

`int64`
:   Specifies output data type is
    `int64`.

`uint64`
:   Specifies output data type is
    `uint64`.

`fixdt(1,16,0)`
:   Specifies output data type is fixed point
    `fixdt(1,16,0)`.

`fixdt(1,16,2^0,0)`
:   Specifies output data type is fixed point
    `fixdt(1,16,2^0,0)`.

`Enum: <class name>`
:   Uses an enumerated data type, for example,
    `Enum: BasicColors`.

`Simulink.ImageType(480,640,3)`
:   Uses a `Simulink.ImageType` (Computer Vision Toolbox) object if you have
    Computer Vision Toolbox™.

`string`
:   Specifies output data type is string.

`<data type expression>`
:   Uses a data type object, for example,
    `Simulink.NumericType`.

#### Tip

When the output is of enumerated type, both data inputs should use
the same enumerated type as the output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'`  | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'`, `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `Enum: <class name>` | `Simulink.ImageType(480,640,3)` | `'string'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Specify the rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Choose one of these rounding modes.

`Ceiling`
:   Rounds both positive and negative numbers
    toward positive infinity. Equivalent to the
    MATLAB
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

### **Allow different data input sizes** — Allow different data input sizes `off` (default) | `on`

Select this check box to allow input signals with different sizes. The
block propagates the input signal size to the output signal. If the two
data inputs are variable-size signals, the maximum size of the signals
can be equal or different.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AllowDiffInputSizes` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or `memset`
functions (string.h) under certain conditions.

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

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
