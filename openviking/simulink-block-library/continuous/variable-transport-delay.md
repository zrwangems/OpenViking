---
type: simulink-block
title: 'Variable Transport Delay'
family: continuous
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'variabletransportdelay'
---

# Variable Transport Delay

Delay input by variable amount of time

## Libraries

Simulink / Continuous

## Description

The Variable Transport Delay and Variable Time
Delay blocks appear as two blocks in the Simulink® block library. However, they are the same Simulink block with different settings for the **Select delay
type** parameter. Use this parameter to specify the mode in which the block
operates.

### Variable Transport Delay

In this mode, the block output at the current time step is equal to the value of its data
(top, or left) input at an earlier time step equal to the current time minus a
transport delay.

y(t)=u(t−td(t))

Simulink software finds the transport delay, td(t), by solving the following equation:

∫t−td(t)t1ti(τ)dτ=1

This equation involves an instantaneous time delay, ti(t), given by the time delay (bottom, or right) input.

Suppose that you want to use this block to model the fluid flow through a pipe where the fluid
speed varies with time. In this case, the time delay input to the block is

ti(t)=Lvi(t)

where `L` is the length of the pipe and vi(t) is the speed of the fluid.

### Variable Time Delay

In this mode, the block has a data input, a time delay input, and a data output. (See Identify Port Location on Rotated or Flipped Block for a description of the port order for various block orientations.) The output at the current time step equals the value of its data input at a previous time step. This time step is the current simulation time minus a delay time specified by the time delay input.

y(t)=u(t−t0)=u(t−τ(t))

During the simulation, the block stores time and input value pairs in an internal buffer. At the start of simulation, the block outputs the value of the **Initial output** parameter until the simulation time exceeds the time delay input. Then, at each simulation step, the block outputs the signal at the time that corresponds to the current simulation time minus the delay time.

If you want the output at a time between input storing times and the solver is a continuous
solver, the block interpolates linearly between points. If the time delay is smaller than
the step size, the block extrapolates an output point from a previous point. For example,
consider a fixed-step simulation with a step size of `1` and the current
time at `t = 5`. If the delay is `0.5`, the block must
generate a point at `t = 4.5`, but the most recent stored time value is at
`t = 4`. Thus, the block extrapolates the input at
`4.5` from the input at `4` and uses the extrapolated
value as its output at `t = 5`.

Extrapolating forward from the previous time step can produce a less accurate result than extrapolating back from the current time step. However, the block cannot use the current input to calculate its output value because the input port does not have direct feedthrough.

If the model specifies a discrete solver, the block does not interpolate between time steps. Instead, it returns the nearest stored value that precedes the required value.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal specified as a scalar, vector, or matrix.

This port has direct feedthrough when you select the **Handle zero
delay** parameter. This port has direct feedthrough during
trimming and linearization operations when you select the **Direct
feedthrough of input during linearization** parameter.

**Data Types:** `double`

### **t0** — Time delay input scalar | vector | matrix

Time delay input specified as a scalar, vector, or matrix. When the block is in `Variable time delay` mode, this value specifies the time delay. For more information about that calculation, see Variable Time Delay.

This port has direct feedthrough.

#### Dependencies

To enable this port, set **Select delay type** to `Variable time delay`.

**Data Types:** `double`

### **ti** — Instantaneous time delay input scalar | vector | matrix

Instantaneous time delay input specified as a scalar, vector, or matrix. When the block is in
`Variable transport delay` mode, this value is
used to calculate the transport delay. For more information about that
calculation, see Variable Transport Delay.

This port has direct feedthrough.

#### Dependencies

To enable this port, set **Select delay type** to `Variable transport delay`.

**Data Types:** `double`
### Output

### **Port\_1** — Delayed signal scalar | vector | matrix

Output signal specified as a scalar, vector, or matrix.

**Data Types:** `double`

## Parameters

### **Select delay type** — Type of delay `Variable time delay` | `Variable transport delay`

Specify the type of delay as `Variable time delay` or `Variable transport delay`.

The default value of this parameter depends on the block implementation:
`Variable time delay` for the Variable Time
Delay block, and `Variable transport delay` for
the Variable Transport Delay block.

#### Dependencies

- Setting this parameter to `Variable time
  delay` enables the **Handle zero
  delay** parameter.
- Setting this parameter to `Variable transport
  delay` enables the **Absolute
  tolerance** and **State Name**
  parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariableDelayType` |
| **Type:** character vector, string |
| **Values:** `'Variable transport delay'` | `'Variable time delay'` |

### **Maximum delay** — Maximum value of time delay input `10` (default) | scalar | vector

Set the maximum value of the time delay input. This value defines the largest time delay input that this block allows. The block clips any delay that exceeds this value. This value cannot be negative. If the time delay becomes negative, the block clips it to zero and issues a warning message.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaximumDelay` |
| **Type:** character vector, string |
| **Value:** scalar | vector |
| **Default:** `'10'` |

### **Initial output** — Initial output `0` (default) | scalar | vector

Specify the output that the block generates until the simulation time first exceeds the time delay input.

#### Dependencies

- The initial output of this block cannot be `inf` or `NaN`.
- A `Run-to-run tunable parameter` cannot be changed during simulation run time. However, changing it before a simulation begins does not cause Accelerator or Rapid Accelerator to regenerate code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** character vector, string |
| **Values:** scalar | vector |
| **Default:** `'0'` |

