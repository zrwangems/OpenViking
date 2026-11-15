---
type: simulink-block
title: 'Thyristor Rectifier Voltage Controller (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Converter Control\u200b'
documentation_page: 'thyristorrectifiervoltagecontrollerthreephase'
documentation_source_path: 'ref/thyristorrectifiervoltagecontrollerthreephase.html'
language: en
---

# Thyristor Rectifier Voltage Controller (Three-Phase)

## Ports

### Input

### **VdcRef** — Reference DC voltage, V scalar

Desired DC-link voltage.

**Data Types:** `single` | `double`

### **Vdc** — DC-link voltage, V scalar

Measured DC-link voltage.

**Data Types:** `single` | `double`

### **Reset** — External reset scalar

External reset signal (rising edge) for integrators.

**Data Types:** `single` | `double`

### **Vabc** — Three-phase voltage, V vector

Three-phase voltage specified as a vector of that contains the
*a*-, *b*-, and
*c*-phase voltages.

**Data Types:** `single` | `double`
### Output

### **P** — Pulses vector

Pulse control signal.

**Data Types:** `single` | `double`

## Parameters

### **Loop filter proportional gain** — Loop filter *Kp* `2` (default) | positive scalar

Loop filter proportional gain for the phase-locked loop (PLL).

### **Loop filter integral gain** — Loop filter *Ki* `20` (default) | positive scalar

Loop filter integral gain for the phase-locked loop (PLL).

### **Proportional gain** — Controller *Kp* `1` (default) | positive scalar

Proportional gain for the PI-controller that generates the reference phase
voltage.

### **Integral gain** — Controller *Ki* `1` (default) | positive scalar

Integral gain for the PI-controller that generates the reference phase
voltage.

### **Thyristor pulse width (rad)** — Pulse width `5*pi/6` (default) | positive scalar

Angular width of pulses.

### **Pulse ordering** — Pulse ordering rule `Sequential device order` (default) | `Natural order of commutation`

Model for the ordering the generated pulses.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

### **Time constant voltage filter** — DC voltage filter *τ* `0.001` (default) | positive scalar

Time constant for the DC voltage filter.

#### Dependencies

The **Time constant voltage filter** parameter is only visible when the
**Filter DC voltage** check box is selected.

### **Filter DC voltage** — DC voltage filter option on (default) | off

When the check box is:

- Selected — The block filters the DC voltage signal.
- Cleared — The block does not filter the DC voltage
  signal.

#### Dependencies

The **Time constant voltage filter** parameter is only visible when the
**Filter DC voltage** check box is selected.

## Libraries

Simscape / Electrical / Control / Converter Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Discrete-time DC-link voltage PI control for thyristor rectifiers

The Thyristor Rectifier Voltage Controller (Three-Phase) block implements a
discrete-time proportional-integral (PI) based DC-link voltage controller for thyristor
rectifiers.

### Model

To regulate the output DC-link voltage of a thyristor rectifier, the Thyristor
Rectifier Voltage Controller (Three-Phase) block determines firing
angles using the cosine wave-crossing method. The figure shows the control
structure, which includes a three-phase phase-locked loop (PLL).
