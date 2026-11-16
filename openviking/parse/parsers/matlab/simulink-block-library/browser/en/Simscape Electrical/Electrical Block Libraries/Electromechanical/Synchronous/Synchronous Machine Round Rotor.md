---
type: simulink-block
title: 'Synchronous Machine Round Rotor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Synchronous'
documentation_page: 'synchronousmachineroundrotor'
documentation_source_path: 'ref/synchronousmachineroundrotor.html'
language: en
---

# Synchronous Machine Round Rotor

## Ports

### Output

### **pu** — Machine per-unit measurements physical

Physical signal vector port associated with the machine per-unit
measurements. The vector elements are:

- Field voltage (field circuit base, Efd),
  *pu\_fd\_Efd*
- Field current (field circuit base, Ifd),
  *pu\_fd\_Ifd*
- Electrical torque, *pu\_torque*
- Rotor velocity, *pu\_velocity*
- Stator d-axis voltage, *pu\_ed*
- Stator q-axis voltage, *pu\_eq*
- Stator zero-sequence voltage,
  *pu\_e0*
- Stator d-axis current, *pu\_id*
- Stator q-axis current, *pu\_iq*
- Stator zero-sequence current,
  *pu\_i0*
- Rotor electrical angle,
  *electrical\_angle\_out*

To connect to this port, use the Synchronous Machine Measurement block.
### Conserving

### **fd+** — Field winding positive terminal electrical

Electrical conserving port associated with the field winding positive
terminal.

### **fd-** — Field winding negative terminal electrical

Electrical conserving port associated with the field winding negative
terminal.

### **R** — Machine rotor mechanical

Mechanical rotational conserving port associated with the machine
rotor.

### **C** — Machine case mechanical

Mechanical rotational conserving port associated with the machine
case.

### **~** — Stator windings electrical

Expandable three-phase
port associated with the stator windings.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **n** — Neutral phase electrical

Electrical conserving port associated with the neutral point of the
wye winding configuration.

#### Dependencies

To enable this port, set **Zero sequence** to
`Include`.

### **a** — *a*-phase electrical

Electrical conserving port associated with
*a*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b** — *b*-phase electrical

Electrical conserving port associated with
*b*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c** — *c*-phase electrical

Electrical conserving port associated with
*c*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **HA** — *a*-phase terminal thermal port thermal

Thermal conserving port associated with stator winding
*a*.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HB** — *b*-phase terminal thermal port thermal

Thermal conserving port associated with stator winding
*b*.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HC** — *c*-phase terminal thermal port thermal

Thermal conserving port associated with stator winding
*c*.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HR** — Rotor thermal port thermal

Thermal conserving port associated with the rotor.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Option to enable thermal ports `No thermal port` (default) | `Show thermal port`

Option to enable the thermal ports of the block and model the effects of generated
heat and machine temperature.

### Main

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Rated apparent power** — Rated apparent power `555e6` `V*A` (default)

Rated apparent power.

### **Rated voltage** — RMS rated line-line voltage `24e3` `V` (default)

RMS rated line-line voltage.

### **Rated electrical frequency** — Nominal electrical frequency `60` `Hz` (default)

Nominal electrical frequency at which rated apparent power is
quoted.

### **Number of pole pairs** — Number of pole pairs `1` (default)

Number of machine pole pairs.

### **Specify parameterization by** — Block parameterization `Fundamental parameters` (default) | `Standard parameters`

Block parameterization method. Options are:

- `Fundamental parameters` —
  Specify impedance using fundamental parameters.
- `Standard parameters` —
  Specify impedance using fundamental parameters and specify
  d-axis and q-axis time constants.

This parameter affects the visibility of the **Time
Constant** settings and the parameters in the
**Impedances** settings.

### **Specify field circuit input required to produce rated terminal voltage at no load by** — Specify field circuit input required to produce rated terminal voltage at no load by `Field circuit current` (default) | `Field circuit voltage`

Field circuit parameterization method. Options are:

- `Field circuit voltage` —
  Specify the field circuit in terms of voltage.
- `Field circuit current` —
  Specify the field circuit in terms of current.

This parameter affects the visibility of the **Field circuit
voltage** and **Field circuit current**
parameters.

### **Field circuit voltage** — Field circuit voltage `95.95` `V` (default)

Voltage across field circuit which produces rated voltage at machine
terminals.

#### Dependencies

This parameter is visible only if the **Specify field
circuit input required to produce rated terminal voltage at no
load by** parameter is set to `Field
circuit voltage`.

### **Field circuit current** — Field circuit current `1300` `A` (default)

Current in field circuit which produces rated voltage at machine
terminals.

#### Dependencies

This parameter is visible only if the **Specify field
circuit input required to produce rated terminal voltage at no
load by** parameter is set to `Field
circuit current`.

### **Zero sequence** — Zero-sequence model `Include` (default) | `Exclude`

Zero-sequence model:

- `Include` — Prioritize model fidelity.
  This model is the default zero-sequence model. An error occurs if you
  Include zero-sequence terms for simulations that use the Partitioning
  solver. For more information, see Increase Simulation Speed Using the Partitioning Solver.
- `Exclude` — Prioritize simulation speed for desktop simulation or real-time deployment.

#### Dependencies

If this parameter is set to:

- `Include` and **Specify
  parameterization by** is set to **Fundamental
  parameters** — The **Stator zero-sequence
  inductance, L0** parameter in the
  **Impedances** settings is visible.
- `Include` and **Specify
  parameterization by** is set to **Standard
  parameters** — The **zero-sequence
  reactance, X0** parameter in the
  **Impedances** settings is visible.
- `Exclude` — The zero-sequence
  parameter in the **Impedances** settings is not
  visible.

### **Rotor angle definition** — Reference point for the rotor angle measurement `Angle between the a-phase magnetic axis and the d-axis` (default) | `Angle between the a-phase magnetic axis and the q-axis`

Reference point for the rotor angle measurement.

When you select the default value, the rotor *d*-axis and stator *a*-phase magnetic axis are aligned when the rotor angle is zero.

The other value you can choose for this parameter is `Angle between the a-phase magnetic axis and the q-axis`. When you select this value, the rotor *q*-axis and stator *a*-phase magnetic axis are aligned when the rotor angle is zero.

### Impedances

### **Stator d-axis mutual inductance (unsaturated), Ladu** — Stator d-axis mutual inductance (unsaturated) `1.66` (default) | positive scalar

Unsaturated stator *d*-axis mutual inductance. If
**Magnetic saturation representation** is set to
`None`, this is equivalent to the stator
d-axis mutual inductance. This parameter must be greater than
`0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Stator q-axis mutual inductance (unsaturated), Laqu** — Stator q-axis mutual inductance (unsaturated) `1.61` (default) | positive scalar

Unsaturated stator *q*-axis mutual inductance. If
**Magnetic saturation representation** is set to
`None`, this is equivalent to the stator
q-axis mutual inductance. This parameter must be greater than
`0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Stator zero-sequence inductance, L0** — Stator zero-sequence inductance `0.15` (default) | positive scalar

Stator zero-sequence inductance. This parameter must be greater than
`0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters` and the
**Zero Sequence** parameter to
`Include`.

### **Stator leakage inductance, Ll** — Stator leakage inductance `0.15` (default) | positive scalar

Stator leakage inductance. This parameter must be greater than
`0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Stator resistance, Ra** — Stator resistance `0.003` (default) | positive scalar

Stator resistance. This parameter must be greater than
`0`.

### **Rotor field circuit inductance, Lfd** — Rotor field circuit inductance `0.165` (default) | positive scalar

Rotor field circuit inductance. This parameter must be greater than
`0`.

### **Rotor field circuit resistance, Rfd** — Rotor field circuit resistance `0.0006` (default) | positive scalar

Rotor field circuit resistance. This parameter must be greater than
`0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Rotor d-axis damper winding 1 inductance, L1d** — Rotor d-axis damper winding 1 inductance `0.1713` (default) | positive scalar

