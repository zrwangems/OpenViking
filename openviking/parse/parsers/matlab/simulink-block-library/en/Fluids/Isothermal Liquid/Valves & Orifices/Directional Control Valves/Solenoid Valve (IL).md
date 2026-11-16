---
type: simulink-block
title: 'Solenoid Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'solenoidvalveil'
documentation_source_path: 'ref/solenoidvalveil.html'
language: en
---

# Solenoid Valve (IL)

## Ports

### Input

### **S** — Signal that controls valve, unitless physical signal

Physical signal that controls the valve. When the signal at port **S**
is above 0.5, the solenoid turns on and the valve opens. When the signal
at port **S** falls below 0.5 the solenoid turns off,
and the valve closes.

#### Dependencies

To enable this port, set **Solenoid control** to
`Physical signal`.
### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port.

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive terminal of the valve
control.

#### Dependencies

To enable this port, set **Solenoid control** to
`Electrical ports`.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative terminal of the valve control.

#### Dependencies

To enable this port, set **Solenoid control** to
`Electrical ports`.

## Parameters

### **Solenoid control** — Select valve control method `Physical signal` (default) | `Electrical ports`

Select the method the block uses to control the valve. If you select
`Physical signal`, the block uses the physical
signal **S** to control the valve. If you select
`Electrical network`, the block enables the
electrical **+** and **-** ports and
models the electrical responses.

### **Valve initial position** — Initial position for valve `Closed` (default) | `Open`

Whether the initial position of the valve is open or closed.

### **Opening switching time** — Time for flow rate to rise when opening `0.05` `s` (default) | positive scalar

Time from the solenoid turning on to the flow rate reaching 90% of the way between its
maximum and minimum values.

If **Solenoid control** is set to
`Electrical ports`, calculate this parameter at
the value of the **Rated voltage** parameter using a step
input.

### **Closing switching time** — Time for flow rate to fall when closing `0.1` `s` (default) | positive scalar

Time from the solenoid turning off to the flow rate falling to 10% of the way between its
maximum and minimum values.

If **Solenoid control** is set to
`Electrical ports`, calculate this parameter at
the value of the **Rated voltage** parameter using a step
input.

### **Maximum opening area** — Area of fully opened valve `1e-4` `m^2` (default) | positive scalar

Cross-sectional area of the valve in the fully open position.

### **Leakage area** — Valve gap area when in fully closed position `1e-10` `m^2` (default)

Sum of all the gaps when the valve is in the fully closed position. The
block saturates any valve area smaller than this value to the specified
leakage area. The leakage area contributes to numerical stability by
maintaining continuity in the flow.

### **Cross-sectional area at ports A and B** — Area at valve entry or exit `inf` `m^2` (default) | positive scalar

Cross-sectional area at the entry and exit ports **A**
and **B**. The block uses this area in the pressure-flow
rate equation that determines the mass flow rate through the valve.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether the block accounts for pressure increase when fluid flows from a region of
smaller cross-sectional area to a region of larger cross-sectional
area.

### **Rated voltage** — Solenoid rated voltage `12` `V` (default) | positive scalar

Rated voltage of the solenoid. Calculate the values of the **Opening switching
time** and **Closing switching time**
parameters at this voltage by using a step input.

#### Dependencies

To enable this parameter, set **Solenoid control** to
`Electrical ports`.

### **Nominal current** — Steady-state current `2e-4` `A` (default) | positive scalar

Steady-state current of the solenoid at the value of the **Rated
voltage** parameter.

#### Dependencies

To enable this parameter, set **Solenoid control** to
`Electrical ports`.

### **Solenoid inductance** — Linear solenoid inductance `1e-6` `H` (default) | positive scalar

Linear inductance of the solenoid. The block approximates the inductance as linear.

#### Dependencies

To enable this parameter, set **Solenoid control** to
`Electrical ports`.

### **Plunger distance of travel** — Distance plunger travels `1.8e-3` `m` (default) | positive scalar

Distance the plunger travels between the fully closed and fully open valve
positions.

#### Dependencies

To enable this parameter, set **Solenoid control** to
`Electrical ports`.

### **Initial current** — Solenoid initial current `0` `A` (default) | positive scalar

Initial current in the solenoid.

#### Dependencies

To enable this parameter, set **Solenoid control** to
`Electrical ports`.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2023b: Connect the valve directly to an electrical network

You can now control the block by connecting it directly to an electrical network.
Set the **Solenoid control** parameter to Electrical network to
model electrical responses and enable the electrical + and - ports.

## Description

Solenoid valve in an isothermal liquid system

The Solenoid Valve (IL) block models flow through a solenoid
valve in an isothermal liquid network. The valve consists of a two-way directional
control valve with a solenoid actuator. The physical signal at port
**S** controls the solenoid. When the signal at port
**S** is above 0.5, the solenoid turns on and the valve opens. When
the signal at port **S** falls below 0.5, the solenoid turns off,
closing the valve.

