---
type: simulink-block
title: 'PMLSM'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'pmlsm'
documentation_source_path: 'ref/pmlsm.html'
language: en
---

# PMLSM

## Ports

### Conserving

### **~** — Three-phase port electrical

Expandable three-phase
port.

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

To enable this port, set **Winding Type** to
`Wye-wound` and **Zero
sequence** to
`Include`.

### **R** — Motor mover mechanical

Mechanical translational conserving port associated with the motor
mover.

### **C** — Motor case mechanical

Mechanical translational conserving port associated with the motor case.

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

Configuration for the windings:

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

### **Modeling fidelity** — Modeling fidelity `Constant Ld, Lq and PM` (default) | `Tabulated Ld, Lq and PM`

Modeling fidelity:

- `Constant Ld, Lq and PM` — The
  *Ld*, *Lq*, and
  *PM* values are constant and defined by
  their respective parameters.
- `Tabulated Ld, Lq and PM` — The
  *Ld*, *Lq*, and
  *PM* values are computed online from DQ
  current lookup tables as follows:h

  Ld=f1(id,iq)

  Ld=f2(id,iq)

  λPM=f2(id,iq)

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0`.

### **Polar pitch** — Polar pitch `0.03` `m` (default) | scalar

Polar pitch.

### **Permanent magnet flux linkage parameterization** — Permanent magnet flux linkage parameterization `Specify flux linkage` (default) | `Specify force constant` | `Specify back EMF constant`

Permanent magnet flux linkage, specified as `Specify flux
linkage`, `Specify force
constant`, or `Specify back EMF
constant`.

### **Permanent magnet flux linkage** — Permanent magnet flux linkage `0.03` `Wb` (default) | scalar

Peak permanent magnet flux linkage with any of the stator
windings.

#### Dependencies

To enable this parameter, set **Permanent magnet flux linkage
parameterization** to `Specify flux
linkage` and **Modeling fidelity**
to `Constant Ld, Lq and PM`.

### **Force constant** — Force constant `0.18` `N/A` (default) | scalar

Force constant for any of the stator windings.

#### Dependencies

To enable this parameter, set **Permanent magnet flux linkage
parameterization** to `Specify force
constant` and **Modeling
fidelity** to `Constant Ld, Lq and
PM`.

### **Back EMF constant** — Back EMF constant `0.18` `s*V/m` (default) | scalar

Back EMF constant for any of the stator windings.

#### Dependencies

To enable this parameter, set **Permanent magnet flux linkage
parameterization** to `Specify back EMF
constant` and **Modeling
fidelity** to `Constant Ld, Lq and
PM`.

### **Stator parameterization** — Stator parameterization `Specify Ld, Lq, and L0` (default) | `Specify Ls, Lm, and Ms`

Stator parameterization, specified as `Specify Ld, Lq, and L0`
or `Specify Ls, Lm, and Ms`.

### **Stator d-axis inductance, Ld** — Stator `d`-axis inductance `0.00019` `H` (default) | scalar

`d`-axis inductance.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Constant Ld, Lq and PM`.

### **Stator q-axis inductance, Lq** — Stator q-axis inductance `0.00025` `H` (default) | scalar

`q`-axis inductance.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Constant Ld, Lq and
PM`.

### **Stator zero-sequence inductance, L0** — Stator zero-sequence inductance `0.00016` `H` (default) | scalar

Zero-sequence inductance.

#### Dependencies

To enable this parameter either:

- Set **Winding Type** to
  `Wye-wound`, **Zero
  sequence** to
  `Include`, and
  **Stator parameterization** to
  `Specify Ld, Lq, and L0`.
- Set **Winding Type** to
  `Delta-wound` and
  **Stator parameterization** to
  `Specify Ld, Lq, and L0`.

### **Direct-axis current vector, iD** — Direct-axis current vector `[-200, 0, 200]` `A` (default) | vector

Direct-axis current vector, iD.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Tabulated Ld, Lq and
PM`.

### **Quadrature-axis current vector, iQ** — Quadrature-axis current vector `[-200, 0, 200]` `A` (default) | vector

Quadrature-axis current vector, iQ.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Tabulated Ld, Lq and
PM`.

### **Ld matrix, Ld(id,iq)** — Ld matrix `0.00019 * ones(3, 3)` `H` (default) | matrix

Ld matrix.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Tabulated Ld, Lq and
PM`.

### **Lq matrix, Lq(id,iq)** — Lq matrix `0.00025 * ones(3, 3)` `H` (default) | matrix

