---
type: simulink-block
title: 'Spool Orifice Flow Force (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces'
documentation_page: 'spoolorificeflowforceil'
documentation_source_path: 'ref/spoolorificeflowforceil.html'
language: en
---

# Spool Orifice Flow Force (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port to the block.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port to the block.
### Input

### **S** — Control member displacement, m physical signal

Spool displacement in m, specified as a physical signal.
### Output

### **F** — Flow force, N physical signal

Axial flow force in N, specified as a physical signal.

## Parameters

### **Orifice geometry** — Type of orifice `Round holes` (default) | `Rectangular slot`

Whether the modeled spool has round holes or a rectangular slot in the
sleeve.

### **Diameter of round holes** — Diameter of round holes `5e-3 m` (default) | positive scalar

Diameter of all holes on the sleeve.

#### Dependencies

To enable this parameter, set **Orifice geometry** to
`Round holes`.

### **Number of round holes** — Number of round holes `6` (default) | positive integer

Number of holes along the sleeve circumference.

#### Dependencies

To enable this parameter, set **Orifice geometry** to
`Round holes`.

### **Orifice width** — Rectangular slot width `0.01 m` (default) | positive scalar

Rectangular slot width.

#### Dependencies

To enable this parameter, set **Orifice geometry** to
`Rectangular slot`.

### **Spool travel between closed and open orifice** — Maximum spool stroke `1 m` (default) | positive scalar

Maximum orifice opening, including the **Spool position at maximum
orifice area**.

#### Dependencies

To enable this parameter, set **Orifice geometry** to
`Rectangular slot`.

### **Radial clearance** — Spool-sleeve clearance `1e-5 m` (default) | positive scalar

Radial distance between the spool and the sleeve.

### **Spool position at closed orifice** — Initial spool offset `0 m` (default) | scalar

Initial offset if the spool is extended or retracted in its neutral
position.

### **Opening orientation** — Direction of changing orifice area `Positive spool displacement opens orifice` (default) | `Negative spool displacement closes orifice`

Direction of member movement that opens the orifice. A positive
orientation indicates that positive control member displacement increases
the orifice opening. A negative orientation indicates that negative control
member displacement increases the orifice opening. The magnitude is always
positive.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the valve is in near-open or near-closed positions.
Set this value to a nonzero value less than one to increase the stability of
your simulation in these regimes.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Axial fluid force on spool orifice in an isothermal liquid system

The Spool Orifice Flow Force (IL) block models the hydraulic axial force on a spool orifice.
It receives the spool position as a physical signal at port **S**. You
can also model the flow through a spool orifice with round or rectangular holes. A
positive force acts to close the orifice.

If you would like to model the spool and axial force in one block, use the Spool Orifice (IL) block. The axial
force is output as a physical signal at port **F**.

### Flow Force

The force on the spool is calculated as:

F=−m˙A2ρAcos(α)ε,

where:

- m˙A is the mass flow rate at port
  **A**.
- *ρ* is the fluid density.
- *A* is the orifice open area, which is determined by
  the spool position and orifice parameterization.
- *α* is the jet angle, which is calculated from an approximation of the
  von Mises formula:

  αjet=0.3663+0.8373(1−e−h1.848c),

  where *c* is the **Radial
  clearance** and *h* is the orifice
  opening.
- *ε* is the opening orientation, which indicates
  orifice opening that is associated with a positive or negative signal at
  **S**.

### Opening Area

The orifice opening is based on the open area created by the displaced spool:

ΔS=(S−Smin)ε,

where:

- *S*min is the **Spool
  position at closed orifice**.
- *S* is the displacement signal at port
  **S**.

If *Δs* falls below 0, the orifice leakage area is
used. If *ΔS* is greater than the **Spool travel between
closed and open orifice**, the maximum orifice area is used.

**Round Holes**

Setting **Orifice geometry** to `Round
holes` evenly distributes a user-defined number of holes along
the sleeve perimeter that have equal diameters and centers aligned in the same
plane.

The open area is

Aorifice=n0d028(θ−sin(θ2))+Aleak,

where:

- *n*0 is the number of
  holes.
- *d*0 is the diameter of
  the holes.
- *θ* is the orifice opening angle:

  θ=2cos−1(1−2ΔSd0).

  If *θ* is greater than
  *2π*, *θ* remains at
  *2π*.
- *A*leak is the
  **Leakage area**.

The open area expression is based on a geometric derivation and
calculates the area of each hole as a planar circle. If the sleeve is
cylindrical, the holes are not planar and this expression is an
approximation.

The maximum open area is:

Amax=π4d02n0+Aleak.

**Rectangular Slot**

Setting **Orifice geometry** to `Rectangular
slot` models one rectangular slot in the tube sleeve.

For an orifice with a slot in a rectangular sleeve, the open area is

Aorifice=wΔS+Aleak,

where *w* is the orifice width.

The maximum opening distance between the sleeve and case is:

Amax=wΔSmax+Aleak.

where *ΔS*max is the
**Spool travel between closed and open orifice**.

### Numerically-Smoothed Displacement

At the extremes of the orifice opening range, you can maintain numerical
robustness in your simulation by adjusting the block **Smoothing
factor**. The block applies a smoothing function to every calculated
displacement, but primarily influences the simulation at the extremes of this
range.

If the **Smoothing factor**
parameter is nonzero, the block smoothly saturates the orifice opening between
`0` and *ΔSmax* where
*ΔSmax* is the:

- Value of the **Diameter of round holes** parameter,
  when **Orifice parameterization** is set to
  `Round holes`.
- Value of the **Spool travel between closed and open
  orifice** parameter, when **Orifice
  parameterization** is set to `Rectangular
  slot`.

For more information, see Numerical Smoothing.

### Assumptions and Limitations

- The transient effects are negligible.
- The jet angle approximation is based on the Richard von Mises
  equation.
- The jet angle variation with the orifice opening is identical for the
  rectangular slot and the round holes orifices.
