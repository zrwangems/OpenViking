---
type: simulink-block
title: 'Synchronous Machine Model 2.1'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Synchronous'
documentation_page: 'synchronousmachinemodel21'
documentation_source_path: 'ref/synchronousmachinemodel21.html'
language: en
---

# Synchronous Machine Model 2.1

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
- Stator zero-sequence voltage, *pu\_e0*
  — This port is provided to maintain a compatible
  interface with other machine models. Its value is always
  zero.
- Stator d-axis current, *pu\_id*
- Stator q-axis current, *pu\_iq*
- Stator zero-sequence current, *pu\_i0*
  — This port is provided to maintain a compatible
  interface with other machine models. Its value is always
  zero.
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
wye winding configuration. This port is provided to maintain a
compatible interface for existing machine models. The voltage and
current on this port are ignored.

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
  Fundamental parameters are visible in the
  **Impedances** settings and the
  **Time Constants** settings are not
  visible.
- `Standard parameters` —
  Standard parameters are visible in the
  **Impedances** and the **Time
  Constants** settings are visible.

This parameter affects the visibility of the **Time
Constant** settings and the parameters in the
**Impedances** settings.

### **Specify field circuit input required to produce rated terminal voltage at no load by** — Specify field circuit input required to produce rated terminal voltage at no load by `Field circuit current` (default) | `Field circuit voltage`

Field circuit parameterization method. Options are:

- `Field circuit voltage` —
  Specify the field circuit in terms of voltage.
- `Field circuit current` —
  Specify the field circuit in terms of current. This method
  is the default field-circuit parameterization method.

This parameter affects the visibility of the **Field circuit
voltage** and **Field circuit current**
parameters.

### **Field circuit voltage** — Field circuit voltage `92.95` `V` (default)

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

### **Rotor angle definition** — Reference point for the rotor angle measurement `Angle between the a-phase magnetic axis and the d-axis` (default) | `Angle between the a-phase magnetic axis and the q-axis`

Reference point for the rotor angle measurement.

When you select the default value, the rotor *d*-axis and stator *a*-phase magnetic axis are aligned when the rotor angle is zero.

The other value you can choose for this parameter is `Angle between the a-phase magnetic axis and the q-axis`. When you select this value, the rotor *q*-axis and stator *a*-phase magnetic axis are aligned when the rotor angle is zero.

### Impedances

### **Stator d-axis mutual inductance (unsaturated), Ladu** — Stator d-axis mutual inductance (unsaturated) `1.66` (default) | positive scalar

Unsaturated stator *d*-axis mutual inductance. This
parameter must be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Stator q-axis mutual inductance (unsaturated), Laqu** — Stator q-axis mutual inductance (unsaturated) `1.61` (default) | positive scalar

Unsaturated stator *q*-axis mutual inductance. This
parameter must be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Stator leakage inductance, Ll** — Stator leakage inductance `0.15` (default) | positive scalar

Stator leakage inductance. This parameter must be greater than
0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Stator resistance, Ra** — Stator resistance `0.003` (default) | positive scalar

Stator resistance. This parameter must be greater than 0.

### **Rotor field circuit inductance, Lfd** — Rotor field circuit inductance `0.165` (default) | positive scalar

Rotor field circuit inductance. This parameter must be greater than
0.

### **Rotor field circuit resistance, Rfd** — Rotor field circuit resistance `0.0006` (default) | positive scalar

Rotor field circuit resistance. This parameter must be greater than
0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Rotor d-axis damper winding 1 inductance, L1d** — Rotor d-axis damper winding 1 inductance `0.1713` (default) | positive scalar

Rotor *d*-axis damper winding 1 inductance. This
parameter must be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Rotor d-axis damper winding 1 resistance, R1d** — Rotor d-axis damper winding 1 resistance `0.0284` (default) | positive scalar

Rotor *d*-axis damper winding 1 resistance. This
parameter must be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Rotor q-axis damper winding 1 inductance, L1q** — Rotor q-axis damper winding 1 inductance `0.1066` (default) | positive scalar

Rotor *q*-axis damper winding 1 inductance. This
parameter must be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Rotor q-axis damper winding 1 resistance, R1q** — Rotor q-axis damper winding 1 resistance `0.0650` (default) | positive scalar

