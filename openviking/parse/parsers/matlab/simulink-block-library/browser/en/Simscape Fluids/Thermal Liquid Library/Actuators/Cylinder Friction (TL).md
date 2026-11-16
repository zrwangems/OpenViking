---
type: simulink-block
title: 'Cylinder Friction (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Actuators'
documentation_page: 'cylinderfrictiontl'
documentation_source_path: 'ref/cylinderfrictiontl.html'
language: en
---

# Cylinder Friction (TL)

## Ports

### Conserving

### **A** — Liquid port thermal liquid

Thermal liquid conserving port associated with the liquid entry or exit point to the
orifice.

### **B** — Liquid port thermal liquid

Thermal liquid conserving port associated with the liquid entry or exit point to the
orifice.

### **C** — Mechanical port velocity mechanical translational

Mechanical translational conserving port associated with the cylinder housing
motion.

### **R** — Mechanical port velocity mechanical translational

Mechanical translational conserving port associated with the cylinder rod motion.

## Parameters

### **Same fluid on both sides** — Option to model same fluid on both sides of block `on` (default) | `off`

Whether to model the same fluid on both sides of the block. If you select
this parameter, the block propagates fluid properties through the block.
Clear this parameter to model each chamber as a different fluid, where each
chamber is connected to an isolated fluid network.

### **Breakaway to Coulomb friction force ratio** — Ratio of breakaway force to Coulomb friction force `1.2` (default) | positive scalar

Ratio of the breakaway force to the Coulomb friction force, RBreak,Coulomb=FbreakFCoulomb.

### **Breakaway friction velocity** — Threshold for motion against friction force `0.1 m/s` (default) | positive scalar

Threshold for the cylinder moving against the friction force.

### **Preload force** — Initial force in cylinder due to seal assembly `20 N` (default) | scalar

Initial force in the cylinder due to the seal assembly. The block uses this parameter to
calculate the Coulomb friction force.

### **Coulomb friction force coefficient** — Coulomb friction force coefficient `1e-6 N/Pa` (default) | positive scalar

Coulomb friction force coefficient. The block uses this parameter to
calculate the Coulomb friction force.

### **Viscous friction coefficient** — Viscous friction coefficient `100 N*s/m` (default) | positive scalar

Viscous friction coefficient. The block uses this parameter to calculate
the viscous friction force.

### **Environment pressure specification** — Pressure reference source `Atmospheric pressure` (default) | `Specified pressure`

Pressure reference to use for the Coulomb friction calculation.

### **Environment pressure** — User-defined pressure reference `0.101325 MPa` (default) | positive scalar

User-defined pressure reference for the Coulomb friction
calculation.

#### Dependencies

To enable this parameter, set **Environment pressure
specification** to `Specified
pressure`.

## Libraries

Simscape / Fluids / Thermal Liquid / Actuators / Auxiliary Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

### R2024a: Model different fluids on each side of the block

Clear the new **Same fluid on both sides** parameter to block
the propagation of fluid properties and model each chamber as a different fluid
connected to its own isolated fluid network.

## Description

Cylinder friction in a thermal liquid network

The Cylinder Friction (TL) block models friction on a moving
cylinder in a thermal liquid network. The total friction is a combination of the
Stribeck, Coulomb, and viscous effects. The Coulomb friction component includes any
initial force applied by the seal and the influence of pressure in the cylinder.

The block calculates the Stribeck and viscous forces using the same approach as the
Simscape Foundational Library Translational Friction block.

### The Coulomb Friction Force

The Coulomb friction force is a force that acts normal to the friction surface.
The cylinder motion creates a radial stress inside the fixed cylinder casing, which
increases as the cylinder compresses the internal fluid. The radial stress is normal
to the cylinder motion, and results in a Coulomb friction force that opposes
cylinder motion.

The Coulomb frictional force is

FCoulomb=Fctanh(υυCoulomb,th),

where *ν* is the relative velocity between ports
**R** and **C**,
*νR* –
*νC*.
*νCoulomb,th* is the threshold
velocity for the Coulomb force,

υCoulomb,th=vbreak10.

The threshold velocity for the Coulomb force is a different
quantity than the threshold velocity for the static force, which the block uses to
calculate the Stribeck friction force, although they both act as a threshold region
to ensure smooth modeling of the Coulomb and Stribeck forces.

*FC* is the force contribution from seal
preloading and the pressure in the cylinder,

FC=Fpreload+fCoulomb(PA+PB),

where:

- *Fpreload* is the value of the
  **Preload force** parameter.
- *fCoulomb* is the value of the
  **Coulomb friction force coefficient** parameter.
- *PA* and
  *PB* are the pressures
  at cylinder ports **A** and **B**,
  respectively. These values are gauge pressures with respect to the
  environmental pressure. You can specify these values either as
  atmospheric or another user-defied value by using the
  **Environment pressure specification**
  parameter.

### The Stribeck Friction and Viscous Friction Forces

The Stribeck friction force, *FStribeck*, is the
dominating friction component at low velocities. The block uses the equation

FStribeck=2e(Rbreak,Coulomb−1)⋅FC(υυstatic,th)e−(υυstatic,th)2,

where:

- *Rbreak,Coulomb* is the value
  of the **Breakaway to Coulomb friction force ratio**
  parameter, RBreak,Coulomb=FbreakFCoulomb.
- *ν* is the velocity of the cylinder, υ=υR−υC.
- *νstatic,th* is the threshold
  velocity for static torque

  υstatic,th=2vbreak,

  where
  *vbreak* is the value of the
  **Breakaway friction velocity** parameter. The
  block establishes a transition range between 0 and the threshold
  velocity for static torque to ensure smooth modeling of the friction
  force.
- *FC* is the force contribution
  from seal preloading and the pressure in the cylinder.

The viscous friction force is based on the value of the **Viscous friction
coefficient** parameter for the working fluid,
*fviscous*, and is proportional to
the cylinder velocity

Fviscous=fviscousυ.
