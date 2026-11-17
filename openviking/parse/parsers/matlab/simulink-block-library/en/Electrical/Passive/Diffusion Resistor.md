---
type: simulink-block
title: 'Diffusion Resistor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'diffusionresistor'
documentation_source_path: 'ref/diffusionresistor.html'
language: en
---

# Diffusion Resistor

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
- name: H
  summary: Resistor thermal mass thermal
  direction: conserving
```

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
```yaml
parameters:
- name: Modeling option
  summary: Whether to enable thermal port No thermal port (default) | Show thermal port
  group: ''
- name: Resistance
  summary: Nominal zero-bias resistance 1 Ohm (default)
  group: Main
- name: Tolerance (%)
  summary: Resistor tolerance, in percent 5 (default)
  group: Main
- name: Tolerance application
  summary: Select how to apply tolerance during simulation None — use nominal value (default) | Random tolerance | Apply maximum
    tolerance value | Apply minimum tolerance value
  group: Main
- name: Tolerance distribution
  summary: Select the distribution type Uniform (default) | Gaussian
  group: Main
- name: Number of standard deviations for quoted tolerance
  summary: Used for calculating the Gaussian random number 4 (default)
  group: Main
- name: Parameterization
  summary: Select parameterization method Simplified (default) | Advanced
  group: Main
- name: Critical voltage
  summary: Critical voltage for saturation 4 V (default)
  group: Main
- name: Corner voltage
  summary: Voltage at which the resistance increase starts to occur 2 V (default)
  group: Main
- name: Quadratic voltage coefficient
  summary: Coefficient *p*2 0.25 (default)
  group: Main
- name: Inverse voltage for quadratic voltage activation
  summary: Coefficient *θ*2 0.25 1/V (default)
  group: Main
- name: Linear voltage coefficient
  summary: Coefficient *p*3 0.25 (default)
  group: Main
- name: Inverse voltage for linear voltage activation
  summary: Coefficient *θ*3 0.25 1/V (default)
  group: Main
- name: Enable operating limits
  summary: Select Yes to enable reporting when the operational limits are exceeded No (default) | Yes
  group: Operating Limits
- name: Reporting when operating limits exceeded
  summary: Select the reporting method Warn (default) | Error
  group: Operating Limits
- name: Maximum working voltage
  summary: Maximum voltage allowed for normal block operation 100 V (default)
  group: Operating Limits
- name: Power rating
  summary: Maximum power allowed for normal block operation 1 W (default)
  group: Operating Limits
- name: Temperature below which full power rating is available
  summary: Maximum temperature where full power rating still applies 70 degC (default)
  group: Operating Limits
- name: Temperature above which power rating is reduced to zero
  summary: Temperature where power rating becomes 0 155 degC (default)
  group: Operating Limits
- name: Operating temperature range, [Tmin Tmax]
  summary: Minimum and maximum temperature values allowed for normal block operation [-50 150] degC (default)
  group: Operating Limits
- name: Resistance fault
  summary: Option to add resistance fault Add fault (default)
  group: Faults
- name: Faulted zero-voltage resistance
  summary: Resistance when block is in faulted state inf Ohm (default) | positive scalar
  group: Faults
- name: Trigger fault at time
  summary: Time before entering faulted state 0 s (default) | nonnegative scalar
  group: Faults
- name: Maximum permissible current
  summary: Current threshold to fault transition 1 A (default) | positive scalar
  group: Faults
- name: Time to fail when exceeding maximum permissible current
  summary: Maximum length of time the current exceeds the threshold 1 s (default) | nonnegative scalar
  group: Faults
- name: Noise mode
  summary: Select whether to model thermal noise current Disabled (default) | Enabled
  group: Noise
- name: Sample time
  summary: Rate at which the noise source is sampled 1e-3 s (default)
  group: Noise
- name: Repeatability
  summary: Select the noise control option Not repeatable (default) | Repeatable | Specify seed
  group: Noise
- name: Auto-generated seed used for repeatable option
  summary: Auto-generated random number seed random real number
  group: Noise
- name: Seed
  summary: Random number seed 0 (default)
  group: Noise
- name: Device simulation temperature
  summary: Temperature of resistor at the start of the simulation 25 degC (default)
  group: Noise
- name: Resistance linear temperature coefficient
  summary: Specifies how the resistance value changes with temperature 0 1/K (default)
  group: Thermal
- name: Resistance quadratic temperature coefficient
  summary: Specifies how the resistance value changes with temperature 0 1/K^2 (default)
  group: Thermal
