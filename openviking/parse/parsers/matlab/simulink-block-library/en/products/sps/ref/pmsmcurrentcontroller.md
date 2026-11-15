---
type: simulink-block
title: 'PMSM Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control\u200b'
documentation_page: 'pmsmcurrentcontroller'
documentation_source_path: 'ref/pmsmcurrentcontroller.html'
language: en
---

# PMSM Current Controller

## Ports

### Input

### **idqRef** — Reference currents vector

Desired *d*- and *q*-axis
currents for control of a PMSM, in A.

**Data Types:** `single` | `double`

### **idq** — Measured currents vector

Actual *d*- and *q*-axis
currents of the controlled PMSM, in A.

**Data Types:** `single` | `double`

### **vdqFF** — Feedforward voltages vector

Feedforward pre-control voltages, in V.

**Data Types:** `single` | `double`

### **VphMax** — Maximum phase voltage scalar

Maximum allowable voltage in each phase, in V.

**Data Types:** `single` | `double`

### **Reset** — External reset scalar

External reset signal (rising edge) for integrators.

**Data Types:** `single` | `double`
### Output

### **vdqRef** — Reference voltages vector

Desired *d*- and *q*-axis
voltages for control of a PMSM, in V.

**Data Types:** `single` | `double`

## Parameters

#### Control Parameters

### **D-axis current proportional gain** — D-axis proportional gain `1` (default) | positive number

Proportional gain of the PI controller used for direct-axis current
control.

### **D-axis current integral gain** — D-axis integral gain `100` (default) | positive number

Integrator gain of the PI controller used for direct-axis current
control.

### **D-axis current anti-windup gain** — D-axis anti-windup gain `1` (default) | positive number

Anti-windup gain of the PI controller used for direct-axis current
control.

### **Q-axis current proportional gain** — Q-axis proportional gain `1` (default) | positive number

Proportional gain of the PI controller used for quadrature-axis current
control.

### **Q-axis current integral gain** — Q-axis integral gain `100` (default) | positive number

Integrator gain of the PI controller used for quadrature-axis current
control.

### **Q-axis current anti-windup gain** — Q-axis anti-windup gain `1` (default) | positive number

Anti-windup gain of the PI controller used for quadrature-axis current
control.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `-1` or positive number

Sample time for the block (-1 for inherited). If you use this block inside
a triggered subsystem, set the sample time to -1. If you use this block in a
continuous variable-step model, you can specify the sample time
explicitly.

### **Axis prioritization** — Axis prioritization for voltage limiter `q-axis` (default) | `d-axis` | `d-q equivalence`

Prioritize or maintain the ratio between the *d*- and
*q*-axes when the block limits voltage.

### **Enable zero cancellation** — Feedforward zero-cancellation `off` (default) | `on`

Enable or disable zero-cancellation on the feedforward path.

### **Enable pre-control voltage** — Pre-control voltage `on` (default) | `off`

Enable or disable pre-control voltage.

## Libraries

Simscape / Electrical / Control / PMSM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time permanent magnet synchronous machine current controller

The PMSM Current Controller block implements a discrete-time PI-based
permanent magnet synchronous machine (PMSM) current controller in the rotor
*d*-*q* reference frame.

You typically use this block in a series of blocks making up a control structure.

- You can generate a current reference in the d-q frame to be used as an
  input to this block with a PMSM Current Reference
  Generator.
- You can obtain a voltage reference in the abc domain by converting the
  output of this block using an Inverse Park Transform
  block.

You can see an example of a full control structure, from machine measurements to
machine inputs, in the PMSM Field-Oriented Control block.

### Equations

The block is discretized using the backward Euler method due to its first-order
simplicity and its stability.

Two PI current controllers implemented in the rotor reference frame produce the
reference voltage vector:

vdref=(Kp\_id+Ki\_idTszz−1)(idref−id)+vd\_FF,

and

vqref=(Kp\_iq+Ki\_iqTszz−1)(iqref−iq)+vq\_FF,

where:

- vdref and vqref are the *d*-axis and
  *q*-axis reference voltages, respectively.
- idref and iqref are the *d*-axis and
  *q*-axis reference currents, respectively.
- id and iq are the *d*-axis and
  *q*-axis currents, respectively.
- *Kp\_id* and
  *Kp\_iq* are the
  proportional gains for the *d*-axis and
  *q*-axis controllers, respectively.
- *Ki\_id* and
  *Ki\_iq* are the integral
  gains for the *d*-axis and
  *q*-axis controllers, respectively.
- *vd\_FF* and
  *vq\_FF* are the
  feedforward voltages for the *d*-axis and
  *q*-axis, respectively, obtained from the machine
  mathematical equations and provided as inputs.
- *Ts* is the sample time of the
  discrete controller.

### Zero Cancellation

Using PI control results in a zero in the closed-loop transfer function, which can
result in undesired overshoot in the closed-loop response. This zero can be canceled
by introducing a zero-cancelation block in the feedforward path. The zero
cancellation transfer functions in discrete time are:

GZC\_id(z)=TsKi\_idKp\_idz+(Ts−Kp\_idKi\_idKp\_idKi\_id),

and

GZC\_iq(z)=TsKi\_iqKp\_iqz+(Ts−Kp\_iqKi\_iqKp\_iqKi\_iq).

### Voltage Saturation

Saturation must be imposed when the stator voltage vector exceeds the voltage
phase limit *Vph\_max*:

vd2+vq2≤Vph\_max,

where *vd* and
*vq* are the
*d*-axis and *q*-axis voltages, respectively.

In the case of axis prioritization, the voltages
*v1* and
*v2* are introduced, where:

- *v1 =
  vd* and
  *v2 =
  vq* for *d*-axis
  prioritization.
- *v1 =
  vq* and
  *v2 =
  vd* for *q*-axis
  prioritization.

The constrained (saturated) voltages v1sat and v2sat are obtained as follows:

v1sat=min(max(v1unsat,−Vph\_max),Vph\_max)

and

v2sat=min(max(v2unsat,−V2\_max),V2\_max),

where:

- v1unsat and v2unsat are the unconstrained (unsaturated) voltages.
- *v2\_max* is the maximum value
  of *v2* that does not exceed the
  voltage phase limit, given by v2\_max=(Vph\_max)2−(v1sat)2.

In the case that the direct and quadrature axes have the same priority (d-q
equivalence) the constrained voltages are obtained as follows:

vdsat=min(max(vdunsat,−Vd\_max),Vd\_max)

and

vqsat=min(max(vqunsat,−Vq\_max),Vq\_max),

where

Vd\_max=Vph\_max|vdunsat|(vdunsat)2+(vqunsat)2

and

Vq\_max=Vph\_max|vqunsat|(vdunsat)2+(vqunsat)2.

### Integral Anti-Windup

An anti-windup mechanism is employed to avoid saturation of integrator output. In
such a situation, the integrator gains become:

Ki\_id+Kaw\_id(vdsat−vdunsat)

and

Ki\_iq+Kaw\_iq(vqsat−vqunsat),

where *Kaw\_id* and
*Kaw\_iq* are the anti-windup gains
for the *d*-axis and *q*-axis,
respectively.

### Assumptions

- The plant model for direct and quadrature axis can be approximated
  with a first-order system.
- This control solution is used only for permanent magnet synchronous
  motors with sinusoidal flux distribution and field windings.
