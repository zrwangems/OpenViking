---
type: simulink-block
title: 'Switched Reluctance Machine'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Reluctance and Stepper'
documentation_page: 'switchedreluctancemachine'
documentation_source_path: 'ref/switchedreluctancemachine.html'
language: en
---

# Switched Reluctance Machine

## Ports

### Conserving

### **~1** — Positive three-phase composite terminal electrical

Electrical conserving three-phase
port associated with the positive terminals of the stator
windings.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **~2** — Negative three-phase composite terminal electrical

Electrical conserving three-phase
port associated with the negative terminals of the stator
windings.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **a1** — Positive *a*-phase terminal electrical

Electrical conserving port associated with the positive terminal of
stator winding *a*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **a2** — Negative *a*-phase terminal electrical

Electrical conserving port associated with the negative terminal of
stator winding *a*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b1** — Positive *b*-phase terminal electrical

Electrical conserving port associated with the positive terminal of
stator winding *b*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b2** — Negative *b*-phase terminal electrical

Electrical conserving port associated with the negative terminal of
stator winding *b*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c1** — Positive *c*-phase terminal electrical

Electrical conserving port associated with the positive terminal of
stator winding *c*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c2** — Negative *c*-phase terminal electrical

Electrical conserving port associated with the negative terminal of
stator winding *c*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **R** — Rotor mechanical

Mechanical rotational conserving port associated with the
rotor.

### **C** — Casing mechanical

Mechanical rotational conserving port associated with the stator or
casing.

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

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of losses that convert
power to heat.

### Main

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Number of rotor poles** — Rotor poles `4` (default) | positive integer

Number of rotor poles.

### **Stator resistance per phase** — Resistance `3` `Ohm` (default) | positive scalar

Per-phase resistance of each of the stator windings.

### **Stator parameterization** — Parameterization method `Specify parametric data` (default) | `Specify parametric and geometric data` | `Specify tabulated flux data`

Method for parameterizing the stator.

#### Dependencies

Selecting `Specify parametric data`
enables these parameters:

- **Magnetizing resistance**
- **Saturated flux linkage**
- **Aligned inductance**
- **Unaligned inductance**

Selecting `Specify parametric and geometric
data` enables these parameters:

- **Magnetizing resistance**
- **Saturated flux linkage**
- **Aligned inductance**
- **Unaligned inductance**
- **Angle subtended by each stator
  pole**
- **Angle subtended by each rotor
  pole**
- **Angle over which flux gradient changes are
  smoothed**

Selecting `Specify tabulated flux data`
enables these parameters:

- **Current vector, i**
- **Angle vector, theta**
- **Flux linkage matrix,
  Phi(i,theta)**

### **Magnetizing resistance** — Magnetic losses `inf` `Ohm` (default) | real scalar

The total magnetizing resistance for each of the phase windings. The
default value `inf` indicates that there are no iron
losses.

#### Dependencies

This parameter is exposed when you set **Stator
parameterization** to `Specify parametric
data` or `Specify parametric and
geometric data`.

### **Saturated flux linkage** — Flux linkage `0.43` `Wb` (default) | positive scalar

Saturated flux linkage per phase.

#### Dependencies

This parameter is exposed when you set **Stator
parameterization** to `Specify parametric
data` or `Specify parametric and
geometric data`.

### **Aligned inductance** — Inductance `0.0046` `H` (default) | positive scalar

The value of this parameter must be greater than the value of the
**Unaligned inductance** parameter.

#### Dependencies

This parameter is exposed when you set **Stator
parameterization** to `Specify parametric
data` or `Specify parametric and
geometric data`.

### **Unaligned inductance** — Inductance `6.7e-4` `H` (default) | positive scalar

The value of this parameter must be less than the value of the
**Aligned inductance** parameter.

#### Dependencies

This parameter is exposed when you set **Stator
parameterization** to `Specify parametric
data` or `Specify parametric and
geometric data`.

### **Angle subtended by each stator pole** — Stator tooth angle `45` `deg` (default) | positive scalar

Angle spanned by each stator tooth. This value must be greater than or
equal to the value of **Angle subtended by each rotor
pole**.

#### Dependencies

This parameter is exposed when you set **Stator
parameterization** to `Specify parametric
and geometric data`.

