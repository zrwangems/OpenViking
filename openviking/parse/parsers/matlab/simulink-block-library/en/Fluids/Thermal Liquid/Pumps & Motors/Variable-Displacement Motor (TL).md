---
type: simulink-block
title: 'Variable-Displacement Motor (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pumps & Motors'
documentation_page: 'variabledisplacementmotortl'
documentation_source_path: 'ref/variabledisplacementmotortl.html'
language: en
---

# Variable-Displacement Motor (TL)

## Ports

### Input

### **D** — Displacement volume, cm^3/rev physical signal

Physical signal input port for the volume of fluid displaced per
rotation. A smoothing function eases the transition between positive and
negative input values.

### **EV** — Volumetric efficiency, unitless physical signal

Physical signal input port for the volumetric efficiency coefficient.
The input signal has an upper bound at the **Maximum volumetric
efficiency** parameter value and a lower bound at the
**Minimum volumetric efficiency** parameter
value.

#### Dependencies

This port is exposed only when the block variant is set to
`Input efficiencies`.

### **EM** — Mechanical efficiency, unitless physical signal

Physical signal input port for the mechanical efficiency coefficient.
The input signal has an upper bound at the **Maximum mechanical
efficiency** parameter value and a lower bound at the
**Minimum mechanical efficiency** parameter
value.

#### Dependencies

This port is exposed only when the block variant is set to
`Input efficiencies`.

### **LV** — Volumetric loss, `m^3/s` physical signal

Physical signal input port for the volumetric loss, defined as the
internal leakage flow rate between the motor inlets.

#### Dependencies

This port is exposed only when the block variant is set to
`Input losses`.

### **LM** — Mechanical loss, `N*m` physical signal

Physical signal input port for the mechanical loss, defined as the
friction torque on the rotating motor shaft.

#### Dependencies

This port is exposed only when the block variant is set to
`Input losses`.
### Conserving

### **A** — Motor inlet thermal liquid

Thermal liquid conserving port representing the motor inlet.

### **B** — Motor outlet thermal liquid

Thermal liquid conserving port representing the motor outlet.

### **C** — Motor Case mechanical rotational

Mechanical rotational conserving port representing the motor
case.

### **R** — Motor Shaft mechanical rotational

Mechanical rotational conserving port representing the rotational
motor shaft.

## Parameters

### **Leakage and friction parameterization** — Parameterization of leakage flow rate and friction torque `Analytical` (default) | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

Method to compute flow-rate and torque losses due to internal leaks and
friction. When you select `Analytical`, the block
parameters are generally available from component data sheets. When you
select `Tabulated data - volumetric and mechanical
efficiencies` or `Tabulated data - volumetric
and mechanical losses`, the block uses lookup tables to map
pressure drop, angular velocity, and displacement to component efficiencies
or losses.

When you select `Input signal - volumetric and mechanical
efficiencies` or `Input signal - volumetric and
mechanical losses`, the block performs the leakage flow
rate and friction torque calculations the same as the `Tabulated
data - volumetric and mechanical efficiencies` or
`Tabulated data - volumetric and mechanical
losses` settings, respectively. When you select
`Input signal - volumetric and mechanical
efficiencies` the block enables the physical signal ports,
**EV** and **EM**. You use these ports
to specify the volumetric and mechanical efficiency. When you select
`Input signal - volumetric and mechanical
losses` the block enables the physical signal ports,
**LV** and **LM**. You use these ports
to specify the volumetric and mechanical losses.

### **Nominal displacement** — Displacement at which to specify the volumetric efficiency `30` `cm^3/rev` (default) | positive scalar

Fluid displacement for a given volumetric efficiency. These values are
typically available at standard operating conditions in the manufacturer
data sheet. The block uses this parameter to calculate the leakage flow rate
and friction torque.

### **Nominal shaft angular velocity** — Shaft angular velocity for given volumetric efficiency `1800` `rpm` (default) | scalar

Angular velocity of the rotary shaft that corresponds to the given
volumetric efficiency. These values are typically available at standard
operating conditions in the manufacturer data sheet. The block uses this
parameter to calculate the leakage flow rate and friction torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Nominal pressure drop** — Pressure drop for corresponding volumetric efficiency `10` `MPa` (default) | scalar

