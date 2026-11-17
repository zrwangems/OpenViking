---
type: simulink-block
title: 'Quaternion Rotation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternionrotation'
documentation_source_path: 'quaternionrotation.html'
language: en
---

# Quaternion Rotation

## Ports
```yaml
ports:
- name: q
  summary: Quaternion quaternion | vector
  direction: input
  data_types: double
- name: vec
  summary: Initial vector vector | vector of vectors
  direction: input
  data_types: double
- name: vec_rot
  summary: Final quaternion rotated quaternion | vector of rotated quaternions
  direction: output
  data_types: double
```

### Input

### **q** — Quaternion quaternion | vector

Quaternions in the form of
[*q*0,
*r*0, ...,
*q*1,
*r*1, ... ,
*q*2,
*r*2, ... ,
*q*3,
*r*3, ...], specified as a
quaternion or vector of quaternions.

**Data Types:** `double`

### **vec** — Initial vector vector | vector of vectors

Initial vector or vector of vectors in the form of
[*v*1,
*u*1, ... ,
*v*2,
*u*2, ... ,
*v*3,
*u*3, ...].

**Data Types:** `double`
### Output

### **vec\_rot** — Final quaternion rotated quaternion | vector of rotated quaternions

Final vector or vector of rotated vectors.

**Data Types:** `double`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Aerospace Blockset / Utilities / Math Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Rotate vector by quaternion

The Quaternion Rotation block calculates the resulting vector following the
passive rotation of initial vector `vec` by quaternion
`q` and returns a final vector, the rotated vector or vector of
rotated vectors. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. This
block normalizes all quaternion inputs. For the equations used for the quaternion,
initial vector, and final vector, see Algorithms.
