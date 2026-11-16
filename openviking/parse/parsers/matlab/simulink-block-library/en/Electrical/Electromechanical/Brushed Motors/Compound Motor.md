---
type: simulink-block
title: 'Compound Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Brushed Motors'
documentation_page: 'compoundmotor'
documentation_source_path: 'ref/compoundmotor.html'
language: en
---

# Compound Motor

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the compound motor positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the compound motor negative
terminal.

### **C** — Motor case mechanical

Mechanical rotational conserving port associated with the compound
motor case.

### **R** — Motor rotor mechanical

Mechanical rotational conserving port associated with the compound
motor rotor.

### **Hs** — Series field winding thermal port thermal

Thermal conserving port associated with the series field winding. For more information,
see Model Thermal Effects.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **Hp** — Shunt field winding thermal port thermal

Thermal conserving port associated with the shunt field winding.. For more information,
see Model Thermal Effects.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **Ha** — Armature thermal port thermal

Thermal conserving port associated with the armature. For more information, see Model Thermal Effects.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of losses that
convert power to heat.

### Configuration

### **Electrical circuit topology** — Topology of electrical circuit `Long-shunt` (default) | `Short-shunt`

Topology of the electrical circuit.

### **Shunt winding polarity** — Shunt winding polarity `Cumulative` (default) | `Differential`

Magnetic orientation of the shunt winding.

### Steady-State

### **Steady-state parameterization** — Block parameterization `By equivalent circuit parameters` (default) | `By rated, stall, and no-load datasheet parameters`

Select one of the following methods for block parameterization:

- `By equivalent circuit
  parameters` — Provide electrical
  parameters for an equivalent circuit model of the
  motor.
- `By rated, stall, and no-load datasheet
  parameters` — Provide current and
  speed parameters that the block converts to an equivalent
  circuit model of the motor.

### **Armature resistance, Ra** — Armature resistance `1.68` `Ohm` (default) | positive scalar

Resistance of the conducting portion of the motor.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By equivalent
circuit parameters`.

### **Series field winding resistance, Rs** — Series field winding resistance `1.68` `Ohm` (default) | positive scalar

Resistance of the series field winding.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By equivalent
circuit parameters`.

### **Shunt field winding resistance, Rp** — Shunt field winding resistance `303` `Ohm` (default) | positive scalar

Resistance of the shunt field winding.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By equivalent
circuit parameters`.

### **Series field winding to armature back EMF constant, Lsa** — Series field winding to armature back EMF constant `0.69` `H` (default) | positive scalar

Series field winding to armature back EMF constant.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By equivalent
circuit parameters`.

### **Shunt field winding to armature back EMF constant, Lpa** — Shunt field winding to armature back EMF constant `0.64` `H` (default) | positive scalar

Shunt field winding to armature back EMF constant.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By equivalent
circuit parameters`.

### **Rated voltage** — Rated voltage `100` `V` (default) | positive scalar

Voltage at which the motor is rated to operate.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By rated, stall, and
no-load datasheet parameters`.

### **Rated speed** — Rated speed `1000` `rpm` (default) | positive scalar

Speed at which the motor is rated to operate.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By rated, stall, and
no-load datasheet parameters`.

### **Rated electrical power** — Rated electrical power `136` `W` (default) | positive scalar

Power at which the motor is rated to operate.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By rated, stall, and
no-load datasheet parameters`.

### **Rated efficiency (percent)** — Rated efficiency `85` (default) | positive scalar

Efficiency at which the motor is rated to operate, as a percentage.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By rated, stall, and
no-load datasheet parameters`.

### **Stall current** — Zero speed current `30` `A` (default) | positive scalar

Amount of current generated by the motor when the speed is approximately zero. This
parameter must be greater than the value of the **No-load
current** parameter.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By rated, stall, and
no-load datasheet parameters`.

### **No-load speed** — No-load speed `4500` `rpm` (default) | positive scalar

