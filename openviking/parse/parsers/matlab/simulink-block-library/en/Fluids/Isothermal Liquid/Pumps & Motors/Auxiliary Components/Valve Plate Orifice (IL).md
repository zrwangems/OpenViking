---
type: simulink-block
title: 'Valve Plate Orifice (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors / Auxiliary Components'
documentation_page: 'valveplateorificeil'
documentation_source_path: 'ref/valveplateorificeil.html'
language: en
---

# Valve Plate Orifice (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Entry point to the orifice.

### **B** — Liquid port isothermal liquid

Exit point from the orifice.
### Input

### **G** — Cylinder rotation angle, rad physical signal

Cylinder rotation angle in radians, specified as a physical
signal..

## Parameters

### **Cylinder block pitch radius** — Cylinder pitch radius `0.05 m` (default) | positive scalar

Pitch radius of the rotating cylinder.

### **Cylinder orifice diameter** — Diameter of the cylinder slot `2.5e-3 m` (default) | positive scalar

Diameter of the cylinder slot.

### **Pressure carryover angle** — Pressure transition distance `0.06 rad` (default) | scalar

Average angular distance the piston travels during the pressure transition
period from a closed to opening slot.

### **Phase angle** — Initial plate offset angle `0 rad` (default) | scalar

Initial plate offset angle. The total angle between the plate and slot is
the sum of the **Phase angle** and the **Pressure
carryover angle**, *Ψ*.

### **Leakage area** — Gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in a fully closed position. Any area
smaller than this value is maintained at the specified leakage area. This
contributes to numerical stability by maintaining continuity in the
flow.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the valve is in near-open or near-closed positions.
Set this value to a nonzero value less than one to increase the stability of
your simulation in these regimes.

## Libraries

Simscape / Fluids / Isothermal Liquid / Pumps & Motors / Auxiliary Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Variable orifice in an isothermal axial-piston machine

The Valve Plate Orifice (IL) block models a crescent-shaped opening between moving
pistons and a pump in an axial-piston machine. The rotating pistons periodically connect
to the pump intake or discharge through the orifice plate. You can connect two valve
plate blocks to each cylinder of an axial-piston pump to represent both the pump inlet
and outlet slots.

A rotating cylinder, with one crescent slot, is connected to the pump intake at port
**A** and pump discharge at port **B**. These
points are connected to the plate between the **Pressure carryover
angle** and π radians (180 degrees) from each other. The plate rotation angle is set
by the signal at port **G**. The cylinder position angle,
*γ*, is the sum of the position signal, *G*, and
the initial angle offset, the **Phase angle**,
*γ*0:

γ=γ0+G.

*γ* is always between 0 and 2π. For any combined signal and offset
larger than 2π rad, *γ* is maintained at 2π, and for any combined
signal and offset lower than 0 rad, and *γ* is maintained at 0. To
change the initial position of the orifice relative to the slot, you can adjust the
**Phase angle** parameter.

**Axial-Piston Machine With Five Pistons**

The numbers in the diagram indicate the components of an axial-piston machine:

1. Valve plate orifice
2. Rotor
3. Piston
4. Driving shaft
5. Swash plate

### Cylinder Angle

The cylinder rotational alignment with the slot is described by the following angles:

- Cylinder angle at rotation onto slot,
  *γ*1:

  γ1=Ψ−rR
- Cylinder angle at complete rotation onto slot,
  *γ*2:

  γ2=Ψ+rR
- Cylinder angle at rotation beyond slot,
  *γ*3:

  γ3=π−2rR
- Cylinder angle at complete rotation beyond slot,
  *γ*4:

  γ4=π

where:

- *Ψ* is the **Pressure carryover
  angle**. This angle represents the average angular distance
  the piston travels during its pressure transition period from a closed
  to opened slot.
- *r* is the half of the **Cylinder orifice
  diameter**.
- *R* is the **Cylinder block pitch
  radius**.

### Orifice Opening Area

**Orifice area calculations during cylinder motion**

The transition opening area, which is the opening between the cylinder rotation angles
*γ1* and
*γ2*, is calculated as:

Aγ1γ2=Sopening+SLeak=r2(2βopening−sin(2βopening))+SLeak.

The transition closing area, which is the opening between the cylinder rotation angles
*γ3* and
*γ4*, is calculated as:

Aγ3γ4=Sclosing+SLeak=r2(2βclosing−sin(2βclosing))+SLeak,

where the opening and closing parameters are:

βopening=cos−1(Rrsin((ψ+rR)−γ2)),

and

βclosing=cos−1(Rrsin(γ−(π−2rR)2)).

The area between *γ*2 and
*γ*3 is Aγ2γ3=SMax+SLeak, and the area between *γ4*
and *γ1* is Aγ4γ1=SLeak.The maximum opening of the orifice is SMax=πr2.

A nonzero **Smoothing factor** can provide additional numerical stability when the orifice is in near-closed or near-open position.

### Numerically-Smoothed Orifice Angle

At the orifice slot entrance and exit angles, you
can maintain numerical robustness in your simulation by adjusting the block
**Smoothing factor** parameter. If the **Smoothing
factor** parameter is nonzero, the block smoothly saturates the
transition opening angle between *γ1* and
*γ2* and the transition closing
angle between *γ3* and
*γ4*. For more information, see
Numerical Smoothing.

### Mass Flow Rate Equation

The flow through a valve plate orifice is calculated from the pressure-area relationship:

m˙=CdAorifice2ρ¯Δp[Δp2+Δpcrit2]1/4,

where:

- *C*d is the
  **Discharge coefficient**.
- *A*orifice is the area open to
  flow.
- ρ¯ is the average fluid density.
- *Δp* is the pressure drop over the valve,
  *P*A –
  *P*B.

The critical pressure difference,
*Δp*crit, is the pressure differential
associated with the **Critical Reynolds number**,
*Re*crit, which is the point of
transition between laminar and turbulent flow in the fluid:

Δpcrit=πρ¯8Aorifice(νRecritCd)2.
