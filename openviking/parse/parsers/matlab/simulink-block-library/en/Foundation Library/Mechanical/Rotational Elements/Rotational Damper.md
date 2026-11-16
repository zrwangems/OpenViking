---
type: simulink-block
title: 'Rotational Damper'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Rotational Elements'
documentation_page: 'rotationaldamper'
documentation_source_path: 'ref/rotationaldamper.html'
language: en
---

# Rotational Damper

## Ports

### Conserving

### **R** — Rod mechanical rotational

Mechanical rotational conserving port associated with the rod, that is, the moving
body.

### **C** — Case mechanical rotational

Mechanical rotational conserving port associated with the case, that is, the
stationary body.

## Parameters

### **Damping coefficient** — Damping coefficient `0.001 N*m/(rad/s)` (default) | scalar

Damping coefficient, defined by viscous friction.

## Libraries

Simscape / Foundation Library / Mechanical / Rotational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Viscous damper in mechanical rotational systems

The Rotational Damper block represents an ideal mechanical
rotational viscous damper described with the following equations:

T=D·ω

ω=ωR−ωC

where

- *T* is torque transmitted through the damper.
- *D* is damping coefficient, defined by viscous friction.
- *ω* is relative angular velocity.
- *ω*R and
  *ω*C are absolute angular velocities of ports
  **R** and **C**, respectively.

The block positive direction is from port **R** to port
**C**. This means that if the port **R** velocity is
greater than that of port **C**, the block transmits torque from
**R** to **C**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
