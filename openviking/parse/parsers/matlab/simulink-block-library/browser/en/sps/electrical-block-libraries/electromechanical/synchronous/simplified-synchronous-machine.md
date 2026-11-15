---
type: simulink-block
title: 'Simplified Synchronous Machine'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Synchronous'
documentation_page: 'simplifiedsynchronousmachine'
documentation_source_path: 'ref/simplifiedsynchronousmachine.html'
language: en
---

# Simplified Synchronous Machine

## Ports

### Input

### **E\_si** — Amplitude of internal generated voltage (phase-to-neutral) vector of physical signals

Physical signal port associated with the amplitude of the internal
generated voltage (phase-to-neutral), specified as a vector of physical
signals.

#### Dependencies

To enable this port, set **Parameterization
unit** to `SI`.

### **E\_pu** — Amplitude of internal generated voltage, in per-unit vector of physical signals

Physical signal port associated with the per-unit amplitude of the
internal generated voltage, specified as a vector of physical
signals.

#### Dependencies

To enable this port, set **Parameterization
unit** to `Per unit`.
### Output

### **o** — Machine per-unit measurements vector of physical signals

Physical signal port associated with the machine per-unit
measurements, returned as a vector of physical signals. The vector
elements are:

- Electromotive force associated with phase a,
  *pu\_EMF(1)*
- Electromotive force associated with phase b,
  *pu\_EMF(2)*
- Electromotive force associated with phase c,
  *pu\_EMF(3)*
- Electrical torque, *pu\_torque*
- Rotor velocity, *pu\_velocity*
- Stator `d`-axis voltage,
  *pu\_vd*
- Stator `q`-axis voltage,
  *pu\_vq*
- Stator zero-sequence voltage,
  *pu\_e0*
- Stator `d`-axis current,
  *pu\_id*
- Stator `q`-axis current,
  *pu\_iq*
- Stator zero-sequence current,
  *pu\_i0*
- Rotor electrical angle,
  *electrical\_angle\_out*

To connect to this port, use the Synchronous Machine Measurement block.
### Conserving

### **R** — Machine rotor mechanical rotational

Mechanical rotational conserving port associated with the machine
rotor.

### **C** — Machine case mechanical rotational

Mechanical rotational conserving port associated with the machine
case.

### **~** — Stator windings electrical

Expandable three-phase
electrical port associated with the stator windings.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **n** — Neutral phase electrical

Electrical conserving port associated with the neutral point of the
wye winding configuration.

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

### **Rated apparent power** — Rated apparent power `555e6` `V*A` (default) | scalar

Rated apparent power.

### **Rated voltage** — RMS rated line-to-line voltage `24e3` `V` (default) | scalar

RMS rated line-to-line voltage.

### **Rated electrical frequency** — Nominal electrical frequency `60` `Hz` (default) | scalar

Nominal electrical frequency at which rated apparent power is
quoted.

### **Number of pole pairs** — Number of pole pairs `2` (default) | scalar

Number of machine pole pairs.

### **Parameterization unit** — Block parameterization `SI` (default) | `Per unit`

Block parameterization method. Options are:

- `SI`
- `Per unit`

### **Internal resistance (pu)** — Internal per-unit resistance `0.05` (default) | scalar

Internal per-unit resistance.

#### Dependencies

To enable this parameter, set **Parameterization
unit** to `Per unit`.

### **Internal inductance (pu)** — Internal per-unit inductance `0.3` (default) | scalar

Internal per-unit inductance in per-unit.

#### Dependencies

To enable this parameter, set **Parameterization
unit** to `Per unit`.

### **Internal resistance** — Internal resistance `0.0519` `Ohm` (default) | scalar

Internal resistance.

#### Dependencies

To enable this parameter, set **Parameterization
unit** to `SI`.

### **Internal inductance** — Internal inductance `8.2589e-04` `H` (default) | scalar

Internal inductance.

#### Dependencies

To enable this parameter, set **Parameterization
unit** to `SI`.

### Initial Conditions

### **Initialization option** — Initialization option `Set real power, reactive power, terminal voltage, and terminal phase` (default) | `Set targets for rotor angle and Park's transform variables` | `Set targets for load flow variables`

Model for specifying values for certain parameters and variables at
the start of simulation. To:

- Set an operating point regardless of the connected
  network, select `Set real power, reactive power,
  terminal voltage and terminal
  phase`.
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

### **Source type** — Voltage source model `Swing bus` (default) | `PV bus` | `PQ bus`

Type of voltage source that the block models.