- name: Measurement temperature
  summary: Temperature corresponding to nominal resistance 25 degC (default)
  group: Thermal
- name: Thermal mass
  summary: Thermal mass associated with port H 100 J/K (default)
  group: Thermal
```

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and specify how the
resistance value changes with temperature and to set the thermal
mass.

### Main

### **Resistance** — Nominal zero-bias resistance `1` `Ohm` (default)

Zero-bias resistance, used as the nominal resistance value. Resistance value must be greater
than zero. If you set **Modeling option** to
`Show thermal port`, this is the zero-bias
resistance at a temperature equal to the **Measurement
temperature** parameter in the Thermal section.

### **Tolerance (%)** — Resistor tolerance, in percent `5` (default)

Resistor tolerance as defined on the manufacturer datasheet.

### **Tolerance application** — Select how to apply tolerance during simulation `None — use nominal value` (default) | `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

Select how to apply tolerance during simulation:

- `None — use nominal value`
  — The block does not apply tolerance, uses the nominal
  resistance value.
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

### **Parameterization** — Select parameterization method `Simplified` (default) | `Advanced`

Select how to apply tolerance during simulation:

- `Simplified` — Assume that the
  quadratic and linear coefficients are the same, and define block
  behavior using the **Critical voltage** and
  **Corner voltage** parameters.
- `Advanced` — Explicitly
  specify values for the quadratic and linear voltage coefficients
  and for the inverse voltages for quadratic and linear voltage
  activation.

### **Critical voltage** — Critical voltage for saturation `4` `V` (default)

