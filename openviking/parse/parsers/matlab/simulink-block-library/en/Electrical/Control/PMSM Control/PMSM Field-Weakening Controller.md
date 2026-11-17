---
type: simulink-block
title: 'PMSM Field-Weakening Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control'
documentation_page: 'pmsmfieldweakeningcontroller'
documentation_source_path: 'ref/pmsmfieldweakeningcontroller.html'
language: en
---

# PMSM Field-Weakening Controller

## Ports
```yaml
ports:
- name: idqRef
  summary: Reference currents vector
  direction: input
  data_types: single | double
- name: vdq
  summary: Voltages vector
  direction: input
  data_types: single | double
- name: VphMax
  summary: Maximum phase voltage scalar
  direction: input
  data_types: single | double
- name: idqRefFW
  summary: Field-weakening reference currents vector
  direction: output
  data_types: single | double
```

### Input

### **idqRef** — Reference currents vector

Desired *d*- and *q*-axis currents
for control of permanent magnet synchronous motor, in A.

**Data Types:** `single` | `double`

### **vdq** — Voltages vector

Direct and quadrature axis voltages of permanent magnet synchronous
motor, in V.

**Data Types:** `single` | `double`

### **VphMax** — Maximum phase voltage scalar

Maximum allowable voltage in each phase, in V.

**Data Types:** `single` | `double`
### Output

### **idqRefFW** — Field-weakening reference currents vector

Field-weakening reference direct and quadrature axis currents, in
A.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Modulation index threshold
  summary: Modulation index threshold 1 (default) | positive number
  group: ''
- name: Field-weakening controller integral gain
  summary: Integral gain 100 (default) | positive number
  group: ''
- name: Integral anti-windup gain
  summary: Anti-windup gain 10 (default) | positive number
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | -1 or positive number
  group: ''
```

### **Modulation index threshold** — Modulation index threshold `1` (default) | positive number

Reference modulation index.

### **Field-weakening controller integral gain** — Integral gain `100` (default) | positive number

Integrator gain of the field-weakening controller.

### **Integral anti-windup gain** — Anti-windup gain `10` (default) | positive number

Anti-windup gain of the field-weakening controller.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `-1` or positive number

Sample time for the block (-1 for inherited). If you use this block inside
a triggered subsystem, set the sample time to `-1`. If you
use this block in a continuous variable-step model, set the sample time
explicitly.
## Libraries

Simscape / Electrical / Control / PMSM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Permanent magnet synchronous machine field-weakening controller

The PMSM Field-Weakening Controller block implements a field-weakening
controller for a permanent magnet synchronous machine (PMSM).

Use this block to enforce phase voltage constraints on a current-controlled PMSM. The
block decreases the PMSM phase voltage by adjusting the angle of the reference current
vector when the voltage vector magnitude exceeds its limit. The block does not adjust
the amplitude of the current vector.

You can use this block as part of a PMSM control system:

- Use the zero *d*-axis control technique to generate an
  unconstrained current reference vector to drive the PMSM. You can implement
  this strategy with the PMSM
  Current Reference Generator block.
- Use this block to adjust the angle of the current reference vector in
  order to satisfy voltage phase constraints.
- Use a PMSM
  Current Controller to generate a voltage reference vector to
  drive the PMSM.

### Equations

An internal integral controller outputs a factor *β∈[0,1]*, which
is determined by how closely the required stator voltage approaches the saturated
voltage value at any instant in time:

- When the required stator voltage exceeds the limit,
  *β* tends to 0, decreasing the
  *q*-axis current.
- When the required stator voltage is within its limit,
  *β* tends to 1 and the angle remains
  unchanged.

This diagram shows the structure of the field-weakening controller.

In the diagram, you provide the modulation index threshold
*Mth* as an input parameter to the
block, and the block computes the modulation index *M* as the ratio
between the actual phase voltage and the maximum available phase voltage
*Vph\_max*:

M=vd2+vq2Vph\_max,

where *vd* and
*vq* are the
*d*-axis and *q*-axis components of the
voltage vector.
