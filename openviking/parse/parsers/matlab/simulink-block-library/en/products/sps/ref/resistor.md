---
type: simulink-block
title: 'Resistor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Basic'
documentation_page: 'resistor'
documentation_source_path: 'ref/resistor.html'
language: en
---

# Resistor

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the resistor positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the resistor negative
terminal.

### **H** — Resistor thermal mass thermal

Thermal conserving port that represents the resistor thermal mass.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and specify how the
resistance value changes with temperature and to set the thermal
mass.

### Main

### **Resistance** — Nominal resistance value `1` `Ohm` (default)

Nominal resistance value. Resistance value must be greater than zero.

### **Tolerance (%)** — Resistor tolerance, in percent `5` (default)

Resistor tolerance as defined on the manufacturer datasheet.

### **Tolerance application** — Select how to apply tolerance during simulation `None — use nominal value` (default) | `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

Select how to apply tolerance during simulation:

- `None — use nominal value`
  — The block does not apply tolerance. The block uses the
  nominal resistance value.
- `Random tolerance` — The block
  applies random offset to the resistance value, within the
  tolerance value limit. You can choose Uniform or Gaussian
  distribution for calculating the random number by using the
  **Tolerance distribution**
  parameter.
- `Apply maximum tolerance value`
  — The resistance is increased by the specified tolerance
  percent value.
- `Apply minimum tolerance value`
  — The resistance is decreased by the specified tolerance
  percent value.

### **Tolerance distribution** — Select the distribution type `Uniform` (default) | `Gaussian`

Select the distribution type for random tolerance:

- `Uniform` — Uniform
  distribution
- `Gaussian` — Gaussian
  distribution

#### Dependencies

To enable this parameter, set **Tolerance application** to
`Random tolerance`.

### **Number of standard deviations for quoted tolerance** — Used for calculating the Gaussian random number `4` (default)

Number of standard deviations for calculating the Gaussian random
number.

#### Dependencies

To enable this parameter, set **Tolerance distribution** to
`Gaussian`.

### Operating Limits

### **Enable operating limits** — Select `Yes` to enable reporting when the operational limits are exceeded `No` (default) | `Yes`

Select `Yes` to enable reporting when the operational
limits are exceeded. The associated parameters in the
**Operating Limits** section become visible to let
you select the reporting method and specify the operating limits in
terms of power and maximum working voltage. Parameters that specify
operating limits in terms of temperature are visible only for blocks
with an exposed thermal port (see Model Thermal Effects). The default value is
`No`.

### **Reporting when operating limits exceeded** — Select the reporting method `Warn` (default) | `Error`

Select what happens when an operating limit is exceeded:

- `Warn` — The block
  issues a warning.
- `Error` — Simulation
  stops with an error.

#### Dependencies

To enable this parameter, set **Enable operating limits** to
`Yes`.

### **Maximum working voltage** — Maximum voltage allowed for normal block operation `100` `V` (default)

Maximum voltage magnitude allowed for normal block operation.

#### Dependencies

To enable this parameter, set **Enable operating limits** to
`Yes`.

### **Power rating** — Maximum power allowed for normal block operation `1` `W` (default)

Maximum power allowed for normal block operation.

If you expose the thermal port of the block, this parameter
becomes temperature dependent. The value you specify for the **Power
rating** parameter applies up to the temperature specified
by the **Temperature below which full power rating is available** parameter
value. Then the power rating decreases linearly with temperature,
until it becomes 0 at temperature specified by the **Temperature
above which power rating is reduced to zero** parameter value.

#### Dependencies

To enable this parameter, set **Enable operating limits** to
`Yes`.

### **Temperature below which full power rating is available** — Maximum temperature where full power rating still applies `70` `degC` (default)

Maximum temperature where full power rating, specified by the **Power
rating** parameter value, still applies.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### **Temperature above which power rating is reduced to zero** — Temperature where power rating becomes 0 `155` `degC` (default)

Temperature where power rating becomes 0. Above this temperature,
the simulation always issues an assertion regardless of dissipated
power. This parameter value must be higher than **Temperature
below which full power rating is available**.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### **Operating temperature range, [Tmin Tmax]** — Minimum and maximum temperature values allowed for normal block operation `[-50 150]` `degC` (default)