Lq matrix.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Tabulated Ld, Lq and
PM`.

### **Permanent magnet flux linkage, PM(id,iq)** — Permanent magnet flux linkage `0.03 * ones(3, 3)` `Wb` (default)

Permanent magnet flux linkage.

#### Dependencies

To enable this parameter, set:

- **Stator parameterization** to
  `Specify Ld, Lq, and L0`
- **Modeling fidelity** to
  `Tabulated Ld, Lq and
  PM`
- **Permanent magnet flux linkage
  parameterization** to `Specify
  flux linkage`

### **Force constant matrix, kf(iD,iQ)** — Force constant matrix `0.18 * ones(3, 3)` `N/A` (default) | matrix

Force constant matrix.

#### Dependencies

To enable this parameter, set:

- **Stator parameterization** to
  `Specify Ld, Lq, and L0`
- **Modeling fidelity** to
  `Tabulated Ld, Lq and
  PM`
- **Permanent magnet flux linkage
  parameterization** to `Specify
  force constant`

### **Back EMF constant matrix, ke(iD,iQ)** — Back EMF constant matrix `0.18 * ones(3, 3)` `s*V/m` (default) | matrix

Back EMF constant matrix.

#### Dependencies

To enable this parameter, set:

- **Stator parameterization** to
  `Specify Ld, Lq, and L0`
- **Modeling fidelity** to
  `Tabulated Ld, Lq and
  PM`
- **Permanent magnet flux linkage
  parameterization** to `Specify
  back EMF constant`

### **Stator self-inductance per phase, Ls** — Stator self-inductance per phase `0.0002` `H` (default) | scalar

Average self-inductance of each of the five stator windings.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ls, Lm, and Ms`.

### **Stator inductance fluctuation, Lm** — Stator inductance fluctuation `-0.00002` `H` (default) | scalar

Fluctuation in self-inductance and mutual inductance of the stator windings with
angle.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ls, Lm, and Ms`.

### **Stator mutual inductance, Ms** — Stator mutual inductance `0.00002` `H` (default) | scalar

Average mutual inductance between the stator windings.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ls, Lm, and Ms`.

### **Stator resistance per phase, Rs** — Stator resistance per phase `0.013` `Ohm` (default) | scalar

Resistance of each of the stator windings.

### **Zero sequence** — Zero sequence option `Include` (default) | `Exclude`

Option to include or exclude zero-sequence terms.

- `Include` — Include zero-sequence
  terms. To prioritize model fidelity, use this default
  setting. Using this option:

  - Results in an error for simulations that use
    the Partitioning solver. For more information, see
    Increase Simulation Speed Using the Partitioning Solver.
  - Exposes a zero-sequence parameter.
- `Exclude` — Exclude zero-sequence
  terms. To prioritize simulation speed for desktop simulation
  or real-time deployment, select this option.

#### Dependencies

To enable this parameter, set **Winding Type** to
`Wye-wound`.

### **Angle definition** — Reference point for angle measurement `Angle between the a-phase magnetic axis and the d-axis` (default) | `Angle between the a-phase magnetic axis and the q-axis`

Reference point for the angle measurement. The default value is
`Angle between the a-phase magnetic axis and the
d-axis`. This definition is shown in the Motor Construction figure. When you
select this value, the mover and *a*-phase fluxes are
aligned when the mover angle is zero.

The other value you can choose for this parameter is `Angle
between the a-phase magnetic axis and the q-axis`. When you
select this value, the *a*-phase current generates
maximum force when the mover angle is zero.

### Mechanical

### **Mass of the mover** — Mass of the mover `0.01` `kg` (default)

Mass of the motor mover.

### **Linear damping** — Linear damping `0` `N/(m/s)` (default)

Linear damping.

### Thermal

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Measurement temperature** — Measurement temperature `298.15` `K` (default)

The temperature for which motor parameters are quoted.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default)

Coefficient α in the equation relating resistance to temperature, as
described in Thermal Model for Actuator Blocks. The default value is for
copper.

### **Permanent magnet flux temperature coefficient** — Permanent magnet flux temperature coefficient `-0.001` `1/K` (default)

Fractional rate of change of permanent magnet flux density with
temperature. Use this parameter to linearly reduce the torque and the
induced back EMF as temperature rises.

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

**Introduced in R2020a**

### R2024a: Open-end configuration for stator windings

To model the stator windings of the machine in an open-end configuration, set the
**Winding type** parameter to
`Open-end`. The PMLSM block then exposes each end
of the windings by enabling the corresponding electrical conserving ports.

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Permanent magnet linear synchronous motor with sinusoidal flux distribution

