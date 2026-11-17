---
type: simulink-block
title: 'Enabled Delay'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'enableddelay'
documentation_source_path: '../hdlcoder/ref/enableddelay.html'
language: en
---

# Enabled Delay

## Ports
```yaml
ports:
- name: u
  summary: Data input signal scalar | vector
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus
- name: d
  summary: Delay length scalar
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | fixed point
- name: Enable
  summary: External enable signal scalar
  direction: input
  data_types: Boolean
- name: External reset
  summary: External reset signal scalar
  direction: input
  data_types: Boolean
- name: x0
  summary: Initial condition scalar | vector
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | bus
- name: Port_1
  summary: Output signal scalar | vector
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus
```

### Input

### **u** — Data input signal scalar | vector

Input data signal delayed according to parameters settings.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **d** — Delay length scalar

Delay length specified as inherited from an input port. Enabled when you select
the **Delay length: Source** parameter as `Input
port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Enable** — External enable signal scalar

Enable signal that enables or disables execution of the block. To create this
port, select the **Show enable port** parameter.

**Data Types:** `Boolean`

### **External reset** — External reset signal scalar

External signal that resets execution of the block to the initial condition. To
create this port, select the **External reset** parameter.

**Data Types:** `Boolean`

### **x0** — Initial condition scalar | vector

Initial condition specified as inherited from an input port. Enabled when you
select the **Initial Condition: Source** parameter as
`Input port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal that is the input signal delayed by the length of time specified by
the parameter **Delay length**. The initial value of the output
signal depends on several conditions. See Delay.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
## Parameters
```yaml
parameters:
- name: Delay length
  summary: Delay length Dialog (default) | Input port
  group: Main
  block_parameter: DelayLengthUpperLimit
  type: character vector
  values: scalar
  default: '''100'''
- name: Initial condition
  summary: Initial condition Dialog (default) | Input port
  group: Main
  values: scalar
  block_parameter: InitialCondition
  type: character vector
  default: '''0.0'''
- name: Input processing
  summary: Specify sample- or frame-based processing Elements as channels (sample based) (default) | Columns as channels (frame
    based)
  group: Main
  block_parameter: InputProcessing
  type: character vector
  values: '''Columns as channels (frame based)'' | ''Elements as channels (sample based)'''
  default: '''Elements as channels (sample based)'''
- name: Use circular buffer for state
  summary: Circular buffer for storing state off (default) | on
  group: Main
  block_parameter: UseCircularBuffer
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Prevent direct feedthrough
  summary: Prevent direct feedthrough off (default) | on
  group: Main
  block_parameter: PreventDirectFeedthrough
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Remove delay length check in generated code
  summary: Remove delay length out-of-range check off (default) | on
  group: Main
  block_parameter: RemoveDelayLengthCheckInGeneratedCode
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Diagnostic for delay length
  summary: Diagnostic checks for delay length None (default) | Warning | Error
  group: Main
  block_parameter: DiagnosticForDelayLength
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''None'''
- name: Show enable port
  summary: Create enable port on (default) | off
  group: Main
  block_parameter: ShowEnablePort
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: External reset
  summary: External state reset None (default) | Rising | Falling | Either | Level | Level hold
  group: Main
  block_parameter: ExternalReset
  type: character vector
  values: '''None'' | ''Rising'' | ''Falling'' | ''Either'' | ''Level'' | ''Level hold'''
  default: '''None'''
- name: Sample time (-1 for inherited)
  summary: Discrete interval between sample time hits -1 (default) | scalar
  group: Main
  block_parameter: SampleTime
  type: character vector
  values: real scalar
  default: '''-1'''
- name: State name
  summary: Unique name for block state '' (default) | alphanumeric string
  group: State Attributes
  block_parameter: StateName
  type: character vector
  values: unique name
  default: ''''''
- name: State name must resolve to Simulink signal object
  summary: Option to require that state names resolve to signal object off (default) | on
  group: State Attributes
  block_parameter: StateMustResolveToSignalObject
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Delay length** — Delay length `Dialog` (default) | `Input port`

Specify whether to enter the delay length directly on the dialog box (fixed delay)
or to inherit the delay from an input port (variable delay).

- If you set **Source** to `Dialog`,
  enter the delay length in the edit field under **Value**.
- If you set **Source** to `Input
  port`, verify that an upstream signal supplies a delay length for
  the `d` input port. You can also specify its maximum value by
  specifying the parameter **Upper limit**.

Specify the scalar delay length as a real, non-negative integer. An out-of-range
or non-integer value in the dialog box (fixed delay) returns an error. An out-of-range
value from an input port (variable delay) casts it into the range. A noninteger value
from an input port (variable delay) truncates it to the integer.

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

Specify whether to enter the initial condition directly on the dialog box or to
inherit the initial condition from an input port.

- If you set **Source** to `Dialog`,
  enter the initial condition in the edit field under
  **Value**.
- If you set **Source** to `Input
  port`, verify that an upstream signal supplies an initial condition
  for the `x0` input port.

Simulink converts offline the data type of **Initial condition**
to the data type of the input signal `u` using a round-to-nearest
operation and saturation.

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
  each element of the input as a separate channel (sample-based processing).

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

Select to use a circular buffer for storing the state in simulation and code
generation. Otherwise, an array buffer stores the state.

Using a circular buffer can improve execution speed when the delay length is
large. For an array buffer, the number of copy operations increases as the delay
length goes up. For a circular buffer, the number of copy operations is constant for
increasing delay length.

If one of the following conditions is true, an array buffer always stores the
state because a circular buffer does not improve execution speed.

- For sample-based signals, the delay length is 1.
- For frame-based signals, the delay length is no larger than the frame
  size.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `UseCircularBuffer` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Prevent direct feedthrough** — Prevent direct feedthrough `off` (default) | `on`

Select to increase the delay length from zero to the lower limit for the
**Input processing** mode.

- For sample-based signals, increase the minimum delay length to 1.
- For frame-based signals, increase the minimum delay length to the frame
  length.

Selecting this check box prevents direct feedthrough from the input port,
`u`, to the output port. However, this check box cannot prevent
direct feedthrough from the initial condition port, `x0`, to the
output port.

#### Dependency

To enable this parameter, set **Delay length: Source** to
`Input port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PreventDirectFeedthrough` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Remove delay length check in generated code** — Remove delay length out-of-range check `off` (default) | `on`

Select to remove code that checks for out-of-range delay length.

| Check Box | Result | When to Use |
| --- | --- | --- |
| Selected | Generated code does not include conditional statements to check for out-of-range delay length. | For code efficiency |
| Cleared | Generated code includes conditional statements to check for out-of-range delay length. | For safety-critical applications |

#### Dependency

To enable this parameter, set **Delay length: Source** to
`Input port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RemoveDelayLengthCheckInGeneratedCode` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Diagnostic for delay length** — Diagnostic checks for delay length `None` (default) | `Warning` | `Error`

Specify whether to produce a warning or error when the input `d`
is less than the lower limit or greater than the **Delay length: Upper
limit**. The lower limit depends on the setting for **Prevent
direct feedthrough**.

- If the check box is cleared, the lower limit is zero.
- If the check box is selected, the lower limit is 1 for sample-based signals
  and frame length for frame-based signals.

Options for the diagnostic include:

- `None` — Simulink software takes no action.
- `Warning` — Simulink software displays a warning and continues the simulation.
- `Error` — Simulink software terminates the simulation and displays an error.

#### Dependency

To enable this parameter, set **Delay length: Source** to
`Input port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DiagnosticForDelayLength` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'None'` |

