---
type: simulink-block
title: 'Poppet Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Flow Control Valves'
documentation_page: 'poppetvalvema'
documentation_source_path: 'ref/poppetvalvema.html'
language: en
---

# Poppet Valve (MA)

## Ports

### Conserving

### **A** — Valve entry or exit moist air

Liquid entry or exit port to the valve.

### **B** — Valve entry or exit moist air

Liquid entry or exit port to the valve.
### Input

### **S** — Stem displacement, m physical signal

Displacement of the valve control member in m, specified as a physical
signal.

## Parameters

### **Poppet geometry** — Type of poppet `Cylindrical stem` (default) | `Round ball`

Type of poppet. You can choose either a cylindrical or ball-shaped control
member.

### **Valve seat geometry** — Geometry of valve seat `Sharp-edged` (default) | `Conical`

Geometry of valve seat. The block uses this parameter to calculate the
open area between the poppet and seat.

#### Dependencies

To enable this parameter, set **Poppet geometry** to
`Round ball`.

### **Ball diameter** — Diameter of ball control member `0.01 m` (default) | positive scalar

Diameter of the ball control member.

#### Dependencies

To enable this parameter, set **Poppet geometry** to
`Round ball`.

### **Orifice diameter** — Seat orifice diameter `7e-3 m` (default) | positive scalar

Seat orifice diameter.

#### Dependencies

To enable this parameter, set **Poppet geometry** to
`Round ball`.

### **Stem diameter** — Diameter of cylindrical stem `0.01 m` (default) | positive scalar

Diameter of the cylindrical stem.

#### Dependencies

To enable this parameter, set **Poppet geometry** to
`Cylindrical stem`.

### **Seat cone angle** — Angle of seat opening `120 deg` (default) | positive scalar

Angle of the seat opening.

#### Dependencies

To enable this parameter, set either:

- **Poppet geometry** to
  `Cylindrical stem`
- **Poppet geometry** to `Round
  ball` and **Valve seat geometry** to `Conical`

### **Control member position at closed orifice** — Control member offset `0 m` (default) | positive scalar

Poppet offset when valve is closed. A positive, nonzero value indicates a
partially open valve. A negative, nonzero value indicates an overlapped
valve that remains closed for an initial displacement set by the physical
signal at port **S**.

### **Valve parameterization** — Parameterization used to specify flow characteristics of orifice `Orifice area based on geometry` (default) | `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

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
- `Orifice area based on geometry` — The
  size of the flow restriction determines the block parametrization.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar in the range of [0,1]

Correction factor that accounts for discharge losses in theoretical
flows.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice area based on
geometry`.

### **Maximum Cv flow coefficient** — Cv coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow coefficient
when the restriction area available for flow is at a maximum. This parameter
measures the ease with which the moist air traverses the resistive element
when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient`.

### **xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure,
*pin*, and the outlet pressure,
*pout*, defined as (pin−pout)/pin where choking first occurs. If you do not have this value,
look it up in table 2 in ISA-75.01.01 [3]. Otherwise, the default value of 0.7 is reasonable for
many valves.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient` or `Kv flow
coefficient`.

### **Maximum Kv flow coefficient** — Kv coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Maximum value of the *Kv* flow
coefficient when the restriction area available for flow is at a maximum.
This parameter measures the ease with which the moist air traverses the
resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Kv flow
coefficient`.

### **Maximum sonic conductance** — Sonic conductance corresponding to maximally open component `12 l/(bar*s)` (default) | positive scalar

Value of the sonic conductance when the cross-sectional area available for
flow is at a maximum.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance`.

### **Critical pressure ratio** — Ratio of downstream and upstream pressures at which the flow first chokes `0.3` (default) | positive scalar

Pressure ratio at which flow first begins to choke and the flow velocity
reaches its maximum, given by the local speed of sound. The pressure ratio
is the outlet pressure divided by inlet pressure.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Sonic
conductance`.

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

### **Leakage flow fraction** — Ratio of flow rates `1e-6` (default) | positive scalar

Ratio of the flow rate of the orifice when it is closed to when it is
open.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the orifice is in near-open or near-closed positions.
Set this parameter to a nonzero value less than one to increase the
stability of your simulation in these regimes.

### **Laminar flow pressure ratio** — Pressure ratio at which flow transitions between laminar and turbulent regimes `0.999` (default) | positive scalar

Pressure ratio at which flow transitions between laminar and turbulent
flow regimes. The pressure ratio is the outlet pressure divided by inlet
pressure. Typical values range from `0.995` to
`0.999`.

### **Cross-sectional area at ports A and B** — Flow area at moist air ports `0.01 m^2` (default) | positive scalar

Area normal to the flow path at each port. The ports are equal in size. The value of this
parameter should match the inlet area of the components to which the
resistive element connects.

## Libraries

Simscape / Fluids / Moist Air / Valves & Orifices / Flow Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Poppet valve in a moist air network

The Poppet Valve (MA) block represents an orifice with
a translating ball that moderates flow through the valve. In the fully closed position,
the ball rests at the perforated seat, and fully blocks the fluid from passing between
ports **A** and **B**. The area between the ball and
seat is the opening area of the valve.

