---
type: simulink-block
title: 'BLDC'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'bldc'
documentation_source_path: 'ref/bldc.html'
language: en
---

# BLDC

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

### **R** — Motor rotor mechanical

Mechanical rotational conserving port associated with the motor
rotor.

### **C** — Motor case mechanical

Mechanical rotational conserving port associated with the motor
case.

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

### **Selected part** — Predefined parameterization option `<click to select>` (default)

Option to parameterize the block to represent components by specific suppliers. Click the
**<click to select>** hyperlink to open the Block
Parameterization Manager window. For more information about the Block Parameterization
Manager, see Load Predefined Parameterizations.

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of losses that convert
power to heat.

### Rotor

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Back EMF profile** — Back EMF profile `Perfect trapezoid - specify maximum flux linkage` (default) | `Perfect trapezoid - specify maximum rotor-induced back emf` | `Tabulated - specify flux partial derivative with respect to rotor angle` | `Tabulated - specify rotor-induced back emf as a function of rotor angle`

Parameterization for defining the permanent magnet flux distribution
as a function of rotor angle. Choose:

- `Perfect trapezoid - specify maximum flux
  linkage` to specify the maximum flux linkage
  for the permanent magnet and the rotor angle where the back EMF
  is constant. The block assumes a perfect trapezoid for the back
  EMF.
- `Perfect trapezoid - specify maximum rotor-induced
  back emf` to specify the maximum rotor-induced
  back EMF and the corresponding rotor speed. The block assumes a
  perfect trapezoid for the back EMF.
- `Tabulated - specify flux partial derivative with
  respect to rotor angle` to specify values for
  the partial derivative of flux linkage and the corresponding
  rotor angles.
- `Tabulated - specify rotor-induced back emf as a
  function of rotor angle` to specify the
  measured back EMF constant and the corresponding rotor speed and
  angles.

### **Maximum permanent magnet flux linkage** — Maximum permanent magnet flux linkage `0.03` `Wb` (default)

Peak permanent magnet flux linkage with any of the stator
windings.

#### Dependencies

To enable this parameter, set **Back EMF
profile** to `Perfect trapezoid - specify
maximum flux linkage`.

### **Rotor angle over which back emf is constant** — Rotor angle over which back EMF is constant `pi / 12` `rad` (default)

Rotor angle range over which the permanent magnet flux linking the
stator winding is constant. This angle is θF in
the figure that shows the Trapezoidal Rate of Change of Flux.

#### Dependencies

To enable this parameter, set **Back EMF
profile** to `Perfect trapezoid - specify
maximum flux linkage` or `Perfect
trapezoid - specify maximum rotor-induced back
emf`.

### **Maximum rotor-induced back emf** — Maximum rotor-induced back EMF `9.6` `V` (default)

Peak rotor-induced back EMF into the stator
windings.

#### Dependencies

To enable this parameter, set **Back EMF
profile** to `Perfect trapezoid - specify
maximum rotor-induced back emf`.

### **Rotor-induced back emf** — Rotor-induced back EMF `[0, -9.6, -9.6, 9.6, 9.6, 0]` `V` (default)

Vector of values for the rotor-induced back EMF as a function of rotor
angle. The first and last values must be the same, and are normally both
zero. For more information, see the **Corresponding rotor
angles** parameter. First and last values are the same
because flux is cyclic with period 2π/N, where N is the number of permanent magnet pole
pairs.

#### Dependencies

To enable this parameter, set **Back EMF
profile** to `Tabulated - specify
rotor-induced back emf as a function of rotor
angle`.

### **Flux linkage partial derivative with respect to rotor angle** — Flux linkage partial derivative with respect to rotor angle `[0, -.1528, -.1528, .1528, .1528, 0]` `Wb/rad` (default)

Vector of values for the partial derivative of flux linkage (where
flux linkage is flux times number of winding turns) with respect to
rotor angle. The first and last values must be the same, and are
normally both zero. For more information, see the
**Corresponding rotor angles** parameter. First and
last values are the same because flux is cyclic with period 2π/N, where *N* is the number of permanent
magnet pole pairs.

### **Corresponding rotor angles** — Corresponding rotor angles `[0, 7.5, 22.5, 37.5, 52.5, 60]` `deg` (default)

