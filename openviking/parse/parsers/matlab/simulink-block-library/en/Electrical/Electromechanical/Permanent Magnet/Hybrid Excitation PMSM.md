---
type: simulink-block
title: 'Hybrid Excitation PMSM'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'hybridexcitationpmsm'
documentation_source_path: 'ref/hybridexcitationpmsm.html'
language: en
---

# Hybrid Excitation PMSM

## Ports

### Conserving

### **R** — Machine rotor mechanical rotational

Mechanical rotational conserving port associated with the machine
rotor.

### **C** — Machine case mechanical rotational

Mechanical rotational conserving port associated with the machine
case.

### **~** — Three-phase composite electrical

Expandable three-phase
port associated with the stator windings.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **a** — *a*-phase electrical

Electrical conserving port associated with
*a*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **b** — *b*-phase electrical

Electrical conserving port associated with
*b*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **c** — *c*-phase electrical

Electrical conserving port associated with
*c*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **~1** — Stator positive-end connections electrical

*Since R2024a*

Expandable three-phase
port associated with the stator positive-end
connections.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports` and **Winding type** to
`Open-end`.

### **~2** — Stator negative-end connections electrical

*Since R2024a*

Expandable three-phase
port associated with the stator negative-end
connections.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports` and **Winding type** to
`Open-end`.

### **a1** — *a* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *a*
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **b1** — *b* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *b*
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **c1** — *c* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *c*
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **a2** — *a* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *a*
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **b2** — *b* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *b*
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **c2** — *c* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *c*
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **n** — Neutral phase electrical

Electrical conserving port associated with the neutral phase.

#### Dependencies

To enable this port, set **Winding type** to
`Wye-wound` and **Zero
sequence** to
`Include`.

### **fd+** — Field winding positive terminal electrical

Electrical conserving port associated with the field winding positive
terminal.

### **fd-** — Field winding negative terminal electrical

Electrical conserving port associated with the field winding negative
terminal.

### **HA** — Winding A thermal port thermal

Thermal conserving port associated with winding A.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HB** — Winding B thermal port thermal

Thermal conserving port associated with winding B.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HC** — Winding C thermal port thermal

Thermal conserving port associated with winding C.

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

Whether to enable the thermal ports of the block and model the effects of generated heat and motor temperature.

### Main

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Winding type** — Windings configuration `Wye-wound` (default) | `Delta-wound` | `Open-end`

*Since R2024a*

Select the configuration for the windings:

- `Wye-wound` — The windings are
  wye-wound.
- `Delta-wound` — The windings are
  delta-wound. The *a*-phase is connected
  between ports **a** and
  **b**, the *b*-phase
  between ports **b** and
  **c** and the
  *c*-phase between ports
  **c** and
  **a**.
- `Open-end` — The windings are in
  an open-end configuration. The block exposes each end of the
  windings as electrical connections.

### **Modeling fidelity** — Modeling fidelity `Constant Ld, Lq, Lmf, Lf and PM` (default) | `Tabulated Ld, Lq, Lmf, Lf and PM`

Select the modeling fidelity:

- `Constant Ld, Lq, Lmf, Lf and PM`
  — *Ld*, *Lq*,
  *Lmf*, *Lf*, and
  *PM* values are constant and defined by
  their respective parameters.
- `Tabulated Ld, Lq, Lmf, Lf and
  PM` — *Ld*,
  *Lq*, *Lmf*,
  *Lf*, and *PM* values
  are computed online from DQ and field currents look-up
  tables as follows:

  Ld=f1(id,iq,if)

  Lq=f2(id,iq,if)

  Lmf=f3(id,iq,if)

  λPM=f4(id,iq,if)

  Lf=f5(if)

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify
Ld, Lq, and L0`.

### **Number of pole pairs** — Rotor pole pairs `6` (default) | integer

Number of permanent magnet pole pairs on the rotor.

### **Permanent magnet flux linkage** — Flux linkage `0.09` `Wb` (default) | positive integer

Peak permanent magnet flux linkage for any of the stator
windings.

#### Dependencies

This parameter is visible only when you set the **Modeling
fidelity** parameter to `Constant Ld, Lq,
Lmf, Lf and PM`.

### **Stator parameterization** — Parameterization model `Specify Ld, Lq and L0` (default) | `Specify Ls, Lm, and Ms`

Stator parameterization model.

#### Dependencies

The **Stator parameterization** setting affects
the visibility of other parameters.

### **Stator d-axis inductance, Ld** — Inductance `0.0031` `H` (default)

Direct-axis inductance of the machine stator.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify
Ld, Lq, and L0` and the **Modeling
fidelity** parameter to `Constant Ld, Lq,
Lmf, Lf and PM`.

