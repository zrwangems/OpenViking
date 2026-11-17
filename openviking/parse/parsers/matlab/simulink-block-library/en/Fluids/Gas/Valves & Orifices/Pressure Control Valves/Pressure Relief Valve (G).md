---
type: simulink-block
title: 'Pressure Relief Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereliefvalveg'
documentation_source_path: 'ref/pressurereliefvalveg.html'
language: en
---

# Pressure Relief Valve (G)

## Ports
```yaml
ports:
- name: A
  summary: Valve entrance gas
  direction: conserving
- name: B
  summary: Valve entrance gas
  direction: conserving
```

### Conserving

### **A** — Valve entrance gas

Gas conserving port associated with the opening through which the flow
must enter the valve.

### **B** — Valve entrance gas

Gas conserving port associated with the opening through which the flow
must exit the valve.
## Parameters
```yaml
parameters:
- name: Opening pressure specification
  summary: Choice of pressure measurement to use as valve control signal Pressure difference of port A relative to port B
    (default) | Gauge pressure at port A
  group: ''
- name: Valve parameterization
  summary: Parameterization used to specify flow characteristics of valve Cv flow coefficient (default) | Kv flow coefficient
    | Sonic conductance | Orifice area
  group: ''
- name: Opening characteristic
  summary: Method to calculate the opening characteristics of the valve Linear (default) | Tabulated
  group: ''
- name: Set pressure differential
  summary: Threshold differential for valve operation 0 MPa (default) | positive scalar
  group: ''
- name: Pressure regulation range
  summary: Width of the pressure range over which the opening area is variable 0.1 MPa (default) | positive scalar
  group: ''
- name: Set pressure (gauge)
  summary: Inlet gauge pressure required to open the valve 0.1 MPa (default) | positive scalar in units of pressure
  group: ''
- name: Opening pressure differential vector
  summary: 'Vector of control pressures at which to specify valve opening data 0.2 : 0.2 : 1.2 MPa (default) | vector'
  group: ''
- name: Opening pressure (gauge) vector
  summary: 'Vector of control pressures at which to specify valve opening data 0.2 : 0.2 : 1.2 MPa (default) | vector'
  group: ''
- name: Maximum Cv flow coefficient
  summary: Cv coefficient that corresponds to maximally open component 4 (default) | positive scalar
  group: ''
- name: xT pressure differential ratio factor at choked flow
  summary: Ratio of pressure differentials 0.7 (default) | positive scalar
  group: ''
- name: Leakage flow fraction
  summary: Ratio of flow rates 1e-6 (default) | positive scalar
  group: ''
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range [0,1]
  group: ''
- name: Cv flow coefficient vector
  summary: Cv coefficients corresponding to values in opening fraction vector [1e-06, .8, 1.6, 2.4, 3.2, 4] (default) | vector
    of positive numbers
  group: ''
- name: Maximum Kv flow coefficient
  summary: Kv coefficient that corresponds to maximally open component 3.6 (default) | positive scalar
  group: ''
- name: Kv flow coefficient vector
  summary: Kv coefficients corresponding to values in opening fraction vector [1e-06, .72, 1.44, 2.16, 2.88, 3.6] (default)
    | vector of positive numbers
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
  summary: Sonic conductances corresponding to values in opening fraction vector [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)
    (default) | vector of positive values
  group: ''
- name: Critical pressure ratio vector
  summary: Critical pressure ratios corresponding to values in opening fraction vector 0.3 * ones(1,6) (default) | vector
    of positive numbers
  group: ''
- name: Maximum orifice area
  summary: Flow area corresponding to maximally open component 1e-4 m^2 (default) | positive scalar
  group: ''
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar in the range of [0,1]
  group: ''
- name: Orifice area vector
  summary: Vector of orifice opening area values [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2 (default) | vector
  group: ''
- name: Laminar flow pressure ratio
  summary: Pressure ratio at which flow transitions between laminar and turbulent regimes 0.999 (default) | positive scalar
  group: ''
- name: Cross-sectional area at ports A and B
  summary: Flow area at gas ports 0.01 m^2 (default) | positive scalar
  group: ''
```

