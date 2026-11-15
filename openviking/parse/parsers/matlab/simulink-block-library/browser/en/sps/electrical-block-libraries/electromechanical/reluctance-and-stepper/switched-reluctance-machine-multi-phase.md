---
type: simulink-block
title: 'Switched Reluctance Machine (Multi-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Reluctance and Stepper'
documentation_page: 'switchedreluctancemachinemultiphase'
documentation_source_path: 'ref/switchedreluctancemachinemultiphase.html'
language: en
---

# Switched Reluctance Machine (Multi-Phase)

## Ports

### Conserving

### **R** — Machine rotor mechanical rotational

Mechanical rotational conserving port associated with the machine
rotor.

**Data Types:** `double`

### **C** — Machine case mechanical rotational

Mechanical rotational conserving port associated with the machine
case.

**Data Types:** `double`

### **a1** — *a*-phase positive supply electrical

Electrical positive supply for phase-*a*.

**Data Types:** `double`

### **b1** — *b*-phase positive supply electrical

Electrical positive supply for phase-*b*.

**Data Types:** `double`

### **c1** — *c*-phase positive supply electrical

Electrical positive supply for phase-*c*.

**Data Types:** `double`

### **d1** — *d*-phase positive supply electrical

Electrical positive supply for phase-*d*.

**Data Types:** `double`

### **e1** — *e*-phase positive supply electrical

Electrical positive supply for phase-*e*.

This port is visible if you select
`Five-phase` for the **Number of
stator phases** parameter.

**Data Types:** `double`

### **f1** — *f*-phase positive supply electrical

Electrical positive supply for phase-*f*.

This port is visible if you select
`Six-phase` for the **Number of
stator phases** parameter.

**Data Types:** `double`

### **a2** — *a*-phase negative supply electrical

Electrical negative supply for phase-*a*.

**Data Types:** `double`

### **b2** — *b*-phase negative supply electrical

Electrical negative supply for phase-*b*.

**Data Types:** `double`

### **c2** — *c*-phase negative supply electrical

Electrical negative supply for phase-*c*.

**Data Types:** `double`

### **d2** — *d*-phase negative supply electrical

Electrical negative supply for phase-*d*.

**Data Types:** `double`

### **e2** — *e*-phase negative supply electrical

Electrical negative supply for phase-*e*.

This port is visible if you select
`Five-phase` for the **Number of
stator phases** parameter.

**Data Types:** `double`

### **f2** — *f*-phase negative supply electrical

Electrical negative supply for phase-*f*.

This port is visible if you select
`Six-phase` for the **Number of
stator phases** parameter.

**Data Types:** `double`

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

### **HE** — *e*-phase terminal thermal port thermal

Thermal conserving port associated with stator winding
*e*.

#### Dependencies

To enable this port, set **Modeling option** to `Show
thermal port` and **Number of stator
phases** to `Five-phase`.

### **HF** — *f*-phase terminal thermal port thermal

Thermal conserving port associated with stator winding
*f*.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port` and
**Number of stator phases** to
`Six-phase`.

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

### **Number of stator phases** — Four- or five-phase SRM `Four-phase` (default) | `Five-phase` | `Six-phase`

Type of multiphase SRM in terms of the number of stator phases.

### **Number of rotor poles** — Rotor pole `8` (default) | positive integer

Number of pole pairs on the rotor.

### **Stator resistance per phase** — Resistance `3` `Ohm` (default) | positive scalar

Per-phase resistance of each of the stator windings.

### **Stator parameterization** — Parameterization method `Specify saturated flux linkage` (default) | `Specify flux characteristic`

Method for parameterizing the stator.

#### Dependencies

Selecting `Specify saturated flux
linkage` enables these parameters:

- **Saturated flux linkage**
- **Aligned inductance**
- **Unaligned inductance**

Selecting `Specify flux characteristic`
enables these parameters:

- **Current vector, i**
- **Angle vector, theta**
- **Flux linkage matrix,
  Phi(i,theta)**

### **Saturated flux linkage** — Flux linkage `0.43` `Wb` (default) | positive scalar

Saturated flux linkage per phase.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify saturated
flux linkage`.

### **Aligned inductance** — Inductance `0.0046` `H` (default) | positive scalar

Inductance when the axis of the rotor pole is identical to the axis of the excited
stator pole. The value of this parameter must be greater than the value
of the **Unaligned inductance** parameter.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify saturated
flux linkage`.

### **Unaligned inductance** — Inductance `6.7e-4` `H` (default) | positive scalar

Inductance when the axis between two rotor poles is identical to the axis of the excited
stator pole. The value of this parameter must be less than the value of
the **Aligned inductance** parameter.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify saturated
flux linkage`.

### **Current vector, i** — Current `[0, 50, 100]` `A` (default) | positive vector

Current vector used to identify the flux linkage curve family.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify flux
characteristic`.

### **Angle vector, theta** — Angle `[0, 22.5, 45]` `deg` (default) | positive vector

Angle vector used to identify the flux linkage curve family.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify flux
characteristic`.