### **Show enable port** — Create enable port `on` (default) | `off`

Select to control execution of this block with an enable port. The block is
considered enabled when the input to this port is nonzero, and is disabled when the
input is `0`. The value of the input is checked at the same time step
as the block execution.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowEnablePort` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'on'` |

### **External reset** — External state reset `None` (default) | `Rising` | `Falling` | `Either` | `Level` | `Level hold`

Specify the trigger event to use to reset the states to the initial
conditions.

| Reset Mode | Behavior |
| --- | --- |
| `None` | No reset |
| `Rising` | Reset on a rising edge |
| `Falling` | Reset on a falling edge |
| `Either` | Reset on either a rising or falling edge |
| `Level` | Reset in either of these cases:  - When the reset signal is nonzero at the current time step - When the reset signal value changes from nonzero at the previous   time step to zero at the current time step |
| `Level hold` | Reset when the reset signal is nonzero at the current time step |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ExternalReset` |
| **Type**: character vector |
| **Values**: `'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **Default**: `'None'` |

### **Sample time (-1 for inherited)** — Discrete interval between sample time hits `-1` (default) | `scalar`

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. This block supports discrete sample time, but not
continuous sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Value**: real scalar |
| **Default**: `'-1'` |

### State Attributes

### **State name** — Unique name for block state `''` (default) | alphanumeric string

