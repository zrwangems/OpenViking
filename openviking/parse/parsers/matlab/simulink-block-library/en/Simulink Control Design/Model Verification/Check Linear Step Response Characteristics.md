---
type: simulink-block
title: 'Linear Step Response Plot'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Linear Analysis Plots'
documentation_page: 'linearstepresponseplot'
documentation_source_path: 'ug/linearstepresponseplot.html'
language: en
---

# Linear Step Response Plot

## Ports

### Input

### **Trigger** — External trigger signal scalar

Use this input port (indicated by External trigger icon) to connect an external trigger signal for computing
the model linearization. To specify the type of trigger signal to detect, use the
**Trigger type** parameter.

#### Dependencies

To enable this port, set the **Linearize on** parameter to `External trigger`.
### Output

### **z–1** — Assertion signal `1` | `0`

Output the value of the assertion signal as a logical value. If any bound specified on the **Bounds** tab is violated, the assertion signal is false (`0`). Otherwise, this signal is true (`1`).

By default, the data type of the output signal is double. To set the output data type as Boolean, in the Simulink model, in the Configuration Parameters dialog box, select the **Implement logic signals as Boolean data** parameter. This setting applies to all blocks in the model that generate logic signals.

You can use the assertion signal to design complex assertion logic. For an example, see Verify Model Using Simulink Control Design and Simulink Verification Blocks.

#### Dependencies

To enable this port, select the **Output assertion signal** parameter.

## Parameters

### **Show Plot** — Open plot button

To view gain and phase margins computed during a simulation, click this button
before starting the simulation. If you specify bounds on the **Bounds**
tab, they are also shown on the plot.

To show the plot when opening the block, select the **Show plot on block
open** parameter.

For more information on using the plot, see Using the Plot.

### **Show plot on block open** — Open plot when opening block `off` (default) | `on`

Select this parameter to open the plot when opening the block. You can then perform
tasks, such as adding or modifying bounds, in the plot window instead of using the block
parameters. To access the block parameters from the plot window, select
**Edit** or click Parameter icon.