### **Flux linkage matrix, Phi(i,theta)** — Flux `[0, 0, 0; .37, .06, .37; .43, .1, .43]` `Wb` (default) | scalar

Flux linkage matrix that defines the flux linkage curve family.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify flux
characteristic`.

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
data`.

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

### **Rotor inertia** — Inertia `0.01` `kg*m^2` (default) | positive scalar

Inertia of the rotor attached to mechanical translational port
**R**.

### **Rotor Damping** — Damping `0` `N*m/(rad/s)` (default) | scalar

Rotary damping.

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

### **Percentage of total iron losses associated with the rotor** — Percentage of total iron losses `50` (default)

Percentage of total iron losses associated with the rotor.

#### Dependencies

To enable this parameter, set **Model** to either
`Tabulate losses from current and
speed` or `Tabulate losses from
current, speed, and angle`.

## Libraries

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Four, five, or six-phase switched reluctance machine (SRM)

The Switched Reluctance Machine (Multi-Phase) block
represents a four-phase, five-phase, or six-phase switched reluctance machine (SRM).

This diagram shows the motor construction for the four-phase machine.

This diagram shows the motor construction for the five-phase machine.

This diagram shows the motor construction for the six-phase machine.

### Equations

The rotor stroke angle for a multiphase machine is

θst=2πNsNr

where:

- *θst* is the stoke
  angle.
- *Ns* is the number of
  phases.
- *Nr* is the number of rotor
  poles.

The torque production capability, *β*, of one rotor pole is

β=2πNr.

The mathematical model for a switched reluctance machine (SRM) is highly nonlinear due to
influence of the magnetic saturation on the flux linkage-to-angle curve,
*λ*(*θph*). The phase
voltage equation for an SRM is

vph=Rsiph+dλph(iph,θph)dt

where:

- *vph* is the voltage per
  phase.
- *Rs* is the stator resistance
  per phase.
- *iph* is the current per
  phase.
- *λph* is the flux linkage per
  phase.
- *θph* is the angle per
  phase.

Rewriting the phase voltage equation in terms of partial derivatives yields this
equation:

vph=Rsiph+∂λph∂iphdiphdt+∂λph∂θphdθphdt.

Transient inductance is defined as

Lt(iph,θph)=∂λph(iph,θph)∂iph,

or more simply as

∂λph∂iph.

Back electromotive force is defined as

Eph=∂λph∂θphωr.

Substituting these terms into the rewritten voltage equation yields this voltage equation:

vph=Rsiph+Lt(iph,θph)diphdt+Eph.

Applying the co-energy formula to equations for torque,

Tph=∂W(θph)∂θr,

and energy,

W(iph,θph)=∫0iphλph(iph,θph)diph

yields an integral equation that defines the instantaneous torque
per phase, that is,

Tph (iph,θph)=∫0iph∂λph(iph,θph)∂θphdiph.

Integrating over the phases gives this equation, which defines
the total instantaneous torque as

T=∑j=1NsTph(j).

The equation for motion is

Jdωdt=T−TL−Bmω

where:

- *J* is the rotor inertia.
- *ω* is the mechanical rotational speed.
- *T* is the rotor torque. For the Switched
  Reluctance Machine block, torque flows from the machine case
  (block conserving port **C**) to the machine rotor
  (block conserving port **R**).
- *TL* is the load
  torque.
- *J* is the rotor inertia.
- *Bm* is the rotor
  damping.

For high-fidelity modeling and control development, use empirical data and finite
element calculation to determine the flux linkage curve in terms of current and
angle, that is,

λph(iph,θph).

For low-fidelity modeling, you can also approximate the curve using analytical
techniques. One such technique [2] uses this exponential function:

λph(iph,θph)=λsat(1−e−iphf(θph)),

where:

- *λsat* is the saturated flux
  linkage.
- *f*(*θr*) is
  obtained by Fourier expansion.

For the Fourier expansion, use the first two even terms of this equation:

f(θph)=a+bcos(Nrθph)

where *a* > *b*,

a= Lmin+Lmax2λsat,

and

b= Lmax−Lmin2λsat.

### Calculating Iron Losses

The Switched Reluctance Machine (Multi-Phase) block
implements the iron losses as a reduction in the electrical torque.

If you set the **Stator parameterization** parameter to
`Specify parametric data`, specify the
**Magnetizing resistance** parameter to model iron
losses.

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

If you expose the thermal ports of the block, the power dissipated in each phase act as
heat sources in the motor and in the rotor:

PdissA=Raia2+PironAPdissB=Rbib2+PironBPdissC=Rcic2+PironCPdissR=PironR

The iron loss in the rotor is equal to a percentage of the total iron losses. This loss
remains constant and does not depend on other states:

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

### Assumptions

A zero rotor angle corresponds to a rotor pole that is aligned perfectly with the
*a*-phase, that is, peak flux.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
