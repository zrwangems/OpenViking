---
type: simulink-block
title: 'Check Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Directional Control Valves'
documentation_page: 'checkvalveg'
documentation_source_path: 'ref/checkvalveg.html'
language: en
---

# Check Valve (G)

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
- name: Cracking pressure differential
  summary: Pressure drop required to open valve 0.01 MPa (default) | positive scalar
  group: ''
- name: Maximum opening pressure differential
  summary: Pressure drop at which valve is fully open 0.02 MPa (default) | positive scalar
  group: ''
- name: Cracking pressure (gauge)
  summary: Minimum pressure at inlet required to open valve 0.01 MPa (default) | positive scalar
  group: ''
- name: Maximum opening pressure (gauge)
  summary: Maximum pressure at inlet 0.02 MPa (default) | positive scalar
  group: ''
- name: Valve parameterization
  summary: Parameterization used to specify flow characteristics of orifice Cv flow coefficient (default) | Kv flow coefficient
    | Sonic conductance | Orifice area
  group: ''
- name: Maximum Cv flow coefficient
  summary: Cv coefficient that corresponds to maximally open component 4 (default) | positive scalar
  group: ''
- name: xT pressure differential ratio factor at choked flow
  summary: Ratio of pressure differentials 0.7 (default) | positive scalar
  group: ''
- name: Maximum Kv flow coefficient
  summary: Kv coefficient that corresponds to maximally open component 3.6 (default) | positive scalar
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
- name: Maximum orifice area
  summary: Flow area corresponding to maximally open component 1e-4 m^2 (default) | positive scalar
  group: ''
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar in the range of [0,1]
  group: ''
- name: Leakage flow fraction
  summary: Ratio of flow rates 1e-6 (default) | positive scalar
  group: ''
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range [0,1]
  group: ''
- name: Laminar flow pressure ratio
  summary: Pressure ratio at which flow transitions between laminar and turbulent regimes 0.999 (default) | positive scalar
  group: ''
- name: Cross-sectional area at ports A and B
  summary: Flow area at gas ports 0.01 m^2 (default) | positive scalar
  group: ''
```

### **Opening pressure specification** — Choice of pressure measurement to use as valve control signal `Pressure difference of port A relative to port B` (default) | `Gauge pressure at port A`

Choice of pressure measurement to use as valve control signal. The block uses this
setting to determine when the valve should begin to open. In the default
setting, `Pressure difference of port A relative to port
B`, the opening pressure of the valve is expressed as a
pressure drop from inlet to outlet. In the alternative setting,
`Gauge pressure at port A`, it is expressed as
a gauge pressure.

### **Cracking pressure differential** — Pressure drop required to open valve `0.01 MPa` (default) | positive scalar

Minimum pressure drop, from inlet to outlet, required to open the valve.
This value marks the beginning of the pressure differential range of the
valve, over which it progressively opens to allow for increased flow.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Pressure difference of port
A relative to port B`.

### **Maximum opening pressure differential** — Pressure drop at which valve is fully open `0.02 MPa` (default) | positive scalar

Pressure drop, from inlet to outlet, at which the valve is fully open.
This value marks the end of the pressure differential range of the valve,
over which the same progressively opens to allow for increased flow.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Pressure difference of port
A relative to port B`.

### **Cracking pressure (gauge)** — Minimum pressure at inlet required to open valve `0.01 MPa` (default) | positive scalar

Minimum gauge pressure at the inlet (port **A**) required
to open the valve. This value marks the beginning of the pressure range of
the valve, over which the same progressively opens to allow for increased
flow.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Gauge pressure at port
A`.

### **Maximum opening pressure (gauge)** — Maximum pressure at inlet `0.02 MPa` (default) | positive scalar

