---
type: simulink-block
title: 'Translational Spring (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationalspringpb'
documentation_source_path: 'ref/translationalspringpb.html'
language: en
---

# Translational Spring (PB)

## Ports
```yaml
ports:
- name: B
  summary: Base port position-based mechanical translational
  direction: conserving
- name: F
  summary: Follower port position-based mechanical translational
  direction: conserving
```

### Conserving

### **B** — Base port position-based mechanical translational

Position-based mechanical translational conserving port that represents the base
connection.

### **F** — Follower port position-based mechanical translational

Position-based mechanical translational conserving port that represents the
follower connection. For positive length, port **F** has a more
positive position than port **B**.
## Parameters
```yaml
parameters:
- name: Spring stiffness
  summary: Spring rate 1e5 N/m (default) | scalar
  group: ''
```

### **Spring stiffness** — Spring rate `1e5 N/m` (default) | scalar

Spring rate.
## Libraries

Simscape / Foundation Library / Translational / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Ideal spring in position-based mechanical translational systems

The Translational Spring (PB) block represents an ideal
translational spring. Spring deformation is the difference between length and rest length.
Positive deformation increases length.

f=−K⋅δ

δ=length−lengthrest

length=xF−xB

where:

- *f* is force transmitted through the spring.
- *K* is the spring stiffness.
- *δ* is the spring deformation.
- *length* is the spring length.
- *length*rest is the spring rest length.
- *x*B and
  *x*F are the absolute positions of ports
  **B** and **F**, respectively.
- *power\_dissipated* is the power dissipated through the damper.

Connections **B** and **F** are position-based
mechanical translational conserving ports. The spring force acts from port
**B** on port **F**. Positive spring force drives port
**F** in the positive direction. Positive spring force corresponds to the
spring in a state of compression, if length is positive. For more information, see Two-Port Block Orientation and Force Flow Conventions.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

The correct way to initialize the block depends on its placement in the block
diagram:

- In general, specify any two variables as high-priority targets, for example,
  **Force** and **Length**, or **Rest
  length** and **Deformation**. The exception is
  **Force** and **Deformation**, because these two
  variables are proportional to each other.
- If the spring is in series with a known force, specify only
  **Length** or **Rest length** as a high-priority
  target.
- If the spring is in parallel with a known length, specify only
  **Force**, **Deformation**, or **Rest
  length** as a high-priority target.
- If the spring is in series with a known force and in parallel with a known length,
  do not specify any high-priority targets.
