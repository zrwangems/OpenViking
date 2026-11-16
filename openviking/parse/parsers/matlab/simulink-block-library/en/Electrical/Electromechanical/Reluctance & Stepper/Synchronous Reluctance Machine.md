---
type: simulink-block
title: 'Synchronous Reluctance Machine'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Reluctance & Stepper'
documentation_page: 'synchronousreluctancemachine'
documentation_source_path: 'ref/synchronousreluctancemachine.html'
language: en
---

# Synchronous Reluctance Machine

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

Whether to enable the thermal ports of the block and model the effects of losses that convert
power to heat.

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

### **Number of pole pairs** — Rotor pole pairs `6` (default) | integer

Number of permanent magnet pole pairs on the rotor.

### **Stator parameterization** — Parameterization model `Specify Ld, Lq and L0` (default) | `Specify Ls, Lm, and Ms`

Stator parameterization model.

#### Dependencies

The **Stator parameterization** setting affects
the visibility of other parameters.

### **Modeling fidelity** — Modeling fidelity `Constant Ld and Lq` (default) | `Tabulated Ld and Lq`

Select the modeling fidelity:

- `Constant Ld and Lq` —
  *Ld* and *Lq* values
  are constant and defined by their respective
  parameters.
- `Tabulated Ld and Lq` —
  *Ld* and *Lq* values
  are computed online from DQ currents look-up tables as follows:

  Ld=f1(id,iq)

  Ld=f2(id,iq)

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify
Ld, Lq, and L0`.

### **Stator d-axis inductance, Ld** — Inductance `0.0031` `H` (default)

Direct-axis inductance of the machine stator.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify
Ld, Lq, and L0` and the **Modeling
fidelity** parameter to `Constant Ld and
Lq`.

### **Stator q-axis inductance, Lq** — Inductance `0.004` `H` (default)

Quadrature-axis inductance of the machine stator.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify
Ld, Lq, and L0` and the **Modeling
fidelity** parameter to `Constant Ld and
Lq`.

### **Direct-axis current vector, iD** — Direct-axis current vector `[-200, 0, 200]` `A` (default)

Direct-axis current vector, iD.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld and
Lq`.

### **Quadrature-axis current vector, iQ** — Quadrature-axis current vector `[-200, 0, 200]` `A` (default)

Quadrature-axis current vector, iQ.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld and
Lq`.

### **Ld matrix, Ld(id,iq)** — Ld matrix `0.0031 * ones(3, 3)` `H` (default)

Ld matrix.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld and
Lq`.

### **Lq matrix, Lq(id,iq)** — Lq matrix `0.004 * ones(3, 3)` `H` (default)

Lq matrix.

#### Dependencies

This parameter is visible only when you set the **Stator
parameterization** parameter to `Specify Ld,
Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld and
Lq`.

### **Stator zero-sequence inductance, L0** — Inductance `0.0005` `H` (default)

Zero-axis inductance for the machine stator.

#### Dependencies

This parameter is visible only if **Stator
parameterization** is set to `Specify Ld,
Lq and L0` and **Zero sequence**
is set to `Include`.

### **Stator self-inductance per phase, Ls** — Inductance `0.0025` `H` (default)

Average self-inductance of the three stator windings.

#### Dependencies

This parameter is visible only if **Stator
parameterization** is set to `Specify Ls,
Lm, and Ms`.

### **Stator inductance fluctuation, Lm** — Inductance `-0.0003` `H` (default)

Amplitude of the fluctuation in self-inductance and mutual inductance
with the rotor angle.

#### Dependencies

This parameter is visible only if **Stator
parameterization** is set to `Specify Ls,
Lm, and Ms`.

### **Stator mutual inductance, Ms** — Inductance `0.0010` `H` (default)

Average mutual inductance between the stator windings.

#### Dependencies

This parameter is visible only if **Stator
parameterization** is set to `Specify Ls,
Lm, and Ms`.

### **Stator resistance per phase, Rs** — Resistance `0.7` `Ohm` (default)

Resistance of each of the stator windings.

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

### Iron Losses

For more information on calculating iron losses, see Calculating Iron Losses.

