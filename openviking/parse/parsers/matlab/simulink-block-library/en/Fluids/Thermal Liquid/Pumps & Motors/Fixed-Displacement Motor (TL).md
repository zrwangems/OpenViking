---
type: simulink-block
title: 'Fixed-Displacement Motor (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pumps & Motors'
documentation_page: 'fixeddisplacementmotortl'
documentation_source_path: 'ref/fixeddisplacementmotortl.html'
language: en
---

# Fixed-Displacement Motor (TL)

## Ports

### Input

### **EV** — Volumetric efficiency, unitless physical signal

Physical signal input port for the volumetric efficiency coefficient.
The input signal has an upper bound at the **Maximum volumetric
efficiency** parameter value and a lower bound at the
**Minimum volumetric efficiency** parameter
value.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **EM** — Mechanical efficiency, unitless physical signal

Physical signal input port for the mechanical efficiency coefficient.
The input signal has an upper bound at the **Maximum mechanical
efficiency** parameter value and a lower bound at the
**Minimum mechanical efficiency** parameter
value.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **LV** — Volumetric loss, m^3/s physical signal

Physical signal input port for the volumetric loss, defined as the
internal leakage flow rate between the motor inlets.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.

### **LM** — Mechanical loss, N\*m physical signal

Physical signal input port for the mechanical loss, defined as the
friction torque on the rotating motor shaft.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.
### Conserving

### **A** — Motor inlet thermal liquid

Thermal liquid conserving port associated with the motor inlet.

### **B** — Motor outlet thermal liquid

Thermal liquid conserving port associated with the motor
outlet.

### **C** — Motor Case mechanical rotational

Mechanical rotational conserving port associated with the motor
case.

### **R** — Motor Shaft mechanical rotational

Mechanical rotational conserving port associated with the rotational
motor shaft.

## Parameters

### Parameters

### **Leakage and friction parameterization** — Parameterization of leakage flow rate and friction torque `Analytical` (default) | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Tabulated data - torque and speed` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

Method to compute flow-rate and torque losses due to internal leaks
and friction. When you select `Analytical`, the
block parameters are generally available from component data sheets.
When you select `Tabulated data - volumetric and mechanical
efficiencies` or `Tabulated data -
volumetric and mechanical losses`, the block uses
lookup tables to map pressure drop, angular velocity, and displacement
to component efficiencies or losses. When you select
`Tabulated data - torque and speed`, you
can enter the torque and shaft speed as functions of flow rate and
pressure drop by using the **Torque table T(q,dp)** and
**Shaft speed table w(q,dp)** parameters.

When you select `Input signal - volumetric and mechanical
efficiencies` or `Input signal - volumetric
and mechanical losses`, the block performs the leakage
flow rate and friction torque calculations the same as the
`Tabulated data - volumetric and mechanical
efficiencies` or `Tabulated data -
volumetric and mechanical losses` settings,
respectively. When you select `Input signal - volumetric and
mechanical efficiencies` the block enables the physical
signal ports, **EV** and **EM**. You
use these ports to specify the volumetric and mechanical efficiency.
When you select `Input signal - volumetric and mechanical
losses` the block enables the physical signal ports,
**LV** and **LM**. You use these
ports to specify the volumetric and mechanical losses.

### **Displacement** — Fluid volume displaced per shaft rotation `30` `cm^3/rev` (default) | positive scalar

Fluid volume displaced per shaft rotation. The block maintains this
value throughout the simulation.

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

Pressure drop that corresponds to the given volumetric efficiency.
These values are typically available at standard operating conditions in
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

### **Volumetric efficiency at nominal conditions** — Volumetric efficiency at the specified nominal conditions `0.92` (default) | positive scalar

Volumetric efficiency for the given conditions. The block defines the
volumetric efficiency as the ratio of actual to ideal volumetric flow
rates. These values are typically available at standard operating
conditions in manufacturer data sheet. The block uses this parameter to
calculate the internal leakage flow rate.

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

