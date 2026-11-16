---
type: simulink-block
title: 'Inverse Decoupled Transform (Six-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'inversedecoupledtransformsixphase'
documentation_source_path: 'ref/inversedecoupledtransformsixphase.html'
language: en
---

# Inverse Decoupled Transform (Six-Phase)

## Ports

### Input

### **dqz1z2o1o2** — Direct, Quadrature, *z1*, *z2*, *o1*, and *o2* components vector

Direct, quadrature, *z1*-axis,
*z2*-axis,
*o1*-axis, and
*o2*-axis components of
the system in the rotating reference frame, specified as a
vector.

**Data Types:** `single` | `double`

### **θelec** — Rotational angle scalar

Angular position of the rotating reference frame, specified as a
scalar.

**Data Types:** `single` | `double`
### Output

### **abc** — *a*-, *b*-, and *c*-phase components vector

Components of the three-phase system in
an *abc* reference frame, returned as a vector.

**Data Types:** `single` | `double`

### **xyz** — *x*-, *y*-, and *z*-phase components vector

Components of the three-phase system in
an *xyz* reference frame, returned as a vector.

**Data Types:** `single` | `double`

## Parameters

### **Phase-a axis alignment** — *dqz1z2o1o2* reference frame alignment `Q-axis` (default) | `D-axis`

Whether to align the *a*-phase vector of the *abc*
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

Implement dqz 1 z 2 o 1 o 2 to abc and xyz transform

The Inverse Decoupled Transform (Six-Phase) block converts the direct,
quadrature, *z1*,
*z2*,
*o1*, and
*o2* components in a rotating reference
frame to the components of a six-phase system in the *abc* and
*xyz* reference frame. The three-phase systems
*abc* and *xyz* are spatially shifted by 30
electrical degrees.

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
- Offset=0,     d−axis alignment−π2,    q−axis alignment

### Equations

The Inverse Decoupled Transform (Six-Phase) block implements the
transform as

[abcxyz]=[cosθ−sinθ1010cos(θ−2π3)−sin(θ−2π3)−12−3210cos(θ+2π3)−sin(θ+2π3)−123210cos(θ−π6)−sin(θ−π6)−321201cos(θ−5π6)−sin(θ−5π6)321201cos(θ+π2)−sin(θ+π2)0−101][dqz1z2o1o2]

The
*z1*–*z2*
and
*o1*–*o2*
pairs do not form a rotating magnetic potential. They are generalized zero-sequence
components.