### **Initial buffer size** — Initial memory allocation `1024` (default) | scalar

Define the initial memory allocation for the number of input points to store. The input points define the history of the input signal up to the current simulation time.

- If the number of input points exceeds the initial buffer size, the block allocates additional memory.
- After simulation ends, a message displays if the buffer is not sufficient
  and more memory must be allocated.

#### Tips

- Because allocating memory slows down simulation, choose this value carefully if simulation speed is an issue.
- For long time delays, this block might use a large amount of memory, particularly for dimensionalized input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaximumPoints` |
| **Type:** character vector, string |
| **Values:** scalar | vector |
| **Default:** `'1024'` |

### **Use fixed buffer size** — Use fixed-size buffer `off` (default) | `on`

Selecting this check box uses a fixed-size buffer to save input data from previous time steps. When you clear this check box, the block does not use a fixed-size buffer.

The **Initial buffer size** parameter specifies the buffer size. If the buffer is full, new data replaces data already in the buffer. Simulink software uses linear extrapolation to estimate output values that are not in the buffer.

**Note**

ERT or GRT code generation uses a fixed-size buffer even if you do not select this check box.

#### Tips

- If the input data is linear, selecting this check box can save memory.
- If the input data is nonlinear, do not select this check box. Doing so might yield inaccurate results.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FixedBuffer` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Handle zero delay** — Option to allow zero delay `off` (default) | `on`

Specify whether the block allows a delay value of `0`.

- `off` — The block does not allow zero delay. The
  input signal port does not have direct feedthrough.
- `on` — The block allows zero delay. The input signal
  port has direct feedthrough.

#### Dependencies

To enable this parameter, set the **Select delay type**
parameter to `Variable time delay`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ZeroDelay` |
| **Type:** string | character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Direct feedthrough of input during linearization** — Option to use zero delay during linearization and trimming operations `off` (default) | `on`

Specify whether to use a delay value of zero for the block during trimming or
linearization operations.

#### Tips

Selecting this parameter can cause a change in the order of states in the
model when you use the functions `linmod`, `dlinmod`, or `trim`. To extract this new
state ordering:

1. Compile the model using this command, where
   `model` is the name of the model.

   ```
       [sizes,x0,x_str] = model([],[],[],'lincompile');
   ```
2. Terminate the compilation with the following command.

   ```
     model([],[],[],'term');
   ```

   The output argument `x_str`, which is a cell
   array of the states in the Simulink model, contains the new state ordering. When you pass
   a vector of states as input to the `linmod`,
   `dlinmod`, or `trim`
   functions, the state vector must use this new state ordering.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TransDelayFeedthrough` |
| **Type:** string | character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Pade order (for linearization)** — Order of Pade approximation `0` (default) | scalar

Set the order of the Pade approximation for linearization routines.

- The default value is `0`, which results in a unity gain with no dynamic states.
- Setting the order to a positive integer `n` adds `n` states to your model, but results in a more accurate linear model of the transport delay.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PadeOrder` |
| **Type:** character vector, string |
| **Values:** scalar |
| **Default:** `'0'` |

### **Absolute tolerance** — Absolute tolerance for computing block state `auto` (default) | positive, real, scalar or vector

Specify the absolute tolerance for computing the block state.

#### Dependencies

To enable this parameter, set **Select delay type** to `Variable transport delay`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AbsoluteTolerance` |
| **Type:** character vector, string |
| **Values:** `'auto'` | `'-1'` | any positive real scalar or vector |
| **Default:** `'auto'` |

### **State Name (e.g., 'position')** — Unique name for each state `' '` (default) | character vector, string

Assign a unique name to each state. If this field is blank, no name assignment occurs.

#### Tips

- To assign a name to a single state, enter the name between quotes, for example, `'velocity'`.
- To assign names to multiple states, enter a comma-delimited list surrounded by braces, for example, `{'a', 'b', 'c'}`. Each name must be unique.
- The state names apply only to the selected block.
- The number of states must divide evenly among the number of state names.
- You can specify fewer names than states, but you cannot specify more names than states.

  For example, you can specify two names in a system with four states. The first name applies to the first two states and the second name to the last two states.
- To assign state names with a variable in the MATLAB® workspace, enter the variable without quotes. A variable
  can be a character vector, string, cell array, or structure.

#### Dependencies

To enable this parameter, set **Select delay type** to `Variable transport delay`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ContinuousStateAttributes` |
| **Type:** character vector, string |
| **Values:** `' '` | user-defined character vector, user-defined string |
| **Default:** `' '` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `noa, b` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Ports of this block have different direct feedthrough characteristics.  b Direct feedthrough characteristics for this block depend on block parameter values. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production-quality code. Relates to resource limits and restrictions on speed and memory often found in embedded systems. The code generated can contain dynamic allocation and freeing of memory, recursion, additional memory overhead, and widely-varying execution times. While the code is functionally valid and generally acceptable in resource-rich environments, smaller embedded targets often cannot support such code.

In general, consider using the Simulink Model Discretizer to map continuous blocks into
discrete equivalents that support production code generation. To start the Model
Discretizer, in the Simulink Editor, on the **Apps** tab, under
**Apps**, under **Control Systems**, click
**Model Discretizer**. One exception is the Second-Order
Integrator block because, for this block, the Model Discretizer produces an
approximate discretization.

## Version History

**Introduced in R2007a**