Critical voltage for the saturation mechanism. You can determine this
parameter value by taking the reciprocal of the slope of the increase of
*R*/*R*0
with voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Simplified`.

### **Corner voltage** — Voltage at which the resistance increase starts to occur `2` `V` (default)

Corner voltage, at which the resistance increase starts to occur. The
**Corner voltage** must be less than the
**Critical voltage**.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Simplified`.

### **Quadratic voltage coefficient** — Coefficient *p*2 `0.25` (default)

Coefficient *p*2 from the
defining equation.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Advanced`.

### **Inverse voltage for quadratic voltage activation** — Coefficient *θ*2 `0.25` `1/V` (default)

Coefficient *θ*2 from the
defining equation.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Advanced`.

### **Linear voltage coefficient** — Coefficient *p*3 `0.25` (default)

Coefficient *p*3 from the
defining equation.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Advanced`.

### **Inverse voltage for linear voltage activation** — Coefficient *θ*3 `0.25` `1/V` (default)

Coefficient *θ*3 from the
defining equation.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Advanced`.

### Operating Limits

### **Enable operating limits** — Select `Yes` to enable reporting when the operational limits are exceeded `No` (default) | `Yes`

Select `Yes` to enable reporting when the operational
limits are exceeded. The associated parameters in the
**Operating Limits** section become visible to let
you select the reporting method and specify the operating limits in
terms of power and maximum working voltage. Parameters that specify
operating limits in terms of temperature are visible only for blocks
with exposed thermal port (see Model Thermal Effects). The default value is
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

If you expose the thermal port of the block, this parameter becomes
temperature dependent. The value you specify for the **Power
rating** parameter applies up to the temperature specified
by the **Temperature below which full power rating is
available** parameter value. Then the power rating
decreases linearly with temperature, until it becomes 0 at temperature
specified by the **Temperature above which power rating is
reduced to zero** parameter value.

#### Dependencies

To enable this parameter, set **Enable operating
limits** to `Yes`.

### **Temperature below which full power rating is available** — Maximum temperature where full power rating still applies `70` `degC` (default)

Maximum temperature where full power rating, specified by the
**Power rating** parameter value, still
applies.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### **Temperature above which power rating is reduced to zero** — Temperature where power rating becomes 0 `155` `degC` (default)

Temperature where power rating becomes 0. Above this temperature, the
simulation always issues an assertion regardless of dissipated power.
This parameter value must be higher than **Temperature below
which full power rating is available**.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### **Operating temperature range, [Tmin Tmax]** — Minimum and maximum temperature values allowed for normal block operation `[-50 150]` `degC` (default)

A row vector of length 2 specifying minimum and maximum temperature
values allowed for normal block operation. The first element is the
lowest allowable operating temperature, and the second element is the
largest allowable operating temperature.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### Faults

### **Resistance fault** — Option to add resistance fault `Add fault` (default)

Option to add a resistance fault in the Diffusion Resistor block.

To add a fault, click the **Add fault**
hyperlink.

### **Faulted zero-voltage resistance** — Resistance when block is in faulted state `inf` `Ohm` (default) | positive scalar

Zero-voltage resistance between the + and – ports when the block is in
the faulted state.

#### Dependencies

To enable this parameter, add a fault to the Diffusion Resistor block by
clicking the **Add fault** hyperlink in the
**Resistance fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.

### **Maximum permissible current** — Current threshold to fault transition `1` `A` (default) | positive scalar

Current threshold to a fault transition. If the current exceeds this
value for longer than the **Time to fail when exceeding maximum
permissible current** parameter value, then the block
enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Time to fail when exceeding maximum permissible current** — Maximum length of time the current exceeds the threshold `1` `s` (default) | nonnegative scalar

Maximum length of time that the current can exceed the maximum
permissible value without triggering the fault.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### Noise

### **Noise mode** — Select whether to model thermal noise current `Disabled` (default) | `Enabled`

Select whether to model thermal noise current:

- `Disabled` — No noise is
  produced by the resistor.
- `Enabled` — Resistor generates
  thermal noise current, and the associated parameters become
  visible in the **Noise** section.

### **Sample time** — Rate at which the noise source is sampled `1e-3` `s` (default)

Defines the rate at which the noise source is sampled. Choose
it to reflect the frequencies of interest in your model. Making the
sample time too small will unnecessarily slow down your simulation.

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

The temperature of the resistor at the start of the simulation.

#### Dependencies

To enable this parameter, set **Noise mode** to
`Enabled`.

For blocks with an exposed thermal port, this parameter is disabled.
Instead, use the **Variables** tab to set the initial
temperature target. For more information, see Variables.

### Thermal

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Resistance linear temperature coefficient** — Specifies how the resistance value changes with temperature `0` `1/K` (default)

The coefficient TC1eff in the equation that describes resistance as a
function of temperature. See Model Thermal Effects for details.

### **Resistance quadratic temperature coefficient** — Specifies how the resistance value changes with temperature `0` `1/K^2` (default)

The coefficient TC2eff in the equation that describes resistance as a
function of temperature. See Model Thermal Effects for details.

### **Measurement temperature** — Temperature corresponding to nominal resistance `25` `degC` (default)

The temperature *T*0,
for which the nominal resistance *R* is specified.

### **Thermal mass** — Thermal mass associated with port H `100` `J/K` (default)

Thermal mass associated with the thermal port H. It represents
the energy required to raise the temperature of the thermal port by
one degree.
## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

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

Resistor model with velocity saturation and optional tolerance, operational limits, fault behavior, and noise

The Diffusion Resistor block represents a resistor with
velocity saturation, while letting you model the following effects:

- Tolerances
- Operating Limits
- Faults
- Thermal Noise
- Model Thermal Effects

You can turn these modeling options on and off independently
of each other.

In its simplest form, the resistance of the Diffusion Resistor
block is:

R=R0(1−p2−p3+p21+(θ2vpn)2+p31+|θ3vpn|33)

where:

- *R0* is zero-bias resistance.
- *p2* and
  *p*3 are the quadratic and linear
  voltage coefficients, respectively.
- *θ2* and
  *θ*3 are inverse voltages for
  quadratic and linear voltage activation, respectively.
- *vpn* is applied voltage across the
  resistor.

At low bias,

R≈R0(1+p2θ22vpn22)

and therefore *p2* and
*θ2* determine the low-bias quadratic
behavior of the resistor.

At high bias,

R≈R0(1−p2−p3+|vpn|(p2θ2+p3θ3))

and therefore *p3* and
*θ3* impact only the high-bias linear
behavior of the resistor.

You can use the voltage-dependence of the resistance to model
velocity saturation in a diffused resistor. For sufficiently high
voltage,

isat=1R0(p2θ2+p3θ3)

where *isat* is saturation current.

### Simplified Parameterization

The simplified parameterization model assumes that the quadratic and linear
coefficients are the same. This is one of the recommended assumptions for the r2\_cmc
model provided by the Compact Model Coalition, as a reasonable initial guess when
performing parameter extraction. With this assumption, it is possible to define two
new parameters, **Critical voltage** and **Corner
voltage**, which provide a simpler means for parameterizing
models:

p2=p3=vco2vcritθ2=θ3=12vco

where:

- *vcrit* is critical
  voltage.
- *vco* is corner voltage.

At high voltage,

dRdvpn≈R0vcrit

and therefore, critical voltage is the reciprocal of the slope of the increase of
*R*/*R0* with voltage.