Pressure drop that corresponds to the given volumetric efficiency. These
values are typically available at standard operating conditions in
manufacturer data sheet. The block uses this parameter to calculate the
internal leakage flow rate.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Nominal dynamic viscosity** — Dynamic viscosity at which to specify the volumetric efficiency `0.9` `cP` (default) | scalar

Dynamic viscosity of the hydraulic fluid for the given volumetric
efficiency. These values are typically available at standard operating
conditions in manufacturer data sheet. The block uses this parameter to
calculate the internal leakage flow rate.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Volumetric efficiency at nominal conditions** — Volumetric efficiency at the specified nominal conditions `0.92` (default) | scalar in the range (0,1)

Volumetric efficiency for the given conditions. The block defines the
volumetric efficiency as the ratio of actual to ideal volumetric flow rates.
These values are typically available at standard operating conditions in
manufacturer data sheet. The block uses this parameter to calculate the
internal leakage flow rate.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Mechanical efficiency at nominal conditions** — Ratio of actual to ideal mechanical power `0.88` (default) | positive scalar

Ratio of actual mechanical power to ideal mechanical power at nominal
conditions.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **No-load torque** — Minimum torque required to induce shaft rotation `0` `N*m` (default) | scalar

Torque to overcome the seal friction and induce rotation of the mechanical
shaft. This torque is the load-independent component of the total friction
torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Pressure drop vector, dp** — Pressure drops for given volumetric and mechanical efficiencies `[.1, 1, 2]` `MPa` (default) | vector

Pressure drops for the corresponding tabular efficiency data. The vector
must be at least two elements in strictly increasing order.

You can specify the data for a single octant, (*ɷ*,
*Δp*, *D*). Refer to the block
description for the operation modes corresponding to the various
octant.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Shaft angular velocity vector, w** — Angular velocities at which to specify the volumetric and mechanical efficiencies `[250, 500, 1000, 2000, 3000, 4000]` `rpm` | vector

Shaft angular velocities for the corresponding tabular efficiency data.
The vector must be at least two elements in strictly increasing
order.

You can specify the data for a single octant, (*ɷ*,
*Δp*,*D*). Refer to the block
description for the operation modes corresponding to the various
octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies` or
`Tabulated data - volumetric and mechanical
losses`.

### **Displacement vector, D** — Displacements at which to specify the volumetric and mechanical efficiencies `[-30, -19, 19, 30]` `cm^3/rev` (default)

Displacements at which to specify the efficiency tabular data. The vector
must be at least two elements in strictly increasing order.

You can specify the data for a single octant, (*ɷ*,
*Δp*, *D*). Refer to the block
description for the operation modes corresponding to the various
octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Volumetric efficiency table, e\_v(dp,w,D)** — Volumetric efficiencies for given pressure drops, angular velocities, and displacements `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)` | matrix

Volumetric efficiencies at the specified fluid pressure drops, shaft
angular velocities, and displacements. The efficiencies must be in the range
of `0`–`1`. *M*,
*N*, and *L* are the sizes of the
specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in the
  **Shaft angular velocity vector, w**
  parameter.
- *L* is the number of vector elements in the
  **Displacement vector, D**
  parameter.

You can specify the data for a single octant, (*ɷ*,
*Δp*, *D*). Refer to the block
description for the operation modes corresponding to the various
octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Mechanical efficiency table, e\_m(dp,w,D)** — Mechanical efficiencies for given pressure drops, angular velocities, and displacements `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)` | matrix

Mechanical efficiencies corresponding to the specified fluid pressure
drops, shaft angular velocities, and displacements. The efficiencies must be
in the range of `0`–`1`.
*M*, *N*, and *L* are
the sizes of the specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in the
  **Shaft angular velocity vector, w**
  parameter.
- *L* is the number of vector elements in the
  **Displacement vector, D**
  parameter.

You can specify the data for a single octant, (*ɷ*,
*Δp*, *D*). Refer to the block
description for the operation modes corresponding to the various
octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Pressure drop vector, dp** — Pressure drop for corresponding losses `[.1, 1, 2]` `MPa` (default)

Pressure drops for the corresponding tabular loss data. The vector must be
at least two elements in strictly increasing order.

You can specify the data for a single octant, (*ɷ*,
*Δp*, *D*). Refer to the block
description for the operation modes corresponding to the various
octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical losses`.

