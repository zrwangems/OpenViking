---
type: simulink-block
title: 'Normalize Vector'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'normalizevector'
documentation_source_path: 'normalizevector.html'
language: en
---

# Normalize Vector

## Ports

### Input

### **Input 1** — Input signal vector

Vector of arbitrary size.

**Data Types:** `single` | `double`
### Output

### **Output 1** — Unit vector vector

Unit vector parallel to the vector provided by the input
signal.

**Data Types:** `single` | `double`

## Parameters

### **Maximum modulus to treat vector as zero** — Input signal threshold `0` (default)

The output is set to zeros if the modulus of the input is equal to or lower than this
value.

## Libraries

Simulink 3D Animation / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2006a**

### R2023b: To be removed

The `Normalize Vector` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB® and Simulink® with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Output unit vector parallel to input vector

Use the Normalize Vector block to obtain a unit vector parallel to a
given vector.