Rotor *d*-axis damper winding 1 inductance. This
parameter must be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Rotor d-axis damper winding 1 resistance, R1d** — Rotor d-axis damper winding 1 resistance `0.0284` (default) | positive scalar

Rotor *d*-axis damper winding 1 resistance. This
parameter must be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Rotor q-axis damper winding 1 inductance, L1q** — Rotor q-axis damper winding 1 inductance `0.7252` (default) | positive scalar

Rotor *q*-axis damper winding 1 inductance. This
parameter must be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Rotor q-axis damper winding 1 resistance, R1q** — Rotor q-axis damper winding 1 resistance `0.00619` (default) | positive scalar

Rotor *q*-axis damper winding 1 resistance. This
parameter must be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Rotor q-axis damper winding 2 inductance, L2q** — Rotor q-axis damper winding 2 inductance `0.125` (default) | positive scalar

Rotor *q*-axis damper winding 2 inductance. This
parameter must be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Rotor q-axis damper winding 2 resistance, R2q** — Rotor q-axis damper winding 2 resistance `0.02368` (default) | positive scalar

Rotor *q*-axis damper winding 2 resistance. This
parameter must be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Stator leakage reactance, Xl** — Stator leakage reactance `0.15` (default) | positive scalar

Stator leakage reactance. This parameter must be greater than
`0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **d-axis synchronous reactance, Xd** — d-axis synchronous reactance `1.81` (default) | positive scalar

*d*-axis synchronous reactance. This parameter must
be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **q-axis synchronous reactance, Xq** — q-axis synchronous reactance `1.76` (default) | positive scalar

*q*-axis synchronous reactance. This parameter must
be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **zero-sequence reactance, X0** — Zero-sequence reactance `0.15` (default) | positive scalar

Zero-sequence reactance. This parameter must be greater than
`0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters` and the
**Zero Sequence** parameter to
`Include`.

### **d-axis transient reactance, Xd'** — d-axis transient reactance `0.3` (default) | positive scalar

*d*-axis transient reactance. This parameter must be
greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **q-axis transient reactance, Xq'** — q-axis transient reactance `0` (default) | positive scalar

*q*-axis transient reactance. This parameter must be
greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **d-axis subtransient reactance, Xd''** — d-axis subtransient reactance `0.23` (default) | positive scalar

*d*-axis subtransient reactance. This parameter must
be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **q-axis subtransient reactance, Xq''** — q-axis subtransient reactance `0.25` (default) | positive scalar

*q*-axis subtransient reactance. This parameter must
be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### Time Constants

### **Specify d-axis time constant** — Specify d-axis time constant `Open circuit` (default) | `Short circuit`

Select between `Open circuit` and
`Short circuit`.

The setting for this parameter affects the visibility of the
*d*-axis time constant parameters.

### **d-axis transient open-circuit, Td0'** — d-axis transient open-circuit `8` `s` (default) | positive scalar

*d*-axis transient open-circuit time constant. This
parameter must be:

- Greater than 0.
- Greater than **d-axis subtransient open-circuit,
  Td0''**.

#### Dependencies

This parameter is visible only if the **Specify d-axis
transient time constant** parameter is set to
`Open circuit`.

### **d-axis transient short-circuit, Td'** — d-axis transient short-circuit `1.3260` `s` (default) | positive scalar

*d*-axis transient short-circuit time constant. This
parameter must be:

- Greater than 0.
- Greater than **d-axis subtransient short-circuit,
  Td''**.

#### Dependencies

This parameter is visible only if the **Specify d-axis
transient time constant** parameter is set to
`Short circuit`.

### **d-axis subtransient open-circuit, Td0''** — d-axis subtransient open-circuit `0.03` `s` (default) | positive scalar

*d*-axis subtransient open-circuit time constant.
This parameter must be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify d-axis
transient time constant** parameter is set to
`Open circuit`.

### **d-axis subtransient short-circuit, Td''** — d-axis subtransient short-circuit `0.0230` `s` (default) | positive scalar

*d*-axis subtransient short-circuit time constant.
This parameter must be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify d-axis
transient time constant** parameter is set to
`Short circuit`.

### **Specify q-axis time constant** — Specify q-axis time constant `Open circuit` (default) | `Short circuit`

Select between `Open circuit` and
`Short circuit`.

The setting for this parameter affects the visibility of the
*q*-axis time constant parameters.

### **q-axis transient open-circuit, Tq0'** — q-axis transient open-circuit `1` `s` (default) | positive scalar

*q*-axis transient open-circuit time constant. This
parameter must be:

- Greater than 0.
- Greater than **q-axis subtransient open-circuit,
  Tq0''**.

#### Dependencies

This parameter is visible only if the **Specify q-axis
transient time constant** parameter is set to
`Open circuit`.

### **q-axis transient short-circuit, Tq'** — q-axis transient short-circuit `0.3693` `s` (default) | positive scalar

*q*-axis transient short-circuit time constant. This
parameter must be:

- Greater than 0.
- Greater than **q-axis subtransient short-circuit,
  Tq''**.

#### Dependencies

This parameter is visible only if the **Specify q-axis
transient time constant** parameter is set to
`Short circuit`.

### **q-axis subtransient open-circuit, Tq0''** — q-axis subtransient open-circuit `0.07` `s` (default) | positive scalar

*q*-axis subtransient open-circuit time constant.
This parameter must be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify q-axis
transient time constant** parameter is set to
`Open circuit`.

### **q-axis subtransient short-circuit, Tq''** — q-axis subtransient short-circuit `0.0269` `s` (default) | positive scalar

*q*-axis subtransient short-circuit time constant.
This parameter must be greater than `0`.

#### Dependencies

This parameter is visible only if the **Specify q-axis
transient time constant** parameter is set to
`Short circuit`.

### Saturation

### **Magnetic saturation representation** — Magnetic saturation representation `None` (default) | `Open-circuit lookup table (v versus i)`

Block magnetic saturation model:

- `None`
- `Open-circuit lookup table (v versus
  i)`

#### Dependencies

If you set this parameter to `Open-circuit lookup
table (v versus i)`, related parameters are
visible.

### **Per-unit field current saturation data, ifd** — Per-unit field current saturation data `[0, .48, .76, 1.38, 1.79]` (default)

Field current, *ifd*, data
that populates the air-gap voltage,
*Vag*, versus field current,
*ifd*, lookup table.
This parameter must contain a vector with at least five elements.

#### Dependencies

This parameter is visible only if the **Magnetic
saturation representation** parameter is set to
`Open-circuit lookup table (v versus
i)`.

### **Per-unit air-gap voltage saturation data, Vag** — Per-unit air-gap voltage saturation data `[0, .8, 1.08, 1.31, 1.4]` (default)

Air-gap voltage, *Vag*, data
that populates the air-gap voltage,
*Vag*, versus field current,
*ifd*, lookup table.
This parameter must contain a vector with at least five elements.

#### Dependencies

This parameter is visible only if the **Magnetic
saturation representation** parameter is set to
`Open-circuit lookup table (v versus
i)`.

### Initial Conditions

### **Initialization option** — Option for specifying values at start of simulation `Set real power, reactive power, terminal voltage, and terminal phase` (default) | `Set targets for rotor angle and Park's transform variables` | `Set targets for load flow variables`

