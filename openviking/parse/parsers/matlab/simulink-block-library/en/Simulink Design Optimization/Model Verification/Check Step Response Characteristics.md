---
type: simulink-block
title: 'Check Step Response Characteristics'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkstepresponsecharacteristics'
documentation_source_path: 'ref/checkstepresponsecharacteristics.html'
language: en
---

# Check Step Response Characteristics

## Ports
```yaml
ports:
- name: Port_1 (u)
  summary: Signal to check against specified bounds scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | enumerated
    | bus
- name: Port_1 (out)
  summary: Output assertion signal 1 | 0
  direction: output
  data_types: Boolean | double
```

### Input

### **Port\_1 (u)** — Signal to check against specified bounds scalar | vector | matrix

Signal to check against the specified step response characteristics
during simulation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1 (out)** — Output assertion signal `1` | `0`

Output signal indicating if the input signal is within bounds of the
specified assertion signal. At each time step, the output is returned as
one of the following:

- True (`1`) if the assertion succeeds, that
  is, the signal satisfies all bounds
- False (`0`) if the assertion fails, that is,
  the signal violates a bound

The data type of the output signal is double by default. To set the
output data type as Boolean for all blocks that generate logic signals
in your Simulink model, select **Implement logic signals as Boolean
data** in Configuration Parameters.

#### Dependencies

To enable this port, on the **Assertion** tab,
select the **Output assertion signal**
parameter.

