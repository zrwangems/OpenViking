---
type: simulink-block
title: 'Fixed-Displacement Pump (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors'
documentation_page: 'fixeddisplacementpumpil'
documentation_source_path: 'ref/fixeddisplacementpumpil.html'
language: en
---

# Fixed-Displacement Pump (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
- name: B
  summary: Liquid port isothermal liquid
  direction: conserving
- name: R
  summary: Mechanical port mechanical rotational
  direction: conserving
- name: C
  summary: Mechanical port mechanical rotational
  direction: conserving
- name: EV
  summary: Volumetric efficiency physical signal
  direction: input
- name: EM
  summary: Mechanical efficiency physical signal
  direction: input
- name: LV
  summary: Leakage flow rate, m^3/s physical signal
  direction: input
- name: LM
  summary: Friction torque, N*m physical signal
  direction: input
```

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port to the pump.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port to the pump.

### **R** — Mechanical port mechanical rotational

Rotating shaft angular velocity and torque.

### **C** — Mechanical port mechanical rotational

Pump casing angular velocity and torque.
### Input

### **EV** — Volumetric efficiency physical signal

Pump efficiency for fluid displacement, specified as a physical
signal. The value must be between 0 and 1.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **EM** — Mechanical efficiency physical signal

Pump efficiency for the mechanical supply of energy, specified as a
physical signal. The value must be between 0 and 1.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical efficiencies`.

### **LV** — Leakage flow rate, `m^3/s` physical signal

Pump volumetric losses in m^3/s, specified as a physical
signal.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.

### **LM** — Friction torque, `N*m` physical signal