With this parameterization, the saturation current is

isat=vcritR0

### Tolerances

You can apply tolerances to the nominal value you provide for
the **Resistance** parameter. Datasheets typically
provide a tolerance percentage for a given resistor type. The table
shows how the block applies tolerances and calculates resistance based
on the selected **Tolerance application** option.

| Option | Resistance Value |
| --- | --- |
| `None — use nominal value` | *R*0 |
| `Random tolerance` | Uniform distribution: *R0* · (1 – *tol* + 2· *tol*· `rand`)  Gaussian distribution: *R0* · (1 + *tol* · `randn` / *nSigma*) |
| `Apply maximum tolerance value` | *R0* · (1 + *tol* ) |
| `Apply minimum tolerance value` | *R0* · (1 – *tol* ) |

In the table,

- *R*0 is the **Resistance** parameter
  value, nominal zero-bias resistance.
- *tol* is fractional tolerance, **Tolerance
  (%)** /100.
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

To model a fault in the Diffusion Resistor block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Diffusion Resistor block allows you to model an electrical
fault as an instantaneous change in resistance. The block can trigger fault
events:

- At a specific time.
- When the current exceeds the maximum permissible value for longer than a
  specific time interval.

If you want to trigger a fault at a specific time, in the
**Fault Inspector** window, set **Trigger type** to
`Timed`. If you want to determine whether a system fails and, if
so, when it fails, in the **Fault Inspector** window, set **Trigger
type** to `Behavioral`.

When the resistor fails, its resistance is changed to the value you specify for the
**Faulted zero-voltage resistance** parameter.

### Thermal Noise

The Diffusion Resistor block can generate thermal noise
current. If you set the **Noise mode** parameter to
`Enabled`, then the block includes a noise current
source connected in parallel to the diffusion resistor.

If the sampling time is *h*, then the thermal
noise is given by:

iN=2kT/RN(0,1)h

where:

- *k* is the Boltzmann constant, 1.3806504e-23
  J/K.
- *T* is temperature.
- *R* is resistance.
- *N* is a Gaussian random number with
  zero mean and standard deviation of one.
- *2kT/R* is the double-sided thermal
  noise power distribution (the single-sided equivalent is *4kT/R*).

The block generates Gaussian noise by using the PS Random Number source in
the Simscape™ Foundation library. You can control the random number seed by setting
the **Repeatability** parameter:

- `Not repeatable` —
  Every time you simulate your model, the block resets the random seed
  using the MATLAB random number generator:

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — The block automatically generates a seed value
  and stores it inside the block, to always start the simulation with the same
  random number. This auto-generated seed value is set when you add a
  Diffusion Resistor block from the block
  library to the model. When you make a new copy of the
  Diffusion Resistor block from an existing
  one in a model, a new seed value is generated. The block sets the value
  using the MATLAB random number generator command shown above.
- `Specify seed` — If
  you select this option, the additional **Seed** parameter
  lets you directly specify the random number seed value.

### Model Thermal Effects

You can expose thermal ports to specify how the resistance value changes with temperature and to set the thermal mass. To expose the thermal ports, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain thermal ports.
- `Show thermal port` — The block contains one thermal conserving port.

Use the **Variables** settings to set the initial temperature target.

If you set the **Modeling option** parameter to `Show thermal
port`, the defining equation for the resistance is augmented with
additional temperature scaling:

R=R0(1+TC1effΔT+TC2eff(ΔT)2)(1−p2−p3+p21+(θ2vpn)2+p31+|θ3vpn|33)

where TC1eff and TC2eff are
the linear and quadratic temperature scaling coefficients, respectively.

ΔT=Tsim−Tmeas

where:

- *T*sim is
  simulation temperature.
- *T*meas is
  measurement temperature.

With the thermal port exposed, the generated noise uses the temperature at the
thermal port when determining the instantaneous noise value. Exposing the thermal
port also extends the options on the **Operating Limits** tab as
follows:

- The **Power rating** parameter becomes temperature
  dependent. You define a temperature up to which the full power rating is
  available, plus a higher temperature for which the power rating is reduced
  to zero. It is assumed that the power rating decreases linearly with
  temperature between these two values.
- An additional parameter, **Operating temperature range, [Tmin
  Tmax]**, lets you define the valid temperature range for block
  operation.

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

### Basic Assumptions and Limitations

Simulating with noise enabled slows down simulation. Choose
the sample time (*h*) so that noise is generated
only at frequencies of interest, and not higher.