Option for specifying values for certain parameters and variables at
the start of simulation. Set this parameter to:

- `Set real power, reactive power, terminal
  voltage and terminal phase` — Set an
  operating point regardless of the connected network.
- `Set targets for rotor angle and Park's
  transform variables` — Specify the priority
  and initial target values for block variables before
  simulation using the **Variables**
  settings. For more information, see Set Priority and Initial Target for Block Variables.
- `Set targets for load flow
  variables` — Select a bus type and specify
  the related parameters for a load-flow analysis in the
  **Initial Conditions** settings.

### **Source type** — Voltage source model `Swing bus` (default) | `PV bus` | `PQ bus`

Type of voltage source that the block models.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set targets for load flow
variables`.

### **Terminal voltage magnitude** — Terminal voltage magnitude `24e3` `V` (default) | positive scalar

Terminal voltage magnitude.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal phase`.
Alternatively, set **Initialization option** to
`Set targets for load flow variables`
and **Source type** to `Swing
bus` or `PV bus`.

### **Terminal voltage angle** — Terminal voltage angle `0` `deg` (default) | scalar

Terminal voltage angle.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal phase`.
Alternatively, set **Initialization option** to
`Set targets for load flow variables`
and **Source type** to `Swing
bus`.

### **Active power generated** — Generated active power `500e6` `V*A` (default) | scalar

Active power that the machine generates.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal phase`.
Alternatively, set **Initialization option** to
`Set targets for load flow variables`
and **Source type** to `PV
bus` or `PQ bus`.

