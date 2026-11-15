---
type: simulink-block
title: 'Synchronous Machine (Six-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Synchronous'
documentation_page: 'synchronousmachinesixphase'
documentation_source_path: 'ref/synchronousmachinesixphase.html'
language: en
---

# Synchronous Machine (Six-Phase)

## Ports

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

### **~ABC** — Stator ABC windings electrical

Three-phase electrical port
associated with the stator ABC windings.

### **~XYZ** — Stator XYZ windings electrical

Three-phase electrical port
associated with the stator XYZ windings.

### **n1** — ABC winding neutral point electrical

Electrical conserving port associated with the neutral point of the
ABC winding configuration.

#### Dependencies

To enable this port, set **Zero sequence** to
`Include`.

### **n2** — XYZ winding neutral point electrical

Electrical conserving port associated with the neutral point of the
XYZ winding configuration.

#### Dependencies

To enable this port, set **Zero sequence** to
`Include`.

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

### **HX** — *x*-phase terminal thermal port thermal

Thermal conserving port associated with stator winding
*x*.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HY** — *y*-phase terminal thermal port thermal

Thermal conserving port associated with stator winding
*y*.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HZ** — *z*-phase terminal thermal port thermal

Thermal conserving port associated with stator winding
*z*.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HR** — Rotor thermal port thermal

Thermal conserving port associated with the rotor.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of losses that
convert power to heat.

### Main

### **Nominal power** — Nominal power `100e3` `V*A` (default) | scalar

Nominal power.

### **Nominal voltage (line-to-line,rms)** — Nominal root mean square voltage `240` `V` (default) | scalar

Nominal root mean square (RMS) line-to-line voltage.

### **Nominal electrical frequency** — Nominal electrical frequency `60` `Hz` (default) | scalar

Nominal electrical frequency at which the nominal power is
quoted.

### **Number of pole pairs** — Rotor pole pairs `2` (default) | positive scalar

Number of machine pole pairs.

### **Zero sequence** — Zero sequence model `Include` (default) | `Exclude`

Zero-sequence model with two options:

- `Include` — Prioritize
  model fidelity. An error occurs if you Include zero-sequence
  terms for simulations that use the Partitioning solver. For
  more information, see Increase Simulation Speed Using the Partitioning Solver.
- `Exclude` — Prioritize
  simulation speed for desktop simulation or real-time
  deployment.

### **Rotor angle definition** — Rotor angle reference point `Angle between the a-phase magnetic axis and the d-axis` (default) | `Angle between the a-phase magnetic axis and the q-axis`

Reference point for the rotor angle measurement. If you select the
default value, the rotor and *a*-phase fluxes are
aligned for a zero-rotor angle. Otherwise, an *a*-phase
current generates the maximum torque value for a zero-rotor angle.

### Impedances

### **Stator resistance, Rs** — Stator resistance `0.0288` (default) | positive scalar

Resistance of the stator. This parameter must be greater than
`0`.

### **Stator leakage inductance, Ll** — Stator leakage inductance `0.0969` (default) | positive scalar

Leakage inductance of the stator. This parameter must be greater than
`0`.

### **Stator d-axis mutual inductance, Lmd** — Stator *d*-axis mutual inductance `1.9583` (default) | positive scalar

*d*-axis mutual inductance of the stator. This
parameter must be greater than 0.

### **Stator q-axis mutual inductance, Lmq** — Stator *q*-axis mutual inductance `0.9045` (default) | positive scalar

*q*-axis mutual inductance of the stator. This
parameter must be greater than 0.

### **Rotor field winding resistance, Rfd'** — Rotor field winding resistance `0.0028` (default) | positive scalar

Resistance of the field winding of the rotor. This parameter must be
greater than 0.

### **Rotor field winding inductance, Llfd'** — Rotor field winding inductance `0.0813` (default) | positive scalar

Inductance of the field winding of the rotor. This parameter must be
greater than 0.

### **Rotor d-axis damper winding resistance, Rkd'** — Rotor *d*-axis damper winding resistance `0.0041` (default) | positive scalar

Resistance of the damper winding of the rotor in the
*d*-axis. This parameter must be greater than
0.

### **Rotor d-axis damper winding inductance, Llkd'** — Rotor *d*-axis damper winding inductance `0.0918` (default) | positive scalar

Inductance of the damper winding of the rotor in the
*d*-axis. This parameter must be greater than
0.

