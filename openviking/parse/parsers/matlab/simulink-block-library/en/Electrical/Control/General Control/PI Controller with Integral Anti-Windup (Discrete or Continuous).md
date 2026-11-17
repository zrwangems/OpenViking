---
type: simulink-block
title: 'PI Controller with Integral Anti-Windup (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'picontrollerwithintegralantiwindupdiscreteorcontinuous'
documentation_source_path: 'ref/picontrollerwithintegralantiwindupdiscreteorcontinuous.html'
language: en
---

# PI Controller with Integral Anti-Windup (Discrete or Continuous)

## Ports
```yaml
ports:
- name: e
  summary: Error signal scalar
  direction: input
  data_types: single | double
- name: Reset
  summary: Integrator gain reset scalar
  direction: input
  data_types: single | double
- name: u
  summary: Control signal scalar
  direction: output
  data_types: single | double
```

### Input

### **e** — Error signal scalar

Error signal, *e(k)*, obtained as the difference
between the reference, *r(k)*, and measurement
*y(k)* signals.

**Data Types:** `single` | `double`

### **Reset** — Integrator gain reset scalar

External reset (rising edge) signal for the integrator.

**Data Types:** `single` | `double`
### Output

### **u** — Control signal scalar

Control signal, *u(k)*.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Proportional gain
  summary: '*Kp* 1 (default) | positive scalar'
  group: ''
- name: Integral gain
  summary: '*Ki* 1 (default) | positive scalar'
  group: ''
- name: Upper saturation limit
  summary: '*B* 5 (default) | scalar greater than the value of the Lower saturation limit parameter'
  group: ''
- name: Lower saturation limit
  summary: '*A* -5 (default) | scalar'
  group: ''
- name: Integrator initial condition
  summary: Initial integrator value 0 (default) | scalar
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | 0 | positive scalar
  group: ''
```

### **Proportional gain** — *Kp* `1` (default) | positive scalar

Proportional gain, *Kp*, of the PI
controller.

### **Integral gain** — *Ki* `1` (default) | positive scalar

Integral gain, *Ki*, of the PI
controller.

### **Upper saturation limit** — *B* `5` (default) | scalar greater than the value of the **Lower saturation limit** parameter

Upper limit, *B*, of the output for the PI
controller.

### **Lower saturation limit** — *A* `-5` (default) | scalar

Lower limit, *A*, of the output for the PI
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

The PI Controller with Integral Anti-Windup (Discrete or Continuous) block now supports continuous-time simulation. For continuous-time
operation, set the **Sample time (-1 for inherited)** parameter to
`0`.

## Description

Discrete-time or continuous-time PI control with integral anti-windup

The PI Controller with Integral Anti-Windup (Discrete or Continuous)
block implements discrete-time or continuous-tiime PI control with internal anti-windup.
This figure shows the equivalent circuit for the controller with internal anti-windup.

### Equations

The block calculates the control signal using the backward Euler discretization method:

u(k)=sat(Kpe(k)+sat(KiTszz−1e(k),A,B),A,B),

sat(x,A,B)=min(max(x,A),B),

where:

- *u* is the control signal.
- *Kp* is the proportional gain
  coefficient.
- *e* is the error signal.
- *Ki* is the integral gain
  coefficient.
- *Ts* is the sampling
  period.
- *A* is the lower limit for saturation.
- *B* is the upper limit for saturation.
