---
type: simulink-block
title: 'Length Actuator (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Sources'
documentation_page: 'lengthactuatorpb'
documentation_source_path: 'ref/lengthactuatorpb.html'
language: en
---

# Length Actuator (PB)

## Ports

### Input

### **S** — Control signal, m physical signal

Physical signal input port for the control signal that drives the source. A
positive signal at this port applies a positive force from port **B**
to port **F** and acts to separate the ports **B**
and **F** when the actuator length is positive.
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

Ideal actuator that maintains length proportional to the input signal

The Length Actuator (PB) block represents an ideal actuator
that maintains a specified length regardless of the load at the connected ports.

Connections **B** and **F** are position-based
mechanical translational conserving ports. The physical signal at port **S**
specifies the distance between the ports **B** and **F**. A
positive signal at port **S** indicates that port **F** has
a more positive position than port **B**.

The block logs these variables:

- `f` — force that port **B** applies to port
  **F**. A positive logged force indicates that the actuator acts to
  separate the ports when length is positive, that is, the actuator is in a state of
  compression. A negative logged force indicates that the actuator acts to bring the ports
  closer together when length is positive, that is, the actuator is in a state of
  tension.
- `v` — relative velocity, v=vF−vB
- `length` — distance between ports, specified by the signal at port
  **S**, length=xF−xB.

For more information, see Data Logging.