A row vector of length 2 specifying minimum and maximum temperature
values allowed for normal block operation. The first element is the
lowest allowable operating temperature, and the second element is
the largest allowable operating temperature.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### Noise

### **Noise mode** — Select whether to model thermal noise current `Disabled` (default) | `Enabled`

Select whether to model thermal noise current:

- `Disabled` — No noise is
  produced by the resistor.
- `Enabled` — Resistor generates
  thermal noise current, and the associated parameters become
  visible in the **Noise** section.

### **Sample time** — Rate at which the noise source is sampled `1e-3` `s` (default)

Rate at which the noise source is sampled. Choose it to reflect the frequencies of interest in
your model. Making the sample time too small will unnecessarily slow
down your simulation.

#### Dependencies

To enable this parameter, set **Noise mode** to
`Enabled`.

### **Repeatability** — Select the noise control option `Not repeatable` (default) | `Repeatable` | `Specify seed`

Select the noise control option:

- `Not repeatable` —
  The random sequence used for noise generation is not repeatable.
- `Repeatable` — The
  random sequence used for noise generation is repeatable, with a system-generated
  seed.
- `Specify seed` — The
  random sequence used for noise generation is repeatable, and you control
  the seed by using the **Seed** parameter.

#### Dependencies

To enable this parameter, set **Noise mode** to
`Enabled`.

### **Auto-generated seed used for repeatable option** — Auto-generated random number seed random real number

Random number seed stored inside the block to make the random
sequence repeatable. The parameter value is automatically generated
using the MATLAB random number generator command. You can modify
this parameter value, but it gets overwritten by a new random value
if you copy the block to another block in the model. Therefore, if
you want to control the seed of the random sequence, use the `Specify
seed` option for the **Repeatability** parameter
and specify the desired seed value using the **Seed** parameter.

#### Dependencies

To enable this parameter, set **Repeatability** to
`Repeatable`.

### **Seed** — Random number seed `0` (default)

Seed used by the noise random number generator.

#### Dependencies

To enable this parameter, set **Repeatability** to `Specify
seed`.

### **Device simulation temperature** — Temperature of resistor at the start of the simulation `25` `degC` (default)

Temperature of the resistor at the start of the simulation.

#### Dependencies

To enable this parameter, set **Noise mode** to
`Enabled`.

For blocks with an exposed thermal port, this parameter is disabled.
Instead, use the **Variables** tab to set the initial
temperature target. For more information, see Variables.

### Thermal

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Resistance temperature coefficient** — Specifies how the resistance value changes with temperature `0.00393` `1/K` (default)

Coefficient α in the equation that describes resistance as a function
of temperature, *R*T =
*R*
(1+*α*(*T*–*T*0)). The default value is for copper.

### **Measurement temperature** — Temperature corresponding to nominal resistance `25` `degC` (default)

Temperature *T*0, for which
the nominal resistance *R* is specified.

### **Thermal mass** — Thermal mass associated with port H `100` `J/K` (default)

Thermal mass associated with the thermal port H. It represents the
energy required to raise the temperature of the thermal port by one
degree.

### Faults

### **Resistance fault** — Option to add resistance fault `Add fault` (default)

Option to add a resistance fault in the Resistor block.

To add a fault, click the **Add fault**
hyperlink.

### **Faulted resistance** — Resistance when block is in faulted state `inf` `Ohm` (default) | positive scalar

Resistance between the + and – ports when the block is in the faulted
state.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Resistance fault**
parameter.

### **Trigger type** — Trigger type `Always on` (default) | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

Trigger type, specified as one of these options:

- `Always On` — The fault injects at the start of the
  simulation.
- `Timed` — The fault injects when the simulation time
  reaches the value you specify for the **Trigger fault at time**
  parameter.
- `Behavioral` — The fault injects as a result of fault
  parameter values during simulation. Setting **Trigger type** to
  `Behavioral` enables block parameters that define
  the failure conditions.
- `Additional triggers` — The fault injects as a result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. To model
    irreversible faults, select the **Trigger stays on once
    activated** parameter in the Property Inspector. The block
    enters the faulted state when the trigger condition becomes true for the
    first time and remains in the faulted state for the rest of the
    simulation. To model reversible faults, clear the **Trigger
    stays on once activated** parameter. The block enters the
    faulted state when the trigger condition is true and enters the
    unfaulted state when the trigger condition is false. To learn more, see
    Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Resistance fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Resistance fault** parameter