The flow can be laminar or turbulent, and it can reach up to sonic speeds. The maximum
velocity happens at the throat of the valve where the flow is narrowest and fastest. The
flow chokes and the velocity saturates when a drop in downstream pressure can no longer
increase the velocity. Choking occurs when the back-pressure ratio reaches the critical
value characteristic of the valve. The block does not capture supersonic flow.

Side-view schematic explaining the relationship between the seat, the poppet, and the open area. The seat is a V-shape. The poppet is rectangular. The open area is the orange trapezoid depicting where flow occurs.

Top-view schematic explaining the relationship between the seat, the poppet, and the open area. The seat is the outside ring. The poppet is the filled-in inner circle. The open area is the ring between the poppet and the seat.

### Cylindrical Stem Poppet Opening Area

The opening area of the valve is calculated as:

Aopen=πhsin(θ2)[ds+h2sin(θ)]+Aleak,

where:

- *h* is the vertical distance between the outer edge
  of the cylinder and the seat, indicated in the schematic above.
- *θ* is the **Seat cone
  angle**.
- *d*s is the **Stem
  diameter**.
- *A*leak is the
  **Leakage area**.

The opening area is bounded by the maximum displacement
*h*max:

hmax=ds[1+cos(θ2)−1]sin(θ).

For any stem displacement larger than
*h*max,
*A*open is the sum of the maximum
orifice area and the **Leakage area**:

Aopen=π4ds2+Aleak.

For any combination of the signal at port **S**
and the cylinder offset less than 0, the minimum valve area is the **Leakage
area**.

### Round Ball Poppet Opening Area

**Sharp-edged Seat Geometry**

The opening area of the valve is calculated as:

Aopen,sharp−edged=πrO(Gsharp+h)2+rO2[1−rB2(Gsharp+h)2+rO2]+Aleak,

where:

- *h* is the vertical distance between the outer
  edge of the cylinder and the seat, indicated in the schematic
  above.
- *r*O is the seat orifice
  radius, calculated from the **Orifice
  diameter**.
- *r*B is the radius of the
  ball, calculated from the **Ball diameter**.
- *G*sharp is the geometric
  parameter: Gsharp=rB2−rO2.
- *A*leak is the
  **Leakage area**.

The opening area is bounded by the maximum displacement
*h*max:

hmax=2rB2−rO2+rOrO2+4rB22−Gsharp.

For any ball displacement larger than
*h*max,
*A*open is the sum of the maximum
orifice area and the **Leakage area**:

Aopen=π4dO2+Aleak.

For any combination of the signal at port
**S** and the ball offset that is less than 0, the minimum
valve area is the **Leakage area**.

**Conical Seat Geometry**

The opening area of the valve is calculated as:

Aopen,conical=Gconicalh+π2sin(θ)sin(θ2)h2+Aleak,

where:

- *h* is the vertical distance between the outer
  edge of the cylinder and the seat, indicated in the schematic
  above.
- *θ* is the **Seat cone
  angle**.
- *G*conical is the
  geometric parameter: Gconical=πrBsin(θ), where *r*B
  is the ball radius.
- *A*leak is the
  **Leakage area**.

The opening area is bounded by the maximum displacement
*h*max:

hmax=rB2+rO2cos(θ2)−rBsin(θ2).

For any ball displacement larger than
*h*max,
*A*open is the sum of the maximum
orifice area and the **Leakage area**:

Aopen=π4dO2+Aleak.

For any combination of the signal at port
**S** and the ball offset that is less than 0, the minimum
valve area is the **Leakage area**.

### Valve Parameterizations

The block behavior depends on the **Valve parametrization**
parameter:

- `Cv flow coefficient` — The flow coefficient
  *C*v
  determines the block parameterization. The flow coefficient measures the
  ease with which the moist air can flow when driven by a certain pressure
  differential.
- `Kv flow coefficient` — The flow coefficient
  *K*v, where Kv=0.865Cv, determines the block parameterization. The flow
  coefficient measures the ease with which the moist air can flow when driven
  by a certain pressure differential.
- `Sonic conductance` — The sonic conductance of
  the resistive element at steady state determines the block parameterization.
  The sonic conductance measures the ease with which the moist air can flow
  when *choked*, which is a condition in which the flow
  velocity is at the local speed of sound. Choking occurs when the ratio
  between downstream and upstream pressures reaches a critical value known as
  the *critical pressure ratio*.
- `Orifice area based on geometry` — The size of
  the flow restriction determines the block parametrization.

The block scales the specified flow capacity by the fraction of valve opening. As
the fraction of valve opening rises from `0` to
`1`, the measure of flow capacity scales from its specified
minimum to its specified maximum.

### Momentum Balance

The block equations depend on the **Valve parameterization** parameter.
When you set **Valve parameterization** to `Cv flow
coefficient`, the mass flow rate, m˙, is

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

When you set **Valve parameterization** to `Kv flow
coefficient`, the block uses these same equations, but replaces
*Cv* with
*Kv* by using the relation Kv=0.865Cv. For more information on the mass flow equations when the
**Valve parameterization** parameter is `Kv
flow coefficient` or `Cv flow
coefficient`, [2][3].

When you set **Valve parameterization** to `Sonic
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
parameterization** parameter is `Sonic
conductance`, see [1].

When you set **Valve parameterization** to `Orifice area
based on geometry`, the mass flow rate, m˙, is

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
parameterization** parameter is `Orifice area based on
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