Vector of rotor angles where the flux linkage partial derivative or
rotor-induced back EMF is defined. Rotor angle is defined as the angle
between the *a*-phase magnetic axis and the
*d*-axis. That is, when the angle is zero, the
magnetic fields due to the rotor and the *a*-phase
winding align. This definition is used regardless of your block setting
for rotor angle definition. The first value is zero, and the last value
is 2π/N, where *N* is the number of permanent
magnet pole pairs.

#### Dependencies

To enable this parameter, set **Back EMF
profile** to `Tabulated - specify flux
partial derivative with respect to rotor angle` or
`Tabulated - specify rotor-induced back emf as a
function of rotor angle`.

### **Rotor speed used for back emf measurement** — Rotor speed used for back EMF measurement `600` `rpm` (default)

Specify the rotor speed corresponding to the maximum rotor-induced
back EMF.

#### Dependencies

To enable this parameter, set **Back EMF
profile** to `Perfect trapezoid - specify
maximum rotor-induced back emf` or
`Tabulated - specify rotor-induced back emf as a
function of rotor angle`.

### **Number of pole pairs** — Number of pole pairs `6` (default)

Number of permanent magnet pole pairs on the
rotor.

### **Rotor angle definition** — Reference point for the rotor angle measurement `Angle between the a-phase magnetic axis and the d-axis` (default) | `Angle between the a-phase magnetic axis and the q-axis`

Reference point for the rotor angle measurement. The default value is
`Angle between the a-phase magnetic axis and the
d-axis`. This definition is shown in the Motor Construction figure. When you
select this value, the rotor and *a*-phase fluxes are
aligned when the rotor angle is zero.

The other value you can choose for this parameter is `Angle
between the a-phase magnetic axis and the q-axis`. When you
select this value, the *a*-phase current generates
maximum torque when the rotor angle is zero.

### Stator

### **Winding type** — Windings configuration `Wye-wound` (default) | `Delta-wound` | `Open-end`

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

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0`.

### **Stator parameterization** — Stator parameterization `Specify Ld, Lq, and L0` (default) | `Specify Ls, Lm, and Ms`

Choose `Specify Ld, Lq, and L0` or
`Specify Ls, Lm, and Ms`.

### **Stator d-axis inductance, Ld** — Stator d-axis inductance `0.00022` `H` (default)

D-axis inductance.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Constant Ld and Lq`.

### **Stator q-axis inductance, Lq** — Stator q-axis inductance `0.00022` `H` (default)

Q-axis inductance.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Constant Ld and Lq`.

### **Direct-axis current vector, iD** — Direct-axis current vector `[-200, 0, 200]` `A` (default)

Direct-axis current vector, iD.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Tabulated Ld and Lq`.

### **Quadrature-axis current vector, iQ** — Quadrature-axis current vector `[-200, 0, 200]` `A` (default)

Quadrature-axis current vector, iQ.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Tabulated Ld and Lq`.

### **Ld matrix, Ld(id,iq)** — Ld matrix `0.00022 * ones(3, 3)` `H` (default)

Ld matrix.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Tabulated Ld and Lq`.

### **Lq matrix, Lq(id,iq)** — Lq matrix `0.00022 * ones(3, 3)` `H` (default)

Lq matrix.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Tabulated Ld and Lq`.

### **Stator zero-sequence inductance, L0** — Stator zero-sequence inductance `0.00016` `H` (default)

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

### **Stator self-inductance per phase, Ls** — Stator self-inductance per phase `0.0002` `H` (default)

Average self-inductance of each of the three stator windings.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ls, Lm, and
Ms`.

### **Stator inductance fluctuation, Lm** — Stator inductance fluctuation `0` `H` (default)

Fluctuation in self-inductance and mutual inductance of the stator
windings with rotor angle.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ls, Lm, and
Ms`.

### **Stator mutual inductance, Ms** — Stator mutual inductance `0.00002` `H` (default)

Average mutual inductance between the stator windings.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ls, Lm, and
Ms`.

### **Stator resistance per phase, Rs** — Stator resistance per phase `0.013` `Ohm` (default)

Resistance of each of the stator windings.

