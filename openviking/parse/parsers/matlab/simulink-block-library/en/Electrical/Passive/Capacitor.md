---
type: simulink-block
title: 'Capacitor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'capacitor'
documentation_source_path: 'ref/capacitor.html'
language: en
---

# Capacitor

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
  summary: Capacitor thermal mass thermal
  direction: conserving
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the capacitor positive
voltage.

### **-** — Negative terminal electrical

Electrical conserving port associated with the capacitor negative
voltage.

### **H** — Capacitor thermal mass thermal

*Since R2024a*

Thermal conserving port associated with the capacitor thermal
mass.
## Parameters
```yaml
parameters:
- name: Capacitance model
  summary: Capacitor type Constant (default) | Lookup table | Dielectric relaxation (Debye)
  group: Main
- name: Capacitance
  summary: Nominal capacitance 1e-6 F (default)
  group: Main
- name: Capacitance values
  summary: Vector of capacitance values [1e-05, 1e-06] F (default) | positive vector
  group: Main
- name: Corresponding voltage values
  summary: Input vector of voltage values [0, 10] V (default)
  group: Main
- name: Symmetric C-V table
  summary: Table data Yes - use voltage magnitude when computing C (default) | No - use C-V data as-is
  group: Main
- name: Frequencies for specifying dissipation factors [f1 f2]
  summary: Frequencies for dissipation factors calculation [1, 10] kHz (default)
  group: Main
- name: Dissipation factors (%) at f1 and f2 [DF1 DF2]
  summary: Dissipation factors at f1 and f2 [.8, 1.2] (default)
  group: Main
- name: Capacitance tolerance (%)
  summary: Capacitor tolerance 5 (default)
  group: Main
- name: Tolerance application
  summary: Tolerance application None — use nominal value (default) | Random tolerance | Apply maximum tolerance value | Apply
    minimum tolerance value
  group: Main
- name: Tolerance distribution
  summary: Tolerance distribution type Uniform (default) | Gaussian
  group: Main
- name: Number of standard deviations for quoted tolerance
  summary: Number of standard deviations for quoted tolerance 4 (default)
  group: Main
- name: Series resistance
  summary: Series resistance 1e-6 Ohm (default)
  group: Main
- name: Parallel conductance
  summary: Parallel leakage path 0 1/Ohm (default)
  group: Main
- name: Averaging period for power logging
  summary: Averaging period for power logging 0 s (default)
  group: Main
- name: Enable operating limits
  summary: Enable operating limits No (default) | Yes
  group: Operating Limits
- name: Reporting if operating limits exceeded
  summary: Report behavior Warn (default) | Error
  group: Operating Limits
- name: Working voltage range
  summary: Working voltage range [-25, 25] V (default)
  group: Operating Limits
- name: Power rating
  summary: Maximum instantaneous power dissipation 1 W (default)
  group: Operating Limits
- name: Temperature
  summary: Maximum permissible temperature 85 degC (default)
  group: Operating Limits
- name: Model thermal port
  summary: Option to model thermal port off (default) | on
  group: Thermal
- name: Thermal mass
  summary: Thermal mass associated with thermal port 1 J/K (default)
  group: Thermal
- name: Capacitor fault
  summary: Option to model fault in capacitor Add fault (default)
  group: Faults
- name: Faulted capacitance as % of unfaulted
  summary: Faulted capacitance as % of unfaulted 100 (default) | positive scalar
  group: Faults
- name: Faulted series resistance
  summary: Faulted series resistance 1e-3 Ohm (default) | finite positive scalar
  group: Faults
- name: Faulted parallel conductance
  summary: Faulted parallel conductance 0 1/Ohm (default) | finite nonnegative scalar
  group: Faults
- name: Fault transition time constant
  summary: Fault transition time constant 1e-3 s (default) | positive scalar
  group: Faults
- name: Trigger fault at time
  summary: Time before entering faulted state 0 s (default) | nonnegative scalar
  group: Faults
- name: Maximum permissible temperature
  summary: Maximum permissible temperature 85 degC (default) | nonnegative scalar
  group: Faults
- name: Time to fail when exceeding maximum temperature
  summary: Time to fail when exceeding maximum temperature 1 s (default) | nonnegative scalar
  group: Faults
- name: Permissible voltage range
  summary: Minimum and maximum permissible voltage [-100, 100] V (default) | vector of length 2
  group: Faults
- name: Time to fail when exceeding voltage range
  summary: Time to fail when exceeding voltage range 1 s (default) | nonnegative scalar
  group: Faults
```