For more information on using the plot, see Using the Plot.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LaunchViewOnOpen` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Response Optimization** — Open Response Optimizer button

Open the Response Optimizer app to optimize the model response to meet the design requirements specified on the **Bounds** tab.

This button is available only if you have Simulink
Design Optimization™ software installed.

For more information on response optimization, see Design Optimization to Meet Step Response Requirements (GUI) (Simulink Design Optimization) and Design Optimization to Meet Time-Domain and Frequency-Domain Requirements (GUI) (Simulink Design Optimization).

### Linearizations

To specify the portion of the model to linearize and other linearization settings, use
the parameters on the **Linearizations** tab. The default settings on this
tab are the same for the Linear Step Response Plot and Check Linear
Step Response Characteristics blocks.

### **Linearization inputs/outputs** — Specify portion of model to linearize linear analysis points

To specify the portion of the model to linearize, select signals from the Simulink model and add them as linearization inputs or outputs.

Linearization input and output table

In the table, the **Block:Port:Bus Element** column shows the
following information for each signal.

- Source block
- Output port of the source block to which the signal is connected
- Bus element name (if the signal is in a bus)

In the **Configuration** column, select the type of linear analysis
point from the following types. For more information on linear analysis points, see
Specify Portion of Model to Linearize.

- `Open-loop Input` — Specifies a linearization input
  point after a loop opening
- `Open-loop Output` — Specifies a linearization output
  point before a loop opening
- `Loop Transfer` — Specifies an output point before a
  loop opening followed by an input
- `Input Perturbation` — Specifies an additive input to
  a signal
- `Output Measurement` — Takes a measurement at a
  signal
- `Loop Break` — Specifies a loop opening
- `Sensitivity` — Specifies an additive input followed
  by an output measurement
- `Complementary Sensitivity` — Specifies an output
  followed by an additive input

**Note**

If you simulate the model without specifying a linearization input or output, the
software generates a warning in the MATLAB Command Window and does not compute a linear system.

#### Edit Linearization Inputs and Outputs

To add linearization inputs and outputs:

1. To expand the signal selection area, click Plus.

   The dialog box expands to display a **Click a signal in the model
   to select it** area.
2. In the Simulink model, select one or more signals.

   The selected signals appear in the **Model signal**
   table.

   Signal table with signal added
3. (Optional) For bus signals, expand the bus to select individual
   elements.

   **Tip**

   For large buses or other large lists of signals, you can filter the
   signal names. In the **Filter by name** box, enter
   search text. The name match is case-sensitive.

   To modify the filtering options, click Down arrow. For more information on filtering
   options, see the **Enable regular expression** and
   **Show filtered results as a flat list**
   parameters.
4. To add the selected signal to the **Linearization
   inputs/outputs** table, click Left arrow.
5. In the **Configuration** column, specify the signal
   type.

Alternatively, if you have linearization inputs and outputs defined in your model,
you can add them to the **Linearization inputs/outputs** table by
clicking Import icon.

To remove a signal from the **Linearization inputs/outputs**
table, select the signal and click Delete icon.

To highlight the source block of a signal in the Simulink model, select the signal in the **Linearization
inputs/outputs** table and click Highlight icon.

### **Enable regular expression** — Enable signal searching using regular expressions `on` (default) | `off`

Select this option to enable the use of MATLAB regular expressions for filtering signal names. For example, entering
`t$` in the **Filter by name** text box displays
all signals whose names end with a lowercase `t` (and their immediate
parents). For more information, see Regular Expressions.

#### Dependencies

To enable this parameter, click Down arrow next to the **Filter by name** text
box.

### **Show filtered results as a flat list** — Display filtered bus signal hierarchy using flat list `off` (default) | `on`

Select this option to display the list of filtered signals in a flat list format. The flat list format uses dot notation to reflect the hierarchy of bus signals. The signals are filtered based on the text in the **Filter by name** text box.

The following figure shows an example of the flat list format for a filtered set of nested bus signals.

#### Dependencies

To enable this parameter, click Down arrow next to the **Filter by name** text
box.

### **Linearize on** — When to compute linear model `Simulation snapshots` (default) | `External trigger`

Use this parameter to specify when you want to compute a linear model.

To compute linear models at specified simulation snapshot times, set this parameter to
`Simulation snapshots`. Specify snapshot times using the
**Snapshot times** parameter.

Use simulation snapshots when you:

- Know one or more times when the model is at a steady-state operating
  point
- Want to compute linear systems at specific times

To compute linear models at trigger-based simulation events, set this parameter to
`External trigger`. Selecting this option adds a trigger
input port to the block, to which you connect your external trigger signal. To specify
the type of trigger to detect, use the **Trigger type**
parameter.

Use an external trigger when a signal generated during simulation indicates that the
model is at a steady-state condition of interest. For example, for an aircraft model,
you might want to compute the linear system whenever the fuel mass is a given fraction
of the maximum fuel mass.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LinearizeAt` |
| **Type:** character vector |
| **Value:** `'SnapshotTimes'` | `'ExternalTrigger'` |
| **Default:** `'SnapshotTimes'` |

### **Snapshot times** — Simulation times at which to compute linear model `0` (default) | positive real value | vector of positive real values

To compute a linear system at specific simulation times, such as a time that you know
the model reaches a steady state operating point, specify one or more snapshot times. To
specify multiple snapshot times, specify this parameter as a vector of positive
values.

Snapshot times must be less than or equal to the simulation time specified in the
Simulink model.

For examples of linearizing a model at simulation snapshot times, see:

- Visualize Linear System at Multiple Simulation Snapshots
- Verify Model at Default Simulation Snapshot Time
- Verify Model at Multiple Simulation Snapshots

#### Dependencies

To enable this parameter, set the **Linearize on** parameter to
`Simulation snapshots`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SnapshotTimes` |
| **Type:** character vector |
| **Value:** `'0'` | positive real value | vector of positive real values |
| **Default:** `'0'` |

### **Trigger type** — Type of external trigger to detect `Rising edge` (default) | `Falling edge`

Specify the trigger to detect in the external trigger signal as one of the following types.

- `Rising edge` — Use the rising edge of the trigger
  signal; that is, when the signal changes from `0` to
  `1`.
- `Falling edge` — Use the falling edge of the trigger
  signal; that is, when the signal changes from `1` to
  `0`.

#### Dependencies

To enable this parameter, set the **Linearize on** parameter to `External trigger`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TriggerType` |
| **Type:** character vector |
| **Value:** `'rising'` | `'falling'` |
| **Default:** `'rising'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select this option to enable zero-crossing detection.

When you set the **Linearize on** parameter to `Simulation snapshots`, enabling zero-crossing detection ensures that the software computes the linear model at the exact snapshot times you specify in the **Snapshot times** parameter.

When you set the **Linearize on** parameter to `External trigger`, enabling zero-crossing detection ensures that the software computes the linear model at the exact time that the external trigger is detected. To specify the type of trigger, use the **Trigger type** parameter.

If you clear this option, the software computes the linear system at simulation times selected by the variable-step Simulink solver, which might not correspond to an exact snapshot time or the exact time when a trigger signal is detected.

For example, consider the case where the variable-step solver selects simulation times
*T**n*–1 and
*Tn*. As shown in the following figure,
the specified snapshot time *Tsnap* can be
between the selected simulation times. If you enable zero-crossing detection, the solver
also simulates the model at time *Tsnap* and
computes the linear model at this point.

Similarly, the external trigger can be detected at a time
*Ttrig* that is between the selected
simulation times. If you enable zero-crossing detection, the solver also simulates the
model at time *Ttrig* and computes the linear
model at this point.

In both cases, if you do not enable zero-crossing detection, the software computes the linear
model at either *T**n*–1 or
*Tn*.

For more information on zero-crossing detection, see Zero-Crossing Detection.

#### Dependencies

This parameter is ignored when you use a fixed-step Simulink solver.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ZeroCross` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Use exact delays** — Use exact delays in linear model `off` (default) | `on`

