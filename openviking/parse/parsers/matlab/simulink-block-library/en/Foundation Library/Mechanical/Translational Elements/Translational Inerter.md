---
type: simulink-block
title: 'Translational Inerter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'translationalinerter'
documentation_source_path: 'ref/translationalinerter.html'
language: en
---

# Translational Inerter

## Ports
```yaml
ports:
- name: R
  summary: Rod mechanical translational
  direction: conserving
- name: C
  summary: Case mechanical translational
  direction: conserving
```

### Conserving

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with the rod, that is, the
moving body.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the case, that is, the
stationary body.
## Parameters
```yaml
parameters:
- name: Inertance
  summary: Proportionality coefficient between force and rate of change of relative velocity across ports 1 kg (default) |
    scalar
  group: ''
```

### **Inertance** — Proportionality coefficient between force and rate of change of relative velocity across ports `1 kg` (default) | scalar

Proportionality coefficient between the force and the rate of change of the relative
velocity across the ports.
## Libraries

Simscape / Foundation Library / Mechanical / Translational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Two-port inertia in mechanical translational systems

The Translational Inerter block represents a device that
has force proportional to the rate of change of the relative velocity across the ports. It is
essentially a two-port inertia that works on the velocity difference between the ports, not
the absolute velocity. An inerter is the mechanical equivalent of a capacitor. An inerter with
one port connected to ground essentially behaves as a mass with the mass equal to the
inerter’s inertance.

Use this block in high performance suspension systems, to decouple weave and roll modes,
or in applications where you need to model a passively tuned mass-spring-damper
response.

The block is described with the following equations:

f=Bdvdt

v=vR−vC

where

- *f* is force transmitted through the inerter.
- *B* is inertance.
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
