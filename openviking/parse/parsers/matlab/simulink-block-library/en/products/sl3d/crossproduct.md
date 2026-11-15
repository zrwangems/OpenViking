---
type: simulink-block
title: 'Cross Product'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'crossproduct'
documentation_source_path: 'crossproduct.html'
language: en
---

# Cross Product

## Ports

### Input

### **Port 1 (a)** — 3-element vector vector

Input vector a→, where the elements represent the magnitude of the
vector parallel to the *x*, *y*, and
*z* coordinate axes.

**Data Types:** `double`

### **Port 2 (b)** — 3-element vector vector

Input vector b→, where the elements represent the magnitude of the
vector parallel to the *x*, *y*, and
*z* coordinate axes.

**Data Types:** `double`
### Output

### **Port 1 (y)** — Resultant vector vector

Output vector y→=a→×b→, which is orthogonal to a→ and b→.

**Data Types:** `double`

## Parameters

Not documented in R2025b.

## Libraries

Simulink 3D Animation / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2006a**

### R2023b: To be removed

The `Cross Product` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB® and Simulink® with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Cross product of two 3-D vectors

Return the cross product–or vector product–of two 3-by-1 vectors. Each input is a
vector of the form a1i^+a2j^+a3k^ where *i*, *j*, and
*k* are unit vectors parallel to the *x*,
*y*, and *z* coordinate axes. The output vector y→=a→×b→ is a 3 element vector orthogonal to the input vectors a→ and b→.
