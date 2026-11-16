---
type: simulink-block
title: 'Variable Integer Delay'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'variableintegerdelay'
documentation_source_path: 'slref/variableintegerdelay.html'
language: en
---

# Variable Integer Delay

## Ports

### Input

### **u** — Data input signal scalar | vector

Input data signal delayed according to parameters settings.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **d** — Delay length scalar

Delay length specified as inherited from an input port. Enabled when
you select the **Delay length: Source** parameter as
`Input port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Enable** — External enable signal scalar

Enable signal that enables or disables execution of the block. To create this port,
select the **Show enable port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **External reset** — External reset signal scalar

External signal that resets execution of the block to the initial condition. To create
this port, select the **External reset**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **x0** — Initial condition scalar | vector

Initial condition specified as inherited from an input port. Enabled
when you select the **Initial Condition: Source**
parameter as `Input port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal that is the input signal delayed by the length of time
specified by the parameter **Delay length**. The
initial value of the output signal depends on several conditions. See
Initial Block Output.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### Main

### **Delay length** — Delay length `Dialog` (default) | `Input port`

Specify whether to enter the delay length directly on the dialog box
(fixed delay) or to inherit the delay from an input port (variable
delay).

- If you set **Source** to
  `Dialog`, enter the delay length in
  the edit field under **Value**.
- If you set **Source** to `Input
  port`, verify that an upstream signal supplies
  a delay length for the `d` input port. You can
  also specify its maximum value by specifying the parameter
  **Upper limit**.

Specify the scalar delay length as a real, non-negative integer. An
out-of-range or non-integer value in the dialog box (fixed delay)
returns an error. An out-of-range value from an input port (variable
delay) casts it into the range. A non-integer value from an input port
(variable delay) truncates it to the integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DelayLengthSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Input port'` | |
| **Default**: `'Dialog'` |

|  |
| --- |
| **Block Parameter**: `DelayLength` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'2'` |

|  |
| --- |
| **Block Parameter**: `DelayLengthUpperLimit` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'100'` |

### **Initial condition** — Initial condition `Dialog` (default) | `Input port`

Specify whether to enter the initial condition directly on the dialog
box or to inherit the initial condition from an input port.

- If you set **Source** to
  `Dialog`, enter the initial
  condition in the edit field under
  **Value**.
- If you set **Source** to `Input
  port`, verify that an upstream signal supplies
  an initial condition for the `x0` input
  port.

Simulink® converts offline the data type of **Initial
condition** to the data type of the input signal
`u` using a round-to-nearest operation and
saturation.

**Note**

When **State name must resolve to Simulink signal
object** is selected on the **State
Attributes** pane, the block copies the initial value
of the signal object to the **Initial condition**
parameter. However, when the source for **Initial
condition** is `Input port`,
the block ignores the initial value of the signal object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialConditionSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Input port'` | |
| **Default**: `'Dialog'` |

|  |
| --- |
| **Block Parameter**: `InitialCondition` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0.0'` |

### **Input processing** — Specify sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing:

- `Columns as channels (frame based)` — Treat
  each column of the input as a separate channel (frame-based processing).

  **Note**

  Frame-based processing requires a DSP System Toolbox™ license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).
- `Elements as channels (sample based)` — Treat
  each element of the input as a separate channel (sample-based
  processing).

Use **Input processing** to specify whether the block performs
sample- or frame-based processing. For more information about these two processing
modes, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputProcessing` |
| **Type**: character vector |
| **Values**: `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **Default**: `'Elements as channels (sample based)'` |

### **Use circular buffer for state** — Circular buffer for storing state `off` (default) | `on`

Select to use a circular buffer for storing the state in simulation
and code generation. Otherwise, an array buffer stores the state.

Using a circular buffer can improve execution speed when the delay
length is large. For an array buffer, the number of copy operations
increases as the delay length goes up. For a circular buffer, the number
of copy operations is constant for increasing delay length.

If one of the following conditions is true, an array buffer always
stores the state because a circular buffer does not improve execution
speed:

- For sample-based signals, the delay length is 1.
- For frame-based signals, the delay length is no larger than
  the frame size.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `UseCircularBuffer` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Prevent direct feedthrough** — Prevent direct feedthrough `off` (default) | `on`

Select to increase the delay length from zero to the lower limit for
the **Input processing** mode:

- For sample-based signals, increase the minimum delay length to
  1.
- For frame-based signals, increase the minimum delay length to
  the frame length.

Selecting this check box prevents direct feedthrough from the input
port, `u`, to the output port. However, this check box
cannot prevent direct feedthrough from the initial condition port,
`x0`, to the output port.

#### Dependency

To enable this parameter, set **Delay length:
Source** to `Input
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PreventDirectFeedthrough` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Remove delay length check in generated code** — Remove delay length out-of-range check `off` (default) | `on`

Select to remove code that checks for out-of-range delay
length.

| Check Box | Result | When to Use |
| --- | --- | --- |
| Selected | Generated code does not include conditional statements to check for out-of-range delay length. | For code efficiency |
| Cleared | Generated code includes conditional statements to check for out-of-range delay length. | For safety-critical applications |

#### Dependency

To enable this parameter, set **Delay length:
Source** to `Input
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RemoveDelayLengthCheckInGeneratedCode` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Diagnostic for delay length** — Diagnostic checks for delay length `None` (default) | `Warning` | `Error`

Specify whether to produce a warning or error when the input
`d` is less than the lower limit or greater than
the **Delay length: Upper limit**. The lower limit
depends on the setting for **Prevent direct
feedthrough**.

- If the check box is cleared, the lower limit is zero.
- If the check box is selected, the lower limit is 1 for
  sample-based signals and frame length for frame-based
  signals.

Options for the diagnostic include:

- `None` — Simulink software takes no action.
- `Warning` — Simulink software displays a warning and continues the
  simulation.
- `Error` — Simulink software terminates the simulation and displays an
  error.

#### Dependency

To enable this parameter, set **Delay length:
Source** to `Input
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DiagnosticForDelayLength` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'None'` |

### **Show enable port** — Create enable port `off` (default) | `on`

Select to control execution of this block with an enable port. The block is considered
enabled when the input to this port is nonzero, and is disabled when the input is
`0`. The value of the input is checked at the same time step as the
block execution.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowEnablePort` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

### **Sample time (-1 for inherited)** — Discrete interval between sample time hits `-1` (default) | `scalar`

Specify the time interval between samples. To inherit the sample time,
set this parameter to `-1`. This block supports
discrete sample time, but not continuous sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Value**: real scalar |
| **Default**: `'-1'` |

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

Simulink / Discrete

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

Generated code relies on `memcpy` or
`memset` functions (`string.h`) under
certain conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

For information about HDL code generation, see HDL Code Generation on the Delay page.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2012b**

## Description

Delay input signal by variable sample period

The Variable Integer Delay block is a variant
of the Delay block that has the
source of the delay length set to `Input port`, by default.
