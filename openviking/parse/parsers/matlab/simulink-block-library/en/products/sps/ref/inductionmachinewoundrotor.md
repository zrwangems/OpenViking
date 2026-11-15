---
type: simulink-block
title: 'Induction Machine Wound Rotor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Asynchronous\u200b'
documentation_page: 'inductionmachinewoundrotor'
documentation_source_path: 'ref/inductionmachinewoundrotor.html'
language: en
---

# Induction Machine Wound Rotor

## Ports

### Output

### **pu** — Per-unit measurements output port physical

Physical signal vector port associated with the machine per-unit
measurements. The vector elements are:

- *pu\_torque*
- *pu\_velocity*
- *pu\_vds*
- *pu\_vqs*
- *pu\_v0s*
- *pu\_ids*
- *pu\_iqs*
- *pu\_i0s*
### Conserving

### **R** — Machine rotor mechanical

Mechanical rotational conserving port associated with the machine
rotor.

### **C** — Machine case mechanical

Mechanical rotational conserving port associated with the machine
case.

### **~1** — Stator positive-end connections electrical

Expandable three-phase
port associated with the stator positive-end
connections.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **~2** — Stator negative-end connections electrical

Expandable three-phase
port associated with the stator negative-end
connections.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **~1r'** — Rotor positive-end connections electrical

Expandable three-phase
port associated with the rotor positive-end
connections.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **~2r'** — Rotor negative-end connections electrical

Expandable three-phase
port associated with the rotor negative-end
connections.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **a1** — *a* stator positive-end connection electrical

Electrical conserving port associated with *a* stator
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b1** — *b* stator positive-end connection electrical

Electrical conserving port associated with *b* stator
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c1** — *c* stator positive-end connection electrical

Electrical conserving port associated with *c* stator
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **a2** — *a* stator negative-end connection electrical

Electrical conserving port associated with *a* stator
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b2** — *b* stator negative-end connection electrical

Electrical conserving port associated with *b* stator
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c2** — *c* negative-end connection electrical

Electrical conserving port associated with *c* stator
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **a1r'** — *a* rotor positive-end connection electrical

Electrical conserving port associated with *a* rotor
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b1r'** — *b* rotor positive-end connection electrical

Electrical conserving port associated with *b* rotor
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c1r'** — *c* rotor positive-end connection electrical

Electrical conserving port associated with *c* rotor
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **a2r'** — *a* rotor negative-end connection electrical

Electrical conserving port associated with *a* rotor
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b2r'** — *b* rotor negative-end connection electrical

Electrical conserving port associated with *b* rotor
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c2r'** — *c* rotor-end connection electrical

Electrical conserving port associated with *c* rotor
negative-end connection.

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

### **HAr** — *a*-phase terminal thermal port thermal

Thermal conserving port associated with rotor winding
*a*.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HBr** — *b*-phase terminal thermal port thermal

Thermal conserving port associated with rotor winding
*b*.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HCr** — *c*-phase terminal thermal port thermal

Thermal conserving port associated with rotor winding
*c*.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

All default parameter values are based on a machine delta-winding
configuration.

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of generated heat and motor temperature.

### Main

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Rated apparent power** — Rated apparent power `15e3` `V*A` (default)

Rated apparent power of the induction machine.

### **Rated voltage** — RMS voltage `220` `V` (default)

RMS line-line voltage.

### **Rated electrical frequency** — Nominal electrical frequency `60` `Hz` (default)

Nominal electrical frequency corresponding to the rated apparent
power.

### **Number of pole pairs** — Machine pole pairs `1` (default)

Number of machine pole pairs.

### **Parameterization unit** — Unit system for block parameterization `SI` (default) | `Per unit`

Unit system for block parameterization. Choose between
`SI`, the international system of units,
and `Per unit`, the per-unit system.

#### Dependencies

Selecting:

- `SI` exposes SI parameters in
  the **Impedances** and
  **Saturation** settings.
- `Per unit` exposes per-unit
  parameters in the **Impedances** and
  **Saturation** settings.

### **Zero sequence** — Zero sequence `Include` (default) | `Exclude`

Zero-sequence model:

- `Include` — Prioritize model
  fidelity. An error occurs if you Include zero-sequence terms
  for simulations that use the Partitioning solver. For more
  information, see Increase Simulation Speed Using the Partitioning Solver.
- `Exclude` — Prioritize simulation
  speed for desktop simulation or real-time deployment.

