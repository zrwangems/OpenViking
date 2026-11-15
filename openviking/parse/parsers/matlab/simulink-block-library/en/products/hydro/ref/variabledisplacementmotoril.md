---
type: simulink-block
title: 'Variable-Displacement Motor (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Pumps and Motors'
documentation_page: 'variabledisplacementmotoril'
documentation_source_path: 'ref/variabledisplacementmotoril.html'
language: en
---

# Variable-Displacement Motor (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port to the motor.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port to the motor.

### **R** — Mechanical port mechanical rotational

Rotating shaft angular velocity and torque.

### **C** — Mechanical port mechanical rotational

Motor casing reference angular velocity and torque.
### Input

### **D** — Volumetric displacement, cm^3/rad physical signal

Volumetric displacement of the motor, in m^3/rad, specified as a
physical signal.

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

### **LV** — Leakage flow rate, m^3/s physical signal

Motor volumetric losses, in m^3/s, specified as a physical
signal.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.

### **LM** — Friction torque, N\*m physical signal

Motor mechanical losses in N\*m, specified as a physical signal.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.

## Parameters

### **Leakage and friction parameterization** — Method of calculating leakage flow rate and friction torque `Analytical` (default) | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

Parameterization of the leakage and friction characteristics of the motor.

- In the `Analytical` parameterization,
  the leakage flow rate and the friction torque are calculated by
  analytical equations.
- In the `Tabulated data - volumetric and
  mechanical efficiencies` parameterization, the
  leakage flow rate and torque friction are calculated from the
  user-supplied **Pressure drop vector, dp**,
  **Shaft angular velocity vector, w**, and
  **Displacement vector, D** parameters and
  interpolated from the 3-D dependent **Volumetric
  efficiency table, e\_v(dp,w,D)** and
  **Mechanical efficiency table,
  e\_m(dp,w,D)** tables.
- In the `Tabulated data - volumetric and mechanical
  loss` parameterization, the leakage flow rate
  and torque friction are calculated from the user-supplied
  **Pressure drop vector, dp**;
  **Shaft angular velocity vector, w**; and
  **Displacement vector, D** parameters and
  interpolated from the 3-D dependent **Volumetric loss
  table, q\_loss(dp,w,D)** and **Mechanical
  loss table, torque\_loss(dp,w,D)** tables.
- In the `Input signal - volumetric and mechanical
  efficiencies` parameterization, the volumetric
  and mechanical efficiencies are received as physical signals at
  ports **EV** and **EM**,
  respectively.
- In the `Input signal - volumetric and mechanical
  loss` parameterization, the leakage flow rate
  and friction torque are received as physical signals at ports
  **LV** and **LM**,
  respectively.

### **Nominal displacement** — Fixed-volume fluid displacement `30 cm^3/rev` (default) | scalar

Amount of fluid displaced by shaft rotating under nominal operating
conditions.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Nominal shaft angular velocity** — Shaft angular velocity `1800 rpm` (default) | scalar

Angular velocity of the shaft under nominal operating conditions.

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

### **Volumetric efficiency at nominal conditions** — Ratio of actual flow rate to ideal flow rate at nominal conditions `0.92` (default) | positive scalar in the range of (0,1]

Ratio of actual flow rate to ideal flow rate at nominal conditions.

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

### **Mechanical efficiency at nominal conditions** — Ratio of actual to ideal mechanical power `0.88` (default) | positive scalar

Ratio of actual mechanical power to ideal mechanical power at nominal
conditions.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Pressure drop vector, dp** — Vector of pressure data for tabulated data parameterization `[.1, 1, 2] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular parameterization of
leakage and torque friction. This vector forms an independent axis with the
**Shaft angular velocity vector, w** and the
**Displacement vector, D** parameters for the 3-D
dependent **Volumetric efficiency table, e\_v(dp,w,D)** and
**Mechanical efficiency table, e\_m(dp,w,D)**
parameters. The vector elements must be listed in ascending order.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to either:

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Tabulated data - volumetric and mechanical
  losses`

