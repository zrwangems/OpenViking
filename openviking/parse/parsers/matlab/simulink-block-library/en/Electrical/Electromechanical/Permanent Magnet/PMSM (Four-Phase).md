---
type: simulink-block
title: 'PMSM (Four-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'pmsmfourphase'
documentation_source_path: 'ref/pmsmfourphase.html'
language: en
---

# PMSM (Four-Phase)

## Ports

### Conserving

### **a** — *a*-phase electrical

Electrical conserving port associated with
*a*-phase.

#### Dependencies

To enable this port, set **Winding type** to
`Cross-wound` or
`Square-wound`.

### **b** — *b*-phase electrical

Electrical conserving port associated with
*b*-phase.

#### Dependencies

To enable this port, set **Winding type** to
`Cross-wound` or
`Square-wound`.

### **c** — *c*-phase electrical

Electrical conserving port associated with
*c*-phase.

#### Dependencies

To enable this port, set **Winding type** to
`Cross-wound` or
`Square-wound`.

### **d** — *d*-phase electrical

Electrical conserving port associated with
*d*-phase.

#### Dependencies

To enable this port, set **Winding type** to
`Cross-wound` or
`Square-wound`.

### **a1** — *a* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *a*
positive-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **b1** — *b* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *b*
positive-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **c1** — *c* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *c*
positive-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **d1** — *d* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *d*
positive-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **a2** — *a* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *a*
negative-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **b2** — *b* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *b*
negative-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **c2** — *c* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *c*
negative-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **d2** — *d* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *d*
negative-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **n** — Neutral phase electrical

Electrical conserving port associated with the neutral phase.

#### Dependencies

To enable this port, set **Winding Type** to
`Cross-wound` and **Zero
sequence** to
`Include`.

### **R** — Motor rotor mechanical

Mechanical rotational conserving port associated with the motor
rotor.

### **C** — Motor case mechanical

Mechanical rotational conserving port associated with the motor
case.

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

### **HD** — *d*-phase terminal thermal port thermal

Thermal conserving port associated with stator winding
*d*.

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

### **Winding type** — Windings configuration `Cross-wound` (default) | `Square-wound` | `Open-end`

Configuration for the windings:

- `Cross-wound` — The windings are
  cross-wound.
- `Square-wound` — The windings are
  square-wound.
- `Open-end` — The windings are in
  an open-end configuration. The block exposes each end of the
  windings as electrical connections.

### **Number of pole pairs** — Number of pole pairs `6` (default) | scalar

Number of permanent magnet pole pairs on the rotor.

### **Permanent magnet flux linkage parameterization** — Permanent magnet flux linkage `Specify flux linkage` (default) | `Specify torque constant` | `Specify back EMF constant`

Permanent magnet flux linkage, specified as `Specify flux
linkage`, `Specify torque
constant`, or `Specify back EMF
constant`.

### **Permanent magnet flux linkage** — Permanent magnet flux linkage `0.03` `Wb` (default) | scalar

Peak permanent magnet flux linkage for any of the stator
windings.

#### Dependencies

To enable this parameter, set **Permanent magnet flux
linkage** to `Specify flux
linkage`.

### **Torque constant** — Torque constant `0.18` `N*m/A` (default) | scalar

Torque constant for any of the stator windings.

#### Dependencies

To enable this parameter, set **Permanent magnet flux
linkage** to `Specify torque
constant`.

### **Back EMF constant** — Back EMF constant `0.18` `V/(rad/s)` (default) | scalar

Back EMF constant for any of the stator windings.

#### Dependencies

To enable this parameter, set **Permanent magnet flux
linkage** to `Specify back EMF
constant`.

### **Stator parameterization** — Stator parameterization `Specify Ld, Lq, and L0` (default) | `Specify Ls, Lm, and Ms`

Stator parameterization, specified as `Specify Ld, Lq, and
L0` or `Specify Ls, Lm, and
Ms`.

### **Stator d-axis inductance, Ld** — Stator *d*-axis inductance `0.00019` `H` (default) | scalar

*d*-axis inductance.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0`.

### **Stator q-axis inductance, Lq** — Stator *q*-axis inductance `0.00025` `H` (default) | scalar

*q*-axis inductance.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0`.

### **Stator zero-sequence inductance, L0** — Stator zero-sequence inductance `0.00016` `H` (default) | scalar

Zero-sequence inductance.

#### Dependencies

To enable this parameter either:

- Set **Winding Type** to
  `Cross-wound`,
  **Zero sequence** to
  `Include`, and
  **Stator parameterization** to
  `Specify Ld, Lq, and L0`.
- Set **Winding Type** to
  `Square-wound` and
  **Stator parameterization** to
  `Specify Ld, Lq, and L0`.

### **Stator self-inductance per phase, Ls** — Stator self-inductance per phase `0.0002` `H` (default) | scalar

Average self-inductance of each of the four stator windings.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ls, Lm, and
Ms`.

### **Stator inductance fluctuation, Lm** — Stator inductance fluctuation `-0.00002` `H` (default) | scalar

Amount that the self-inductance and mutual inductance of the stator
windings fluctuate with the rotor angle.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ls, Lm, and
Ms`.

