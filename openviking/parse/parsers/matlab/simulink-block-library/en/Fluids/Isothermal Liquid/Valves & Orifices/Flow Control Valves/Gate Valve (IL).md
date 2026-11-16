---
type: simulink-block
title: 'Gate Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'gatevalveil'
documentation_source_path: 'ref/gatevalveil.html'
language: en
---

# Gate Valve (IL)

## Ports

### Input

### **S** — Gate displacement, m physical signal

Physical signal port associated with the valve gate displacement, in
m. A positive signal retracts the gate and opens the valve.
### Conserving

### **A** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with valve inlet A.

### **B** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with valve inlet
B.

## Parameters

### **Valve orifice diameter** — Orifice diameter `5e-3` `m^2` (default) | positive scalar

Valve open-area diameter.

### **Gate position when fully covering orifice** — Gate offset `0` `m` (default) | positive scalar

Gate offset when the valve is closed. A positive, nonzero value indicates
a partially open valve when the signal at port **S** is 0.
A negative, nonzero value indicates an overlapped valve that remains closed
for an initial positive displacement set by the physical signal at port
**S**.

### **Leakage area** — Gap area when in fully closed position `1e-10` `m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any area
smaller than this value is saturated to the specified leakage area. This
contributes to numerical stability by maintaining continuity in the
flow.

### **Cross-sectional area at ports A and B** — Orifice area at conserving ports `inf` `m^2` (default) | positive scalar

Areas at the entry and exit ports **A** and
**B**, which are used in the pressure-flow rate
equation that determines the mass flow rate through the orifice.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor accounting for discharge losses in theoretical flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to the flow response
when the valve is in near-open or near-closed positions.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether to account for pressure increase when fluid flows from a region of smaller
cross-sectional area to a region of larger cross-sectional area.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Gate valve in an isothermal liquid system

The Gate Valve (IL) block represents flow control by a gate
valve in an isothermal liquid network. The valve comprises a round, sharp-edged orifice
and a round gate with the same diameter. The gate opens or closes according to the
displacement signal at port **S**. A positive signal retracts the gate
and opens the valve.

### Opening Area

**Gate Valve Opening Schematic**

The area open to flow as the gate retracts is:

Aopen=πd024−Ashielded,

where *d*0 is the
**Valve orifice diameter**. The area shielded by the gate in a
partially open valve is:

Ashielded=d022cos−1(Δld0)−Δl2d02−(Δl)2,

where *Δl* is the gate displacement, which is
the sum of the signal at port **S** and the **Gate position
when fully covering orifice**.

If displacement exceeds the **Orifice diameter**, the valve area
*A*open is the sum of the maximum
orifice area and the **Leakage area**:

Aopen=π4d02+Aleak.

For any combination of the signal at port **S**
and the gate offset that is less than 0, the minimum valve area is the
**Leakage area**.

### Numerically Smoothed Displacement

When the valve is in a near-open or near-closed position,
you can maintain numerical robustness in your simulation by adjusting the
**Smoothing factor** parameter. If the **Smoothing
factor** parameter is nonzero, the block smoothly saturates the gate
displacement between `0` and the **Valve orifice
diameter** parameter. For more information, see Numerical Smoothing.

### Mass Flow Rate Equation

Mass is conserved through the valve:

m˙A+m˙B=0.

The mass flow rate through the valve is calculated as:

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *C*d is the
  **Discharge coefficient**.
- *A*valve is the valve open
  area.
- *A*port is the
  **Cross-sectional area at ports A and B**.
- ρ¯ is the average fluid density.
- *Δp* is the valve pressure difference
  *p*A –
  *p*B.

The critical pressure difference,
*Δp*crit, is the pressure differential
associated with the **Critical Reynolds number**,
*Re*crit, which is the flow regime
transition point between laminar and turbulent flow:

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*Pressure loss* describes the reduction of pressure in the
valve due to a decrease in area. *PR*loss is
calculated as:

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*Pressure recovery* describes the positive pressure change in the valve
due to an increase in area. If you do not want to capture this increase in pressure,
clear the **Pressure recovery** check box. In this case,
*PR*loss is 1.