### **Displacement vector, D** — Displacements at which to specify the volumetric and mechanical losses `[-30, -19, 19, 30]` `cm^3/rev` (default)

Displacements at which to specify the loss tabular data. The vector must
be at least two elements in strictly increasing order.

You can specify the data for a single octant, (*ɷ*,
*Δp*, *D*). Refer to the block
description for the operation modes corresponding to the various
octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical losses`.

### **Volumetric loss table, q\_loss(dp,w,D)** — Internal leakage flow rates for corresponding pressure drops, angular velocities, and displacements `repmat([.0282, .0253, .0241, .0235, .0291, .0325; .2596, .1271, .1017, .0917, .1216, .1142; .7874, .1901, .141, .1211, .1797, .1978] * 1e-3, 1, 1, 4)` `m^3/s`

Volumetric losses at the specified fluid pressure drops, shaft angular
velocities, and displacements. The block defines volumetric loss the
internal leakage volumetric flow rate between port **A**
and port **B**. *M* and
*N* are the sizes of the specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in the
  **Shaft angular velocity vector, w**
  parameter.
- *L* is the number of vector elements in the
  **Displacement vector, D**
  parameter.

You can specify the data for a single octant, (*ɷ*,
*Δp*, *D*). Refer to the block
description for the operation modes corresponding to the various
octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical losses`.

### **Mechanical loss table, torque\_loss(dp,w,D)** — Friction torques for the corresponding pressure drops, angular velocities, and displacements `repmat([.002, .002, .002, .002, .002, .002; .06, .055, .055, .055, .055, .05; .19, .19, .18, .18, .17, .16], 1, 1, 4)` `N*m`

Mechanical losses for the given pressure drops, shaft angular velocities,
and displacements. The block defines mechanical loss as the friction torque
due to seals and internal components. *M* and
*N* are the sizes of the specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in the
  **Shaft angular velocity vector, w**
  parameter.
- *L* is the number of vector elements in the
  **Displacement vector, D**
  parameter.

You can specify the data for a single octant, (*ɷ*,
*Δp*,*D*). Refer to the block
description for the operation modes corresponding to the various octants.
The tabulated data for the mechanical losses must obey the convention in the
figure, with positive values at positive angular velocities and negative
values at negative angular velocities.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical losses`.

### **Minimum volumetric efficiency** — Lower saturation bound on the volumetric efficiency input signal `1e-3` (default) | scalar in the range (0,1)

Smallest allowed value of the volumetric efficiency. The input from the
physical signal port **EV** saturates inputs below this
value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Maximum volumetric efficiency** — Upper saturation bound on the volumetric efficiency input signal `1` (default) | scalar in the range (0,1)

Largest allowed value of the volumetric efficiency. The input from the
physical signal port **EV** saturates inputs above this
value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Minimum mechanical efficiency** — Lower saturation bound on the volumetric efficiency input signal `1e-3` (default) | scalar in the range (0,1)

Smallest allowed value of the mechanical efficiency. The input from the
physical signal port **EM** saturates inputs below this
value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Maximum mechanical efficiency** — Upper saturation bound on the volumetric efficiency input signal `1` (default) | scalar in the range (0,1)

Largest allowed value of the mechanical efficiency. The input from the
physical signal port **EM** saturates inputs above this
value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Pressure drop threshold for motor-pump transition** — Pressure drop at which to initiate a smooth transition between motor and pump modes `1e-3` `MPa` (default) | scalar

Pressure drop from inlet to outlet below which the block begins to
transition between motoring and pumping modes. The block uses a hyperbolic
tangent function to smooth the leakage flow rate and friction torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies` or
`Input signal - volumetric and mechanical
losses`.

### **Angular velocity threshold for motor-pump transition** — Angular velocity at which to initiate a smooth transition between pump and motor modes `100` `rpm` (default) | scalar

