---
type: simulink-block
title: 'SRM Current Controller with PWM Generation'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SRM Control\u200b'
documentation_page: 'srmcurrentcontrollerwithpwmgeneration'
documentation_source_path: 'ref/srmcurrentcontrollerwithpwmgeneration.html'
language: en
---

# SRM Current Controller with PWM Generation

## Ports

### Input

### **IsRef** — Reference current scalar

Reference current for control.

**Data Types:** `single` | `double`

### **Is** — Measured current scalar

Actual current.

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

### **G** — Gate control vector

Pulse waveforms that determine switching behavior.

**Data Types:** `single` | `double`

## Parameters

### Control Parameters

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

### PWM Generator

### **Carrier counter** — Carrier counter model `Up` (default) | `Down` | `Up-Down`

Use the carrier counter strategy to change the initial behavior of the PWM output:

- Up counter — PWM output begins at the start of the on state.
- Down counter — PWM output begins at the start of the off state.
- Up-down counter — PWM output begins in the middle of the on state.

### **Timer period (s)** — PWM timer period `0.001` (default) | positive scalar

Pulse width modulation timer period, *Tper*,
in seconds.

### **Fundamental sample time (s)** — Sample time for PWM generation `0.0001` (default) | positive scalar

Time, in s, between
consecutive PWM generator executions. During execution, the block produces PWM output
and, if appropriate, updates its internal state. For more information, see What Is Sample Time? and Specify Sample Time.

To ensure adequate resolution in the generated PWM signal,
set the fundamental sample time so that 0<Ts\_pwm≤10Tper, where:

- *Ts\_pwm* is the
  **Fundamental sample time (s)**.
- *Tper* is the **Timer
  period (s)**.

## Libraries

Simscape / Electrical / Control / SRM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Current controller with internal pulse width modulation for switched reluctance machines

The SRM Current Controller with PWM Generation block performs discrete-time
proportional-integral (PI) current control for the Switched Reluctance
Machine (SRM) block. The block includes pulse width modulation
(PWM).

### PWM Generation Model

The figure shows the converter structure for an SRM.

As the figure shows, the PWM generation signal is for high side switching devices.

When the control signal is greater than the carrier counter value, the PWM
generator outputs 1. Otherwise, it outputs 0.

### Equations

To determine the duty cycle, the block implements PI current control in the rotor reference
frame in accordance with this equation.

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
