---
type: simulink-block
title: 'FEM-Parameterized Synchronous Machine'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'femparameterizedsynchronousmachine'
documentation_source_path: 'ref/femparameterizedsynchronousmachine.html'
language: en
---

# FEM-Parameterized Synchronous Machine

## Ports

### Conserving

### **~** — Three-phase composite electrical

Expandable three-phase port associated with the stator windings. For
more information, see Three-Phase
Ports.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **a** — *A* phase electrical

Electrical conserving port associated with the *A*
phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **b** — *B* phase electrical

Electrical conserving port associated with the *B*
phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **c** — *C* phase electrical

Electrical conserving port associated with the *C*
phase.

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
`Wye-wound` and select the
**Expose neutral port** parameter.

### **fd+** — Field winding positive terminal electrical

Electrical conserving port associated with the field winding positive
terminal.

### **fd-** — Field winding negative terminal electrical

Electrical conserving port associated with the field winding negative
terminal.

### **R** — Machine rotor mechanical rotational

Mechanical rotational conserving port associated with the machine
rotor.

### **C** — Machine case mechanical rotational

Mechanical rotational conserving port associated with the machine
case.

### **HA** — Winding *A* thermal port thermal

Thermal conserving port associated with winding *A*.

#### Dependencies

To enable this port, in the **Thermal Ports**
section, enable the **Model thermal effects**
parameter.

### **HB** — Winding *B* thermal port thermal

Thermal conserving port associated with winding *B*.

#### Dependencies

To enable this port, in the **Thermal Ports**
section, enable the **Model thermal effects**
parameter.

### **HC** — Winding *C* thermal port thermal

Thermal conserving port associated with winding *C*.

#### Dependencies

To enable this port, in the **Thermal Ports**
section, enable the **Model thermal effects**
parameter.

### **HR** — Rotor thermal port thermal

Thermal conserving port associated with the rotor.

#### Dependencies

To enable this port, in the **Thermal Ports**
section, enable the **Model thermal effects**
parameter.

## Parameters

### Flux & Torque

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Option to specify composite or expanded three-phase ports.

### **Winding type** — Stator windings configuration `Wye-wound` (default) | `Delta-wound` | `Open-end`

Configuration of the stator windings, specified as one of these values:

- `Wye-wound` — Specify wye-wound
  stator windings.
- `Delta-wound` — Specify
  delta-wound stator windings. The *A*-phase
  is connected between ports **a** and
  **b**, the *B*-phase
  between ports **b** and
  **c**, and the
  *C*-phase between ports
  **c** and
  **a**.
- `Open-end` — The windings are in
  an open-end configuration. The block exposes each end of the
  windings as electrical connections.

### **Number of pole pairs** — Rotor pole pairs `4` (default) | positive integer

Number of machine pole pairs.

### **Park's convention for tabulated data** — Park convention for tabulated data `Q leads D, rotor angle measured from A-phase to D-axis` (default) | `Q leads D, rotor angle measured from A-phase to Q-axis` | `D leads Q, rotor angle measured from A-phase to D-axis` | `D leads Q, rotor angle measured from A-phase to Q-axis`

Order and reference angle for the Park transform that the block uses
to map the *dq* data to the three windings.

- `Q leads D, rotor angle measured from A-phase
  to D-axis` — Apply a quadrature-direct
  transformation and measure the angle with respect to the
  *D* axis.
- `Q leads D, rotor angle measured from A-phase
  to Q-axis` — Apply a quadrature-direct
  transformation and measure the angle with respect to the
  *Q* axis.
- `D leads Q, rotor angle measured from A-phase
  to D-axis` — Apply a direct-quadrature
  transformation and measure the angle with respect to the
  *D* axis.
- `D leads Q, rotor angle measured from A-phase
  to Q-axis` — Apply a direct-quadrature
  transformation and measure the angle with respect to the
  *Q* axis.