Shaft angular velocity below which the block begins to transition between
motoring and pumping modes. The block uses the hyperbolic tangent function
to smooth the leakage flow rate and friction torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies` or
`Input signal - volumetric and mechanical
losses`.

### **Cross-sectional area at ports A and B** — Flow area at the component inlet and outlet `0.01` `m^2` (default) | positive scalar

Flow area at the component inlet and outlet. The areas are assumed
equal.

### **Check if operating beyond the range of supplied tabulated data** — Simulation warning mode for operating conditions outside the range of tabulated data `None` (default) | `Warning`

Simulation warning mode for operating conditions outside the range of
tabulated data. Select `Warning` to be notified
when the fluid pressure drop, shaft angular velocity, or instantaneous
displacement cross outside the specified tabular data. The warning does not
cause simulation to stop.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to:

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Tabulated data - volumetric and mechanical
  losses`
- `Input signal - volumetric and mechanical
  efficiencies`
- `Input signal - volumetric and mechanical
  losses`

### **Check if operating outside of motor mode** — Simulation warning mode for operating conditions outside motoring mode `None` (default) | `Warning`

Simulation warning mode for operating conditions outside the motoring
mode. The block generates a warning if the motor transitions to pumping
mode. Select `Warning` to be notified when this
transition occurs. The warning does not cause simulation to stop.

## Libraries

Simscape / Fluids / Thermal Liquid / Pumps & Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2024a: Check if block operates outside range of calculated data

The **Check if operating beyond the octants of supplied tabulated
data** parameter has been renamed to **Check if operating
beyond the range of supplied tabulated data**. You can enable the
**Check if operating beyond the range of supplied tabulated
data** parameter to check if the block is operating beyond the data
specified in the block parameters, that is, operating in a region where the block
has extended the data.

## Description

Variable-displacement bidirectional thermal liquid motor

The Variable-Displacement Motor block represents a device that extracts
power from a thermal liquid network and delivers it to a mechanical rotational network.
The motor displacement varies during simulation according to the physical signal input
specified at port **D**.

Ports **A** and **B** represent the motor inlets.
Ports **R** and **C** represent the motor drive shaft
and case. During normal operation, a pressure drop from port **A** to
port **B** causes a positive flow rate from port **A**
to port **B** and a positive rotation of the motor shaft relative to
the motor case. This operation mode is referred to here as *forward
motor*.

**Operation Modes**

The block has eight modes of operation. The working mode depends on the pressure gain
from port **A** to port **B**, *Δp =
p*A – *p*B;
the angular velocity, *ω = ω*R –
*ω*C; and the fluid volumetric displacement
at port **D**. The figure above maps these modes to the octants of a
*Δp*-*ω*-*D* chart:

- Mode 1, *Forward Motor*: Flow from port
  **A** to port **B** causes a pressure
  decrease from **A** to **B** and a
  positive shaft angular velocity.
- Mode 2, *Reverse Pump*: Negative shaft angular velocity
  causes a pressure increase from port **B** to port
  **A** and flow from **B** to port
  **A**.
- Mode 3, *Reverse Motor*: Flow from port
  **B** to port **A** causes a pressure
  decrease from **B** to **A** and a
  negative shaft angular velocity.
- Mode 4, *Forward Pump*: Positive shaft angular velocity
  causes a pressure increase from port **A** to port
  **B** and flow from **A** to
  **B**.
- Mode 5, *Reverse Pump*: Positive shaft angular velocity
  causes a pressure increase from port **B** to port
  **A** and flow from **B** to
  **A**.
- Mode 6, *Forward Motor*: Flow from port
  **A** to port **B** causes a pressure
  decrease from **A** to **B** and a
  positive shaft angular velocity.
- Mode 7, *Forward Pump*: Negative shaft angular velocity
  causes a pressure increase from port **A** to port
  **B** and flow from **A** to
  **B**.
- Mode 8, *Reverse Motor*: Flow from
  **B** to **A** causes a pressure
  decrease from **B** to **A** and positive
  shaft angular velocity.

The response time of the motor is considered negligible in comparison with the system
response time. The motor is assumed to reach steady state nearly instantaneously and is
treated as a quasi-steady component.

### Flow Rate and Driving Torque

The mass flow rate generated at the motor is

m˙=m˙Ideal+m˙Leak,

where:

- m˙ is the actual mass flow rate.
- m˙Ideal is the ideal mass flow rate.
- m˙Leak is the internal leakage mas flow rate.

The torque generated at the motor is

τ=τIdeal−τFriction,

where:

- *τ* is the actual torque.
- *τ*Ideal is the ideal
  torque.
- *τ*Friction is the friction
  torque.

**Ideal Flow Rate and Ideal Torque**

The ideal mass flow rate is

m˙Ideal=ρDω,

and the ideal generated torque is

τIdeal=DΔp,

where:

- *ρ* is the average of the fluid densities at
  thermal liquid ports **A** and
  **B**.
- *D* is the displacement specified at physical
  signal port **D**.
- *ω* is the shaft angular velocity.
- *Δp* is the pressure drop from inlet to
  outlet.

### Leakage and friction parameterization

You can parameterize leakage and friction analytically, using tabulated
efficiencies or losses, or by input efficiencies or input losses.

**Analytical**

When you set **Leakage and friction parameterization** to
`Analytical` leakage flow rate is

m˙Leak=KHPρAvgΔpμAvg,

and the friction torque is

τFriction=(τ0+KTP|Δp||D|DNomtanh4ω(5e−5)ωNom),

where:

- *K*HP is the
  Hagen-Poiseuille coefficient for laminar pipe flows. This
  coefficient is computed from the specified nominal
  parameters.
- *μ* is the dynamic viscosity of the thermal
  liquid, taken here as the average of its values at the thermal
  liquid ports.
- *k* is the friction torque vs. pressure gain
  coefficient at nominal displacement, which is determined from the
  **Mechanical efficiency at nominal
  conditions**,
  *ηm,nom*:

  k=τfr,nom−τ0Δpnom.

  *τfr,nom*
  is the friction torque at nominal conditions:

  τfr,nom=(1−ηm,nom)DnomΔpnom.
- *D*Nom is the specified
  value of the **Nominal Displacement** block
  parameter.
- *τ*0 is the specified
  value of the **No-load torque** block
  parameter.
- *ω*Nom is the specified
  value of the **Nominal shaft angular velocity**
  block parameter.
- *Δp*Nom is the specified
  value of the **Nominal pressure drop** block
  parameter. This is the pressure drop at which the nominal volumetric
  efficiency is specified.

The Hagen-Poiseuille coefficient is determined from nominal fluid and
component parameters through the equation

KHP=DNomωNomμNom(1ηv,Nom−1)ΔpNom,

where:

- *ω*Nom is the specified
  value of the **Nominal shaft angular velocity**
  parameter. This is the angular velocity at which the nominal
  volumetric efficiency is specified.
- *μ*Nom is the specified
  value of the **Nominal Dynamic viscosity** block
  parameter. This is the dynamic viscosity at which the nominal
  volumetric efficiency is specified.
- *η*v,Nom is the specified
  value of the **Volumetric efficiency at nominal
  conditions** block parameter. This is the volumetric
  efficiency corresponding to the specified nominal conditions.

**Tabulated Efficiencies**

When you set **Leakage and friction parameterization** to
`Tabulated data - volumetric and mechanical
efficiencies`, the leakage flow rate is

m˙Leak=m˙Leak,Pump(1+α)2+m˙Leak,Motor(1−α)2,

and the friction torque is

τFriction=τFriction,Pump1+α2+τFriction,Motor1−α2,

where:

- *α* is a numerical smoothing parameter for the
  motor-pump transition.
- m˙Leak,Motor is the leakage flow rate in motor mode.
- m˙Leak,Pump is the leakage flow rate in pump mode.
- *τ*Friction,Motor is the
  friction torque in motor mode.
- *τ*Friction,Pump is the
  friction torque in pump mode.

The smoothing parameter *α* is given by the hyperbolic
tangent function

α=tanh(4ΔpΔpThreshold)·tanh(4ωωThreshold)·tanh(4DDThreshold),

where:

- *Δp*Threshold is the
  specified value of the **Pressure gain threshold for
  pump-motor transition** block parameter.
- *ω*Threshold is the
  specified value of the **Angular velocity threshold for
  pump-motor transition** block parameter.