### Main

### **Capacitance model** — Capacitor type `Constant` (default) | `Lookup table` | `Dielectric relaxation (Debye)`

Select the type of capacitor:

- `Constant` — Model a linear
  capacitor, with nominal capacitance defined by the
  **Capacitance** parameter value.
- `Lookup table` — Model a
  nonlinear capacitor, where the nominal capacitance value changes
  based on the value of applied terminal voltage.
- `Dielectric relaxation (Debye)`
  —Model a frequency-dependent capacitor with resistive and
  dielectric losses.

### **Capacitance** — Nominal capacitance `1e-6` `F` (default)

The nominal capacitance value for linear capacitor, or the
low-frequency capacitance in the Debye parameterization.

#### Dependencies

This parameter is visible only when you select
`Constant` or `Dielectric
relaxation (Debye)` for the **Capacitance
model** parameter.

### **Capacitance values** — Vector of capacitance values `[1e-05, 1e-06]` `F` (default) | positive vector

The vector of capacitance values, for table lookup based on the
corresponding voltage value. The vector length must be the same as the
voltage vector length.

#### Dependencies

This parameter is visible only when you select `Lookup
table` for the **Capacitance
model** parameter.

### **Corresponding voltage values** — Input vector of voltage values `[0, 10]` `V` (default)

The input vector of voltage values for table-based capacitance
calculation. The vector length must be greater than or equal to 2, and
the values must be strictly monotonic, either increasing or
decreasing.

#### Dependencies

This parameter is visible only when you select `Lookup
table` for the **Capacitance
model** parameter.

### **Symmetric C-V table** — Table data `Yes - use voltage magnitude when computing C` (default) | `No - use C-V data as-is`

Specify how to use the table data:

- `Yes - use voltage magnitude when computing
  C` — Use this option to ensure symmetry
  of the capacitance with regards to the applied terminal
  voltage.
- `No - use C-V data as-is` —
  Use this option to model polar capacitors. For example, with
  default parameter values for table-based capacitance, applied
  voltage of –10 V would produce nominal capacitance of 1e-6 F.
  However, if you select `No - use C-V data
  as-is` for the **Symmetric C-V
  table** parameter, the resulting capacitance value
  is 1e-5 F, because the block uses the nearest input value for
  extrapolation.

#### Dependencies

This parameter is visible only when you select `Lookup
table` for the **Capacitance
model** parameter.

### **Frequencies for specifying dissipation factors [f1 f2]** — Frequencies for dissipation factors calculation `[1, 10]` `kHz` (default)

Frequencies at which the dissipation factors **[DF1
DF2]** are calculated, in kHz.

#### Dependencies

This parameter is visible only when you select
`Dielectric relaxation (Debye)` for the
**Capacitance model** parameter.

### **Dissipation factors (%) at f1 and f2 [DF1 DF2]** — Dissipation factors at f1 and f2 `[.8, 1.2]` (default)

Ratio between the equivalent series resistance and the capacitive
reactance, or the tangent of the loss angle. Dissipation factors are a
common metric for capacitors.

#### Dependencies

This parameter is visible only when you select
`Dielectric relaxation (Debye)` for the
**Capacitance model** parameter.

### **Capacitance tolerance (%)** — Capacitor tolerance `5` (default)

The capacitor tolerance as defined on the manufacturer datasheet. For
table-based capacitors, this tolerance is applied to the entire table at
once.

### **Tolerance application** — Tolerance application `None — use nominal value` (default) | `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

Select how to apply tolerance during simulation:

- `None — use nominal value`
  — The block does not apply tolerance, uses the nominal
  capacitance value.
- `Random tolerance` — The block
  applies random offset to the capacitance value, within the
  tolerance value limit. You can choose Uniform or Gaussian
  distribution for calculating the random number by using the
  **Tolerance distribution**
  parameter.
- `Apply maximum tolerance value`
  — The capacitance is increased by the specified tolerance
  percent value.
- `Apply minimum tolerance value`
  — The capacitance is decreased by the specified tolerance
  percent value.

### **Tolerance distribution** — Tolerance distribution type `Uniform` (default) | `Gaussian`

Select the distribution type:

- `Uniform` — Uniform
  distribution.
- `Gaussian` — Gaussian
  distribution.

#### Dependencies

This parameter is visible only when you select `Random
tolerance` for the **Tolerance
application** parameter.

### **Number of standard deviations for quoted tolerance** — Number of standard deviations for quoted tolerance `4` (default)

Number of standard deviations for calculating the Gaussian random
number.

#### Dependencies

This parameter is visible only when you select
`Gaussian` for the **Tolerance
distribution** parameter.

### **Series resistance** — Series resistance `1e-6` `Ohm` (default)

Simulation of some circuits may require the presence of the small
series resistance. Equivalent series resistance (ESR) is sometimes
specified on manufacturer datasheets. If not, you can define this
resistance for a linear capacitor via the dissipation factor (DF), which
is also shown on many datasheets. The relationship is *`DF`* = 2π·
*`f`*·
*`C`*·
*`ESR`*, where *`f`* is signal
frequency. For a Debye capacitor, the **Dissipation
factors (%) at f1 and f2 [DF1 DF2]** are corrected for this
additional series resistance prior to computing 𝛼 and 𝜏.

### **Parallel conductance** — Parallel leakage path `0` `1/Ohm` (default)

Parallel leakage path associated with the capacitor. For capacitors
connected in series, the presence of a small parallel conductance can
help with convergence.

### **Averaging period for power logging** — Averaging period for power logging `0` `s` (default)

Averaging period for power logging, in s.

**Note**

If this parameter is set to `0`, the output is
the instantaneous power.

#### Dependencies

This parameter is visible only when you select
`Dielectric relaxation (Debye)` for the
**Capacitance model** parameter.

### Operating Limits

### **Enable operating limits** — Enable operating limits `No` (default) | `Yes`

Select `Yes` to enable reporting when the operational
limits are exceeded. The associated parameters become visible on the
**Operating Limits** tab to let you select the
reporting method and specify the operating limits in terms of power and
working voltage.

### **Reporting if operating limits exceeded** — Report behavior `Warn` (default) | `Error`

Select what happens when an operating limit is exceeded:

- `Warn` — The block issues a warning.
- `Error` — Simulation stops with an error.

### **Working voltage range** — Working voltage range `[-25, 25]` `V` (default)

Range of voltage values allowed for normal block operation, specified as a vector of size 2.

### **Power rating** — Maximum instantaneous power dissipation `1` `W` (default)

Maximum instantaneous power dissipation in the resistance and conductance elements associated with the capacitor.

### **Temperature** — Maximum permissible temperature `85` `degC` (default)

*Since R2024a*

Maximum permissible temperature. If the temperature of the capacitor
is greater than this value, the block throws a warning or an
error.

#### Dependencies

To enable this parameter, in the **Thermal**
section, select the **Model thermal port**
parameter.

### Thermal

### **Model thermal port** — Option to model thermal port `off` (default) | `on`

*Since R2024a*

Option to model a thermal port in the Capacitor block.

### **Thermal mass** — Thermal mass associated with thermal port `1` `J/K` (default)

*Since R2024a*

Thermal mass associated with the thermal port **H**. It
represents the energy required to raise the temperature of the thermal
port by one degree.

#### Dependencies

To enable this parameter, select the **Model thermal
port** parameter.

### Faults

### **Capacitor fault** — Option to model fault in capacitor `Add fault` (default)

Option to model a fault in the
Capacitor block.

To add a fault, click the **Add fault**
hyperlink.

### **Faulted capacitance as % of unfaulted** — Faulted capacitance as % of unfaulted `100` (default) | positive scalar

Relative change in the capacitance when the block is in the faulted
state, as compared to the unfaulted state. For table-based capacitances,
the relative change is applied to all elements of the vector. The
default value is `100`, which means that the faulted
capacitance is equal to the unfaulted capacitance.

#### Dependencies

To enable this parameter, add a fault to the Capacitor block by
clicking the **Add fault** hyperlink in the
**Capacitor fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted series resistance** — Faulted series resistance `1e-3` `Ohm` (default) | finite positive scalar

Equivalent series resistance of the capacitor when the block is in the
faulted state.

#### Dependencies

To enable this parameter, add a fault to the Capacitor block by
clicking the **Add fault** hyperlink in the
**Capacitor fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Faulted parallel conductance** — Faulted parallel conductance `0` `1/Ohm` (default) | finite nonnegative scalar