Pump mechanical losses in N\*m, specified as a physical signal.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.
## Parameters
```yaml
parameters:
- name: Leakage and friction parameterization
  summary: Method of calculating leakage flow rate and friction torque Analytical (default) | Tabulated data - volumetric
    and mechanical efficiencies | Tabulated data - volumetric and mechanical losses | Input signal - volumetric and mechanical
    efficiencies | Input signal - volumetric and mechanical losses
  group: Parameters
- name: Displacement
  summary: Fixed-volume fluid displacement 30 cm^3/rev (default) | scalar
  group: Parameters
- name: Nominal shaft angular velocity
  summary: Shaft angular velocity 1800 rpm (default) | scalar
  group: Parameters
- name: Nominal pressure gain
  summary: Pressure gain between fluid entry and exit 10 MPa (default) | scalar
  group: Parameters
- name: Volumetric efficiency at nominal conditions
  summary: Ratio of actual flow rate to ideal flow rate 0.92 (default) | positive scalar
  group: Parameters
- name: No-load torque
  summary: Baseline torque 0 N*m (default) | scalar
  group: Parameters
- name: Mechanical efficiency at nominal conditions
  summary: Ratio of actual torque to ideal torque generated 0.88 (default) | positive scalar
  group: Parameters
- name: Pressure gain vector, dp
  summary: Vector of pressure data for tabulated data parameterization [.1, 1, 2] MPa (default) | 1-by-*n* vector
  group: Parameters
- name: Shaft angular velocity vector, w
  summary: Vector of angular velocity data for tabulated data parameterization [250, 500, 1000, 2000, 3000, 4000] rpm (default)
    | 1-by-*n* vector
  group: Parameters
- name: Volumetric efficiency table, e_v(dp,w)
  summary: Volumetric efficiency for tabulated data parameterization [.816, .908, .954, .977, .981, .984; .325, .663, .831,
    .916, .925, .946; .137, .568, .78, .892, .893, .91] (default) | *M*-by-*N*-by-*P* matrix
  group: Parameters
- name: Mechanical efficiency table, e_m(dp,w)
  summary: Mechanical efficiency for tabulated data parameterization [.996, .996, .996, .996, .996, .996; .988, .989, .989,
    .989, .989, .99; .981, .981, .982, .982, .983, .984] (default) | *M*-by-*N*-by-*P* matrix
  group: Parameters
- name: Volumetric loss table, q_loss(dp,w)
  summary: Volumetric losses for tabulated data parameterization [.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845,
    .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3 m^3/s (default) | *M*-by-*N*-by-*P* matrix
  group: Parameters
- name: Mechanical loss table, torque_loss(dp,w)
  summary: Mechanical losses for tabulated data parameterization [.002, .002, .002, .002, .002, .002; .0607, .0556, .0556,
    .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626] N*m (default) | *M*-by-*N*-by-*P* matrix
  group: Parameters
- name: Minimum volumetric efficiency
  summary: Minimum value of volumetric efficiency 1e-3 (default) | positive scalar in the range of (0,1]
  group: Parameters
- name: Maximum volumetric efficiency
  summary: Maximum value of volumetric efficiency 1 (default) | positive scalar
  group: Parameters
- name: Minimum mechanical efficiency
  summary: Minimum value of mechanical efficiency 1e-3 (default) | positive scalar in the range of (0,1]
  group: Parameters
- name: Maximum mechanical efficiency
  summary: Maximum value of mechanical efficiency 1 (default) | positive scalar in the range of (0,1]
  group: Parameters
- name: Pressure gain threshold for pump-motor transition
  summary: Pressure threshold for mode transition 1e-3 MPa (default) | positive scalar
  group: Parameters
- name: Angular velocity threshold for pump-motor transition
  summary: Angular velocity threshold for mode transition 100 rpm (default) | positive scalar
  group: Parameters
- name: Check if operating beyond the range of supplied tabulated data
  summary: Whether to notify if extents of supplied data are surpassed None (default) | Warning | Error
  group: Parameters
- name: Check if operating outside of pump mode
  summary: Whether to notify if block operates outside of the pump mode functionality None (default) | Warning | Error
  group: Parameters
- name: Check if pressures are less than pump minimum pressure
  summary: Whether to notify if fluid exit pressure is low None (default) | Warning | Error
  group: Parameters
- name: Pump minimum pressure
  summary: Lower threshold to acceptable pressure at the pump outlet 0.101325 MPa (default) | positive scalar
  group: Parameters
- name: Displacement fault
  summary: Option to model displacement fault Add fault
  group: Faults
- name: Faulted displacement factor
  summary: Factor by which to scale faulted displacement 0.5 (default) | positive scalar
  group: Faults
- name: Leakage fault
  summary: Option to model leakage fault Add fault
  group: Faults
- name: Faulted leakage factor
  summary: Factor by which to scale leakage fault 2.0 (default) | positive scalar
  group: Faults
- name: Shaft friction torque fault
  summary: Option to model shaft friction torque fault Add fault
  group: Faults
- name: Faulted shaft friction torque factor
  summary: Factor by which to scale shaft friction torque fault 2.0 (default) | positive scalar
  group: Faults
```

### Parameters

### **Leakage and friction parameterization** — Method of calculating leakage flow rate and friction torque `Analytical` (default) | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

Parameterization of the leakage and friction characteristics of the
pump.

- In the `Analytical`
  parameterization, the leakage flow rate and the friction
  torque are calculated by analytical equations.
- In the `Tabulated data - volumetric and
  mechanical efficiencies` parameterization,
  the volumetric and mechanical efficiencies are calculated
  from the user-supplied **Pressure gain vector,
  dp** and **Shaft angular velocity
  vector, w** parameters and interpolated from
  the 2-D dependent **Volumetric efficiency table,
  e\_v(dp,w)** and **Mechanical efficiency
  table, e\_m(dp,w)** tables.
- In the `Tabulated data - volumetric and
  mechanical loss` parameterization, the
  leakage flow rate and friction torque are calculated from
  the user-supplied **Pressure gain vector,
  dp** and **Shaft angular velocity
  vector, w** parameters and interpolated from
  the 2-D dependent **Volumetric loss table,
  q\_loss(dp,w)** and **Mechanical loss
  table, torque\_loss(dp,w)** tables.
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

Amount of fluid displaced by shaft rotating under nominal or typical
operating conditions.

### **Nominal shaft angular velocity** — Shaft angular velocity `1800 rpm` (default) | scalar

