---
type: simulink-block
title: 'Ball Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Flow Control Valves'
documentation_page: 'ballvalvema'
documentation_source_path: 'ref/ballvalvema.html'
language: en
---

# Ball Valve (MA)

## Ports

### Input

### **S** — Valve position, rad physical signal

Physical signal port associated with the position of the valve, in
rad. A value of 0 represents a fully shut valve and a value of π/2
represents a fully open valve.
### Conserving

### **A** — Valve inlet or outlet moist air

Moist air conserving port associated with the valve inlet or
outlet.

### **B** — Valve inlet or outlet moist air

Moist air conserving port associated with the valve inlet or
outlet.

## Parameters

### **Valve parameterization** — Parameterization that specifies flow characteristics of valve `Orifice area based on geometry` (default) | `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

Method to calculate the mass flow rate:

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

### **Opening characteristic** — Ball valve parameterization `Area of overlapping circles` (default) | `Tabulated`

Option to parameterize the block by using the method of area of
overlapping circles or by using tabulated data.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar in the range of [0,1]

Correction factor that accounts for discharge losses in theoretical
flows.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice area based on
geometry`.

### **Area vector** — Flow area for tabulated parameterization `[1e-10, 45, 90, 135, 180, 225, 270, 315, 360, 405, 450]` `mm^2` (default) | vector of positive numbers

Flow area for a given ball rotation. Each element corresponds one-to-one
with the elements in the **Ball rotation vector**
parameter. The first element corresponds to the valve leakage and must be
nonzero.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice area based on
geometry` and **Opening
characteristic** to
`Tabulated`.

### **Maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow coefficient
when the restriction area available for flow is at a maximum. This parameter
measures the ease with which the moist air traverses the resistive element
when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient` and **Opening
characteristic** to `Area of overlapping
circles`.

### **Cv flow coefficient vector** — *Cv* coefficients that correspond to values in ball rotation vector `[1e-06, .0725, .1437, .2375, .35, .5375, .875, 1.3125, 2.125, 3.25, 4]` `1` (default) | vector of positive numbers

Vector of *Cv* flow coefficients.
Each coefficient corresponds to an element in the **Ball rotation
vector** parameter. This parameter measures the ease with which
the moist air traverses the resistive element when driven by a pressure
differential. The size of the vector must be the same as the **Ball
rotation vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient` and **Opening
characteristic** to
`Tabulated`.

### **Ball rotation vector** — Values at which to specify tabulated parameter data `pi / 2 .* (0 : 0.1 : 1)` `rad` (default) | vector of positive numbers

Ball rotation for a given flow coefficient or area. The elements in this
vector must correspond one-to-one with the elements in either the
**Cv flow coefficient vector**, **Kv flow
coefficient vector**, **Sonic conductance
vector**, or **Area vector** parameters. The
elements in this vector must increase monotonically from left to
right.

#### Dependencies

To enable this parameter, set **Opening
characteristic** to
`Tabulated`.

### **Maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow coefficient
when the restriction area available for the flow is at a maximum. This
parameter measures the ease with which the moist air traverses the resistive
element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Kv flow
coefficient` and **Opening
characteristic** to `Area of overlapping
circles`.

### **Kv flow coefficient vector** — *Kv* coefficients that correspond to values in ball rotation vector `[1e-06, .0653, .1293, .2137, .315, .4838, .7875, 1.1813, 1.8381, 2.8112, 3.6]` (default) | vector of positive numbers

Vector of *Kv* flow coefficients.
Each coefficient corresponds to an element in the **Ball rotation
vector** parameter. This parameter measures the ease with which
the moist air traverses the resistive element when driven by a pressure
differential. The size of the vector must be the same as the **Ball
rotation vector** parameter.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Kv flow
coefficient` and **Opening
characteristic** to
`Tabulated`.

### **xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure,
*pin*, and the outlet pressure,
*pout*, defined as (pin−pout)/pin where choking first occurs. If you do not have this value,
look it up in table 2 in ISA-75.01.01 [3]. Otherwise, the default value of 0.7 is reasonable for
many valves.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Cv flow coefficient` or `Kv
flow coefficient`.

### **Maximum sonic conductance** — Sonic conductance that corresponds to maximally open component `12` `l/(bar*s)` (default) | positive scalar

Value of the sonic conductance when the cross-sectional area available for
flow is at a maximum.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Sonic conductance` and **Opening
characteristic** to `Area of overlapping
circles`.

