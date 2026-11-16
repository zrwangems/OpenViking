---
type: simulink-block
title: 'BLDC Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / BLDC Control'
documentation_page: 'bldccurrentcontroller'
documentation_source_path: 'ref/bldccurrentcontroller.html'
language: en
---

# BLDC Current Controller

## Ports

### Input

### **IsRef** — Reference current scalar

Reference current for control.

**Data Types:** `single` | `double`

### **Is** — Measured current scalar

Actual current.

**Data Types:** `single` | `double`

### **Reset** — External reset scalar

External reset signal (rising edge) for the integrator.

**Data Types:** `single` | `double`

### **Hall** — Hall sensor vector

Hall sensor data.

**Data Types:** `single` | `double`

### **Direction** — Motor direction scalar

Direction of motor rotation.

**Data Types:** `single` | `double`
### Output

### **vabcRef** — Reference voltage vector

Reference voltage for the *a*-,
*b*-, and *c*-phases.

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

#### Dependencies

If you set **Sample time (-1 for inherited)** to
`-1` and select the **Enable zero
cancellation** option, the **Discretization sample
time** parameter becomes visible.

### **Discretization sample time** — Sample time for discretization `0.001` (default) | positive scalar

Time, in s, between consecutive discretizations. Discretization is required for zero
cancellation.

#### Dependencies

This parameter is only visible when both these conditions are met:

- **Sample time** is set to
  `-1`.
- **Enable zero cancellation** is selected.

### **Enable zero cancellation** — Feedforward zero cancellation off (default) | on

Option to use zero cancellation on the feedforward path.

#### Dependencies

If you select the **Enable zero cancellation** option and set
**Sample time (-1 for inherited)** to `-1`,
the **Discretization sample time** parameter becomes
visible.

## Libraries

Simscape / Electrical / Control / BLDC Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Discrete-time Brushless DC Motor current PI controller

The BLDC Current Controller block uses this algorithm to control current in a
DC brushless motor.

### Equations

The BLDC Current Controller produces the duty cycle for a BLDC block by implementing proportional-integral (PI) current
control using this equation.

D=(Kp+KiTszz−1)(Is\_ref−Is)

Where:

- *D* is the duty cycle.
- *Kp* is the proportional
  gain.
- *Ki* is the integral
  gain.
- *Ts* is the time
  period.
- *Is\_ref* is the reference
  current.
- *Is* is the measured
  current.
- *Gzc* is the zero cancellation
  polynomial.

The closed-loop transfer function for the PI control algorithm yields a zero that can be
cancelled by using zero-cancellation in the feedforward path. The zero-cancellation
transfer function in discrete-time is:

GZC(z)=TsKiKpz+(Ts−KpKiKpKi).

The block obtains control signals for the three phases by multiplying the duty cycle by the
commutation signals. The resulting three control signals are normalized over the
interval [-1, 1].
