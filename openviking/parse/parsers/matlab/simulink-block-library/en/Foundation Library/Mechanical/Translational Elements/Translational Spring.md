---
type: simulink-block
title: 'Translational Spring'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'translationalspring'
documentation_source_path: 'ref/translationalspring.html'
language: en
---

# Translational Spring

## Ports

### Conserving

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with the rod, that is, the
moving body.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the case, that is, the
stationary body.

## Parameters

### **Spring rate** — Spring rate `1000 N/m` (default) | scalar

Spring rate.

## Libraries

Simscape / Foundation Library / Mechanical / Translational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Ideal spring in mechanical translational systems

The Translational Spring block represents an ideal
mechanical linear spring, described with the following equations:

F=Kx

x=xinit+xR−xC

v=dxdt

where

- *F* is force transmitted through the spring.
- *K* is spring rate.
- *x* is relative displacement, that is, spring deformation.
- *x*init is initial displacement, that is,
  initial spring deformation. If *`xinit >
  0`*, the spring is initially compressed. If
  *`xinit < 0`*, the spring is
  initially stretched.
- *x*R and
  *x*C are absolute displacements of ports
  **R** and **C**, respectively.
- *v* is relative velocity.
- *t* is time.

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