Rotor *q*-axis damper winding 1 resistance. This
parameter must be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Fundamental parameters`.

### **Stator leakage reactance, Xl** — Stator leakage reactance `0.15` (default) | positive scalar

Stator leakage reactance. This parameter must be greater than
0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **d-axis synchronous reactance, Xd** — d-axis synchronous reactance `1.81` (default) | positive scalar

*d*-axis synchronous reactance. This parameter must
be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **q-axis synchronous reactance, Xq** — q-axis synchronous reactance `1.76` (default) | positive scalar

*q*-axis synchronous reactance. This parameter must
be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **d-axis transient reactance, Xd'** — d-axis transient reactance `0.3` (default) | positive scalar

*d*-axis transient reactance. This parameter must be
greater than 0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **d-axis subtransient reactance, Xd''** — d-axis subtransient reactance `0.23` (default) | positive scalar

*d*-axis subtransient reactance. This parameter must
be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify
parameterization by** parameter is set to
`Standard parameters`.

### **q-axis subtransient reactance, Xq''** — q-axis subtransient reactance `0.25` (default) | positive scalar

*q*-axis subtransient reactance. This parameter must
be greater than 0.

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
This parameter must be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify d-axis
transient time constant** parameter is set to
`Open circuit`.

### **d-axis subtransient short-circuit, Td''** — d-axis subtransient short-circuit `0.0230` `s` (default) | positive scalar

*d*-axis subtransient short-circuit time constant.
This parameter must be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify d-axis
transient time constant** parameter is set to
`Short circuit`.

### **Specify q-axis time constant** — Specify q-axis time constant `Open circuit` (default) | `Short circuit`

Select between `Open circuit` and
`Short circuit`.

The setting for this parameter affects the visibility of the
*q*-axis time constant parameters.

### **q-axis subtransient open-circuit, Tq0''** — q-axis subtransient open-circuit `0.07` `s` (default) | positive scalar

*q*-axis subtransient open-circuit time constant.
This parameter must be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify q-axis
transient time constant** parameter is set to
`Open circuit`.

### **q-axis subtransient short-circuit, Tq''** — q-axis subtransient short-circuit `0.0269` `s` (default) | positive scalar

*q*-axis subtransient short-circuit time constant.
This parameter must be greater than 0.

#### Dependencies

This parameter is visible only if the **Specify q-axis
transient time constant** parameter is set to
`Short circuit`.

### Initial Conditions

### **Initialization option** — Initialization option `Set real power, reactive power, terminal voltage, and terminal phase` (default) | `Set targets for rotor angle and Park's transform variables` | `Set targets for load flow variables`

Model for specifying values for certain parameters and variables at
the start of simulation. To:

Set an operating point regardless of the connected network,
select `Set real power, reactive power, terminal
voltage and terminal phase`.

- Specify the priority and initial target values for block
  variables before simulation using the
  **Variables** settings, select
  `Set targets for rotor angle and Park's
  transform variables`. For more information,
  see Set Priority and Initial Target for Block Variables.
- Select a bus type and specify the related parameters for a
  load-flow analysis in the **Initial
  Conditions** settings, select `Set
  targets for load flow variables`.

#### Dependencies

If you set this parameter to:

- `Set targets for rotor angle and Park's
  transform variables` — The
  **Variables** settings become
  visible.
- `Set real power, reactive power, terminal
  voltage, and terminal phase` — Related
  parameters become visible.
- `Set targets for load flow
  variables` — Related parameters become
  visible.

### **Source type** — Voltage source model `Swing bus` (default) | `Voltage source with series impedance` | `PV bus` | `PQ bus`

Type of voltage source that the block models.

#### Dependencies

This parameter is visible only if the **Initialization
option** parameter is set to `Set targets
for load flow variables` and the **Source
type** parameter is set to `Swing
bus` or `PV bus`.

