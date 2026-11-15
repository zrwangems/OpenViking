---
type: simulink-block
title: 'Vector Control Reference'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Control Reference'
documentation_page: 'vectorcontrolreference'
documentation_source_path: 'ref/vectorcontrolreference.html'
language: en
---

# Vector Control Reference

## Ports

### Input

### **magref** — Magnitude of reference vector scalar

Magnitude of the reference voltage, current, or flux vector that you provide as an
input to the block.

**Data Types:** `single` | `double` | `fixed point`

### **θe** — Electrical position of reference vector scalar

Electrical position of the reference voltage, current, or flux vector that you
provide as an input to the block.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **dref** — *d*-axis component of reference vector scalar

Reference voltage, current, or flux vector component along the direct axis of the
rotating *dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **qref** — *q*-axis component of reference vector scalar

Reference voltage, current, or flux vector component along the quadrature axis of
the rotating *dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Alpha (phase-a) axis alignment** — *dq* reference frame alignment `D-axis` (default) | `Q-axis`

Align either the *d*- or *q*-axis of the rotating
reference frame to the *α*-axis of the stationary reference
frame.

### **Theta units** — Unit of input position value `Per-unit` (default) | `Radians` | `Degrees`

Unit of the input electrical position of the reference voltage, current, or flux
vector.

### **Number of data points for trigonometric lookup table** — Size of lookup table array `1024` (default) | scalar

Size of the lookup table array.

## Libraries

Motor Control Blockset / Controls / Control Reference

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Compute d and q axis components of reference vector

The Vector Control Reference block calculates the *d*-axis
and *q*-axis components of the reference voltage, current, or flux vector
that you provide as an input to the block.

The block accepts magnitude and position of the reference vector as inputs. The block
outputs the reference vector components along the direct and quadrature axes of the rotating
*dq* reference frame.

### Equations

The block uses these equations to compute the *d*-axis and
*q*-axis vector component outputs.

dref=magref×cosθe

qref=magref×sinθe

where:

- dref is the *d*-axis component of the reference
  vector.
- qref is the *q*-axis component of the reference
  vector.
- magref is the magnitude of the reference vector.
- θe is the electrical position of the reference vector.
