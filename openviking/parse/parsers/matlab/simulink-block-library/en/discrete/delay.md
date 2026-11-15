---
type: simulink-block
title: 'Delay'
family: discrete
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'delay'
language: en
---

# Delay

## Ports

### Input

### **u** — Data input signal scalar | vector

Input data signal delayed according to parameters settings.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **d** — Delay length scalar

Delay length specified as inherited from an input port. Enabled when
you select the **Delay length: Source** parameter as
`Input port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Enable** — External enable signal scalar

Enable signal that enables or disables execution of the block. To
create this port, select the **Show enable port**
parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **External reset** — External reset signal scalar

External signal that resets execution of the block to the initial
condition. To create this port, select the **External
reset** parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **x0** — Initial condition scalar | vector

Initial condition specified as inherited from an input port. Enabled
when you select the **Initial Condition: Source**
parameter as `Input port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal that is the input signal delayed by the length of time
specified by the parameter **Delay length**. The
initial value of the output signal depends on several conditions. See
Initial Block Output.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

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

Specify the scalar delay length as a real, nonnegative integer. The
maximum delay length varies. It is determined by the equation:
*delay\_length* < *2147483647* /
(*bytes\_per\_element* \*
*number\_of\_elements*), where the maximum value that
can be held by an integer type (`intmax`) is
`2147483647`. For example, if the following is
true:

- *number\_of\_elements* =
  `1`
- *bytes\_per\_element* =
  `8`

Then the maximum allowed delay length must be less than
`2147483647/(1 * 8)`, which is
`268435455`. If the delay length is
`268435456` or greater, the block returns an error
message like this:

```
Error:In block  'untitled/Delay', total memory requested
for state is larger than the maximum supported number,
which is '2147483647' bytes for simulation.
To avoid this error, please decrease the value of 'DelayLength'.
```

An out-of-range or noninteger value in the dialog box (fixed delay)
returns an error. An out-of-range value from an input port (variable
delay) casts it into the range. A noninteger value from an input port
(variable delay) truncates it to the integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DelayLengthSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Input port'` |
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
| **Values**: `'Dialog'` | `'Input port'` |
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
speed.

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
the **Input processing** mode.

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

Simulink / Commonly Used Blocks Simulink / Discrete DSP System Toolbox / Signal Operations HDL Coder / Commonly Used Blocks HDL Coder / Discrete

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Direct feedthrough characteristics for this block depend on block parameter values. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or
`memset` functions (`string.h`) under
certain conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides configuration options that affect HDL implementation and
synthesized logic.

| Block Parameter Setting | Description |
| --- | --- |
| Set **External reset** to `Level`. | Generates a reset port in the HDL code. |
| Select **Show enable port**. | Generates an enable port in the HDL code. |
| For **Initial condition**, set **Source** to `Dialog` and enter the value. | Specifies an initial condition for the block. |
| Set **Input processing** to `Columns as channels (frame based)` or `Elements as channels (sample based)`. | Expects vector input data, where each element of the vector represents a sample in time. |

**Additional Settings When Using State Control Block**

If you use a State Control block with the Delay
block inside a subsystem in your Simulink model, use these additional settings.

| Block Parameter Setting | Description |
| --- | --- |
| Set **External reset** to `Level hold` for `Synchronous` mode and `Level` for `Classic` mode of the State Control block. | Generates a reset port in the HDL code. |
| Set **Delay length** to zero for a Delay block with an external enable port. | Treated as a wire in only `Synchronous` mode of the State Control block. |
| Set **Delay length** to zero for a Delay block with an external reset port. | Treated as a wire in `Synchronous` and `Classic` modes of the State Control block. |

