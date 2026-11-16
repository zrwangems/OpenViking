---
type: simulink-block
title: 'Shuttle Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Directional Control Valves'
documentation_page: 'shuttlevalveil'
documentation_source_path: 'ref/shuttlevalveil.html'
language: en
---

# Shuttle Valve (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Entry port to the valve.

### **A1** — Liquid port isothermal liquid

Entry port to the valve.

### **B** — Liquid port isothermal liquid

Exit port from the valve.

## Parameters

### **Pressure at which A-B is fully closed and A1-B is fully open** — Threshold pressure for fully open inlet A1 `-0.01 MPa` (default) | scalar

Pressure threshold between ports **A** and
**A1**, below which the flow path between ports
**A1** and **B** is fully open and the
flow path between ports **A** and **B** is
fully closed.

### **Pressure at which A-B is fully open and A1-B is fully closed** — Threshold pressure for fully open inlet A `0.01 MPa` (default) | scalar

Pressure threshold between ports **A** and
**A1**, above which the flow path between ports
**A** and **B** is fully open and the
flow path between ports **A1** and **B**
is fully closed.

### **Maximum opening area** — Maximum valve area `1e-4 m^2` (default) | positive scalar

Maximum open area of the valve. This value is used to determine the
normalized valve pressure and the valve opening area during
operation.

### **Leakage area** — Gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any area
smaller than this value is saturated to the specified leakage area. This
contributes to numerical stability by maintaining continuity in the
flow.

### **Cross-sectional area at ports A and B** — Area at conserving ports `inf m^2` (default) | positive scalar

Areas at the entry and exit ports **A**,
**A1**, and **B**, which are used in
the pressure-flow rate equation that determines the mass flow rate through
the valve.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor accounting for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the valve is in near-open or near-closed positions.
Set this value to a nonzero value less than one to increase the stability of
your simulation in these regimes.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `Off` (default) | `On`

Whether to account for pressure increase when fluid flows from a region of
smaller cross-sectional area to a region of larger cross-sectional
area.

### **Opening dynamics** — Whether to introduce flow lag due to valve opening `Off` (default) | `On`

Whether to account for transient effects to the fluid system due to
opening the valve. Setting **Opening dynamics** to
`On` approximates the opening conditions by introducing
a first-order lag in the flow response. The **Opening time
constant** also impacts the modeled opening dynamics.

### **Opening time constant** — Valve opening time constant `0.1 s` (default) | positive scalar

Constant that captures the time required for the fluid to reach
steady-state conditions when opening or closing the valve from one position
to another. This parameter impacts the modeled opening dynamics.

#### Dependencies

To enable this parameter, set **Opening dynamics** to
`On`.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

One-way switching valve in an isothermal liquid system

The Shuttle Valve (IL) block models a one-way pressure control valve or switching
component in an isothermal liquid network. Flow through the valve travels from port
**A** or port **A1** to port
**B**. When the pressure differential between
**A** and **A1**,
*p*AA1, is above a specified threshold
pressure, the path between ports **A** and **B** is
open to flow and the port at **A1** closes. The path has been fully
changed when the pressure reaches the **Pressure at which A-B is fully open and
A1-B is fully closed**. When *p*AA1
falls below the threshold pressure, the flow inlet switches to port
**A1**.

### Mass Flow Rate Equation

Mass is conserved through the valve:

m˙A+m˙A1+m˙B=0.

There is no flow between ports **A** and
**A1**.

The mass flow rate through the valve is calculated as:

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *C*d is the
  **Discharge coefficient**.
- *A*valve is the valve open
  area, either between ports **A** and
  **B** or ports **A1** and
  **B**.
- *A*port is the
  **Cross-sectional area at ports A and B**.
- ρ¯ is the average fluid density.
- *Δp* is the valve pressure difference. Depending on
  the flow path through the valve, this is either
  *p*A –
  *p*B,
  *p*A1 –
  *p*B, or the normalized
  pressure when switching between the two inlet ports, p^, defined below.

The critical pressure difference,
*Δp*crit, is the pressure differential
associated with the **Critical Reynolds number**,
*Re*crit, and is also dependent on the
flow path through the valve:

Δpcrit=πρ¯8Avalve(νRecritCd)2.

The critical Reynolds number is the flow regime transition point
between laminar and turbulent flow.

*Pressure loss* describes the reduction of pressure in the
valve due to a decrease in area, and can change if different valve flow paths have
different areas. *PR*loss is calculated as:

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*Pressure recovery* describes the positive pressure change in the valve
due to an increase in area. If you do not want to capture this increase in pressure,
set the **Pressure recovery** to `Off`. In
this case, *PR*loss is 1.

The opening area, *A*valve, is also
impacted by the valve opening dynamics.

### Opening Parameterization

The linear parameterization of the valve area depends on the flow path through the
valve. The dynamic area is based on a normally open path between ports
**A** and **B**:

Avalve,AB=p^(Amax−Aleak)+Aleak.

The normalized pressure, p^, is

p^=pAA1−popen,A1Bpopen,AB−popen,A1B,

when *p*AA1 is between
the parameters **Pressure at which A-B is fully closed and A1-B is fully
open** and **Pressure at which A-B is fully open and A1-B is
fully closed**. If *p*AA1 is
below **Pressure at which A-B is fully closed and A1-B is fully
open**, p^ is 0. If *p*AA1 is above
**Pressure at which A-B is fully open and A1-B is fully
closed**, p^ is 1.

When the valve inlet switches from port **A** to port
**A1**, the valve opening area is:

Avalve,A1B=Amax+Aleak−Avalve,AB.

When the valve is in a near-open or near-closed position
in the linear parameterization, you can maintain numerical robustness in your
simulation by adjusting the **Smoothing factor** parameter. If
the **Smoothing factor** parameter is nonzero, the block smoothly
saturates the normalized control pressure between `0` and
`1`. For more information, see Numerical Smoothing.

### Opening Dynamics

If opening dynamics are modeled, a lag is introduced to the flow response to the
modeled control pressure. *p*control becomes
the dynamic control pressure, *p*dyn;
otherwise, *p*control is the steady-state
pressure. The instantaneous change in dynamic control pressure is calculated based
on the **Opening time constant**, *τ*:

p˙dyn,AB=pcontrol−pdyn,ABτ.

By default, **Opening dynamics** is set to
`Off`.
