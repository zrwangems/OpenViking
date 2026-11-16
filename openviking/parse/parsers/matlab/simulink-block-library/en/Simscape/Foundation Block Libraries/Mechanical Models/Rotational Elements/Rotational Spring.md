---
type: simulink-block
title: 'Rotational Spring'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Rotational Elements'
documentation_page: 'rotationalspring'
documentation_source_path: 'ref/rotationalspring.html'
language: en
---

# Rotational Spring

## Ports

### Conserving

### **R** — Rod mechanical rotational

Mechanical rotational conserving port associated with the rod, that is, the moving
body.

### **C** — Case mechanical rotational

Mechanical rotational conserving port associated with the case, that is, the
stationary body.

## Parameters

### **Spring rate** — Spring rate `10 N*m/rad` (default) | scalar

Spring rate.

## Libraries

Simscape / Foundation Library / Mechanical / Rotational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Ideal spring in mechanical rotational systems

The Rotational Spring block represents an ideal mechanical
rotational linear spring, described with the following equations:

T=K·φ

φ=φinit+φR−φC

ω=dφdt

where

- *T* is torque transmitted through the spring.
- *K* is spring rate.
- *φ* is relative displacement angle, that is, spring
  deformation.
- *φ*init is spring preliminary winding.
- *φ*R and
  *φ*C are absolute angular displacements of ports
  **R** and **C**, respectively.
- *ω* is relative angular velocity.
- *t* is time.

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