### **Opening pressure specification** — Choice of pressure measurement to use as valve control signal `Pressure difference of port A relative to port B` (default) | `Gauge pressure at port A`

Choice of pressure measurement to use as valve control signal. The block
uses this setting to determine when the valve should begin to open. In the
default setting, `Pressure difference of port A relative to port
B`, the opening pressure of the valve is expressed as a
pressure drop from inlet to outlet. In the alternative setting,
`Gauge pressure at port A`, it is expressed as
a gauge inlet pressure.

### **Valve parameterization** — Parameterization used to specify flow characteristics of valve `Cv flow coefficient` (default) | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

Method to calculate the mass flow rate.

- `Cv flow coefficient` — The flow
  coefficient
  *C*v
  determines the block parameterization.
- `Kv flow coefficient` — The flow
  coefficient
  *K*v,
  where Kv=0.865Cv, determines the block parameterization.
- `Sonic conductance` — The sonic
  conductance of the resistive element at steady state determines the
  block parameterization.
- `Orifice area` — The size of the flow
  restriction determines the block parametrization.

### **Opening characteristic** — Method to calculate the opening characteristics of the valve `Linear` (default) | `Tabulated`

Method the block uses to calculate the opening area of the valve. The
linear setting treats the opening area as a linear function of the orifice
opening fraction. The tabulated setting allows for a general, nonlinear
relationship you can specify in tabulated form.

### **Set pressure differential** — Threshold differential for valve operation `0 MPa` (default) | positive scalar

Pressure drop, from inlet to outlet, required to open the valve. This
value marks the beginning of the pressure regulation range, over which the
valve progressively opens in an effort to contain a pressure rise. The
opening area of the valve depends on the difference between the actual
pressure drop to the value specified here.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Pressure difference at port
A relative to port B` and **Opening
characteristic** to
`Linear`.

### **Pressure regulation range** — Width of the pressure range over which the opening area is variable `0.1 MPa` (default) | positive scalar

Valve operational range. The valve begins to open at the set pressure
value, and is fully open at *pmax*,
the end of the pressure regulation range, where
*pmax = pset +
prange*.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to
`Linear`.

### **Set pressure (gauge)** — Inlet gauge pressure required to open the valve `0.1 MPa` (default) | positive scalar in units of pressure

Inlet gauge pressure required to open the valve. This parameter marks the
beginning of the pressure regulation range, over which the valve
progressively opens in an effort to contain a pressure rise The opening area
of the valve depends on the difference between the actual inlet pressure to
the value specified here.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Gauge pressure at port
A` and **Opening characteristic** to
`Linear`.

### **Opening pressure differential vector** — Vector of control pressures at which to specify valve opening data `0.2 : 0.2 : 1.2 MPa` (default) | vector

Vector of control pressures at which to specify the chosen measure of
valve opening—sonic conductance, flow coefficient, or opening area. This
vector must be equal in size to those containing the valve opening data. The
vector elements must be positive and increase monotonically from left to
right. These pressure values are the pressure drop from inlet to outlet.

The first element of this parameter is the pressure setting of the valve, at which the
valve begins to open. The last element is the maximum pressure, at which the
valve is fully open. The difference between the two is the pressure
regulation range of the valve.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Pressure difference at port
A relative to port B` and **Opening
characteristic** to
`Tabulated`.

### **Opening pressure (gauge) vector** — Vector of control pressures at which to specify valve opening data `0.2 : 0.2 : 1.2 MPa` (default) | vector

Vector of control pressures at which to specify the chosen measure of
valve opening—sonic conductance, flow coefficient, or opening area. This
vector must be equal in size to those containing the valve opening data. The
vector elements must be positive and increase monotonically in value from
left to right. These pressures are the gauge pressure at the inlet.

The first element of this parameter is the pressure setting of the valve,
at which the valve begins to open. The last element is the maximum pressure,
at which the valve is fully open. The difference between the two is the
pressure regulation range of the valve.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Gauge pressure at port
A` and **Opening characteristic** to
`Tabulated`.