### **Zero sequence** — Zero sequence option `Include` (default) | `Exclude`

Option to include or exclude zero-sequence terms.

- `Include` — Include zero-sequence terms. To prioritize model fidelity, use this default setting. Using this option:

  - Results in an error for simulations that use the Partitioning solver. For more information, see Increase Simulation Speed Using the Partitioning Solver.
  - Exposes the **Stator zero-sequence inductance,
    L0** parameter.
- `Exclude` — Exclude zero-sequence terms. To prioritize simulation speed for desktop simulation or real-time deployment, select this option.

#### Dependencies

To enable this parameter, set **Winding Type** to
`Wye-wound`.

### Iron Losses

### **Model** — Enable Iron losses computation `None` (default) | `Empirical`

Specify the iron losses computational model.

### **Open-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — Open-circuit iron losses `[0, 0, 0]` `W` (default)

Row vector, of length 3, of the open-circuit iron losses due to
hysteresis, Eddy, and excess losses, respectively, at the frequency
specified by **Electrical frequency at which losses
determined**.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### **Short-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — Short-circuit iron losses `[0, 0, 0]` `W` (default)

Row vector, of length 3, of the short-circuit iron losses due to
hysteresis, Eddy, and excess losses, respectively, at the frequency
specified by **Electrical frequency at which losses
determined**.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### **Electrical frequency at which losses determined** — Electrical frequency at which losses determined `60` `Hz` (default)

Electrical frequency at which the open-circuit and short-circuit iron
losses were measured.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### **Short-circuit RMS current for short-circuit iron losses** — Short-circuit RMS current for short-circuit iron losses `95` `A` (default)

The resulting short-circuit RMS phase current when measuring the
short-circuit losses.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### Mechanical

### **Rotor inertia** — Rotor inertia `0.01` `kg*m^2` (default)

Inertia of the rotor attached to mechanical translational port
**R**. The value can be zero.

### **Rotor damping** — Rotor damping `0` `N*m/(rad/s)` (default)

Rotary damping.

### Temperature Dependence

These parameters appear only for blocks with exposed thermal ports.

### **Measurement temperature** — Measurement temperature `298.15` `K` (default)

The temperature for which motor parameters are quoted.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default)

Coefficient α in the equation relating resistance to temperature, as
described in Thermal Model for Actuator Blocks. The default value is for
copper.

### **Permanent magnet flux temperature coefficient** — Permanent magnet flux temperature coefficient `-0.001` `1/K` (default)

The fractional rate of change of permanent magnet flux density with
temperature. It is used to linearly reduce the torque and the induced
back EMF as temperature rises.

### Thermal Port

These parameters appear only for blocks with exposed thermal ports.

### **Thermal mass for each stator winding** — Thermal mass for each stator winding `100` `J/K` (default)