Torque to overcome the seal friction and induce rotation of the
mechanical shaft. This torque is the load-independent component of the
total friction torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Pressure drop vector, dp** — Vector of pressure data for tabulated data parameterization `[.1, 1, 2] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular
parameterization of leakage and torque friction. This vector forms an
independent axis with the **Shaft angular velocity vector,
w** parameter or the **Flow rate vector,
q** parameter for the 3-D dependent **Volumetric
efficiency table, e\_v(dp,w)**, **Mechanical
efficiency table, e\_m(dp,w)**, **Torque table,
T(q,dp)**, and **Shaft speed table,
w(q,dp)** parameters. The vector elements must be listed in
ascending order.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to either:

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Tabulated data - volumetric and
  mechanical losses`
- `Tabulated data - torque and
  speed`

### **Shaft angular velocity vector, w** — Angular velocities at which to specify the volumetric and mechanical efficiencies `[250, 500, 1000, 2000, 3000, 4000]` `rpm` | vector

Shaft angular velocities for the corresponding tabular efficiency
data. The vector must be at least two elements in strictly increasing
order.

You can specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to the block description for the
operation modes corresponding to the various quadrants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies` or
`Tabulated data - volumetric and mechanical
losses`.

### **Flow rate vector, q** — Vector of flow rate data `[.125, .25, .5, 1, 1.5, 2] * 1e-3 m^3/s` (default) | 1-by-*n* vector

Vector of flow rate data for the tabular parameterization of torque
and speed. This vector forms an independent axis with the
**Pressure drop vector, dp** parameter for the 3-D
dependent **Torque table, T(q,dp)** and **Shaft
speed table, w(q,dp)** parameters. The vector elements must
be listed in ascending order.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
torque and speed`.

### **Volumetric efficiency table, e\_v(dp,w)** — Volumetric efficiencies for given pressure drops and angular velocities `[.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91]` | matrix

Volumetric efficiencies for the given fluid pressure drops and shaft
angular velocities.. The efficiencies must be in the range (0,1].
*M* and *N* are the sizes of the
specified lookup-table vectors:

- *M* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

You can specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to the block description for the
operation modes corresponding to the various quadrants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Mechanical efficiency table, e\_m(dp,w)** — Mechanical efficiencies for given pressure drops and angular velocities `[.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984]` | matrix

Mechanical efficiencies for the given fluid pressure drops and shaft
angular velocities. The efficiencies must be in the range (0,1].
*M* and *N* are the sizes of the
specified lookup-table vectors:

- *M* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

You can specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to the block description for the
operation modes corresponding to the various quadrants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Volumetric loss table, q\_loss(dp,w)** — Internal leakage flow rates for corresponding pressure drops and angular velocities `[.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3` `m^3/s`

Volumetric losses at the specified fluid pressure drops and shaft
angular velocities. Volumetric loss is defined here as the internal
leakage volumetric flow rate between port A and port B.
*M* and *N* are the sizes of the
specified lookup-table vectors:

- *M* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

You can specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to the block description for the
operation modes corresponding to the various quadrants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical losses`.

### **Mechanical loss table, torque\_loss(dp,w)** — Friction torques for the corresponding pressure drops and angular velocities `[.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626]` `N*m`

Mechanical losses for the given pressure drops and shaft angular
velocities. The block defines mechanical loss as the friction torque due
to seals and internal components. *M* and
*N* are the sizes of the specified lookup-table vectors:

- *M* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

You can specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to the block description for the
operation modes corresponding to the various quadrants. The tabulated
data for the mechanical losses must obey the convention in the figure,
with positive values at positive angular velocities and negative values
at negative angular velocities.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical losses`.

### **Torque table, T(q,dp)** — Torque values for tabulated data parameterization `[.47, 4.72, 9.35; .47, 4.7, 9.36; .47, 4.7, 9.4; .47, 4.7, 9.41; .47, 4.7, 9.46; .47, 4.68, 9.5] N*m` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of torque values
at the specified fluid pressure drop and flow rate. The block employs
linear interpolation between table elements. *M* and
*N* are the sizes of the correlated vectors:

- *M* is the number of elements in the
  **Flow rate vector, q**
  parameter.
- *N* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.

If your table has unknown data points in any of the four corners, use
`NaN` in place of these values.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
torque and speed`.

### **Shaft speed table, w(q,dp)** — Shaft speed for tabulated data parameterization `[205, 80, 35; 455, 330, 285; 955, 831, 780; 1950, 1830, 1780; 2940, 2775, 2680; 3940, 3780, 3640] rpm` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of shaft speed
values at the specified fluid pressure drop and flow rate. The block
employs linear interpolation between table elements.
*M* and *N* are the sizes of the
correlated vectors:

- *M* is the number of elements in the
  **Flow rate vector, q**
  parameter.
- *N* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.

If your table has unknown data points in any of the four corners, use
`NaN` in place of these values.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
torque and speed`.

### **Minimum volumetric efficiency** — Lower saturation bound on the volumetric efficiency input signal `1e-3` (default) | scalar in the range (0,1)

Smallest allowed value of the volumetric efficiency. The input from
the physical signal port **EV** saturates inputs below
this value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Maximum volumetric efficiency** — Upper saturation bound on the volumetric efficiency input signal `1` (default) | positive scalar

Largest allowed value of the volumetric efficiency. The input from the
physical signal port **EV** saturates inputs above this
value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Minimum mechanical efficiency** — Lower saturation bound on the volumetric efficiency input signal `1e-3` (default) | scalar in the range (0,1)

Smallest allowed value of the mechanical efficiency. The input from
the physical signal port **EM** saturates inputs below
this value.

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
transition between motoring and pumping modes. The block uses a
hyperbolic tangent function to smooth the leakage flow rate and friction
torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies` or
`Input signal - volumetric and mechanical
losses`.

### **Angular velocity threshold for motor-pump transition** — Angular velocity at which to initiate a smooth transition between pump and motor modes `100` `rpm` (default) | scalar

Shaft angular velocity below which the block begins to transition
between motoring and pumping modes. The block uses the hyperbolic
tangent function to smooth the leakage flow rate and friction
torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies` or
`Input signal - volumetric and mechanical
losses`.

### **Cross-sectional area at ports A and B** — Flow area at the component inlet and outlet `0.01` `m^2` (default) | positive scalar

Flow area at the component inlet and outlet. The areas are assumed
equal.

### **Check if operating beyond the range of supplied tabulated data** — Whether to notify if extents of supplied data are surpassed `None` (default) | `Warning` | `Error`

Whether to notify if the extents of the supplied data are surpassed.
Select `Warning` to be notified when the block
uses values beyond the supplied data range. Select
`Error` to stop the simulation when the
block uses values beyond the supplied data range.