**Data Types:** `Boolean` | `double`
## Parameters
```yaml
parameters:
- name: Show Plot
  summary: Open plot window button
  group: ''
- name: Show plot on block open
  summary: Double-click block to open plot off (default) | on
  group: ''
  block_parameter: LaunchViewOnOpen
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Response Optimization
  summary: Open Response Optimizer button
  group: ''
- name: Include step response bound in assertion
  summary: Check that signal satisfies step response bounds on (default) | off
  group: Bounds Tab
  block_parameter: EnableStepResponseBound
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Step time
  summary: Time when step response bounds start 0 (default) | nonnegative scalar
  group: Bounds Tab
  block_parameter: StepTime
  type: character vector
  values: nonnegative scalar
  default: '0'
- name: Initial value
  summary: Signal value before step 0 (default) | scalar
  group: Bounds Tab
  block_parameter: InitialValue
  type: character vector
  values: scalar
  default: '0'
- name: Final value
  summary: Signal value after step 1 (default) | scalar
  group: Bounds Tab
  block_parameter: FinalValue
  type: character vector
  values: scalar
  default: '1'
- name: Rise time
  summary: Time taken to reach specified percentage of step range 5 (default) | positive scalar
  group: Bounds Tab
  block_parameter: RiseTime
  type: character vector
  values: positive scalar
  default: '5'
- name: '% Rise'
  summary: Percentage of step range value for rise time 80 (default) | scalar in range 0–100
  group: Bounds Tab
  block_parameter: PercentRise
  type: character vector
  values: scalar in range 0–100
  default: '80'
- name: Settling time (seconds)
  summary: Time taken to reach settling range 7 (default) | positive scalar
  group: Bounds Tab
  block_parameter: SettlingTime
  type: character vector
  values: positive scalar
  default: '7'
- name: '% Settling'
  summary: Settling range around final value 1 (default) | scalar in range 0–100
  group: Bounds Tab
  block_parameter: PercentSettling
  type: character vector
  values: scalar in range 0–100
  default: '1'
- name: '% Overshoot'
  summary: Amount by which signal can exceed final value 10 (default) | scalar in range 0–100
  group: Bounds Tab
  block_parameter: PercentOvershoot
  type: character vector
  values: scalar in range 0–100
  default: '10'
- name: '% Undershoot'
  summary: Amount by which signal can undershoot initial value 1 (default) | scalar in range 0–100
  group: Bounds Tab
  block_parameter: PercentUndershoot
  type: character vector
  values: scalar in range 0–100
  default: '1'
- name: Enable zero-crossing detection
  summary: Evaluate model at bound edges on (default) | off
  group: Bounds Tab
  block_parameter: ZeroCross
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Enable assertion
  summary: Enable or disable check on (default) | off
  group: Assertion Tab
  block_parameter: enabled
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Simulation callback when assertion fails (optional)
  summary: Expression to evaluate when assertion fails '' (default) | MATLAB expression
  group: Assertion Tab
  block_parameter: callback
  type: character vector
  values: MATLAB expression
  default: ''''''
- name: Stop simulation when assertion fails
  summary: Halt simulation when assertion fails off (default) | on
  group: Assertion Tab
  block_parameter: stopWhenAssertionFail
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Output assertion signal
  summary: Create output signal off (default) | on
  group: Assertion Tab
  block_parameter: export
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Show Plot** — Open plot window `button`

Use the plot to view the following.

- System characteristics and signals computed during simulation —
  Click this button before you simulate the model to view the system
  characteristics or signal.

  You can display additional characteristics, such as the peak
  response time, by right-clicking the plot and selecting
  **Characteristics**.
- Bounds — You can specify bounds on the **Bounds**
  tab or by right-clicking the plot and selecting **Bounds** > **New Bound**.

  You can modify bounds by dragging the bound segment or by
  right-clicking the plot and selecting **Bounds** > **Edit Bound**. Before you simulate the model, click
  **Update Block** to update the bound value in
  the block parameters.

Typical tasks that you perform in the plot window include:

- Opening the Block Parameters dialog box by clicking Open block parameters dialog icon or selecting
  **Edit**.
- Finding the block that the plot window corresponds to by clicking Highlight block icon or selecting **View** > **Highlight Simulink Block**. This action makes the model window active and
  highlights the block.
- Simulating the model by clicking Run icon. This action also linearizes the
  portion of the model between the specified linearization input and
  output.
- Adding a legend on the linear system characteristic plot by
  clicking Insert legend icon.

### **Show plot on block open** — Double-click block to open plot `off` (default) | `on`

Open the plot window instead of the block parameters when you double-click
the block in the Simulink model.

Use this parameter if you prefer to open and perform tasks, such as adding
or modifying bounds, in the plot window instead of the block parameters. If
you want to access the block parameters from the plot window, select
**Edit** or click Open block parameters dialog icon.

For more information on the plot, see the **Show plot**
parameter.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `LaunchViewOnOpen` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Response Optimization** — Open Response Optimizer `button`

Open the Response Optimizer to optimize the model response to
meet design requirements specified on the **Bounds**
tab.

#### See Also

- Design Optimization to Meet Step Response Requirements (GUI)
- Design Optimization to Meet Time-Domain and Frequency-Domain Requirements (GUI)

### Bounds Tab

### **Include step response bound in assertion** — Check that signal satisfies step response bounds `on` (default) | `off`

Check that the signal satisfies *all* the step response
characteristics specified on the **Bounds** tab. The
software displays a warning if the signal violates the specified step
response characteristics.

To view the specified step response bounds on a plot, click
**Show Plot**.

Specified step response bounds on a plot

By default, the line segments represent the following step response
requirements:

- Amplitude greater than or equal to –0.01 up to the rise
  time of 5 seconds for 1% undershoot
- Amplitude greater than or equal to 0.8 between 5 and 7
  seconds for 80% rise
- Amplitude less than or equal to 1.1 up to the settling
  time of 7 seconds for 10% overshoot
- Amplitude between 0.99 and 1.01 beyond the settling time
  for 1% settling

When you disable this parameter, the software stops checking that the input signal
satisfies the bounds during simulation. The bound segments are also
grayed out on the plot.

Grayed out bound segments on the plot

To view only the bounds and input signal on the plot, clear **Enable
assertion**.

#### Dependencies

To use this parameter, on the **Assertion** tab,
select **Enable assertion**. If you clear
**Enable assertion**, the software does not use
the bounds for assertion, but they continue to appear on the
plot.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `EnableStepResponseBound` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Step time** — Time when step response bounds start `0` (default) | nonnegative scalar

Time, in seconds, when the step response bounds start, specified as a finite, real,
nonnegative scalar.

To modify the step time value from the plot window, drag the
corresponding bound segment. Alternatively, right-click the segment, and
select **Edit**. Specify the new value in
**Step time**. Click **Update
Block** before simulating the model.

To check that the input signal satisfies the step time value, select both
**Include step response bound in assertion** and
**Enable assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `StepTime` |
| **Type:** character vector |
| **Value:** nonnegative scalar |
| **Default:** `0` |

### **Initial value** — Signal value before step `0` (default) | scalar

Value of the signal before the step occurs, specified as a finite real scalar not equal
to the **Final value** parameter.

To modify the initial value from the plot window, drag the
corresponding bound segment. Alternatively, right-click the segment, and
select **Edit**. Specify the new value in
**Initial value**. Click **Update
Block** before simulating the model.

To check that the input signal satisfies the initial value, select both
**Include step response bound in assertion** and
**Enable assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `InitialValue` |
| **Type:** character vector |
| **Value:** scalar |
| **Default:** `0` |

### **Final value** — Signal value after step `1` (default) | scalar

Value of the signal after the step occurs, specified as a finite real scalar not equal
to the **Initial value** parameter.

To modify the final value from the plot window, drag the corresponding
bound segment. Alternatively, right-click the segment, and select
**Edit**. Specify the new value in
**Final value**. You must click **Update
Block** before simulating the model.

To check the input signal satisfies the final value, select both **Include step
response bound in assertion** and **Enable
assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `FinalValue` |
| **Type:** character vector |
| **Value:** scalar |
| **Default:** `1` |

### **Rise time** — Time taken to reach specified percentage of step range `5` (default) | positive scalar

Time taken, in seconds, for the signal to reach the percentage of the
step range (**Final value** – **Initial
value**) specified in **% Rise**,
specified as a finite, positive, real scalar less than the
**Settling time** parameter.

To modify the rise time from the plot window, drag the corresponding
bound segment. Alternatively, right-click the segment, and select
**Edit**. Specify the new value in
**Rise time**. Click **Update
Block** before simulating the model.

To check that the input signal satisfies the rise time value, select
both **Include step response bound in assertion** and
**Enable assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `RiseTime` |
| **Type:** character vector |
| **Value:** positive scalar |
| **Default:** `5` |

### **% Rise** — Percentage of step range value for rise time `80` (default) | scalar in range 0–100

The percentage of the step range value to use along with
**Rise time** to define the overall rise time
characteristics, specified as a real finite scalar in range 0–100 and
less than 100 – **% Settling**.

To modify the percent rise from the plot window, drag the
corresponding bound segment. Alternatively, right-click the segment, and
select **Edit**. Specify the new value in
**% Rise**. Click **Update
Block** before simulating the model.

To check that the input signal satisfies the percent rise value,
select both **Include step response bound in
assertion** and **Enable
assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PercentRise` |
| **Type:** character vector |
| **Value:** scalar in range 0–100 |
| **Default:** `80` |