Speed of the motor when no load is applied. This parameter must be greater than the
value of the **Rated speed** parameter.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By rated, stall, and
no-load datasheet parameters`.

### **No-load current** — No-load current `0.33` `A` (default) | positive scalar

Current of the motor when no load is applied.

#### Dependencies

To enable this parameter, set **Steady-state
parameterization** to `By rated, stall, and
no-load datasheet parameters`.

### **Ratio of shunt field winding resistance divided by series field winding resistance** — Ratio of shunt field winding resistance divided by series field winding resistance `190` (default) | nonnegative scalar

Ratio of the shunt field winding resistance divided by the series field winding
resistance.

#### Dependencies

To enable this parameter, in the
**Configuration** tab, set **Electrical
circuit topology** to
`Short-shunt` and, in the
**Steady-state** tab, set
**Steady-state parameterization** to
`By rated, stall, and no-load datasheet
parameters`.

### **Ratio of armature resistance divided by series field winding resistance** — Ratio of armature resistance divided by series field winding resistance `1.0` (default) | nonnegative scalar

Ratio of armature resistance divided by series field winding
resistance.

#### Dependencies

To enable this parameter, in the
**Configuration** tab, set **Electrical
circuit topology** to
`Long-shunt` and, in the
**Steady-state** tab, set
**Steady-state parameterization** to
`By rated, stall, and no-load datasheet
parameters`.

### Mechanical

### **Rotor inertia** — Rotor inertia `1e-4` `kg*m^2` (default) | scalar

Resistance of the rotor to change in motor motion. The value can be
zero.

### **Rotor damping** — Rotor dissipated energy `1e-6` `N*m/(rad/s)` (default) | scalar

Energy dissipated by the rotor. The value can be zero.

#### Dependencies

To enable this parameter, in the **Steady-State** tab, set
**Steady-state parameterization** to
`By equivalent circuit
parameters`.

### Electrical Dynamics

### **Series field winding inductance, Ls** — Series field winding inductance `0.9` `H` (default) | positive scalar

Inductance of the series field winding.

### **Shunt field winding inductance, Lp** — Shunt field winding inductance `0.85` `H` (default) | positive scalar

Inductance of the shunt field winding.

### **Coefficient of mutual inductance between shunt-series windings, k\_sp** — Coefficient of mutual inductance between shunt-series windings `0.8` (default) | nonnegative scalar between `0` and `1`

Coefficient of mutual inductance between shunt-series windings.

### Thermal

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default) | scalar

Coefficient α in the equation relating resistance to temperature. The
default value is for copper.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **Measurement temperature** — Measurement temperature `25` `degC` (default) | scalar

Temperature for which motor parameters are quoted.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **Thermal masses, [Ms Mp Ma]** — Thermal masses `[100, 100, 100]` `J/K` (default) | vector

1-by-3 row vector that defines the thermal mass for the series and shunt field windings
and armature winding. The thermal mass is the energy required to raise
the temperature by one degree.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### Faults

### **Armature winding fault** — Option to add armature winding fault `Add fault` (default)

Option to add a fault to the armature winding of the
Compound Motor block.

To add a fault, click the **Add fault**
hyperlink.

### **Fraction of revolution during which armature is open-circuit** — Fraction of revolution during which armature is open-circuit `1/3` (default) | scalar

Fraction of the revolution of the compound motor during which the
armature winding is faulted and the voltage source observes an open
circuit. For more information, see the Faults
section.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Armature winding fault** parameter.

### **Faulted armature winding open-circuit conductance** — Open-circuit conductance of faulted armature winding `1e-5` `S` (default) | scalar

Open-circuit conductance when the armature winding is faulted.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Armature winding fault**
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
hyperlink for the **Armature winding fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Armature winding fault** parameter and set
**Trigger type** to
`Timed`.

### **Maximum permissible armature winding current** — Maximum permissible armature winding current `inf` `A` (default)

Upper load-current threshold for open-circuit armature winding
faults.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Armature winding fault** parameter and set
**Trigger type** to
`Behavioral`.

### **Time to fail when exceeding armature winding current** — Time to fail when exceeding armature winding current `1` `s` (default) | scalar

Amount of time that the winding current must continuously exceed the
maximum permissible armature winding current before a behavioral fault
is triggered.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Armature winding fault** parameter and set
**Trigger type** to
`Behavioral`.

### **Series field winding fault** — Option to add series field winding fault `Add fault` (default)

Option to add a fault to the series field winding of the
Compound Motor block.

To add a fault, click the **Add fault**
hyperlink.

### **Faulted series field winding open-circuit conductance** — Open-circuit conductance of faulted field winding `1e-5` `S` (default) | scalar

Open-circuit conductance when the series field winding is
faulted.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Series field winding fault**
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
hyperlink for the **Series field winding fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Series field winding fault** parameter and
set **Trigger type** to
`Timed`.

### **Maximum permissible series field winding current** — Maximum permissible series field winding current `inf` `A` (default)

Upper load-current threshold for open-circuit series field winding
faults.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Series field winding fault** parameter and
set **Trigger type** to
`Behavioral`.

### **Time to fail when exceeding series field winding current** — Time to fail when exceeding series field winding current `1` `s` (default) | scalar

Amount of time that the winding current must continuously exceed the
maximum permissible series field winding current before a behavioral
fault is triggered.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Series field winding fault** parameter and
set **Trigger type** to
`Behavioral`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Series field winding fault** parameter and
set **Trigger type** to
`Additional triggers`.

### **Shunt field winding fault** — Option to add shunt field winding fault `Add fault` (default)

Option to add a fault to the shunt field winding of the
Compound Motor block.

To add a fault, click the **Add fault**
hyperlink.

### **Faulted shunt field winding open-circuit conductance** — Open-circuit conductance of faulted shunt winding `1e-5` `S` (default) | scalar

Open-circuit conductance when the shunt field winding is
faulted.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Shunt field winding fault** parameter.

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
hyperlink for the **Shunt field winding fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Shunt field winding fault** parameter and set
**Trigger type** to
`Timed`.

### **Maximum permissible shunt field winding current** — Maximum permissible shunt field winding current `inf` `A` (default)

Upper load-current threshold for open-circuit shunt field winding
faults.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Shunt field winding fault** parameter and set
**Trigger type** to
`Behavioral`.

### **Time to fail when exceeding shunt field winding current** — Time to fail when exceeding shunt field winding current `1` `s` (default) | scalar

Amount of time that the winding current must continuously exceed the
maximum permissible shunt field winding current before a behavioral
fault is triggered.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Shunt field winding fault** parameter and set
**Trigger type** to
`Behavioral`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Shunt field winding fault** parameter and set
**Trigger type** to
`Additional triggers`.

## Libraries

Simscape / Electrical / Electromechanical / Brushed Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

### R2025a: Model Reversible Conditional Faults

You can now model reversible conditional faults in the Compound Motor block by clearing the
**Trigger stays on once activated** parameter. The block enters the
faulted state when the trigger condition is true and enters the unfaulted state when the
trigger condition is false.

Before R2025a, the block enters the faulted state when the trigger condition becomes true
for the first time and remains in the faulted state for the rest of the simulation.

If you create a model before R2025a and enable a conditional fault in the Compound Motor
block, the block now selects the **Trigger stays on once activated**
parameter by default for backward compatibility.

## Description

Compound motor model with electrical and torque characteristics and fault modeling

The Compound Motor block represents the electrical and torque
characteristics of a compound motor. This figure shows the equivalent circuit for a
short-shunt compound motor:

Short-shunt compound motor model

This figure shows the equivalent circuit for a long-shunt compound motor:

Long-shunt compound motor model

where:

- *i* is the total current.
- *is* is the series field winding
  current.
- *ip* is the parallel field winding
  current.
- *ia* is the armature current.
- *V* is the total voltage.
- *Vs* is the series field winding
  voltage.
- *Vp* is the parallel field winding
  voltage.
- *Va* is the armature
  voltage.
- *ω* is the angular velocity.
- *te* is the torque.

If you set the **Steady-state parameterization** parameter to
`By equivalent circuit parameters`, you can specify the
equivalent circuit parameters for this model:

- *Ra* — **Armature
  resistance, Ra**
- *Rs* — **Series
  field winding resistance, Rs**
- *Rp* — **Shunt
  field winding resistance, Rp**
- *Lsa* — **Series
  field winding to armature back EMF constant, Lsa**
- *Lpa* — **Shunt
  field winding to armature back EMF constant, Lpa**

### Short-Shunt Equations

When **Electrical circuit topology** is set to
`Short-shunt`, the electrical dynamic equations
are:

Vs=Rsis+Lsdisdt+LspdipdtVp=Rpip+Lpdipdt+LspdisdtVemf=kvω=(Lsais+Lpaip)ωV=Vs+VpVp=kvω+Raiai=isia=is−ip

These are the mechanical dynamic equations for the short-shunt compound
motor:

Jω˙+Dω=te+tloadte=kvia=(Lsais+Lpaip)ia

From these dynamic equations, the block obtains the steady-state equations by
making the derivatives equal to zero:

Vemf=Lsaisω+Lpaipωtelec=kv(is−ip)=Vemfis−ipωV=Rsis+RpipRpip=Vemf+Ra(is−ip)

Then, it computes the steady-state currents and torque as follows:

telec(ω,V)=−V2(Lpaω+Lsaω−Rp)(RaLpa+RaLsa+RpLsa)(RaRp+RaRs+RpRs+LsaRpω−LpaRsω)2i=is(ω,V)=V(Ra+Rp−Lpaω)RaRp+RaRs+RpRs+LsaRpω−LpaRsω

### Long-Shunt Equations

When **Electrical circuit topology** is set to
`Long-shunt`, the electrical dynamic equations
are:

Vs=Rsis+Lsdisdt+LspdipdtVp=Rpip+Lpdipdt+LspdisdtVemf=kvω=(Lsais+Lpaip)ωV=VpVp=kvω+Raia+Vsi=is+ipia=is

These are the mechanical dynamic equations for the long-shunt compound
motor:

Jω˙+Dω=te+tloadte=kvia=(Lsais+Lpaip)ia

From these dynamic equations, the block obtains the steady-state equations by
making the derivatives equal to zero:

Vemf=Lsaisω+Lpaipωtelec=kvis=VemfisωV=RpipRpip=Vemf+(Ra+Rs)is

Then, it computes the steady-state currents and torque as follows:

telec(ω,V)=V2(Ra−Lpaω)(RaLpa+RsLpa+RpLsa)Rp2(Ra+Rs+Lsaω)2i(ω,V)=is+ip=VRp+RpV−LpaVωRp(Ra+Rs+Lsaω)

### Faults

To model a fault in the Compound Motor block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Compound Motor block allows you to model three types of
faults:

- Armature winding fault — The armature winding fails and becomes
  open circuit.
- Series field winding fault — The series field winding fails and
  becomes open circuit.
- Shunt field winding fault — The shunt field winding fails and
  becomes open circuit.

When the armature fails, the voltage source connected to this block observes an open
circuit for a fraction of the total motor revolution, specified by the
**Fraction of revolution during which armature is
open-circuit** parameter. This figure illustrates the circuit state
behavior and the open-circuit state (`rev_faulted`) for a
revolution period:

**Fault Triggers**

You specify how and when faults occur by using the **Trigger type**
parameter.

If you set the **Trigger type** to `Behavioral`,
the Compound Motor block triggers faults when the winding currents continuously
exceed a threshold value for longer than a specific time interval:

- Armature winding faults occur when the winding currents
  continuously exceed the value of the **Maximum permissible
  armature winding current** parameter for a duration
  longer than the value of the **Time to fail when exceeding
  armature winding current** parameter.
- Series field winding faults occur when the winding currents exceed
  the value of the **Maximum permissible series field winding
  current** parameter for a duration longer than the
  value of the **Time to fail when exceeding series field
  winding current** parameter.
- Shunt field winding faults occur when the winding currents exceed
  the value of the **Maximum permissible shunt field winding
  current** parameter for a duration longer than the
  value of the **Time to fail when exceeding shunt field
  winding current** parameter.

If you set the **Trigger
type** to `Conditional`, you can choose whether faults
in the Compound Motor block are reversible *(since R2025a)*. To model irreversible faults, click
**Open fault properties** to open the Property Inspector and select the
**Trigger stays on once activated** parameter. The block enters the faulted
state when the trigger condition becomes true for the first time and remains in the faulted
state for the rest of the simulation. To model reversible faults, clear the **Trigger
stays on once activated** parameter. The block enters the faulted state when the
trigger condition is true and enters the unfaulted state when the trigger condition is
false.

For more information about adding faults to blocks and
specifying fault triggers, see Introduction to Simscape Faults.

### Model Thermal Effects

You can expose thermal ports to model the effects of losses that convert power to heat. To
expose the thermal ports, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain
  thermal ports.
- `Show thermal port` — The block contains thermal
  conserving ports for the series field winding, the shunt field winding, and the
  armature.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.
