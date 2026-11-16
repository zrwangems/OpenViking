---
type: simulink-block
title: 'External Force Source (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Sources'
documentation_page: 'externalforcesourcepb'
documentation_source_path: 'ref/externalforcesourcepb.html'
language: en
---

# External Force Source (PB)

## Ports

### Input

### **S** — Control signal, N physical signal

Physical signal input port for the control signal that drives the source. A
positive signal at this port applies a positive force on the network at port
**R**.
### Conserving

### **R** — Port that applies external force to the network position-based mechanical translational

Position-based mechanical translational conserving port that connects the block to
the circuit and applies the external force to the physical network.

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

Ideal source of mechanical energy that generates force proportional to the input signal

The External Force Source (PB) block represents an ideal
external force source that generates a specified force regardless of the load or velocity at
the connected port.

Port **R** is a position-based mechanical translational conserving port.
Specify the force at physical signal port **S**. A positive signal at port
**S** applies a positive force on the network at port
**R**.

For example, in this model, the External Force Source (PB)
block applies a positive force of 1 N between the two springs. The positive direction of the
rail is horizontal, from left to right.

Model diagram with force applied

The force flows outward from the External Force Source (PB)
block. Therefore, negative force flows through the spring on the left and positive force flows
through the spring on the right. The spring on the left is in tension and the spring on the
right is in compression.

The block logs the variable `f`, which represents the force applied on
the network at port **R**. For more information, see Data Logging.