Angular velocity of the shaft under nominal operating
conditions.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Nominal pressure gain** — Pressure gain between fluid entry and exit `10 MPa` (default) | scalar

Pump pressure gain between the fluid entry and exit under nominal or
typical operating conditions.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to
`Analytical`.

### **Volumetric efficiency at nominal conditions** — Ratio of actual flow rate to ideal flow rate `0.92` (default) | positive scalar

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

### **Pressure gain vector, dp** — Vector of pressure data for tabulated data parameterization `[.1, 1, 2] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular
parameterization of leakage and torque friction. This vector forms an
independent axis with the **Shaft angular velocity vector,
w** parameter for the 2-D dependent **Volumetric
efficiency table, e\_v(dp,w)** and **Mechanical
efficiency table, e\_m(dp,w,D)** parameters. The vector
elements must be listed in ascending order.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to either:

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Tabulated data - volumetric and
  mechanical losses`

### **Shaft angular velocity vector, w** — Vector of angular velocity data for tabulated data parameterization `[250, 500, 1000, 2000, 3000, 4000] rpm` (default) | 1-by-*n* vector

Vector of angular velocity data for the tabular parameterization of
leakage and torque friction. This vector forms an independent axis with
the **Shaft angular velocity vector, w** parameter for
the 2-D dependent **Volumetric efficiency table,
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

### **Volumetric efficiency table, e\_v(dp,w)** — Volumetric efficiency for tabulated data parameterization `[.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91]` (default) | *M*-by-*N*-by-*P* matrix

*M*-by-*N* matrix of volumetric
efficiencies at the specified fluid pressure gain and shaft angular
velocity. Linear interpolation is employed between table elements.
*M* and *N* are the sizes of the
correlated vectors:

- *M* is the number of vector elements in
  the **Pressure gain vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Mechanical efficiency table, e\_m(dp,w)** — Mechanical efficiency for tabulated data parameterization `[.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984]` (default) | *M*-by-*N*-by-*P* matrix

*M*-by-*N* matrix of mechanical
efficiencies at the specified fluid pressure gain and shaft angular
velocity. Linear interpolation is employed between table elements.
*M* and *N* are the sizes of the
correlated vectors:

- *M* is the number of vector elements in
  the **Pressure gain vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical efficiencies`.

### **Volumetric loss table, q\_loss(dp,w)** — Volumetric losses for tabulated data parameterization `[.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3 m^3/s` (default) | *M*-by-*N*-by-*P* matrix

*M*-by-*N* matrix of volumetric
efficiencies at the specified fluid pressure gain and shaft angular
velocity. Linear interpolation is employed between table elements.
*M* and *N* are the sizes of the
correlated vectors:

- *M* is the number of vector elements in
  the **Pressure gain vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical loss`.

### **Mechanical loss table, torque\_loss(dp,w)** — Mechanical losses for tabulated data parameterization `[.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626] N*m` (default) | *M*-by-*N*-by-*P* matrix

*M*-by-*N* matrix of mechanical
losses at the specified fluid pressure gain and shaft angular velocity.
Linear interpolation is employed between table elements.
*M* and *N* are the sizes of the
correlated vectors:

- *M* is the number of vector elements in
  the **Pressure gain vector, dp**
  parameter.
- *N* is the number of vector elements in
  the **Shaft angular velocity vector, w**
  parameter.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data -
volumetric and mechanical loss`.

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

### **Pressure gain threshold for pump-motor transition** — Pressure threshold for mode transition `1e-3 MPa` (default) | positive scalar

Threshold pressure gain value for the transition between pump and
motor functionality. A transition region is defined around 0 MPa between
the positive and negative values of the pressure gain threshold. Within
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

### **Angular velocity threshold for pump-motor transition** — Angular velocity threshold for mode transition `100 rpm` (default) | positive scalar

