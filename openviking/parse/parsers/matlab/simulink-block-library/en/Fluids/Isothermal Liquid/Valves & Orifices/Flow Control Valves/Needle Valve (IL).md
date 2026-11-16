---
type: simulink-block
title: 'Needle Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'needlevalveil'
documentation_source_path: 'ref/needlevalveil.html'
language: en
---

# Needle Valve (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port to the valve.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port to the valve.
### Input

### **S** — Needle displacement, m physical signal

Control member displacement in m, specified as a physical signal. A
positive signal retracts the needle and opens the valve.

## Parameters

### **Seat orifice diameter** — Diameter of seat `5e-3 m` (default) | positive scalar

Diameter of the seat orifice.

### **Needle cone angle** — Control member geometry angle `90 deg` (default) | positive scalar

Control member geometry angle. Refer to the Needle Valve Schematic in the
valve description.

### **Needle position when in the seat** — Needle offset `0 m` (default) | scalar

Needle offset when the valve is closed. A positive, nonzero value
indicates a partially open valve. A negative, nonzero value indicates an
overlapped valve that remains closed for an initial displacement set by the
physical signal at port **S**.

### **Leakage area** — Gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any area
smaller than this value is saturated to the specified leakage area. This
contributes to numerical stability by maintaining continuity in the
flow.

### **Cross-sectional area at ports A and B** — Area at conserving ports `inf m^2` (default) | positive scalar

Areas at the entry and exit ports **A** and
**B**, which are used in the pressure-flow rate
equation that determines the mass flow rate through the valve.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor accounting for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to the flow response
when the valve is in near-open or near-closed positions. Set this value to a
nonzero value less than one to increase the stability of your simulation in
these regimes.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether to account for pressure increase when fluid flows from a region of
smaller cross-sectional area to a region of larger cross-sectional
area.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Needle valve in an isothermal liquid system

The Needle Valve (IL) block models flow reductions by a needle valve. The valve
comprises a conical needle and a round, sharp-edged seat. The needle opens or closes
according to the displacement signal at port **S**. A positive signal
retracts the needle and opens the valve.

### Opening Area

**Needle Valve Schematic**

**Needle Valve Top View**

The opening area of the valve is calculated as:

Aopen=πhsin(θ2)[d0−h2sin(θ)]+Aleak,

where:

- *h* is the vertical distance between the outer edge
  of the needle and the seat, as indicated in the schematic above.
- *θ* is the seat cone angle, which always matches the
  **Needle cone angle**.
- *d*0 is the **Seat
  orifice diameter**.
- *A*leak is the
  **Leakage area**.

The opening area is bounded by the maximum displacement
*h*max:

hmax=d0[1−1−cos(θ2)]sin(θ).

For any needle displacement larger than
*hmax*,
*A*open is the sum of the maximum
orifice area and the **Leakage area**:

Aopen=π4d02+Aleak.

For any combination of the signal at port **S**
and the needle offset that is less than 0, the minimum valve area is the
**Leakage area**.

If the **Smoothing factor** parameter is nonzero, the block smoothly
saturates the displacement between `0` and
*hmax*. For more information, see
Numerical Smoothing.

### Mass Flow Rate Equation

Mass is conserved through the valve:

m˙A+m˙B=0.

The mass flow rate through the valve is calculated as:

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *C*d is the
  **Discharge coefficient**.
- *A*valve is the instantaneous
  valve open area.
- *A*port is the
  **Cross-sectional area at ports A and B**.
- ρ¯ is the average fluid density.
- *Δp* is the valve pressure difference
  *p*A –
  *p*B.

The critical pressure difference,
*Δp*crit, is the pressure differential
associated with the **Critical Reynolds number**,
*Re*crit, the flow regime transition
point between laminar and turbulent flow:

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*Pressure loss* describes the reduction of pressure in the
valve due to a decrease in area. *PR*loss is
calculated as:

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*Pressure recovery* describes the positive pressure change in the valve
due to an increase in area. If you do not want to capture this increase in pressure,
clear the **Pressure recovery** check box. In this case,
*PR*loss is 1.