The visibility of **Terminal voltage magnitude**,
**Terminal voltage angle**, **Active
power generated**, **Reactive power
generated**, **Minimum terminal voltage
magnitude (pu**, **Phase search range at
terminals**, and **Phase search range at
terminals** depend on the value that you choose for
this parameter.

### **Terminal voltage magnitude** — Terminal voltage magnitude `24e3` `V` (default)

Terminal voltage magnitude.

#### Dependencies

This parameter is visible only if the **Initialization
option** parameter is set to `Set real
power, reactive power, terminal voltage, and terminal
phase` or if the **Initialization
option** parameter is set to `Set targets
for load flow variables` and the **Source
type** parameter is set to `Swing
bus` or `PV bus`.

### **Terminal voltage angle** — Terminal voltage angle `0` `deg` (default)

Terminal voltage angle.

#### Dependencies

This parameter is visible only if the **Initialization
option** parameter is set to `Set real
power, reactive power, terminal voltage, and terminal
phase` or if the **Initialization
option** parameter is set to `Set targets
for load flow variables` and the **Source
type** parameter is set to `Swing
bus`.

### **Active power generated** — Active power generated `500e6` `V*A` (default)

Active power generated.

#### Dependencies

This parameter is visible only if the **Initialization
option** parameter is set to `Set real
power, reactive power, terminal voltage, and terminal
phase` or if the **Initialization
option** parameter is set to `Set targets
for load flow variables` and the **Source
type** parameter is set to `PV
bus` or `PQ bus`.

### **Reactive power generated** — Reactive power generated `0` `V*A` (default)

Reactive power generated.

#### Dependencies

This parameter is visible only if the **Initialization
option** parameter is set to `Set real
power, reactive power, terminal voltage, and terminal
phase` or if the **Initialization
option** parameter is set to `Set targets
for load flow variables` and the **Source
type** parameter is set to `PQ
bus`.

### **Minimum terminal voltage magnitude (pu)** — Minimum terminal voltage magnitude `0.95` (default)

Per-unit minimum steady-state voltage magnitude.

#### Dependencies

This parameter is visible only if the **Initialization
option** parameter is set to `Set targets
for load flow variables` and the **Source
type** parameter is set to `PQ
bus`.

### **Phase search range at terminals** — Phase search range at terminals `[-inf, inf]` `deg` (default)

Vector that defines the phase angle search range.

#### Dependencies

This parameter is visible only if the **Initialization
option** parameter is set to `Set targets
for load flow variables` and the **Source
type** parameter is set to `PV
bus` or `PQ bus`.

### **Parasitic conductance to electrical reference** — Parasitic conductance to electrical reference `1e-6` `S` (default)

Parasitic conductance to the electrical reference.

#### Dependencies

This parameter is visible only if the **Initialization
option** parameter is set to `Set targets
for load flow variables`.

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

**Introduced in R2015a**

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

Synchronous machine with simplified transformation, simplified representation, and fundamental or standard parameterization

The Synchronous Machine Model 2.1 block models a
synchronous machine with one field winding and one damper on the
*d*-axis and one damper on the *q*-axis. You use
fundamental or standard parameters to define the characteristics of the machine. This
block contains a *d**q* Park transformation, so use it
only for balanced operation.

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

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)].

The Park transformation is used to define the per-unit synchronous machine
equations. The stator voltage equations are defined by

ed=ed"−Raid+xq"iq

and

eq=eq"−xd"id−Raiq,

where:

- *e”d* and
  *e”q* are the
  *d*-axis and *q*-axis voltages
  behind subtransient reactances.
- *Ra* is the stator
  resistance.
- *id* and
  *iq* are the
  *d*-axis and *q*-axis stator
  currents, defined by

  [idiq]=Ps[iaibic].

  *ia*,
  *ib*, and
  *ic* are the stator
  currents flowing from port ~ to port n.
- *x”d* and
  *x”q* are the
  *d*-axis and *q*-axis subtransient
  reactances.

- *ed* and
  *eq* are the
  *d*-axis and *q*-axis stator
  voltages, defined by

  [edeq]=Ps[vavbvc].

  *va*,
  *vb*, and
  *vc* are the stator
  voltages measured from port ~ to neutral port n.

The rotor voltage equation is defined by

efd=Rfd⋅ifd,

where:

- *Rfd* is the resistance of
  rotor field circuit.
- *ifd* is the per-unit field
  current using the synchronous machine model reciprocal per-unit
  system.
- *efd* is the per-unit field
  voltage using the synchronous machine model reciprocal per-unit
  system.

The voltage-behind-transient-reactance equations are defined by

ded"dt=(xq−xq")iq−ed"Tq0",

deq'dt=Efd−(xd−xd')id−eq'Td0',

and

deq"dt=eq'−(xd'−xd")id−eq"Td0",

where:

- *xd* and
  *xq* are the
  *d*-axis and *q*-axis synchronous
  reactances.
- *T”d0* and
  *T”q0* are the
  *d*-axis and *q*-axis subtransient
  open-circuit time constants.
- *Efd* is the per-unit field
  voltage using the exciter model nonreciprocal per-unit system.
- *x’d* is the
  *d*-axis transient reactance.
- *e’q* is the
  *q*-axis voltage behind transient reactance.
- *T’d0* is the
  *d*-axis transient open-circuit time
  constant.

The rotor torque is defined by

Te=ed"id+eq"iq−(xd"−xq")idiq.

These defining equations do not describe the parameters you can set in the dialog
box. To see their relationship with the equation coefficients, see the book of P.
Kundur about understanding, modeling, analyzing, and mitigating power system
stability and control problems [1].

### Display Options

You can perform display actions using the **Electrical**
menu on the block context menu.

Right-click the block and, from the **Electrical** menu, select an option:

- **Display Base Values** displays the machine
  per-unit base values in the MATLAB® Command Window.
- **Display Associated Base Values** displays
  associated per-unit base values in the MATLAB Command Window.
- **Display Associated Initial Conditions** displays
  associated initial conditions in the MATLAB Command Window.

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
