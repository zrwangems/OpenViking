---
type: simulink-block
title: 'Rotational Inerter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Rotational Elements'
documentation_page: 'rotationalinerter'
documentation_source_path: 'ref/rotationalinerter.html'
language: en
---

# Rotational Inerter

## Ports
```yaml
ports:
- name: R
  summary: Rod mechanical rotational
  direction: conserving
- name: C
  summary: Case mechanical rotational
  direction: conserving
```

### Conserving

### **R** — Rod mechanical rotational

Mechanical rotational conserving port associated with the rod, that is, the moving
body.

### **C** — Case mechanical rotational

Mechanical rotational conserving port associated with the case, that is, the
stationary body.
## Parameters
```yaml
parameters:
- name: Rotational inertance
  summary: Proportionality coefficient between torque and rate of change of relative velocity across ports 1 kg*m^2 (default)
    | scalar
  group: ''
```

### **Rotational inertance** — Proportionality coefficient between torque and rate of change of relative velocity across ports `1 kg*m^2` (default) | scalar

Proportionality coefficient between the torque and the rate of change of the
relative angular velocity across the ports.
## Libraries

Simscape / Foundation Library / Mechanical / Rotational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Two-port inertia in mechanical rotational systems

The Rotational Inerter block represents a device that has
torque proportional to the rate of change of the relative angular velocity across the ports.
It is essentially a two-port inertia that works on the velocity difference between the ports,
not the absolute velocity.

Use this block in high performance suspension systems, to decouple weave and roll modes,
or in applications where you need to model a passively tuned mass-spring-damper
response.

The block is described with the following equations:

T=Bdωdt

ω=ωR−ωC

where

- *T* is torque transmitted through the inerter.
- *B* is inertance.
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
