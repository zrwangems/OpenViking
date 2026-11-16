---
type: simulink-block
title: 'Sliding Mode Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'slidingmodecontroller'
documentation_source_path: 'ref/slidingmodecontroller.html'
language: en
---

# Sliding Mode Controller

## Ports

### Input

### **r** — Plant reference scalar

Plant system reference signal.

**Data Types:** `single` | `double`

### **y** — Plant output scalar

Plant system output signal.

**Data Types:** `single` | `double`
### Output

### **u** — Controller output scalar

Control system output signal.

**Data Types:** `single` | `double`

## Parameters

### **Sliding factor** — Sliding factor `1` (default) | nonnegative scalar

*Since R2024b*

Sliding factor that affects the convergence speed of the error to
zero.

### **Hysteresis band** — Total hysteresis bandwidth `0.2` (default)

Total hysteresis bandwidth, distributed symmetrically about the set
point.

### **Control action upper limit** — Control signal upper limit, *umax* `10` (default) | scalar greater than the value of the **Control action lower limit** parameter

Upper limit for the control output signal.

### **Control action lower limit** — Control signal lower limit, *umin* `-10` (default) | scalar

Lower limit for the control output signal.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: Specify the sliding factor of the controller

You can now specify the value of the sliding factor of the controller by using the
**Sliding factor** parameter. The **Sliding
factor** parameter affects the speed of the convergence of the error to
zero, allowing you to obtain the desired response faster.

## Description

Hysteresis-based sliding mode control

The Sliding Mode Controller block implements hysteresis-based sliding mode
control (SMC).

The sliding mode controller has this structure.

Implementation of the sliding mode controller in Simulink. There are two input ports, r and y, and one output port, u.

In this controller, *lambda* is the value of the
**Sliding factor** parameter. To change the convergence speed of
the error to zero, specify a value greater than `0` for the
**Sliding factor** parameter.