### **Maximum Cv flow coefficient** — Cv coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow coefficient
when the restriction area available for flow is at a maximum. This parameter
measures the ease with which the gas traverses the resistive element when
driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Cv flow coefficient`, and
**Opening characteristic** to
`Linear`.

### **xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure, *pin*, and the
outlet pressure, *pout*, defined as (pin−pout)/pin where choking first occurs. If you do not have this value,
look it up in table 2 in ISA-75.01.01 [3]. Otherwise, the default value of 0.7 is reasonable for
many valves.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient` or `Kv flow
coefficient`.

### **Leakage flow fraction** — Ratio of flow rates `1e-6` (default) | positive scalar

Ratio of the flow rate of the orifice when it is closed to when it is
open.

#### Dependencies

To enable this parameter, set **Opening characteristic** to
`Linear`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the orifice is in near-open or near-closed positions.
Set this parameter to a nonzero value less than one to increase the
stability of your simulation in these regimes.

#### Dependencies

To enable this parameter, set **Opening characteristic** to
`Linear`.

### **Cv flow coefficient vector** — Cv coefficients corresponding to values in opening fraction vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | vector of positive numbers

Vector of *Cv* flow coefficients.
Each coefficient corresponds to a value in the **Opening fraction
vector** parameter. This parameter measures the ease with which
the gas traverses the resistive element when driven by a pressure
differential. The flow coefficients must increase monotonically from left to
right, with greater opening fractions representing greater flow
coefficients. The size of the vector must be the same as the
**Opening fraction vector**.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Cv flow coefficient`, and
**Opening characteristic** to
`Tabulated`.

### **Maximum Kv flow coefficient** — Kv coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow coefficient
when the restriction area available for flow is at a maximum. This parameter
measures the ease with which the gas traverses the resistive element when
driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Kv flow coefficient`, and
**Opening characteristic** to
`Linear`.

### **Kv flow coefficient vector** — Kv coefficients corresponding to values in opening fraction vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | vector of positive numbers

Vector of *Kv* flow coefficients.
Each coefficient corresponds to a value in the **Opening fraction
vector** parameter. This parameter measures the ease with which
the gas traverses the resistive element when driven by a pressure
differential. The flow coefficients must increase monotonically from left to
right, with greater opening fractions representing greater flow
coefficients. The size of the vector must be the same as the
**Opening fraction vector** parameter.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Kv flow coefficient`, and
**Opening characteristic** to
`Tabulated`.

### **Maximum sonic conductance** — Sonic conductance corresponding to maximally open component `12 l/(bar*s)` (default) | positive scalar

Value of the sonic conductance when the cross-sectional area available for
flow is at a maximum.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Sonic conductance`, and **Opening
characteristic** to
`Linear`.

### **Critical pressure ratio** — Ratio of downstream and upstream pressures at which the flow first chokes `0.3` (default) | positive scalar

Pressure ratio at which flow first begins to choke and the flow velocity reaches its
maximum, given by the local speed of sound. The pressure ratio is the outlet
pressure divided by inlet pressure.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance`, and **Opening
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

### **Sonic conductance vector** — Sonic conductances corresponding to values in opening fraction vector `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)` (default) | vector of positive values

Vector of sonic conductances inside the resistive element. Each
conductance corresponds to a value in the **Opening fraction
vector** parameter. The sonic conductances must increase
monotonically from left to right, with greater opening fractions
representing greater sonic conductances. The size of the vector must be the
same as the **Opening fraction vector** parameter.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Sonic conductance`, and **Opening
characteristic** to
`Tabulated`.

### **Critical pressure ratio vector** — Critical pressure ratios corresponding to values in opening fraction vector `0.3 * ones(1,6)` (default) | vector of positive numbers

Vector of critical pressure ratios at which the flow first chokes, with
each critical pressure ratio corresponding to a value in the
**Opening fraction vector** parameter. The critical
pressure ratio is the fraction of downstream-to-upstream pressures at which
the flow velocity reaches the local speed of sound. The size of the vector
must be the same as the **Opening fraction vector**
parameter.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Sonic conductance`, and **Opening
characteristic** to
`Tabulated`.

### **Maximum orifice area** — Flow area corresponding to maximally open component `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the orifice opening when the cross-sectional area
available for flow is at a maximum.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Orifice area`, and **Opening
characteristic** to
`Linear`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar in the range of [0,1]

Correction factor that accounts for discharge losses in theoretical
flows.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice
area`.

