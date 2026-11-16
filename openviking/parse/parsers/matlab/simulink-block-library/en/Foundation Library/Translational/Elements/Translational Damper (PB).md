---
type: simulink-block
title: 'Translational Damper (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationaldamperpb'
documentation_source_path: 'ref/translationaldamperpb.html'
language: en
---

# Translational Damper (PB)

## Ports

### Conserving

### **B** — Base port position-based mechanical translational

Position-based mechanical translational conserving port that represents the base
connection.

### **F** — Follower port position-based mechanical translational

Position-based mechanical translational conserving port that represents the
follower connection. For positive length, port **F** has a more
positive position than port **B**.

## Parameters

### **Damping coefficient** — Damping coefficient, defined by viscous friction `1e5 N/(m/s)` (default) | scalar

Damping coefficient, defined by viscous friction.

## Libraries

Simscape / Foundation Library / Translational / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Viscous damper in position-based mechanical translational systems

The Translational Damper (PB) block represents an ideal
viscous damper in position-based mechanical translational systems. The block uses these
equations

f=−D⋅v

v=vF−vB

length=xF−xB

power\_dissipated=D⋅v2

where:

- *f* is force transmitted through the damper.
- *D* is damping coefficient, defined by viscous friction.
- *v* is relative velocity.
- *v*F and
  *v*B are the absolute velocities of ports
  **B** and **F**, respectively.
- *length* is the damper length.
- *x*B and
  *x*F are the absolute positions of ports
  **B** and **F**, respectively.
- *power\_dissipated* is the power dissipated through the damper.

Connections **B** and **F** are position-based
mechanical translational conserving ports. The damper force acts from port
**B** on port **F**. The negative sign in the first
equation reflects the force flow conventions used in the position-based mechanical
translational domain. For more information, see Two-Port Block Orientation and Force Flow Conventions.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
