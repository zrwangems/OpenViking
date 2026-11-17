---
type: simulink-block
title: 'Poppet Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'poppetvalveil'
documentation_source_path: 'ref/poppetvalveil.html'
language: en
---

# Poppet Valve (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
- name: B
  summary: Liquid port isothermal liquid
  direction: conserving
- name: S
  summary: Stem displacement, m physical signal
  direction: input
```

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port to the valve.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port to the valve.
### Input

### **S** — Stem displacement, m physical signal

Displacement of the valve control member in m, specified as a physical signal.
## Parameters
```yaml
parameters:
- name: Poppet geometry
  summary: Type of poppet Cylindrical stem (default) | Round ball
  group: ''
- name: Valve seat specification
  summary: Geometry of valve seat Sharp-edged (default) | Conical
  group: ''
- name: Ball diameter
  summary: Diameter of ball control member 0.01 m (default) | positive scalar
  group: ''
- name: Seat orifice diameter
  summary: Seat orifice diameter 7e-3 m (default) | positive scalar
  group: ''
- name: Stem diameter
  summary: Diameter of cylindrical stem 0.01 m (default) | positive scalar
  group: ''
- name: Seat cone angle
  summary: Angle of seat opening 120 deg (default) | positive scalar
  group: ''
- name: Poppet position when in the seat
  summary: Control member offset 0 m (default) | positive scalar
  group: ''
- name: Leakage area
  summary: Gap area when in fully closed position 1e-10 m^2 (default) | positive scalar
  group: ''
- name: Cross-sectional area at ports A and B
  summary: Area at conserving ports inf m^2 (default) | positive scalar
  group: ''
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: ''
- name: Critical Reynolds number
  summary: Upper Reynolds number limit for laminar flow 150 (default) | positive scalar
  group: ''
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range [0,1]
  group: ''
- name: Pressure recovery
  summary: Whether to account for pressure increase in area expansions off (default) | on
  group: ''
