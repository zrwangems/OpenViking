---
type: simulink-block
title: 'SM Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smcurrentcontroller'
documentation_source_path: 'ref/smcurrentcontroller.html'
language: en
---

# SM Current Controller

## Ports
```yaml
ports:
- name: idqfRef
  summary: Reference currents, A vector
  direction: input
  data_types: single | double
- name: idqf
  summary: Measured currents, A vector
  direction: input
  data_types: single | double
- name: vdqFF
  summary: Purpose, V vector
  direction: input
  data_types: single | double
- name: VphMax
  summary: Maximum phase voltage, V scalar
  direction: input
  data_types: single | double
- name: VfMax
  summary: Maximum field voltage, V scalar
  direction: input
  data_types: single | double
- name: Reset
  summary: External reset scalar
  direction: input
  data_types: single | double
- name: vdqfRef
  summary: Reference voltages, V vector
  direction: output
  data_types: single | double
```

### Input

### **idqfRef** — Reference currents, A vector

Reference d-q and field currents for control of synchronous
motor.

**Data Types:** `single` | `double`

### **idqf** — Measured currents, A vector

Actual d-q and field axis currents of controlled synchronous
motor.

**Data Types:** `single` | `double`

### **vdqFF** — Purpose, V vector

Feedforward pre-control voltages.

**Data Types:** `single` | `double`

### **VphMax** — Maximum phase voltage, V scalar

Maximum allowable voltage in each phase.

**Data Types:** `single` | `double`

### **VfMax** — Maximum field voltage, V scalar

Maximum allowable field voltage.

**Data Types:** `single` | `double`

### **Reset** — External reset scalar

External reset signal (rising edge) for integrators.

**Data Types:** `single` | `double`
### Output

### **vdqfRef** — Reference voltages, V vector

Reference d-q and field voltages for control of synchronous
motor.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | positive scalar
  group: ''
- name: Discretization sample time
  summary: Block discretization sample time 0.001 (default) | -1 or positive number
  group: ''
- name: Axis prioritization
  summary: Axis prioritization for voltage limiter q-axis (default) | d-axis | d-q equivalence
  group: ''
- name: Enable zero cancellation
  summary: Feedforward zero-cancellation off (default) | on
  group: ''
- name: Enable pre-control voltage
  summary: Pre-control voltage on (default) | off
  group: ''
- name: D-axis current proportional gain
  summary: D-axis proportional gain 1 (default) | positive number
  group: ''
- name: D-axis current integral gain
  summary: D-axis integral gain 100 (default) | positive number
  group: ''
- name: D-axis current anti-windup gain
  summary: D-axis anti-windup gain 1 (default) | positive number
  group: ''
- name: Q-axis current proportional gain
  summary: Q-axis proportional gain 1 (default) | positive number
  group: ''
- name: Q-axis current integral gain
  summary: Q-axis integral gain 100 (default) | positive number
  group: ''
- name: Q-axis current anti-windup gain
  summary: Q-axis anti-windup gain 1 (default) | positive number
  group: ''
- name: Field current proportional gain
  summary: Field current proportional gain 9 (default) | positive number
  group: ''
- name: Field current integral gain
  summary: Field current integral gain 350 (default) | positive number
  group: ''
- name: Field current anti-windup gain
  summary: Field current anti-windup gain 1 (default) | positive number
  group: ''
