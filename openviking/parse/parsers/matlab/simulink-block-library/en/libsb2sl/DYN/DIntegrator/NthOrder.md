---
type: simulink-block
title: 'Integrator'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'DYN / CIntegrator'
documentation_page: 'integrator'
documentation_source_path: '../simulink/slref/integrator.html'
language: en
---

# Integrator

## Ports
```yaml
ports:
- name: Port_1
  summary: Signal to integrate scalar | vector | matrix
  direction: input
  data_types: double
- name: External Reset
  summary: Signal for resetting state to initial condition scalar | vector | matrix
  direction: input
  data_types: Boolean
- name: x0
  summary: Initial condition scalar | vector | matrix
  direction: input
  data_types: double
- name: Port_1
  summary: Integrated signal scalar | vector | matrix
  direction: output
  data_types: double
- name: Port_2
  summary: Output saturation signal scalar | vector | matrix
  direction: output
  data_types: double
- name: Port_3
  summary: Block state scalar | vector | matrix
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Signal to integrate scalar | vector | matrix

The input signal is a real-valued scalar, vector, or matrix that this
block integrates.

This port does not have direct feedthrough.

**Data Types:** `double`

### **External Reset** — Signal for resetting state to initial condition scalar | vector | matrix

The external reset signal is a Boolean scalar, vector, or matrix that
resets the block state to the initial condition. See Resetting the State.

This port has direct feedthrough.

#### Dependencies

To enable this port, select **External
Reset**.

**Data Types:** `Boolean`

### **x0** — Initial condition scalar | vector | matrix

The initial condition signal is a real-valued scalar, vector, or
matrix that sets the initial condition for the block.

This port has direct feedthrough.

#### Dependencies

To enable this port, set the **Initial
Conditions** parameter to
`external`.

**Data Types:** `double`
### Output

### **Port\_1** — Integrated signal scalar | vector | matrix

The output signal is a scalar, vector, or matrix with the value of the
integrated input signal. The dimensions of the integrated signal match
the dimensions of the input signal.

**Data Types:** `double`

### **Port\_2** — Output saturation signal scalar | vector | matrix

The output saturation signal is a scalar, vector, or matrix that
indicates when each element in the block state is limited by the upper
or lower saturation limit. The signal value indicates whether the value
is limited and which limit is applied.

- `-1` — Value limited by lower saturation
  limit
- `0` — Value not limited by either
  saturation limit
- `1` — Value limited by upper saturation
  limit

For more information, see Limiting the Integral.

#### Dependencies

To enable this port, select **Show saturation
port**.

**Data Types:** `double`

### **Port\_3** — Block state scalar | vector | matrix

The block state signal is a real-valued scalar, vector, or matrix with
a value that matches the block state value.

For more information, see About the State Port.

#### Dependencies

To enable this port, select **Show state
port**.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: External reset
  summary: Reset states to their initial conditions none (default) | rising | falling | either | level | level hold
  group: ''
  block_parameter: ExternalReset
  type: character vector , string
  values: '''none'' | ''rising'' | ''falling'' | ''either'' | ''level'' | ''level hold'''
  default: '''none'''
- name: Initial condition source
  summary: Option to set initial condition using external signal internal (default) | external
  group: ''
  block_parameter: InitialConditionSource
  type: character vector, string
  values: '''internal'' | ''external'''
  default: '''internal'''
- name: Initial condition
  summary: Initial state 0 (default) | real scalar or array
  group: ''
  block_parameter: InitialCondition
  type: scalar or vector
  default: '''0'''
- name: Limit output
  summary: Limit block output values to specified range off (default for Integrator) | on (default for Integrator Limited)
  group: ''
  block_parameter: LimitOutput
  type: character vector , string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Upper saturation limit
  summary: Upper limit for the integral inf (default) | scalar | vector | matrix
  group: ''
  block_parameter: UpperSaturationLimit
  type: character vector, string
  values: scalar | vector | matrix
  default: '''inf'''
- name: Lower saturation limit
  summary: Lower limit for the integral -inf (default) | scalar | vector | matrix
  group: ''
  block_parameter: LowerSaturationLimit
  type: character vector , string
  values: scalar | vector | matrix
  default: '''-inf'''
- name: Wrap state
  summary: Enable wrapping of states off (default) | on
  group: ''
  block_parameter: WrapState
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Wrapped state upper value
  summary: Specify upper value for wrapped state pi (default) | scalar | vector
  group: ''
  block_parameter: WrappedStateUpperValue
  type: scalar or vector
  values: '''2*pi'''
  default: '''pi'''
- name: Wrapped state lower value
  summary: Specify lower value for wrap state -pi (default) | scalar | vector
  group: ''
  block_parameter: WrappedStateLowerValue
  type: scalar or vector
  values: '''0'''
  default: '''-pi'''
- name: Show saturation port
  summary: Enable saturation output port off (default) | on
  group: ''
  block_parameter: ShowSaturationPort
  type: character vector , string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Show state port
  summary: Enable state output port off (default) | on
  group: ''
  block_parameter: ShowStatePort
  type: character vector , string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Absolute tolerance
  summary: Absolute tolerance for block states auto (default) | real scalar or vector
  group: ''
  block_parameter: AbsoluteTolerance
  type: character vector, string, scalar, or vector
  values: '''auto'' | ''-1'' | any positive real scalar or vector'
  default: '''auto'''
- name: Ignore limit and reset when linearizing
  summary: Option to use default reset and limit behavior for block during linearization off (default) | on
  group: ''
  block_parameter: IgnoreLimit
  type: character vector | string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Enable zero-crossing detection
  summary: Enable zero-crossing detection on (default) | off
  group: ''
  block_parameter: ZeroCross
  type: character vector | string
  values: '''off'' | ''on'''
  default: '''on'''
- name: State Name (e.g., 'position')
  summary: Assign unique name to each state ' ' (default) | character vector | string
  group: ''
  block_parameter: ContinuousStateAttributes
  type: character vector, string
  values: ''' '' | user-defined'
  default: ''' '''
```

