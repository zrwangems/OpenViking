---
type: simulink-block
title: 'Pressure Relief Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereliefvalvema'
documentation_source_path: 'ref/pressurereliefvalvema.html'
language: en
---

# Pressure Relief Valve (MA)

## Ports

### Conserving

### **A** — Fluid entry or exit moist air

Moist air conserving port associated with the fluid entry or exit
port.

### **B** — Fluid entry or exit moist air

Moist air conserving port associated with the fluid entry or exit
port.
### Input

### **Ps** — Set pressure, Pa physical signal

Input port for varying set pressure signal.

#### Dependencies

To enable this port, set **Set pressure control**
to `Controlled`.

## Parameters

### **Valve parameterization** — Model for valve parameterization `Cv flow coefficient` (default) | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

Method the block uses to calculate the mass flow rate from the pressure
difference across the valve or the pressure difference from the mass flow
rate.

### **Opening characteristic** — Method to convert from control signal to measure of flow capacity `Linear` (default) | `Tabulated`

Method by which to parameterize the chosen measure of flow capacity.

### **Opening pressure specification** — Control pressure `Pressure differential` (default) | `Gauge pressure at port A`

Control pressure specification:

- When this parameter is `Pressure
  differential`, the valve opens when
  *pA ̶
  pB* exceeds the
  **Set pressure differential**.
- When this parameter is `Gauge pressure at port
  A`, the valve opens when
  *pA ̶
  patm* exceeds the
  **Set pressure (gauge)**.

### **Set pressure control** — Variable or constant set pressure `Constant` (default) | `Controlled`

Whether the pressure threshold is constant or variable. Setting this
parameter to `Controlled` exposes the physical
signal port **Ps**.

### **Set pressure differential** — Set pressure `0.01` MPa (default) | positive scalar

Valve pressure threshold. When the control pressure,
*pA ̶
pB*, exceeds the set pressure, the valve
begins to open.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Pressure
differential` and **Set pressure
control** to `Constant`.

### **Set pressure (gauge)** — Set pressure `0.1` MPa (default) | positive scalar

Valve pressure threshold. When the control pressure,
*pA ̶
patm*, exceeds the set pressure, the
valve begins to open.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Gauge pressure at port
A` and **Set pressure control** to
`Constant`.

### **Pressure regulation range** — Valve operational range `0.1` MPa (default) | positive scalar

Valve operational range. The valve begins to open at the set pressure
value, and is fully open at *pmax*,
the end of the pressure regulation range, where
*pmax = pset +
prange*.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to
`Linear`.

### **Opening pressure differential vector** — Vector of pressure differentials `[0.2 : 0.2 : 1.2] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the tabulated parameterization
of valve area.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Pressure
differential` and **Opening
characteristic** to
`Tabulated`.

### **Opening pressure (gauge) vector** — Vector of gauge pressures `[0.2 : 0.2 : 1.2] MPa` (default) | 1-by-*n* vector

Vector of gauge pressure values for the tabulated parameterization of
valve area.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Gauge pressure at port
A` and **Opening characteristic** to
`Tabulated`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Ratio of actual flow rate to ideal flow rate. This parameter accounts for
real-world losses that are not captured in the orifice equation.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice
area`.

### **Maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow coefficient
when the restriction area available for flow is at a maximum. This parameter
measures the ease with which the vapor traverses the resistive element when
driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient` and **Opening
characteristic** to
`Linear`.

### **Cv flow coefficient vector** — *Cv* coefficients that correspond to values in member position vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | 1-by-*n* vector

Vector of *Cv* flow coefficients.
Each coefficient corresponds to a value in the **Opening pressure
differential vector** or the **Opening pressure (gauge)
vector** parameters. This parameter measures the ease with
which the vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient` and **Opening
characteristic** to
`Tabulated`.

### **Maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow coefficient
when the restriction area available for flow is at a maximum. This parameter
measures the ease with which the vapor traverses the resistive element when
driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Kv flow
coefficient` and **Opening
characteristic** to
`Linear`.

### **Kv flow coefficient vector** — *Kv* coefficients that correspond to values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | 1-by-*n* vector

Vector of *Kv* flow coefficients.
Each coefficient corresponds to a value in the **Opening pressure
differential vector** or the **Opening pressure (gauge)
vector** parameters. This parameter measures the ease with
which the vapor traverses the resistive element when driven by a pressure
differential.

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