For more information about the State Control block, see State Control (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | Allow delay to be distributed or absorbed during the distributed pipelining and delay absorption optimizations. The default is `inherit`. For more details, see AllowDelayDistribution (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |
| **UseRAM** | Map delays to RAM instead of registers. The default is `off`. See also UseRAM (HDL Coder). |

**Variable Integer Delay Support**

- You can generate HDL code for the Delay block that has
  **Delay Length** set through the
  `Input port`. Input delay length can be
  integer types or floating-point types.
- The code generation supports positive integer values at the 'd' port
  of the delay block. The delay length set through the input port must be
  between `0` and `Upper limit`,
  specified in the Block Parameters dialog box.
- For negative delay length values, HDL Coder translates these negative delay length to
  `0`.
- Similarly, if you specify delay length greater than the upper limit,
  HDL Coder translates the delay length to the `Upper
  limit` value.
- Upper limit range is defined by the range of the delay length input
  data type. For example, if you specify delay length input data type as
  `uint8`, then the upper limit must not exceed
  `255`.
- You can use enable and reset ports for the variable integer Delay
  block.

**Complex Data Support**

This block supports code generation for complex signals.

**Use Structures as Initial Values**

You can generate HDL code for Delay blocks that use structures to specify the
initial conditions for the Delay block. When you use bus input for a Delay block
in your model, you can set initial condition for the delay block with a
structure value to initialize the bus delay.

To specify initial conditions defined by structures:

1. Define a structure in the model workspace, MATLAB® base workspace, mask workspace, or Simulink data dictionary.
2. Assign the initial condition value to this structure.
3. Set the **Initial Condition** parameter to
   `Dialog` and input the structure in the
   **Value** field.

You also use structures as the initial values in other delay blocks, including the Unit Delay and Tapped Delay blocks

**Restrictions**

- For **Initial condition**,
  **Source** set to `Input
  port` is not supported for HDL code
  generation.
- HDL code generation supports only the Boolean data type at the
  Reset and Enable ports.
- HDL Block Property **UseRAM** for RAM mapping is
  not supported for Delay block that has **Delay
  Length** set through the `Input
  port`.
- The Delay block that has **Delay Length**
  set through the `Input port` does not
  support bus and matrix data input for HDL code generation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Delay input signal by fixed or variable sample periods

The Delay block outputs the input of the block after a delay. The block
determines the delay time based on the value of the **Delay length**
parameter. The block supports:

- Variable delay length
- Specification of the initial condition from an input port
- State storage
- Using a circular buffer instead of an array buffer for state storage
- Resetting the state to the initial condition with an external reset
  signal
- Controlling execution of the block at every time step with an external enable
  signal

The initial block output depends on several factors such as the **Initial
condition** parameter and the simulation start time. For more information,
see Initial Block Output. The **External reset** parameter
determines if the block output resets to the initial condition on triggering. The
**Show enable port** parameter determines if the block execution is
controlled in every time step by an external enable signal.

### Initial Block Output

The output in the first few time steps of the simulation depends on the block
sample time, the delay length, and the simulation start time. The block supports
specifying or inheriting discrete sample times to determine the time interval
between samples. For more information, see Specify Sample Time.

The table shows the Delay block output for the first few time steps with these
settings. The block inherits a discrete sample time as
`[Tsampling,Toffset]`,
where `Tsampling` is the sampling period
and `Toffset` is the initial time
offset. *`n`* is the value of the **Delay
length** parameter and
`Tstart` is the simulation start
time for the model

| Simulation Time Range | Block Output |
| --- | --- |
| `(Tstart)` to `(Tstart + Toffset)` | Zero |
| `(Tstart + Toffset)` to `(Tstart + Toffset + n * Tsampling)` | **Initial condition** parameter |
| After `(Tstart + Toffset + n * Tsampling)` | Input signal |

### Behavior with External Enable Signal

Selecting the **Show enable port** check box enables the Enable
port. If the enable port is enabled, the block operates in this order

1. Checks if the enable condition is satisfied.
2. If the reset port is enabled, checks the reset condition.
3. Performs the Delay block functionality.

The block has this operation with the Enable port:

- At the first block enable, the block output is the initial condition value
  (`x0`).
- For consecutive enable signals, the block takes the last state of the
  input signal u.
- If the port is not enabled at the start of simulation, the
  Delay block outputs `0`.
- During simulation, if the port becomes disabled after having been enabled,
  the block does not execute and holds its last value.

### Variable-Size Support

The Delay block provides the following support for variable-size
signals:

- The data input port `u` accepts variable-size signals.
  The other input ports do not accept variable-size signals.
- The output port has the same signal dimensions as the data input port
  `u` for variable-size inputs.

The rules that apply to variable-size signals depend on the input processing mode
of the Delay block.

| Input Processing Mode | Rules for Variable-Size Signal Support |
| --- | --- |
| `Elements as channels (sample based)` | - The signal dimensions change only during state reset   when the block is enabled. - The initial condition must be scalar. |
| `Columns as channels (frame based)` | - No support |

### Bus Support

The Delay block provides the following support for bus
signals:

- The data input `u` accepts virtual and nonvirtual bus
  signals. Other than input port `x0`, the other input ports
  do not accept bus signals.
- The initial condition `x0` port accepts nonvirtual bus
  signals.
- The output port has the same bus type as the data input port
  `u` for bus inputs.
- Buses work with:

  - Sample-based and frame-based processing
  - Fixed and variable delay length
  - Array and circular buffers

To use a bus signal as the input to a Delay block, specify the
initial condition on the dialog box or through the `x0` port.
Support for virtual and nonvirtual buses depends on the initial condition that you
specify and whether the **State name** parameter is empty or not.
For the `x0` input port, only nonvirtual buses are
supported.

| Initial Condition | State Name | |
| --- | --- | --- |
| Empty | Not Empty |
| Zero | Virtual and nonvirtual bus support | Nonvirtual bus support only |
| Nonzero scalar | Virtual and nonvirtual bus support | No bus support |
| Nonscalar | No bus support | No bus support |
| Structure | Virtual and nonvirtual bus support | Nonvirtual bus support only |
| Partial structure | Virtual and nonvirtual bus support | Nonvirtual bus support only |

### String Support

The Delay block can accept and output string data type only
if:

- The block is configured for the default value of the **Initial
  condition** parameter (0).
- The **Delay length** value is 1 or less.