### **Shaft angular velocity vector, w** — Vector of angular velocity data for tabulated data parameterization `[250, 500, 1000, 2000, 3000, 4000] rpm` (default) | 1-by-*n* vector

Vector of angular velocity data for the tabular parameterization of
leakage and torque friction. This vector forms an independent axis with the
**Shaft angular velocity vector, w** and the
**Displacement vector, D** parameters for the 3-D
dependent **Volumetric efficiency table, e\_v(dp,w,D)** and
**Mechanical efficiency table, e\_m(dp,w,D)**
parameters. The vector elements must be listed in ascending order.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to either:

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Tabulated data - volumetric and mechanical
  losses`

### **Displacement vector, D** — Vector of displacement volumes for tabulated data parameterization `[-30, -19, 19, 30] cm^3/s` (default) | 1-by-*n* vector

Vector of volumetric displacement data for the tabular parameterization of
leakage and torque friction. This vector forms an independent axis with the
**Shaft angular velocity vector, w** and the
**Pressure drop vector, dp** parameters for the 3-D
dependent **Volumetric efficiency table, e\_v(dp,w,D)** and
**Mechanical efficiency table, e\_m(dp,w,D)**
parameters. The vector elements must be listed in ascending order.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to either:

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Tabulated data - volumetric and mechanical
  losses`

### **Volumetric efficiency table, e\_v(dp,w,D)** — Volumetric efficiency for tabulated data parameterization `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)` (default) | *M*-by-*N*-by-*P* matrix

*M*-by-*N*-by-*P*
matrix of volumetric efficiencies at the specified fluid pressure drop,
shaft angular velocity, and volumetric displacement. Linear interpolation is
employed between table elements. *M*, *N*,
and *P* are the sizes of the corresponding vectors:

- *M* is the number of vector elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in the
  **Shaft angular velocity vector, w**
  parameter.
- *P* is the number of vector elements in the
  **Displacement vector, D**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Mechanical efficiency table, e\_m(dp,w,D)** — Mechanical efficiency for tabulated data parameterization `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)` (default) | *M*-by-*N*-by-*P* matrix

*M*-by-*N*-by-*P*
matrix of mechanical efficiencies at the specified fluid pressure drop,
shaft angular velocity, and displacement. Linear interpolation is employed
between table elements. *M*, *N*, and
*P* are the sizes of the corresponding vectors:

- *M* is the number of vector elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in the
  **Shaft angular velocity vector, w**
  parameter.
- *P* is the number of vector elements in the
  **Displacement vector, D**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Volumetric loss table, q\_loss(dp,w,D)** — Volumetric losses for tabulated data parameterization `repmat([.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3, 1, 1, 4)` (default) | *M*-by-*N*-by-*P* matrix

*M*-by-*N*-by-*P*
matrix of volumetric leakage at the specified fluid pressure drop, shaft
angular velocity, and displacement. Linear interpolation is employed between
table elements. *M*, *N*, and
*P* are the sizes of the corresponding vectors:

- *M* is the number of vector elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in the
  **Shaft angular velocity vector, w**
  parameter.
- *P* is the number of vector elements in the
  **Displacement vector, D**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical losses`.

### **Mechanical loss table, torque\_loss(dp,w,D)** — Mechanical losses for tabulated data parameterization `repmat([.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626], 1, 1, 4) N*m` (default) | *M*-by-*N*-by-*P* matrix

*M*-by-*N*-by-*P*
matrix of mechanical losses at the specified fluid pressure drop and shaft
angular velocity. Linear interpolation is employed between table elements.
*M*, *N*, and *P* are
the sizes of the correlated vectors:

- *M* is the number of vector elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of vector elements in the
  **Shaft angular velocity vector, w**
  parameter.
- *P* is the number of vector elements in the
  **Displacement vector, D**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical losses`.