Select this option to compute a linear model with exact delays. If you clear this option, the linear model uses Padé approximations of any delays.

For more information on linearizing models with delays, see Linearize Models with Delays.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseExactDelayModel` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Linear system sample time** — Sample time of linear system `'auto'` (default) | positive finite value | `0`

To compute a linear system with the specified sample time, the software coverts sample
times in the model using the method you specify in the **Sample time rate
conversion method** parameter.

You can set the sample time to one of the following values.

- `auto` — If all blocks in the model are continuous-time, use
  a sample time of `0`. Otherwise, set the sample time to the
  least common multiple of the nonzero sample times in the model.
- Positive finite value — Create a discrete-time model with the specified sample
  time.
- `0` — Create a continuous-time model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Value:** `'auto'` | positive finite value | `'0'` |
| **Default:** `'auto'` |

### **Sample time rate conversion method** — Rate conversion method `Zero-Order Hold` (default) | `Tustin (bilinear)` | `Tustin with Prewarping` | ...

Method for converting sample times during linearization, specified as one of the following values.

- `Zero-Order Hold` — Zero-order hold, where the control inputs are assumed piecewise constant over the sample time `Ts`. This method usually performs better in the time domain.
- `Tustin (bilinear)` — Bilinear (Tustin) approximation without frequency prewarping. The software rounds off fractional time delays to the nearest multiple of the sampling time. This method usually performs better in the frequency domain.
- `Tustin with Prewarping` — Bilinear (Tustin) approximation with frequency prewarping. Specify the prewarp frequency using the **Prewarp frequency** parameter. This method usually performs better in the frequency domain. Use this method to ensure matching in a frequency region of interest.
- `Upsampling when possible, Zero-Order Hold otherwise` — Upsample a discrete-time system when possible; otherwise, use a zero-order hold.
- `Upsampling when possible, Tustin otherwise` — Upsample a discrete-time system when possible; otherwise, use a Tustin approximation.
- `Upsampling when possible, Tustin with Prewarping otherwise` — Upsample a discrete-time system when possible; otherwise, use a Tustin approximation with frequency prewarping.

You can upsample only when you convert a discrete-time system to a new faster sample time that is an integer multiple of the sample time of the original system.

For more information on rate conversion and linearization of multirate models, see:

- Multirate Linearization Algorithm
- Linearize Models Using Different Rate Conversion Methods
- Continuous-Discrete Conversion Methods

**Note**

If you use a rate conversion method other than `Zero-Order
Hold`, the converted states no longer have the same physical
meaning as the original states. As a result, the state names in the resulting LTI
system change to `'?'`.

#### Dependencies

To enable this parameter, set the **Linear system sample time** parameter to a value other than `auto`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RateConversionMethod` |
| **Type:** character vector |
| **Value:** `'zoh'` | `'tustin'` | `'prewarp'`| `'upsampling_zoh'`| `'upsampling_tustin'`| `'upsampling_prewarp'` |
| **Default:** `'zoh'` |

### **Prewarp frequency** — Prewarp frequency for Tustin rate conversion `'10'` (default) | positive scalar

Prewarp frequency for Tustin rate conversion in radians per second, specified as a scalar value less than the Nyquist frequency before and after resampling.

#### Dependencies

To enable this parameter, set the **Sample time rate conversion method** parameter to one of the following values.

