---
type: simulink-block
title: 'SRM Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SRM Control\u200b'
documentation_page: 'srmcurrentcontroller'
documentation_source_path: 'ref/srmcurrentcontroller.html'
language: en
---

# SRM Current Controller

## Ports

### Input

### **IsRef** — Reference current scalar

Reference current for control.

**Data Types:** `single` | `double`

### **Is** — Measured current scalar

Measured current.

**Data Types:** `single` | `double`

### **Reset** — Integrator reset scalar

External reset signal (rising edge) for the integrator.

**Data Types:** `Boolean`

### **theta** — Theta-rotor angle scalar

Rotor angle in the interval [0, *β* ].

**Data Types:** `single` | `double`

### **thetaON** — Switch-on angle scalar

Angle for switching on the phase supply.

**Data Types:** `single` | `double`

### **thetaOFF** — Switch-off angle scalar

Angle for switching on the phase supply.

**Data Types:** `single` | `double`
### Output

### **abcRef** — Reference voltage vector

Control signal normalized in the interval [0, 1].

**Data Types:** `single` | `double`

### **abcOnOff** — Switch signal vector

Switch signal for the *a*-, *b*-, and
*c*-phases. `1` for the switch-on
condition and `0` for switch-off condition

**Data Types:** `single` | `double`

## Parameters

### **Proportional gain** — Controller proportional gain, *Kp* `1` (default) | positive scalar

Proportional gain, *Kp*, of the
controller.

### **Integral gain** — Integral gain, *Ki* `5` (default) | positive scalar

Integral gain, *Ki*, of the controller.

### **Anti-windup gain** — Anti-windup gain, *Kaw* `1` (default) | positive scalar

Anti-windup gain, *Kaw*, of the
controller.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

## Libraries

Simscape / Electrical / Control / SRM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Current control for switched reluctance machines

The SRM Current Controller block performs discrete-time proportional-integral
(PI) current control for the Switched Reluctance
Machine (SRM) block.

### Equations

To determine the duty cycle, the block implements discrete-time proportional-integral (PI)
current control in accordance with this equation.

D=(Kp+KiTszz−1)(Is\_ref−Is)

Where:

- *D* is the duty cycle.
- *Kp* is the proportional
  gain.
- *Ki* is the integral
  gain.
- *Ts* is the sample
  time.
- *Is\_ref* is the reference
  current.
- *Is* is the measured
  current.

To obtain control signals for the three-phases, the block then multiplies the duty
cycle with the commutation signals. The resulting three control signals are
normalized over the interval [0, 1].