### **Rotor q-axis damper winding resistance, Rkq'** — Rotor *q*-axis damper winding resistance `0.0043` (default) | positive scalar

Resistance of the damper winding of the rotor in the
*q*-axis. This parameter must be greater than
0.

### **Rotor q-axis damper winding inductance, Llkq'** — Rotor *q*-axis damper winding inductance `0.1174` (default) | positive scalar

Inductance of the damper winding of the rotor in the
*q*-axis. This parameter must be greater than
0.

### Initial Conditions

### **Initialization option** — Initialization option `Set real power, reactive power, terminal voltage, and terminal phase` (default) | `Set targets for rotor angle and Park's transform variables`

Model for specifying values for certain parameters and variables at
the start of simulation:

- To set an operating point independent of the connected
  network, select `Set real power, reactive power,
  terminal voltage and terminal phase`.
- To specify the priority and initial target values for block
  variables before simulation using the **Variables** settings, select `Set
  targets for rotor angle and Park's transform
  variables`. For more information, see Set Priority and Initial Target for Block Variables.

### **Terminal voltage magnitude** — Terminal voltage magnitude `240` `V` (default) | scalar

Terminal voltage magnitude.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal
phase`.

### **Terminal voltage angle corresponding to ABC group** — Terminal voltage angle corresponding to ABC group `0` `deg` (default) | scalar

Terminal voltage angle corresponding to the ABC stator.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal
phase`.

### **Terminal active power (ABC group)** — ABC terminal active power `50e3` `V*A` (default) | scalar

Terminal active power generated by the stator ABC windings.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal
phase`.

### **Terminal reactive power (ABC group)** — ABC terminal reactive power `0` `V*A` (default) | scalar

Terminal reactive power generated by the stator ABC windings.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal
phase`.

### **Terminal active power (XYZ group)** — XYZ terminal active power `20e3` `V*A` (default) | scalar