### **Critical pressure ratio** — Ratio of downstream and upstream pressures at which the flow first chokes `0.3` (default) | positive scalar

Pressure ratio at which flow first begins to choke and the flow velocity
reaches its maximum, given by the local speed of sound. The pressure ratio
is the outlet pressure divided by inlet pressure.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Sonic conductance` and **Opening
characteristic** to `Area of overlapping
circles`.

### **Sonic conductance vector** — Sonic conductances that correspond to values in ball rotation vector `[1e-05, .2175, .4312, .7125, 1.05, 1.6125, 2.625, 3.9375, 6.375, 9.75, 12]` `l/(bar*s)` (default) | vector of positive numbers

Vector of sonic conductances inside the resistive element. Each
conductance corresponds to an element in the **Ball rotation
vector** parameter. The size of the vector must be the same as
the **Ball rotation vector** parameter.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Sonic conductance` and **Opening
characteristic** to
`Tabulated`.

### **Critical pressure ratio vector** — Critical pressure ratios that correspond to values in ball rotation vector `0.3 * ones(1, 11)` (default) | vector of positive numbers

Vector of critical pressure ratios at which the flow first chokes. Each
critical pressure ratio corresponds to an element in the **Ball
rotation vector** parameter. The critical pressure ratio is the
fraction of downstream-to-upstream pressures at which the flow velocity
reaches the local speed of sound. The size of the vector must be the same as
the **Ball rotation vector** parameter.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Sonic conductance` and **Opening
characteristic** to
`Tabulated`.

### **Subsonic index** — Exponent used to calculate mass flow in subsonic flow regime `0.5` (default) | positive scalar

Empirical value used to calculate the mass flow rate in the subsonic flow
regime.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Sonic conductance`.

### **ISO reference temperature** — ISO 8778 reference temperature `293.15 K` (default) | scalar

Temperature at standard reference atmosphere, defined as 293.15 K in ISO
8778.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Sonic conductance`.

### **ISO reference density** — ISO 8778 reference density `1.185 kg/m^3` (default) | positive scalar

Density at standard reference atmosphere, defined as 1.185 kg/m3 in ISO
8778.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Sonic conductance`.

### **Cross-sectional area at ports A and B** — Flow area at moist air ports `pi * (0.025 ^ 2) / 4` `m^2` (default) | positive scalar

Cross-sectional area of the valve ports. The valve ports are the paths in
the valve body where the flow meets the ball bore.

### **Ball bore area** — Area of ball bore `pi * (0.02 ^ 2) / 4` `m^2` (default) | positive scalar

Cross-sectional area of the bore in the valve ball.

#### Dependencies

To enable this parameter, set **Valve parameterization** to
`Orifice area based on geometry` and
**Opening characteristic** to `Area of
overlapping circles`.

### **Leakage flow fraction** — Ratio of flow rate `1e-6` (default) | positive scalar

