---
type: simulink-block
title: 'Gate Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Gas Library / Valves and Orifices / Flow Control Orifices'
documentation_page: 'gatevalveg'
documentation_source_path: 'ref/gatevalveg.html'
language: en
---

# Gate Valve (G)

## Ports

### Input

### **L** — Valve control signal, `unitless` physical signal

Input port through which to specify the relative displacement of the gate as a fraction
of its maximum. This input specifies the gate position, which the block
uses to compute the mass flow rate through the valve. This position
should range between `0` for a maximally closed valve
to `1` for a fully open valve.
### Conserving

### **A** — Valve entrance gas

Gas conserving port associated with the opening through which the flow
enters or exits the valve. The direction of flow depends on the pressure
differential established across the valve. The block allows both forward
and backward directions.

### **B** — Valve entrance gas

Gas conserving port associated with the opening through which the flow
enters or exits the valve. The direction of flow depends on the pressure
differential established across the valve. The block allows both forward
and backward directions.

## Parameters

### **Orifice diameter** — Diameter of the bore of the valve `0.01 m` (default) | positive scalar

Diameter of the bore of the valve and of the gate that controls the opening area. The
orifice is assumed to be constant in cross section throughout its length
from one port to the other.

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
measures the ease with which the gas traverses the resistive element when
driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Cv flow
coefficient`.

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

### **Maximum Kv flow coefficient** — Kv coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Maximum value of the *Kv* flow
coefficient when the restriction area available for flow is at a maximum.
This parameter measures the ease with which the gas traverses the resistive
element when driven by a pressure differential.

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

Pressure ratio at which flow first begins to choke and the flow velocity reaches its
maximum, given by the local speed of sound. The pressure ratio is the outlet
pressure divided by inlet pressure.

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

### **Cross-sectional area at ports A and B** — Flow area at gas ports `0.01 m^2` (default) | positive scalar

Area normal to the flow path at each port. The ports are equal in size.
The value of this parameter should match the inlet area of the components to
which the resistive element connects.

## Libraries

Simscape / Fluids / Gas / Valves & Orifices / Flow Control Valves

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

### R2022b: Offset parameter removed

The block no longer has a **Gate displacement fraction offset** parameter
and the block no longer offsets the input signal. This change does not impact
compatibility.

## Description

Gate valve in a gas network

The Gate Valve (G) block represents an orifice with a
translating gate, or *sluice*, as a flow control mechanism. The gate
is circular and must slide perpendicular to the flow due to the constrains of the groove
of its seat. The seat of the valve is annular. The flow passes through the bore, which
is sized to match the gate. The overlap of the gate and the bore determines the opening
area of the valve.

This image shows a gate valve with a conical seat.

The flow can be laminar or turbulent, and it can reach up to sonic speeds. The maximum
velocity happens at the throat of the valve where the flow is narrowest and fastest. The
flow chokes and the velocity saturates when a drop in downstream pressure can no longer
increase the velocity. Choking occurs when the back-pressure ratio reaches the critical
value characteristic of the valve. The block does not capture supersonic flow.

Gate valves generally open quickly. Gate valves are most sensitive to gate displacement
near the closed position, where a small displacement translates into a
disproportionately large change in opening area. Consequently, gate valves have too high
a gain in that region to effectively throttle or modulate flow. You can use this block
as a binary switch to open and close gas circuits.

### Gate Mechanics

In a real valve, the gate connects by a gear mechanism to a handle. When the handle is
turned from a fully closed position, the gate rises from the bore and progressively
opens the valve up to a maximum. Hard stops keep the disk from breaching its minimum
and maximum positions.

The block captures the motion of the disk but not the detail of its mechanics. You specify
the motion as a normalized displacement at port **L**. The input
physical signal carries the fraction of the instantaneous displacement over its
value in the fully open valve.

If you want to model the action of the handle and hard stop, use Simscape
mechanical blocks to capture the displacement signal. However, in many cases, it
suffices to know what displacement to impart to the disk and you do not need to
model the mechanics of the valve.

### Gate Position

The block models the displacement of the gate but not the valve opening or closing
dynamics. The signal at port **L** provides the normalized gate
position, *L*. *L* is a normalized distance
between 0 and 1, which indicates a fully closed valve and a fully open valve,
respectively. If the calculation returns a number outside of this range, the block
sets that number to the nearest bound.

**Numerical Smoothing**

When the **Smoothing factor** parameter is nonzero, the block
applies numerical smoothing to the normalized gate position,
*L*. Enabling smoothing helps maintain numerical robustness
in your simulation.

For more information, see Numerical Smoothing.

### Opening Area

The opening area of the valve is the area of the bore adjusted for the instantaneous
overlap of the gate

Sopen=pD24-SC,

where:

- *Sopen* is the instantaneous
  valve opening area. The block then smooths this area to remove
  derivative discontinuities at the limiting valve positions.
- *D* is the common diameter of the gate and its bore,
  which are identical. This is the value of the **Orifice
  diameter** parameter.
- *SC* is the area of overlap
  between the gate and bore, which the block computes as a function of the
  gate position, *L*:

  SC=D22acos(L)−LD2D2−L2D2.

The figure shows a front view of the valve when maximally closed, partially open, and fully
open, from left to right. The figure also shows the parameters and variables in the
opening area calculation.

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
- `Orifice area based on geometry` — The size of
  the flow restriction determines the block parametrization.

The block scales the specified flow capacity by the fraction of valve opening. As the
fraction of valve opening rises from `0` to `1`,
the measure of flow capacity scales from its specified minimum to its specified
maximum.

### Momentum Balance

The block equations depend on the **Orifice parametrization** parameter.
When you set **Orifice parametrization** to `Cv
flow coefficient parameterization`, the mass flow rate, m˙, is

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

When you set **Orifice parametrization** to `Kv flow
coefficient parameterization`, the block uses these same
equations, but replaces *Cv* with
*Kv* by using the relation Kv=0.865Cv. For more information on the mass flow equations when the
**Orifice parametrization** parameter is `Kv
flow coefficient parameterization` or `Cv flow
coefficient parameterization`, [2][3].

When you set **Orifice parametrization** to `Sonic
conductance parameterization`, the mass flow rate, m˙, is

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
applications. If you use this setting for gases other than air, you may need to
scale the sonic conductance by the square root of the specific gravity.

For more information on the mass flow equations when the **Orifice
parametrization** parameter is `Sonic conductance
parameterization`, see [1].

When you set **Orifice parametrization** to
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

For more information on the mass flow equations when the **Orifice
parametrization** parameter is `Orifice area based on
geometry`, see [4].

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

- The equation for the `Orifice area based on
  geometry` parameterization is less accurate for gases
  that are far from ideal.
- This block does not model supersonic flow.