### **Minimum volumetric efficiency** — Minimum value of volumetric efficiency `1e-3` (default) | positive scalar in the range of (0,1]

Minimum value of volumetric efficiency. If the input signal is below this
value, the volumetric efficiency is set to the minimum volumetric
efficiency.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Maximum volumetric efficiency** — Maximum value of volumetric efficiency `1` (default) | positive scalar in the range of (0,1]

Maximum value of volumetric efficiency. If the input signal is above this
value, the volumetric efficiency is set to the maximum volumetric
efficiency.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Minimum mechanical efficiency** — Minimum value of mechanical efficiency `1e-3` (default) | positive scalar in the range of (0,1]

Minimum value of mechanical efficiency. If the input signal is below this
value, the mechanical efficiency is set to the minimum mechanical
efficiency.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Maximum mechanical efficiency** — Maximum value of mechanical efficiency `1` (default) | positive scalar in the range of (0,1]

Maximum value of mechanical efficiency. If the input signal is above this
value, the mechanical efficiency is set to the maximum mechanical
efficiency.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **Pressure drop threshold for motor-pump transition** — Pressure threshold for mode transition `1e-3 MPa` (default) | positive scalar

Motor pressure drop that indicates the transition threshold between motor
and pump functionality. A transition region is defined around 0 MPa between
the positive and negative values of the pressure drop threshold. Within this
transition region, the computed leakage flow rate and friction torque are
adjusted according to the transition term *α* to ensure
smooth transition from one mode to the other.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to either:

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Input signal - volumetric and mechanical
  efficiencies`
- `Input signal - volumetric and mechanical
  losses`

### **Angular velocity threshold for motor-pump transition** — Angular velocity threshold for mode transition `100 rpm` (default) | positive scalar

Shaft angular velocity that indicates the transition threshold between motor and pump
functionality. A transition region is defined around 0 rpm between the
positive and negative values of the angular velocity threshold. Within this
transition region, the computed leakage flow rate and friction torque are
adjusted according to the transition term *α* to ensure
smooth transition from one mode to the other.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to:

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Input signal - volumetric and mechanical
  efficiencies`
- `Input signal - volumetric and mechanical
  losses`

### **Displacement threshold for motor-pump transition** — Displacement threshold for mode transition `0.1 cm^3/s` (default) | positive scalar

Volumetric displacement that indicates the transition threshold between
motor and pump functionality. A transition region is defined around 0 cm^3/s
between the positive and negative values of the displacement threshold.
Within this transition region, the computed leakage flow rate and friction
torque are adjusted according to the transition term *α* to
ensure smooth transition from one mode to the other. It is also used to
transition the ideal mass flow rate when the sign of **D**
changes.

### **Check if operating beyond the range of supplied tabulated data** — Whether to notify if extents of supplied data are surpassed `None` (default) | `Warning` | `Error`