The thermal mass value for the A, B, and C windings. The thermal mass
is the energy required to raise the temperature by one degree.

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K` (default)

The thermal mass of the rotor, that is, the energy required to raise
the temperature of the rotor by one degree.

### **Percentage of main flux path iron losses associated with the rotor** — Percentage of main flux path iron losses associated with the rotor `90` (default)

The percentage of the main flux path iron losses associated with the
magnetic path through the rotor. It determines how much of the iron loss
heating is attributed to the rotor thermal port **HR**,
and how much is attributed to the three winding thermal ports
**HA**, **HB**, and
**HC**.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### **Percentage of cross-tooth flux path iron losses associated with the rotor** — Percentage of cross-tooth flux path iron losses associated with the rotor `30` (default)

The percentage of the cross-tooth flux path iron losses associated
with the magnetic path through the rotor. It determines how much of the
iron loss heating is attributed to the rotor thermal port
**HR**, and how much is attributed to the three
winding thermal ports **HA**, **HB**,
and **HC**.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

## Libraries

Simscape / Electrical / Electromechanical / Permanent Magnet

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2024a: Open-end configuration for stator windings

To model the stator windings of the machine in an open-end configuration, set the
**Winding type** parameter to
`Open-end`. The BLDC block then exposes each end
of the windings by enabling the corresponding electrical conserving ports.

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

## Description

Three-winding brushless direct current motor with trapezoidal flux distribution

The BLDC block models a brushless direct current (BLDC)
motor with a three-phase wye-wound, delta-wound, or open-end stator. Use this block to
model BLDC motors and BLDC servomotors.

BLDC motors have a permanent magnet rotor and a wound stator. The flux distribution is
trapezoidal, presenting a constant back EMF to the drive electronics, which simplifies
motor control. You can use these motors in consumer goods like washing machines,
small-scale quadcopters, pumps, and fans, and in applications like industrial automation
and robotics.

You can choose how to parameterize the permanent magnet flux distribution using the
**Back EMF profile** parameter. Two options allow for simple
parameterization by assuming a perfect trapezoid for the back EMF. You specify either
the flux linkage or the rotor-induced back EMF. The other two options give more accurate
results using tabulated data that you specify. You specify either the flux linkage
partial derivative or the measured back EMF constant for a given rotor speed.

You can use the **Winding type** parameter to specify the
configuration of the windings. This figure shows the equivalent electrical circuit for a
wye-wound stator.

You can also model a delta-wound or open-end stator by setting **Winding
type** to `Delta-wound` or
`Open-end`, respectively.

**Note**

Simscape™
Electrical™ includes several blocks that can model the same type of motor or actuator.
Choose a block that has sufficient modeling detail for the engineering design questions that
you need to answer. Do not use a block that has more modeling detail than you need, because
higher-fidelity models slow down simulation and are more complex to parameterize.

Blocks like the BLDC block model motors with fixed or
parameter-dependent coefficients with a simple equivalent circuit. These models have an
intermediate level of fidelity. Use this block to design controls or systems in actuation
applications, such as robotics and mechatronics, and for efficiency predictions when saturation
and harmonics only weakly impact losses. For more information about choosing the right block to
model your motor at the right level of fidelity, see Choose Blocks to Model Motors or Actuators.

### Motor Construction

This figure shows the motor construction with a single pole-pair on the rotor.

For the axes convention in the preceding figure, the
*a*-phase and permanent magnet fluxes are aligned when rotor
angle *θr* is zero. The block supports a
second rotor-axis definition. For the second definition, the rotor angle is the
angle between the *a*-phase magnetic axis and the rotor
*q*-axis.

### Trapezoidal Rate of Change of Flux

The rotor magnetic field due to the permanent magnets create a trapezoidal rate of
change of flux with rotor angle. The figure shows this rate of change of
flux.

Back EMF is the rate of change of flux, defined by

dΦdt=∂Φ∂θdθdt=∂Φ∂θω,

where:

- *Φ* is the permanent magnet flux linkage.
- *θ* is the rotor angle.
- *ω* is the mechanical rotational speed.

The height `h` of the trapezoidal rate of change of flux profile
is derived from the permanent magnet peak flux.

Integrating ∂Φ∂θ over the range 0 to π/2,

Φmax=h2(θF+θW),

where:

- *Φmax* is the permanent magnet
  flux linkage.
- *h* is the rate of change of flux profile height.
- *θF* is the rotor angle range over
  which the back EMF that the permanent magnet flux induces in the stator is
  constant.
- *θW* is the rotor angle range over
  which back EMF increases or decreases linearly when the rotor moves at
  constant speed.

Rearranging the preceding equation,

h=2Φmax/(θF+θW).

### Electrical Defining Equations

Voltages across the stator windings are defined by

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

where:

- *va*,
  *vb*, and
  *vc* are the external
  voltages applied to the three motor electrical connections.
- *Rs* is the equivalent resistance
  of each stator winding.
- *ia*,
  *ib*, and
  *ic* are the currents
  flowing in the stator windings.
- dψadt,dψbdt, and dψcdt

  are the rates of change of magnetic flux in each stator winding.

The permanent magnet and the three windings contribute to the total flux linking
each winding. The total flux is defined by

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
  *Lba*, etc. are the mutual
  inductances of the stator windings.
- *ψam*,
  *ψbm*, and
  *ψcm* are the permanent
  magnet fluxes linking the stator windings.

The inductances in the stator windings are functions of rotor angle, defined by

Laa=Ls+Lmcos(2θr),

Lbb=Ls+Lmcos(2(θr−2π/3)),

Lcc=Ls+Lmcos(2(θr+2π/3)),

Lab=Lba=−Ms−Lmcos(2(θr+π/6)),

Lbc=Lcb=−Ms−Lmcos(2(θr+π/6−2π/3)),

and

Lca=Lac=−Ms−Lmcos(2(θr+π/6+2π/3)),

where:

- *Ls* is the stator
  self-inductance per phase — The average self-inductance of each
  of the stator windings.
- *Lm* is the stator inductance
  fluctuation — The fluctuation in self-inductance and mutual
  inductance with changing rotor angle.
- *Ms* is the stator mutual
  inductance — The average mutual inductance between the stator
  windings.

The permanent magnet flux linking each stator winding follows the
trapezoidal profile shown in the figure. The block implements the trapezoidal
profile using lookup tables to calculate permanent magnet flux values.

### Simplified Equations

The defining voltage and torque equations for the block are

[vdvqv0]=P([vavbvc]−Nω[∂ψam∂θr∂ψbm∂θr∂ψcm∂θr]),

vd=Rsid+Lddiddt−NωiqLq

vq=Rsiq+Lqdiqdt+NωidLd,

v0=Rsi0+L0di0dt

and

T=32N(iqidLd−idiqLq)+[iaibic][∂ψam∂θr∂ψbm∂θr∂ψcm∂θr],

where:

- *vd*,
  *vq*, and
  *v0* are the
  *d*-axis, *q*-axis, and zero-sequence
  voltages.
- *P* is Park’s Transformation, defined by

  P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5]
- *N* is the number of rotor permanent magnet pole
  pairs.
- *ω* is the rotor mechanical rotational speed.
- ∂ψam∂θr,∂ψbm∂θr, and ∂ψcm∂θr

  are the partial derivatives of instantaneous permanent magnet flux linking
  each phase winding.
- *id*,
  *iq*, and
  *i0* are the
  *d*-axis, *q*-axis, and zero-sequence
  currents, defined by

  [idiqi0]=P[iaibic]
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
- *T* is the rotor torque. Torque flows from the motor case
  (block physical port **C**) to the motor rotor (block
  physical port **R**).

### Calculating Iron Losses

Iron losses are divided into two terms, one representing the main magnetizing
path, and the other representing the cross-tooth tip path that becomes active during
field weakened operation. The iron losses model, which is based on the work of
Mellor [3].

The term representing the main magnetizing path depends on the induced RMS stator
voltage, Vmrms:

POC(Vmrms)=ahkVmrms+ajk2Vmrms2+aexk1.5Vmrms1.5.

This is the dominant term during no-load operation. *k* is the
back EMF constant relating RMS volts per Hz. It is defined as k=Vmrms/f, where *f* is the electrical frequency. The first
term on the right-hand side is the magnetic hysteresis loss, the second is the eddy
current loss and the third is the excess loss. The three coefficients appearing on
the numerators are derived from the values that you provide for the open-circuit
hysteresis, eddy, and excess losses.

The term representing the cross-tooth tip path becomes important when a
demagnetizing field is set up and can be determined from a finite element analysis
short-circuit test. It depends on the RMS EMF associated with the cross-tooth tip
flux, Vdrms\*:

PSC(Vdrms\*)=bhkVdrms\*+bjk2Vdrms\*2+bexk1.5Vdrms\*1.5.

The three numerator terms are derived from the values you provide for the
short-circuit hysteresis, eddy, and excess losses.

### Predefined Parameterization

There are multiple available built-in parameterizations for the BLDC block.

This pre-parameterization data allows you to set up the block to represent
components by specific suppliers. The parameterizations of these brushless DC motors
match the manufacturer data sheets. To load a predefined parameterization,
double-click the BLDC block, click the **<click to
select>** hyperlink of the **Selected part** parameter
and, in the Block Parameterization Manager window, select the part you want to use
from the list of available components.

**Note**

The predefined parameterizations of Simscape components use available data sources for the parameter values. Engineering
judgment and simplifying assumptions are used to fill in for missing data. As a result,
expect deviations between simulated and actual physical behavior. To ensure accuracy,
validate the simulated behavior against experimental data and refine component models as
necessary.

For more information about pre-parameterization and for a list of the available
components, see List of Pre-Parameterized Components.

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