### **Settling time (seconds)** — Time taken to reach settling range `7` (default) | positive scalar

The time taken, in seconds, for the signal to settle within a specified range around the
final value, specified as a finite positive real scalar greater than
**Rise time**. This settling range is defined as
the final value plus or minus the settling range value. Specify the
settling range in the **% Settling** parameter.

To modify the settling time from the plot window, drag the
corresponding bound segment. Alternatively, right-click the segment, and
select **Edit**. Specify the new value in
**Settling time**. Click **Update
Block** before simulating the model.

To check that the input signal satisfies the settling time value, select both
**Include step response bound in assertion** and
**Enable assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `SettlingTime` |
| **Type:** character vector |
| **Value:** positive scalar |
| **Default:** `7` |

### **% Settling** — Settling range around final value `1` (default) | scalar in range 0–100

The percentage of the step range value (**Final value** –
**Initial value**) that defines the settling range
of the **Settling time** characteristic, specified as a
finite real scalar in the range 0–100. Specify a value less than both
100 – **% Rise** and **%
Overshoot**.

To modify the percent settling from the plot window, drag the
corresponding bound segment. Alternatively, right-click the segment, and
select **Edit**. Specify the new value in **%
Settling**. Click **Update Block**
before simulating the model.

To check that the input signal satisfies the percent settling value, select both
**Include step response bound in assertion** and
**Enable assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PercentSettling` |
| **Type:** character vector |
| **Value:** scalar in range 0–100 |
| **Default:** `1` |

### **% Overshoot** — Amount by which signal can exceed final value `10` (default) | scalar in range 0–100

The amount by which the signal can exceed the final value before settling, specified as
a positive real scalar in the range 0–100 and greater than **%
Settling**. This amount is specified as a percentage of
step range. The step range is the difference between the final and
initial values.

To modify the percent overshoot from the plot window, drag the
corresponding bound segment. Alternatively, right-click the segment, and
select **Edit**. Specify the new value in **%
Overshoot**. Click **Update Block**
before simulating the model.

To check that the input signal satisfies the percent overshoot value, select both
**Include step response bound in assertion** and
**Enable assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PercentOvershoot` |
| **Type:** character vector |
| **Value:** scalar in range 0–100 |
| **Default:** `10` |

### **% Undershoot** — Amount by which signal can undershoot initial value `1` (default) | scalar in range 0–100

The amount by which the signal can undershoot the initial value before
rising, specified as a positive real scalar in the range 0–100. This
amount is specified as a percentage of the step range. The step range is
the difference between the final and initial values.

To modify the percent undershoot from the plot window, drag the
corresponding bound segment. Alternatively, right-click the segment, and
select **Edit**. Specify the new value in **%
Undershoot**. Click **Update Block**
before simulating the model.

To check that the input signal satisfies the percent undershoot value,
select both **Include step response bound in
assertion** and **Enable
assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PercentUndershoot` |
| **Type:** character vector |
| **Value:** scalar in range 0–100 |
| **Default:** `1` |

### **Enable zero-crossing detection** — Evaluate model at bound edges `on` (default) | `off`

Ensure that the software simulates the model to produce output at the
bound edges. Simulating the model at the bound edges prevents the
simulation solver from missing an assertion that the signal satisfies
that bound at its edge.

Graph showing the time points at which the model is simulated

For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `ZeroCross` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'on'` |