Threshold angular velocity value for the transition between pump and
motor functionality. A transition region is defined around 0 rpm between
the positive and negative values of the angular velocity threshold.
Within this transition region, the computed leakage flow rate and
friction torque are adjusted according to the transition term
*α* to ensure smooth transition from one mode to
the other.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to:

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

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to:

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Tabulated data - volumetric and
  mechanical losses`

### **Check if operating outside of pump mode** — Whether to notify if block operates outside of the pump mode functionality `None` (default) | `Warning` | `Error`

Whether to notify if block operates outside of the pump mode
functionality. This block has four operation modes: forward pump,
reverse pump, reverse motor, and forward motor. Select
`Warning` to be notified when the block
operates in the forward or reverse motor modes. Select
`Error` to stop the simulation when the
block operates in the forward or reverse motor modes.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal -
volumetric and mechanical losses`.

### **Check if pressures are less than pump minimum pressure** — Whether to notify if fluid exit pressure is low `None` (default) | `Warning` | `Error`

Whether to notify if the fluid at port **A** or
**B** experiences low pressure. Select
`Warning` to be notified when the outlet
pressure falls below a minimum specified value. Select
`Error` to stop the simulation when the
outlet pressure falls below a minimum specified value.

The parameter helps to identify potential conditions for cavitation,
when the fluid pressure falls below the fluid vapor pressure.

### **Pump minimum pressure** — Lower threshold to acceptable pressure at the pump outlet `0.101325 MPa` (default) | positive scalar

Lower threshold of acceptable pressure at the pump inlet and
outlet.

#### Dependencies

To enable this parameter, set **Check if pressures are
less than pump minimum pressure** to:

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

The Fixed-Displacement Pump (IL) block now supports the Simscape™ faults interface. To learn more, see Introduction to Simscape Faults.

### R2024a: Check if block operates outside range of calculated data

The **Check if operating beyond the quadrants of supplied tabulated
data** parameter has been renamed to **Check if operating
beyond the range of supplied tabulated data**. You can enable the
**Check if operating beyond the range of supplied tabulated
data** parameter to check if the block is operating beyond the data
specified in the block parameters, that is, operating in a region where the block
has extended the data.

## Description

Fixed-displacement pump in isothermal liquid system

The Fixed-Displacement Pump (IL) block models a pump with constant-volume
displacement. The fluid may move from port **A** to port
**B**, called *forward mode*, or from port
**B** to port **A**, called *reverse
mode*. Pump mode operation occurs when there is a pressure gain in the
direction of the flow. Motor mode operation occurs when there is a pressure drop in the
direction of the flow.

Shaft rotation corresponds to the sign of the fluid volume. Positive fluid
displacement corresponds to positive shaft rotation in forward mode. Negative fluid
displacement corresponds to negative shaft angular velocity in forward mode.

**Operation Modes**

The block has four modes of operation. The working mode depends on the pressure gain
from port **A** to port **B**, *Δp =
p*B – *p*A
and the angular velocity, *ω = ω*R –
*ω*C:

- Mode 1, *Forward Pump*: Positive shaft angular velocity
  causes a pressure increase from port **A** to port
  **B** and flow from port **A** to port
  **B**.
- Mode 2, *Reverse Motor*: Flow from port
  **B** to port **A** causes a pressure
  decrease from **B** to **A** and negative
  shaft angular velocity.
- Mode 3, *Reverse Pump*: Negative shaft angular velocity
  causes a pressure increase from port **B** to port
  **A** and flow from **B** to
  **A**.
- Mode 4, *Forward Motor*: Flow from port
  **A** to **B** causes a pressure
  decrease from **A** to **B** and positive
  shaft angular velocity.

The pump block has analytical, lookup table, and physical signal parameterizations.
When using tabulated data or an input signal for parameterization, you can choose to
characterize pump operation based on efficiency or losses.

The threshold parameters **Pressure gain threshold for pump-motor
transition** and **Angular velocity threshold for pump-motor
transition** identify regions where numerically smoothed flow transition
between the pump operational modes can occur. For the pressure and angular velocity
thresholds, choose a transition region that provides some margin for the transition
term, but which is small enough relative to the typical pump pressure gain and angular
velocity so that it will not impact calculation results.

