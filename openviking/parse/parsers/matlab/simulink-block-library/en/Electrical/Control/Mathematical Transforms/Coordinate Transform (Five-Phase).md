---
type: simulink-block
title: 'Coordinate Transform (Five-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'coordinatetransformfivephase'
documentation_source_path: 'ref/coordinatetransformfivephase.html'
language: en
---

# Coordinate Transform (Five-Phase)

## Ports
```yaml
ports:
- name: abcde
  summary: '*a*-, *b*-, *c*-, *d*-, and *e*-phase components vector'
  direction: input
  data_types: single | double
- name: θelec
  summary: Rotational angle scalar
  direction: input
  data_types: single | double
- name: dqxy0
  summary: Direct, quadrature, *x*, *y*, and zero components vector
  direction: output
  data_types: single | double
```

### Input

### **abcde** — *a*-, *b*-, *c*-, *d*-, and *e*-phase components vector

Components of the five-phase system in
an *abcde* reference frame, specified as a
vector.

**Data Types:** `single` | `double`

### **θelec** — Rotational angle scalar

Angular position of the rotating reference frame, specified as a
scalar.

**Data Types:** `single` | `double`
### Output

### **dqxy0** — Direct, quadrature, *x*, *y*, and zero components vector

Direct, quadrature, *x*-axis,
*y*-axis, and zero components of the system in the
rotating reference frame, returned as a vector.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Phase-a axis alignment
  summary: '*dqxy0* reference frame alignment Q-axis (default) | D-axis'
  group: ''
```

### **Phase-a axis alignment** — *dqxy0* reference frame alignment `Q-axis` (default) | `D-axis`

Whether to align the *a*-phase vector of the *abcde*
reference frame to the *d*-axis or
*q*-axis of the rotating reference frame.
## Libraries

Simscape / Electrical / Control / Mathematical Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Implement abcde to dqxy0 transform

The Coordinate Transform (Five-Phase) block converts the time-domain
components of a five-phase system in an *abcde* reference frame to
direct, quadrature, *x*, *y*, and zero components in a
rotating reference frame.

You can configure the block to align the phase *a*-axis of the five-phase
system to either the *d*-axis or *q*-axis of the
rotating reference frame at time *t* = 0.

*θ = ωt + Offset* is the angle between the *a* and
*q* axes for the *q*-axis alignment or the angle
between the *a* and *d* axes for the
*d*-axis alignment, where:

- *ω* is the rotational speed of the rotational reference
  frame.
- *t* is the time, in s, from the initial alignment.
- Offset=π2,d−axis alignment0,q−axis alignment

### Equations

The Coordinate Transform (Five-Phase) block implements the
transform as

[dqxy0]=25[sinθsin(θ−2π5)sin(θ−4π5)sin(θ+4π5)sin(θ+2π5)cosθcos(θ−2π5)cos(θ−4π5)cos(θ+4π5)cos(θ+2π5)sinθsin(θ+4π5)sin(θ−2π5)sin(θ+2π5)sin(θ−4π5)cosθcos(θ+4π5)cos(θ−2π5)cos(θ+2π5)cos(θ−4π5)1212121212][abcde]