### **Stator mutual inductance, Ms** — Stator mutual inductance `0.00002` `H` (default) | scalar

Average mutual inductance between the stator windings.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ls, Lm, and
Ms`.

### **Stator resistance per phase, Rs** — Stator resistance per phase `0.013` `Ohm` (default) | scalar

Resistance of each of the stator windings.

### **Rotor angle definition** — Reference point for the rotor angle measurement `Angle between the a-phase magnetic axis and the d-axis` (default) | `Angle between the a-phase magnetic axis and the q-axis`

Reference point for the rotor angle measurement. When you select
`Angle between the a-phase magnetic axis and the
d-axis`, the rotor and *a*-phase
fluxes align when the rotor angle is zero.

When you select `Angle between the a-phase magnetic axis
and the q-axis`, the *a*-phase current
generates maximum torque when the rotor angle is zero.

### **Zero sequence** — Zero sequence option `Include` (default) | `Exclude`

Whether to include or exclude zero-sequence terms.

- `Include` — Include zero-sequence
  terms. Select this option to prioritize model fidelity.
  Using this option:

  - Results in an error for simulations that use
    the Partitioning solver. For more information, see
    Increase Simulation Speed Using the Partitioning Solver.
  - Exposes a zero-sequence parameter in the
    **Impedances** settings.
- `Exclude` — Exclude zero-sequence
  terms. Select this option to prioritize simulation speed for
  desktop simulation or real-time deployment.

#### Dependencies

To enable this parameter, set the **Winding
Type** to
`Cross-wound`.

### Mechanical

### **Rotor inertia** — Rotor inertia `0.01` `kg*m^2` (default) | nonnegative scalar

Inertia of the rotor attached to mechanical translational port
**R**. The value can be zero.

### **Rotor damping** — Rotor damping `0` `N*m/(rad/s)` (default) | nonnegative scalar

Rotary damping.

### Thermal

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Measurement temperature** — Rated temperature `298.15` `k` (default) | real scalar

Temperature for which the motor parameters are quoted.

### **Resistance temperature coefficient** — Temperature coefficient `3.93e-3` `1/K` (default) | positive scalar

Coefficient α in the equation relating resistance to temperature for
all four windings, as described in Thermal Model for Actuator Blocks. The default value,
`3.93e-3` 1/K, is for copper.

### **Permanent magnet flux temperature coefficient** — Permanent magnet flux temperature coefficient `-0.001` `1/K` (default) | scalar

Fractional rate at which the permanent magnet flux density changes
with temperature. Use this parameter to linearly reduce the torque and
the induced back EMF as temperature rises.

### **Thermal mass for each stator winding** — Winding thermal mass `100` `J/K` (default) | positive scalar

Thermal mass value for each stator winding. The thermal mass is the
energy required to raise the temperature by one degree.

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K` (default) | positive scalar

Thermal mass of the rotor. The thermal mass is the energy required to
raise the temperature of the rotor by one degree.

## Libraries

Simscape / Electrical / Electromechanical / Permanent Magnet

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2024a: Open-end configuration for stator windings

To model the stator windings of the machine in an open-end configuration, set the
**Winding type** parameter to
`Open-end`. The PMSM (Four-Phase) block then exposes each end
of the windings by enabling the corresponding electrical conserving ports.

## Description

Four-phase permanent magnet synchronous motor with sinusoidal flux distribution

The PMSM (Four-Phase) block models a permanent magnet
synchronous motor (PMSM) with a four-phase cross-wound or square-wound stator. Use this
block to model these types of motor if the motor has four stator windings: interior
permanent magnet synchronous machine (IPMSM), surface permanent magnet synchronous
machine (SPMSM), axial flux (pancake) motor, or PMSM servomotor. The figure shows the
equivalent electrical circuits for the cross-connected and square-connected stator windings.

### Motor Construction

Permanent magnets generate a rotor magnetic field that creates a sinusoidal rate
of change of flux based on the rotor angle.

For the axes convention, when you set the **Rotor angle
definition** parameter to `Angle between the a-phase
magnetic axis and the d-axis`, the *a*-phase and
permanent magnet fluxes align when the rotor mechanical angle,
*θr*, is zero. When you set the
**Rotor angle definition** parameter to `Angle
between the a-phase magnetic axis and the q-axis`, the rotor
mechanical angle is the angle between the *a*-phase magnetic axis
and the rotor *q*-axis.

### Equations

The voltages across the stator windings are

[vavbvcvd]=[Rs0000Rs0000Rs0000Rs][iaibicid]+[dψadtdψbdtdψcdtdψddt],

where:

- *va*,
  *vb*,
  *vc*, and
  *vd* are the individual
  phase voltages across the stator windings.
- *Rs* is the equivalent resistance
  of each stator winding.
- *ia*,
  *ib*,
  *ic*, and
  *id* are the currents
  flowing in the stator windings.
- dψadt,dψbdt,dψcdt, and dψddt are the rates of change for the magnetic flux in each
  stator winding.