### **Orifice area vector** — Vector of orifice opening area values `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2` (default) | vector

Vector of cross-sectional areas of the orifice opening. The values in this
vector correspond one-to-one with the elements in the **Opening
fraction vector** parameter. The first element of this vector
is the orifice leakage area and the last element is the maximum orifice
area.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice
area`, and **Opening characteristic**
to `Tabulated`.

### **Laminar flow pressure ratio** — Pressure ratio at which flow transitions between laminar and turbulent regimes `0.999` (default) | positive scalar

Pressure ratio at which flow transitions between laminar and turbulent
flow regimes. The pressure ratio is the outlet pressure divided by inlet
pressure. Typical values range from `0.995` to
`0.999`.

### **Cross-sectional area at ports A and B** — Flow area at gas ports `0.01 m^2` (default) | positive scalar

Area normal to the flow path at each port. The ports are equal in size.
The value of this parameter should match the inlet area of the components to
which the resistive element connects.
## Libraries

Simscape / Fluids / Gas / Valves & Orifices / Pressure Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

### R2022b: Model gas systems using improved flow computations

In previous versions, the blocks in the gas library used a conversion factor to
implement different orifice parameterizations in terms of sonic conductance. You can
use the **Valve parameterization** parameter to specify the
parameterization.

The new parameterizations also include new parameters:

- **xT pressure differential ratio factor at choked
  flow**
- **Discharge coefficient**
- **Leakage flow fraction**. This parameter replaces
  the **Cv coefficient (USCS) at leakage flow**,
  **Kv coefficient (SI) at leakage flow**,
  **Sonic conductance at leakage flow**, and
  **Restriction area at leakage flow**
  parameters.

To improve clarity:

- The **Opening parameterization** parameter has been
  renamed to **Opening characteristic**.
- The **Reference temperature** and **Reference
  density** parameters have been renamed to **ISO
  reference temperature** and **ISO reference
  density**, respectively.
- The **Cv coefficient (USCS) at maximum flow** and
  **Kv coefficient (USCS) at maximum flow**
  parameters have been renamed to **Maximum Cv
  coefficient** and **Maximum Kv coefficient**, respectively.
- The **Sonic conductance at maximum flow** parameter
  has been renamed to **Maximum sonic
  conductance**.
- The **Pressure control specification** parameter has
  been renamed to **Opening pressure specification**. The
  options for this parameter have been renamed to `Pressure
  difference of port A relative to port B` and
  `Gauge pressure at port A`.
- The **Control pressure vector** parameter has been
  renamed to **Opening pressure differential vector** or
  **Opening pressure (gauge) vector**, depending on
  the choice for **Opening pressure
  specification**.

## Description

Pressure relief valve in a gas network

The Pressure Relief Valve (G) block represents an orifice
that opens with inlet pressure to keep the pressure from reaching extreme levels. At
normal pressures, the valve is closed and only releases leakage flow. Above a specified
pressure setting, the valve begins to open, which allows the gas to vent from the region
of high pressure. The opening area increases with inlet pressure up to a maximum value,
at which point the valve is fully open and pressure rises unabated.

The valve responds to inlet pressure relative to the outlet or inlet pressure relative to
the environment. The chosen pressure measurement is the *control
pressure* of the valve. The **Control pressure
specification** parameter determines which of the measurements the block
uses during simulation.

The relationship between the opening area and the pressure drop depends on the
parameterization of the valve. That relationship can take the form of a linear
analytical expression or a tabulated function.

The flow can be laminar or turbulent, and it can reach up to sonic speeds. The maximum
velocity happens at the throat of the valve where the flow is narrowest and fastest. The
flow chokes and the velocity saturates when a drop in downstream pressure can no longer
increase the velocity. Choking occurs when the back-pressure ratio reaches the critical
value characteristic of the valve. The block does not capture supersonic flow.

### Valve Opening Fraction

The inlet pressure is the valve control signal. The more the inlet pressure rises over the
pressure setting of the valve, the greater the opening area becomes. The amount that
the control pressure exceeds the pressure setting determines how much the valve
opens. When the **Opening characteristic** parameter is
`Linear`, the block calculates the valve opening
fraction to scale the flow characteristic parameters. The normalized control
pressure is

p^=PCtl-PSetΔP,

where:

- *PCtl* is the control
  pressure.

  When **Opening pressure specification** is
  `Pressure difference of port A relative to port
  B`,

  PCtl=PA−PB,

  where *PA* is
  the absolute pressure at port **A** and
  *PB* is the absolute
  pressure at port **B**.

  When **Opening pressure specification** is
  `Gauge pressure at port A`,

  PCtl=PA−PAtm,

  where *PAtm*
  is the atmospheric pressure specified in the Gas Properties
  (G) block of the model.
- *PSet* is the set pressure.

  When **Opening pressure specification** is
  `Pressure difference of port A relative to port
  B`, *PSet*, is
  the value of the **Set pressure differential**
  parameter

  When **Opening pressure specification** is
  `Gauge pressure at port A`,
  *PSet* is the value of
  the **Set pressure (gauge)** parameter
- *ΔP* is the value of the **Pressure
  regulation range** parameter.

The fraction of valve opening, *L*, is

L=(1-Lleak)P^+Lleak,

where *Lleak* is the
value of the **Leakage flow fraction** parameter.

**Numerical Smoothing**

When the **Opening characteristic** parameter is
`Linear` and the **Smoothing
factor** parameter is nonzero, the block applies numerical
smoothing to the normalized control pressure, p^. Enabling smoothing helps maintain numerical robustness in
your simulation.

For more information, see Numerical Smoothing.

### Valve Parameterizations

The block behavior depends on the **Valve parametrization**
parameter:

- `Cv flow coefficient` — The flow coefficient
  *C*v
  determines the block parameterization. The flow coefficient measures the
  ease with which a gas can flow when driven by a certain pressure
  differential.
- `Kv flow coefficient` — The flow coefficient
  *K*v, where Kv=0.865Cv, determines the block parameterization. The flow
  coefficient measures the ease with which a gas can flow when driven by a
  certain pressure differential.
- `Sonic conductance` — The sonic conductance of
  the resistive element at steady state determines the block parameterization.
  The sonic conductance measures the ease with which a gas can flow when
  *choked*, which is a condition in which the flow
  velocity is at the local speed of sound. Choking occurs when the ratio
  between downstream and upstream pressures reaches a critical value known as
  the *critical pressure ratio*.
- `Orifice area` — The size of the flow restriction
  determines the block parametrization.

### Opening Characteristics

The flow characteristic relates the opening of the valve to the input that
produces it. The opening is expressed as a sonic conductance, flow coefficient, or
restriction area, determined by the **Valve parameterization**
parameter.

The flow characteristic is normally given at steady state, with the inlet at a
constant, carefully controlled pressure. The flow characteristic depends only on the
valve and can be linear or nonlinear. To capture the flow characteristics, use the
**Opening characteristic** parameter:

- `Linear` — The measure of flow capacity is a
  linear function of the valve opening fraction. As the opening fraction
  rises from `0` to `1`, the measure of
  flow capacity scales from the specified minimum to the specified
  maximum.
- `Tabulated` — The measure of flow capacity is
  a general function, which can be linear or nonlinear, of the orifice
  opening fraction. The function is specified in tabulated form, with the
  independent variable specified by the **Opening pressure
  differential vector** or the **Opening pressure
  (gauge) vector**.

### Momentum Balance

The block equations depend on the **Orifice parametrization** parameter.
When you set **Orifice parametrization** to `Cv
flow coefficient parameterization`, the mass flow rate, m˙, is

m˙=CvN6Y(pin−pout)ρin,

where:

- *Cv* is the flow
  coefficient.
- *N6* is a constant equal
  to 27.3 for mass flow rate in kg/hr, pressure in bar, and density in
  kg/m3.
- *Y* is the expansion factor.
- *pin* is the inlet
  pressure.
- *pout* is the outlet
  pressure.
- *ρin* is the inlet
  density.

The expansion factor is

Y=1−pin−pout3pinFγxT,

where:

- *Fγ* is the ratio of the
  isentropic exponent to 1.4.
- *xT* is the value of the
   **xT pressure differential ratio factor at choked
  flow** parameter.

The block smoothly transitions to a linearized form of the equation when the
pressure ratio, pout/pin, rises above the value of the **Laminar flow pressure
ratio** parameter,
*Blam*,

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout),

where:

Ylam=1−1−Blam3FγxT.

When the pressure ratio, pout/pin, falls below 1−FγxT, the orifice becomes choked and the block switches to the
equation

m˙=23CvN6FγxTpinρin.

When you set **Orifice parametrization** to `Kv flow
coefficient parameterization`, the block uses these same
equations, but replaces *Cv* with
*Kv* by using the relation Kv=0.865Cv. For more information on the mass flow equations when the
**Orifice parametrization** parameter is `Kv
flow coefficient parameterization` or `Cv flow
coefficient parameterization`, see [2][3].

When you set **Orifice parametrization** to
`Sonic conductance parameterization`, the mass flow
rate, m˙, is

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

where:

- *C* is the sonic conductance.
- *Bcrit* is the critical
  pressure ratio.
- *m* is the value of the **Subsonic
  index** parameter.
- *Tref* is the value of the
  **ISO reference temperature** parameter.
- *ρref* is the value of the
  **ISO reference density** parameter.
- *Tin* is the inlet
  temperature.

The block smoothly transitions to a linearized form of the equation when the
pressure ratio, pout/pin, rises above the value of the **Laminar flow pressure
ratio** parameter
*Blam*,

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

When the pressure ratio, pout/pin, falls below the critical pressure ratio,
*Bcrit*, the orifice becomes
choked and the block switches to the equation

m˙=CρrefpinTrefTin.

The `Sonic conductance` setting of the
**Valve parameterization** parameter is for pneumatic
applications. If you use this setting for gases other than air, you may need to
scale the sonic conductance by the square root of the specific gravity.

For more information on the mass flow equations when the **Orifice
parametrization** parameter is `Sonic conductance
parameterization`, see [1].

When you set **Orifice parametrization** to
`Orifice area parameterization`, the mass flow
rate, m˙, is

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ],

where:

- *Sr* is the orifice or
  valve area.
- *S* is the value of the **Cross-sectional
  area at ports A and B** parameter.
- *Cd* is the value of the
  **Discharge coefficient** parameter.
- *γ* is the isentropic exponent.

The block smoothly transitions to a linearized form of the equation when the
pressure ratio, pout/pin, rises above the value of the **Laminar flow pressure
ratio** parameter,
*Blam*,

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

When the pressure ratio, pout/pin, falls below(2γ+1)γγ−1 , the orifice becomes choked and the block switches to the
equation

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2.

For more information on the mass flow equations when the **Orifice
parametrization** parameter is `Orifice area
parameterization`, see [4].

### Mass Balance

The block assumes the volume and mass of fluid inside the valve is very small and
ignores these values. As a result, no amount of fluid can accumulate in the valve.
By the principle of conservation of mass, the mass flow rate into the valve through
one port equals that out of the valve through the other port

m˙A+m˙B=0,

where m˙ is defined as the mass flow rate into the valve through the port
indicated by the **A** or **B** subscript.

### Energy Balance

The resistive element of the block is an adiabatic component. No heat exchange can
occur between the fluid and the wall that surrounds it. No work is done on or by the
fluid as it traverses from inlet to outlet. Energy can flow only by advection,
through ports **A** and **B**. By the principle of conservation of energy, the sum of the port
energy flows is always equal to zero

ϕA+ϕB=0,

where *ϕ* is the energy flow rate into the valve through ports
**A** or **B**.

### Assumptions and Limitations

- The equation for the `Orifice area` parameterization
  is less accurate for gases that are far from ideal.
- This block does not model supersonic flow.