Maximum pressure at inlet port **A**, at which the valve is fully open.
This value marks the end of the pressure differential range of the valve,
over which the same progressively opens to allow for increased flow. If the
valve does not fully open in your model as expected, you can try lowering
the value of this parameter.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Gauge pressure at port
A`.

### **Valve parameterization** — Parameterization used to specify flow characteristics of orifice `Cv flow coefficient` (default) | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

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

### **Maximum orifice area** — Flow area corresponding to maximally open component `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the orifice opening when the cross-sectional area
available for flow is at a maximum.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice
area`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar in the range of [0,1]

Correction factor that accounts for discharge losses in theoretical
flows.

#### Dependencies

To enable this parameter, set **Valve
parameterization** to `Orifice
area`.

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

Simscape / Fluids / Gas / Valves & Orifices / Directional Control Valves

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

## Description

Check valve in a gas network

The Check Valve (G) block represents an orifice with a
unidirectional opening mechanism that prevents unwanted backflow. The opening mechanism
responds to pressure, and opens the orifice when the pressure gradient falls from the
inlet at port **A** to the outlet at port **B**. Check
valves protect components upstream against pressure surges, temperature spikes, and
chemical contamination stemming from points downstream.

The valve begins opening at the cracking pressure and continues opening until the end of the
pressure regulation range. The cracking pressure is the initial resistance, due to
friction or spring forces, that the valve must overcome to crack open. Below this
threshold, the valve is closed and only leakage flow can pass. Past the end of the
pressure regulation range, the valve is fully open and the flow at the maximum value is
determined by the instantaneous pressure conditions.

The flow can be laminar or turbulent, and it can reach up to sonic speeds. The maximum
velocity happens at the throat of the valve where the flow is narrowest and fastest. The
flow chokes and the velocity saturates when a drop in downstream pressure can no longer
increase the velocity. Choking occurs when the back-pressure ratio reaches the critical
value characteristic of the valve. The block does not capture supersonic flow.

### Control and Other Pressures

The pressure to which the valve responds is the control pressure. By default, the control
pressure is the drop from inlet to outlet. This setting ensures that the valve
closes if the direction of flow should reverse.

You can also specify the control pressure as the gauge pressure at the inlet. Use this
setting if you know that the inlet will always be at a higher pressure than the
outlet. For example, when the inlet connects to a pressure source, such as a
pump.

You can select the control pressure by setting the **Opening pressure
specification** parameter to `Pressure difference of port A
relative to port B` or `Gauge pressure at port
A`.

**Pressure difference of port A relative to port B**

When the **Opening pressure specification** parameter is
`Pressure difference of port A relative to port B`:

- The control pressure is:

  PCtl=PA-PB,

  where
  *PA* is the absolute
  pressure at port **A** and
  *PB* is the absolute
  pressure at port **B**.
- The cracking pressure,
  *PCrk*, is the value of
  the **Cracking pressure differential** parameter.
- The maximum pressure of the valve,
  *PMax*, where the
  valve is fully open, is the value of the **Maximum opening
  pressure differential** parameter.

**Gauge pressure at port A**

When the **Opening pressure specification** parameter is
`Gauge pressure at port A`:

- The control pressure is

  PCtrl=PA−PAtm,

  where
  *PAtm* is the
  atmospheric pressure specified in the Gas Properties
  (G) block of the model.
- The cracking pressure,
  *PCrk*, is the value of
  the **Cracking pressure (gauge)** parameter.
- The maximum pressure of the valve,
  *PMax*, where the
  valve is fully open, is the value of the **Maximum opening
  pressure (gauge)** parameter.

### Fraction of Valve Opening

The degree to which the control pressure exceeds the cracking pressure determines how much
the valve opens. The normalized control pressure is

P^=PCtrl−PCrkPMax−PCrk,

where:

- *PCtrl* is the control
  pressure.
- *PCrk* is the cracking
  pressure.
- *PMax* is the maximum opening
  pressure.

The fraction is normalized so that it is `0` in the fully closed valve and
`1` in the fully open valve. If the calculation returns a value
outside of these bounds, the block saturates the value to the nearest of the two
limits.

The fraction of valve opening, *L*, is

L=(1-Lleak)P^+Lleak,

where *Lleak* is the
value of the **Leakage flow fraction** parameter.

**Numerical Smoothing**

When the **Smoothing factor** parameter is nonzero, the block applies
numerical smoothing to the normalized control pressure, p^. Enabling smoothing helps maintain numerical robustness in
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

The block scales the specified flow capacity by the fraction of valve opening. As the
fraction of valve opening rises from `0` to `1`,
the measure of flow capacity scales from its specified minimum to its specified
maximum.

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
