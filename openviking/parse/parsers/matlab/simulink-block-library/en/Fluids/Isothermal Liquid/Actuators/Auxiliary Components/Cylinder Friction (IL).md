---
type: simulink-block
title: 'Cylinder Friction (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators / Auxiliary Components'
documentation_page: 'cylinderfrictionil'
documentation_source_path: 'ref/cylinderfrictionil.html'
language: en
---

# Cylinder Friction (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
- name: B
  summary: Liquid port isothermal liquid
  direction: conserving
- name: C
  summary: Mechanical port velocity mechanical translational
  direction: conserving
- name: R
  summary: Mechanical port velocity mechanical translational
  direction: conserving
```

### Conserving

### **A** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the liquid entry or
exit point to the orifice.

### **B** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the liquid entry or
exit point to the orifice.

### **C** — Mechanical port velocity mechanical translational

Mechanical translational conserving port associated with the cylinder
housing motion.

### **R** — Mechanical port velocity mechanical translational

Mechanical translational conserving port associated with the cylinder
rod motion.
## Parameters
```yaml
parameters:
- name: Same fluid on both sides
  summary: Option to model same fluid on both sides of block on (default) | off
  group: ''
- name: Breakaway to Coulomb friction force ratio
  summary: Ratio of breakaway force to Coulomb friction force 1.2 (default) | positive scalar
  group: ''
- name: Breakaway friction velocity
  summary: Threshold for motion against friction force 0.1 m/s (default) | positive scalar
  group: ''
- name: Preload force
  summary: Initial force in cylinder due to seal assembly 20 N (default) | scalar
  group: ''
- name: Coulomb friction force coefficient
  summary: Coulomb friction force coefficient 1e-6 N/Pa (default) | positive scalar
  group: ''
- name: Viscous friction coefficient
  summary: Viscous friction coefficient 100 N*s/m (default) | positive scalar
  group: ''
- name: Environment pressure specification
  summary: Pressure reference source Atmospheric pressure (default) | Specified pressure
  group: ''
- name: Environment pressure
  summary: User-defined pressure reference 0.101325 MPa (default) | positive scalar
  group: ''
```

### **Same fluid on both sides** — Option to model same fluid on both sides of block `on` (default) | `off`

Whether to model the same fluid on both sides of the block. If you select
this parameter, the block propagates fluid properties through the block.
Clear this parameter to model each chamber as a different fluid, where each
chamber is connected to an isolated fluid network.

### **Breakaway to Coulomb friction force ratio** — Ratio of breakaway force to Coulomb friction force `1.2` (default) | positive scalar

Ratio of the breakaway force to the Coulomb friction force, RBreak,Coulomb=FbreakFCoulomb.

### **Breakaway friction velocity** — Threshold for motion against friction force `0.1 m/s` (default) | positive scalar

Threshold for movement against friction force.

### **Preload force** — Initial force in cylinder due to seal assembly `20 N` (default) | scalar

Initial force in the cylinder due to the seal assembly. The block uses this parameter to
calculate the Coulomb friction force.

### **Coulomb friction force coefficient** — Coulomb friction force coefficient `1e-6 N/Pa` (default) | positive scalar

Coulomb friction force coefficient. The block uses this parameter to calculate the
Coulomb friction force.

### **Viscous friction coefficient** — Viscous friction coefficient `100 N*s/m` (default) | positive scalar

Viscous friction coefficient. This parameter is used to calculate the
viscous friction force.

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

Simscape / Fluids / Isothermal Liquid / Actuators / Auxiliary Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2024a: Model different fluids on each side of the block

Clear the new **Same fluid on both sides** parameter to block
the propagation of fluid properties and model each chamber as a different fluid
connected to its own isolated fluid network.

## Description

Adds friction to cylinders with moving components

The Cylinder Friction (IL) block models friction on a moving cylinder in an isothermal
liquid network. The total friction is a combination of the Stribeck, Coulomb, and
viscous effects. The Coulomb friction component includes any initial force applied by
the seal and the influence of pressure in the cylinder.

The Stribeck and viscous forces are calculated in the same way as for the Simscape
Foundational Library Translational Friction block.

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

The Stribeck friction force, *FStribeck*,
is the dominating friction component at low velocities. The block uses the equation

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