- `Tustin with Prewarping`
- `Upsampling when possible, Tustin with Prewarping otherwise`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PreWarpFreq` |
| **Type:** character vector |
| **Value:** positive scalar |
| **Default:** `'10'` |

### **Use full block names** — Use full block path in state, input, and output names `off` (default) | `on`

To show the state, input, and output names of the computed linear system using their full
block path, select this parameter. For example, in the `scdcstr` model
used in the Plot Linear System Characteristics of a Chemical Reactor example, a
state in the `Integrator1` block of the `CSTR`
subsystem appears with full path as `scdcstr/CSTR/Integrator1`.

If you clear this parameter, only the names of the states, inputs, and outputs are used, which
is useful when the signal names are unique and you know their locations in your
Simulink model. In the preceding example, the state name of the integrator block
appears as `Integrator1`.

The computed linear system is a state-space object (`ss`). The state, input, and output names for the system appear in the
following state-space object properties.

| Input, Output, or State Name | State-Space Object Property |
| --- | --- |
| Linearization input names | `InputName` |
| Linearization output names | `OutputName` |
| State names | `StateName` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseFullBlockNameLabels` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Use bus signal names** — Use bus signal names in linear system `off` (default) | `on`

When you select an entire bus as a linearization input or output, select this parameter to use the signal names of the individual bus elements in the computed linear system. If you do not enable this option, the bus channel numbers are used instead.

**Note**

Selecting an entire bus signal is not recommended. Instead, select individual bus elements.

Bus signal names appear when the linearization input or output is from one of the following blocks.

- Root-level inport block containing a bus object
- Bus creator block
- Subsystem block whose source traces back to the output of a bus creator block
- Subsystem block whose source traces back to a root-level inport by passing through only virtual or nonvirtual subsystem boundaries

#### Dependencies

Using this parameter is not supported when your model contains mux/bus mixtures.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseBusSignalLabels` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### Bounds

To define bounds on step response characteristics and specify whether to check for
violations of these bounds, use the parameters on the **Bounds** tab. The
default settings on this tab are different for the Linear Step Response Plot
and Check Linear Step Response Characteristics blocks.

### **Include step response bound in assertion** — Check whether step response violates bounds on characteristics `on` | `off`

Select this parameter to check whether the step response characteristics violate
the bounds specified on the **Bounds** tab.

By default, this parameter is cleared for the Linear Step Response
Plot block and selected for the Check Linear Step Response
Characteristics block.

#### Dependencies

This parameter is used for assertion only if you select the **Enable
assertion** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnableStepResponseBound` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` for Linear Step Response Plot block, `'on'` for Check Linear Step Response Characteristics block |

### **Final value** — Final value of output signal in response to step input finite real scalar

To compute the other step response characteristics on the
**Bounds** tab, the block uses the expected final value of the
output signal in response to a step input.

By default, this parameter is `[]` for the Linear Step
Response Plot block and `1` for the Check Linear
Step Response Characteristics block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FinalValue` |
| **Type:** character vector |
| **Value:** finite real scalar |
| **Default:** `'[]'` for Linear Step Response Plot block, `'1'` for Check Linear Step Response Characteristics block |

### **Rise time** — Upper bound on rise time finite positive scalar

Upper bound on the time in seconds for the step response to reach a percentage of
the final value.

- To specify the final value, use the **Final value**
  parameter.
- To specify the percentage of the final value, use the **%
  Rise** parameter.

By default, this parameter is `[]` for the Linear Step
Response Plot block and `5` for the Check Linear
Step Response Characteristics block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RiseTime` |
| **Type:** character vector |
| **Value:** finite positive scalar |
| **Default:** `'[]'` for Linear Step Response Plot block, `'5'` for Check Linear Step Response Characteristics block |

### **% Rise** — Percentage of final value used for computing rise time positive scalar less than (100 - % Settling)

Percentage of the final value used to define the rise time bound.

- To specify the final value, use the **Final value**
  parameter.
- To specify the rise time bound, use the **Rise time**
  parameter.

By default, this parameter is `[]` for the Linear Step
Response Plot block and `80` for the Check Linear
Step Response Characteristics block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PercentRise` |
| **Type:** character vector |
| **Value:** positive scalar less than (100 - % Settling) |
| **Default:** `'[]'` for Linear Step Response Plot block, `'80'` for Check Linear Step Response Characteristics block |

### **Settling time** — Upper bound on settling time finite scalar greater than rise time