and set **Trigger type** to
`Timed`.

### **Maximum permissible current** — Current threshold for fault transition `1` `A` (default) | positive scalar

Current threshold for a fault transition. The block enters the faulted
state if the current continuously exceeds this value for a period longer
than the value of the **Time to fail when exceeding maximum
permissible current** parameter.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Resistance fault** parameter
and set **Trigger type** to
`Behavioral`.

### **Time to fail when exceeding maximum permissible current** — Maximum length of time the current exceeds the threshold `1` `s` (default) | nonnegative scalar

Amount of time that the current must continuously exceed the maximum permissible current
before a fault triggers.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Resistance fault** parameter
and set **Trigger type** to
`Behavioral`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Resistance fault** parameter
and set **Trigger type** to
`Additional triggers`.

## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

### R2025a: Model Transient Conditional Faults

You can now model reversible conditional faults in the Resistor block by clearing the
**Trigger stays on once activated** parameter. The block enters the
faulted state when the trigger condition is true and enters the unfaulted state when the
trigger condition is false.

Before R2025a, the block enters the faulted state when the trigger condition becomes true
for the first time and remains in the faulted state for the rest of the simulation.

If you create a model before R2025a and enable a conditional fault in the Resistor
block, the block now selects the **Trigger stays on once activated**
parameter by default for backward compatibility.

### R2023a: Implement temporal or behavioral triggers for faults using a single parameter

The **Enable temporal trigger** and **Enable behavioral trigger** parameters have been removed and are replaced with the **Fault
trigger** parameter. You can set the **Fault trigger**
parameter to `Temporal` or `Behavioral`.
You can enable only one trigger.

If you created a model in an earlier release and enabled both temporal and behavioral
triggers, now only the temporal trigger is enabled. Therefore, the simulation results are
different if the behavioral trigger causes the fault in your model.

If you want to trigger a fault at a specific time, set the **Fault trigger**
parameter to `Temporal`. If you want to determine whether a system
fails and, if so, when it fails, set the **Fault Trigger** parameter to
`Behavioral`.

## Description

Resistor including optional tolerance, operational limits, fault behavior, and noise

The Resistor block represents a linear resistor, while letting
you model the following effects:

- Tolerances
- Operating Limits
- Faults
- Thermal Noise
- Model Thermal Effects

You can turn these modeling options on and off independently
of each other. When all the additional options are turned off, the
component behavior is identical to the Simscape™ Foundation library Resistor block.

In its simplest form, the Resistor block models
a linear resistor, described with the following equation:

i=v/R

where:

- *i* is current.
- *v* is voltage.
- *R* is resistance.

If you set the **Noise mode** parameter to `Enabled`,
then the defining equations are augmented by a discrete variable *i*N to
represent thermal noise, as described in Thermal Noise.

### Tolerances

You can apply tolerances to the nominal value you provide for
the **Resistance** parameter. Datasheets typically
provide a tolerance percentage for a given resistor type. The table
shows how the block applies tolerances and calculates resistance based
on the selected **Tolerance application** option.

| Option | Resistance Value |
| --- | --- |
| `None — use nominal value` | *R* |
| `Random tolerance` | Uniform distribution: *R* · (1 – *tol* + 2· *tol*· `rand`)  Gaussian distribution: *R* · (1 + *tol* · `randn` / *nSigma*) |
| `Apply maximum tolerance value` | *R* · (1 + *tol* ) |
| `Apply minimum tolerance value` | *R* · (1 – *tol* ) |

In the table,

- *R* is the **Resistance** parameter
  value, nominal resistance.
- *tol* is fractional tolerance, calculated from the
  percent-based **Tolerance (%)** parameter.
- *nSigma* is the value you provide
  for the **Number of standard deviations for quoted tolerance** parameter.
- `rand` and `randn` are standard MATLAB® functions
  for generating uniform and normal distribution random numbers.

**Note**

If you choose the `Random tolerance` option and you
are in "Fast Restart" mode, the random tolerance value is updated on every
simulation if at least one between the fractional tolerance,
*tol*, or the **Number of standard deviations for
quoted tolerance**, *nSigma*, is set to Run-time
and is defined with a variable (even if you do not modify that variable).