### **External reset** — Reset states to their initial conditions `none` (default) | `rising` | `falling` | `either` | `level` | `level hold`

Specify the type of trigger to use for the external reset signal.

- Select `rising` to reset the state when the
  reset signal rises from a negative or zero value to a positive value, or
  a negative value to zero value.
- Select `falling` to reset the state when the
  reset signal falls from a positive value to a zero or negative value, or
  from a zero value to negative value.
- Select `either` to reset the state when the
  reset signal changes from zero to a nonzero value, from a nonzero value
  to zero, or changes sign.
- Select `level` to reset the state when the
  reset signal is nonzero at the current time step or changes from nonzero
  at the previous time step to zero at the current time step.
- Select `level hold` to reset the state when
  the reset signal is nonzero at the current time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ExternalReset` |
| **Type:**  character vector , string |
| **Values:**  `'none'` | `'rising'` | `'falling'` | `'either'` | `'level'` | `'level hold'` |
| **Default:**  `'none'` |

### **Initial condition source** — Option to set initial condition using external signal `internal` (default) | `external`

Select source of initial condition:

- `internal` — Get the initial conditions of the states
  from the **Initial condition** parameter.
- `external` — Get the initial conditions of the states
  from an external signal. When you select this option, an input port appears on
  the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`InitialConditionSource` |
| **Type:**  character vector, string |
| **Values:**  `'internal'` | `'external'` |
| **Default:**  `'internal'` |

### **Initial condition** — Initial state 0 (default) | real scalar or array

Set the initial state of the Integrator block.

#### Tips

Simulink software does not allow the initial condition of this block to be
`inf` or `NaN`.

#### Dependencies

Setting **Initial condition source** to
`internal` enables this parameter.

Setting **Initial condition source** to
`external` disables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`InitialCondition` |
| **Type:**  scalar or vector |
| **Default:**  `'0'` |

### **Limit output** — Limit block output values to specified range `off` (default for Integrator) | `on` (default for Integrator Limited)

Limit the block's output to a value between the **Lower
saturation limit** and **Upper saturation
limit** parameters.

- Selecting this check box limits the block output to a value between the
  **Lower saturation limit** and **Upper saturation limit** parameters.
- Clearing this check box does not limit the block output values.

#### Dependencies

Selecting this parameter enables the **Lower saturation
limit** and **Upper saturation limit**
parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `LimitOutput` |
| **Type:**  character vector , string |
| **Values:**  `'off'` | `'on'` |
| **Default:**  `'off'` |

### **Upper saturation limit** — Upper limit for the integral `inf` (default) | scalar | vector | matrix

Specify the upper limit for the integral as a scalar,
vector, or matrix. You must specify a value
between the **Output minimum**
and **Output maximum** parameter
values.

#### Dependencies

To enable this parameter, select the
**Limit output** check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UpperSaturationLimit` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix |
| **Default:** `'inf'` |

