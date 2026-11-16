---
type: simulink-block
title: 'd-q Voltage Limiter'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Protection\u200b'
documentation_page: 'dqvoltagelimiter'
documentation_source_path: 'ref/dqvoltagelimiter.html'
language: en
---

# d-q Voltage Limiter

## Ports

### Input

### **vdRefUnsat** — *vdunsat* scalar

Unsaturated direct-axis reference voltage.

**Example:** Example

**Data Types:** `single` | `double`

### **VqRefUnsat** — *vqunsat* scalar

Unsaturated quadrature-axis reference voltage.

**Example:** Example

**Data Types:** `single` | `double`

### **VphMax** — *Vph\_max* scalar

Maximum phase voltage.

**Data Types:** `single` | `double`
### Output

### **vdRef** — *vdsat* scalar

Saturated direct-axis reference voltage.

**Data Types:** `single` | `double`

### **vqRef** — *vdsat* scalar

Saturated quadrature-axis reference voltage.

**Example:** Example

**Data Types:** `single` | `double`

## Parameters

### **Axis prioritization** — Prioritize the *d*- or *q* axis `Q-axis` (default) | `D-axis` | `D-Q equivalence`

Prioritize the direct-axis, the quadrature-axis, or neither axis.

### **Sample time (-1 for inherited)** — Sampling interval `-1` (default) | default value or a positive number

Time interval between samples. If the block is
inside a triggered subsystem, inherit the sample time by setting this
parameter to `-1`. If this block is in a continuous
variable-step model, specify the sample time explicitly. For more
information, see What Is Sample Time? and
Specify Sample Time.

## Libraries

Simscape / Electrical / Control / Protection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Limit voltage in the rotor direct-quadrature reference frame

The d-q Voltage Limiter block implements a voltage limiter in the rotor
direct-quadrature (*d*-*q*) reference frame.

### Equations

The figure shows the circle that limits the
*d*-*q* voltage vector.

That is,

vd2+vq2≤Vph\_max

where:

- *vd* is the
  *d*-axis voltage.
- *vq* is the
  *q*-axis voltage.
- *Vph\_max* is the maximum phase
  voltage.

Three cases of voltage limiting are possible:

- *d*-axis prioritization
- *q*-axis prioritization
- *d*-*q* equivalence

If one axis is prioritized over the other axis, the constrained or saturated
voltages are defined as

v1sat=min(max(v1unsat,−Vph\_max),Vph\_max)

and

v2sat=min(max(v2unsat,−V2\_max),V2\_max),

where:

- v2\_max=(Vph\_max)2−(v1sat)2
- *v1* is voltage of the
  prioritized axis.
- *v2* is voltage of the
  nonprioritized axis.

If neither axis is prioritized, the constrained voltages are defined as

vdsat=min(max(vdunsat,−Vd\_max),Vd\_max)

and

vqsat=min(max(vqunsat,−Vq\_max),Vq\_max),

where:

- Vd\_max=Vph\_max|vdunsat|(vdunsat)2+(vqunsat)2
- Vq\_max=Vph\_max|vqunsat|(vdunsat)2+(vqunsat)2
