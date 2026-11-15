---
type: simulink-block
title: 'Memory'
family: discrete
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'memory'
language: en
---

# Memory

Output input from previous time step

## Libraries

Simulink / Discrete HDL Coder / Discrete

## Description

The Memory block holds and delays its input by one major integration
time step. When placed in an iterator subsystem, it holds and delays its input by one
iteration. This block accepts continuous and discrete signals. The block accepts one
input and generates one output. Each signal can be a scalar, vector, matrix, or N-D
array. If the input is non-scalar, the block holds and delays all elements of the input
by the same time
step.

You specify the block output for the first time step using the **Initial
condition** parameter. Careful selection of this parameter can minimize
unwanted output behavior. However, you cannot specify the sample time. This block’s
sample time depends on the type of solver used, or you can specify to inherit it. The
**Inherit sample time** parameter determines whether sample time is
inherited or based on the solver.

**Tip**

Avoid using the Memory block when both these conditions are true:

- Your model uses the variable-step solver `ode15s` or
  `ode113`.
- The input to the block changes during simulation.

When the Memory block inherits a discrete sample time, the block is analogous to the
Unit Delay block. However, the Memory
block does not support state logging. If logging the final state is necessary, use a
Unit Delay block instead.

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

### Bus Support

The Memory block is a bus-capable block. The input can be a virtual
or nonvirtual bus signal subject to the following restrictions:

- **Initial condition** must be zero, a nonzero scalar, or
  a finite numeric structure.
- If **Initial condition** is zero or a structure, and you
  specify a **State name**, the input cannot be a virtual
  bus.
- If **Initial condition** is a nonzero scalar, you cannot
  specify a **State name**.

For information about specifying an initial condition structure, see Specify Initial Conditions for Bus Elements.

All signals in a nonvirtual bus input to a Memory block must have
the same sample time, even if the elements of the associated bus object specify
inherited sample times. You can use a Rate Transition block to change the
sample time of an individual signal, or of all signals in a bus. See Modify Sample Times for Nonvirtual Buses and
Bus-Capable
Blocks for more information.

You can use an array of buses as an input signal to a Memory block.
You can specify the **Initial condition** parameter with:

- The value `0`. In this case, all the individual
  signals in the array of buses use the initial value
  `0`.
- An array of structures that specifies an initial condition for each of
  the individual signals in the array of buses.
- A scalar structure that specifies an initial condition for each of the
  elements that the bus type defines. Use this technique to specify the
  same initial conditions for each of the buses in the array.

For details about defining and using an array of buses, see Group Nonvirtual Buses in Arrays of Buses.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D array. The input can be
continuous or discrete, containing real, or complex values of any data
type Simulink® supports.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Input delayed by one major integration time step scalar | vector | matrix | N-D array

Output is the input from the previous time step.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### Main

### **Initial condition** — Initial condition 0 (default) | scalar | vector | matrix | N-D array

Specify the output at the initial integration step. This value must be 0 when you do not
use a built-in input data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'0'` |

### **Inherit sample time** — Inherit sample time `off` (default) | `on`

Select to inherit the sample time from the driving block:

- If the driving block has a discrete sample time, the block
  inherits the sample time.
- If the driving block has a continuous sample time,
  selecting this check box has no effect. The sample time
  depends on the type of solver used for simulating the
  model.

When this check box is cleared, the block sample time
depends on the type of solver used for simulating the model:

- If the solver is a variable-step solver, the block sample time
  is continuous but fixed in minor time step: `[0,
  1]`.
- If the solver is a fixed-step solver, the `[0,
  1]` sample time converts to the solver step size
  after sample-time propagation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InheritSampleTime` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Direct feedthrough of input during linearization** — Output the input during linearization and trim `off` (default) | `on`

Select to output the input during linearization and trim. This
selection sets the block mode to direct feedthrough.

Selecting this check box can cause a change in the ordering of states
in the model when using the functions `linmod`, `dlinmod`, or `trim`. To extract this
new state ordering, use the following commands.

First compile the model using the following command, where
`model` is the name of the Simulink model.

```
    [sizes, x0, x_str] = model([],[],[],'lincompile');
```

Next, terminate the compilation with this command.

```
  model([],[],[],'term');
```

The output argument, `x_str`, which is a cell array
of the states in the Simulink model, contains the new state ordering. When passing a
vector of states as input to the `linmod`,
`dlinmod`, or `trim` functions,
the state vector must use this new state ordering.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LinearizeMemory` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Treat as a unit delay when linearizing with discrete sample time** — Linearize to unit delay for discrete inputs `off` (default) | `on`

Select to linearize the Memory block to a unit delay
when the Memory block is driven by a signal with a
discrete sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LinearizeAsDelay` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Direct feedthrough characteristics for this block depend on block parameter values. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

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
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