### **Stator q-axis inductance, Lq** — Inductance `0.0045` `H` (default)

Quadrature-axis inductance of the machine stator.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify
Ld, Lq, and L0` and the **Modeling
fidelity** parameter to `Constant Ld, Lq,
Lmf, Lf and PM`.

### **Direct-axis current vector, iD** — Direct-axis current vector `[-200, 0, 200]` `A` (default)

Direct-axis current vector, iD.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld, Lq,
Lmf, Lf and PM`.

### **Quadrature-axis current vector, iQ** — Quadrature-axis current vector `[-200, 0, 200]` `A` (default)

Quadrature-axis current vector, iQ.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld, Lq,
Lmf, Lf and PM`.

### **Excitation current vector, iF** — Excitation current vector `[-20, 0, 20]` `A` (default)

Excitation current vector, iF.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld, Lq,
Lmf, Lf and PM`.

### **Ld matrix, Ld(id,iq,if)** — Ld matrix `0.0031 * ones(3, 3, 3)` `H` (default)

Ld matrix.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld, Lq,
Lmf, Lf and PM`.

### **Lq matrix, Lq(id,iq,if)** — Lq matrix `0.0045 * ones(3, 3, 3)` `H` (default)

Lq matrix.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld, Lq,
Lmf, Lf and PM`.

### **Mutual field armature inductance, Lmf(id,iq,if)** — Mutual field armature inductance `0.0067 * ones(3, 3, 3)` `H` (default)

Mutual field armature inductance.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld, Lq,
Lmf, Lf and PM`.

### **Permanent magnet flux linkage, PM(id,iq,if)** — Permanent magnet flux linkage `0.1 * ones(3, 3, 3)` `Wb` (default)

Permanent magnet flux linkage.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0`, the **Modeling fidelity**
parameter to `Tabulated Ld, Lq, Lmf, Lf and
PM`.

### **Lf vector, Lf(if)** — Lf vector `0.06 * ones(1, 3)` `H` (default)

Lf vector.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0`, the **Modeling fidelity**
parameter to `Tabulated Ld, Lq, Lmf, Lf and
PM`.

### **Stator zero-sequence inductance, L0** — Inductance `0.0006` `H` (default)

Zero-axis inductance for the machine stator.

#### Dependencies

This parameter is visible only if **Stator
parameterization** is set to `Specify Ld,
Lq and L0` and **Zero sequence**
is set to `Include`.

### **Stator self-inductance per phase, Ls** — Inductance `0.0027` `H` (default)

Average self-inductance of the three stator windings.

#### Dependencies

This parameter is visible only if **Stator
parameterization** is set to `Specify Ls,
Lm, and Ms`.

### **Stator inductance fluctuation, Lm** — Inductance `-0.0005` `H` (default)

Fluctuation in self-inductance and mutual inductance with the rotor
angle.

#### Dependencies

This parameter is visible only if **Stator
parameterization** is set to `Specify Ls,
Lm, and Ms`.

### **Stator mutual inductance, Ms** — Inductance `0.0011` `H` (default)

Average mutual inductance between the stator windings.

#### Dependencies

This parameter is visible only if **Stator
parameterization** is set to `Specify Ls,
Lm, and Ms`.

### **Field winding inductance, Lf** — Inductance `0.06` `H` (default)

Inductance of the field winding.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify
Ld, Lq, and L0` and the **Modeling
fidelity** parameter to `Constant Ld, Lq,
Lmf, Lf and PM` or **Stator
parameterization** parameter to `Specify
Ls, Lm, and Ms`

### **Mutual field armature inductance, Lmf** — Inductance `0.0067` `H` (default)