### Analytical Leakage and Friction Parameterization

If you set **Leakage and friction parameterization** to
`Analytical`, the block calculates leakage and friction
from constant values of shaft velocity, pressure gain, and friction torque. The
leakage flow rate, which is correlated with the pressure differential over the pump,
is calculated as:

m˙leak=KρavgΔp,

where:

- *Δp* is *p*B
  – *p*A.
- *ρavg* is the average fluid
  density.
- *K* is the Hagen-Poiseuille coefficient for
  analytical loss,

  K=Dωnom(1−ηv,nom)Δpnom,

  where:

  - *D* is the
    **Displacement**.
  - *ωnom* is the
    **Nominal shaft angular
    velocity**.
  - *ηv, nom* is the
    **Volumetric efficiency at nominal
    conditions**.
  - *Δpnom* is the
    **Nominal pressure gain**.

The friction torque, which is related to the pump pressure differential, is
calculated as:

τfr=(τ0+k|Δp|)tanh(4ω5×10−5ωnom),

where:

- *τ0* is the **No-load
  torque**.
- *k* is the friction torque vs. pressure gain coefficient at nominal
  displacement, which is determined from the **Mechanical
  efficiency at nominal conditions**,
  *ηm, nom*:

  k=τfr,nom−τ0Δpnom.

  *τfr,nom* is
  the friction torque at nominal conditions:

  τfr,nom=(1−ηm,nomηm,nom)DΔpnom.
- *ω* is the relative shaft angular velocity, or ωR−ωC.

### Tabulated Data Parameterizations

When using tabulated data for pump efficiencies or losses, you can provide data for one or
more of the pump operational modes. The signs of the tabulated data determine the
operational regime of the block. When data is provided for less than four
operational modes, the block calculates the complementing data for the other modes
by extending the given data into the remaining quadrants.

**The `Tabulated data - volumetric and mechanical
efficiencies` parameterization**

The leakage flow rate is

m˙leak=m˙leak,pump(1+α2)+m˙leak,motor(1−α2),

where:

- m˙leak,pump=(1−ηυ)m˙ideal
- m˙leak,motor=(ηv−1)m˙

and *η*v is the volumetric efficiency, which is
interpolated from the user-provided tabulated data. The transition term,
*α*, is

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold),

where:

- *Δp* is
  *p*B –
  *p*A.
- *p*threshold is the
  **Pressure gain threshold for pump-motor
  transition**.
- *ω* is
  *ω*R –
  *ω*C.
- *ω*threshold is the
  **Angular velocity threshold for pump-motor
  transition**.

The friction torque is calculated as:

τfr=τfr,pump(1+α2)+τfr,motor(1−α2),

where:

- τfr,pump=(1−ηm)τ
- τfr,motor=(ηm−1)τideal

and *η*m is the
mechanical efficiency, which is interpolated from the user-provided tabulated
data.

**The `Tabulated data - volumetric and mechanical
losses` parameterization**

The leakage flow rate is calculated as:

m˙leak=ρavgqloss(Δp,ω),

where *q*loss is interpolated from the
**Volumetric loss table, q\_loss(dp,w)** parameter, which is
based on user-supplied data for pressure drop, shaft angular velocity, and fluid
volumetric displacement.

The shaft friction torque is

τfr=τloss(Δp,ω)tanh(4ωωthreshold),

where *τ*loss is interpolated from the
**Mechanical loss table, torque\_loss(dp,w)** parameter,
which is based on user-supplied data for pressure drop and shaft angular
velocity.

### Input Signal Parameterization

When you select `Input signal - volumetric and mechanical
efficiencies`, ports **EV** and
**EM** are enabled. The internal leakage and shaft friction are
calculated in the same way as the `Tabulated data - volumetric and
mechanical efficiencies` parameterization, except that
*η*v and
*η*m are received directly at ports
**EV** and **EM**, respectively.

When you select `Input signal - volumetric and mechanical
losses`, ports **LV** and **LM**
are enabled. These ports receive leakage flow and friction torque as positive
physical signals. The leakage flow rate is calculated as:

m˙leak=ρavgqLVtanh(4Δppthresh),

where:

- *q*LV is the leakage flow
  received at port **LV**.
- *p*thresh is the
  **Pressure gain threshold for pump-motor
  transition** parameter.

The friction torque is calculated as:

τfr=τLMtanh(4ωωthresh),

where

- *τ*LM is the friction torque
  received at port **LM**.
- *ω*thresh is the
  **Angular velocity threshold for pump-motor
  transition** parameter.

The volumetric and mechanical efficiencies range between the user-defined
specified minimum and maximum values. Any values lower or higher than this range
will take on the minimum and maximum specified values, respectively.

### Pump Operation

The pump flow rate is:

m˙=m˙ideal−m˙leak,

where m˙ideal=ρavgD⋅ω.

The pump torque is:

τ=τideal+τfr,

where τideal=D⋅Δp.

The mechanical power delivered by the pump shaft is:

φmech=τω,

and the pump hydraulic power is:

φhyd=Δpm˙ρavg.

If you would like to know if the block is operating beyond the
supplied tabulated data, you can set **Check if operating beyond the range
of supplied tabulated data** to `Warning` to
receive a warning if this occurs, or `Error` to stop the
simulation when this occurs. For parameterization by input signal for volumetric or
mechanical losses, you can be notified if the simulation surpasses operating modes
with the **Check if operating beyond pump mode** parameter.

You can also monitor pump functionality. Set **Check if pressures are less
than pump minimum pressure** to `Warning` to
receive a warning if this occurs, or `Error` to stop the
simulation when this occurs.

### Predefined Parameterization

Pre-parameterization of the Fixed-Displacement Pump
(IL) block with manufacturer data is available. This data allows
you to model a specific supplier component.

To load a predefined parameterization,

1. Click the "Select a predefined parameterization" hyperlink in the
   Fixed-Displacement Pump (IL) block
   dialog description.
2. Select a part from the drop-down menu and click **Update block
   with selected part**.
3. If you change any parameter settings after loading a parameterization,
   you can check your changes by clicking **Compare block settings
   with selected part**. Any difference in settings between
   the block and pre-defined parameterization will display in the MATLAB
   command window.

**Note**

Predefined parameterizations of Simscape components use available data sources
for supplying parameter values. Engineering judgment and simplifying assumptions
are used to fill in for missing data. As a result, deviations between simulated
and actual physical behavior should be expected. To ensure requisite accuracy,
you should validate simulated behavior against experimental data and refine
component models as necessary.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

You can model a displacement fault, leakage, or a shaft friction torque fault.

When you enable the **Displacement fault** parameter, the block scales the
displacement by the value of the **Faulted displacement factor** parameter
when the fault triggers,

DFault=fDD,

where *fD* is the value of the **Faulted
displacement factor** parameter. When the **Leakage and friction
parameterization** parameter is `Analytical`, the
block does not use the faulted displacement value to calculate the Hagen-Poiseuille
coefficient or the friction torque at nominal conditions.

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

When **Leakage and friction parameterization** is `Tabulated data
- volumetric and mechanical losses` or `Input signal -
volumetric and mechanical losses`, the faulted leakage volumetric flow rate
is

qLeak,Fault=fLeakqLeak.

When you enable the **Shaft friction torque fault** parameter and
**Leakage and friction parameterization** is
`Analytical`, `Tabulated data - volumetric and
mechanical efficiencies`, or `Input signal - volumetric and
mechanical efficiencies`, the faulted mechanical efficiency is

ηm,Fault=ηmfFriction,

where *fFriction* is the value
of the **Faulted shaft friction torque factor** parameter and
*ηm* is the mechanical efficiency. When
**Leakage and friction parameterization** is
`Analytical`, the block uses the faulted mechanical efficiency
to calculate the friction torque at nominal conditions.

When **Leakage and friction parameterization** is `Tabulated data
- volumetric and mechanical losses` or `Input signal -
volumetric and mechanical losses`, the faulted friction torque is

τFriction,Fault=fFrictionτFriction.
