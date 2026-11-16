---
type: simulink-block
title: 'Induction Machine Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinecurrentcontroller'
documentation_source_path: 'ref/inductionmachinecurrentcontroller.html'
language: en
---

# Induction Machine Current Controller

## Ports

### Input

### **idqRef** — Reference currents vector

Desired *d*- and *q*-axis currents
for control of the induction machine, in A.

**Data Types:** `single` | `double`

### **idq** — Measured currents vector

Actual *d*- and *q*-axis currents of
the controlled induction machine, in A.

**Data Types:** `single` | `double`

### **vdqFF** — Feedforward voltages vector

Feedforward pre-control voltages, in V.

**Data Types:** `single` | `double`

### **VphMax** — Maximum phase voltage scalar

Maximum allowable voltage in each phase, in V.

**Data Types:** `single` | `double`

### **Reset** — External reset scalar

External reset signal (rising edge) for integrators.

**Data Types:** `Boolean`
### Output

### **vdqRef** — Reference voltages vector

Desired *d*- and *q*-axis voltages
for control of the induction machine, in V.

**Data Types:** `single` | `double`

## Parameters

#### Control Parameters

### **D-axis current proportional gain** — *d*-axis proportional gain `1` (default)

Proportional gain for direct-axis current control.

### **D-axis current integral gain** — *d*-axis integral gain `100` (default)

Integral gain for direct-axis current control.

### **D-axis current anti-windup gain** — *d*-axis anti-windup gain `1` (default)

Anti-windup gain for direct-axis current control.

### **Q-axis current proportional gain** — *q*-axis proportional gain `1` (default)

Proportional gain for quadrature-axis current control.

### **Q-axis current integral gain** — *q*-axis integral gain `100` (default)

Integral gain for quadrature-axis current control.

### **Q-axis current anti-windup gain** — *q*-axis anti-windup gain `1` (default)

Anti-windup gain for quadrature-axis current control.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

### **Axis prioritization** — Axis prioritization for voltage limiter `Q-axis` (default) | `D-axis` | `D-Q equivalence`

Prioritize or maintain the ratio between the *d*- and
*q*-axes when the block limits voltage.

### **Enable pre-control voltage** — Pre-control voltage `on` (default) | `off`

Enable or disable pre-control voltage.

## Libraries

Simscape / Electrical / Control / Induction Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time induction machine current PI controller

The Induction Machine Current Controller implements discrete-time
proportional-integral (PI) based induction machine current control in the rotor
*d*-*q* reference frame. You typically use the
Induction Machine Current Controller in a series of blocks that make
up a control structure. For example, to convert the *dq0* reference
frame output voltage to voltage in an *abc* reference frame, connect
the Induction Machine Current Controller to an Inverse Clarke
Transform in the control structure.

### Equations

The block uses the backward Euler discretization method.

Two PI current controllers that are implemented in the rotor reference frame
produce the reference voltage vector:

vdref=(Kp\_id+Ki\_idTszz−1)(idref−id)+vd\_FF,

and

vqref=(Kp\_iq+Ki\_iqTszz−1)(iqref−iq)+vq\_FF,

where

- vdref, and vqref are the *d*-axis and
  *q*-axis reference voltages, respectively.
- idref, and iqref are the *d*-axis and
  *q*-axis reference currents, respectively.
- id and iq are the *d*-axis and
  *q*-axis currents, respectively.
- *Kp\_id*, and
  *Kp\_iq* are the
  proportional gains for the *d*-axis and
  *q*-axis controllers, respectively.
- *Ki\_id* and
  *Ki\_iq* are the integral
  gains for the *d*-axis and *q*-axis
  controllers, respectively.
- *vd\_FF*, and
  *vq\_FF* are the
  feedforward voltages for the *d*-axis and
  *q*-axis, respectively. The feedforward voltages
  are obtained from the machine mathematical equations and provided as
  inputs.
- *Ts*, is the sample time of the
  discrete controller.

### Voltage Saturation

Saturation is imposed when the stator voltage vector exceeds the voltage phase
limit *Vph\_max*:

vd2+vq2≤Vph\_max,

where *vd*, and
*vq* are the
*d*-axis and *q*-axis voltages, respectively.

In the case of axis prioritization, the voltages
*v1* and
*v2* are introduced, where:

- For *d*-axis prioritization *—
  v1 = vd*
  and *v2 =
  vq*.
- For *q*-axis prioritization*—**v1 =
  vq* and
  *v2 =
  vd*.

The constrained (saturated) voltages v1sat and v2sat are obtained as:

v1sat=min(max(v1unsat,−Vph\_max),Vph\_max)

and

v2sat=min(max(v2unsat,−V2\_max),V2\_max),

where:

- v1unsat and v2unsat are the unconstrained (unsaturated) voltages.
- *v2\_max* is the maximum value
  of *v2* that does not exceed the
  voltage phase limit. The equation that define
  *v2\_max* is v2\_max=(Vph\_max)2−(v1sat)2.

In the case of *d*-*q* equivalence, the direct
and quadrature axes have the same priority, and the constrained voltages are:

vdsat=min(max(vdunsat,−Vd\_max),Vd\_max)

and

vqsat=min(max(vqunsat,−Vq\_max),Vq\_max),

where:

Vd\_max=Vph\_max|vdunsat|(vdunsat)2+(vqunsat)2

and

Vq\_max=Vph\_max|vqunsat|(vdunsat)2+(vqunsat)2.

### Integral Anti-Windup

An anti-windup mechanism is employed to avoid the saturation of the integrator
output. In such a situation, the integrator gains become:

Ki\_id+Kaw\_id(vdsat−vdunsat)

and

Ki\_iq+Kaw\_iq(vqsat−vqunsat),

where *Kaw\_id*,
*Kaw\_iq*, and
*Kaw\_if* are the anti-windup gains
for the *d*-axis, *q*-axis, and field controllers,
respectively.

### Assumptions and Limitations

- The plant model for the direct and quadrature axes can be approximated
  with a first-order system.
