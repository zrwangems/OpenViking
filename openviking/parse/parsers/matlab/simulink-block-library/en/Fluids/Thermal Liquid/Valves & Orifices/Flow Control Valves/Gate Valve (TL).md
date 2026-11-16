---
type: simulink-block
title: 'Gate Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'gatevalvetl'
documentation_source_path: 'ref/gatevalvetl.html'
language: en
---

# Gate Valve (TL)

## Ports

### Input

### **S** — Gate displacement, m physical signal

Physical signal port associated with the valve gate displacement, in
m. A positive signal retracts the gate and opens the valve.
### Conserving

### **A** — Liquid port thermal liquid

Thermal liquid conserving port associated with valve inlet A.

### **B** — Liquid port thermal liquid

Thermal liquid conserving port associated with valve inlet B.

## Parameters

### **Orifice diameter** — Orifice diameter `0.01` `m` (default) | positive scalar

Valve open-area diameter.

### **Gate position when fully covering orifice** — Gate offset `0` `m` (default) | nonnegative scalar

Gate offset when the valve is closed. A positive, nonzero value indicates
a partially open valve when the signal at port **S** is 0.
A negative, nonzero value indicates an overlapped valve that remains closed
for an initial positive displacement set by the physical signal at port
**S**.

### **Leakage area** — Gap area when in fully shut position `1e-10` `m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully shut position. The block
saturates smaller numbers to this value. This parameter contributes to
numerical stability by maintaining continuity in the flow.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the valve is in near-open or near-closed
positions.

### **Cross-sectional area at ports A and B** — Orifice area at conserving ports `0.01` `m^2` (default) | positive scalar

Areas at the entry and exit ports **A** and
**B**, which are used in the pressure-flow rate
equation that determines the mass flow rate through the orifice.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

## Libraries

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Flow Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Gate valve in a thermal liquid system

The Gate Valve (TL) block represents a gate valve in a
thermal liquid network. The valve comprises a round, sharp-edged orifice and a round
gate with the same diameter. The gate opens or closes according to the displacement
signal at port **S**. A positive signal lifts the gate to open the
valve. The diagram shows the relationship between the opening area and the net
displacement of the gate.

Diagram showing the relationship between the opening area and the net displacement of the gate.

A smoothing function allows the valve opening area to change smoothly between the
fully closed and fully open positions. The smoothing function reduces the abrupt opening
area changes at the zero and maximum gate positions.

### Mass Balance

The mass conservation equation in the valve is

m˙A+m˙B=0,

where:

- m˙A is the mass flow rate into the valve through port
  **A**.
- m˙B is the mass flow rate into the valve through port
  **B**.

### Momentum Balance

The momentum conservation equation in the valve is

pA−pB=m˙m˙2+m˙cr22ρAvgCd2S2[1−(SRS)2]PRLoss,

where:

- *p*A and
  *p*B are the pressures at
  port **A** and port **B**.
- m˙ is the mass flow rate.
- m˙cr is the critical mass flow rate:

  m˙cr=RecrμAvgπ4SR.
- *ρ*Avg is the average liquid
  density.
- *C*d is the discharge
  coefficient.
- *S* is the valve inlet area.
- *PR*Loss is the pressure ratio:

  PRLoss=1−(SR/S)2(1−Cd2)−Cd(SR/S)1−(SR/S)2(1−Cd2)+Cd(SR/S).

### Energy Balance

The energy conservation equation in the valve is

ϕA+ϕB=0,

where:

- *ϕ*A is the energy flow rate
  into the valve through port **A**.
- *ϕ*B is the energy flow rate
  into the valve through port **B**.

### Valve Opening Area

The block computes the valve opening area by using the expression

A=πd024−ACovered+Aleak,

where:

- *A* is the valve opening area.
- *Aleak* is the value of the
  **Leakage area** parameter.
- *d*0 is the valve orifice
  diameter.
- *A*Covered is the portion of
  the valve orifice area covered by the gate:

  ACovered=d022acos(Δld0)−Δl2d02−(Δl)2.
- *Δl* is the net displacement of the gate center
  relative to the orifice center.

  Δl={0,(Sd−Smin)≤0d0,(Sd−Smin)≥d0(Sd−Smin),Else
- *S*min is value of the
  **Gate position when fully covering orifice**
  parameter specified in the block dialog box.
- *S*d is the gate displacement
  specified through physical signal input port S.

### Numerically Smoothed Displacement

When the valve is in a near-open or near-closed position,
you can maintain numerical robustness in your simulation by adjusting the
**Smoothing factor** parameter. If the **Smoothing
factor** parameter is nonzero, the block smoothly saturates the gate
displacement between `0` and the **Valve orifice
diameter** parameter. For more information, see Numerical Smoothing.