Upper bound on the time in seconds for the step response to settle within a
specified range around the final value. This settling range is defined as the final
value plus or minus the specified settling percentage of the final value.

- To specify the final value, use the **Final value**
  parameter.
- To specify the settling percentage, use the **% Settling**
  parameter.

By default, this parameter is `[]` for the Linear Step
Response Plot block and `7` for the Check Linear
Step Response Characteristics block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SettlingTime` |
| **Type:** character vector |
| **Value:** finite scalar greater than rise time |
| **Default:** `'[]'` for Linear Step Response Plot block, `'7'` for Check Linear Step Response Characteristics block |

### **% Settling** — Percentage of final value used for computing settling range positive scalar less than (100 - % Rise)

Percentage of the final value used to define the settling range bounds. The
settling range is defined as the final value plus or minus the specified settling
percentage of the final value.

- To specify the final value, use the **Final value**
  parameter.
- To specify the settling time bound, use the **Settling time**
  parameter.

By default, this parameter is `[]` for the Linear Step
Response Plot block and `1` for the Check Linear
Step Response Characteristics block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PercentSettling` |
| **Type:** character vector |
| **Value:** positive scalar less than (100 - % Settling) |
| **Default:** `'[]'` for Linear Step Response Plot block, `'1'` for Check Linear Step Response Characteristics block |

### **% Overshoot** — Upper bound on overshoot scalar between 0 and 100

The amount by which the step response can exceed the final value, defined as a
percentage of the final value. To specify the final value, use the **Final
value** parameter.

By default, this parameter is `[]` for the Linear Step
Response Plot block and `10` for the Check Linear
Step Response Characteristics block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PercentOvershoot` |
| **Type:** character vector |
| **Value:** scalar between 0 and 100 |
| **Default:** `'[]'` for Linear Step Response Plot block, `'10'` for Check Linear Step Response Characteristics block |

### **% Undershoot** — Upper bound on undershoot scalar between 0 and 100

The amount by which the step response can undershoot the initial value, defined as
a percentage of the final value. To specify the final value, use the **Final
value** parameter.

By default, this parameter is `[]` for the Linear Step
Response Plot block and `1` for the Check Linear
Step Response Characteristics block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PercentUndershoot` |
| **Type:** character vector |
| **Value:** scalar between 0 and 100 |
| **Default:** `'[]'` for Linear Step Response Plot block, `'1'` for Check Linear Step Response Characteristics block |

### Logging

To control whether linearization results computed during the simulation are saved, use
the parameters on the **Logging** tab. The default settings on this tab are
the same for the Linear Step Response Plot and Check Linear Step
Response Characteristics blocks.

### **Save data to workspace** — Save linear systems for further analysis `off` (default) | `on`

Select this parameter to save the computed linear systems for further analysis or control design. The data is saved in a structure with the following fields.

- `time` — Simulation times at which the linear systems are computed.
- `values` — State-space model representing the linear system. If the linear system is computed at multiple simulation times, `values` is an array of state-space models.
- `operatingPoints` — Operating points corresponding to each linear system in `values`. To enable this field, select the **Save operating points for each linearization** parameter.

To specify the name of the saved data structure, use the **Variable name** property.

The location of the saved data structure depends upon the configuration of the Simulink model.

- If the model is not configured to save simulation output as a single object, the data structure is a variable in the MATLAB workspace.
- If the model is configured to save simulation output as a single object, the data structure is a field in the `Simulink.SimulationOutput` object that contains the logged simulation data.

To configure your model to save simulation output in a single object, in the Configuration Parameters dialog box, select the **Single simulation output** parameter.

For more information about data logging in Simulink, see Save Simulation Data and the `Simulink.SimulationOutput` reference page.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaveToWorkspace` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Variable name** — Name of data structure for saving linear systems `sys` (default) | character vector

Specify the name of the data structure that stores linear systems computed during simulation.

The name must be unique among the variable names used in all data logging model blocks, such as Linear Analysis Plot blocks, Model Verification blocks, Scope blocks, To Workspace blocks, and simulation return variables such as time, states, and outputs.

For more information about data logging in Simulink, see Save Simulation Data and the `Simulink.SimulationOutput` reference page.

#### Dependencies

To enable this parameter, select the **Save data to workspace** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaveName` |
| **Type:** character vector |
| **Default:** `'sys'` |

### **Save operating points for each linearization** — Save operating points with linearization `off` (default) | `on`

Select this parameter to save the operating point at which each linearization is computed. Selecting this parameter adds the `operatingPoints` field to the saved data structure.