#### Dependencies

To enable this parameter set **Initialization
option** to `Set targets for load flow
variables` and **Source type** to
`Swing bus` or `PV
bus`.

### **Terminal voltage magnitude** — Terminal voltage magnitude `24e3` `V` (default)

Terminal voltage magnitude.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal phase` or
**Initialization option** to `Set
targets for load flow variables` and
**Source type** to `Swing
bus` or `PV bus`.

### **Terminal voltage angle** — Terminal voltage angle `0` `deg` (default)

Terminal voltage angle.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal phase` or
**Initialization option** to `Set
targets for load flow variables` and
**Source type** to `Swing
bus`.

### **Active power generated** — Active power generated `500e6` `V*A` (default)

Active power generated.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal phase` or
**Initialization option** to `Set
targets for load flow variables` and
**Source type** to `PV
bus` or `PQ bus`.

### **Reactive power generated** — Reactive power generated `0` `V*A` (default)

Reactive power generated.

#### Dependencies

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal phase` or
**Initialization option** to `Set
targets for load flow variables` and
**Source type** to `PQ
bus`.

### **Minimum terminal voltage magnitude (pu)** — Minimum terminal voltage magnitude `0.95` (default)

Per-unit minimum steady-state voltage magnitude.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set targets for load flow
variables` and **Source type** to
`PQ bus`.

### **Phase search range at terminals** — Phase search range at terminals `[-inf, inf]` `deg` (default)

Vector that defines the phase angle search range.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set targets for load flow
variables` and **Source type** to
`PV bus` or `PQ
bus`.

### **Parasitic conductance to electrical reference** — Parasitic conductance to electrical reference `1e-6` `S` (default)

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

**Introduced in R2020b**

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

Simplified synchronous machine with electromotive force

The Simplified Synchronous Machine block models a simplified
synchronous machine with a voltage source that represents electromotive force (EMF). You
can specify the internal resistance and inductance with per-unit or SI
parameters.

The equivalent circuits of the simplified synchronous machine for the direct axis, the
quadrature axis, and the zero sequence are:

### Equations

The simplified synchronous machine equations are expressed with respect to a rotating
reference frame, which is defined by:

θe(t)=Nθr(t),

where:

- *θe* is the electrical
  angle.
- *N* is the number of pole pairs.
- *θr* is the rotor
  angle.

The Park transformation maps the synchronous machine equations to the rotating reference
frame with respect to the electrical angle. The Park transformation is defined
by:

Ps=23[−cosθe−cos(θe−2π3)−cos(θe+2π3)sinθesin(θe−2π3)sin(θe+2π3)121212].

The Park transformation is used to define the per-unit simplified synchronous machine
equations. The voltage equations are defined by:

ed=1ωbasedψddt−Ψqωr+Rid+vd

eq=1ωbasedψqdt+Ψdωr+Riq+vq

e0=1ωbasedΨ0dt+Ri0+v0

where:

- *ed*,
  *eq*, and
  *e0* are the
  *d*-axis, *q*-axis, and
  zero-sequence voltages, defined by:

  [edeqe0]=Ps[eaebec].

  *ea*,
  *eb*, and
  *ec* are the per-unit
  internal voltage sources, defined by:

  ea=Epusinθeeb=Epusin(θe−120°)ec=Epusin(θe+120°)

  *epu* is the per-unit
  amplitude of the internal generated voltage.
- *vd*,
  *vq*, and
  *v0* are defined
  by:

  [vdvqv0]=Ps[vavbvc].

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
  zero-sequence flux linkages.
- *ωr* is the per-unit rotor
  rotational speed.
- *R* is the stator resistance.
- *id*,
  *iq*, and
  *i0* are the
  *d*-axis, *q*-axis, and
  zero-sequence stator currents, defined by:

  [idiqi0]=Ps[iaibic].

  *ia*,
  *ib*, and
  *ic* are the stator
  currents flowing out of port **~**.

The stator flux linkage equations are defined by

ψd=L⋅idψq=L⋅iqψ0=L⋅i0

where *L* is the stator leakage inductance.

The power equation of the simplified synchronous machine in per-unit is defined by:

P=edid+eqiq.

### Plotting and Display Options

You can perform plotting and display actions using the
**Electrical** menu on the block context menu.

Right-click the block and, from the **Electrical** menu, select one of these options:

- **Display Base Values** — Displays the machine
  per-unit base values in the MATLAB® Command Window.
- **Display Associated Initial Conditions** —
  Displays associated initial conditions in the MATLAB Command Window.

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