#### Dependencies

If this parameter is set to:

- `Include` and
  **Parameterization unit** is set to
  `SI` — The **Stator
  zero-sequence reactance, X0** parameter in
  the **Impedances** settings is
  visible.
- `Include` and
  **Parameterization unit** is set to
  `Per unit` — The
  **Stator zero-sequence inductance, L0
  (pu)** parameter in the
  **Impedances** settings is
  visible.
- `Exclude` — The stator
  zero-sequence parameter in the
  **Impedances** settings is not
  visible.

### **Initialization option** — Initialization method `Set targets for flux variables` (default) | `Set targets for load flow variables`

Initialization method. You can initialize a machine for steady-state simulation using
either flux data or data from a load-flow analysis.

If you select
`Set targets for load flow variables`, to fully specify the initial
condition, you must include an initialization constraint in the form of a high-priority target
value. For example, if your induction machine is connected to an Inertia block, the initial condition for the induction machine is
completely specified if, in the **Initial Targets** section of the
Inertia block, the
**Priority** for **Rotational velocity** is set to
`High`. Alternatively, you could set the
**Priority** to `None` for the Inertia block **Rotational velocity**, and instead set the
**Priority** for the induction machine block **Slip**,
**Real power generated**, or **Mechanical power consumed**
to `High`.

#### Dependencies

The type of
variables that are visible in the **Initial Targets** section depends on the
initialization method that you select, in the **Main** section, for the
**Initialization option** parameter. To specify target values using:

- Flux variables — Set the **Initialization option** parameter to
  `Set targets for flux variables`.
- Data from a load-flow analysis — Set the **Initialization
  option** parameter to `Set targets for load flow
  variables`.

### Impedances

For the **Parameterization unit** parameter in the
**Main** settings, select `SI` to
expose SI parameters or `Per unit` to expose per-unit
parameters.

### **Stator resistance, Rs** — Stator resistance `0.25` `Ohm` (default)

Stator resistance.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to
`SI`.

### **Stator leakage reactance, Xls** — Stator leakage reactance `0.4` `Ohm` (default)

Stator leakage reactance.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to
`SI`.

### **Referred rotor resistance, Rr'** — Referred rotor resistance `0.14` `Ohm` (default)

Rotor resistance referred to the stator.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to
`SI`.

### **Referred rotor leakage reactance, Xlr'** — Referred rotor leakage reactance `0.41` `Ohm` (default)

Rotor leakage reactance referred to the stator.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to
`SI`.

### **Magnetizing reactance, Xm** — Magnetizing reactance `17` `Ohm` (default)

Magnetizing reactance.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to
`SI`.

### **Stator zero-sequence reactance, X0** — Stator zero-sequence reactance `0.4` `Ohm` (default)

Stator zero-sequence reactance.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to
`SI`.

### **Stator resistance, Rs (pu)** — Per-unit stator resistance `0.0258` (default)

Per-unit stator resistance.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to `Per
unit`.

### **Stator leakage inductance, Lls (pu)** — Per-unit stator leakage inductance `0.0413` (default)

Per-unit stator leakage inductance.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to `Per
unit`.

### **Referred rotor resistance, Rr' (pu)** — Per-unit referred rotor resistance `0.0145` (default)

Per-unit rotor resistance referred to the stator.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to `Per
unit`.

### **Referred rotor leakage inductance, Llr' (pu)** — Per-unit referred rotor leakage inductance `0.0424` (default)

Per-unit rotor leakage inductance referred to the stator.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to `Per
unit`.

### **Magnetizing inductance, Lm (pu)** — Per-unit magnetizing inductance `1.7562` (default)

Per-unit magnetizing inductance, that is, the peak value of
stator-rotor mutual inductance.

#### Dependencies

This parameter is visible only if you set the
**Parameterization unit** parameter in the
**Main** setting to `Per
unit`.

### **Stator zero-sequence inductance, L0 (pu)** — Per-unit stator zero-sequence inductance `0.0413` (default)

Per-unit stator zero-sequence inductance.

#### Dependencies

This parameter is visible only if, in the
**Main** settings, the
**Parameterization unit** parameter is set to
`Per unit` and the **Zero
sequence** parameter is set to
`Include`.

### Saturation

For the **Parameterization unit** parameter in the **Main**
settings, select `SI` to expose SI parameters or `Per
unit` to expose per-unit parameters.

The saturation characteristic is based on the machine being connected in a delta-winding
configuration.