- *D*Threshold is the
  specified value of the **Angular velocity threshold for
  motor-pump transition** block parameter.

The leakage flow rate is calculated from the volumetric efficiency, a quantity
that is specified in tabulated form over the
*Δp*–*ɷ*–*D* domain via
the **Volumetric efficiency table** block parameter. When
operating in pump mode (octants **1** and
**3** of the
*Δp*–*ɷ*–*D* chart shown
in the Operation Modes figure), the
leakage flow rate is:

m˙Leak,Pump=(1−ηv)m˙Ideal,

where *η*v is the
volumetric efficiency, obtained either by interpolation or extrapolation of the
tabulated data. Similarly, when operating in motor mode (octants
**2** and **4** of the
*Δp*–*ɷ*–*D* chart), the
leakage flow rate is:

m˙Leak,Motor=−(1−ηv)m˙.

The friction torque is similarly calculated from the mechanical efficiency, a
quantity that is specified in tabulated form over the
*Δp*–*ɷ*–*D* domain via
the **Mechanical efficiency table** block parameter. When
operating in pump mode (octants **1** and
**3** of the
*Δp*–*ɷ*–*D* chart):

τFriction,Pump=(1−ηm)τ,

where *η*m is the
mechanical efficiency, obtained either by interpolation or extrapolation of the
tabulated data. Similarly, when operating in motor mode (octants
**2** and **4** of the
*Δp*–*ɷ*–*D* chart):

τFriction,Motor=−(1−ηm)τIdeal.

**Tabulated Losses**

When you set **Leakage and friction parameterization** to
`Tabulated data - volumetric and mechanical
losses`, the leakage (volumetric) flow rate is specified directly
in tabulated form over the
*Δp*–*ɷ*–*D*
domain:

qLeak=qLeak(Δp,ω,D).

The mass flow rate due to leakage is calculated from the
volumetric flow rate:

m˙Leak=ρqLeak.

The friction torque is similarly specified in tabulated form:

τFriction=τFriction(Δp,ω,D),

where *q*Leak(*Δp*,*ω*,*D*) and *τ*Friction(*Δp*,*ω*,*D*) are the volumetric and mechanical losses, obtained through
interpolation or extrapolation of the tabulated data specified via the
**Volumetric loss table** and **Mechanical loss
table** block parameters.

**Input Efficiencies**

When you set **Leakage and friction parameterization** to
`Input signal - volumetric and mechanical
efficiencies`, the leakage flow rate and friction torque
calculations are identical to the `Tabulated data - volumetric and
mechanical efficiencies` setting. The volumetric and mechanical
efficiency lookup tables are replaced with physical signal inputs that you
specify through ports **EV** and
**EM**.

The efficiencies are positive quantities with value between
`0` and `1`. Input values outside of these
bounds are set equal to the nearest bound (`0` for inputs
smaller than `0`, `1` for inputs greater than
`1`). The efficiency signals are saturated at the
**Minimum volumetric efficiency** or **Minimum
mechanical efficiency**  and **Maximum volumetric
efficiency** or **Maximum mechanical efficiency**.

**Input Losses**

When you set **Leakage and friction parameterization** to
`Input signal - volumetric and mechanical
efficiencies`, the leakage flow rate and friction torque
calculations are identical to the `Tabulated data - volumetric and
mechanical efficiencies` setting. The volumetric and
mechanical loss lookup tables are replaced with physical signal inputs that you
specify through ports **LV** and **LM**.

The block expects the inputs to be positive. It sets the signs automatically
from the operating conditions established during simulation—more precisely, from
the *Δp*–*ɷ* quadrant in which the component
happens to be operating.

### Energy Balance

Mechanical work done by the motor is associated with an energy exchange. The
governing energy balance equation is:

ϕA+ϕB−Phydro=0,

where:

- *Φ*A and
  *Φ*B are energy flow rates
  at ports **A** and **B**,
  respectively.
- *P*hydro is a function of the
  pressure difference between motor ports: Phydro=Δpm˙ρ.

The motor mechanical power is generated due to torque,
*τ*, and angular velocity, *ω*:

Pmech=τω.

### Assumptions

- Fluid compressibility is negligible.
- Loading on the motor shaft due to inertia, friction, and spring forces is
  negligible.