Whether to notify if the extents of the supplied data are surpassed.
Select `Warning` to be notified when the block uses
values beyond the supplied data range. Select
`Error` to stop the simulation when the block
uses values beyond the supplied data range.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to:

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Tabulated data - volumetric and mechanical
  losses`

### **Check if operating beyond motor mode** — Whether to notify if block operates outside of the motor mode functionality `None` (default) | `Warning` | `Error`

Whether to notify if the block operates outside of the motor mode
functionality. Select `Warning` to be notified when
the block operates in the forward or reverse pump modes. Select
`Error` to stop the simulation when the block
operates in the forward or reverse pump modes.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.

### **Check if pressures are less than motor minimum pressure** — Whether to notify if fluid exit pressure is low `None` (default) | `Warning` | `Error`

Whether to notify if the fluid at port **A** or
**B** experiences low pressure. Select
`Warning` to be notified when the pressure
falls below a minimum specified value. Select
`Error` to stop the simulation when the
pressure falls below a minimum specified value.

The parameter helps identify potential conditions for cavitation, when the
fluid pressure falls below the fluid vapor pressure.

### **Motor minimum pressure** — Lower threshold of acceptable pressure at the motor outlet `0.101325 MPa` (default) | positive scalar

Lower threshold of acceptable pressure at the motor inlet or
outlet.

#### Dependencies

To enable this parameter, set **Check if pressures are less
than motor minimum pressure** to either:

- `Warning`
- `Error`

## Libraries

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2024a: Check if block operates outside range of calculated data

The **Check if operating beyond the octants of supplied tabulated
data** parameter has been renamed to **Check if operating
beyond the range of supplied tabulated data**. You can enable the
**Check if operating beyond the range of supplied tabulated
data** parameter to check if the block is operating beyond the data
specified in the block parameters, that is, operating in a region where the block
has extended the data.

## Description

Variable-displacement motor in an isothermal liquid system

The Variable-Displacement Motor (IL) block models a motor with variable-volume
displacement. The fluid may move from port **A** to port
**B**, called *forward mode*, or from port
**B** to port **A**, called *reverse
mode*. Motor mode operation occurs when there is a pressure drop in the
direction of the flow. Pump mode operation occurs when there is a pressure gain in the
direction of the flow.

The shaft rotation corresponds to the sign of the fluid volume moving through the
motor, which is received as a physical signal at port **D**. Positive
fluid displacement at **D** corresponds to positive shaft rotation in
forward mode. Negative fluid displacement at **D** corresponds to
negative shaft angular velocity in forward mode.

**Operation Modes**

The block has eight modes of operation. The working mode depends on the pressure drop
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

The motor block has analytical, lookup table, and physical signal parameterizations.
When using tabulated data or an input signal for parameterization, you can choose to
characterize the motor operation based on efficiency or losses.

The threshold parameters **Pressure drop threshold for motor-pump
transition**, **Angular velocity threshold for motor-pump
transition**, and **Displacement threshold for motor-pump
transition** identify regions where numerically smoothed flow transition
between the motor operational modes can occur. For the pressure and angular velocity
thresholds, choose a transition region that provides some margin for the transition
term, but which is small enough relative to the typical motor pressure drop and angular
velocity so that it will not impact calculation results. For the displacement threshold,
choose a threshold value that is smaller than the typical displacement volume during
normal operation.

### Analytical Leakage and Friction Parameterization

If you set **Leakage and friction parameterization** to
`Analytical`, the block calculates internal leakage and
shaft friction from constant nominal values of shaft velocity, pressure drop,
volumetric displacement, and torque. The leakage flow rate, which is correlated with
the pressure differential over the motor, is calculated as:

m˙leak=KρavgΔp,

where:

- *Δp* is *p*A
  – *p*B.
- *ρ*avg is the average fluid
  density.
- *K* is the Hagen-Poiseuille coefficient for
  analytical loss,

  K=Dnomωnom(1ηv,nom−1)Δpnom,

  where:

  - *D*nom is the
    **Nominal displacement**.
  - *ω*nom is the
    **Nominal shaft angular
    velocity**.
  - *η*nom is the
    **Volumetric efficiency at nominal
    conditions**.
  - *Δp*nom is the
    **Nominal pressure drop**.

The torque, which is related to the motor pressure differential, is calculated as:

τfr=(τ0+k|ΔpDDnom|)tanh(4ω5×10−5ωnom),

where:

- *τ*0 is the **No-load
  torque**.
- *k* is the friction torque vs. pressure gain coefficient at nominal
  displacement, which is determined from the **Mechanical
  efficiency at nominal conditions**,
  *ηm,nom*:

  k=τfr,nom−τ0Δpnom.

  *τfr,nom* is
  the friction torque at nominal conditions:

  τfr,nom=(1−ηm,nom)DnomΔpnom.
- *Δp* is the pressure drop between ports
  **A** and **B**.
- *ω* is the relative shaft angular velocity, or ωR−ωC.

### Tabulated Data Parameterizations

When using tabulated data for motor efficiencies or losses, you can provide data
for one or more of the motor operational modes. The signs of the tabulated data
determine the operational regime of the block. When data is provided for less than
eight operational modes, the block calculates the complementing data for the other
mode(s) by extending the given data into the remaining octants.

**The `Tabulated data - volumetric and mechanical
efficiencies` parameterization**

The leakage flow rate is calculated as:

m˙leak=m˙leak,motor(1+α2)+m˙leak,pump(1−α2),

where:

- m˙leak,pump=(ηυ−1)m˙ideal
- m˙leak,motor=(1−ηv)m˙

and *η*v is the volumetric efficiency,
which is interpolated from the user-provided tabulated data. The transition
term, *α*, is

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold)tanh(4DDthreshold),

where:

- *Δp* is
  *p*A –
  *p*B.
- *Δp*threshold is the
  **Pressure drop threshold for motor-pump
  transition**.
- *ω* is
  *ω*R –
  *ω*C.
- *ω*threshold is the
  **Angular velocity threshold for motor-pump
  transition**.

The torque is calculated as:

τfr=τfr,pump(1+α2)+τfr,motor(1−α2),

where:

- τfr,pump=(ηm−1)τ
- τfr,motor=(1−ηm)τideal

and *η*m is the
mechanical efficiency, which is interpolated from the user-provided tabulated
data.

**The `Tabulated data - volumetric and mechanical
losses` parameterization**

The leakage flow rate is calculated as:

m˙leak=ρavgqloss(Δp,ω,D),

where *q*loss is interpolated from the
**Volumetric loss table, q\_loss(dp,w,D)** parameter, which
is based on user-supplied data for pressure drop, shaft angular velocity, and
fluid volumetric displacement.

The shaft friction torque is calculated as:

τfr=τloss(Δp,ω,D),

where *τ*loss is interpolated from the
**Mechanical loss table, torque\_loss(dp,w,D)** parameter,
which is based on user-supplied data for pressure drop, shaft angular velocity,
and fluid volumetric displacement.

### Input Signal Parameterization

When **Leakage and friction parameterization** is set
to`Input signal - volumetric and mechanical
efficiencies`, ports **EV** and
**EM** are enabled. The internal leakage and shaft friction are
calculated in the same way as the `Tabulated data - volumetric and
mechanical efficiencies` parameterization, except that
*η*v and
*η*m are received directly at ports
**EV** and **EM**, respectively.

When **Leakage and friction parameterization** is set
to`Input signal - volumetric and mechanical losses`,
ports **LV** and **LM** are enabled. These ports
receive leakage flow and friction torque as positive physical signals. The leakage
flow rate is calculated as:

m˙leak=ρavgqLVtanh(4Δppthresh),

where:

- *q*LV is the leakage flow
  received at port **LV**.
- *p*thresh is the
  **Pressure drop threshold for motor-pump
  transition** parameter.

The friction torque is calculated as:

τfr=τLMtanh(4ωωthresh),

where

- *τ*LM is the friction torque
  received at port **LM**.
- *ω*thresh is the
  **Angular velocity threshold for motor-pump
  transition** parameter.

The volumetric and mechanical efficiencies range between the user-defined
specified minimum and maximum values. Any values lower or higher than this range
will take on the minimum and maximum specified values, respectively.

### Motor Operation

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

To be notified if the block is operating beyond the supplied
tabulated data, you can set **Check if operating beyond the range of
supplied tabulated data** to `Warning` to
receive a warning if this occurs, or `Error` to stop the
simulation when this occurs. When using input signal for volumetric or mechanical
losses, you can be notified if the simulation surpasses operating modes with the
**Check if operating beyond motor mode** parameter.

You can also monitor motor functionality. Set **Check if pressures are
less than motor minimum pressure** to
`Warning` to receive a warning if this occurs, or
`Error` to stop the simulation when this occurs.
