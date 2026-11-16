---
type: simulink-block
title: 'Rotation Between 2 Vectors'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'rotationbetween2vectors'
documentation_source_path: 'rotationbetween2vectors.html'
language: en
---

# Rotation Between 2 Vectors

## Ports

### Input

### **Port 1** — Input signal 3-element vector

The input signal is a 3-element vector whose elements correspond to
its magnitudes along the i^,j^,k^ unit vectors, respectively.

**Data Types:** `double`

### **Port 2** — Input signal 3-element vector

The input signal is a 3- element vector whose elements correspond to
its magnitudes along the i^,j^,k^ unit vectors, respectively.

**Data Types:** `double`
### Output

### **Output 1** — Axis-Angle rotation 4-element vector

The output of the block is an axis-angle representation of the
rotation needed to transform the first input vector to the second input
vector.

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

The `Rotation Between 2 Vectors` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB® and Simulink® with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Virtual world rotation between two 3-D vectors

The Rotation Between 2 Vectors takes the input of two 3-by-1 vectors
and returns a virtual world rotation (specified as a 4-element vector defining the axis
and angle) that is needed to transform the first input vector to the second input
vector.
