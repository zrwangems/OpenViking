---
type: simulink-block
title: 'Pilot-Operated Check Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'pilotoperatedcheckvalvetl'
documentation_source_path: 'ref/pilotoperatedcheckvalvetl.html'
language: en
---

# Pilot-Operated Check Valve (TL)

## Ports

### Conserving

### **A** — Valve entrance thermal liquid

Opening through which the working fluid must, during normal operation
(when the pilot mechanism is disabled), enter the valve. This port can
serve as an exit only when the pilot port is pressurized to a sufficient
degree.

### **B** — Valve entrance thermal liquid

Opening through which the working fluid must, during normal operation
(when the pilot mechanism is disabled), exit the valve.

### **X** — Pilot port thermal liquid

Opening by which to actuate (by the application of a sufficient
pressure) the pilot mechanism that opens the valve for reverse
flow.

## Parameters

### **Pressure control specification** — Choice of pressure measurement to use as valve control signal `Pressure difference of port X relative to port A` (default) | `Pressure at port X`

Choice of pressure measurement to use as pilot control signal. The block
uses the chosen measurement to calculate the control pressure of the valve.
(See the block description for the calculations.)

In the default setting `Pressure difference of port X relative to port
A`, the control pressure is a function of the pressure drop
from the pilot port (**X**) to the inlet
(**A**). In the alternate setting `Pressure
at port X`, it is a function of the gauge pressure at the
inlet.

### **Cracking pressure differential** — Effective control pressure at which the valve first opens `0.01 MPa` (default) | positive scalar in units of pressure

Effective pressure differential at which the valve begins to open. This
differential—the *control pressure* in the block
description—is the sum of the pressure drop from inlet to outlet with the
product of the pilot pressure and the pilot ratio. (The pilot pressure used
depends on the setting of the **Pressure control
specification** parameter.)

### **Maximum opening pressure differential** — Effective control pressure at which the valve is fully open `0.02 MPa` (default) | positive scalar in units of pressure

Effective pressure differential at which the valve is fully open. This
differential—the *control pressure* in the block
description—is the sum of the pressure drop from inlet to outlet with the
product of the pilot pressure and the pilot ratio. (The pilot pressure used
depends on the setting of the **Pressure control
specification** parameter.)

### **Pilot ratio** — Ratio of pilot port area to inlet port area `1` (default) | positive unitless scalar

Ratio of the pilot port area to the inlet port area.

### **Maximum opening area** — Opening area in the fully open position due to sealing imperfections `1e-4 m^2` (default) | positive scalar in units of area

Opening area of the valve in the fully open position, when the valve is at
the upper limit of the pressure regulation range.

### **Leakage area** — Opening area in the maximally closed position due to sealing imperfections `1e-10 m^2` (default) | positive scalar in units of area

Opening area of the valve in the maximally closed position, when only
internal leakage between the ports remains. This parameter serves primarily
to ensure that closure of the valve does not cause portions of the fluid
network to become isolated (a condition known to cause problems in
simulation). The exact value specified here is less important that its being
a (very small) number greater than zero.

### **Smoothing factor** — Amount of smoothing to apply to the valve opening area function `0` (default)

Amount of smoothing to apply to the opening area function of the valve.
This parameter determines the widths of the regions to be smoothed—one
located at the fully open position, the other at the fully closed position.

The smoothing superposes on each region of the opening area function a
nonlinear segment (a third-order polynomial function, from which the
smoothing arises). The greater the value specified here, the greater the
smoothing is, and the broader the nonlinear segments become.

At the default value of `0`, no smoothing is applied. The
transitions to the maximally closed and fully open positions then introduce
discontinuities (associated with zero-crossings), which tend to slow down
the rate of simulation.

### **Cross-sectional area at ports A and B** — Area normal to the flow path at the valve ports `0.01 m^2` (default) | positive scalar in units of area

Area normal to the flow path at the valve ports. The ports are assumed to
be the same in size. The flow area specified here should ideally match those
of the inlets of adjoining components.

### **Discharge coefficient** — Empirical factor defined as the ratio of actual to ideal mass flow rates `0.64` (default) | positive unitless scalar

Ratio of the actual flow rate through the valve to the theoretical value
that it would have in an ideal valve. This semi-empirical parameter measures
the flow allowed through the valve: the greater its value, the greater the
flow rate. Refer to the valve data sheet, if available, for this
parameter.

### **Critical Reynolds number** — Reynolds number at the boundary between laminar and turbulent flow regimes `150` (default) | positive unitless scalar

Reynolds number at which the flow is assumed to transition between laminar
and turbulent regimes.

## Libraries

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Check valve with control port to enable flow in reverse direction

The Pilot-Operated Check Valve (TL) block models a
check valve with an override mechanism to allow for backflow when activated. (A check
valve in turn is an orifice with a unidirectional opening mechanism installed to prevent
just that backflow.)

The override mechanism adds a third port—the *pilot*—to the valve.
During normal operation, the pilot port is inactive and the valve behaves as any other
check valve. Its orifice is then open only when the pressure gradient across it drops
from inlet to outlet. Backflow, which requires the reverse pressure gradient, cannot
occur. This mode protects components upstream of the valve against pressure surges,
temperature spikes, and (in real systems) chemical contamination arising from points
downstream.

When backflow is desired, the pilot port is pressurized and the control element of the
valve—often a ball or piston—is forced off its seat. The valve is then open to flow in
both directions, with a reverse pressure drop (aimed from outlet to inlet) sufficing to
drive the flow upstream. (The seat, which lies in the path of the flow, determines if
the valve is open. When it is covered—by a ball, piston, or other control element—the
flow is cut off and the valve is closed.)