### **Peak current magnitude vector, I** — Peak current magnitudes `[0, 100, 200]` `A` (default) | row vector of nonnegative values

Row vector of current magnitudes at which the block tabulates the flux
linkage. The first element must be `0`. The second
current value must be small relative to the current values at which
magnetic saturation begins to occur. This restriction is necessary
because the derived flux partial derivatives are ill-defined at zero
current, and the block calculates them at this first nonzero current
instead.

### **Current advance angle vector, B** — Current advance angles `[-180, -90, 0, 90, 180]` `deg` (default) | row vector of real values

Row vector of current advance angle values at which the block
calculates the flux linkage. The current advance angle is the angle by
which the current leads the *Q*-axis.

### **Field current vector, If** — Field currents `[0, 2, 4, 6, 8, 10]` `A` (default) | row vector of nonnegative values

Row vector of field current values at which the block calculates the
flux linkage. The first element must be `0`.

### **Rotor angle vector, theta** — Rotor angles `[0, 15, 30, 45, 60, 75, 90]` `deg` (default) | row vector of nonnegative values

Vector of the rotor angles at which the block tabulates the flux linkage. The first
element of this vector must be `0`. The number of pole
pairs is 360/*Θ*max, where *Θ*max
is expressed in degrees. The default value corresponds to a four
pole-pair motor.

### **A-phase flux linkage, F(I,B,If,theta)** — *A*-phase flux linkage `zeros(3, 5, 6, 7)` `Wb` (default) | 4-D array

4-D array of *A*-phase flux linkage values as a
function of the **Peak current magnitude vector, I**,
**Current advance angle vector, B**,
**Field current vector, If**, and **Rotor
angle vector, theta** parameters.

If your flux data is in a different order, use the `permute` function to
reorder it. For an example of this reordering, see the
`ee_ece_table`  function in Import IPMSM Flux Linkage Data from ANSYS Maxwell.

### **Torque matrix, T(I,B,If,theta)** — Torque `zeros(3, 5, 6, 7)` `N*m` (default) | 4-D array

4-D array of the electromagnetic torque applied to the rotor as a
function of the **Peak current magnitude vector, I**,
**Current advance angle vector, B**,
**Field current vector, If**, and **Rotor
angle vector, theta**.

If your flux data is in a different order,use the `permute` function to
reorder it. For an example of this reordering, see the
`ee_ece_table`  function in Import IPMSM Flux Linkage Data from ANSYS Maxwell.

### **Interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Interpolation method for approximating the output value when the input
value is between two consecutive grid points.

- `Linear` — Use an extension of
  the linear algorithm for multidimensional interpolation. Select
  this option to get the best performance.
- `Smooth` — Use a modified
  Akima interpolation algorithm. Select this option to produce a
  continuous surface with continuous first-order
  derivatives.

For more information on interpolation methods, see the PS Lookup Table (4D)
block reference page.

### **Expose neutral port** — Neutral port visibility `Off` (default) | `On`

Option to expose the neutral port of the block.

If you expose the neutral port, the block also models the
zero-sequence currents and parameterizes the zero sequence by using the
**Stator zero-sequence inductance, L0** parameter.

#### Dependencies

To enable this parameter, set **Winding type** to
`Wye-wound`.

### **Stator zero-sequence inductance, L0** — Stator zero-sequence inductance `0.00016` `H` (default) | positive scalar

Zero-sequence inductance.

#### Dependencies

To enable this parameter, set **Winding type** to
`Delta-Wound` or enable the
**Expose neutral port** parameter.

### Resistance

### **Stator resistance per phase** — Stator resistance per phase `0.013` `Ohm` (default) | positive scalar

Resistance of each phase of the stator windings.

### **Field winding resistance** — Resistance of field winding `0.1` `Ohm` (default) | positive scalar

Resistance of the field winding.

### **Resistance temperature coefficient** — Temperature coefficient `3.93e-3` `1/K` (default) | positive scalar

Coefficient *α* in the equation relating resistance
to temperature for all three windings. For more information, see Thermal Model for Actuator Blocks. The default value is for
copper.

#### Dependencies

To enable this parameter, in the **Thermal
Ports** section, enable the **Model thermal
effects** parameter.

### **Measurement temperature** — Resistance measurement temperature `298.15` `k` (default) | nonnegative scalar

Temperature at which the block measures the field winding and stator
resistances.

#### Dependencies

To enable this parameter, in the **Thermal
Ports** section, enable the **Model thermal
effects** parameter.

### Iron Losses

### **Rotor hysteresis loss coefficient, k\_hr(I,B,If)** — Rotor hysteresis loss coefficient `zeros(3, 5, 6)` `W/Hz` (default) | 3-D array of real values

Hysteresis loss coefficient of the rotor. The value depends on the
current magnitude, current phase advance, and field current. The block
uses this value in the Steinmetz equation.

### **Rotor eddy current loss coefficient, k\_Jr(I,B,If)** — Rotor eddy current loss coefficient `zeros(3, 5, 6)` `W/Hz^2` (default) | 3-D array of real values

Eddy current loss coefficient of the rotor. The value depends on the
current magnitude, current phase advance, and field current. The block
uses this value in the Steinmetz equation.

### **Rotor excess current loss coefficient, k\_er(I,B,If)** — Rotor excess current loss coefficient `zeros(3, 5, 6)` `W/Hz^(3/2)` (default) | 3-D array of real values

Excess current loss coefficient of the rotor. The value depends on the
current magnitude, current phase advance, and field current. The block
uses this value in the Steinmetz equation.

### **Stator hysteresis loss coefficient, k\_hs(I,B,If)** — Stator hysteresis loss coefficient `zeros(3, 5, 6)` `W/Hz` (default) | 3-D array of real values

Hysteresis loss coefficient of the stator. The value depends on the
current magnitude, current phase advance, and field current. The block
uses this value in the Steinmetz equation.

### **Stator eddy current loss coefficient, k\_Js(I,B,If)** — Stator eddy current loss coefficient `zeros(3, 5, 6)` `W/Hz^2` (default) | 3-D array of real values

Eddy current loss coefficient of the stator. The value depends on the
current magnitude, current phase advance, and field current. The block
uses this value in the Steinmetz equation.

### **Stator excess current loss coefficient, k\_es(I,B,If)** — Stator excess current loss coefficient `zeros(3, 5, 6)` `W/Hz^(3/2)` (default) | 3-D array of real values

Excess current loss coefficient of the stator. The value depends on
the current magnitude, current phase advance, and field current. The
block uses this value in the Steinmetz equation.

### Mechanical

### **Rotor inertia** — Inertia `0` `kg*m^2` (default) | nonnegative scalar

Inertia of the rotor attached to mechanical translational port
**R**.

### **Rotor Damping** — Damping `0` `N*m*s/rad` (default) | nonnegative scalar

Rotary damping.

### Thermal Ports

### **Model thermal effects** — Option to model thermal effects `Off` (default) | `On`

Option to expose the thermal ports and model the effects of losses
that convert power to heat.

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

**Introduced in R2023a**

### R2024a: Open-end configuration for stator windings

To model the stator windings of the machine in an open-end configuration, set the
**Winding type** parameter to
`Open-end`. The FEM-Parameterized Synchronous Machine block then exposes each end
of the windings by enabling the corresponding electrical conserving ports.

## Description

Synchronous machine defined in terms of magnetic flux linkage

The FEM-Parameterized Synchronous Machine block models the
electrical and mechanical characteristics of an externally excited synchronous machine
or a hybrid excitation permanent magnet synchronous machine (PMSM) for which the
magnetic flux linkage depends nonlinearly on the stator currents, field current, and
rotor angle. Externally excited synchronous machines and PMSMs are also called
synchronous AC motors and doubly-excited synchronous motors, respectively.

Use this block to model an externally excited electric motor or a machine that has a rotor
field winding. This block captures detailed behavior like saturation effects and cogging
torques by importing finite-element-derived lookup tables from a motor design tool. You
can also model a hybrid excitation machine where the permanent magnets and the field
winding generate the rotor flux.

The FEM-Parameterized Synchronous Machine block uses flux
linkage that you must calculate using an external finite element (FE) tool. The block
uses the *A*-phase flux linkage, which is a four-dimensional table that
depends on the stator current magnitude, stator current phase advance, field winding
current, and rotor angle. The block derives the field winding flux linkage by
calculating the *D*-axis flux linkage from the
*A*-phase, *B*-phase, and *C*-phase
flux linkages and by subtracting the flux linkage when the field current is zero.

### Equations

This equation defines the back electromotive force (EMF) of the stator:

[eAeBeC]=[dΨAdtdΨBdtdΨCdt]+P−1[00L0]di0dt,

where

- *eA*,
  *eB*, and
  *eC* are the stator
  winding voltages.
- *ΨA*,
  *ΨB*, and
  *ΨC* are the magnetic
  fluxes that link each stator winding.
- *L0* is the value of the
  **Stator zero-sequence inductance, L0**
  parameter.
- *i0* is the zero-sequence
  current.
- *P* is the Park transform.

To keep the table dimension small, this block does not tabulate the stator flux
linkages with the zero-sequence current. The block then adds the zero-sequence
dynamics with a separate term. If you set the **Winding type**
parameter to `Wye-wound` and do not enable the
**Expose neutral port** parameter, then the zero-sequence
dynamics are zero.

This equation defines the back EMF for the field winding of the rotor:

ef=dΨfdt,

where:

- *Ψf* is the field winding flux
  linkage. These equations define the field winding flux linkage:

  [ΨdΨqΨ0]=P(θ)[ΨA(I,B,θ,if)ΨB(I,B,θ,if)ΨC(I,B,θ,if)]Ψf(I,B,θ,if)=Ψd(I,B,θ,if)−Ψd(I,B,θ,0)
- *ef* is the field winding
  voltage.
- *Ψd*,
  *Ψq*, and
  *Ψ0* are the
  *d*-axis, *q*-axis, and
  zero-sequence fluxes, respectively.
- *ΨA(I,B,θ,if)*,
  *ΨB(I,B,θ,if)*,
  and
  *ΨC(I,B,θ,if)*
  are the *A*-phase, *B*-phase, and
  *C*-phase flux linkages, respectively, tabulated
  with respect to *I*, *B*,
  *θ*, and
  *if*.
- *I* is the stator peak current magnitude.
- *B* is the stator current advance angle.
- *θ* is the rotor angle.
- *Ψf
  (I,B,θ,if)* is the field winding
  flux linkage tabulated with respect to *I*,
  *B*, *θ*, and
  *if*.

*P* is the Park transform, which depends on the option you choose
for the **Park’s convention for tabulated data** parameter.

**Note**

The Park transform option of the **Park’s convention for tabulated
data** parameter must match the version of the Park transform
that you use in the FE tool to generate the flux linkage data.

**Option 1: `Q leads D, rotor angle measured from A-phase to
D-axis`**

Simscape™
Electrical™ motor and machine blocks use this convention internally and
convert all other options to this format.

- *N* is the value of the **Number of pole
  pairs** parameter.
- *θ*r is the rotor
  angle.
- *i*d and
  *i*q are the
  *D*-axis and *Q*-axis
  currents, respectively.
- *i*p is the current magnitude
  and is equal to id2+iq2.
- *β* is the current advance angle and is equal to tan−1(−id/iq).

The corresponding Park transform is

[idiqi0]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)121212][iaibic]

where *i*a,
*i*b, and
*i*c are the
*A*-phase, *B*-phase, and
*C*-phase currents, respectively.

**Option 2: `Q leads D, rotor angle measured from A-phase to
Q-axis`**

- *N* is the value of the **Number of pole
  pairs** parameter.
- *θ*r is the rotor
  angle.
- *i*d and
  *i*q are the
  *D*-axis and *Q*-axis
  currents, respectively.
- *i*p is the current magnitude
  and is equal to id2+iq2.
- *β* is the current advance angle and is equal to tan−1(−id/iq).

The corresponding Park transform is

[idiqi0]=23[sin(Nθr)sin(Nθr−2π3)sin(Nθr+2π3)cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)121212][iaibic]

where *i*a,
*i*b, and
*i*c are the
*A*-phase, *B*-phase, and
*C*-phase currents, respectively.

**Option 3: `D leads Q, rotor angle measured from A-phase to
D-axis`**

- *N* is the value of the **Number of pole
  pairs** parameter.
- *θ*r is the rotor
  angle.
- *i*d and
  *i*q are the
  *D*-axis and *Q*-axis
  currents, respectively.
- *i*p is the current magnitude
  and is equal to id2+iq2.
- *β* is the current advance angle and is equal to tan−1(−id/iq).

The corresponding Park transform is

[idiqi0]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)sin(Nθr)sin(Nθr−2π3)sin(Nθr+2π3)121212][iaibic]

where *i*a,
*i*b, and
*i*c are the
*A*-phase, *B*-phase, and
*C*-phase currents, respectively.

**Option 4: `D leads Q, rotor angle measured from A-phase to
Q-axis`**

- *N* is the value of the **Number of pole
  pairs** parameter.
- *θ*r is the rotor
  angle.
- *i*d and
  *i*q are the
  *D*-axis and *Q*-axis
  currents, respectively.
- *i*p is the current magnitude
  and is equal to id2+iq2.
- *β* is the current advance angle and is equal to tan−1(−id/iq).

The corresponding Park transform is

[idiqi0]=23[−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)121212][iaibic]

where *i*a,
*i*b, and
*i*c are the
*A*-phase, *B*-phase, and
*C*-phase currents, respectively.

### Calculating Iron Losses

The FEM-Parameterized Synchronous Machine block
models iron losses by using the Steinmetz equation. The Steinmetz equation scales
for different motor speeds or electrical frequencies, so the block requires iron
loss data only as a function of motor currents.

The block tabulates the iron losses coefficients with the **Peak current
magnitude vector, I**, **Current advance angle vector,
B**, and **Field current vector, If** parameters:

Protor(f)=khr(Ip,β,If)f+kJr(Ip,β,If)f2+ker(Ip,β,If)f1.5Pstator(f)=khs(Ip,β,If)f+kJs(Ip,β,If)f2+kes(Ip,β,If)f1.5

where:

- *f* is the electrical frequency, in Hz.
- *khr(Ip,β,If)*
  is the **Rotor hysteresis loss coefficient,
  k\_hr(I,B,If)** parameter value.
- *kJr(Ip,β,If)*
  is the **Rotor eddy current loss coefficient,
  k\_Jr(I,B,If)** parameter value.
- *ker(Ip,β,If)*
  is the **Rotor excess current loss coefficient,
  k\_er(I,B,If)** parameter value.
- *khs(Ip,β,If)*
  is the **Stator hysteresis loss coefficient,
  k\_hs(I,B,If)** parameter value.
- *kJs(Ip,β,If)*
  is the **Stator eddy current loss coefficient,
  k\_Js(I,B,If)** parameter value.
- *kes(Ip,β,If)*
  is the **Stator excess current loss coefficient,
  k\_es(I,B,If)** parameter value.

### Modeling Thermal Effects

You can expose thermal ports to model the effects of losses that convert power to
heat. To expose the thermal ports, in the **Thermal Ports**
section, enable the **Model thermal effects** parameter.

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
