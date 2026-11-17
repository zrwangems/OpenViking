---
type: simulink-block
title: 'Pilot-Operated Check Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Directional Control Valves'
documentation_page: 'pilotoperatedcheckvalvema'
documentation_source_path: 'ref/pilotoperatedcheckvalvema.html'
language: en
---

# Pilot-Operated Check Valve (MA)

## Ports
```yaml
ports:
- name: A
  summary: Valve entrance or exit moist air
  direction: conserving
- name: B
  summary: Valve entrance or exit moist air
  direction: conserving
- name: X
  summary: Pilot port moist air
  direction: conserving
```

### Conserving

### **A** — Valve entrance or exit moist air

Moist air conserving port associated with the opening through which
the flow enters the valve during normal operation when the pilot
mechanism is disabled. This port can serve as an exit only when the
pilot port is pressurized to a sufficient degree.

### **B** — Valve entrance or exit moist air

Moist air conserving port associated with the opening through which
the flow exits the valve during normal operation when the pilot
mechanism is disabled.

### **X** — Pilot port moist air

Moist air conserving port associated that actuates, by the application
of a sufficient pressure, the pilot mechanism that opens the valve for
reverse flow. There is no mass flow through this port.
## Parameters
```yaml
parameters:
- name: Valve parameterization
  summary: Parameterization used to specify flow characteristics of orifice Cv flow coefficient (default) | Kv flow coefficient
    | Sonic conductance | Orifice area
  group: ''
- name: Pilot configuration
  summary: Method for handling negative pilot pressure forces Rigidly connected pilot spool and poppet (default) | Disconnected
    pilot spool and poppet
  group: ''
- name: Pilot pressure specification
  summary: Choice of pressure measurement to use as valve control signal Pressure difference of port X relative to port A
    (default) | Gauge pressure at port X
  group: ''
- name: Cracking pressure differential
  summary: Effective control pressure at which the valve first opens 0.01 MPa (default) | positive scalar
  group: ''
- name: Maximum opening pressure differential
  summary: Effective control pressure at which the valve is fully open 0.02 MPa (default) | positive scalar
  group: ''
- name: Pilot ratio
  summary: Ratio of pilot port area to inlet port area 1 (default) | positive scalar
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
  summary: Flow area at moist air ports 0.01 m^2 (default) | positive scalar
  group: ''
```

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

### **Pilot configuration** — Method for handling negative pilot pressure forces `Rigidly connected pilot spool and poppet` (default) | `Disconnected pilot spool and poppet`

Method the block uses when the pilot pressure is negative:

- `Rigidly connected pilot spool and
  poppet` — The pilot spool transmits both positive
  and negative pilot pressure forces, so the block uses
  *ppilot* as
  is.
- `Disconnected pilot spool and poppet` —
  The pilot spool only transmits positive pilot pressure forces, so
  the block limits *ppilot* to
  positive values only. The block replaces negative values with
  zero.

### **Pilot pressure specification** — Choice of pressure measurement to use as valve control signal `Pressure difference of port X relative to port A` (default) | `Gauge pressure at port X`

Choice of pressure measurement to use as valve control signal. The block
uses this setting to determine when the valve should begin to open. In the
default setting, `Pressure difference of port X relative to port
A`, the opening pressure of the valve is expressed as a
pressure drop from the pilot port, **X**, to the inlet,
**A**. In the alternative setting, `Gauge
pressure at port X`, it is expressed as a gauge inlet
pressure measured against the environment pressure.

### **Cracking pressure differential** — Effective control pressure at which the valve first opens `0.01 MPa` (default) | positive scalar

Effective pressure differential at which the valve begins to open. This
differential is the sum of the pressure drop from inlet to outlet with the
product of the pilot pressure and the pilot ratio. The pilot pressure used
depends on the setting of the **Pilot pressure
specification** parameter.

### **Maximum opening pressure differential** — Effective control pressure at which the valve is fully open `0.02 MPa` (default) | positive scalar

Effective pressure differential at which the valve is fully open. This
differential is the sum of the pressure drop from inlet to outlet with the
product of the pilot pressure and the pilot ratio. The pilot pressure used
depends on the setting of the **Pilot pressure
specification** parameter.

### **Pilot ratio** — Ratio of pilot port area to inlet port area `1` (default) | positive scalar

Ratio of the pilot port area to the inlet port area.

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

### **Cross-sectional area at ports A and B** — Flow area at moist air ports `0.01 m^2` (default) | positive scalar

Area normal to the flow path at each port. The ports are equal in size.
The value of this parameter should match the inlet area of the components to
which the resistive element connects.
## Libraries

Simscape / Fluids / Moist Air / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Pilot-operated check valve in a moist air network

The Pilot-Operated Check Valve (MA) block represents a
check valve with an override mechanism that allows backflow in the moist air domain. A
check valve is an orifice with a unidirectional opening mechanism that prevents
backflow.

The **X** port of the block represents a pilot port that serves as an
override mechanism. During normal operation, the pilot port is inactive and the valve
behaves as a check valve. In a check valve, the orifice only opens when the pressure
gradient across the valve drops from inlet to outlet. The orifice opening prevents
backflow, which requires the reverse pressure gradient, and protects the upstream
components of the valve from downstream pressure surges, temperature spikes, and
chemical contamination.

