---
type: simulink-block
title: 'Unit Delay'
family: discrete
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'unitdelay'
language: en
---

# Unit Delay

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal that the block delays by one sample period.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal that is the input delayed by one sample period.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### Main

### **Initial condition** — First sample period output `0` (default) | scalar | vector

Specify the output of the simulation for the first sampling period,
during which the output of the Unit Delay block is
otherwise undefined.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialCondition` |
| **Type**: character vector |
| **Value**: scalar | vector |
| **Default**: `'0'` |

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

### **Sample time (-1 for inherited)** — Discrete interval between sample time hits `-1` (default) | 1-by-2 vector

Enter the discrete interval between sample time hits or specify
`-1` to inherit the sample time.

See also Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Value**: real scalar | 1-by-2 vector |
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

### **State name must resolve to Simulink signal object** — Option to require that state names resolve to signal object `off` (default) | `on`

Specify whether state names are required to resolve to signal objects. If selected,
the software generates an error at run time if you specify a state name that does not
match the name of a signal object.

Selecting this parameter disables the **Code generation storage
class** parameter.

#### Dependencies

Enabled when you specify a value for the **State name** parameter
and set the **Signal resolution** model configuration parameter to
a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StateMustResolveToSignalObject` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

## Libraries

Simulink / Discrete HDL Coder / Discrete

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

Generated code relies on `memcpy` or `memset`
functions (`strong.h`) under certain conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | Allow delay to be distributed or absorbed during the distributed pipelining and delay absorption optimizations. The default is `inherit`. For more details, see AllowDelayDistribution (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Delay signal one sample period

The Unit Delay block holds and delays its input by one sample period. When
placed in an iterator subsystem, it holds and delays its input by one iteration. This
block is equivalent to the z-1 discrete-time operator. The
block accepts one input and generates one output. Each signal can be scalar or vector.
If the input is a vector, the block holds and delays all elements of the vector by the
same sample period.

You specify the block output for the first sampling period with the **Initial
conditions** parameter. Careful selection of this parameter can minimize
unwanted output behavior. You specify the time between samples with the **Sample
time** parameter. A setting of `-1` means the block
inherits the **Sample time**.

**Note**

The Unit Delay block errors out if you use it to create a
transition between blocks operating at different sample rates. Use the Rate Transition block
instead.

### Comparison with Similar Blocks

The Memory, Unit Delay, and Zero-Order Hold
blocks provide similar functionality but have different capabilities. Also, the purpose of
each block is different.

This table shows recommended usage for each block.

| Block | Purpose of the Block | Reference Examples |
| --- | --- | --- |
| Unit Delay | Implement a delay using a discrete sample time that you specify. The block accepts and outputs signals with a discrete sample time. | - Engine Timing Model with Closed Loop Control (Compression subsystem) |
| Memory | Implement a delay by one major integration time step. Ideally, the block accepts continuous (or fixed in minor time step) signals and outputs a signal that is fixed in minor time step. | - Building a Clutch Lock-Up Model (Friction Mode Logic/Lockup FSM subsystem) - Capture the Velocity of a Bouncing Ball with the Memory Block |
| Zero-Order Hold | Convert an input signal with a continuous sample time to an output signal with a discrete sample time. | - Developing the Apollo Lunar Module Digital Autopilot - Radar Tracking Using MATLAB Function Blocks |

Each block has the following capabilities.

| Capability | Memory | Unit Delay | Zero-Order Hold |
| --- | --- | --- | --- |
| Specification of initial condition | Yes | Yes | No, because the block output at time t = 0 must match the input value. |
| Specification of sample time | No, because the block can only inherit sample time from the driving block or the solver used for the entire model. | Yes | Yes |
| Support for frame-based signals | No | Yes | Yes |
| Support for state logging | No | Yes | No |

### String Support

The Unit Delay block can accept and output string data type only if
the block is configured for the default value of the **Initial
condition** parameter (0).
