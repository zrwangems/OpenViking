---
type: simulink-block
title: 'Symmetric Inertia Tensor'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Mass Properties'
documentation_page: 'symmetricinertiatensor'
documentation_source_path: 'symmetricinertiatensor.html'
language: en
---

# Symmetric Inertia Tensor

## Ports
```yaml
ports:
- name: Ixx
  summary: Moment of inertia scalar
  direction: input
  data_types: double
- name: Ixy
  summary: Product of inertia in *xy* plane scalar
  direction: input
  data_types: double
- name: Ixz
  summary: Product of inertia in *xz* plane scalar
  direction: input
  data_types: double
- name: Iyy
  summary: Moment of inertia about *y*-axis scalar
  direction: input
  data_types: double
- name: Iyz
  summary: Product of inertia in *yz* plane scalar
  direction: input
  data_types: double
- name: Izz
  summary: Moment of inertia about *z*-axis scalar
  direction: input
  data_types: double
- name: I
  summary: Inertia tensor 3-by-3 matrix
  direction: output
  data_types: double
```

### Input

### **Ixx** — Moment of inertia scalar

Moment of inertia about the *x*-axis, specified as
a scalar.

**Data Types:** `double`

### **Ixy** — Product of inertia in *xy* plane scalar

Product of inertia in the *xy* plane, specified as a
scalar.

**Data Types:** `double`

### **Ixz** — Product of inertia in *xz* plane scalar

Product of inertia in the *xz* plane, specified as a
scalar.

**Data Types:** `double`

### **Iyy** — Moment of inertia about *y*-axis scalar

Moment of inertia about the *y*-axis, specified as a
scalar.

**Data Types:** `double`

### **Iyz** — Product of inertia in *yz* plane scalar

Product of inertia in the *yz* plane, specified as a
scalar.

**Data Types:** `double`

### **Izz** — Moment of inertia about *z*-axis scalar

Moment of inertia about the *z*-axis, specified as a
scalar.

**Data Types:** `double`
### Output

### **I** — Inertia tensor 3-by-3 matrix

Symmetric inertia tensor, returned as a 3-by-3 matrix.

**Data Types:** `double`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Aerospace Blockset / Mass Properties

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Create inertia tensor from moments and products of inertia

The Symmetric Inertia Tensor block creates an inertia tensor
from moments and products of inertia. Each input corresponds to an element of the
tensor.

The inertia tensor has the form of:

Inertia=[Ixx−Ixy−Ixz−IxyIyy−Iyz−Ixz−IyzIzz]