The valve opens by degrees, beginning at its cracking pressure, and continuing to the
end of its pressure regulation range. The cracking pressure gives the initial
resistance, due to friction or spring forces, that the valve must overcome to open by a
sliver (or to *crack* open). Below this threshold, the valve is
closed and only leakage flow can pass. Past the end of the pressure regulation range,
the valve is fully open and the flow at a maximum (determined by the instantaneous
pressure conditions).

The cracking pressure assumes an important role in check valves installed upside down.
There, the weight of the opening element—such as a ball or piston—and the elevation head
of the fluid can act to open the valve. (The elevation head can arise in a model from a
pipe upstream of the inlet when it is vertical or given a slant.) A sufficient cracking
pressure keeps the valve from opening inadvertently even if placed at a disadvantageous
angle.

### Control Pressure

The opening of the valve depends both on the pilot pressure and on the pressure
drop from inlet to outlet:

pCtl=kXpX+pA−pB,

where *p* is gauge pressure and
*k* is the pilot ratio—the proportion of the pilot opening area
(*S*X) to the valve opening area
(*S*R). The subscript
`X` denotes a pilot value and the subscripts
`A` and `B` the inlet and outlet values,
respectively. The port pressures are variables determined (against absolute zero)
during simulation.

The pilot pressure can be a differential value relative to the inlet (port
**A**) or a gauge value (relative to the environment). You can
select an appropriate setting—`Pressure difference of port X relative to
port A` or `Pressure at port X`—using the
**Pressure control specification** dropdown list. If you select
`Pressure at port X`,

pX=pX,Abs−pAtm,

where the subscript `Atm` denotes the
atmospheric value (obtained from the Thermal Liquid Settings (TL)
or Thermal Liquid
Properties (TL) block of the model). The subscript
`X,Abs` denotes the absolute value at the pilot port. If you
select `Pressure difference of port X relative to port A`,

pX=pX,Abs−pA,Abs

where the subscript `A,Abs` similarly denotes
the absolute value at the inlet of the valve (port **A**). The
pilot pressure differential is constrained to be greater than or equal to zero—if
its calculated value should be negative, zero is assumed in the control pressure
calculation.

### Control Pressure Overshoot

The degree to which the control pressure exceeds the cracking pressure determines
how much the valve will open. The pressure overshoot is expressed here as a fraction
of the (width of the) pressure regulation range:

p^=pCtl−PCrkPMax−PCrk.

The control pressure, *pCtl*, cracking pressure,
*pCrk*, and maximum opening
pressure, *P*Max, correspond to the control
pressure specification chosen: `Pressure differential` or
`Pressure at port A`.

The fraction—technically, the overshoot *normalized*—is valued
at `0` in the fully closed valve and `1` in the
fully open valve. If the calculation should return a value outside of these bounds,
the nearest of the two is used instead. (In other words, the fraction
*saturates* at `0` and
`1`.)

### Opening Parameterization

The linear parameterization of the valve area is

Avalve=p^(Amax−Aleak)+Aleak,

where the normalized pressure, p^, is

p^=pcontrol−pcrackingpmax−pcracking.

When the valve is in a near-open or near-closed
position in the linear parameterization, you can maintain numerical robustness in
your simulation by adjusting the **Smoothing factor** parameter.
If the **Smoothing factor** parameter is nonzero, the block
smoothly saturates the control pressure between
*pcracking* and
*pmax*. For more information, see
Numerical Smoothing.

### Opening Area

The valve area opens linearly with the smoothed control pressure,

S=(SMax−SMin)p^+SMin,

where *SMax* is the
maximum valve area and *SMin* is the value
of the **Leakage area** parameter.

### Momentum Balance

The causes of those pressure losses incurred in the passages of the valve are
ignored in the block. Whatever their natures—sudden area changes, flow passage
contortions—only their cumulative effect is considered during simulation. This
effect is captured in the block by the discharge coefficient, a measure of the mass
flow rate through the valve relative to the theoretical value that it would have in
an ideal valve. Expressing the momentum balance in the valve in terms of the
pressure drop induced in the flow:

pA−pB=m˙Avgm˙Avg2+m˙Crit22ρAvgCDS\*2[1−(S\*S)2]ξp,

where *ρ* is density,
*C*D is the discharge coefficient, and
*ξ*p is the pressure drop ratio—a
measure of the extent to which the pressure recovery at the outlet contributes to
the total pressure drop of the valve. The subscript Avg denotes an average of the
values at the thermal liquid ports. The critical mass flow rate, m˙Crit, is calculated from the critical Reynolds number—that at which the
flow in the valve is assumed to transition from laminar to turbulent:

m˙Crit=ReCritμAvgπ4S,

where *μ* denotes dynamic viscosity. The
pressure drop ratio is calculated as:

ξp=1−(S\*S)2(1−CD2)−CDS\*S1−(S\*S)2(1−CD2)+CDS\*S.

### Mass Balance

The volume of fluid inside the valve, and therefore the mass of the same, is
assumed to be very small and it is, for modeling purposes, ignored. As a result, no
amount of fluid can accumulate there. By the principle of conservation of mass, the
mass flow rate into the valve through one port must therefore equal that out of the
valve through the other port:

m˙A+m˙B=0,

where m˙ is defined as the mass flow rate *into* the
valve through port **A** or **B**.

### Energy Balance

The valve is modeled as an adiabatic component. No heat exchange can occur between
the fluid and the wall that surrounds it. No work is done on or by the fluid as it
traverses from inlet to outlet. With these assumptions, energy can flow by advection
only, through ports **A** and **B**. By the
principle of conservation of energy, the sum of the port energy flows must then
always equal zero:

ϕA+ϕB=0,

where *ϕ* is defined as the energy flow rate
*into* the valve through one of the ports
(**A** or **B**).
