---
type: simulink-block
title: 'Translational Damper'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Translational Elements'
documentation_page: 'translationaldamper'
documentation_source_path: 'ref/translationaldamper.html'
language: en
---

# Translational Damper

## Ports

### Conserving

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with the rod, that is, the
moving body.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the case, that is, the
stationary body.

## Parameters

### **Damping coefficient** — Damping coefficient, defined by viscous friction `100 N/(m/s)` (default) | scalar

Damping coefficient, defined by viscous friction.

## Libraries

Simscape / Foundation Library / Mechanical / Translational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Viscous damper in mechanical translational systems

The Translational Damper block represents an ideal
mechanical translational viscous damper, described with the following equations:

F=Dv

v=vR−vC

where

- *F* is force transmitted through the damper.
- *D* is damping coefficient, defined by viscous friction.
- *v* is relative velocity.
- *v*R and
  *v*C are absolute velocities of ports
  **R** and **C**, respectively.

The block positive direction is from port **R** to port
**C**. This means that the force is positive if it acts in the direction
from **R** to **C**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
