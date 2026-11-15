---
type: simulink-block
title: 'Fixed-Displacement Motor (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Pumps and Motors'
documentation_page: 'fixeddisplacementmotoril'
documentation_source_path: 'ref/fixeddisplacementmotoril.html'
language: en
---

# Fixed-Displacement Motor (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Entry or exit port to the motor.

### **B** — Liquid port isothermal liquid

Entry or exit port to the motor.

### **R** — Mechanical port mechanical rotational

Rotating shaft angular velocity and torque.

### **C** — Mechanical port mechanical rotational

Motor casing reference angular velocity and torque.
### Input

### **EV** — Volumetric efficiency physical signal

Motor efficiency for fluid displacement, specified as a physical
signal. The value must be between 0 and 1.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **EM** — Mechanical efficiency physical signal

Motor efficiency for the mechanical extraction of energy, specified as
a physical signal. The value must be between 0 and 1.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **LV** — Leakage flow rate, `m^3/s` physical signal

Motor losses associated with fluid displacement in m^3/s, specified as
a physical signal.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.

### **LM** — Friction torque, `N*m` physical signal

Motor losses associated with the mechanical extraction of energy in
N\*m, specified as a physical signal.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.

## Parameters

### Parameters

### **Leakage and friction parameterization** — Method of calculating leakage flow rate and friction torque `Analytical` (default) | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Tabulated data - torque and speed` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

Parameterization of the leakage and friction characteristics of the
pump.

- In the `Analytical`
  parameterization, the leakage flow rate and the friction
  torque are calculated by analytical equations.
- In the `Tabulated data - volumetric and
  mechanical efficiencies` parameterization,
  the volumetric and mechanical efficiencies are calculated
  from the user-supplied **Pressure drop vector,
  dp** and **Shaft angular velocity
  vector, w** parameters and interpolated from
  the 2-D dependent **Volumetric efficiency table,
  e\_v(dp,w)** and **Mechanical efficiency
  table, e\_m(dp,w)** tables.
- In the `Tabulated data - volumetric and
  mechanical loss` parameterization, the
  leakage flow rate and torque friction are calculated from
  user-supplied **Pressure drop vector, dp**
  and **Shaft angular velocity vector, w**
  parameters and interpolated from the 2-D dependent
  **Volumetric loss table, q\_loss(dp,w)**
  and **Mechanical loss table,
  torque\_loss(dp,w)** tables.
- In the `Tabulated data - torque and
  speed` parameterization, you can enter the
  torque and shaft speed as functions of flow rate and
  pressure drop by using the **Torque table
  T(q,dp)** and **Shaft speed table
  w(q,dp)** parameters.
- In the `Input signal - volumetric and
  mechanical efficiencies` parameterization,
  the volumetric and mechanical efficiencies are received as
  physical signals at ports **EV** and
  **EM**, respectively.
- In the `Input signal - volumetric and
  mechanical loss` parameterization, the
  leakage flow rate and torque friction are received as
  physical signals at ports **LV** and
  **LM**, respectively.

### **Displacement** — Fixed-volume fluid displacement `30 cm^3/rev` (default) | scalar

Amount of fixed-volume fluid displacement.

### **Nominal shaft angular velocity** — Shaft angular velocity `1800 rpm` (default) | scalar

Angular velocity of the shaft under nominal operating
conditions.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Nominal pressure drop** — Pressure drop between fluid entry and exit `10 MPa` (default) | scalar

Motor pressure drop between the fluid entry and exit under nominal
operating conditions.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Volumetric efficiency at nominal conditions** — Ratio of actual flow rate to ideal flow rate at nominal conditions `0.92` (default) | positive scalar

Ratio of actual flow rate to ideal flow rate at nominal
conditions.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **No-load torque** — Baseline torque `0 N*m` (default) | scalar

Minimum value of torque to overcome seal friction and induce shaft
motion.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Mechanical efficiency at nominal conditions** — Ratio of actual torque to ideal torque generated `0.88` (default) | positive scalar

Ratio of actual torque to ideal torque generated at nominal
conditions.

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

