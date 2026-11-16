---
type: simulink-block
title: 'PI Controller (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Controllers'
documentation_page: 'picontrollerdiscreteorcontinuous'
documentation_source_path: 'ref/picontrollerdiscreteorcontinuous.html'
language: en
---

# PI Controller (Discrete or Continuous)

## Ports

### Input

### **e** — Error signal scalar

Error signal, *e(k)*, obtained as the difference
between the reference, *r(k)*, and measurement,
*y(k)*, signals.

**Data Types:** `single` | `double`

### **du** — Control signal saturation scalar

Difference, *du(k)*, between the saturated
*u^sat(k)* and the unsaturated control signals,
*u(k)*. If *du(k)* is zero, the
anti-windup is disabled.

Description

**Data Types:** `single` | `double`

### **Reset** — Integrator gain reset scalar

External reset (rising edge) signal for the integrator.

**Data Types:** `single` | `double`
### Output

### **u** — Control signal scalar

Control signal, *u(k)*.

**Data Types:** `single` | `double`

## Parameters

### **Proportional gain** — *Kp* `1` (default) | positive scalar

Proportional gain, *Kp*, of the PI
controller.

### **Integral gain** — *Ki* `1` (default) | positive scalar

Integral gain,*Ki*, of the PI
controller.

### **Anti-windup gain** — *Kaw* `1` (default) | positive scalar

Anti-windup gain, *Kaw*, of the PI
controller.

### **Integrator initial condition** — Initial integrator value `0` (default) | scalar

Value of the integrator at simulation start time.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `0` | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set this parameter to `-1`.
For discrete-time operation, set this parameter to a positive integer. For
continuous-time operation, set this parameter to `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote this parameter to ensure
correct switching between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2025a: Support continuous-time simulation

The PI Controller (Discrete or Continuous) block now supports continuous-time simulation. For continuous-time
operation, set the **Sample time (-1 for inherited)** parameter to
`0`.

## Description

Discrete-time or continuous-time PI controller with external anti-windup input

The Discrete PI Controller block implements discrete-time or
continuous-time PI control with external anti-windup input.

This diagram shows the equivalent circuit for the controller with external anti-windup input.

### Equations

The PI Controller (Discrete or Continuous) block calculates the
control signal using the backward Euler discretization method:

u(k)=[Kp+(Ki+du(k)Kaw)Tszz−1]e(k),

where

- *u* is the control signal.
- *Kp* is the proportional gain
  coefficient.
- *Ki* is the integral gain
  coefficient.
- *Kaw* is the anti-windup gain
  coefficient.
- *Ts* is the sampling
  period.
- *e* is the error signal.

To prevent excessive overshoot, the block can use back calculation to implement an
external anti-windup mechanism. It inputs *du(k)*, the difference
between the saturated control signal,
*usat(k)*, and the calculated
unsaturated control signal, *u(k)*. It then multiplies the
difference by the anti-windup coefficient and adds the amplified signal from the
integral gain.