Parallel leakage conductance of the capacitor when the block is in the
faulted state.

#### Dependencies

To enable this parameter, add a fault to the Capacitor block by
clicking the **Add fault** hyperlink in the
**Capacitor fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Fault transition time constant** — Fault transition time constant `1e-3` `s` (default) | positive scalar

Time constant associated with the transition to the faulted state, as
described in Faults.

#### Dependencies

To enable this parameter, add a fault to the Capacitor block by
clicking the **Add fault** hyperlink in the
**Capacitor fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.

### **Maximum permissible temperature** — Maximum permissible temperature `85` `degC` (default) | nonnegative scalar

*Since R2024a*

Maximum permissible temperature. If the temperature value is outside
this value for longer than the **Time to fail when exceeding
maximum temperature** parameter value, then the block
starts entering the fault state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Time to fail when exceeding maximum temperature** — Time to fail when exceeding maximum temperature `1` `s` (default) | nonnegative scalar

*Since R2024a*

Maximum length of time that the temperature can be outside the
permissible temperature range without triggering the fault.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Permissible voltage range** — Minimum and maximum permissible voltage `[-100, 100]` `V` (default) | vector of length 2

Minimum and maximum permissible voltage. If the voltage value is
outside this range for longer than the **Time to fail when
exceeding voltage range** parameter value, then the block
starts entering the fault state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Time to fail when exceeding voltage range** — Time to fail when exceeding voltage range `1` `s` (default) | nonnegative scalar

Maximum length of time that the voltage can be outside the permissible
voltage range without triggering the fault.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.
## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2024a: Model thermal effects by exposing thermal port

The Capacitor block now supports a thermal port. To
model a thermal port, in the **Thermal** section, select the
**Model thermal port** parameter. To specify the value of the
thermal mass and the maximum permissible temperature of the capacitor, specify the
values of the new **Temperature** and **Thermal
mass** parameters in the **Operating Limits** and
**Thermal** sections, respectively.

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

Linear or nonlinear capacitor with optional tolerance, operational limits and fault behavior

The Capacitor block lets you model linear, nonlinear
(table-based), and frequency-dependent capacitors, including polar capacitors.
Optionally, you can also model the following effects:

- Tolerances
- Operating Limits
- Faults

You can turn these modeling options on and off independently of each other. When all
the additional options are turned off, the component behavior is identical to the
Simscape™ Foundation library Capacitor block.

In its simplest form, the Capacitor block models a
linear capacitor, described with the following equation:

I=CdVdt

where:

- *I* is the current.
- *C* is the capacitance.
- *V* is the voltage.
- *t* is the time.

To model a nonlinear or polar capacitor, set the **Capacitance model**parameter to `Lookup table` and provide a lookup
table of capacitance-voltage values:

- For polar capacitors, where this lookup table is asymmetric with respect to
  the applied terminal voltage, set the **Symmetric C-V table**parameter to `No - use C-V data
  as-is`.
- For other types of nonlinear capacitor, ensure symmetry of the capacitance
  with regards to the applied terminal voltage by setting the **Symmetric
  C-V table** parameter to `Yes - use voltage magnitude
  when computing C`.

To model a frequency-dependent capacitor with resistive and dielectric losses, set the
**Capacitance model** parameter to `Dielectric
relaxation
(Debye)`.
The Debye relaxation model considers a collection of noninteracting dipoles in the
frequency domain. The result is in terms of a complex permittivity. The real (𝜖′) and
imaginary (𝜖′′) parts of the complex permittivity are given by the equations:

ε'=ε∞+εs−ε∞1+ω2τ2

ε''=(εs−ε∞)ωτ1+ω2τ2,

where 𝜔 is the radial frequency, 𝜖∞ is the
real permittivity at very high frequency, 𝜖𝑠 is the real
permittivity at low frequency and 𝜏 is the relaxation time constant.

In the time-domain, the characteristic equation for a capacitor in the Debye model is

τi=−q+Cs(ατν˙+ν),

where 𝐶𝑠 is the low-frequency capacitance,
𝛼 = 𝜖∞/𝜖𝑠, 𝑞 is the charge, 𝑖 is the
current and 𝑣 is the voltage across the capacitor.

Most datasheets do not provide explicit values for the complex permittivity nor for
the relaxation time; however, often the dissipation factor is provided at two
frequencies. The parameters 𝛼 and 𝜏 may be derived from these values as described by
the equations:

