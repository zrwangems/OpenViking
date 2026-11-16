---
type: simulink-block
title: 'Model Reference Adaptive Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'modelreferenceadaptivecontroller'
documentation_source_path: 'ref/modelreferenceadaptivecontroller.html'
language: en
---

# Model Reference Adaptive Controller

## Ports

### Input

### **r** — Plant reference, *r* scalar

Plant system reference signal.

**Data Types:** `single` | `double`

### **y** — Plant output, *y* scalar

Plant system output signal.

**Data Types:** `single` | `double`

### **Reset** — Integrator reset scalar

External reset signal (rising edge) for the integrator.

**Data Types:** `Boolean`
### Output

### **u** — Controller adjusted output, *u* scalar

Adjusted control signal.

**Data Types:** `single` | `double`

## Parameters

### Controller Parameters

### **Proportional gain** — Controller proportional gain, *Kp* `1` (default) | positive scalar

Proportional gain, *Kp*, of the
controller.

### **Integral gain** — Controller integral gain, *Ki* `1` (default) | positive scalar

Integral gain, *Ki*, of the controller.

### **Derivative gain** — Controller derivative gain, *Kd* `0` (default)

Derivative gain, *Kd*, of the
controller.

### **Anti-windup gain** — Controller anti-windup gain `1` (default) | positive scalar

Anti-windup gain of the controller.

### **Use filtered derivative** — Filter option `on` (default) | off

Choose whether to use a filter coefficient for the reference
signal.

#### Dependencies

The **Filter coefficient** parameter is only visible when the
**Use filtered derivative** check box is
selected.

### **Filter coefficient** — Reference signal filter coefficient `100` (default)

Filter coefficient for the reference signal.

#### Dependencies

This parameter is only visible when the **Use filtered derivative**
check box is selected.

### **Control action upper limit** — Control signal upper limit, *upid\_max* `5` (default)

Upper bound for the control signal.

### **Control action lower limit** — Control signal lower limit, *upid\_min* `-5` (default)

Lower bound for the control signal.

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
`-1` and, in the **Reference Model** settings,
set **Model parameterization** to
`Continuous-time`, the **Discretization sample
time** parameter becomes visible in the **Reference
Model** settings.

### Reference Model

### **Model parameterization** — Discrete or continuous model option `Discrete-time` (default) | `Continuous-time`

Mathematical model for the controller.

#### Dependencies

Choosing:

- `Discrete-time` makes the
  discrete-time parameters visible.
- `Continuous-time` makes the
  continuous-time parameters visible. Also, in the
  **Controller Parameter** settings,
  if **Sample time (-1 for inherited)**
  is set to `-1`, choosing this option
  makes the **Discretization sample
  time** parameter visible in the
  **Reference Model**
  settings.

### **Discrete-time numerator** — Discrete-time transfer function numerator `[0.01 -0.0099]` (default)

Numerator for the discrete-time transfer function.

#### Dependencies

Choosing `Discrete-time` for
**Model parameterization** makes this parameter
visible.

### **Discrete-time denominator** — Discrete-time transfer function denominator `[1 -1.9801 0.9802]` (default) | vector

Denominator for the discrete-time transfer function.

#### Dependencies

Choosing `Discrete-time` for
**Model parameterization** makes this parameter
visible.

### **Discretization sample time** — Sample time for discretization `0.01` (default) | `-1` or positive number

Time, in seconds, between consecutive discretizations. If block sample
time is inherited, specify the discretization sample time
explicitly.

#### Dependencies

This parameter is only visible when both of these conditions are met:

- In the **Control Parameters**
  settings, **Sample time (-1 for
  inherited)** is set to
  `-1`.
- In the **Reference Model** settings,
  **Model parameterization** is set
  to `Continuous-time`.

### **Continuous-time numerator** — Continuous-time transfer function numerator `[1 1]` (default) | vector

Numerator for the continuous-time transfer function.

#### Dependencies

Choosing `Continuous-time` for
**Model parameterization** makes this parameter
visible.

### **Continuous-time denominator** — Continuous-time transfer function denominator `[1 2 1]` (default) | vector

Denominator for the continuous-time transfer function.

#### Dependencies

Choosing `Continuous-time` for
**Model parameterization** makes this parameter
visible.

### Adjustment Mechanism

### **Learning rate** — *γ* `0.5` (default)

Rate of adjustment to plant changes.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Discrete-time PID-based model reference adaptive control

The Model Reference Adaptive Controller block implements discrete-time
proportional-integral-derivative (PID) model reference adaptive control (MRAC). The
three main components of an MRAC system are the reference model, the adjustment
mechanism, and the controller.

### Equations

The control equation is

upid(k)=[Kp+KiTszz−1+Kdz−1Tsz]e(k),

where:

- *upid* is the controller
  output.
- *Kp* is the proportional
  gain.
- *Ki* is the integral
  gain.
- *Kd* is the differential
  gain.
- *Ts* is the sample
  time.
- *e* is the error.

The reference model is the transfer function for the closed-loop system. This
model captures the desired behavior of the closed-loop system. It is implemented as
the discrete-time transfer function

Gm(z)=B(z)A(z).

The adaptation mechanism adjusts the control action based on the error between the
plant output and the reference model output as

θ=(y−ym)ym−γTszz−1,

where:

- *θ* is the adaptation parameter.
- *y* is the plant output.
- *ym* is the reference model output.
- *γ* is the learning rate.

Increasing the value of *γ* results in faster adaptation to plant
changes.

The adjusted control signal, *u*, is

u(k)=upid(k)θ(k).