### **Shaft angular velocity vector, w** — Vector of angular velocity data for tabulated data parameterization `[250, 500, 1000, 2000, 3000, 4000] rpm` (default) | 1-by-*n* vector

Vector of angular velocity data for the tabular parameterization of
leakage and torque friction. This vector forms an independent axis with
the **Shaft angular velocity vector, w** parameter for
the 3-D dependent **Volumetric efficiency table,
e\_v(dp,w)** and **Mechanical efficiency table,
e\_m(dp,w)** parameters. The vector elements must be listed
in ascending order.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to either:

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Tabulated data - volumetric and
  mechanical losses`

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

### **Volumetric efficiency table, e\_v(dp,w)** — Volumetric efficiency for tabulated data parameterization `[.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91]` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric
efficiencies at the specified fluid pressure drop and shaft angular
velocity. The block employs linear interpolation between table elements.
*M* and *N* are the sizes of the
correlated vectors:

- *M* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Mechanical efficiency table, e\_m(dp,w)** — Mechanical efficiency for tabulated data parameterization `[.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984]` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of mechanical
efficiencies at the specified fluid pressure drop and shaft angular
velocity. The block employs linear interpolation between table elements.
*M* and *N* are the sizes of the
correlated vectors:

- *M* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Volumetric loss table, q\_loss(dp,w)** — Volumetric losses for tabulated data parameterization `[.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3 m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric
efficiencies at the specified fluid pressure drop and shaft angular
velocity. The block employs linear interpolation between table elements.
*M* and *N* are the sizes of the
correlated vectors:

- *M* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical losses`.

### **Mechanical loss table, torque\_loss(dp,w)** — Mechanical losses for tabulated data parameterization `[.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626] N*m` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of mechanical
losses at the specified fluid pressure drop and shaft angular velocity.
The block employs linear interpolation between table elements.
*M* and *N* are the sizes of the
correlated vectors:

- *M* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

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

### **Minimum volumetric efficiency** — Minimum value of volumetric efficiency `1e-3` (default) | positive scalar in the range of (0,1]

Minimum value of volumetric efficiency. If the input signal is below
this value, the volumetric efficiency is set to the minimum volumetric
efficiency.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Maximum volumetric efficiency** — Maximum value of volumetric efficiency `1` (default) | positive scalar

Maximum value of volumetric efficiency. If the input signal is above
this value, the volumetric efficiency is set to the maximum volumetric
efficiency.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Minimum mechanical efficiency** — Minimum value of mechanical efficiency `1e-3` (default) | positive scalar in the range of (0,1]

Minimum value of mechanical efficiency. If the input signal is below
this value, the mechanical efficiency is set to the minimum mechanical
efficiency.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Maximum mechanical efficiency** — Maximum value of mechanical efficiency `1` (default) | positive scalar in the range of (0,1]

Maximum value of mechanical efficiency. If the input signal is above
this value, the mechanical efficiency is set to the maximum mechanical
efficiency.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Pressure drop threshold for motor-pump transition** — Pressure threshold for mode transition `1e-3 MPa` (default) | positive scalar

Threshold pressure drop value for the transition between pump and
motor functionality. A transition region is defined around 0 MPa between
the positive and negative values of the pressure drop threshold. Within
this transition region, the computed leakage flow rate and friction
torque are adjusted according to the transition term
*α* to ensure smooth transition from one mode to
the other.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to either:

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Input signal - volumetric and mechanical
  efficiencies`
- `Input signal - volumetric and mechanical
  losses`

### **Angular velocity threshold for motor-pump transition** — Angular velocity threshold for mode transition `100 rpm` (default) | positive scalar

Threshold angular velocity value for the transition between pump and
motor functionality. A transition region is defined around 0 rpm between
the positive and negative values of the angular velocity threshold.
Within this transition region, the computed leakage flow rate and
friction torque are adjusted according to the transition term
*α* to ensure smooth transition from one mode to
the other.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to either:

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Input signal - volumetric and mechanical
  efficiencies`
- `Input signal - volumetric and mechanical
  losses`

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

### **Check if operating outside of motor mode** — Whether to notify if block operates outside of the motor mode functionality `None` (default) | `Warning` | `Error`

Whether to notify if block operates outside of the motor mode
functionality. This block has four operation modes: forward motor,
reverse motor, reverse pump, and forward pump. Select
`Warning` to be notified when the block
operates in the forward or reverse motor pump modes. Select
`Error` to stop the simulation when the
block operates in the forward or reverse pump modes.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.

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

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2024b: Model faults with the Simscape faults interface

The Fixed-Displacement Motor (IL) block now supports the Simscape™ faults interface. To learn more, see Introduction to Simscape Faults.

### R2024a: Parameterize block using torque and shaft speed

You can now parameterize the block by specifying the torque and shaft speed by
setting the **Leakage and friction parameterization** parameter to
`Tabulated data - torque and speed`. Manufacturers
often provide motor datasheets in this format.

### R2024a: Check if block operates outside range of calculated data

The **Check if operating beyond the quadrants of supplied tabulated
data** parameter has been renamed to **Check if operating
beyond the range of supplied tabulated data**. You can enable the
**Check if operating beyond the range of supplied tabulated
data** parameter to check if the block is operating beyond the data
specified in the block parameters, that is, operating in a region where the block
has extended the data.

## Description

Fixed-displacement motor in isothermal liquid system

The Fixed-Displacement Motor (IL) block models a motor with constant-volume
displacement. The fluid may move from port **A** to port
**B**, called *forward mode*, or from port
**B** to port **A**, called *reverse
mode*. Motor mode operation occurs when there is a pressure drop in the
direction of the flow. Pump mode operation occurs when there is a pressure gain in the
direction of the flow.

Shaft rotation corresponds to the sign of the fluid volume moving through the motor.
Positive fluid displacement at corresponds to positive shaft rotation in forward mode.
Negative fluid displacement corresponds to negative shaft angular velocity in forward
mode.

The block has eight modes of operation. The working mode depends on the
pressure drop from port **A** to port **B**,
*Δp = p*A –
*p*B and the angular velocity, *ω =
ω*R – *ω*C:

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

The motor block has analytical, lookup table, and physical signal parameterizations.
When using tabulated data or an input signal for parameterization, you can choose to
characterize the motor operation based on efficiency or losses.

In the tabulated data and the input signal parameterization options, the threshold
parameters **Pressure drop threshold for motor-pump transition** and
**Angular velocity threshold for motor-pump transition** identify
regions where numerically smoothed flow transition between the motor operational modes
can occur. Choose a transition region that provides some margin for the transition term,
but which is small enough relative to the pressure and angular velocity that it will not
impact calculation results.

### Analytical Leakage and Friction Parameterization

If you set **Leakage and friction parameterization** to
`Analytical`, the block calculates leakage and friction
from constant values of shaft velocity, pressure drop, and friction torque. The
leakage flow rate, which is correlated with the pressure differential over the
motor, is calculated as:

m˙leak=KρavgΔp,

where:

- *Δp* is *p*A
  – *p*B.
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

### Tabulated Data Parameterizations

When using tabulated data for motor efficiencies or losses, you can provide data
for one or more of the motor operational modes. The signs of the tabulated data
determine the operational regime of the block. When data is provided for less than
four operational modes, the block calculates the complementing data for the other
mode(s) by extending the given data into the remaining quadrants.

**Tabulated Data - Volumetric and Mechanical Efficiencies
Parameterization**

The leakage flow rate is

m˙leak=m˙leak,motor(1+α2)+m˙leak,pump(1−α2),

where:

- m˙leak,pump=(ηυ−1)m˙ideal
- m˙leak,motor=(1−ηv)m˙

and *ηv* is the volumetric efficiency,
which is interpolated from the user-provided tabulated data. The transition
term, *α*, is

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold),

where:

- *Δp* is
  *p*A –
  *p*B.
- *p*threshold is the value
  of the **Pressure drop threshold for motor-pump
  transition** parameter.
- *ω* is
  *ω*R –
  *ω*C.
- *ω*threshold is the value
  of the **Angular velocity threshold for motor-pump
  transition** parameter.

The friction torque is

τfr=τfr,motor(1+α2)+τfr,pump(1−α2),

where:

- τfr,pump=(ηm−1)τ
- τfr,motor=(1−ηm)τideal

and *η*m is the
mechanical efficiency, which is interpolated from the user-provided tabulated
data.

**Tabulated Data - Volumetric and Mechanical Losses Parameterization**

The leakage flow rate is

m˙leak=ρavgqloss(Δp,ω),

where *qloss* is interpolated from the
**Volumetric loss table, q\_loss(dp,w)** parameter, which is
based on user-supplied data for pressure drop, shaft angular velocity, and fluid
volumetric displacement.

The shaft friction torque is

τfr=τloss(Δp,ω)tanh(4ωωthreshold),

where *τloss* is interpolated from the
**Mechanical loss table, torque\_loss(dp,w)** parameter,
which is based on user-supplied data for pressure drop and shaft angular
velocity.

**Tabulated Data - Torque and Speed Parameterization**

The block calculates the volumetric loss table,
*qloss,TLU* and the mechanical
loss table, *τloss,TLU*, as

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

### Input Signal Parameterization

When **Leakage and friction parameterization** is
`Input signal - volumetric and mechanical
efficiencies`, ports **EV** and
**EM** are enabled. The internal leakage and shaft friction are
calculated in the same way as the `Tabulated data - volumetric and
mechanical efficiencies` parameterization, except that
*η*v and
*η*m are received directly at ports
**EV** and **EM**, respectively.

When **Leakage and friction parameterization** is
`Input signal - volumetric and mechanical losses`,
ports **LV** and **LM** are enabled. These ports
receive leakage flow and friction torque as positive physical signals. The leakage
flow rate is calculated as:

m˙leak=ρavgqLVtanh(4Δppthresh),

where:

- *q*LV is the leakage flow
  received at port **LV**.
- *p*thresh is the value of the
  **Pressure drop threshold for motor-pump
  transition** parameter.

The friction torque is calculated as:

τfr=τLMtanh(4ωωthresh),

where

- *τ*LM is the friction torque
  received at port **LM**.
- *ω*thresh is the value of the
  **Angular velocity threshold for motor-pump
  transition** parameter.

The volumetric and mechanical efficiencies range between the user-defined
specified minimum and maximum values. Any values lower or higher than this range
will take on the minimum and maximum specified values, respectively.

### Pump Operation

The motor flow rate is:

m˙=m˙ideal+m˙leak,

where m˙ideal=ρavgD⋅ω.

The motor torque is:

τ=τideal−τfr,

where τideal=D⋅Δp.

The mechanical power extracted by the motor shaft is:

φmech=τω,

and the motor hydraulic power is:

φhyd=Δpm˙ρavg.

If you would like to know if the block is operating beyond the
supplied tabulated data, you can set **Check if operating beyond the range
of supplied tabulated data** to `Warning` to
receive a warning if this occurs, or `Error` to stop the
simulation when this occurs. For parameterization by input signal for volumetric or
mechanical losses, you can be notified if the simulation surpasses operating modes
with the **Check if operating outside of motor mode**
parameter.

You can also monitor motor functionality. Set **Check if pressures are
less than motor minimum pressure** to
`Warning` to receive a warning if this occurs, or
`Error` to stop the simulation when this occurs.

### Predefined Parameterization

Pre-parameterized manufacturer data is available for this block. This data allows
you to model a specific supplier component.

To load a predefined parameterization,

1. Click the "Select a predefined parameterization" hyperlink in the
   block dialog box description.
2. Select a part from the drop-down menu and click **Update block
   with selected part**.
3. If you change any parameter settings after loading a parameterization,
   you can check your changes by clicking **Compare block settings
   with selected part**. Any difference in settings between
   the block and pre-defined parameterization will display in the
   MATLAB® command window.

**Note**

Predefined block parameterizations use available data sources to supply
parameter values. The block substitutes engineering judgment and simplifying
assumptions for missing data. As a result, expect some deviation between
simulated and actual physical behavior. To ensure accuracy, validate the
simulated behavior against experimental data and refine your component models as
necessary.

To learn more, see List of Pre-Parameterized Components.

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
