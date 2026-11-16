---
type: simulink-block
title: 'Poppet Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'poppetvalvetl'
documentation_source_path: 'ref/poppetvalvetl.html'
language: en
---

# Poppet Valve (TL)

## Ports

### Conserving

### **A** — Liquid port thermal liquid

Thermal liquid conserving port associated with valve inlet A.

### **B** — Liquid port thermal liquid

Thermal liquid conserving port associated with valve inlet B.
### Input

### **S** — Poppet displacement, m physical signal

Physical signal port associated with the displacement of the poppet,
in m.

## Parameters

### **Valve seat specification** — Geometry of valve seat `Sharp-edged` (default) | `Conical`

Geometry of the valve seat. The block uses this parameter to calculate the
open area between the poppet and seat.

### **Cone angle** — Angle of seat opening `120` `deg` (default) | positive scalar

Angle of the seat opening.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to
`Conical`.

### **Ball diameter** — Poppet diameter `0.01` `m` (default) | positive scalar

Diameter of the poppet.

### **Orifice diameter** — Seat orifice diameter `7e-3` `m` (default) | positive scalar

Seat orifice diameter.

### **Poppet position when in the seat** — Poppet offset `0` `m` (default) | nonnegative scalar

Poppet offset when valve is shut. A positive, nonzero value indicates a
partially open valve. A negative, nonzero value indicates an overlapped
valve that remains shut for an initial displacement set by the physical
signal at port **S**.

### **Leakage area** — Gap area when in fully closed position `1e-10` `m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully shut position. The block
saturates smaller numbers to this value. This parameter contributes to
numerical stability by maintaining continuity in the flow.

### **Smoothing factor** — Gap area when in fully closed position `0.01` (default) | scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the valve is in the near-open or near-shut positions.
Set this value to a nonzero number less than one to increase the stability
of your simulation in these regimes.

### **Cross-sectional area at ports A and B** — Area at conserving ports `0.01` `m^2` (default) | positive scalar

Area at ports **A** and **B**, which are
used in the pressure-flow rate equation that determines the mass flow rate
through the valve.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.

## Libraries

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Flow Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Poppet flow control valve in a thermal liquid network

The Poppet Valve (TL) block represents the flow control
within a thermal liquid network. You can specify the seat geometry as either sharp-edged
or conical. Set the poppet displacement with the physical signal at port
**S**.

Two poppet valve diagrams. The sharp-edged seat has a 90 degree seat angle. The conical seat has an acute seat angle. Positive displacement is when the poppet moves away from the seat.

### Mass Balance

The mass conservation equation in the valve is

m˙A+m˙B=0,

where:

- m˙A is the mass flow rate into the valve through port
  **A**.
- m˙B is the mass flow rate into the valve through port
  **B**.

### Momentum Balance

The pressure differential over the valve is:

pA−pB=m˙m˙2+m˙cr22ρAvgCd2S2[1−(SRS)2]PRLoss,

where:

- *p*A is the pressure at port
  **A**.
- *p*B is the pressure at port
  **B**.
- m˙ is the mass flow rate.
- *ρ*Avg is the average liquid
  density.
- *C*d is the value of the
  **Discharge coefficient** parameter.
- m˙cr is the critical mass flow rate:

  m˙cr=RecrμAvgπ4SR.

  where:

  - *Recr* is the
    value of the **Critical Reynolds number**
    parameter.
  - *μAvg* is the
    average fluid dynamic viscosity.
- *S* is the value of the **Cross-sectional
  area at port A and B** parameter.
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

### Opening Area With a Sharp-Edged Seat

When you set **Valve seat specification** to
`Sharp-edged`, the block calculates the valve opening
area using

A=πro(1−(rpdOB)2)dOB(h)+Aleak,

where:

- *r*o is the valve orifice
  radius.
- *r*p is the valve poppet
  radius.
- *d*OB(*h*) is the distance between the center of the poppet and
  the edge of the orifice. This distance is a function of the valve
  lift,*h*.
- *Aleak* is the leakage
  area.

The maximum displacement, *h*max, is

hmax=2rp2−ro2+roro2+4rp22−rp2−ro2.

The figure shows a schematic of a hard-edged seat.

Schematic of a hard-edged seat.

### Opening Area With a Conical Seat

When you set **Valve seat specification** to
`Conical`, the block calculates the valve opening area
using a geometric relationship, such that

A=πrpsin(θ)h+π2sin(θ2)sin(θ)h2+Aleak.

The maximum displacement, *h*max, is:

hmax=rp2+ro2cos(θ2)−rpsin(θ2),

where *θ* is the **Cone
angle**. The figure shows a schematic of a conical seat.

Schematic of a conical seat.

### Numerically Smoothed Displacement

The block calculates the poppet displacement, *h*, such that

h={0,(S−Smin)≤0hMax,(S−Smin)≥hMax(S−Smin),Else

where:

- *S* is the physical signal input.
- *Smin* is the **Poppet
  position when in the seat** parameter.
- *hMax* is the maximum
  displacement.

If the **Smoothing factor** parameter is nonzero, the block smoothly
saturates the poppet displacement between `0` and
*hMax*.

For more information, see Numerical Smoothing.
