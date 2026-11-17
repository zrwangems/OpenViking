---
type: simulink-block
title: 'PMSM Current Controller with Pre-Control'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control'
documentation_page: 'pmsmcurrentcontrollerwithprecontrol'
documentation_source_path: 'ref/pmsmcurrentcontrollerwithprecontrol.html'
language: en
---

# PMSM Current Controller with Pre-Control

## Ports
```yaml
ports:
- name: idqRef
  summary: Reference currents vector
  direction: input
  data_types: single | double
- name: idq
  summary: Measured currents vector
  direction: input
  data_types: single | double
- name: wElectrical
  summary: Measured electrical velocity vector
  direction: input
  data_types: single | double
- name: VphMax
  summary: Maximum phase voltage scalar
  direction: input
  data_types: single | double
- name: Reset
  summary: External reset scalar
  direction: input
  data_types: single | double
- name: vdqRef
  summary: Reference voltages vector
  direction: output
  data_types: single | double
```

### Input

### **idqRef** — Reference currents vector

Desired *d*- and *q*-axis
currents for control of a PMSM, in A.

**Data Types:** `single` | `double`

### **idq** — Measured currents vector

Actual *d*- and *q*-axis
currents of the controlled PMSM, in A.

**Data Types:** `single` | `double`

### **wElectrical** — Measured electrical velocity vector

Rotor electrical velocity used for feedforward pre-control, in
rad/s.

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
```yaml
parameters:
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
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | -1 or positive number
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
- name: D-axis current vector, id (A)
  summary: D-axis current breakpoint vector [-200,0,200]A (default) | monotonically increasing vector
  group: ''
- name: Q-axis current vector, iq (A)
  summary: Q-axis current breakpoint vector [-200,0,200]A (default) | monotonically increasing vector
  group: ''
- name: Ld matrix, Ld(id,iq) (H)
  summary: D-axis inductance lookup data 0.0002 * ones(3, 3)H (default) | positive matrix
  group: ''
- name: Lq matrix, Lq(id,iq) (H)
  summary: Q-axis inductance lookup data 0.0002 * ones(3, 3)H (default) | positive matrix
  group: ''
- name: Permanent magnet flux linkage matrix, PM(id,iq) (Wb)
  summary: Flux linkage lookup data 0.04 * ones(3, 3)Wb (default) | real matrix
  group: ''
```

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

Prioritize or maintain the ratio between *d*- and
*q*-axes when the block limits voltage.

### **Enable zero cancellation** — Feedforward zero-cancellation `off` (default) | `on`

Enable or disable zero-cancellation on the feedforward path.

### **Enable pre-control voltage** — Pre-control voltage `on` (default) | `off`

Enable or disable pre-control voltage.

#### Pre-Control Parameters

### **D-axis current vector, id (A)** — D-axis current breakpoint vector `[-200,0,200]``A` (default) | monotonically increasing vector

Direct-axis current vector used in the lookup tables for parameters
determination. For constant machine parameters, do not change the
default.

### **Q-axis current vector, iq (A)** — Q-axis current breakpoint vector `[-200,0,200]``A` (default) | monotonically increasing vector

Quadrature-axis current vector used in the lookup tables used to determine
parameters. For constant machine parameters, do not change the
default.

### **Ld matrix, Ld(id,iq) (H)** — D-axis inductance lookup data `0.0002 * ones(3, 3)``H` (default) | positive matrix

*Ld* matrix used as lookup-table
data. For constant machine parameters change only the constant factor, for
example, *Ld* \* `ones(3,
3)`.

### **Lq matrix, Lq(id,iq) (H)** — Q-axis inductance lookup data `0.0002 * ones(3, 3)``H` (default) | positive matrix

*Lq* matrix used as lookup-table
data. For constant machine parameters change only the constant factor, e.g.,
*Lq* \* `ones(3,
3)`.

### **Permanent magnet flux linkage matrix, PM(id,iq) (Wb)** — Flux linkage lookup data `0.04 * ones(3, 3)``Wb` (default) | real matrix

Permanent magnet flux linkage matrix used in the lookup table. For
constant machine parameters change only the constant factor, for example
*psim* \* `ones(3, 3)`.
## Libraries

Simscape / Electrical / Control / PMSM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time permanent magnet synchronous machine current controller with pre-control

The PMSM Current Controller with Pre-Control block implements a
discrete-time PI-based permanent magnet synchronous machine (PMSM) current controller in
the rotor *d*-*q* reference frame with internal
feedforward pre-control.

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
- *Ts* is the sample time of the
  discrete controller.
- *vd\_FF* and
  *vq\_FF* are the
  feedforward voltages for the *d*-axis and
  *q*-axis, respectively.

The feedforward voltages are obtained from the machine mathematical
equations:

vd\_FF=−ωeLqiqref,

and

vq\_FF=ωe(Ldidref+ψm),

where:

- *ωe* is the rotor electrical
  velocity.
- *Ld* and
  *Lq* are the
  *d*-axis and *q*-axis
  inductances, respectively.
- *ψm* is the permanent magnet
  flux linkage.

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
equivalence), the constrained voltages are obtained as follows:

vdsat=min(max(vdunsat,−Vd\_max),Vd\_max)

and

vqsat=min(max(vqunsat,−Vq\_max),Vq\_max),

where:

Vd\_max=Vph\_max|vdunsat|(vdunsat)2+(vqunsat)2

and

Vq\_max=Vph\_max|vqunsat|(vdunsat)2+(vqunsat)2.

### Integral Anti-Windup

An anti-windup mechanism is employed to avoid saturation of integrator output. In
such a situation, the integrator gains become:

Ki\_id+Kaw\_id(vdsat−vdunsat)

and

Ki\_iq+Kaw\_iq(vqsat−vqunsat),

where *Kaw\_id*,
*Kaw\_iq*, and
*Kaw\_if* are the anti-windup gains
for the *d*-axis, *q*-axis, and field
controllers, respectively.

### Assumptions

- The plant model for direct and quadrature axis can be approximated
  with a first-order system.
- This control solution is used only for permanent magnet synchronous
  motors with sinusoidal flux distribution and field windings.