The PMLSM block models a permanent magnet linear synchronous
motor (PMLSM) with a three-phase wye-wound stator. Use this block to model linear
synchronous motors (LSMs) and linear servo motors. This figure shows the equivalent
electrical circuit for the stator windings.

You can also model the permanent magnet linear synchronous motor in a
delta-wound configuration by setting **Winding type** to
`Delta-wound`.

### Motor Construction

This figure shows the motor construction.

### Equations

Voltages across the stator windings are defined by:

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

where:

- *va*,
  *vb*, and
  *vc* are the individual
  phase voltages across the stator windings.
- *Rs* is the equivalent resistance
  of each stator winding.
- *ia*,
  *ib*, and
  *ic* are the currents
  flowing in the stator windings.
- dψadt,dψbdt, and dψcdt are the rates of change of magnetic flux in each stator
  winding.

The permanent magnet and the three windings contribute to the total flux linking
each winding. The total flux is defined by:

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]+[ψamψbmψcm],

where:

- *ψa*,
  *ψb*, and
  *ψc* are the total fluxes
  linking each stator winding.
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
  *ψcm* are the permanent
  magnet fluxes linking the stator windings.

The inductances in the stator windings are functions of electrical angle, and are
defined by:

θe=Npx+rotor offset,

Laa=Ls+Lmcos(2θe)

Lbb=Ls+Lmcos(2(θe−2π/3))

Lcc=Ls+Lmcos(2(θe+2π/3))

Lab=Lba=−Ms−Lmcos(2(θe+π/6))

Lbc=Lcb=−Ms−Lmcos(2(θe+π/6−2π/3))

and

Lca=Lac=−Ms−Lmcos(2(θe+π/6+2π/3))

where:

- *θe* is the electrical
  angle.
- *rotor offset* is `0` if you define the
  rotor electrical angle with respect to the d-axis, or
  `-pi/2` if you define the rotor electrical angle with
  respect to the q-axis.
- Np=πτ and *τ* is the polar pitch.
- *x* is the distance.
- *Ls* is the per-phase stator
  self-inductance. This value is the average self-inductance of each of the
  stator windings.
- *Lm* is the stator inductance
  fluctuation. This value is the fluctuation in self-inductance and mutual
  inductance with changing angle.
- *Ms* is the stator mutual
  inductance. This value is the average mutual inductance between the stator
  windings.

The permanent magnet flux linking winding *a* is a maximum when
*θe* = 0° and zero when
*θe* = 90°. Therefore, the
linked motor flux is defined by:

[ψamψbmψcm]=[ψmcosθeψmcos(θe−2π/3)ψmcos(θe+2π/3)]

where *ψm* is the permanent magnet flux
linkage.

### Simplified Electrical Equations

Applying Park’s transformation to the electrical equations produces an expression
for force that is independent of the angle.

Park’s transformation is defined by:

P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5]

where *θe* is the electrical angle defined
as *Npx*.

Using Park's transformation on the stator winding voltages and currents transforms
them into the dq0 frame, which is independent of the angle:

[vdvqv0]=P[vavbvc]

and

[idiqi0]=P[iaibic]

Applying Park’s transformation to the first two electrical equations produces the
following equations that define the block behavior:

vd=Rsid+Lddiddt−NpviqLq,

vq=Rsiq+Lqdiqdt+Npv(idLd+ψm),

v0=Rsi0+L0di0dt

and

F=32Np(iq(idLd+ψm)−idiqLq),

Mdvdt=F−FL−Bmv,

where:

- *Ld* =
  *Ls* +
  *Ms* + 3/2
  *Lm*.
  *Ld* is the stator
  *d*-axis inductance.
- *Lq* =
  *Ls* +
  *Ms* − 3/2
  *Lm*.
  *Lq* is the stator
  *q*-axis inductance.
- *L0* =
  *Ls* –
  2*Ms*.
  *L0* is the stator
  zero-sequence inductance.
- *Rs* is the stator resistance per
  phase.
- *v* is the linear speed.
- *Np* is the polar pitch
  factor.
- *M* is the mass of the mover.
- *Bm* is the damping.
- *FL* is the load force.

The PMLSM block uses the original, nonorthogonal
implementation of the Park transform. If you try to apply the alternative
implementation, you get different results for the dq0 voltage and currents.

The relationship between the force constant
*kf*, the back-emf constant
*ke*, and the permanent magnet flux
linkage is defined as follows:

ke=kf=Npψm.

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