### **Magnetic saturation representation** — Magnetic saturation representation `None` (default) | `Open-circuit lookup table (v versus i)`

Block magnetic saturation representation.

#### Dependencies

If this parameter is set to `Open-circuit lookup table (v
versus i)`, related parameters are visible.

### **No-load line current saturation data, i (rms)** — No-load line RMS current saturation data `[0, 4, 9, 18, 25, 34, 50, 68, 95, 120]` `A` (default)

Current *i* data populates the voltage *v*
versus field current *i* lookup table. This parameter must
contain a vector with at least 10 elements.

#### Dependencies

This parameter is visible only if the **Magnetic saturation
representation** parameter is set to `Open-circuit
lookup table (v versus i)` and, in the
**Main** settings, the **Parameterization
unit** parameter is set to
`SI`.

### **Terminal voltage saturation data, v (phase-phase, rms)** — Terminal RMS voltage saturation data `[0, 88, 154, 198, 220, 242, 264, 286, 308, 327]` `V` (default)

Terminal voltage *v* data populates the voltage
*v* versus current *i* lookup table. This
parameter must contain a vector with at least 10 elements. The number of
elements must match the number of elements in the vector for the
**No-load line current saturation data, i (rms)**
parameter.

#### Dependencies

This parameter is visible only if the **Magnetic saturation
representation** parameter is set to `Open-circuit
lookup table (v versus i)` and, in the
**Main** settings, the **Parameterization
unit** parameter is set to
`SI`.

### **Per-unit no-load line current saturation data, i** — Per-unit no-load line current saturation data `[0, .176, .396, .792, 1.1, 1.496, 2.2, 2.992, 4.18, 5.28]` (default)

Current *i* data populates the voltage *v*
versus field current *i* lookup table. This parameter must
contain a vector with at least 10 elements.

#### Dependencies

This parameter is visible only if the **Magnetic saturation
representation** parameter is set to `Open-circuit
lookup table (v versus i)` and, in the
**Main** settings, the **Parameterization
unit** parameter is set to `Per
unit`.

### **Per-unit terminal voltage saturation data, v** — Per-unit terminal voltage saturation data `[0, .4, .7, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.4864]` (default)

Terminal voltage *v* data populates the voltage
*v* versus current *i* lookup table. This
parameter must contain a vector with at least 10 elements. The number of
elements must match the number of elements in the vector for the
**Per-unit no-load line current saturation data, i**
parameter.

#### Dependencies

This parameter is visible only if the **Magnetic saturation
representation** parameter is set to `Open-circuit
lookup table (v versus i)` and, in the
**Main** settings, the **Parameterization
unit** parameter is set to `Per
unit`.

### Thermal

These parameters appear only for blocks with exposed thermal ports.

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

Simscape / Electrical / Electromechanical / Asynchronous

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

### R2020a: Saturation characteristic update

From R2020a forward, for the saturation characteristic, the
Induction Machine Wound Rotor block takes into
account the magnetic flux due to the leakage inductance.

The default values for these parameters have changed:

- **Stator leakage reactance, Xls**
- **Stator zero-sequence reactance, X0**
- **Stator leakage inductance, Lls (pu)**
- **Stator zero-sequence inductance, L0 (pu)**
- **Terminal voltage saturation data, v (phase-phase,
  rms)**
- **Per-unit terminal voltage saturation data,
  v**

As a result of these changes, inside a model saved in an earlier release, if you
have used the Induction Machine Wound Rotor block
with saturation enabled, review the saturation data.

## Description

Wound-rotor induction machine with per-unit or SI parameterization

The Induction Machine Wound Rotor block models a wound-rotor
asynchronous machine with fundamental parameters expressed in per-unit or in the
International System of Units (SI). A wound-rotor asynchronous machine is a type of
induction machine. All stator and rotor connections are accessible on the block.
Therefore, you can model soft-start regimes using a switch between wye and delta
configurations or by increasing rotor resistance. If you do not need access to the rotor
windings, use the Induction Machine Squirrel Cage block
instead.

Connect port **~1** to a three-phase circuit. To connect the stator
in delta configuration, connect a Phase Permute block between ports
**~1** and **~2**. To connect the stator in wye
configuration, connect port **~2** to a Grounded Neutral
or a Floating Neutral block. If you do not need to vary rotor resistance,
connect rotor port **~1r'** to a Floating Neutral block
and rotor port **~2r'** to a Grounded Neutral
block.

