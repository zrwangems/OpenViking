---
type: simulink-block
title: '2-Way Directional Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Directional Control Valves'
documentation_page: '2waydirectionalvalvema'
documentation_source_path: 'ref/2waydirectionalvalvema.html'
language: en
---

# 2-Way Directional Valve (MA)

## Ports
```yaml
ports:
- name: A
  summary: Moist air inlet or outlet moist air
  direction: conserving
- name: B
  summary: Moist air inlet or outlet moist air
  direction: conserving
- name: S
  summary: Spool displacement, m physical signal
  direction: input
```

### Conserving

### **A** — Moist air inlet or outlet moist air

Moist air conserving port associated with the valve inlet or
outlet.

### **B** — Moist air inlet or outlet moist air

Moist air conserving port associated with the valve inlet or
outlet.
### Input

### **S** — Spool displacement, m physical signal

Physical signal associated with the spool displacement, in m. A
positive value causes the valve to open.
## Parameters
```yaml
parameters:
- name: Valve parameterization
  summary: Variable or constant orifice parameterization Cv flow coefficient (default) | Kv flow coefficient | Sonic conductance
    | Orifice area
  group: ''
- name: Opening characteristic
  summary: Method to convert from control signal to measure of flow capacity Linear (default) | Tabulated
  group: ''
- name: Spool position at maximum orifice area
  summary: Spool offset at maximum area 5e-3 m (default) | positive scalar
  group: ''
- name: Spool travel between closed and open orifice
  summary: Maximum spool stroke 5e-3 m (default) | positive scalar
  group: ''
- name: Spool travel vector
  summary: Vector of spool positions [0, .003, .006, .009, .012, .015] m (default) | 1-by-*n* vector
  group: ''
- name: Maximum Cv flow coefficient
  summary: '*Cv* coefficient that corresponds to maximally open component 4 (default) | positive scalar'
  group: ''
- name: Cv flow coefficient vector
  summary: '*Cv* coefficients that correspond to values in member position vector [1e-06, .8, 1.6, 2.4, 3.2, 4] (default)
    | 1-by-*n* vector'
  group: ''
- name: xT pressure differential ratio factor at choked flow
  summary: Ratio of pressure differentials 0.7 (default) | positive scalar
  group: ''
- name: Maximum Kv flow coefficient
  summary: '*Kv* coefficient that corresponds to maximally open component 3.6 (default) | positive scalar'
  group: ''
- name: Kv flow coefficient vector
  summary: '*Kv* coefficients that correspond to values in member position vector [1e-06, .72, 1.44, 2.16, 2.88, 3.6] (default)
    | 1-by-*n* vector'
  group: ''
- name: Maximum sonic conductance
  summary: Sonic conductance corresponding to maximally open component 12 l/(bar*s) (default) | positive scalar
  group: ''
- name: Critical pressure ratio
  summary: Ratio of downstream and upstream pressures at which the flow first chokes 0.3 (default) | positive scalar
  group: ''
- name: Subsonic index
  summary: Exponent used to characterize mass flow in subsonic flow regime 0.5 (default) | positive scalar
  group: ''
- name: ISO reference temperature
  summary: ISO 8778 reference temperature 293.15 K (default) | scalar
  group: ''
- name: ISO reference density
  summary: ISO 8778 reference density 1.185 kg/m^3 (default) | positive scalar
  group: ''
- name: Sonic conductance vector
  summary: Sonic conductances corresponding to values in control member position vector [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)
    (default) | vector of positive values
  group: ''
- name: Critical pressure ratio vector
  summary: Critical pressure ratios corresponding to values in control member position vector 0.3 * ones(1,6) (default) |
    vector of positive numbers
  group: ''
- name: Maximum orifice area
  summary: Maximum orifice opening area 1e-4 m^2 (default) | positive scalar
  group: ''
- name: Orifice area vector
  summary: Vector of orifice opening area values [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: ''
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: ''
- name: Leakage flow fraction
  summary: Ratio of flow rates 1e-6 (default) | positive scalar
  group: ''
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range [0,1]
  group: ''
- name: Laminar flow pressure ratio
  summary: Laminar-turbulent transition pressure ratio 0.999 (default) | positive scalar
  group: ''
- name: Cross-sectional area at ports A and B
  summary: Valve port areas 0.01 m^2 (default) | positive scalar
  group: ''
```

### **Valve parameterization** — Variable or constant orifice parameterization `Cv flow coefficient` (default) | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

Method the block uses to calculate the mass flow rate from the pressure
difference across the orifice or the pressure difference from the mass flow
rate.

### **Opening characteristic** — Method to convert from control signal to measure of flow capacity `Linear` (default) | `Tabulated`

Method by which to convert the control signal specified at port **S** to the chosen measure of flow capacity.

