---
type: simulink-block
title: 'Temperature Control Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Moist Air Library / Valves and Orifices / Flow Control Orifices'
documentation_page: 'temperaturecontrolvalvema'
documentation_source_path: 'ref/temperaturecontrolvalvema.html'
language: en
---

# Temperature Control Valve (MA)

## Ports

### Conserving

### **A** — Valve entrance or exit moist air

Moist air conserving port associated with the opening through which
the flow enters or exits the valve. The direction of flow depends on the
pressure differential established across the valve. The block allows
both forward and backward directions.

### **B** — Valve entrance or exit moist air

Moist air conserving port associated with the opening through which
the flow enters or exits the valve. The direction of flow depends on the
pressure differential established across the valve. The block allows
both forward and backward directions.

### **T** — Sensing port moist air | thermal

Moist air or thermal conserving port associated with temperature
sensing. There is no mass or energy flow through this port. When
**Temperature sensing** is `Moist air
sensing port`, port **T** is a moist
air sensing port. When **Temperature sensing** is
`Thermal sensing port`, port
**T** is a thermal sensing port.

#### Dependencies

To enable this port, set **Temperature sensing**
to `Moist air sensing port` or
`Thermal sensing port`.

## Parameters

### **Valve operation** — Sign of change in opening area `Opens above activation temperature` (default) | `Closes above activation temperature`

Sign of the change in opening area that is induced by warming. The opening
area can expand with a rise in temperature or it can contract. The change
begins at an activation temperature and continues with warming conditions
throughout the temperature regulation range of the valve.

The default setting corresponds to a normally closed valve that opens with
rising temperature. The alternative setting corresponds to a normally open
valve that closes with the same.

### **Temperature sensing** — Method to control valve temperature sensing `Valve inlet temperature` (default) | `Moist air sensing port` | `Thermal sensing port`

Method the block uses to measure the temperature that controls the
valve:

- When you set **Temperature sensing** to
  `Valve inlet temperature`, the valve
  uses the upstream temperature to control the valve.
- When you set **Temperature sensing** to
  `Moist air sensing port`, the block
  enables port **T**, which is a moist air sensing
  port. Connect this port to any part of a moist air network to use
  that temperature to control the valve. Port **T**
  is only used for sensing and has no flow going in or out.
- When you set **Temperature sensing** to
  `Thermal sensing port`, the block
  enables the thermal sensing port **T**. Connect
  this port to any part of a thermal network to use that temperature
  to control the valve. Port **T** is only used for
  sensing and has no heat exchange with the environment.

### **Activation temperature** — Temperature at which opening mechanism is triggered `330 K` (default) | scalar

Temperature at which the opening mechanism is triggered. Warming above
this temperature will either open or close the valve, depending on the
setting of the **Valve operation** parameter. The opening
area remains variable throughout the temperature regulation range of the
valve.

### **Temperature regulation range** — Span of temperature interval over which opening area is variable `8 K` (default) | positive scalar

Span of the temperature interval over which the valve opening area varies
with temperature. The interval begins at the activation temperature of the
valve. It ends at the sum of the same with the regulation range specified
here.

### **Sensor time constant** — Time for temperature change to register at inlet sensor `1.5 s` (default) | positive scalar in units of time

Characteristic time for a temperature change to register at the inlet
sensor. This parameter determines the delay between the onset of a change
and a stable measurement of the same, taken as the sensor nears its new
steady state. A value of `0` means that the sensor responds
instantaneously to a temperature change.

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

Simscape / Fluids / Moist Air / Valves & Orifices / Flow Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Temperature control valve in a moist air network

The Temperature Control Valve (MA) block represents an
orifice with a thermostat as a flow control mechanism. The thermostat contains a
temperature sensor and an opening mechanism. The sensor is at the inlet and responds
with a slight delay, captured by a first-order time lag, to variations in temperature.

When the sensor reads a temperature in excess of a preset activation value, the
opening mechanism actuates and the valve begins to open or close, depending on the
operation mode specified by the **Valve operation** parameter. The
change in opening area continues up to the limit of the temperature range of the valve,
beyond which the opening area is a constant. Within the temperature range, the opening
area is a linear function of temperature.

The flow can be laminar or turbulent, and it can reach up to sonic speeds. The maximum
velocity happens at the throat of the valve where the flow is narrowest and fastest. The
flow chokes and the velocity saturates when a drop in downstream pressure can no longer
increase the velocity. Choking occurs when the back-pressure ratio reaches the critical
value characteristic of the valve. The block does not capture supersonic flow.

### Control Temperature

The temperature reading at the inlet is the control signal for the valve. The more
the temperature reading rises over the activation temperature, the more the opening
area diverges from maximally closed when **Valve operation** is
`Opens above activation temperature`, or from fully
open when **Valve operation** is `Closes above
activation temperature`.

The difference between the sensor temperature reading and the activation
temperature is the temperature overshoot. The block normalizes this variable against
the temperature regulation range of the valve. The fraction of valve opening is

T^=TS-TActΔT,

where:

- *TAct* is the value of the
  **Activation temperature** parameter.
- *TS* is the sensor temperature
  reading.

  - When **Temperature sensing** is
    `Valve inlet temperature`,
    *TS* is the
    upstream temperature of the valve.
  - When **Temperature sensing** is
    `Moist air sensing port`,
    *TS* is the
    temperature of the moist air network where it connects to port
    **T**.
  - When **Temperature sensing** is
    `Thermal sensing port`,
    *TS* is the
    temperature of the thermal network where it connects to port
    **T**.
- *ΔT* is the value of the **Temperature
  regulation range** parameter.

**Numerical Smoothing**

When the **Smoothing factor** parameter is nonzero, the block
applies numerical smoothing to the fraction of valve opening, T^. Enabling smoothing helps maintain numerical robustness in
your simulation.

For more information, see Numerical Smoothing.

**Sensor Dynamics**

To emulate a real temperature sensor, which can only register a shift in
temperature gradually, the block adds a first-order time lag to the temperature
reading, *TS*. The lag gives the sensor
a transient response to variations in temperature. This expression for
*TS* is

ddtTS=TIn−TSτ,

where *TIn* is the
actual inlet temperature at the current time step of the simulation and
*τ* is the value of the **Sensor time
constant** parameter. The smaller this parameter is, the faster the
sensor responds.

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

The block equations depend on the **Orifice parametrization**
parameter. When you set **Orifice parametrization** to
`Cv flow coefficient parameterization`, the mass
flow rate, m˙, is

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
flow coefficient` or `Cv flow
coefficient`, [2][3].

When you set **Orifice parametrization** to `Sonic
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

For more information on the mass flow equations when the **Orifice
parametrization** parameter is `Sonic
conductance`, see [1].

When you set **Orifice parametrization** to `Orifice
area`, the mass flow rate, m˙, is

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
parametrization** parameter is `Orifice area`,
see [4].

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

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or
Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

### Assumptions and Limitations

- This block does not model supersonic flow.
