---
type: simulink-block
title: 'Force Actuator (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Sources'
documentation_page: 'forceactuatorpb'
documentation_source_path: 'ref/forceactuatorpb.html'
language: en
---

# Force Actuator (PB)

## Ports
```yaml
ports:
- name: S
  summary: Control signal, N physical signal
  direction: input
- name: B
  summary: Base port position-based mechanical translational
  direction: conserving
- name: F
  summary: Follower port position-based mechanical translational
  direction: conserving
```

### Input

### **S** — Control signal, N physical signal

Physical signal input port for the control signal that drives the source. A
positive signal at this port applies a positive force on the network at port
**F** and acts to separate the ports **B** and
**F** when the actuator length is positive.
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
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Translational / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Ideal force actuator, with length, that generates force proportional to the input signal

The Force Actuator (PB) block represents an ideal force
actuator that has length and generates a specified force regardless of the load or velocity at
the connected ports.

Connections **B** and **F** are position-based
mechanical translational conserving ports. Specify the force at physical signal port
**S**. A positive signal at port **S** applies a positive
force on the network at port **F** and acts to separate the ports
**B** and **F** when the actuator length is
positive.

For example, in this model, the Force Actuator (PB) block
applies a positive force of 1 N between the two springs. The positive direction of the rail is
horizontal, from left to right.

Model diagram with force applied

Port **F** applies a positive force to the spring on the right. This
spring is in compression. At the same time, because the actuator force acts to separate the
ports, Port **B** applies equal but opposite force to the spring on the left.
This spring is also in compression.

The block logs these variables:

- `f` — force
- `v` — relative velocity, v=vF−vB

For more information, see Data Logging.

The actuator length is length=xF−xB.

The block has no parameters. You specify the actuator length as an initial variable
target.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