The rotor circuit is referred to the stator. Therefore, when you use the block in a
circuit, refer any additional circuit parameters to the stator.

### Induction Machine Initialization Using Load-Flow Target Values

If the block is in a network that is compatible with the
frequency-time simulation mode, you can perform a load-flow analysis on the network. A
load-flow analysis provides steady-state values that you can use to initialize the
machine.

For more information, see Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode. For an example that shows how initialize an
induction machine using data from a load flow analysis, see Induction Motor Initialization with Loadflow.

### Equations

For the SI implementation, the block converts the SI values that you enter to
per-unit values for simulation. The converted values are based on the machine being
connected in a delta-winding configuration.

For the per-unit implementation, you must specify the resistances and inductances
in the impedances tab based on the machine being connected in a delta-winding
configuration.

For information on the relationship between SI and per-unit machine parameters,
see Per-Unit Conversion for Machine Parameters. For information on per-unit parameterization, see Per-Unit System of Units.

The asynchronous machine equations are expressed with respect to a synchronous
reference frame, defined by

θe(t)=∫0t2πfrateddt,

where *frated* is the value of the
**Rated electrical frequency** parameter.

The Park transformation maps stator equations to a reference frame that is
stationary with respect to the rated electrical frequency. The Park transformation
is defined by

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212],

where *θe* is the
electrical angle.

The rotor equations are mapped to another reference frame, defined by the
difference between the electrical angle and the product of rotor angle
θr and number of pole pairs N:

Pr=23[cos(θe−Nθr)cos(θe−Nθr−2π3)cos(θe−Nθr+2π3)−sin(θe−Nθr)−sin(θe−Nθr−2π3)−sin(θe−Nθr+2π3)121212].

The Park transformation is used to define the per-unit asynchronous machine
equations. The stator voltage equations are defined by

vds=1ωbasedψdsdt−ωψqs+Rsids,

vqs=1ωbasedψqsdt+ωψds+Rsiqs,

and

v0s=1ωbasedψ0sdt+Rsi0s,

where:

- *vds*,
  *vqs*, and
  *v0s* are the
  *d*-axis, *q*-axis, and zero-sequence
  stator voltages, defined by

  [vdsvqsv0s]=Ps[vavbvc].

  *va*,
  *vb*, and
  *vc* are the stator voltages
  across ports **~1** and **~2**.
- *ωbase* is the per-unit base
  electrical speed.
- *ψds*,
  *ψqs*, and
  *ψ0s* are the
  *d*-axis, *q*-axis, and zero-sequence
  stator flux linkages.
- *Rs* is the stator
  resistance.
- *ids*,
  *iqs*, and
  *i0s* are the
  *d*-axis, *q*-axis, and zero-sequence
  stator currents, defined by

  [idsiqsi0s]=Ps[iaibic].

  *ia*,
  *ib*, and
  *ic* are the stator currents
  flowing from port **~1** to port
  **~2**.

The rotor voltage equations are defined by

vdr=1ωbasedψdrdt−(ω−ωr)ψqr+Rrdidr,

vqr=1ωbasedψqrdt+(ω−ωr)ψdr+Rrdiqr,

and

v0r=1ωbasedψ0rdt+Rrdi0s,

where:

- *vdr*,
  *vqr*, and
  *v0r* are the
  *d*-axis, *q*-axis, and zero-sequence
  rotor voltages, defined by

  [vdrvqrv0r]=Pr[varvbrvcr].

  *var*,
  *vbr*, and
  *vcr* are the rotor voltages
  across ports **~1r'** and **~2r'**.
- *ψdr*,
  *ψqr*, and
  *ψ0r* are the
  *d*-axis, *q*-axis, and zero-sequence
  rotor flux linkages.
- *ω* is the per-unit synchronous speed. For a synchronous
  reference frame, the value is 1.
- *ωr* is the per-unit mechanical
  rotational speed.
- *Rrd* is the rotor resistance
  referred to the stator.
- *idr*,
  *iqr*, and
  *i0r* are the
  *d*-axis, *q*-axis, and zero-sequence
  rotor currents, defined by

  [idriqri0r]=Pr[iaribricr].

  *iar*,
  *ibr*, and
  *icr* are the rotor currents
  flowing from port **~1r'** to port
  **~2r'**.

The stator flux linkage equations are defined by

ψds=Lssids+Lmidr,

ψqs=Lssiqs+Lmiqr,

and

ψ0s=Lssi0s,

