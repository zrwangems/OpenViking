---
type: simulink-block
title: 'Velocity Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Machine Control'
documentation_page: 'velocitycontroller'
documentation_source_path: 'ref/velocitycontroller.html'
language: en
---

# Velocity Controller

## Ports
```yaml
ports:
- name: wRef
  summary: Desired velocity scalar
  direction: input
  data_types: single | double
- name: wMechanical
  summary: Actual velocity scalar
  direction: input
  data_types: single | double
- name: TqRefSat
  summary: Saturated reference torque scalar
  direction: input
  data_types: single | double
- name: Reset
  summary: Integral reset scalar
  direction: input
  data_types: single | double
- name: TqRefUnsat
  summary: Unsaturated desired torque scalar
  direction: output
  data_types: single | double
```

### Input

### **wRef** — Desired velocity scalar

Desired or reference velocity, in rad/s.

**Data Types:** `single` | `double`

### **wMechanical** — Actual velocity scalar

Measured mechanical velocity, in rad/s.

**Data Types:** `single` | `double`

### **TqRefSat** — Saturated reference torque scalar

Saturated torque reference used for integral anti-windup gain, in
N\*m.

**Data Types:** `single` | `double`

### **Reset** — Integral reset scalar

External reset signal (rising edge) for the integrator.

**Data Types:** `single` | `double`
### Output

### **TqRefUnsat** — Unsaturated desired torque scalar

Unsaturated reference torque, in N\*m.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Control type
  summary: Control model PI control (default) | P control | P-PI control
  group: ''
- name: Controller proportional gain
  summary: Proportional gain 1 (default) | positive scalar
  group: ''
- name: Controller integral gain
  summary: Integral gain 1 (default) | positive scalar
  group: ''
- name: P controller proportional gain
  summary: P proportional gain 1 (default) | positive scalar
  group: ''
- name: Integral anti-windup gain
  summary: PI anti-windup gain 1 (default) | positive scalar
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | positive scalar
  group: ''
- name: Discretization sample time
  summary: Sample time for discretization 0.001 (default) | positive scalar
  group: ''
- name: Enable zero cancellation
  summary: Feedforward zero-cancellation off (default) | on
  group: ''
```

### **Control type** — Control model `PI control` (default) | `P control` | `P-PI control`

Type of controller:

- `PI control` — Proportional-integral control
  using a single feedback loop
- `P control` — Proportional-integral control using
  a single feedback loop
- `P-PI control` — Proportional and
  proportional-integral control using a double feedback loop

#### Dependencies

The **Control type** options affect the visibility or
configurability of these parameters:

- **Controller integral gain**
- **P controller proportional gain**
- **Anti-windup gain**
- **Integral anti-windup gain**
- **Sample time (-1 for inherited)**
- **Enable zero cancellation**

### **Controller proportional gain** — Proportional gain `1` (default) | positive scalar

Proportional gain for the:

- PI controller
- P controller in the single-loop control model
- PI controller in the P-PI controller

### **Controller integral gain** — Integral gain `1` (default) | positive scalar

Integral gain for the PI or P-PI controller.

#### Dependencies

This parameter is visible only when the **Control type** is set
to `PI control` or `P-PI
control`.

### **P controller proportional gain** — P proportional gain `1` (default) | positive scalar

Proportional gain for the P controller in the P-PI controller.

#### Dependencies

This parameter is visible only when the **Control type** is set
to `P-PI control`.

### **Integral anti-windup gain** — PI anti-windup gain `1` (default) | positive scalar

Anti-windup gain for the PI controller.

#### Dependencies

This parameter is visible only when the **Control type** is set
to `PI control` or `P-PI
control`.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

#### Dependencies

This parameter is visible only when the **Control type** is set
to `PI control` or `P-PI
control`.

### **Discretization sample time** — Sample time for discretization `0.001` (default) | positive scalar

Time, in s, between consecutive discretizations. Discretization is required for zero
cancellation.

#### Dependencies

This parameter is only visible when all these conditions are met:

- **Control type** is set to `PI
  control` or `P-PI
  control`.
- **Sample time** is set to
  `-1`.
- **Enable zero cancellation** is selected .

### **Enable zero cancellation** — Feedforward zero-cancellation `off` (default) | `on`

Option to use zero cancellation on the feedforward path.

#### Dependencies

The **Enable zero cancellation** parameter is visible only when
**Control type** is set to `PI
control` or `P-PI control`.

The **Discretization sample time** parameter is only visible when
**Enable zero cancellation** is selected .
## Libraries

Simscape / Electrical / Control / General Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time velocity controller

The Velocity Controller block implements a velocity controller in
discrete-time.

You provide measured and reference rotor velocities (*w* and
*wref*) as inputs to the block. The
block then outputs a reference torque *Tref* for
an electric drive.

To prevent windup in the integrator, feed the saturated reference
torque *Tref\_sat* from the electric drive back
to the velocity controller.

### Equations

You can control the rotor angular velocity with discrete sample time
*Ts* using one of three common approaches:

- Proportional-integral (PI) control, with proportional and integral
  gains *Kp\_w* and
  *Ki\_w*:

  Tref=(Kp\_w+Ki\_wTszz−1)(wref−w)
- Proportional (P) control, with proportional gain
  *Kp\_w*:

  Tref=Kp\_w(wref−w)
- P-PI control characterized by a double velocity feedback loop as shown
  in the following figure:

  Here, the PI Controller block is structured as in the
  PI control strategy, and *Kv* is
  the proportional gain for a P controller.

**Zero Cancellation**

Using PI control results in a zero in the closed-loop transfer function, which
can result in undesired overshoot in the closed-loop response. This zero can be
canceled by introducing a zero-cancelation block in the feedforward path. The
zero cancellation transfer function in discrete time is

GZC\_w(z)=TsKi\_wKp\_wz+(Ts−Kp\_wKi\_wKp\_wKi\_w)
