---
type: simulink-block
title: 'DC Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Machine Control\u200b'
documentation_page: 'dccurrentcontroller'
documentation_source_path: 'ref/dccurrentcontroller.html'
language: en
---

# DC Current Controller

## Ports

### Input

### **iRef** — Reference current scalar

Desired output current for the plant.

**Data Types:** `single` | `double`

### **i** — Measured current scalar

Measured current for the plant.

**Data Types:** `single` | `double`

### **vmax** — Maximum DC voltage scalar

Maximum DC output voltage for the plant.

**Data Types:** `single` | `double`

### **Reset** — External reset scalar

External reset signal (rising edge) for the integrator.

**Data Types:** `single` | `double`
### Output

### **vRef** — Reference DC voltage scalar

Desired DC output voltage for the plant.

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

### **Voltage limitation** — Negative voltage restriction `Positive and negative voltage` (default) | `Positive voltage only`

Allow for both positive and negative DC voltage output or limit the output to positive DC
voltage.

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

Simscape / Electrical / Control / General Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Discrete-time DC current PI control with integral anti-windup

The DC Current Controller block implements a discrete-time
proportional-integral (PI) DC voltage controller. The block can implement zero
cancellation in the feedforward path. To avoid saturation of the integral gain, the
block can implement anti-windup gain.

### Equations

The equation that the DC Current Controller block uses to calculate the
reference voltage is

vref=(Kp+KiTszz−1)(iref−i),

where:

- *vref* is the reference
  voltage.
- *Kp* is the proportional
  gain.
- *Ki* is the integral
  gain.
- *Ts* is the sample
  time.
- *iref* is the reference
  current.
- *i* is the measured current.

The PI control calculation yields a zero in the closed-loop transfer function. To cancel
the zero, the block uses this discrete-time zero-cancellation transfer function:

GZC(z)=TsKiKpz+(Ts−KpKiKpKi).

To avoid saturation of the integrator output, the block uses an anti-windup mechanism. The
integrator gain is then equal to

Ki+Kaw(vref\_sat−vref\_unsat),

where:

- *Kaw* is the anti-windup
  gain.
- *vref\_sat* is the saturated
  reference voltage signal, which the block calculates as vref\_sat=min(max(vref\_unsat,vmin),vmax),

  where:

  - *vref\_unsat* is
    the unsaturated reference voltage signal.
  - *vmin* is the
    lower limit for the output voltage. For positive voltage
    only, vmin=0. For positive and negative voltage, vmin=−vmax
  - *vmax* is the
    upper limit for the output voltage.