Ratio of the flow rate of the orifice when it is closed to when it is
open.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice area based on
geometry` and **Opening
characteristic** to `Area of overlapping
circles`.

### **Laminar flow pressure ratio** — Pressure ratio at which flow transitions between laminar and turbulent regimes `0.999` (default) | positive scalar

Pressure ratio at which flow transitions between laminar and turbulent
flow regimes. The pressure ratio is the outlet pressure divided by inlet
pressure. Typical values range from `0.995` to
`0.999`.

## Libraries

Simscape / Fluids / Moist Air / Valves & Orifices / Flow Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Ball valve in a moist air network

The Ball Valve (MA) block models flow through a ball valve in
a moist air network. A rotating ball with a central hole, or bore, controls the flow of
the valve. When the bore aligns with the valve inlet and outlet the valve is open. The
physical signal at port **S** controls the ball rotation.

### Valve Parameterizations

The block behavior depends on the **Valve parametrization**
parameter:

- `Cv flow coefficient` — The flow coefficient
  *C*v
  determines the block parameterization. The flow coefficient measures the
  ease with which the moist air flows when driven by a certain pressure
  differential.
- `Kv flow coefficient` — The flow coefficient
  *K*v, where Kv=0.865Cv, determines the block parameterization. The flow
  coefficient measures the ease with which the moist air flows when driven by
  a certain pressure differential.
- `Sonic conductance` — The sonic conductance of
  the resistive element at steady state determines the block parameterization.
  The sonic conductance measures the ease with which the moist air flows when
  *choked*, which is a condition in which the flow
  velocity is at the local speed of sound. Choking occurs when the ratio
  between downstream and upstream pressures reaches a critical value known as
  the *critical pressure ratio*.
- `Orifice area` — The size of the flow restriction
  determines the block parametrization.

### Opening Area

The block calculates the ball valve opening during simulation from the input at
port **S**. The opening area calculations depend on the
**Opening Characteristic** parameter.

**Area of Overlapping Circles**

If you set **Opening Characteristic** to `Area of
overlapping circles`, the block calculates the opening area of
the valve by assuming that the valve port and the ball bore are overlapping
circles. The open area saturates when the input signal from port
**S** goes outside the range of 0 rad to π/2 rad.

The block calculates the opening area as

Aopen=sin(φ)Rbore2[cos−1(λbore)−λbore1−λ2bore]+Rport2[cos−1(λport)−λport1−λ2port]λbore=Rbore2−Rport2+l22Rborelλport=Rport2−Rbore2+l22Rportl

where:

- *Rport* and
  *Rbore* are the
  radii of the valve port and the ball bore, respectively.
- *l* is the displacement of the bore center from
  the valve port center.
- *φ* is the rotation of the ball valve given by
  the physical signal **S**. The valve is fully shut
  at 0 rad and fully open at π/2 rad.

**Tabulated area**

If you set **Opening Characteristic** to
`Tabulated`, the block interpolates the valve
opening from the **Area vector**, **Cv flow coefficient
vector**, **Kv flow coefficient vector**, or
**Sonic conductance vector** parameters. The elements in
these vectors correspond one-to-one to the elements in the **Ball
rotation vector** parameter. The block interpolates between the
data points with linear interpolation and uses nearest extrapolation for points
beyond the table boundaries.

### Momentum Balance

The block equations depend on the **Valve parametrization**
parameter. When you set **Valve parametrization** to
`Cv flow coefficient`, the mass flow rate, m˙, is

m˙=CvSopenSMaxN6Y(pin−pout)ρin,

where:

- *Cv* is the value of the
  **Maximum Cv flow coefficient**
  parameter.
- *Sopen* is the valve
  opening area.
- *SMax* is the maximum
  valve area when the valve is fully open.
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

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout),

where:

Ylam=1−1−Blam3FγxT.

When the pressure ratio, pout/pin, falls below 1−FγxT, the orifice becomes choked and the block switches to the
equation

m˙=23CvSopenSMaxN6FγxTpinρin.

When you set **Valve parametrization** to `Kv flow
coefficient`, the block uses these same equations, but replaces
*Cv* with
*Kv* by using the relation Kv=0.865Cv. For more information on the mass flow equations when the
**Valve parametrization** parameter is `Kv flow
coefficient` or `Cv flow coefficient`,
[2][3].

When you set **Valve parametrization** to `Sonic
conductance`, the mass flow rate, m˙, is

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

where:

- *C* is the value of the **Maximum sonic
  conductance** parameter.
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

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

When the pressure ratio, pout/pin, falls below the critical pressure ratio,
*Bcrit*, the orifice becomes
choked and the block switches to the equation

m˙=CSopenSMaxρrefpinTrefTin.

The `Sonic conductance` setting of the
**Valve parameterization** parameter is for pneumatic
applications. If you use this setting for moist air with high levels of trace
gasses or are modeling a fluid other than air, you may need to scale the sonic
conductance by the square root of the mixture specific gravity.

For more information on the mass flow equations when the **Valve
parametrization** parameter is `Sonic
conductance`, see [1].

When you set **Valve parametrization** to
`Orifice area based on geometry`, the mass flow
rate, m˙, is

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ],

where:

- *Sopen* is the valve
  opening area.
- *S* is the value of the **Cross-sectional
  area at ports A and B** parameter.
- *Cd* is the value of the
  **Discharge coefficient** parameter.
- *γ* is the isentropic exponent.

The block smoothly transitions to a linearized form of the equation when the
pressure ratio, pout/pin, rises above the value of the **Laminar flow pressure
ratio** parameter,
*Blam*,

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

When the pressure ratio, pout/pin, falls below(2γ+1)γγ−1 , the orifice becomes choked and the block switches to the
equation

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2.

For more information on the mass flow equations when the **Valve
parametrization** parameter is `Orifice area based on
geometry`, see [4].

### Mass Balance

The block conserves mass through the valve

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

where *ṁ* is the mass flow rate and the
subscript *w* denotes water vapor, the subscript
*g* denotes trace gas, and the subscript *d*
denotes water droplets.

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

- This block does not model supersonic flow.