The permanent magnet and the four windings contribute to the total flux linking
each winding. The total flux is

[ψaψbψcψd]=[LaaLabLacLadLbaLbbLbcLbdLcaLcbLccLcdLdaLdbLdcLdd][iaibicid]+[ψamψbmψcmψdm],

where:

- *ψa*,
  *ψb*,
  *ψc*, and
  *ψd* are the total fluxes
  that link each stator winding.
- *Laa*,
  *Lbb*,
  *Lcc*, and
  *Ldd* are the
  self-inductances of the stator windings. These self-inductances are a
  function of the rotor electrical angle,
  *θe*, and depend on the stator
  per-phase self-inductance, *Ls*, and
  the stator inductance fluctuation,
  *Lm*.

  - θe=Nθr+rotor offset where *θr*
    is the rotor mechanical angle.
  - *rotor offset* is `pi/2` if you
    define the rotor electrical angle with respect to the
    *d*-axis, or `0` if you define
    the rotor electrical angle with respect to the
    *q*-axis.
  - *Ls* is the stator
    per-phase self-inductance. This value is the average self-inductance
    of each of the stator windings.
  - *Lm* is the stator
    inductance fluctuation. This value is the amount the self-inductance
    and mutual inductance fluctuate with the changing of the rotor
    angle.
- *Lab*,
  *Lac*,
  *Lba*, and so on, are the
  mutual inductances of the stator windings. These mutual inductances are a
  function of the rotor electrical angle,
  *θe*, and depend on the stator
  mutual inductance, *Ms*, and the
  stator per-phase self-inductance,
  *Ls*.

  - *Ms* is the stator mutual
    inductance. This value is the average mutual inductance between the
    stator windings.
- *ψam*,
  *ψbm*,
  *ψcm*, and
  *ψdm* are the permanent
  magnet fluxes linking the stator windings.

The permanent magnet flux linking winding *a-a'* is at maximum
when *θe* = 0° and zero when
*θe* = 90°. Therefore, the
linked motor flux is defined by:

[ψamψbmψcmψdm]=[ψmcosθeψmcos(θr−π/2)ψmcos(θr+π)ψmcos(θr+π/2)],

where *ψm* is the permanent magnet flux
linkage.

### Simplified Electrical Equations

To remove the rotor angle dependence for the inductive terms, you perform a
transformation, *T*, on the motor equations.

The *T* transformation is defined by:

T(θe)=12[cosθecos(θe−π/2)cos(θe+π)cos(θe+π/2)−sinθe−sin(θe−π/2)−sin(θe+π)−sin(θe+π/2)1/2−1/21/2−1/21/21/21/21/2],

where *θe* is the electrical angle defined
as *Nθr*. *N* is the number
of pole pairs.

The transformation matrix has this pseudo-orthogonal property:

T−1(θe)=2Tt(θe).

Using the *T* transformation on the stator winding voltages and
currents transforms them to the dq0 and xy frames, which are independent of the
rotor angle:

[vdsvqsvxv0]=T[vavbvcvd]

[idsiqsixi0]=T[iaibicid]

Applying this transformation to the first two electrical equations produces these equations

vds=Rsids+Lddidsdt−NωiqsLq

vqs=Rsiqs+Lqdiqsdt+Nω(idsLd+ψm)

vx=Rsix+Ld+Lq2dixdt

v0=Rsi0+L0di0dt

T=2N(iqs(idsLd+ψm)−idsiqsLq)

where:

- *Ld* =
  *Ls* +
  *Ms* + 2
  *Lm*.
  *Ld* is the stator
  *d*-axis inductance.
- *Lq* =
  *Ls* +
  *Ms* − 2
  *Lm*.
  *Lq* is the stator
  *q*-axis inductance.
- *L0* =
  *Ls* –
  3*Ms*.
  *L0* is the stator
  zero-sequence inductance.
- *ω* is the rotor mechanical rotational speed.
- *N* is the number of rotor permanent magnet pole
  pairs.

### Alternative Flux Linkage Parameterization

You can parameterize the motor by using the back EMF or torque constants, which
are more commonly given on motor datasheets, by using the **Permanent magnet
flux linkage** parameter.

The back EMF constant is the peak voltage induced by the permanent magnet in the
per-unit rotational speed of each of the phases. The relationship between the peak
permanent magnet flux linkage and the back EMF is:

ke=Nψm.

The back EMF, *eph*, for one phase
is:

eph=keω.

The torque constant is the peak torque induced by the per-unit current of each of
the phases. It is numerically identical in value to the back EMF constant when both
are expressed in SI units:

kt=Nψm.

When *Ld* =
*Lq* and the currents in all four
phases are balanced, the combined torque *T* is:

T=2ktiq=2ktIpk,

where *Ipk* is the peak current in any of
the four windings.

The factor 2 is calculated from the steady-state sum of the torques from all
phases. Therefore, the torque constant *kt*
can also be:

kt=12(TIpk),

where *T* is the measured total torque when
testing with a balanced four-phase current with a peak line voltage of
*Ipk*. The RMS line voltage is:

kt=12(Tiline,rms).

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

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
