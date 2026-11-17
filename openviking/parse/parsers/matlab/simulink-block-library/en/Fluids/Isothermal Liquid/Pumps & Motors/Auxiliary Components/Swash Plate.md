---
type: simulink-block
title: 'Swash Plate'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors / Auxiliary Components'
documentation_page: 'swashplate'
documentation_source_path: 'ref/swashplate.html'
language: en
---

# Swash Plate

## Ports
```yaml
ports:
- name: A
  summary: Mechanical port associated with actuator mechanical translational
  direction: conserving
- name: P
  summary: Mechanical port associated with piston mechanical translational
  direction: conserving
- name: S
  summary: Mechanical port associated with shaft mechanical rotational
  direction: conserving
```

### Conserving

### **A** — Mechanical port associated with actuator mechanical translational

Swash plate actuator velocity and force.

### **P** — Mechanical port associated with piston mechanical translational

Piston end velocity and force.

### **S** — Mechanical port associated with shaft mechanical rotational

Drive shaft angular velocity and torque. Rotation is relative to the
environment.
## Parameters
```yaml
parameters:
- name: Swash plate actuator arm
  summary: Length of actuator extension 0.065 m (default) | positive scalar
  group: ''
- name: Cylinder block pitch radius
  summary: Cylinder pitch radius 0.05 m (default) | positive scalar
  group: ''
- name: Piston offset from the plate
  summary: Resting piston offset 0 m (default) | scalar
  group: ''
- name: Viscous friction coefficient
  summary: Torque viscous friction coefficient 50 N/(m/s) (default) | positive scalar
  group: ''
```

### **Swash plate actuator arm** — Length of actuator extension `0.065 m` (default) | positive scalar

Length of fully extended actuator arm.

### **Cylinder block pitch radius** — Cylinder pitch radius `0.05 m` (default) | positive scalar

Pitch radius of the rotating cylinder.

### **Piston offset from the plate** — Resting piston offset `0 m` (default) | scalar

Piston offset when the actuator is in neutral position. A positive,
nonzero value indicates a partially retracted piston. A negative, nonzero
value indicates an extended piston that remains within the cylinder block
during an initial actuator displacement away from the cylinder.

### **Viscous friction coefficient** — Torque viscous friction coefficient `50 N/(m/s)` (default) | positive scalar

Coefficient used in the equation for torque due to viscous
friction.
## Libraries

Simscape / Fluids / Isothermal Liquid / Pumps & Motors / Auxiliary Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Swash plate in a single-piston, isothermal axial piston pump

The Swash Plate block models a single, piston-actuated swash plate within an
axial-piston pump. It translates linear actuation into rotational motion that, when
connected to the Valve Plate Orifice (IL) block, periodically connects the piston with
the pump intake and discharge. You can connect multiple swash plate blocks to multiple
pistons.

**Schematic of a Swash Plate Within an Axial-Piston Pump Unit**

### Force Balance

The plate is in dynamic equilibrium if the net work by the piston, actuator, and
plate is zero:

FPδP+FAδA+(τ−τres)δy=0,

where:

- *F*P*δ*P
  is the work done due to piston displacement.
- *F*A*δ*A
  is the work done due to actuator displacement.
- *(τ-τ*res*)δ*y
  is the work done due to the net plate torque tangent to plate
  motion.

The plate torque is:

τ=−rPrAxAFPsinγ+τres,

where:

- *r*P is the **Cylinder
  block pitch radius**.
- *r*A is the **Swash
  plate actuator arm**.
- *X*A is the actuator
  displacement.
- *F*P is the piston
  force.
- *γ* is the plate angular displacement.

The viscous friction torque, or the resistance to motion due to plate-piston
contact, is:

τres=μviscousωrP2,

where:

- *μ*viscous is the
  **Viscous friction coefficient**.
- *ω* is the rotor angular velocity.

### Piston Dynamics

The piston displacement, *x*, is proportional to the actuator
displacement:

x=−hoff(1+xA2rA2−1)−rPrAxAcosγ,

where *h*off is the **Piston
offset from the plate**. Displacement is positive if it moves toward
the cylinder block.

The piston velocity is:

VP=rPrAxAωsin(γ)−rPrAVAcosγ−hoffrA2xAVA1+xA2rA2,

where *V*A is the
actuator velocity.

### Assumptions and Limitations

This block accounts for the effect of viscous friction between the piston and
plate, but neglects plate and fluid inertia.