### **Angle subtended by each rotor pole** — Rotor tooth angle `42` `deg` (default) | positive scalar

Angle spanned by each rotor tooth.

#### Dependencies

This parameter is exposed when you set **Stator
parameterization** to `Specify parametric
and geometric data`.

### **Angle over which flux gradient changes are smoothed** — Inflection point smoothing `0.5` `deg` (default) | positive scalar

Angle over which sharp edges in trapezoidal inductance curve are
smoothed. This value must be smaller than the value of **Angle
subtended by each rotor pole**.

#### Dependencies

This parameter is exposed when you set **Stator
parameterization** to `Specify parametric
and geometric data`.

### **Current vector, i** — Current `[0, 50, 100]` `A` (default) | vector

Current vector used to identify the flux linkage curve family.

#### Dependencies

This parameter is exposed when you set **Stator
parameterization** to `Specify tabulated
flux data`.

### **Angle vector, theta** — Angle `[0, 45, 90]` `deg` (default) | vector

Angle vector used to identify the flux linkage curve family.

#### Dependencies

This parameter is exposed when you set **Stator
parameterization** to `Specify tabulated
flux data`.

### **Flux linkage matrix, Phi(i,theta)** — Flux `[0, 0, 0; .37, .06, .37; .43, .1, .43]` `Wb` (default) | matrix

Flux linkage matrix that defines the flux linkage curve family.

#### Dependencies

This parameter is exposed when you set **Stator
parameterization** to `Specify tabulated
flux data`.

### Iron Losses

For more information on calculating iron losses, see Calculating Iron Losses.

### **Model** — Iron losses modeling option `None` (default) | `Tabulate losses from current and speed` | `Tabulate losses from current, speed, and angle`

Whether to enable iron losses modeling.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify tabulated
flux data`.

### **Magnetizing resistance** — Magnetizing resistance for iron losses `inf` `Ohm` (default)

Magnetizing resistance. The value must be greater than zero. The
default value is `inf`, which implies that there are no
iron losses.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify parametric
data` or `Specify parametric and
geometric data`.

### **Rotor speed vector, w** — Rotor speed `[500, 1000, 1500]` `rpm` (default)

Vector of rotor speed at which the iron loss is tabulated.

#### Dependencies

To enable this parameter, set **Model** to either
`Tabulate losses from current and
speed` or `Tabulate losses from
current, speed, and angle`.

### **Iron loss table, Ploss(i,w)** — Iron loss table tabulated on current and speed `zeros(3, 3)` `W` (default)

Mechanical power lost in the shaft due to iron losses in a particular
phase, tabulated as a function of the instantaneous phase current and
the rotor speed.

#### Dependencies

To enable this parameter, set **Model** to
`Tabulate losses from current and
speed`.

### **Iron loss table, Ploss(i,w,theta)** — Iron loss table tabulated on current, speed, and angle `zeros(3, 3, 2)` `W` (default)

Mechanical power lost in the shaft due to iron losses in a particular
phase, tabulated as a function of the instantaneous phase current, the
rotor speed, and the rotor angle.

#### Dependencies

To enable this parameter, set **Model** to
`Tabulate losses from current, speed, and
angle`.

### Mechanical

### **Rotor inertia** — Inertia `0.01` `kg*m^2` (default) | zero or positive scalar

Inertia of the rotor attached to mechanical translational port
**R**.

### **Rotor Damping** — Damping `0` `N*m/(rad/s)` (default) | positive scalar

Rotary damping.

### Thermal

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Resistance temperature coefficient** — Temperature coefficient `3.93e-3` `1/K` (default) | positive scalar

Coefficient α in the equation relating resistance to temperature for
all three windings, as described in Thermal Model for Actuator Blocks. The default value,
`3.93e-3` 1/K, is for copper.

### **Measurement temperature** — Rated temperature `25` `degC` (default) | real scalar

The temperature for which motor parameters are quoted.

### **Winding thermal mass** — Winding thermal mass `100` `J/K` (default) | positive scalar

The thermal mass value for the *a*-,
*b*-, and *c*-windings. The
thermal mass is the energy required to raise the temperature by one
degree.

### **Rotor thermal mass** — Rotor thermal mass `50` `J/K` (default) | positive scalar

The thermal mass of the rotor. The thermal mass is the energy required
to raise the temperature of the rotor by one degree.