### **Model** — Iron losses modeling option `Specify magnetizing resistance` (default) | `Specify tabulated Steinmetz coefficients` | `Tabulate with current and speed`

Whether to enable iron losses modeling.

#### Dependencies

To enable this parameter, set **Modeling
fidelity** to `Tabulate Ld and
Lq`.

### **Magnetizing resistance** — Magnetizing resistance for iron losses `inf` `Ohm` (default)

Magnetizing resistance. The value must be greater than zero. The
default value is `inf`, which implies that there are no
iron losses.

#### Dependencies

To enable this parameter, either set **Model** to
`Specify magnetizing resistance` or set
**Modeling fidelity** to `Constant
Ld and Lq`.

### **Rotor hysteresis loss coefficient, k\_hr(id,iq)** — Rotor hysteresis loss coefficient `zeros(3, 3)` `W/Hz` (default)

Hysteresis loss coefficient of the rotor depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients`.

### **Rotor eddy current loss coefficient, k\_Jr(id,iq)** — Rotor eddy current loss coefficient `zeros(3, 3)` `W/Hz^2` (default)

Eddy current loss coefficient of the rotor depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients`.

### **Rotor excess current loss coefficient, k\_er(id,iq)** — Rotor excess current loss coefficient `zeros(3, 3)` `W/Hz^1.50000` (default)

Excess current loss coefficient of the rotor depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients`.

### **Stator hysteresis loss coefficient, k\_hs(id,iq)** — Stator hysteresis loss coefficient `zeros(3, 3)` `W/Hz` (default)

Hysteresis loss coefficient of the stator depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients`.

### **Stator eddy current loss coefficient, k\_Js(id,iq)** — Stator eddy current loss coefficient `zeros(3, 3)` `W/Hz^2` (default)

Eddy current loss coefficient of the stator depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients`.

### **Stator excess current loss coefficient, k\_es(id,iq)** — Stator excess current loss coefficient `zeros(3, 3)` `W/Hz^1.50000` (default)

Excess current loss coefficient of the stator depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients`.

### **Rotor speed vector, w** — Rotor speed `[1000, 2000]` `rpm` (default)

Vector of rotor speed at which the iron loss is tabulated.

#### Dependencies

To enable this parameter, set **Model** to
`Tabulate with current and
speed`.

### **Rotor iron loss table, Pr(id,iq,w)** — Rotor iron loss table `zeros(3, 3, 2)` `W` (default)

Iron losses of the rotor tabulated on the *d*-axis
and *q*-axis currents, and rotor speed.

#### Dependencies

To enable this parameter, set **Model** to
`Tabulate with current and
speed`.

### **Stator iron loss table, Ps(id,iq,w)** — Stator iron loss table `zeros(3, 3, 2)` `W` (default)

Iron losses of the stator tabulated on the *d*-axis
and *q*-axis currents, and rotor speed.

#### Dependencies

To enable this parameter, set **Model** to
`Tabulate with current and
speed`.

### Mechanical

### **Rotor inertia** — Inertia `0.01` `kg*m^2` (default)

Inertia of the rotor attached to mechanical translational port
**R**.

### **Rotor Damping** — Damping `0` `N*m/(rad/s)` (default)

Rotary damping.

### **Rotor angle definition** — Angle `Angle between the a-phase magnetic axis and the d-axis` (default) | `Angle between the a-phase magnetic axis and the q-axis`

Reference point for the rotor angle measurement. If you select the
default value, the rotor and *a*-phase fluxes are
aligned for a zero-rotor angle. Otherwise, an *a*-phase
current generates the maximum torque value for a zero-rotor angle.

### Thermal

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Measurement temperature** — Measurement temperature `298.15` `K` (default)

The temperature for which motor parameters are quoted.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default)

Coefficient α in the equation relating resistance to temperature, as
described in Thermal Model for Actuator Blocks. The default value is for
copper.

### **Thermal mass for each stator winding** — Thermal mass for each stator winding `100` `J/K` (default)