Armature-field mutual inductance.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify
Ld, Lq, and L0` and the **Modeling
fidelity** parameter to `Constant Ld, Lq,
Lmf, Lf and PM` or **Stator
parameterization** parameter to `Specify
Ls, Lm, and Ms`

### **Stator resistance per phase, Rs** — Resistance `0.7` `Ohm` (default)

Resistance of each of the stator windings.

### **Field winding resistance, Rf** — Resistance `2.85` `Ohm` (default)

Resistance of the field winding.

### **Zero sequence** — Zero-sequence model `Include` (default) | `Exclude`

Zero-sequence model:

- `Include` — Prioritize model fidelity. An
  error occurs if you Include zero-sequence terms for simulations that use the
  Partitioning solver. For more information, see Increase Simulation Speed Using the Partitioning Solver.
- `Exclude` — Prioritize simulation speed
  for desktop simulation or real-time deployment.

#### Dependencies

If this parameter is set to:

- `Include` and **Stator
  parameterization** is set to **Specify Ld, Lq, and
  L0** — The **Stator zero-sequence
  inductance, L0** parameter is visible.
- `Exclude` — The **Stator
  zero-sequence inductance, L0** parameter is not
  visible.

### **Rotor angle definition** — Angle `Angle between the a-phase magnetic axis and the d-axis` (default) | `Angle between the a-phase magnetic axis and the q-axis`

Reference point for the rotor angle measurement. If you select the
default value, the rotor and *a*-phase fluxes are
aligned for a zero-rotor angle. Otherwise, an *a*-phase
current generates the maximum torque value for a zero-rotor angle.

### Mechanical

### **Rotor inertia** — Inertia `0.01` `kg*m^2` (default)

Inertia of the rotor attached to mechanical translational port
**R**.

### **Rotor Damping** — Damping `0` `N*m/(rad/s)` (default)

Rotary damping.

### Thermal

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Measurement temperature** — Measurement temperature `298.15` `K` (default)

The temperature for which motor parameters are quoted.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default)

Coefficient α in the equation relating resistance to temperature, as
described in Thermal Model for Actuator Blocks. The default value is for
copper.

### **Permanent magnet flux temperature coefficient** — Permanent magnet flux temperature coefficient `-0.001` (default)

The fractional rate of change of permanent magnet flux density with
temperature. It is used to linearly reduce the torque and the induced
back EMF as temperature rises.

### **Thermal mass for each stator winding** — Thermal mass for each stator winding `100` `J/K` (default)

The thermal mass value for the A, B, and C windings. The thermal mass
is the energy required to raise the temperature by one degree.

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K` (default)

The thermal mass of the rotor, that is, the energy required to raise
the temperature of the rotor by one degree.

## Libraries

Simscape / Electrical / Electromechanical / Permanent Magnet

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2024a: Open-end and delta-wound configurations for stator windings

In addition to the wye-wound configuration, you can also model the stator windings
of the machine in a delta-wound configuration or in an open-end configuration.

To model the stator windings of the machine in a delta-wound configuration, set
the **Winding type** parameter to
`Delta-wound`. The *a*-phase is
connected between ports **a** and **b**, the
*b*-phase between ports **b** and
**c** and the *c*-phase between ports
**c** and **a**.

To model the stator windings of the machine in an open-end configuration, set the
**Winding type** parameter to
`Open-end`. The Hybrid Excitation PMSM block then exposes each end
of the windings by enabling the corresponding electrical conserving ports.

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Hybrid excitation synchronous machine with three-phase wye-wound stator

The Hybrid Excitation PMSM block represents a hybrid
excitation synchronous machine with a three-phase wye-wound stator. Permanent magnets
and excitation windings provide the machine excitation. Use this block to model hybrid
excitation permanent magnet synchronous motors (PMSMs), doubly-excited PMSMs, and
synchronous motors. This figure shows the equivalent electrical circuit for the stator
and rotor windings.

You can also model the permanent magnet synchronous motor either in a delta-wound or
in an open-end configuration by setting **Winding type** to
`Delta-wound` or `Open-end`,
respectively.

### Motor Construction

The diagram shows the motor construction with a single pole-pair on the rotor. For
the axes convention, when rotor mechanical angle
*θr* is zero, the
*a*-phase and permanent magnet fluxes are aligned. The block
supports a second rotor axis definition for which rotor mechanical angle is defined
as the angle between the *a*-phase magnetic axis and the rotor
*q*-axis.

### Equations

Voltages across the stator windings are defined by

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

where:

- *va*,
  *vb*, and
  *vc* are the individual
  phase voltages across the stator windings.
- *Rs* is the equivalent
  resistance of each stator winding.
- *ia*,
  *ib*, and
  *ic* are the currents
  flowing in the stator windings.
- dψadt,dψbdt, and dψcdt are the rates of change of magnetic flux in each
  stator winding.

The voltage across the field winding is expressed as

vf=Rfif+dψfdt,

where:

- *vf* is the individual phase
  voltage across the field winding.
- *Rf* is the equivalent
  resistance of the field winding.
- *if* is the current flowing in
  the field winding.
- dψfdt is the rate of change of magnetic flux in the field
  winding.

The permanent magnet, excitation winding, and the three star-wound stator windings
contribute to the flux linking each winding. The total flux is defined by

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]+[ψamψbmψcm]+[LamfLbmfLcmf]if,

where:

- *ψa*,
  *ψb*, and
  *ψc* are the total
  fluxes linking each stator winding.
- *Laa*,
  *Lbb*, and
  *Lcc* are the
  self-inductances of the stator windings.