### **Percentage of total iron losses associated with the rotor** — Percentage of total iron losses `50` (default)

Percentage of total iron losses associated with the rotor.

## Libraries

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Three-phase switched reluctance machine

The Switched Reluctance Machine block represents a
three-phase switched reluctance machine (SRM). The stator has three pole pairs, carrying
the three motor windings, and the rotor has several nonmagnetic poles. The motor
produces torque by energizing a stator pole pair, inducing a force on the closest rotor
poles and pulling them toward alignment. The diagram shows the motor construction.

Choose this machine in your application to take advantage of these properties:

- Low cost
- Relatively safe failing currents
- Robustness to high temperature operation
- High torque-to-inertia ratio

Use this block to model an SRM using easily measurable or estimable parameters. To
model an SRM using FEM data, see Switched Reluctance Motor Parameterized with FEM Data.

### Equations

**Switched Reluctance Machine Block**

The rotor stroke angle for a three-phase machine is

θst=2π3Nr,

where:

- *θst* is the stoke
  angle.
- *Nr* is the number of
  rotor poles.

The torque production capability, *β*, of one rotor pole is

β=2πNr.

The mathematical model for a switched reluctance machine (SRM) is highly
nonlinear due to influence of the magnetic saturation on the flux
linkage-to-angle,
*λ*(*θph*) curve.
The phase voltage equation for an SRM is

vph=Rsiph+dλph(iph,θph)dt

where:

- *vph* is the voltage per
  phase.
- *Rs* is the stator
  resistance per phase.
- *iph* is the current per
  phase.
- *λph* is the flux linkage
  per phase.
- *θph* is the angle per
  phase.

Rewriting the phase voltage equation in terms of partial derivatives yields
this equation:

vph=Rsiph+∂λph∂iphdiphdt+∂λph∂θphdθphdt.

Transient inductance is defined as

Lt(iph,θph)=∂λph(iph,θph)∂iph,

or more simply as

∂λph∂iph.

Back electromotive force is defined as

Eph=∂λph∂θphωr.

Substituting these terms into the rewritten voltage equation yields this
voltage equation:

vph=Rsiph+Lt(iph,θph)diphdt+Eph.

Applying the co-energy formula to equations for torque,

Tph=∂W(θph)∂θr,

and energy,

W(iph,θph)=∫0iphλph(iph,θph)diph

yields an integral equation that defines the instantaneous
torque per phase, that is,

Tph (iph,θph)=∫0iph∂λph(iph,θph)∂θphdiph.

Integrating over the phases give this equation, which defines
the total instantaneous torque for a three-phase SRM:

T=∑j=13Tph(j).

The equation for motion is

Jdωdt=T−TL−Bmω

where:

- *J* is the rotor inertia.
- *ω* is the mechanical rotational speed.
- *T* is the rotor torque. For the
  Switched Reluctance Machine
  block, torque flows from the machine case (block conserving port
  **C**) to the machine rotor (block conserving
  port **R**).
- *TL* is the load
  torque.
- *J* is the rotor inertia.
- *Bm* is the rotor
  damping.

For high-fidelity modeling and control development, use empirical data and
finite element calculation to determine the flux linkage curve in terms of
current and angle, that is,

λph(iph,θph).

For low-fidelity modeling, you can also approximate the curve using analytical
techniques. One such technique [2] uses this exponential function:

λph(iph,θph)=λsat(1−e−iphf(θph)),

where:

- *λsat* is the saturated
  flux linkage.
- *f*(*θr*)
  is obtained by Fourier expansion.

For the Fourier expansion, use the first two even terms of this equation:

f(θph)=a+bcos(Nrθph)

where *a* > *b*,

a= Lmin+Lmax2λsat,

and

b= Lmax−Lmin2λsat.

**Switched Reluctance Motor Block**

The flux linkage curve is approximated based on parametric and geometric data:

λph(iph,θph)=λsat(1−e−L0(θ)iph/λsat),

where *L0* is the
unsaturated inductance.

The effects of saturation are more prominent as the product of current and
unsaturated inductance approach the saturated flux linkage value. Specify this
value using the **Saturated flux linkage** parameter.

Differentiating the flux equation then gives the winding inductance:

L(θph)=L0(θph)e(−L0(θph)iph/λsat)

The unsaturated inductance varies between a minimum and maximum value. The
minimum value occurs when a rotor pole is directly between two stator poles. The
maximum occurs when the rotor pole is aligned with a stator pole. In between
these two points, the block approximates the unsaturated inductance linearly as
a function of rotor angle. This figure shows the unsaturated inductance as a
rotor pole passes over a stator pole.

In the figure:

- *θR* corresponds to the
  angle subtended by the rotor pole. Set it using the **Angle
  subtended by each rotor pole** parameter.
- *θS* corresponds to the
  angle subtended by the stator pole. Set it using the **Angle
  subtended by each stator pole** parameter.
- *θC* corresponds to the
  angle subtended by this full cycle, determined by
  *2π/2n* where *n* is the
  number of stator pole pairs.

### Calculating Iron Losses

The Switched Reluctance Machine (Multi-Phase) block
implements the iron losses as a reduction in the electrical torque.

If you set the **Stator parameterization** parameter to either
`Specify parametric data` or `Specify
parametric and geometric data`, specify the **Magnetizing
resistance** parameter to model iron losses.

If you set the **Stator parameterization** parameter to
`Specify tabulated flux data`, the block tabulates the
losses as the power lost in each stator phase. The losses for each stator only
depends on the stator current in that phase, the rotor angle (geometrically shifted
to that phase), and the rotor speed. The iron loss power of the rotor is computed as
a percentage of the total iron loss power, as specified in the **Percentage
of total iron losses associated with the rotor** parameter.

If you tabulate the losses with current, speed, and angle, the iron loss torque
reduces the electrical torque of a generic "A" phase:

τelecA=τ(iA,θA)−τloss(iA,w,θA)

where τloss(iA,w,θA)=sign(w)Ploss(abs(iA),abs(w),θA)abs(w)+wmin is the torque loss computed as the mechanical power loss divided
by the rotor speed. *wmin* is the minimum
rotor speed and it is equal to `1`
`rad/s`. This value prevents a division by zero when the
rotor speed is equal to `0`.

If you tabulate the losses in function of only current and speed, the iron loss
torque reduces the electrical torque of a generic "A" phase:

τloss(iA,w)=sign(w)Ploss(abs(iA),abs(w))abs(w)+wmin.

The iron losses are applied to the mechanical side as a reduction in torque. If
you create the iron loss table, *Ploss*,
from FEM results, the FEM tool might express the power lost as electrical power
instead of mechanical power.

The total electrical torque is equal to the sum of the electrical torque of each phase:

τelec=τelecA+τelecB+τelecC.

The total power dissipated is equal to the sum of the iron losses and the copper losses:

Pdissipated=(τlossA+τlossB+τlossC)w+Raia2+Rbib2+Rcic2.

**Iron losses with thermal ports**

If you expose the thermal ports of the block, the power dissipated in each
phase act as heat sources in the motor and in the rotor:

PdissA=Raia2+PironAPdissB=Rbib2+PironBPdissC=Rcic2+PironCPdissR=PironR

The iron loss in the rotor is equal to a percentage of the total iron losses.
This loss remains constant and does not depend on other states:

PironR=percentrotor100(τlossA+τlossB+τlossC)w.

Then the remaining iron loss is distributed among the different stator phases:

PironA=(1−percentrotor100)τlossA wPironB=(1−percentrotor100)τlossB wPironC=(1−percentrotor100)τlossC w

### Model Thermal Effects

You can expose thermal ports to model the effects of losses
that convert power to heat. To expose the thermal ports, set the **Modeling
option** parameter to either:

- `No thermal port` — The block does not contain thermal
  ports.
- `Show thermal port` — The block contains multiple thermal
  conserving ports.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.

### Numerical Smoothing

In practice, magnetic edge effects prevent the inductance from taking a
trapezoidal shape as a rotor pole passes over a stator pole. To model these effects,
and to avoid gradient discontinuities that hinder solver convergence, the block
smooths the gradient *∂L0/∂θ* at inflection
points. To change the angle over which this smoothing is applied, use the
**Angle over which flux gradient changes are smoothed**
parameter.

### Assumptions

The block assumes that a zero rotor angle corresponds to a rotor pole that is
aligned perfectly with the *a*-phase.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