### **Spool position at maximum orifice area** — Spool offset at maximum area `5e-3` `m` (default) | positive scalar

Position of the spool travel member when the valve is fully open. The
default value represents a zero-lapped system. A positive, nonzero value
represents an underlapped, or partially closed, system. A negative, nonzero
value represents an overlapped system where the valve remains open over a
range of displacements.

### **Spool travel between closed and open orifice** — Maximum spool stroke `5e-3` `m` (default) | positive scalar

Spool offset at the maximum valve opened area.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to
`Linear`.

### **Spool travel vector** — Vector of spool positions `[0, .003, .006, .009, .012, .015] m` (default) | 1-by-*n* vector

Vector of spool positions for the tabulated orifice parameterizations. The
vector elements correspond one-to-one to the values in the **Orifice
area vector**, **Cv flow coefficient vector**,
or **Kv flow coefficient vector** parameters.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to
`Tabulated`.

### **Maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow coefficient
when the orifice is fully open and the area available for flow is at a
maximum. This parameter measures the ease with which the vapor traverses the
resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient` and **Opening
characteristic** to
`Linear`.

### **Cv flow coefficient vector** — *Cv* coefficients that correspond to values in member position vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | 1-by-*n* vector

Vector of *Cv* flow coefficients.
Each coefficient corresponds to a value in the **Spool travel
vector** parameter. This parameter measures the ease with which
the vapor traverses the resistive element when driven by a pressure
differential. The size of the vector must be the same as the **Spool
travel vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient` and **Opening
characteristic** to
`Tabulated`.

### **xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure,
*pin*, and the outlet pressure,
*pout*, defined as (pin−pout)/pin where choking first occurs.

#### Dependencies

To enable this parameter, **Valve parameterization**
to `Cv flow coefficient` or `Kv
flow coefficient`.

### **Maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow coefficient
when the orifice is fully open and the area available for flow is at a
maximum. This parameter measures the ease with which the vapor traverses the
resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Kv flow
coefficient` and **Opening
characteristic** to
`Linear`.

### **Kv flow coefficient vector** — *Kv* coefficients that correspond to values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | 1-by-*n* vector

Vector of *Kv* flow coefficients.
Each coefficient corresponds to a value in the **Spool travel
vector** parameter. This parameter measures the ease with which
the vapor traverses the resistive element when driven by a pressure
differential. The size of the vector must be the same as the **Spool
travel vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Kv flow
coefficient` and **Opening
characteristic** to
`Tabulated`.

### **Maximum sonic conductance** — Sonic conductance corresponding to maximally open component `12 l/(bar*s)` (default) | positive scalar

Value of the sonic conductance when the control signal specified at port
**S** is `1` and
cross-sectional area available for flow is at a maximum.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance` and **Opening
characteristic** to
`Linear`.

### **Critical pressure ratio** — Ratio of downstream and upstream pressures at which the flow first chokes `0.3` (default) | positive scalar

Pressure ratio at which flow first begins to choke and the flow velocity
reaches its maximum, given by the local speed of sound. The pressure ratio
is the outlet pressure divided by inlet pressure.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance` and **Opening
characteristic** to `Linear`.

### **Subsonic index** — Exponent used to characterize mass flow in subsonic flow regime `0.5` (default) | positive scalar

Empirical value used to more accurately calculate the mass flow rate in
the subsonic flow regime.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance`.

### **ISO reference temperature** — ISO 8778 reference temperature `293.15 K` (default) | scalar

Temperature at standard reference atmosphere, defined as 293.15 K in ISO
8778.

You only need to adjust the ISO reference parameter values if you are
using sonic conductance values that are obtained at difference reference
values.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance`.

### **ISO reference density** — ISO 8778 reference density `1.185 kg/m^3` (default) | positive scalar

Density at standard reference atmosphere, defined as 1.185 kg/m3 in ISO
8778.

You only need to adjust the ISO reference parameter values if you are
using sonic conductance values that are obtained at difference reference
values.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance`.

### **Sonic conductance vector** — Sonic conductances corresponding to values in control member position vector `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)` (default) | vector of positive values

Vector of sonic conductances inside the resistive element. Each
conductance corresponds to a value in the **Spool travel
vector** parameter. The size of the vector must be the same as
the **Spool travel vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance` and **Opening
characteristic** to
`Tabulated`.

### **Critical pressure ratio vector** — Critical pressure ratios corresponding to values in control member position vector `0.3 * ones(1,6)` (default) | vector of positive numbers