Use this parameter to assign a unique name to the block state. The default is
`' '`. When this field is blank, no name is assigned. When using
this parameter, remember these considerations:

- A valid identifier starts with an alphabetic or underscore character, followed
  by alphanumeric or underscore characters.
- The state name applies only to the selected block.

This parameter enables **State name must resolve to Simulink signal
object** when you click **Apply**.

For more information, see C Data Code Interface Configuration for Model Interface Elements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateName` |
| **Type:** character vector |
| **Values:** unique name |
| **Default:** `''` |

### **State name must resolve to Simulink signal object** — Option to require that state names resolve to signal object `off` (default) | `on`

Specify whether state names are required to resolve to signal objects. If
selected, the software generates an error at run time if you specify a state name that
does not match the name of a signal object.

Selecting this parameter disables the **Code generation storage
class** parameter.

#### Dependencies

Enabled when you specify a value for the **State name**
parameter and set the **Signal resolution** model configuration
parameter to a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StateMustResolveToSignalObject` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |
## Libraries

HDL Coder / Discrete Simulink / Discrete

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides configuration options that affect HDL implementation and synthesized
logic.

| Block Parameter Setting | Description |
| --- | --- |
| Set **External reset** to `Level`. | Generates a reset port in the HDL code. |
| Select **Show enable port**. | Generates an enable port in the HDL code. |
| For **Initial condition**, set **Source** to `Dialog` and enter the value. | Specifies an initial condition for the block. |
| Set **Input processing** to `Columns as channels (frame based)` or `Elements as channels (sample based)`. | Expects vector input data, where each element of the vector represents a sample in time. |

**Additional Settings When Using State Control Block**

If you use a State Control block with the Delay block
inside a subsystem in your Simulink model, use these additional settings.

| Block Parameter Setting | Description |
| --- | --- |
| Set **External reset** to `Level hold` for `Synchronous` mode and `Level` for `Classic` mode of the State Control block. | Generates a reset port in the HDL code. |
| Set **Delay length** to zero for a Delay block with an external enable port. | Treated as a wire in only `Synchronous` mode of the State Control block. |
| Set **Delay length** to zero for a Delay block with an external reset port. | Treated as a wire in `Synchronous` and `Classic` modes of the State Control block. |

For more information about the State Control block, see State Control.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | Allow delay to be distributed or absorbed during the distributed pipelining and delay absorption optimizations. The default is `inherit`. For more details, see AllowDelayDistribution. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType. |
| **UseRAM** | Map delays to RAM instead of registers. The default is `off`. See also UseRAM. |

**Variable Integer Delay Support**

- You can generate HDL code for the Delay block that has **Delay
  Length** set through the `Input port`. Input
  delay length can be integer types or floating-point types.
- The code generation supports positive integer values at the 'd' port of the delay
  block. The delay length set through the input port must be between
  `0` and `Upper limit`, specified in the Block
  Parameters dialog box.
- For negative delay length values, HDL Coder translates these negative delay length to `0`.
- Similarly, if you specify delay length greater than the upper limit, HDL Coder translates the delay length to the `Upper limit` value.
- Upper limit range is defined by the range of the delay length input data type. For
  example, if you specify delay length input data type as `uint8`, then
  the upper limit must not exceed `255`.
- You can use enable and reset ports for the variable integer Delay block.

**Complex Data Support**

This block supports code generation for complex signals.

**Restrictions**

- For **Initial condition**, **Source** set to
  `Input port` is not supported for HDL code
  generation.
- HDL code generation supports only the Boolean data type at the Reset and Enable
  ports.
- HDL Block Property **UseRAM** for RAM mapping is not supported
  for Delay block that has **Delay Length** set through the
  `Input port`.
- The Delay block that has **Delay Length** set through the
  `Input port` does not support bus and matrix data input
  for HDL code generation.

## Version History

**Introduced in R2024b**

## Description

Delay input signal by fixed or variable sample periods when external enable signal is true

The Enabled Delay block outputs a delayed version of the input signal based
on the state of the enable signal. At the start of the simulation or upon an enable signal
transition to true, the block outputs the initial condition value x0. If the enable signal s
true during consecutive time steps, the block continues to output the input signal delayed by
specified delay length. If the enable signal is false at the start of the simulation, the
block outputs zero. If the enable signal becomes false after begin true, the block maintains
the last output value until the enable signal becomes true again. The block supports:

- Variable delay length
- State storage
- Using a circular buffer instead of an array buffer for state storage
- Resetting the state to the initial condition with an external reset signal
- Controlling execution of the block at every time step with an external enable
  signal