where *Lss* is the stator self-inductance
and *Lm* is the magnetizing
inductance.

The rotor flux linkage equations are defined by

ψdr=Lrrdidr+Lmids

ψqr=Lrrdiqr+Lmiqs,

and

ψ0r=Lrrdi0r,

where *Lrrd* is the rotor self-inductance
referred to the stator.

The rotor torque is defined by

T=ψdsiqs−ψqsids.

The stator self-inductance *Lss*, stator
leakage inductance *Lls*, and magnetizing
inductance *Lm* are related by

Lss=Lls+Lm.

The rotor self-inductance *Lrrd*, rotor
leakage inductance *Llrd*, and magnetizing
inductance *Lm* are related by

Lrrd=Llrd+Lm.

When a saturation curve is provided, the equations to determine the saturated
magnetizing inductance as a function of magnetizing flux are:

Lm\_sat=f(ψm)

ψm=ψdm2+ψqm2

For no saturation, the equation reduces to

Lm\_sat=Lm

### Plotting and Display Options

You can perform plotting and display actions using the
**Electrical** menu on the block context menu.

Right-click the block and, from the **Electrical** menu,
select an option:

- **Display Base Values** — Displays the machine
  per-unit base values in the MATLAB® Command Window.
- **Plot Torque Speed (SI)** — Plots torque versus
  speed, both measured in SI units, in a MATLAB figure window using the current machine parameters.
- **Plot Torque Speed (pu)** — Plots torque versus
  speed, both measured in per-unit, in a MATLAB figure window using the current machine parameters.
- **Plot Open-Circuit Saturation** — Plots terminal
  voltage versus no-load line current, both in per-unit, in a MATLAB figure window. The plot contains three traces:

  - Unsaturated — Stator magnetizing inductance
    (unsaturated).
  - Saturated — Open-circuit lookup table (*v*
    versus *i*) you specify.
  - Derived — Open-circuit lookup table derived from the per-unit
    open-circuit lookup table (*v* versus
    *i*) you specify. This data is used to
    calculate the saturated magnetizing inductance,
    *Lm\_sat*, and
    the saturation factor,
    *Ks*, versus
    magnetic flux linkage,
    *ψm*,
    characteristics.
- **Plot Saturation Factor** — Plots saturation
  factor, *Ks*, versus magnetic flux
  linkage, *ψm*, in a MATLAB figure window using the machine parameters. This parameter is
  derived from other parameters that you specify:

  - No-load line current saturation data,
    *i*
  - Terminal voltage saturation data, *v*
  - Leakage inductance,
    *Lls*
- **Plot Saturated Inductance** — Plots magnetizing
  inductance, *Lm\_sat*, versus
  magnetic flux linkage, *ψm*, in a
  MATLAB figure window using the machine parameters. This parameter is
  derived from other parameters that you specify:

  - No-load line current saturation data,
    *i*
  - Terminal voltage saturation data, *v*
  - Leakage inductance,
    *Lls*

For the SI implementation, *v* is in V (phase-phase RMS) and
*i* is in A (rms).

### Model Thermal Effects

You can expose thermal ports to simulate the effects of generated heat and motor temperature. To expose the thermal ports and the **Thermal** parameters, set the **Modeling option** parameter to either:

- `No thermal port` — The block contains electrical conserving ports associated with the stator windings, but does not contain thermal ports.
- `Show thermal port` — The block contains expanded electrical conserving ports associated with the stator windings and thermal conserving ports for each of the windings and for the rotor.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

The type of
variables that are visible in the **Initial Targets** section depends on the
initialization method that you select, in the **Main** section, for the
**Initialization option** parameter. To specify target values using:

- Flux variables — Set the **Initialization option** parameter to
  `Set targets for flux variables`.
- Data from a load-flow analysis — Set the **Initialization
  option** parameter to `Set targets for load flow
  variables`.

If you select
`Set targets for load flow variables`, to fully specify the initial
condition, you must include an initialization constraint in the form of a high-priority target
value. For example, if your induction machine is connected to an Inertia block, the initial condition for the induction machine is
completely specified if, in the **Initial Targets** section of the
Inertia block, the
**Priority** for **Rotational velocity** is set to
`High`. Alternatively, you could set the
**Priority** to `None` for the Inertia block **Rotational velocity**, and instead set the
**Priority** for the induction machine block **Slip**,
**Real power generated**, or **Mechanical power consumed**
to `High`.