### **Reactive power generated** — Generated reactive power `0` `V*A` (default) | scalar

Reactive power that the machine generates.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal phase`.
Alternatively, set **Initialization option** to
`Set targets for load flow variables`
and **Source type** to `PQ
bus`.

### **Minimum terminal voltage magnitude (pu)** — Minimum terminal voltage magnitude `0.95` (default) | positive scalar

Per-unit minimum steady-state voltage magnitude.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set targets for load flow
variables` and **Source type** to
`PQ bus`.

### **Phase search range at terminals** — Phase search range at terminals `[-inf, inf]` `deg` (default) | vector of two elements

Vector that defines the search range of the phase angle at the
terminals.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set targets for load flow
variables` and **Source type** to
`PV bus` or `PQ
bus`.

### **Parasitic conductance to electrical reference** — Parasitic conductance to electrical reference `1e-6` `S` (default) | positive scalar

Parasitic conductance to the electrical reference.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set targets for load flow
variables`.

### Thermal

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Measurement temperature** — Rated temperature `298.15` `k` (default) | real scalar

Temperature for which motor parameters are quoted.

### **Resistance temperature coefficient** — Temperature coefficient `3.93e-3` `1/K` (default) | positive scalar

Coefficient α in the equation relating resistance to temperature for
all three windings, as described in Thermal Model for Actuator Blocks. The default value,
`3.93e-3` 1/K, is for copper.

### **Thermal mass for each stator winding** — Winding thermal mass `100` `J/K` (default) | positive scalar