```

### **Poppet geometry** — Type of poppet `Cylindrical stem` (default) | `Round ball`

Type of poppet. You can choose either a cylindrical or ball-shaped control
member.

### **Valve seat specification** — Geometry of valve seat `Sharp-edged` (default) | `Conical`

Geometry of valve seat. The block uses this parameter to calculate the
open area between the poppet and seat.

#### Dependencies

To enable this parameter, set **Poppet geometry** to
`Round ball`.

### **Ball diameter** — Diameter of ball control member `0.01 m` (default) | positive scalar

Diameter of the ball control member.

#### Dependencies

To enable this parameter, set **Poppet geometry** to
`Round ball`.

### **Seat orifice diameter** — Seat orifice diameter `7e-3 m` (default) | positive scalar

Seat orifice diameter.

#### Dependencies

To enable this parameter, set **Poppet geometry** to
`Round ball`.

### **Stem diameter** — Diameter of cylindrical stem `0.01 m` (default) | positive scalar

Diameter of the cylindrical stem.

#### Dependencies

To enable this parameter, set **Poppet geometry** to
`Cylindrical stem`.

### **Seat cone angle** — Angle of seat opening `120 deg` (default) | positive scalar

Angle of the seat opening.

#### Dependencies

To enable this parameter, set either:

- **Poppet geometry** to
  `Cylindrical stem`
- **Poppet geometry** to `Round
  ball` and **Valve seat
  specification** to
  `Conical`

### **Poppet position when in the seat** — Control member offset `0 m` (default) | positive scalar

Poppet offset when valve is closed. A positive, nonzero value indicates a
partially open valve. A negative, nonzero value indicates an overlapped
valve that remains closed for an initial displacement set by the physical
signal at port **S**.

### **Leakage area** — Gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any area
smaller than this value is saturated to the specified leakage area. This
contributes to numerical stability by maintaining continuity in the
flow.

### **Cross-sectional area at ports A and B** — Area at conserving ports `inf` `m^2` (default) | positive scalar

Areas at the entry and exit ports **A** and
**B**, which are used in the pressure-flow rate
equation that determines the mass flow rate through the valve.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
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

Poppet valve in an isothermal liquid network

The Poppet Valve (IL) block represents a flow-control valve
in an isothermal liquid system. The poppet can either be a cylinder or a ball. You can
choose between sharp-edged and conical seats. The poppet opens or closes according to
the displacement signal at port **S**. A positive signal retracts the
poppet and opens the valve.

**Poppet Valve Schematic**

Side-view schematic explaining the relationship between the seat, the poppet, and the open area. The seat is a V-shape. The poppet is rectangular. The open area is the orange trapezoid depicting where flow occurs.

**Poppet Valve Top View**

Top-view schematic explaining the relationship between the seat, the poppet, and the open area. The seat is the outside ring. The poppet is the filled-in inner circle. The open area is the ring between the poppet and the seat.

### Cylindrical Stem Poppet Opening Area

The opening area of the valve is calculated as:

Aopen=πhsin(θ2)[ds+h2sin(θ)]+Aleak,

where:

- *h* is the vertical distance between the outer edge
  of the cylinder and the seat, indicated in the schematic above.
- *θ* is the **Seat cone
  angle**.
- *d*s is the **Stem
  diameter**.
- *A*leak is the
  **Leakage area**.

The opening area is bounded by the maximum displacement
*h*max:

hmax=ds[1+cos(θ2)−1]sin(θ).

For any stem displacement larger than
*h*max,
*A*open is the sum of the maximum
orifice area and the **Leakage area**:

Aopen=π4ds2+Aleak.

For any combination of the signal at port **S**
and the cylinder offset less than 0, the minimum valve area is the **Leakage
area**.

### Round Ball Poppet Opening Area

**Sharp-edged Seat Geometry**

The opening area of the valve is calculated as:

Aopen,sharp−edged=πrO(Gsharp+h)2+rO2[1−rB2(Gsharp+h)2+rO2]+Aleak,

where:

- *h* is the vertical distance between the outer
  edge of the cylinder and the seat, indicated in the schematic
  above.
- *r*O is the seat orifice
  radius, calculated from the **Seat orifice
  diameter**.
- *r*B is the radius of the
  ball, calculated from the **Ball diameter**.
- *G*sharp is the geometric
  parameter: Gsharp=rB2−rO2.
- *A*leak is the
  **Leakage area**.

The opening area is bounded by the maximum displacement
*h*max:

hmax=2rB2−rO2+rOrO2+4rB22−Gsharp.

For any ball displacement larger than
*h*max,
*A*open is the sum of the maximum
orifice area and the **Leakage area**:

Aopen=π4dO2+Aleak.

For any combination of the signal at port
**S** and the ball offset that is less than 0, the minimum
valve area is the **Leakage area**.

**Conical Seat Geometry**

The opening area of the valve is calculated as:

Aopen,conical=Gconicalh+π2sin(θ)sin(θ2)h2+Aleak,

where:

- *h* is the vertical distance between the outer
  edge of the cylinder and the seat, indicated in the schematic
  above.
- *θ* is the **Seat cone
  angle**.
- *G*conical is the
  geometric parameter: Gconical=πrBsin(θ), where *r*B
  is the ball radius.
- *A*leak is the
  **Leakage area**.

The opening area is bounded by the maximum displacement
*h*max:

hmax=rB2+rO2cos(θ2)−rBsin(θ2).

For any ball displacement larger than
*h*max,
*A*open is the sum of the maximum
orifice area and the **Leakage area**:

Aopen=π4dO2+Aleak.

For any combination of the signal at port
**S** and the ball offset that is less than 0, the minimum
valve area is the **Leakage area**.

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

### Mass Flow Rate Equation

Mass is conserved through the valve:

m˙A+m˙B=0.

The mass flow rate through the valve is calculated as:

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *C*d is the
  **Discharge coefficient**.
- *A*valve is the current valve
  open area.
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
