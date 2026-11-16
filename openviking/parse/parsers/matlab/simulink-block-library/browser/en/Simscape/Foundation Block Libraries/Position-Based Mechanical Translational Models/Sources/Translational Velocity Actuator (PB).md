---
type: simulink-block
title: 'Translational Velocity Actuator (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Sources'
documentation_page: 'translationalvelocityactuatorpb'
documentation_source_path: 'ref/translationalvelocityactuatorpb.html'
language: en
---

# Translational Velocity Actuator (PB)

## Ports

### Input

### **S** — Control signal that specifies relative velocity between the ports, m/s physical signal

Physical signal input port for the control signal that drives the source. A
positive signal at this port indicates that the velocity at port
**F** is greater than at port **B**.
### Conserving

### **B** — Base port position-based mechanical translational

Position-based mechanical translational conserving port that represents the base
connection.

### **F** — Follower port position-based mechanical translational

Position-based mechanical translational conserving port that represents the
follower connection. For positive length, port **F** has a more
positive position than port **B**.

## Parameters

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

Ideal velocity actuator, with length, that maintains velocity proportional to the input signal

The Translational Velocity Actuator (PB) block represents
an ideal velocity actuator, with length, that maintains a specified relative velocity
regardless of the load at the connected ports.

Connections **B** and **F** are position-based
mechanical translational conserving ports. The physical signal at port **S**
specifies the relative velocity between the ports **B** and
**F**. A positive signal at port **S** indicates that the
velocity at port **F** is greater than at port **B**.

The block logs these variables:

- `f` — force that port **B** applies to port
  **F**. A positive logged force indicates that the actuator acts to
  separate the ports when length is positive, that is, the actuator is in a state of
  compression. A negative logged force indicates that the actuator acts to bring the ports
  closer together when length is positive, that is, the actuator is in a state of
  tension.
- `v` — relative velocity between ports, specified by the signal at
  port **S**, v=vF−vB

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