Vector of sonic conductances inside the resistive element. The values in
this vector correspond one-to-one with the elements in the **Opening
pressure differential vector** or the **Opening
pressure (gauge) vector** parameters.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance` and **Opening
characteristic** to
`Tabulated`.

### **Critical pressure ratio vector** — Critical pressure ratios corresponding to values in control member position vector `0.3 * ones(1,6)` (default) | vector of positive numbers

Vector of critical pressure ratios at which the flow first chokes. The
critical pressure ratio is the fraction of downstream-to-upstream pressures
at which the flow velocity reaches the local speed of sound. The values in
this vector correspond one-to-one with the elements in the **Opening
pressure differential vector** or the **Opening
pressure (gauge) vector** parameters.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance` and **Opening
characteristic** to
`Tabulated`.

### **xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure,
*pin*, and the outlet pressure,
*pout*, defined as (pin−pout)/pin where choking first occurs.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient` or `Kv flow
coefficient`.

### **Maximum orifice area** — Maximum valve opening area `1e-4 m^2` (default) | positive scalar

Maximum valve area when the valve is fully open.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice
area` and **Opening characteristic**
to `Linear`.

### **Orifice area vector** — Vector of valve opening area values `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of orifice area values for the tabulated parameterization of the
vapor valve area. The values in this vector correspond one-to-one with the
elements in the **Opening pressure differential vector** or
the **Opening pressure (gauge) vector** parameters.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice
area` and **Opening characteristic**
to `Tabulated`.

### **Leakage flow fraction** — Ratio of flow rates `1e-6` (default) | positive scalar

Ratio of the flow rate of the valve when it is closed to when it is
open.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to `Linear`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the valve is in near-open or near-closed positions.
Set this parameter to a nonzero value less than one to increase the
stability of your simulation in these regions.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to `Linear`.

### **Laminar flow pressure ratio** — Laminar-turbulent transition pressure ratio `0.999` (default) | positive scalar

Ratio of the valve outlet pressure to valve inlet pressure at which the
fluid transitions between the laminar and turbulent regimes. The pressure
loss corresponds to the mass flow rate linearly in laminar flows and
quadratically in turbulent flows.

### **Cross-sectional area at ports A and B** — Valve port areas `0.01` m^2 (default) | positive scalar

Area of the ports **A** and
**B**.

### **Opening dynamics** — Whether to account for flow response to valve opening `off` (default) | `on`

Whether to account for transient effects to the fluid system due to the
valve opening. Selecting this parameter approximates the opening conditions
by introducing a first-order lag in the flow response.

### **Opening time constant** — Valve opening time constant `0.1` s (default) | positive scalar

Time constant by which to compute the lag in the opening dynamics.

#### Dependencies

To enable this parameter, select **Opening
dynamics**.

## Libraries

Simscape / Fluids / Moist Air / Valves & Orifices / Pressure Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Pressure relief valve in a moist air network

The Pressure Relief Valve (MA) block models a pressure-controlling relief valve in a moist
air network. The valve opens when the pressure exceeds the set pressure. Specify the
pressure differential that opens the valve in the **Set pressure
specification** parameter, which can be the pressure difference between
ports **A** and **B** or the gauge pressure at port
**A**. When you set **Set pressure control** to
`Controlled`, the set pressure varies according to the
input signal at port **Ps**. For pressure control based on another
location in the fluid network, see the Pressure Compensator
Valve (MA) block.

### Pressure Control

The valve opens when the pressure in the valve,
*pcontrol*, exceeds the set
pressure, *pset*. The valve is fully open
when the control pressure reaches *pset* +
*prange*, where
*prange* is the value of the
**Pressure regulation range** parameter.

For the linear parametrizations, the block calculates the opening fraction of the
valve, *λ*. When you set **Set pressure control**
to `Constant`, *λ* is

λ=(1−fleak)(pcontrol−pset)prange+fleak,

where:

- *fleak* is the value of the
  **Leakage flow fraction** parameter.
- *pcontrol* is the control
  pressure, which depends on the value of the **Set pressure
  specification** parameter.

  When you set **Set pressure specification** to
  `Pressure differential`, the control
  pressure is *pA ̶
  pB*.

  When you set **Set pressure specification** to
  `Gauge pressure at port A`, the control
  pressure is the difference between the pressure at port
  **A** and atmospheric pressure.
- *pset* is the set pressure,
  which depends on the value of the **Set pressure
  specification** parameter.

  When you set **Set pressure specification** to
  `Pressure differential`,
  *pset* is the value of
  the **Set pressure differential** parameter.

  When you set **Set pressure specification** to
  `Gauge pressure at port A`,
  *pset* is the value of
  the **Set pressure (gauge)** parameter.

When you set **Set pressure control** to
`Controlled`, the valve opening fraction is

λ=(1−fleak)(pcontrol−ps)prange+fleak,

where *ps* is the value
of the signal at port **Ps**. If the control pressure exceeds the
valve pressure regulation range, the valve opening fraction is 1.

### Momentum Balance

The flow rate in the valve depends on the **Opening
characteristic** parameter:

- `Linear` — The block scales the measure of flow
  capacity by *λ* to account for the valve opening
  area.
- `Tabulated` — The block interpolates the measure
  of flow capacity from either the **Cv flow coefficient
  vector**, **Kv flow coefficient vector**,
  **Orifice area vector**, or **Sonic conductance
  vector** parameters. This function uses a one-dimensional
  lookup table.

**Cv Flow Coefficient Parameterization**

When you set **Valve parametrization** to `Cv
flow coefficient`, the mass flow rate is

m˙=CvN6Y(pin−pout)vin,

where:

- *Cv* is the flow
  coefficient.
- *N6* is a constant equal
  to 27.3 when mass flow rate is in kg/hr, pressure is in bar, and
  density is in kg/m3.
- *Y* is the expansion factor.
- *pin* is the inlet
  pressure.
- *pout* is the outlet
  pressure.
- *vin* is the inlet
  specific volume.

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

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout),

where:

Ylam=1−1−Blam3FγxT.

When the pressure ratio, pout/pin, falls below 1−FγxT, the valve becomes choked and the block uses the equation

m˙=23CvN6FγxTpinvin.

**Kv Flow Coefficient Parameterization**

When you set **Valve parametrization** to `Kv
flow coefficient`, the block uses the same equations as the
`Cv flow coefficient` parametrization, but replaces
*Cv* with
*Kv* using the relation Kv=0.865Cv.

**Valve Area Parameterization**

When you set **Valve parametrization** to
`Orifice area`, the mass flow rate is

m˙=CdAvalve2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AvalveAport)2(poutpin)2γ],

where:

- *Cd* is the value of
  the **Discharge coefficient** parameter.
- *γ* is the isentropic exponent.

The block smoothly transitions to a linearized form of the equation when
the pressure ratio, pout/pin, rises above the value of the **Laminar flow
pressure ratio** parameter,
*Blam*,

m˙=CdAvalve2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AvalveAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

When the pressure ratio, pout/pin, falls below(2γ+1)γγ−1 , the valve becomes choked and the block uses the
equation

m˙=CdAvalve2γγ+1pin1vin1(γ+12)2γ−1−(AvalveAport)2.

**Sonic Conductance Parameterization**

When you set **Valve parameterization** to `Sonic
conductance`, the mass flow rate is

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
applications. If you use this setting for moist air with high levels of trace
gasses or are modeling a fluid other than air, you may need to scale the sonic
conductance by the square root of the mixture specific gravity.

### Opening Dynamics

When you select **Opening dynamics**, the block introduces a
control pressure lag and replaces *pcontrol*
with the dynamic control pressure, *pdyn*.
The block calculates the dynamic control pressure based on the **Opening
time constant** parameter, *τ*

p˙dyn=pcontrol−pdynτ.

By default, the block clears the **Opening
dynamics** check box.

### Mass Balance

The block conserves mass through the valve

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

where *ṁ* is the mass flow rate and the
subscript *w* denotes water vapor, the subscript
*g* denotes trace gas, and the subscript *d*
denotes water droplets.

### Energy Balance

Energy is conserved in the valve,

ΦA+ΦB=0,

where:

- *ΦA* is the energy flow at
  port **A**.
- *ΦB* is the energy flow at
  port **B**.

### Assumptions and Limitations

- There is no heat exchange between the valve and the
  environment.