### **Lower saturation limit** — Lower limit for the integral `-inf` (default) | scalar | vector | matrix

Specify the lower limit for the integral as a scalar, vector, or matrix. You must
specify a value between the **Output minimum** and **Output
maximum** parameter values.

#### Dependencies

To enable this parameter, select the **Limit output** check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LowerSaturationLimit` |
| **Type:** character vector , string |
| **Values:** scalar | vector | matrix |
| **Default:** `'-inf'` |

### **Wrap state** — Enable wrapping of states `off` (default) | `on`

Enable wrapping of states between the **Wrapped state upper
value** and **Wrapped state lower value** parameters.
Enabling wrap states eliminates the need for zero-crossing detection, reduces solver
resets, improves solver performance and accuracy, and increases simulation time span
when modeling rotary and cyclic state trajectories.

If you specify **Wrapped state upper value** as
`inf` and **Wrapped state lower value** as
`-inf`, wrapping does not occur.

#### Dependencies

Selecting this parameter enables **Wrapped state upper
value** and **Wrapped state lower value**
parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`WrapState` |
| **Type:**  character vector, string |
| **Values:**  `'off'` | `'on'` |
| **Default:**  `'off'` |

### **Wrapped state upper value** — Specify upper value for wrapped state `pi` (default) | scalar | vector

Upper limit of the block output.

#### Dependencies

Selecting **Wrap state** enables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`WrappedStateUpperValue` |
| **Type:**  scalar or vector |
| **Values:**  `'2*pi'` |
| **Default:**  `'pi'` |

### **Wrapped state lower value** — Specify lower value for wrap state `-pi` (default) | scalar | vector

Lower limit of the block output.

#### Dependencies

Selecting **Wrap state** enables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`WrappedStateLowerValue` |
| **Type:**  scalar or vector |
| **Values:**  `'0'` |
| **Default:**  `'-pi'` |

### **Show saturation port** — Enable saturation output port `off` (default) | `on`

Select this check box to add a saturation output port to the block. When you clear this check box, the block does not have a saturation output port.

#### Dependencies

Selecting this parameter enables a saturation output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowSaturationPort` |
| **Type:** character vector , string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Show state port** — Enable state output port `off` (default) | `on`

Select this check box to add a state output port to the block. When you clear this check box, the block does not have a state output port.

#### Dependencies

Selecting this parameter enables a state output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowStatePort` |
| **Type:** character vector , string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Absolute tolerance** — Absolute tolerance for block states `auto` (default) | real scalar or vector

- If you enter `auto` or –1, then Simulink uses the absolute tolerance value in the Configuration
  Parameters dialog box (see Solver Pane) to compute
  block states.
- If you enter a real scalar, then that value overrides the absolute
  tolerance in the Configuration Parameters dialog box for computing all block
  states.
- If you enter a real vector, then the dimension of that vector must match
  the dimension of the continuous states in the block. These values override
  the absolute tolerance in the Configuration Parameters dialog box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `AbsoluteTolerance` |
| **Type:**  character vector, string, scalar, or vector |
| **Values:**  `'auto'` | `'-1'` | any positive real scalar or vector |
| **Default:** `'auto'` |

### **Ignore limit and reset when linearizing** — Option to use default reset and limit behavior for block during linearization `off` (default) | `on`

When you select this parameter, the software ignores reset and limit parameters
for this block during linearization and uses default values for those
parameters.

#### Tip

Enable this parameter when you want to linearize a model around an operating
point that causes the integrator to reset or saturate.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IgnoreLimit` |
| **Type:**  character vector | string |
| **Values:**  `'off'` | `'on'` |
| **Default:**  `'off'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector | string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

### **State Name (e.g., 'position')** — Assign unique name to each state `' '` (default) | character vector | string

- To assign a name to a single state, enter the name between quotes, for
  example, `'velocity'`.
- To assign names to multiple states, enter a comma-delimited list
  surrounded by braces, for example, `{'a', 'b', 'c'}`. Each
  name must be unique.
- The state names apply only to the selected block.
- The number of states must divide evenly among the number of state
  names.
- You can specify fewer names than states, but you cannot specify more names
  than states.

  For example, you can specify two names in a system with four states. The
  first name applies to the first two states and the second name to the last
  two states.
- To assign state names with a variable in the MATLAB® workspace, enter the variable without quotes. A variable can
  be a character vector, string, cell array, or structure.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ContinuousStateAttributes` |