- *Lab*,
  *Lac*,
  *Lba*,
  *Lbc*,
  *Lca*, and
  *Lcb* are the mutual
  inductances of the stator windings.
- *ψam*,
  *ψbm*, and
  *ψcm* are the
  magnetization fluxes linking the stator windings.
- *Lamf*,
  *Lbmf*, and
  *Lcmf* are the mutual
  inductances of the field winding.

The inductances in the stator windings are functions of rotor electrical angle and
are defined by

θe=Nθr+rotor offset

Laa=Ls+Lmcos(2θe),

Lbb=Ls+Lmcos(2(θe−2π/3)),

Lcc=Ls+Lmcos(2(θe+2π/3)),

Lab=Lba=−Ms−Lmcos(2(θe+π/6)),

Lbc=Lcb=−Ms−Lmcos(2(θe+π/6−2π/3)),

Lca=Lac=−Ms−Lmcos(2(θe+π/6+2π/3)),

where:

- *N* is the number of rotor pole pairs.

- *θr* is the rotor mechanical
  angle.

- *θe* is the rotor electrical
  angle.
- *rotor offset* is `0` if you define the
  rotor electrical angle with respect to the d-axis, or
  `-pi/2` if you define the rotor electrical angle with
  respect to the q-axis.
- *Ls* is the stator self-inductance
  per phase. This value is the average self-inductance of each of the stator
  windings.
- *Lm* is the stator inductance
  fluctuation. This value is fluctuation in self-inductance and mutual
  inductance with changing rotor angle.
- *Ms* is the stator mutual
  inductance. This value is the average mutual inductance between the stator
  windings.

The magnetization flux linking winding, *a-a’* is a maximum when
*θe* = 0° and zero when
*θe* = 90°. Therefore:

ψm=[ψamψbmψcm]=[ψmcosθeψmcos(θe−2π/3)ψmcos(θe+2π/3)],

Lmf=[LamfLbmfLcmf]=[LmfcosθeLmfcos(θe−2π/3)Lmfcos(θe+2π/3)],

and

Ψf=Lfif+LmfT[iaibic],

where:

- *ψm* is the linked motor
  flux.
- *Lmf* is the mutual field
  armature inductance.
- *ψf* is the flux linking the
  field winding.
- *Lf* is the field winding
  inductance.
- [Lmf]T is the transform of the
  *Lmf* vector, that is,

  [Lmf]T=[LamfLbmfLcmf]T=[LamfLbmfLcmf].

### Simplified Equations

Applying the Park transformation to the block electrical defining equations
produces an expression for torque that is independent of rotor angle.

The Park transformation is defined by

P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5]

Applying the Park transformation to the first two electrical defining equations
produces equations that define the block behavior:

vd=Rsid+Lddiddt+Lmfdifdt−NωiqLq,

vq=Rsiq+Lqdiqdt+Nω(idLd+ψm+ifLmf),

v0=Rsi0+L0di0dt

vf=Rfif+Lfdifdt+32Lmfdiddt,

T=32N(iq(idLd+ψm+ifLmf)−idiqLq),

and

Jdωdt=T=TL−Bmω.

where:

- *vd*,
  *vq*, and
  *v0* are the
  *d*-axis, *q*-axis, and zero-sequence
  voltages. These voltages are defined by

  [vdvqv0]=P[vavbvc].
- *id*,
  *iq*, and
  *i0* are the
  *d*-axis, *q*-axis, and zero-sequence
  currents, defined by

  [idiqi0]=P[iaibic].
- *Ld* is the stator
  *d*-axis inductance.
  *Ld* =
  *Ls* +
  *Ms* + 3/2
  *Lm*.
- *ω* is the mechanical rotational speed.
- *Lq* is the stator
  *q*-axis inductance.
  *Lq* =
  *Ls* +
  *Ms* − 3/2
  *Lm*.
- *L0* is the stator zero-sequence
  inductance. *L0* =
  *Ls* –
  2*Ms*.
- *T* is the rotor torque. For the Hybrid
  Excitation PMSM block, torque flows from the machine
  case (block conserving port **C**) to the machine rotor
  (block conserving port **R**).
- *J* is the rotor inertia.
- *TL* is the load torque.
- *Bm* is the rotor damping.

### Model Thermal Effects

You can expose thermal ports to model the effects of generated heat and motor temperature. To
expose the thermal ports, set the **Modeling option** parameter to either:

- `No thermal port` — The block contains expanded
  electrical conserving ports associated with the stator windings, but does not
  contain thermal ports.
- `Show thermal port` — The block contains expanded
  electrical conserving ports associated with the stator windings and thermal
  conserving ports for each of the windings and for the rotor.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