Vector of critical pressure ratios at which the flow first chokes, with
each critical pressure ratio corresponding to a value in the **Spool
travel vector** parameter. The critical pressure ratio is the
fraction of downstream-to-upstream pressures at which the flow velocity
reaches the local speed of sound. The size of the vector must be the same as
the **Spool travel vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance` and **Opening
characteristic** to
`Tabulated`.

### **Maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Orifice area when it is fully open.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice
area` and **Opening characteristic**
to `Linear`.

### **Orifice area vector** — Vector of orifice opening area values `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of orifice area values for the tabulated parameterization of the
orifice area. The values in this vector correspond one-to-one with the
elements in the **Spool travel vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice
area` and **Opening characteristic**
to `Tabulated`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Ratio of actual flow rate to ideal flow rate. This parameter accounts for
real-world losses that are not captured in the orifice equation.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice
area`.

### **Leakage flow fraction** — Ratio of flow rates `1e-6` (default) | positive scalar

Ratio of the flow rate of the orifice when it is closed to when it is
open.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to `Linear`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the orifice is in near-open or near-closed positions.
Set this parameter to a nonzero value less than one to increase the
stability of your simulation in these regions.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to `Linear`.

### **Laminar flow pressure ratio** — Laminar-turbulent transition pressure ratio `0.999` (default) | positive scalar

Ratio of the orifice outlet pressure to orifice inlet pressure at which
the fluid transitions between the laminar and turbulent regimes. The
pressure loss corresponds to the mass flow rate linearly in laminar flows
and quadratically in turbulent flows.

### **Cross-sectional area at ports A and B** — Valve port areas `0.01` m^2 (default) | positive scalar

Area of the orifice ports **A** and
**B**.
## Libraries

Simscape / Fluids / Moist Air / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

2-way directional valve in a moist air network

The 2-Way Directional Valve (MA) block represents a
valve with two ports, **A** and **B**, and one flow
path, **A**–**B**. The path runs through an orifice of
variable width. The input signal specified at port **S** controls the
position of the spool. The valve closes when the spool covers the orifice opening. For
more details about how the block calculates flow rate through a variable orifice, see
Orifice
(MA).

### Valve Parameterizations

The block behavior depends on the **Valve parametrization**
parameter:

- `Cv flow coefficient` — The flow coefficient
  *C*v
  determines the block parameterization. The flow coefficient measures the
  ease with which the moist air can flow when driven by a certain pressure
  differential.
- `Kv flow coefficient` — The flow coefficient
  *Kv*,
  where Kv=0.865Cv, determines the block parameterization. The flow
  coefficient measures the ease with which the moist air can flow when driven
  by a certain pressure differential.
- `Sonic conductance` — The sonic conductance of
  the resistive element at steady state determines the block parameterization.
  The sonic conductance measures the ease with which the moist air can flow
  when *choked*, which is a condition in which the flow
  velocity is at the local speed of sound. Choking occurs when the ratio
  between downstream and upstream pressures reaches a critical value known as
  the *critical pressure ratio*.
- `Orifice area` — The size of the flow restriction
  determines the block parametrization.

### Opening Characteristics

The flow characteristic relates the opening of the valve to the input that
produces it, which is often the spool travel. The block expresses the opening as a
sonic conductance, flow coefficient, or restriction area, depending on the setting
of the **Valve parameterization** parameter. The control input is
the orifice opening fraction, a function of the spool displacement specified at port
**S**.

The flow characteristic is normally given at steady state, with the inlet at a
constant, carefully controlled pressure. The flow characteristic depends only on the
valve and can be linear or nonlinear. To capture the flow characteristics, use the
**Opening characteristic** parameter:

- `Linear` — The measure of flow capacity is a
  linear function of the orifice opening fraction. As the opening fraction
  rises, the measure of flow capacity scales from the specified minimum to
  the specified maximum.
- `Tabulated` — The measure of flow capacity is
  a general function, which can be linear or nonlinear, of the orifice
  opening fraction. The function is specified in tabulated form, with the
  independent variable specified by the **Opening fraction
  vector**.

### Visualize Orifice Openings

To visualize the spool offsets and displacement, right-click the block and select **Fluids** > **Plot Valve Characteristics**. The plot shows the sonic conductance,
*Kv* flow
coefficient, *Cv* flow
coefficient, or orifice area as a function of spool position.

To update the data after changing the block parameters, click **Reload
Data** in the figure window.

This figure shows the valve configuration with default values.

Plot of area versus spool position for each orifice.

### Assumptions and Limitations

- The `Sonic conductance` setting of the
  **Valve parameterization** parameter is for
  pneumatic applications. If you use this setting for moist air with high
  levels of trace gasses or are modeling a fluid other than air, you may
  need to scale the sonic conductance by the square root of the mixture
  specific gravity.
- This block does not model supersonic flow.
- There is no heat exchange between the valve and the
  environment.
