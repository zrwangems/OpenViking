---
type: simulink-block
title: 'External Translational Velocity Source (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Sources'
documentation_page: 'externaltranslationalvelocitysourcepb'
documentation_source_path: 'ref/externaltranslationalvelocitysourcepb.html'
language: en
---

# External Translational Velocity Source (PB)

## Ports

### Input

### **S** — Control signal, m/s physical signal

Physical signal input port for the control signal that drives the source. A
positive signal at this port applies a positive velocity to the network at port
**R**.
### Conserving

### **R** — Port that applies external velocity to the network position-based mechanical translational

Position-based mechanical translational conserving port that connects the block to
the circuit and applies the external velocity to the physical network.

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

Ideal source of mechanical energy that generates velocity proportional to the input signal

The External Translational Velocity Source (PB) block
represents an ideal external velocity source that generates a specified velocity regardless of
the load at the connected port.

Port **R** is a position-based mechanical translational conserving port.
Specify the velocity at physical signal port **S**. A positive signal at port
**S** applies a positive velocity to the network at port
**R**.

The block logs the variable `f`, which represents the force applied at
port **R** to generate the specified velocity. A positive force corresponds
to acceleration in the positive direction. For more information, see Data Logging.