τ=DF1DF2(ω22−ω12)+DF12DF22(ω22−ω12)2+4ω1ω2(DF2ω2−DF1ω1)(DF1ω2−DF2ω1)2ω1ω2(DF2ω2−DF1ω1)

α=ω1τ−DF1ω1τ(1+DF1ω1τ),

where 𝜔1 and 𝜔2 are
two different frequencies, and *DF1* and
*DF2* are the dissipation factors
calculated at said frequencies, respectively.

The argument of the square root must be positive for a valid parameterization in the
Debye model.

### Tolerances

You can apply tolerances to the nominal value you provide for the
**Capacitance** parameter. Datasheets typically provide a
tolerance percentage for a given capacitor type. The table shows how the block
applies tolerances and calculates capacitance based on the selected
**Tolerance application** option.

| Option | Capacitance Value |
| --- | --- |
| `None — use nominal value` | *C* |
| `Random tolerance` | Uniform distribution: *C* · (1 – *tol* + 2· *tol*· `rand`)  Gaussian distribution: *C* · (1 + *tol* · `randn` / *nSigma*) |
| `Apply maximum tolerance value` | *C* · (1 + *tol* ) |
| `Apply minimum tolerance value` | *C* · (1 – *tol* ) |

In the table,

- *C* is the **Capacitance** parameter
  value, nominal capacitance.
- *tol* is the fractional tolerance, **Capacitance
  tolerance (%)** /100.
- *nSigma* is the value you provide for the
  **Number of standard deviations for quoted tolerance**
  parameter.
- `rand` and `randn` are standard
  MATLAB® functions for generating uniform and normal distribution
  random numbers.

**Note**

If you choose the `Random tolerance` option and you
are in "Fast Restart" mode, the random tolerance value is updated on every
simulation if at least one between the fractional tolerance,
*tol*, or the **Number of standard deviations for
quoted tolerance**, *nSigma*, is set to Run-time
and is defined with a variable (even if you do not modify that variable).

### Operating Limits

You can specify operating limits in terms of maximum working voltage and the
maximum (instantaneous) power dissipation in the series resistance and in the
parallel conductance of the capacitor.

For polar capacitors, you can define the working voltage range in such a way that
the block provides a warning, or an error, if the polarity of the applied voltage
becomes incorrect.

When an operating limit is exceeded, the block can either generate a warning or
stop the simulation with an error. For more information, see Operating Limits.

### Model Thermal Effects

*Since R2024a*

You can expose the thermal port to observe the power loss and the change in
temperature of the capacitor and to set the thermal mass. To expose the thermal
port, in the **Thermal** section, select the **Model
thermal port** parameter.

Exposing the thermal port also enables a parameter,
**Temperature**, in the **Operating Limits**
section, that defines the maximum valid temperature for the block operation.

Use the **Variables** tab to set the initial temperature
target.

### Faults

To model a fault in the Capacitor block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

Instantaneous changes in capacitor parameters are unphysical. Therefore, when the
Capacitor block enters the faulted state, the
capacitance, resistance, and conductance transition to their faulted values over a
period of time, according to the following formula:

*`CurrentValue`* =
*`FaultedValue`* –
(*`FaultedValue`* –
*`UnfaultedValue`*) · `sech`(∆t
/ τ)

where:

- ∆t is the time since the onset of the fault condition.
- τ is the user-defined time constant associated with the fault
  transition.

The block can trigger the start of fault transition:

- At a specific time.
- When terminal voltage is outside the permissible voltage range for longer
  than a specific time interval.

If you want to trigger a fault at a specific time, in the
**Fault Inspector** window, set **Trigger type** to
`Timed`. If you want to determine whether a system fails and, if
so, when it fails, in the **Fault Inspector** window, set **Trigger
type** to `Behavioral`.

### Variables

Use the **Variables** section of the block interface to set
the priority and initial target values for the block variables prior to
simulation. For more information, see Set Priority and Initial Target for Block Variables.

The **Capacitor voltage** variable lets you specify a
high-priority target for the initial capacitor voltage at the start of simulation.

The **Temperature** variable lets you specify a high-priority target for the
temperature at the start of simulation. To enable this variable, in the
**Thermal** section, select the **Model thermal
port** parameter. *(since R2024a)*