For sufficient values at port **X**, the block pressurizes the pilot
port and forces the control element of the valve off its seat, permitting backflow. The
valve is then open to flow in both directions, with a reverse pressure drop from outlet
to inlet driving the flow upstream. The seat, which lies in the path of the flow,
determines if the valve is open. When it is covered, the flow is cut off and the valve
is closed.

The valve begins opening at the cracking pressure and continues opening until the end
of the pressure regulation range. The cracking pressure is the initial resistance, due
to friction or spring forces, that the valve must overcome to crack open. Below this
threshold, the valve is closed and only leakage flow can pass. Past the end of the
pressure regulation range, the valve is fully open and the flow at the maximum value is
determined by the instantaneous pressure conditions.

The flow can be laminar or turbulent, and it can reach up to sonic speeds. The maximum
velocity happens at the throat of the valve where the flow is narrowest and fastest. The
flow chokes and the velocity saturates when a drop in downstream pressure can no longer
increase the velocity. Choking occurs when the back-pressure ratio reaches the critical
value characteristic of the valve. The block does not capture supersonic flow.

### Control and Other Pressures

The opening of the valve depends on the pilot pressure and the pressure drop from
the inlet to the outlet. The pressure that opens the valve is

PCtrl=kpilotPpilot+PA-PB,

where:

- *Ppilot* is the pilot
  pressure.
- *kpilot* is the pilot
  ratio.
- *PA* is the gauge pressure at port
  **A**.
- *PB* is the gauge pressure at port
  **B**.

The block determines the port pressures against absolute zero during simulation.

The pilot pressure can be relative to the inlet, port **A**, or
relative to the environment. You can select the pilot pressure by setting the
**Pilot pressure specification** parameter to
`Pressure difference of port X relative to port B` or
`Gauge pressure at port X`.

If you select `Gauge pressure at port X`, the pilot
pressure is

Ppilot=PX−Patm,

where *PAtm* is the
atmospheric pressure and *PX* is the
absolute value of the pressure at the pilot port. If you select
`Pressure difference of port X relative to port A`, the
pilot pressure is

Ppilot=PX−PA,

where *PA* is the
absolute value of pressure at the inlet of the valve, port
**A**.

When the **Pilot configuration** parameter is
`Rigidly connected pilot spool and poppet`, the pilot
spool transmits both positive and negative pilot forces and the block uses
*Ppilot* as is in the equation for
*PCtrl*. When the **Pilot
configuration** parameter is `Disconnected pilot spool and
poppet`, the pilot spool transmits only positive pilot pressure
forces and *Ppilot* is limited to positive
values. The block uses
`max(Ppilot,0)` in
the equation for *PCtrl*.

### Fraction of Valve Opening

The degree to which the control pressure exceeds the cracking pressure determines
how much the valve opens. The fraction of valve opening is

P^=PCtrl−PCrkPMax−PCrk,

where:

- *PCtrl* is the control
  pressure.
- *PCrk* is the cracking
  pressure specified by the **Cracking pressure
  differential** parameter.
- *PMax* is the maximum opening
  pressure specified by the **Maximum opening pressure
  differential** parameter.

The fraction is normalized so that it is `0` in the fully closed
valve and `1` in the fully open valve. If the calculation returns a
value outside of these bounds, the block saturates the value to the nearest of the
two limits.

**Numerical Smoothing**

When the **Smoothing factor** parameter is nonzero, the block
applies numerical smoothing to the normalized control pressure, p^. Enabling smoothing helps maintain numerical robustness in
your simulation.

For more information, see Numerical Smoothing.

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
- `Orifice area` — The size of the flow restriction
  determines the block parametrization.

The block scales the specified flow capacity by the fraction of valve opening. As
the fraction of valve opening rises from `0` to
`1`, the measure of flow capacity scales from its specified
minimum to its specified maximum.

### Momentum Balance

The block equations depend on the **Valve parameterization** parameter.
When you set **Valve parameterization** to `Cv flow
coefficient`, the mass flow rate, m˙, is

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

When you set **Valve parameterization** to `Kv flow
coefficient`, the block uses these same equations, but replaces
*Cv* with
*Kv* by using the relation Kv=0.865Cv. For more information on the mass flow equations when the
**Valve parameterization** parameter is `Kv
flow coefficient` or `Cv flow
coefficient`, see [2][3].

When you set **Valve parameterization** to `Sonic
conductance`, the mass flow rate, m˙, is

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

For more information on the mass flow equations when the **Valve
parameterization** parameter is `Sonic
conductance`, see [1].

When you set **Valve parameterization** to `Orifice
area`, the mass flow rate, m˙, is

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

For more information on the mass flow equations when the **Valve
parameterization** parameter is `Orifice
area`, see [4].

### Mass Balance

The block assumes the volume and mass of fluid inside the valve is very small and ignores
these values. As a result, no amount of fluid can accumulate in the valve. The block
conserves mass through the valve

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