#### Dependencies

To enable this parameter, select the **Save data to workspace** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaveOperatingPoints` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### Assertion

To control the assertion behavior of the block when bounds defined on the
**Bounds** tab are violated, use the parameters on the
**Assertion** tab. The default settings on this tab are the same for the
Linear Step Response Plot and Check Linear Step Response
Characteristics blocks.

### **Enable assertion** — Enable bound checking `on` (default) | `off`

To check whether the bounds defined on the **Bounds** tab are satisfied
during the simulation, select this parameter. When a bound is not satisfied, the assertion
fails and a warning is generated.

Clearing this parameter disables assertion; that is, the block no longer checks that the specified bounds are satisfied. The block icon also updates to indicate that assertion is disabled.

Block with X indicating that assertion is disabled.

By default, on the **Bounds** tab:

- The Linear Step Response Plot block does not have defined
  bounds.
- The Check Linear Step Response Characteristics block has
  defined bounds.

You can configure your Simulink model to enable or disable all model verification blocks and override the **Enable assertion** parameter. To do so, in the Simulink model, in the Configuration Parameters dialog box, specify the **Model Verification block enabling** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `enabled` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Simulation callback when assertion fails** — Expression to evaluate when bounds are violated `''` (default) | MATLAB expression

Specify a MATLAB expression to evaluate when the bounds specified on the **Bounds** tab are violated. All variables used in the expression must be in the MATLAB workspace.

#### Dependencies

To enable this parameter, select the **Enable assertion** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `callback` |
| **Type:** character vector |
| **Value:** MATLAB expression |
| **Default:** `''` |

### **Stop simulation when assertion fails** — Stop simulation when bounds are violated `off` (default) | `on`

To stop the simulation when the bounds specified on the **Bounds** tab are violated, select this parameter. If you do not select this option, the bound violation is reported as a warning in the MATLAB Command Window and the simulation continues.

If you run the simulation from the Simulink model, when the assertion fails, the block where the bound violation occurs is highlighted and an error message is displayed in the Simulation Diagnostics window.

**Note**

Since selecting this option stops the simulation as soon as the assertion fails, bound violations that might occur later during the simulation are not reported. If you want all bound violations to be reported, do not select this option.

#### Dependencies

To enable this parameter, select the **Enable assertion** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `stopWhenAssertionFail` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output assertion signal** — Add assertion output port `off` (default) | `on`

Add the **z–1** assertion signal output port to
the block. This port outputs the value of the assertion as a Boolean signal. When the
bounds defined on the **Bounds** tab are violated, the assertion fails
and the assertion signal is `0`. Otherwise, the assertion signal is
`1`.

You can use the assertion signal to design complex assertion logic. For an example, see Verify Model Using Simulink Control Design and Simulink Verification Blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `export` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

## Libraries

Simulink Control Design / Linear Analysis Plots Simulink Control Design / Model Verification

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2010b**

## Description

Step response of linear system computed from nonlinear Simulink model

The Linear Step Response Plot and Check Linear Step Response
Characteristics blocks compute a linear system from a nonlinear Simulink® model and plot the step response of the linear system during simulation. These
blocks are identical except for the default settings on the **Bounds**
tab.

- The Linear Step Response Plot does not define default bounds.
- The Check Linear Step Response Characteristics block defines default
  bounds and enables these bounds for assertion.

For more information on time domain analysis of linear systems, see Time-Domain Responses.

During simulation, the software linearizes the portion of the model between specified
linearization inputs and outputs and then plots the step response of the linear system. You
also can save the linear system as a variable in the MATLAB® workspace.

The Simulink model can be continuous- or discrete-time
or multirate and can have time delays. Because you can specify only
one linearization input/output pair in this block, the linear system
is Single-Input Single-Output (SISO).

You can specify step response bounds and view them on the plot. You can also check that
the bounds are satisfied during simulation:

- If all bounds are satisfied, the block does nothing.
- If a bound is not satisfied, the block asserts and a warning message appears in the
  MATLAB Command Window. You can also specify that the block:

  - Evaluate a MATLAB expression.
  - Stop the simulation and bring that block into focus.

During simulation, the block can also output a logical assertion signal.

- If all bounds are satisfied, the signal is true (`1`).
- If any bound is not satisfied, the signal is false (`0`).

To compute and plot the step response of various portions of your model, you can add
multiple Linear Step Response Plot and Check Linear Step Response
Characteristics blocks.

These blocks do not support code generation and can be used only in
`Normal` simulation mode.