```

#### General

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

### **Discretization sample time** — Block discretization sample time `0.001` (default) | `-1` or positive number

Specify the discretization sample time when zero-cancellation is active
and sample time is set to -1 (e.g., when the block is used inside a
triggered subsystem).

### **Axis prioritization** — Axis prioritization for voltage limiter `q-axis` (default) | `d-axis` | `d-q equivalence`

Prioritize or maintain ratio between d and q axes when block limits
voltage.

### **Enable zero cancellation** — Feedforward zero-cancellation `off` (default) | `on`

Enable or disable zero-cancellation on the feedforward path.

### **Enable pre-control voltage** — Pre-control voltage `on` (default) | `off`

Enable or disable pre-control voltage.

#### d-q Control

### **D-axis current proportional gain** — D-axis proportional gain `1` (default) | positive number

Proportional gain of PI controller used for direct-axis current
control.

### **D-axis current integral gain** — D-axis integral gain `100` (default) | positive number

Integrator gain of PI controller used for direct-axis current
control.

### **D-axis current anti-windup gain** — D-axis anti-windup gain `1` (default) | positive number

Anti-windup gain of PI controller used for direct-axis current
control.

### **Q-axis current proportional gain** — Q-axis proportional gain `1` (default) | positive number

Proportional gain of PI controller used for quadrature-axis current
control.

### **Q-axis current integral gain** — Q-axis integral gain `100` (default) | positive number

Integrator gain of PI controller used for quadrature-axis current
control.

### **Q-axis current anti-windup gain** — Q-axis anti-windup gain `1` (default) | positive number

Anti-windup gain of PI controller used for quadrature-axis current
control.

#### Field Control

### **Field current proportional gain** — Field current proportional gain `9` (default) | positive number

Proportional gain of PI controller used for field current control.

### **Field current integral gain** — Field current integral gain `350` (default) | positive number

Integrator gain of PI controller used for field current control.

### **Field current anti-windup gain** — Field current anti-windup gain `1` (default) | positive number

Anti-windup gain of PI controller used for field current control.
## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time synchronous machine current PI controller

The SM Current Controller block implements a discrete time PI-based
synchronous machine (SM) current controller in the rotor
*d*-*q* reference frame.

### Defining Equations

The block is discretized using the backward Euler method due to its first-order
simplicity and its stability.

Three PI current controllers implemented in the rotor reference frame produce the
reference voltage vector:

vdref=(Kp\_id+Ki\_idTszz−1)(idref−id)+vd\_FF,

vqref=(Kp\_iq+Ki\_iqTszz−1)(iqref−iq)+vq\_FF,

and

vfref=(Kp\_if+Ki\_ifTszz−1)(ifref−if),

where:

- vdref, vqref, and vfref are the *d*-axis,
  *q*-axis, and field reference voltages,
  respectively.
- idref, vqref, and ifref are the *d*-axis,
  *q*-axis, and field reference currents,
  respectively.
- id, iq, and if are the *d*-axis,
  *q*-axis, and field currents,
  respectively.
- *Kp\_id*,
  *Kp\_iq*, and
  *Kp\_if* are the
  proportional gains for the *d*-axis,
  *q*-axis and field controllers,
  respectively.
- *Ki\_id*,
  *Ki\_iq*, and
  *Ki\_if* are the integral
  gains for the *d*-axis, *q*-axis
  and field controllers, respectively.
- *vd\_FF*, and
  *vq\_FF* are the
  feedforward voltages for the *d*-axis and
  *q*-axis, respectively, obtained from the machine
  mathematical equations and provided as inputs.
- *Ts*, is the sample time of the
  discrete controller.

Using PI control results in a zero in the closed-loop transfer function which can
be canceled by introducing a zero-cancelation block in the feedforward path. The
zero cancellation transfer functions in discrete time are:

GZC\_id(z)=TsKi\_idKp\_idz+(Ts−Kp\_idKi\_idKp\_idKi\_id),

GZC\_iq(z)=TsKi\_iqKp\_iqz+(Ts−Kp\_iqKi\_iqKp\_iqKi\_iq),

and

GZC\_if(z)=TsKi\_ifKp\_ifz+(Ts−Kp\_ifKi\_ifKp\_ifKi\_if).

Saturation must be imposed when the stator voltage vector exceeds
the voltage phase limit *Vph\_max*:

vd2+vq2≤Vph\_max,

where *vd*, and
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

v1sat=min(max(v1unsat,−Vph\_max),Vph\_max),

and

v2sat=min(max(v2unsat,−V2\_max),V2\_max),

where:

- v1unsat and v2unsat are the unconstrained (unsaturated) voltages.
- *v2\_max* is the maximum value
  of *v2* that does not exceed the
  voltage phase limit, given by v2\_max=(Vph\_max)2−(v1sat)2.

In the case that the direct and quadrature axes have the same priority (d-q
equivalence) the constrained voltages are obtained as follows:

vdsat=min(max(vdunsat,−Vd\_max),Vd\_max),

and

vqsat=min(max(vqunsat,−Vq\_max),Vq\_max),

where

Vd\_max=Vph\_max|vdunsat|(vdunsat)2+(vqunsat)2,

and

Vq\_max=Vph\_max|vqunsat|(vdunsat)2+(vqunsat)2.

The constrained (saturated) field voltage vfsat is limited according to the maximum admissible value:

vfsat=min(max(vfunsat,−Vf\_max),Vf\_max),

where:

- vfunsat is the unconstrained (unsaturated) field
  voltage.
- *Vf\_max* is the maximum
  allowable field voltage.

An anti-windup mechanism is employed to avoid saturation of integrator output. In
such a situation, the integrator gains become:

Ki\_id+Kaw\_id(vdsat−vdunsat),

Ki\_iq+Kaw\_iq(vqsat−vqunsat),

and

Ki\_if+Kaw\_if(vfsat−vfunsat),

where *Kaw\_id*,
*Kaw\_iq*, and
*Kaw\_if* are the anti-windup gains
for the *d*-axis, *q*-axis and field
controllers, respectively.

### Assumptions

- The plant model for direct and quadrature axis can be approximated
  with a first order system.
- This control solution is used only for synchronous motors with
  sinusoidal flux distribution and field windings.