### Assertion Tab

### **Enable assertion** — Enable or disable check `on` (default) | `off`

Enable the block to check that bounds specified and included for
assertion on the **Bounds** tab are satisfied during
simulation. Assertion fails if a bound is not satisfied. A warning,
reporting the assertion failure, appears at the MATLAB prompt.

If the assertion fails, you can optionally specify that the
block:

- Execute a MATLAB expression, specified in **Simulation
  callback when assertion fails (optional)**.
- Stop the simulation and return an error message, by selecting
  **Stop simulation when assertion
  fails**.

This parameter has no effect if you do not specify any bounds.

When you disable this parameter, the block no longer checks that the
input signal satisfies the specified bounds. The block icon also updates
to indicate that assertion is disabled.

Crossed out block icon

In the Simulink model, in the Configuration Parameters, the
**Model Verification block enabling** parameter
lets you enable or disable all model verification blocks in a model,
regardless of the setting of this option in the block.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `enabled` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Simulation callback when assertion fails (optional)** — Expression to evaluate when assertion fails `''` (default) | MATLAB expression

MATLAB expression to execute when assertion fails.

Because the expression is evaluated in the MATLAB workspace, first define all variables used in the
expression in the workspace.

#### Dependencies

To enable this parameter, select **Enable
assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `callback` |
| **Type:** character vector |
| **Value:** MATLAB expression |
| **Default:** `''` |

### **Stop simulation when assertion fails** — Halt simulation when assertion fails `off` (default) | `on`

Stop the simulation when the input signal violates a bound specified
on the **Bounds** tab during simulation, that is, when
assertion fails.

If you run the simulation from a Simulink model window, the Simulation Diagnostics window opens to
display an error message. The block where the bound violation occurs is
highlighted in the model.

Because selecting this option stops the simulation as soon as the
assertion fails, the software does not report assertion failures that
might occur later during the simulation. If you want to report
*all* assertion failures, do not select this
option.

#### Dependencies

To enable this parameter, select **Enable
assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `stopWhenAssertionFail` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Output assertion signal** — Create output signal `off` (default) | `on`

Output a Boolean signal that, at each time step, is:

- True (`1`) if assertion succeeds, that is,
  the input signal satisfies all bounds
- False (`0`) if assertion fails, that is, the
  input signal violates a bound

The data type of the output signal is double by default. To set the
output data type as Boolean for all blocks that generate logic signals
in your Simulink model, select Implement logic signals as Boolean data in
Configuration Parameters.

Selecting this parameter adds an output port to the block that you can
connect to any block in the model.

Use this parameter to design complex assertion logic. For an example,
see Verify Model Using Simulink Control Design and Simulink Verification Blocks (Simulink Control Design).

#### Programmatic Use

|  |
| --- |
| **Parameter:** `export` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |
## Libraries

Simulink Design Optimization / Model Verification Simulink Design Optimization / Signal Constraints

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Code generation is available only when the **Output assertion signal**
parameter is enabled.

## Version History

**Introduced in R2011b**

## Description

Check that model signal satisfies step response bounds during simulation

Check that a signal satisfies the step response bounds during simulation.

- If the signal satisfies all bounds, the block does nothing.
- If the signal does not satisfy a bound, a warning message appears in the MATLAB® command window. You can also specify that the block:

  - Evaluate a MATLAB expression.
  - Stop the simulation and return an error message.

During simulation, the block can also return a logical assertion signal.

- If the signal satisfies all bounds, the assertion signal is true
  (`1`).
- If the signal does not satisfy a bound, the assertion signal is false
  (`0`).

You can add Check Step Response Characteristics blocks to multiple signals to
check that they satisfy the bounds. You can also plot the bounds on a time plot to
graphically verify that the signal satisfies the bounds.

This block and the other blocks in the Model Verification library
test that a signal remains within specified time-domain characteristic
bounds. When a model does not violate any bound, you can disable the
block by clearing the assertion option. If you modify the model, you
can re-enable assertion to ensure that your changes do not cause the
model to violate a bound.

If the signal does not satisfy the bounds, you can optimize the model parameters to satisfy
the bounds. If you have Simulink®
Control Design™ software, you can add frequency-domain bounds, such as the Bode magnitude, and
optimize the model response to satisfy both time-domain and frequency-domain
requirements.

The block can be used in all simulation modes for signal monitoring, but only in
`Normal` or `Accelerator` simulation
mode for response optimization.