When **Leakage and friction parameterization** to
`Tabulated data - torque and speed`, this
parameter also checks if the block is operating in a region of supplied
`NaN` values.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to:

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Tabulated data - volumetric and
  mechanical losses`
- `Tabulated data - torque and
  speed`

### **Check if operating outside of motor mode** — Simulation warning mode for operating conditions outside motoring mode `None` (default) | `Warning`

Simulation warning mode for operating conditions outside the motoring
mode. The block generates a warning if the motor transitions to pumping
mode. Select `Warning` to be notified when this
transition occurs. The warning does not cause simulation to stop.

### **Check if pressures are less than motor minimum pressure** — Whether to notify if fluid exit pressure is low `None` (default) | `Warning` | `Error`

Whether to notify if the fluid at port **A** or
**B** experiences low pressure. Select
`Warning` to be notified when the outlet
pressure falls below a minimum specified value. Select
`Error` to stop the simulation when the
outlet pressure falls below a minimum specified value.

The parameter helps identify potential conditions for cavitation, when
the fluid pressure falls below the fluid vapor pressure.

### **Motor minimum pressure** — Lower threshold to acceptable pressure at the motor outlet `0.101325 MPa` (default) | positive scalar

Lower threshold of acceptable pressure at the motor inlet or
outlet.

#### Dependencies

To enable this parameter, set **Check if pressures are
less than motor minimum pressure** to either:

- `Warning`
- `Error`

### Faults

### **Displacement fault** — Option to model displacement fault `Add fault`

Option to model a displacement fault in the block. When a fault occurs, the
displacement scales by the value of the **Faulted displacement
factor** parameter. To add a fault, click the **Add
fault** hyperlink.

### **Faulted displacement factor** — Factor by which to scale faulted displacement `0.5` (default) | positive scalar

Factor that the block uses to scale the displacement when a fault
occurs.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Displacement fault** parameter.

### **Leakage fault** — Option to model leakage fault `Add fault`

Option to model a leakage fault in the block. When a fault occurs, the
volumetric efficiencies or losses scale by the value of the **Faulted
leakage factor** parameter. To add a fault, click the **Add
fault** hyperlink.

### **Faulted leakage factor** — Factor by which to scale leakage fault `2.0` (default) | positive scalar

Factor that the block uses to scale the volumetric efficiencies or losses when
a fault occurs.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Leakage fault** parameter.

### **Shaft friction torque fault** — Option to model shaft friction torque fault `Add fault`

Option to model a shaft friction torque fault in the block. When a fault
occurs, the mechanical efficiencies or losses scale by the value of the
**Faulted shaft friction torque factor** parameter. To add
a fault, click the **Add fault** hyperlink.

### **Faulted shaft friction torque factor** — Factor by which to scale shaft friction torque fault `2.0` (default) | positive scalar

Factor that the block uses to scale the mechanical efficiencies or losses when
a fault occurs.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Shaft friction torque fault**
parameter.

## Libraries

Simscape / Fluids / Thermal Liquid / Pumps & Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2024b: Model faults with the Simscape faults interface

The Fixed-Displacement Motor (TL) block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

### R2024b: Parameterize block using torque and shaft speed

You can now parameterize the block by specifying the torque and shaft speed by
setting the **Leakage and friction parameterization** parameter to
`Tabulated data - torque and speed`. Manufacturers
often provide motor datasheets in this format.

### R2024b: Check if port pressures are less than pump minimum pressure

Use the **Check if pressures are less than pump minimum
pressure** parameter to determine what happens if the fluid at port
**A** or **B** falls below the value of the
**Pump pressure minimum** parameter.

### R2024a: Check if block operates outside range of calculated data

The **Check if operating beyond the quadrants of supplied tabulated
data** parameter has been renamed to **Check if operating
beyond the range of supplied tabulated data**. You can enable the
**Check if operating beyond the range of supplied tabulated
data** parameter to check if the block is operating beyond the data
specified in the block parameters, that is, operating in a region where the block
has extended the data.

## Description

Hydraulic-mechanical power conversion device

The Fixed-Displacement Motor (TL) block represents a device that
extracts power from a thermal liquid network and delivers it to a mechanical rotational
network. The motor displacement is fixed at a constant value that you specify through
the **Displacement** parameter.

Ports **A** and **B** represent the motor inlets.
Ports **R** and **C** represent the motor drive shaft
and case. During normal operation, a pressure drop from port **A** to
port **B** causes a positive flow rate from port **A**
to port **B** and a positive rotation of the motor shaft relative to
the motor case. This operation mode is referred to here as *forward
motor*.

**Operation Modes**

The block has four modes of operation. The working mode depends on the pressure drop
from port **A** to port **B**, *Δp =
p*A – *p*B
and the angular velocity, *ω = ω*R –
*ω*C:

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

The response time of the motor is considered negligible in comparison with the system
response time. The motor is assumed to reach steady state nearly instantaneously and is
treated as a quasi-steady component.

### Energy Balance

Mechanical work done by the pump is associated with an energy exchange. The
governing energy balance equation is:

ϕA+ϕB−Phydro=0,

where:

- *Φ*A and
  *Φ*B are energy flow rates
  at ports **A** and **B**,
  respectively.
- *P*hydro is the motor
  hydraulic power. It is a function of the pressure difference between the
  motor ports: Phydro=Δpm˙ρ

The motor mechanical power is generated from the motor torque,
*τ* and angular velocity, *ω*:

Pmech=Tω.

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
- *D* is the **Displacement**
  parameter.
- *ω* is the shaft angular velocity.
- *Δp* is the pressure drop from inlet to
  outlet.

### Analytical Leakage and Friction Parameterization

If you set **Leakage and friction parameterization** to
`Analytical`, the block calculates leakage and friction
from constant values of shaft velocity, pressure drop, and friction torque. The
leakage flow rate, which is correlated with the pressure differential over the
motor, is calculated as:

m˙leak=KρavgΔp,

where:

- *Δp* is *pA*
  – *pB*.
- *ρ*avg is the average fluid
  density.
- *K* is the Hagen-Poiseuille coefficient for
  analytical loss,

  K=Dωnom(1ηv,nom−1)Δpnom,

  where:

  - *D* is the value of the
    **Displacement** parameter.
  - *ωnom* is the
    value of the **Nominal shaft angular
    velocity** parameter.
  - *ηv, nom* is the
    value of the **Volumetric efficiency at nominal
    conditions** parameter.
- *Δpnom* is the value of the
  **Nominal pressure drop** parameter.

The friction torque, which is correlated with shaft angular velocity, is
calculated as:

τfr=(τ0+k|Δp|)tanh(4ω5×10−5ωnom),

where:

- *τ*0 is the value of the
  **No-load torque** parameter.
- *k* is the friction torque vs. pressure gain
  coefficient at nominal displacement, which is determined from the value
  of the **Mechanical efficiency at nominal
  conditions** parameter,
  *ηm*:

  k=τfr,nom−τ0Δpnom.

  *τfric* is
  the friction torque at nominal conditions:

  τfr,nom=(1−ηm,nom)DΔpnom.
- *Δp* is the pressure drop between ports
  **A** and **B**.
- *ω* is the relative shaft angular velocity, or ωR−ωC.

### Tabulated Leakage and Friction Parameterizations

When using tabulated data for motor efficiencies or losses, you can provide data
for one or more of the motor operational modes. The signs of the tabulated data
determine the operational regime of the block. When data is provided for less than
four operational modes, the block calculates the complementing data for the other
mode or modes by extending the given data into the remaining quadrants.

**Tabulated Data - Volumetric and Mechanical Efficiencies**

When you set **Leakage and friction parameterization** to
`Tabulated data - volumetric and mechanical
efficiencies`, the leakage flow rate is

m˙Leak=m˙Leak,Motor(1+α)2+m˙Leak,Pump(1−α)2,

and the friction torque is

τFriction=τFriction,Motor1+α2+τFriction,Pump1−α2,

where:

- *α* is a numerical smoothing parameter for the
  motor-pump transition.
- m˙Leak,Motor is the leakage flow rate in motor mode.
- m˙Leak,Pump is the leakage flow rate in pump mode.
- *τ*Friction,Motor is the
  friction torque in motor mode.
- *τ*Friction,Pump is the
  friction torque in pump mode.

The smoothing parameter *α* is given by the hyperbolic function

α=tanh(4ΔpΔpThreshold)·tanh(4ωωThreshold)·tanh(4DDThreshold),

where:

- *Δp*Threshold is the
  specified value of the **Pressure drop threshold for
  motor-pump transition** block parameter.
- *ω*Threshold is the
  specified value of the **Angular velocity threshold for
  motor-pump transition** block parameter.
- *D*Threshold is the
  specified value of the **Angular velocity threshold for
  motor-pump transition** block parameter.

The leakage flow rate is calculated from the volumetric efficiency, a quantity
that is specified in tabulated form over the
*Δp*–*ɷ*–*D* domain via
the **Volumetric efficiency table** block parameter. When
operating in motor mode (quadrants **1** and
**3** of the
*Δp*–*ɷ*–*D* chart shown
in the Operation Modes figure), the
leakage flow rate is:

m˙Leak,Motor=(1−ηv)m˙,

where *η*v is the
volumetric efficiency, obtained either by interpolation or extrapolation of the
tabulated data. Similarly, when operating in pump mode (quadrants
**2** and **4** of the
*Δp*–*ɷ*–*D* chart), the
leakage flow rate is:

m˙Leak,Pump=−(1−ηv)m˙Ideal.

The friction torque is similarly calculated from the mechanical efficiency, a
quantity that is specified in tabulated form over the
*Δp*–*ɷ*–*D* domain via
the **Mechanical efficiency table** block parameter. When
operating in motor mode (quadrants **1** and
**3** of the
*Δp*–*ɷ*–*D* chart):

τFriction,Motor=(1−ηm)τIdeal,

where *η*m is the
mechanical efficiency, obtained either by interpolation or extrapolation of the
tabulated data. Similarly, when operating in pump mode (quadrants
**2** and **4** of the
*Δp*–*ɷ*–*D* chart):

τFriction,Pump=−(1−ηm)τ.

**Tabulated Data - Volumetric and Mechanical Losses**

When you set **Leakage and friction parameterization** to
`Tabulated data - volumetric and mechanical
losses`, the leakage (volumetric) flow rate is specified directly
in tabulated form over the *Δp*–*ɷ* domain:

qLeak=qLeak(Δp,ω).

The mass flow rate due to leakage is calculated from the
volumetric flow rate:

m˙Leak=ρqLeak.

The friction torque is

τFriction=τLoss(Δp,ω)tanh(4ωωthreshold),

where *q*Leak(*Δp*,*ω*) and *τ*Loss(*Δp*,*ω*) are the volumetric and mechanical losses, obtained through
interpolation or extrapolation of the tabulated data specified via the
**Volumetric loss table** and **Mechanical loss
table** block parameters.

**Tabulated Data - Torque and Speed Parameterization**

When you set **Leakage and friction parameterization** to
`Tabulated data - torque and speed`, the block
calculates the volumetric loss table,
*qloss,TLU* and the mechanical loss
table, *τloss,TLU*, as

qloss,TLU=qTLU−DωTLUτloss,TLU=DΔpTLU−TTLU

where:

- *qTLU* is the value of the
  **Flow rate vector, q** parameter.
- *ωTLU* is the value of the
  **Shaft speed table, w(q,dp)**
  parameter.
- *ΔpTLU* is the value of
  the **Pressure drop vector, dp** parameter.
- *TTLU* is the value of the
  **Torque table, T(q,dp)** parameter.

If the supplied values for the **Shaft speed table, w(q,dp)**
and **Torque table, T(q,dp)** parameters do not cover all four
quadrants, the block extends the data by

- Symmetrically mirroring the values of the **Pressure drop
  vector, dp** and **Flow rate vector,
  q** parameters to contain negative values.
- Symmetrically extending the values of the volumetric loss table,
  *qloss,TLU*, to
  additional quadrants. The signs of these extended values match the
  sign *ΔpTLU* in each
  quadrant.
- Calculating the extended values of the shaft speed vector,
  *ωTLU*, from the
  extended values of the flow rate vector and volumetric loss table, ωTLU=qTLU−qloss,TLUD.
- Symmetrically extending the values of the mechanical loss table,
  *τloss,TLU*, to
  additional quadrants. The signs of these extended values match the
  sign *ωTLU* in each
  quadrant.

If your data tables have unknown data points in any of the four corners or the
**Shaft speed table, w(q,dp)** or **Torque table,
T(q,dp)** parameters, use `NaN` in place of these
values. The block fills in the `NaN` elements in the resulting
volumetric loss table and mechanical loss table with nearest extrapolation with
respect to pressure drop. The block adjusts the signs in the extrapolated
mechanical loss table to match the sign of the corresponding elements in the
shaft speed vector, *ωTLU*, where ωTLU=qTLU−qloss,TLUD.

After extending or filling in the unknown data, the block uses linear
interpolation and nearest extrapolation to calculate the volumetric and
mechanical loss tables during simulation

qloss=tablelookup(qTLU,ΔpTLU,qloss,TLU,Q,Δp,interpolation=linear,extrapolation=nearest)τloss=tablelookup(qTLU,ΔpTLU,τloss,TLU,Q,Δp,interpolation=linear,extrapolation=nearest)

where Q=m˙Aρavg.

### Input Signal Parameterizations

When you set **Leakage and friction parameterization** to
`Input signal - volumetric and mechanical
efficiencies`, the leakage flow rate and friction torque calculations
are identical to the `Tabulated data - volumetric and mechanical
efficiencies` setting. The volumetric and mechanical efficiency
lookup tables are replaced with physical signal inputs that you specify through
ports **EV** and **EM**.

The efficiencies are positive quantities with value between `0`
and `1`. Input values outside of these bounds are set equal to the
nearest bound (`0` for inputs smaller than `0`,
`1` for inputs greater than `1`). The
efficiency signals are saturated at the **Minimum volumetric
efficiency** or **Minimum mechanical efficiency**  and
**Maximum volumetric efficiency** or **Maximum
mechanical efficiency** .

When you set **Leakage and friction parameterization** to
`Input signal - volumetric and mechanical losses`, the
leakage flow rate and friction torque calculations are identical to the
`Tabulated data - volumetric and mechanical losses`
setting. The volumetric and mechanical loss lookup tables are replaced with physical
signal inputs that you specify through ports **LV** and
**LM**.

The block expects the inputs to be positive. It sets the signs automatically from
the operating conditions established during simulation—more precisely, from the
*Δp*–*ɷ* quadrant in which the component
happens to be operating.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

You can model a displacement fault, leakage, or a shaft friction torque fault.

When you enable the **Displacement fault** parameter, the block scales
the displacement by the value of the **Faulted displacement factor**
parameter when the fault triggers,

DFault=fDD,

where *fD* is the value of the **Faulted
displacement factor** parameter. When the **Leakage and friction
parameterization** parameter is `Analytical`, the
block does not use the faulted displacement value to calculate the Hagen-Poiseuille
coefficient or the friction torque.

When you enable the **Leakage fault** parameter and **Leakage and
friction parameterization** is `Analytical`,
`Tabulated data - volumetric and mechanical efficiencies`, or
`Input signal - volumetric and mechanical efficiencies`, the
faulted volumetric efficiency is

ηv,Fault=ηvfLeak,

where *fLeak* is the value of the
**Faulted leakage factor** parameter and
*ηv* is the volumetric efficiency. When
**Leakage and friction parameterization** is
`Analytical`, the block uses the faulted volumetric efficiency
to calculate the Hagen-Poiseuille coefficient.

When **Leakage and friction parameterization** is `Tabulated
data - volumetric and mechanical losses`, `Input signal -
volumetric and mechanical losses`, or `Tabulated data - torque
and speed`, the faulted leakage volumetric flow rate is

qLeak,Fault=fLeakqLeak.

When **Leakage and friction parameterization** is
`Tabulated data - torque and speed`, the block calculates
*qLeak* from the shaft speed and torque
parameters.

When you enable the **Shaft friction torque fault** parameter and
**Leakage and friction parameterization** is
`Analytical`, `Tabulated data - volumetric and
mechanical efficiencies`, or `Input signal - volumetric and
mechanical efficiencies`, the faulted mechanical efficiency is

ηm,Fault=ηmfFriction,

where *fFriction* is the value
of the **Shaft friction torque fault** parameter and
*ηm* is the mechanical efficiency. When
**Leakage and friction parameterization** is
`Analytical`, the block uses the faulted mechanical efficiency
to calculate the friction torque.

When **Leakage and friction parameterization** is `Tabulated
data - volumetric and mechanical losses`, `Input signal -
volumetric and mechanical losses`, or `Tabulated data - torque
and speed`, the faulted friction torque is

τFriction,Fault=fFrictionτFriction.

When **Leakage and friction parameterization** is
`Tabulated data - torque and speed`, the block calculates
*τLeak* from the shaft speed and torque
parameters.

### Assumptions and Limitations

- The motor is treated as a quasi-steady component.
- The effects of fluid inertia and elevation are ignored.
- The motor wall is rigid.
- External leakage is ignored.