A solenoid valves consists of a valve body with a spring-loaded plunger that is operated by
an electric solenoid. When the solenoid is on, the magnetic force lifts the spool,
allowing fluid to flow. When the solenoid is off, the spring pushes the plunger back in
place, stopping flow. The block does not model the mechanics of the solenoid explicitly,
but characterizes the opening and closing of the valve using the opening and closing
switching times.

### Mass Flow Rate

The mass flow rate through the valve is

m˙=CdA2ρ¯(1−AAport)Δp(Δp2+Δpcrit2)1/4,

where:

- *A* is the cross-sectional area of the valve.
- *Aport* is the value of the
  **Cross-sectional area at ports A and B**
  parameter.
- *Cd* is the value of the
  **Discharge coefficient** parameter.
- ρ¯ is the average fluid density in the valve.
- *Δp* is the change in pressure across the
  valve.
- *Δpcrit* is the critical pressure,

  Δpcrit=π8Aρ¯(μRecritCd)2,

  where
  *Recrit* is the value of the
  **Critical Reynolds number** parameter and
  *μ* is the fluid viscosity.

### Opening Dynamics

The block assumes that the solenoid behaves as a resistor-inductor series circuit,
represented as

V=iR+L∂i∂t,

where:

- *V* is the voltage across solenoid inductor.
- *R* is the resistance of the solenoid
  inductor.
- *L* is the inductance of the solenoid.
- *i* is the current through the solenoid
  inductor.

The solenoid generates a force proportional to the current squared, Fmag=−12Ki2, where *K* is a proportionality constant. The
expression for the cross-sectional area of the valve, *A(t)*,
depends on the value of the **Solenoid control**
parameter.

**Valve Controlled with Physical Signal**

When you set **Solenoid control** to `Physical
signal`, the block calculates the opening area based on the
signal at port **S**. When the valve is opening,

A(t)=Amax−Aleak7(e−2t−t0τopen−8et−t0τopen)+Amaxt0=tstart+log(4−16−7Amax−A0Amax−Aleak)τopen.

When the valve is closing,

A(t)=(Amax−Aleak)e−t−t0τclose+Aleakt0=tstart+log(A0−AleakAmax−Aleak)τclose,

where:

- *Amax* is the value of the
  **Maximum opening area** parameter.
- *Aleak* is the value of
  the **Leakage area** parameter.
- *tstart* is the time that
  the solenoid turns on or off.
- *A0* is the valve area at
  the time the solenoid turns on or off.
- τopen=−tswitchopenlog(4−15.3), where
  *tswitchopen*
  is the value of the **Opening switching time**
  parameter.
- τclose=tswitchcloselog(0.1), where
  *tswitchclose*
  is the value of the **Closing switching time**
  parameter.

**Valve Controlled with Electrical Ports**

When you set **Solenoid control** to
`Electrical ports`, the block calculates the
opening area based on the electrical network connected to the solenoid valve at
ports **+** and **-**.

The opening area is

A=xl(Amax−Aleak)+Aleak,

where *x* is the plunger position and
*l* is the value of the **Plunger distance of
travel** parameter.

The block models the plunger motion with the force balance expression

mcorex¨=Fmagnetic−Fspring+Fhardstop,

where:

- *mcore* is the mass of the
  moving parts in the solenoid valve.
- *Fspring* is the force
  exerted by the spring to close the valve when the solenoid is off.
- *Fhardstop* is the
  hard-stop force that prevents the plunger from moving beyond the
  fully open and fully closed positions. The block calculates the
  hard-stop by using mode charts. For more information, see Mode Chart Modeling.
- *Fmagnetic* is the force generated by the
  solenoid,

  Fmagnetic=−12Ki2.

The block uses the solution to the force balance expression to calculate
*mcore*,
*Fspring*, and
*K* at the values of the **Rated
voltage**, **Nominal current**, **Opening
switching time**, and **Closing switching time**
parameters. The block then uses these values for
*mcore*,
*Fspring*, and
*K* to solve for the plunger position at all other
times.

### Switching Time

The block characterizes the solenoid valve by using the valve opening and closing
switching times specified by the **Opening switching time**, and
**Closing switching time** parameters, respectively. The
**Opening switching time** parameter is the time from the
solenoid being turned on to the flow rate rising to 90% of the way between its
maximum and minimum values.

Graph showing the increasing valve area vs time when the valve is opening. When the time reaches the opening switching time, the valve area begins to level off.

The **Closing switching time** parameter is the time from the
solenoid being turned off to the flow rate falling to 10% of the way between its
maximum and minimum values.

Graph showing the decreasing valve area vs time when the valve is closing. When the time reaches the closing switching time, the valve area begins to level off.

### Assumptions and Limitations

- The maximum solenoid force is the same as the force generated by the
  spring.
- The damping inside the solenoid and the pressure flow forces are
  negligible.
- The spool is balanced.
- The solenoid travel distance is short enough that the block assumes the
  inductance is linear.