Terminal active power generated by the stator XYZ windings.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal
phase`.

### **Terminal reactive power (XYZ group)** — XYZ terminal reactive power `0` `V*A` (default) | scalar

Terminal reactive power generated by the stator XYZ windings.

#### Dependencies

To enable this parameter, set **Initialization
option** to `Set real power, reactive
power, terminal voltage, and terminal
phase`.

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

## Description

Six-phase synchronous machine

The Synchronous Machine (Six-Phase) block models a six-phase
synchronous machine, also known as a dual-star machine.

A six-phase synchronous machine has two groups of stator windings: the ABC group and the XYZ
group. These two groups have a 30 degree phase shift.

The equivalent circuits of the six-phase synchronous machine for the direct axis, the
quadrature axis, and the two zero sequence are:

### Equations

The synchronous machine equations are expressed with respect to a synchronously rotating
reference frame, defined by:

θe(t)=Nθr(t)+x\_rotor\_offset,

where:

- *θe* is the rotor electrical
  angle.
- *N* is the number of pole pairs.
- *θr* is the rotor mechanical
  angle.
- *x\_rotor\_offset* is `0` if you
  define the rotor electrical angle with respect to the
  *d*-axis, or `-pi/2` if you define
  the rotor electrical angle with respect to the
  *q*-axis.

Two Park transformations map the synchronous machine equations to the rotating
reference frame with respect to the electrical angle. The Park transformation for
the first group of stator windings, the ABC group, is defined by:

Ps1=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212].

The Park transformation for the second group of stator windings, the XYZ group, is
defined by:

Ps2=23[cos(θe−π6)cos(θe−5π6)cos(θe+π2)−sin(θe−π6)−sin(θe−5π6)sin(θe+π2)121212].

The Park transformations are used to define the per-unit synchronous machine
equations.

The stator voltage equations for the ABC group are defined by:

vd1=Rsid1−ψq1ωr+1ωbasedψd1dt

vq1=Rsiq1+ψd1ωr+1ωbasedψq1dt

v01=Rsi01+1ωbasedψ01dt

where:

- *vd1*,
  *vq1*, and
  *v01* are the
  *d*-axis, *q*-axis, and
  zero-sequence ABC stator voltages, defined by:

  [vd1vq1v01]=Ps1[vavbvc].

  *va*,
  *vb*, and
  *vc* are the ABC stator
  voltages measured from port **~ABC** to neutral port
  **n1**.
- *ωbase* is the per-unit base
  electrical speed.
- *ψd1*,
  *ψq1*, and
  *ψ01* are the
  *d*-axis, *q*-axis, and
  zero-sequence stator flux linkages for the ABC group.
- *ωr* is the per-unit rotor
  rotational speed.
- *Rs* is the stator
  resistance.
- *id1*,
  *iq1*, and
  *i01* are the
  *d*-axis, *q*-axis, and
  zero-sequence ABC stator currents, defined by:

  [id1iq1i01]=Ps1[iAiBiC].

  *ia*,
  *ib*, and
  *ic* are the ABC stator
  currents flowing from port **~ABC** to port
  **n1**.

The stator voltage equations for the XYZ group are defined by:

vd2=Rsid2−ψq2ωr+1ωbasedψd2dt

vq2=Rsiq2+ψd2ωr+1ωbasedψq2dt

v02=Rsi02+1ωbasedψ02dt

where:

- *vd2*,
  *vq2*, and
  *v02* are the
  *d*-axis, *q*-axis, and
  zero-sequence XYZ stator voltages, defined by:

  [vd2vq2v02]=Ps2[vxvyvz].

  *vx*,
  *vy*, and
  *vz* are the XYZ stator
  voltages measured from port **~XYZ** to neutral port
  **n2**.
- *ψd2*,
  *ψq2*, and
  *ψ02* are the
  *d*-axis, *q*-axis, and
  zero-sequence stator flux linkages for the XYZ group.
- *id2*,
  *iq2*, and
  *i02* are the
  *d*-axis, *q*-axis, and
  zero-sequence XYZ stator currents, defined by:

  [id2iq2i02]=Ps2[iXiYiZ].

  *ix*,
  *iy*, and
  *iz* are the XYZ stator
  currents flowing from port **~XYZ** to port
  **n2**.

The rotor voltage equations are defined by:

v'fd=R'fdi'fd+1ωbasedψ'fddt

v'kd=R'kdi'kd+1ωbasedψ'kddt=0

v'kq=R'kqi'kq+1ωbasedψ'kqdt=0

where:

- *v'fd* is the field winding
  voltage referred to the stator side.
- *v'kd* and
  *v'kq* are the
  *dq*-axes damper winding voltages referred to the
  stator side. They are all equal to 0.
- *ψ'fd*,
  *ψ'kd*, and
  *ψ'kq* are the magnetic
  fluxes linking the field circuit, the *d*-axis damper
  winding, and the *q*-axis damper winding.
- *R'fd*,
  *R'kd*, and
  *R'kq* are the
  resistances of the rotor field circuit, *d*-axis damper
  winding, and *q*-axis damper winding.
- *i'fd*,
  *i'kd*, and
  *i'kq* are the field and
  *dq*-axes damper winding currents referred to the
  stator side.

The stator flux linkage equations are defined by:

ψd1=Llid1+Lmd(id1+id2+i′fd+i′kd)

ψq1=Lliq1+Lmq(iq1+iq2+i′kq)

ψ01=Lli01

ψd2=Llid2+Lmd(id1+id2+i′fd+i′kd)

ψq2=Lliq2+Lmq(iq1+iq2+i′kq)

ψ02=Lli02

where:

- *Ll* is the stator leakage
  inductance.
- *Lmd* and
  *Lmq* are the mutual
  inductances of the stator *d*-axis and
  *q*-axis.

The rotor flux linkage equations are defined by:

ψ'fd=L'lfdi'fd+Lmd(id1+id2+i′fd+i′kd)

ψ'kd=L'lkdi'kd+Lmd(id1+id2+i′fd+i′kd)

ψ'kq=L'lkqi'kq+Lmq(iq1+iq2+i′kq)

where:

- *L'lfd* is the rotor field
  winding inductance.
- *L'lkd* is the rotor
  *d*-axis damper winding inductance.
- *L'lkg* is the rotor
  *q*-axis damper winding inductance.

The rotor torque is defined by:

Te=ψd1iq1−ψq1id1+ψd2iq2−ψq2id2.

### Model Thermal Effects

You can expose thermal ports to model the effects of losses that convert power to heat. To
expose the thermal ports, set the **Modeling option** parameter to either:

- `No thermal port` — The block contains expanded
  electrical conserving ports associated with the stator windings, but does not
  contain thermal ports.
- `Show thermal port` — The block contains expanded
  electrical conserving ports associated with the stator windings and thermal
  conserving ports for each of the windings and for the rotor.

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