Thermal mass value for each stator winding. The thermal mass is the
energy required to raise the temperature by one degree.

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K` (default) | positive scalar

Thermal mass of the rotor. The thermal mass is the energy required to
raise the temperature of the rotor by one degree.

## Libraries

Simscape / Electrical / Electromechanical / Synchronous

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`. Also, the simlog format is identical for
`Composite three-phase ports` and `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Round-rotor synchronous machine with fundamental or standard parameterization

The Synchronous Machine Round Rotor block models a
round-rotor synchronous machine using fundamental or standard parameters.

### Synchronous Machine Initialization Using Load-Flow Target Values

If the block is in a network that is compatible with the
frequency-time simulation mode, you can perform a load-flow analysis on the network. A
load-flow analysis provides steady-state values that you can use to initialize the
machine.

For more information, see Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode. For an example that shows how to initialize
a synchronous machine using data from a load-flow analysis, see Synchronous Machine Initialization with Loadflow.

### Equations

The synchronous machine equations are expressed with respect to a rotating
reference frame, defined by

θe(t)=Nθr(t),

where:

- *θe* is the electrical
  angle.
- *N* is the number of pole pairs.
- *θr* is the rotor
  angle.

The Park transformation maps the synchronous machine equations to the rotating
reference frame with respect to the electrical angle. The Park transformation is
defined by

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212].

The Park transformation is used to define the per-unit synchronous machine
equations. The stator voltage equations are defined by

ed=1ωbasedψddt−Ψqωr−Raid,

eq=1ωbasedψqdt+Ψdωr−Raiq,

and

e0=1ωbasedΨ0dt−Rai0,

where:

- *ed*,
  *eq*, and
  *e0* are the
  *d*-axis, *q*-axis, and
  zero-sequence stator voltages, defined by

  [edeqe0]=Ps[vavbvc].

  *va*,
  *vb*, and
  *vc* are the stator
  voltages measured from port **~** to neutral port
  **n**.
- *ωbase* is the per-unit base
  electrical speed.
- *ψd*,
  *ψq*, and
  *ψ0* are the
  *d*-axis, *q*-axis, and
  zero-sequence stator flux linkages.
- *ωr* is the per-unit rotor
  rotational speed.
- *Ra* is the stator
  resistance.
- *id*,
  *iq*, and
  *i0* are the
  *d*-axis, *q*-axis, and
  zero-sequence stator currents, defined by

  [idiqi0]=Ps[iaibic].

  *ia*,
  *ib*, and
  *ic* are the stator
  currents flowing from port **~** to port
  **n**.

The rotor voltage equations are defined by

efd=1ωbasedΨfddt+Rfdifd,

e1d=1ωbasedΨ1ddt+R1di1d=0,

e1q=1ωbasedΨ1qdt+R1qi1q=0,

and

e2q=1ωbasedΨ2qdt+R2qi2q=0,

where:

- *efd* is the field
  voltage.
- *e1d*,
  *e1q*, and
  *e2q* are the voltages
  across the *d*-axis damper winding 1,
  *q*-axis damper winding 1, and
  *q*-axis damper winding 2. They are all equal to
  0.
- *ψfd*,
  *ψ1d*,
  *ψ1q*, and
  *ψ2q* are the magnetic
  fluxes linking the field circuit, *d*-axis damper
  winding 1, *q*-axis damper winding 1, and
  *q*-axis damper winding 2.
- *Rfd*,
  *R1d*,
  *R1q*, and
  *R2q* are the
  resistances of rotor field circuit, *d*-axis damper
  winding 1, *q*-axis damper winding 1, and
  *q*-axis damper winding 2.
- *ifd*,
  *i1d*,
  *i1q*, and
  *i2q* are the currents
  flowing in the field circuit, *d*-axis damper winding
  1, *q*-axis damper winding 1, and
  *q*-axis damper winding 2.

The saturation equations are defined by

ψad=ψd+Llid,

ψaq=ψq+Lliq,

ψat=ψad2+ψaq2,

Ks=1 (If saturation is disabled),

Ks=f(ψat) (If saturation is enabled),

Lad=Ks\*Ladu,

and

Laq=Ks\*Laqu,

where:

- *ψad* is the
  *d*-axis air-gap or mutual flux linkage.
- *ψaq* is the
  *q*-axis air-gap or mutual flux linkage.
- *ψat* is the air-gap flux
  linkage.
- *Ks* is the saturation
  factor.
- *Ladu* is the unsaturated
  mutual inductance of the stator *d*-axis.
- *Lad* is the mutual inductance
  of the stator *d*-axis.
- *Laqu* is the unsaturated
  mutual inductance of the stator *q*-axis.
- *Laq* is the mutual inductance
  of the stator *q*-axis.

The saturation factor function, *f*, is calculated from the
per-unit open-circuit lookup table as:

Lad=dψatdifd,

Vag=g(ifd),

and

Lad=dg(ifd)difd=dVagdifd,

where *Vag* is the per-unit air-gap
voltage.

In per-unit,

Ks=LadLadu,

and

ψat=Vag

can be rearranged to

Ks=f(ψat).

The stator flux linkage equations are defined by

Ψd=−(Lad+Ll)id​+Ladifd+Ladi1d,

Ψq=−(Laq+Ll)iq​+Laqi1q+Laqi2q,

and

Ψ0=−L0i0,

where:

- *Ll* is the stator leakage
  inductance.
- *Lad* and
  *Laq* are the mutual
  inductances of the stator *d*-axis and
  *q*-axis.

The rotor flux linkage equations are defined by

ψfd=Lffdifd+Lf1di1d−Ladid,

ψ1d=Lf1difd+L11di1d−Ladid,

ψ1q=L11qi1q+Laqi2q−Laqiq,

and

ψ2q=Laqi1q+L22qi2q−Laqiq,

where:

- *Lffd* is the self-inductances
  of the rotor field circuit.
- *Lffd* is the self-inductance of
  the rotor field circuit.
- *L11d* is the self-inductance
  of the *d*-axis damper winding 1.
- *L11q* is the self-inductance
  of the *q*-axis damper winding 1.
- *L22q* is the self-inductance
  of the *q*-axis damper winding 2.
- *Lf1d* is the rotor field
  circuit and *d*-axis damper winding 1 mutual
  inductance.

The inductances are defined by these equations:

Lffd=Lad+Lfd

Lf1d=Lffd−Lfd

L11d=Lf1d+L1d

L11q=Laq+L1q

L22q=Laq+L2q

The inductance equations assume that per-unit mutual inductance
*L12q* =
*Laq*, that is, the stator and rotor
currents in the *q*-axis all link a single mutual flux represented
by *Laq*.

The rotor torque is defined by

Te=Ψdiq−Ψqid.

### Plotting and Display Options

You can perform plotting and display actions using the
**Electrical** menu on the block context menu.

Right-click the block and, from the **Electrical** menu, select an option:

- **Display Base Values** — Displays the machine
  per-unit base values in the MATLAB® Command Window.
- **Display Associated Base Values** — Displays
  associated per-unit base values in the MATLAB Command Window.
- **Display Associated Initial Conditions** —
  Displays associated initial conditions in the MATLAB Command Window.
- **Plot Open-Circuit Saturation (pu)** — Plots
  air-gap voltage, *Vag*, versus field
  current, *ifd*, both measured in
  per-unit, in a MATLAB figure window. The plot contains three traces:

  - Unsaturated — **Stator d-axis mutual inductance
    (unsaturated), Ladu** you specify
  - Saturated — **Per-unit open-circuit lookup table (Vag
    versus ifd)** you specify
  - Derived — Open-circuit lookup table (per-unit) derived from
    the **Per-unit open-circuit lookup table (Vag versus
    ifd)** you specify. This data is used to calculate the
    saturation factor, *Ks*,
    versus magnetic flux linkage,
    *ψat*,
    characteristic.
- **Plot Saturation Factor (pu)** — Plots saturation
  factor, *Ks*, versus magnetic flux
  linkage, *ψat*, both measured in
  per-unit, in a MATLAB figure window using the machine parameters. This parameter is
  derived from other parameters that you specify:

  - **Stator d-axis mutual inductance (unsaturated),
    Ladu**
  - **Per-unit field current saturation data,
    ifd**
  - **Per-unit air-gap voltage saturation data,
    Vag**
- **Plot Power Capability
  Curves** — Plots active power P versus reactive power Q,
  both measured in per-unit, in a MATLAB figure window. The plot might contain multiple traces. Each
  trace corresponds to a maximum field circuit voltage measured in per-unit
  (non-reciprocal per-unit system). The plot shows the maximum reactive power
  that the generator produces when operating with a lagging power factor and
  the minimum reactive power that the generator absorbs when operating with a
  leading power factor. *(since R2023b)*

### Model Thermal Effects

You can expose thermal ports to model the effects of generated heat and machine temperature. To expose the thermal ports, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain thermal ports.
- `Show thermal port` — The block contains multiple thermal conserving ports.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

For this block, the **Initial Targets** settings are visible only if, in
the **Initial Conditions** section, you set the **Initialization
option** parameter to `Set targets for rotor angle and Park's
transform variables`.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