| **Type:**  character vector, string |
| **Values:**  `' '` | user-defined |
| **Default:**  `' '` |
## Libraries

Simulink / Commonly Used Blocks Simulink / Continuous

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |
|  |  |
| --- | --- |
| a Ports of this block have different direct feedthrough characteristics. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- Consider discretizing the model
- Not recommended for production code

## Version History

**Introduced before R2006a**

## Description

Integrate signal

The Integrator block integrates an input signal with respect to time
and provides the result as an output signal.

Simulink® treats the Integrator block as a dynamic system with one state.
The block dynamics are given by:

{x˙(t)=u(t)y(t)=x(t)   x(t0)=x0

where:

- *u* is the block input.
- *y* is the block output.
- *x* is the block state.
- *x0* is the initial condition of
  *x*.

While these equations define an exact relationship in continuous time, Simulink uses numerical approximation methods to evaluate them with finite
precision. Simulink can use several different numerical integration methods to compute
the output of the block, each with advantages in particular applications. Use the **Solver** pane of the Configuration Parameters dialog box (see Solver Pane) to select the technique best suited to your application.

The selected solver computes the output of the Integrator block at the
current time step, using the current input value and the value of the state at the previous
time step. To support this computational model, the Integrator block saves
its output at the current time step for use by the solver to compute its output at the next
time step. The block also provides the solver with an initial condition for use in computing
the block's initial state at the beginning of a simulation. The default value of the initial
condition is 0. Use the block parameter dialog box to specify another value for the initial
condition or create an initial value input port on the block.

Use the parameter dialog box to:

- Define upper and lower limits on the integral
- Create an input that resets the block's output (state) to its initial value,
  depending on how the input changes
- Create an optional state output so that the value of the block's output can
  trigger a block reset

Use the Discrete-Time Integrator block to create a purely discrete
system.

### Defining Initial Conditions

You can define the initial conditions as a parameter on the block dialog box or input them from an external signal:

- To define the initial conditions as a block parameter, specify the **Initial condition source** parameter as `internal` and enter the value in the **Initial condition** field.
- To provide the initial conditions from an external source, set the
  **Initial condition source** parameter to
  `external`. An additional input port appears on the
  block.

  An Integrator block configured with an initial condition port has two input ports and one output port.

  **Note**

  If you select the **Limit output** parameter, the initial
  condition must be within the saturation limits. If the initial condition is not
  within the block saturation limits, the block displays an error message.

### Limiting the Integral

To limit the output signal to a specified range of values, select **Limit
output** and specify the saturation limits. When the output reaches one of the
limits, the integral action is disabled to prevent integral wind up. During a simulation,
you can change the limits but not whether the output is limited. The block determines output
signal value using these criteria:

- When the integral value is less than or equal to the lower saturation limit, the
  output signal value is the lower saturation limit.
- When the integral value is between the lower saturation limit and the upper
  saturation limit, the output is the integral value.
- When the integral value is greater than or equal to the upper saturation limit,
  the output signal value is the upper saturation limit.

To generate a signal that indicates when the state is limited by the saturation limits, select
**Show saturation port**. A second output port appears on the
block.

An Integrator block configured to limit the output and show the saturation port. The block has two output signals: the first is labeled Output and the second is labeled Saturation.

The saturation signal has one of three values:

- `1` — State limited by upper saturation limit
- `0` — State not limited
- `–1` — State limited by lower saturation limit

When you limit the Integrator block output, the block has three zero crossing
signals: one to detect when the integral value exceeds the upper saturation limit, one to
detect when the integral value is less than the lower saturation limit, and one to detect
when the integral value changes from being saturated to not being saturated.

**Note**

By default, the **Limit output** parameter is enabled for the
Integrator Limited block, with the **Upper saturation
limit** parameter value set to `1`, and the
**Lower saturation limit** parameter value set to
`0`.

### Wrapping Cyclic States

Several physical phenomena, such as oscillators and machinery that exhibits rotational
movement, are cyclic, periodic, or rotary in nature. Modeling these phenomena in a
Simulink block diagram involves integrating the rate of change for the periodic or
cyclic signals to obtain the state of the movement. Over long simulation time spans, this
approach can result in the states that represent periodic or cyclic signals integrating to
large values. Computing trigonometric values, such as sine or cosine, for these signals
takes longer as the values become larger due to angle reduction. As the signal values become
larger, solver performance and accuracy degrades.

One approach for overcoming this drawback is to reset the angular state to
`0` when it reaches 2π (or to –π when it reaches π, for numerical
symmetry). This approach improves the accuracy of sine and cosine computations and reduces
angle reduction time. But it also requires zero-crossing detection and introduces solver
resets, which slow down the simulation for variable step solvers, particularly in large
models.

To eliminate solver resets at wrap points, the Integrator block supports wrapped states
that you can enable by checking **Wrap state** on the block parameter
dialog box. When you enable **Wrap state**, the block icon changes to
indicate that the block has wrapping states.

An Integrator block configured to wrap state values. The block icon is annotated with a circle with arrows.

The Integrator block supports wrapping states that are bounded by upper and
lower values parameters of the wrapped state. The algorithm for determining wrapping states
is given by:

y={xx∈[xl,xu)x−(xu−xl)⌊x−xlxu−xl⌋otherwise

where:

- *xl* is the lower value of the wrapped
  state.
- *xu* is the upper value of the wrapped
  state.
- *y* is the output.

The support for wrapping states provides these advantages.

- It eliminates simulation instability when your model approaches large angles
  and large state values.
- It reduces the number of solver resets during simulation and eliminates the
  need for zero-crossing detection, improving simulation time.
- It eliminates large angle values, speeding up computation of trigonometric
  functions on angular states.
- It improves solver accuracy and performance and enables unlimited simulation
  time.

### Resetting the State

The block can reset its state to the specified initial condition based on an external signal. To cause the block to reset its state, select one of the **External reset** choices. A trigger port appears below the block's input port and indicates the trigger type.

An integrator block configured to reset the state. The block has two input signals, labeled Input and Reset, and one output signal, labeled Output.

- Select `rising` to reset the state when the reset signal rises from a negative or zero value to a positive value.
- Select `falling` to reset the state when the reset signal falls from a positive value to a zero or negative value.
- Select `either` to reset the state when the reset signal changes from zero to a nonzero value, from a nonzero value to zero, or changes sign.
- Select `level` to reset the state when the reset signal is nonzero at the current time step or changes from nonzero at the previous time step to zero at the current time step.
- Select `level hold` to reset the state when the reset signal is nonzero at the current time step.

The reset port has direct feedthrough. If the block output feeds back into this port, either directly or through a series of blocks with direct feedthrough, an algebraic loop results (see Algebraic Loop Concepts). Use the Integrator block's state port to feed back the block's output without creating an algebraic loop.

**Note**

To be compliant with the Motor Industry Software Reliability Association (MISRA™) software standard, your model must use Boolean signals to drive the external reset ports of Integrator blocks.

### About the State Port

Selecting the **Show state port** check box on the Integrator block's parameter dialog box causes an additional output port, the state port, to appear at the top of the Integrator block.

An integrator block configured to show the state port. The block has one input signal, labeled Input, and two output signals. The state output port is on the top of the block, and the port that provides the output signal value is on the right of the block.

The output of the state port is the same as the output of the block's standard output port except for the following case. If the block is reset in the current time step, the output of the state port is the value that would have appeared at the block's standard output if the block had not been reset. The state port's output appears earlier in the time step than the output of the Integrator block's output port. Use the state port to avoid creating algebraic loops in these modeling scenarios:

- Systems that use self-resetting integrators
- Passing states from one enabled subsystem to another

  **Note**

  When updating a model, Simulink checks that the state port applies to one of these two scenarios.
  If not, an error message appears. Also, you cannot log the output of this port
  in a referenced model that executes in Accelerator mode. If logging is enabled
  for the port, Simulink generates a "signal not found" warning during execution of the
  referenced model.

### Specifying the Absolute Tolerance for the Block Outputs

By default Simulink software uses the absolute tolerance value specified in the Configuration Parameters dialog box (see Error Tolerances for Variable-Step Solvers) to compute the output of the Integrator block. If this value does not provide sufficient error control, specify a more appropriate value in the **Absolute tolerance** field of the Integrator block dialog box. The value that you specify is used to compute all the block outputs.
