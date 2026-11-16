---
type: simulink-block
title: 'Park Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'parktransform'
documentation_source_path: 'ref/parktransform.html'
language: en
---

# Park Transform

## Ports

### Input

### **abc** — *a*-, *b*-, and *c*-phase components vector

Components of the three-phase system in the *abc*
reference frame.

**Data Types:** `single` | `double`

### **θelec** — Rotational angle, radians scalar

Angular position of the rotating reference frame. The value of this
parameter is equal to the polar distance from the vector of the a-phase
in the *abc* reference frame to the initially aligned
axis of the *dq0* reference frame.

**Data Types:** `single` | `double`
### Output

### **dq0** — *d*-*q* axis and zero components vector

Direct-axis and quadrature-axis components and the zero component of
the system in the rotating reference frame.

**Data Types:** `single` | `double`

## Parameters

### **Power Invariant** — Power invariant transform off (default) | on

Option to preserve the active and reactive power of the
*abc* reference frame.

### **Phase-a axis alignment** — *dq0* reference frame alignment `Q-axis` (default) | `D-axis`

Align the *a*-phase vector of the *abc*
reference frame to the *d*- or *q*-axis of
the rotating reference frame.

## Libraries

Simscape / Electrical / Control / Mathematical Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Implement abc to dq0 transform

The Park Transform block converts the time-domain components of a
three-phase system in an *abc* reference frame to direct, quadrature,
and zero components in a rotating reference frame. The block can preserve the active and
reactive powers with the powers of the system in the *abc* reference
frame by implementing an invariant version of the Park transform. For a balanced system,
the zero component is equal to zero.

You can configure the block to align the *a*-axis of the three-phase
system to either the *d*- or *q*-axis of the rotating
reference frame at time, *t* = 0. The figures show the direction of the
magnetic axes of the stator windings in an *abc* reference frame and a
rotating *dq0* reference frame where:

- The *a*-axis and the *q*-axis are
  initially aligned.
- The *a*-axis and the *d*-axis are
  initially aligned.

In both cases, the angle *θ* =
*ω**t*, where:

- *θ* is the angle between the *a* and
  *q* axes for the *q*-axis alignment or
  the angle between the *a* and *d* axes for
  the *d*-axis alignment.
- *ω* is the rotational speed of the
  *d*-*q* reference frame.
- *t* is the time, in s, from the initial alignment.

The figures show the time-response of the individual components of equivalent balanced
*abc* and *dq0* for an:

- Alignment of the *a*-phase vector to the
  *q*-axis
- Alignment of the *a*-phase vector to the
  *d*-axis

### Equations

The Park Transform block implements the transform for an
*a*-phase to *q*-axis alignment as

[dq0]=23[sin(θ)sin(θ−2π3)sin(θ+2π3)cos(θ)cos(θ−2π3)cos(θ+2π3)121212][abc],

where:

- *a*, *b*, and *c*
  are the components of the three-phase system in the
  *abc* reference frame.
- *d* and *q* are the components of
  the two-axis system in the rotating reference frame.
- *0* is the zero component of the two-axis system in
  the stationary reference frame.

For a power invariant *a*-phase to *q*-axis
alignment, the block implements the transform using this equation:

[dq0]=23[sin(θ)sin(θ−2π3)sin(θ+2π3)cos(θ)cos(θ−2π3)cos(θ+2π3)121212][abc].

For an *a*-phase to *d*-axis
alignment, the block implements the transform using this equation:

[dq0]=23[cos(θ)cos(θ−2π3)cos(θ+2π3)−sin(θ)−sin(θ−2π3)−sin(θ+2π3)121212][abc].

The block implements a power invariant *a*-phase
to *d*-axis alignment as

[dq0]=23[cos(θ)cos(θ−2π3)cos(θ+2π3)−sin(θ)−sin(θ−2π3)−sin(θ+2π3)121212][abc].