The thermal mass value for the A, B, and C windings. The thermal mass
is the energy required to raise the temperature by one degree.

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K` (default)

The thermal mass of the rotor, that is, the energy required to raise
the temperature of the rotor by one degree.

### **Percentage of total iron losses associated with the rotor** — Percentage of total iron losses `50` (default)

Percentage of total iron losses associated with the rotor.

#### Dependencies

To enable this parameter, either set **Modeling
fidelity** to `Costant Ld and
Lq` or **Stator parameterization**
to `Specify Ls, Lm, and Ms`.

## Libraries

Simscape / Electrical / Electromechanical / Reluctance & Stepper

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
`Open-end`. The Synchronous Reluctance Machine block then exposes each end
of the windings by enabling the corresponding electrical conserving ports.

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Synchronous reluctance machine with sinusoidal flux distribution

The Synchronous Reluctance Machine block represents a
synchronous reluctance machine (SynRM) with sinusoidal flux distribution. The figure
shows the equivalent electrical circuit for the stator windings.

You can also model the stator windings either in a delta-wound or in an open-end
configuration by setting **Winding type** to
`Delta-wound` or `Open-end`,
respectively.

### Motor Construction

The diagram shows the motor construction with a single pole-pair on the rotor. For
the axes convention shown, when rotor mechanical angle
*θr* is zero, the
*a*-phase and permanent magnet fluxes are aligned. The block
supports a second rotor axis definition for which rotor mechanical angle is defined
as the angle between the *a*-phase magnetic axis and the rotor
*q*-axis.

### Equations

The combined voltage across the stator windings is

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
- *ψa*,
  *ψb*, and
  *ψc* are the magnetic
  fluxes that link each stator winding.

The permanent magnet, excitation winding, and the three stator windings contribute
to the flux that links each winding. The total flux is defined as

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]

where:

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

θe=Nθr+rotor offset

Laa=Ls+Lmcos(2θe)

Lbb=Ls+Lmcos(2(θe−2π/3))

Lcc=Ls+Lmcos(2(θe+2π/3))

Lab=Lba=−Ms−Lmcos(2(θe+π/6))

Lbc=Lcb=−Ms−Lmcos(2(θe+π/6−2π/3))

and

Lca=Lac=−Ms−Lmcos(2(θe+π/6+2π/3))

where:

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
  fluctuation. This value is the amplitude of the fluctuation in
  self-inductance and mutual inductance with changing rotor angle.
- *Ms* is the stator mutual
  inductance. This value is the average mutual inductance between the stator
  windings.

### Simplified Equations

Applying the Park transformation to the block electrical defining equations
produces an expression for torque that is independent of rotor angle.

The Park transformation, *P*, is defined as

P=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212],

where *θe* is the
electrical angle. The electrical angle depends on the rotor mechanical angle and the
number of pole pairs such that

θe=Nθr+rotor offset

where:

- *N* is the number of pole pairs.
- *θr* is the rotor mechanical
  angle.

Applying the Park transformation to the first two electrical defining equations
produces equations that define the behavior of the block:

vd=Rsid+Lddiddt−NωiqLq,

vq=Rsiq+Lqdiqdt+NωidLd,

v0=Rsi0+L0di0dt,

T=32N(iqidLd−idiqLq)

Jdωdt=T−TL−Bmω,

where:

- *id*,
  *iq*, and
  *i0* are the
  *d*-axis, *q*-axis, and
  zero-sequence currents, defined by

  [idiqi0]=P[iaibic],

  where *ia*,
  *ib*, and
  *ic* are the stator
  currents.
- *vd*,
  *vq*, and
  *v0* are the
  *d*-axis, *q*-axis, and
  zero-sequence currents, defined by

  [vdvqv0]=P[vavbvc],

  where *va*,
  *vb*, and
  *vc* are the stator
  currents.
- The *dq0* inductances are defined, respectively
  as

  - Ld=Ls+Ms+32Lm
  - Lq=Ls+Ms−32Lm
  - L0=Ls−2Ms.
- *Rs* is the stator resistance
  per phase.
- *N* is the number of rotor pole pairs.
- *T* is the rotor torque. For the
  Synchronous Reluctance Machine block,
  torque flows from the machine case (block conserving port
  **C**) to the machine rotor (block conserving port
  **R**).
- *TL* is the load
  torque.
- *Bm* is the rotor
  damping.
- *ω* is the rotor mechanical rotational speed.
- *J* is the rotor inertia.

### Calculating Iron Losses

To calculate iron losses in the Synchronous Reluctance
Machine block, choose whether you want to model them by
specifying magnetizing resistance, parameterize them based on the Steinmetz
equation, or if you want to tabulate the losses as a function of currents and rotor
speed.

If you set the **Stator parameterization** parameter to
`Specify Ls, Lm, and Ms` or `Specify Ld,
Lq, and L0` and **Modeling fidelity** to
`Constant Ld and Lq`, then specify the
**Magnetizing resistance** parameter to model iron
losses.

In the **Iron Losses** settings, if you set the
**Model** parameter to `Specify tabulated Steinmetz
coefficients` or `Tabulate with current and
speed`, the iron losses are applied to the mechanical side as a
reduction in the electrical torque:

τloss=sign(w)Ploss,stator+Ploss,rotorabs(w)+wmin,

where *wmin* is minimum
rotor speed to start taking iron losses into account, and it is equal to
`1`
`rad/s`.

The total power dissipated is equal to the sum of the iron losses and the copper losses:

Pdissipated=τlossw+Raia2+Rbib2+Rcic2.

**Steinmetz parameterization method**

To model the iron losses based on the Steinmetz equation, set the
**Stator parameterization** parameter to
`Specify Ld, Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld and
Lq`. The Steinmetz method scales for different motor speeds or
electrical frequencies so that iron loss data is only required as function of
motor currents.

If, in the **Iron losses** settings, you set the
**Model** parameter to `Specify tabulated
Steinmetz coefficients`, the iron losses are given by:

Ploss,rotor(f)=khr(id,iq)f+kJr(id,iq)f2+ker(id,iq)f1.5Ploss,stator(f)=khs(id,iq)f+kJs(id,iq)f2+kes(id,iq)f1.5

where:

- *khr(id,iq)*
  is the **Rotor hysteresis loss coefficient,
  k\_hr(id,iq)**.
- *kJr(id,iq)*
  is the **Rotor eddy current loss coefficient,
  k\_Jr(id,iq)**.
- *ker(id,idq)*
  is the **Rotor excess current loss coefficient,
  k\_er(id,iq)**.
- *khs(id,iq)*
  is the **Stator hysteresis loss coefficient,
  k\_hs(id,iq)**.
- *kJs(id,iq)*
  is the **Stator eddy current loss coefficient,
  k\_Js(id,iq)**.
- *kes(id,iq)*
  is the **Stator excess current loss coefficient,
  k\_es(id,iq)**.
- f=wnPolePairs2π is the electrical frequency, in Hz.

**Tabulate with current and speed**

To model the iron losses by tabulating them independently for rotor and
stator, set the **Stator parameterization** parameter to
`Specify Ld, Lq, and L0` and the **Modeling
fidelity** parameter to `Tabulated Ld and
Lq`.

Then, if in the **Iron losses** settings, you set the
**Model** parameter to `Tabulate with current
and speed`, the iron losses are given by:

Ploss(id,iq,w)=tablelookup(Ptable,id,iq,w).

where *w* is the **Rotor speed
vector, w** parameter.

**Iron losses with thermal ports**

If you expose the thermal ports of the block, the power dissipated in each
phase act as heat sources in the stator and in the rotor:

PdissA=Raia2+Ploss,stator3PdissB=Rbib2+Ploss,stator3PdissC=Rcic2+Ploss,stator3PdissR=Ploss,rotor

If you specify the magnetizing resistance, the iron loss in the rotor is equal
to a percentage of the total iron losses. This percentage remains constant and
does not depend on other states:

Ploss,rotor=percentrotor100Piron loss,total.

Then the remaining iron loss is distributed among the different stator phases:

Ploss,stator=(1−percentrotor100)Piron loss,total.

### Model Thermal Effects

You can expose thermal ports to model the effects of losses
that convert power to heat. To expose the thermal ports, set the **Modeling
option** parameter to either:

- `No thermal port` — The block does not contain thermal
  ports.
- `Show thermal port` — The block contains multiple thermal
  conserving ports.

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