### Operating Limits

You can specify operating limits in terms of power and maximum working voltage. If you set the
**Modeling option** parameter to `Show thermal
port` (see Model Thermal Effects), you can also specify operating
limits in terms of temperature.

When an operating limit is exceeded, the block can either generate
a warning or stop the simulation with an error. For more information,
see the Operating Limits parameters
section.

### Faults

To model a fault in the Resistor block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

When the resistor fails, its resistance changes to the value you specify for the
**Faulted resistance** parameter.

**Fault Triggers**

You specify how and when faults occur by using the **Trigger
type** parameter.

If you set the **Trigger type** to
`Behavioral`, the Resistor block triggers fault
events when the current continuously exceeds the value of the **Maximum
permissible current** parameter for a duration longer than the
value of the **Time to fail when exceeding maximum permissible
current** parameter.

If you set the **Trigger
type** to `Conditional`, you can choose whether faults
in the Resistor block are reversible *(since R2025a)*. To model irreversible faults, click
**Open fault properties** to open the Property Inspector and select the
**Trigger stays on once activated** parameter. The block enters the faulted
state when the trigger condition becomes true for the first time and remains in the faulted
state for the rest of the simulation. To model reversible faults, clear the **Trigger
stays on once activated** parameter. The block enters the faulted state when the
trigger condition is true and enters the unfaulted state when the trigger condition is
false.

For more information about adding faults to blocks and
specifying fault triggers, see Introduction to Simscape Faults.

### Thermal Noise

The Resistor block can generate thermal noise current. If you
set the **Noise mode** parameter to `Enabled`,
then the defining equations are augmented by a discrete variable *i*N to
represent thermal noise:

i=v/R+iN

If the sampling time is *h*, then the thermal
noise is given by:

iN=2kT/RN(0,1)h

where:

- *k* is the Boltzmann constant, 1.3806504e-23
  J/K.
- *T* is the temperature.
- *R* is the resistance.
- *N* is a Gaussian random number with
  zero mean and standard deviation of one.
- *2kT/R* is the double-sided thermal
  noise power distribution (the single-sided equivalent is *4kT/R*).

The block generates Gaussian noise by using the PS Random Number source in
the Simscape Foundation library. You can control the random number seed by setting
the **Repeatability** parameter:

- `Not repeatable` —
  Every time you simulate your model, the block resets the random seed
  using the MATLAB random number generator:

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — The
  block automatically generates a seed value and stores it inside the
  block, to always start the simulation with the same random number.
  This auto-generated seed value is set when you add a Resistor block
  from the block library to the model. When you make a new copy of the
  Resistor block from an existing one in a model, a new seed value is
  generated. The block sets the value using the MATLAB random number
  generator command shown above.
- `Specify seed` — If
  you select this option, the additional **Seed** parameter
  lets you directly specify the random number seed value.

### Model Thermal Effects

You can expose thermal ports to specify how the resistance value changes with temperature and to set the thermal mass. To expose the thermal ports, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain thermal ports.
- `Show thermal port` — The block contains one thermal conserving port.

Use the **Variables** tab to set the initial temperature target.

With the thermal port exposed, the generated noise uses the
temperature at the thermal port when determining the instantaneous
noise value. Exposing the thermal port also extends the options on
the **Operating Limits** tab as follows:

- The **Power rating** parameter becomes
  temperature dependent. You define a temperature up to which the full
  power rating is available, plus a higher temperature for which the
  power rating is reduced to zero. It is assumed that the power rating
  decreases linearly with temperature between these two values.
- An additional parameter, **Operating temperature
  range, [Tmin Tmax]**, lets you define the valid temperature
  range for block operation.

### Plotting and Display Option

If you expose the thermal port, you can perform plotting and display actions using
the **Electrical** menu on the block context menu.

Right-click the block and, from the **Electrical** menu, select **Basic characteristics** to plot
the resistance, measured in SI units, in a MATLAB figure window using the current resistor parameters.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

This section appears only for the blocks with exposed thermal
port. The **Temperature** variable lets you specify
a high-priority target for the temperature at the start of simulation.

### Assumptions and Limitations

Simulating with noise enabled slows down simulation. Choose
the sample time (*h*) so that noise is generated
only at frequencies of interest, and not higher.
