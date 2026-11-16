---
type: simulink-block
title: 'VR to MATLAB Coordinates'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrtomatlabcoordinates'
documentation_source_path: 'vrtomatlabcoordinates.html'
language: en
---

# VR to MATLAB Coordinates

## Ports

### Input

### **VR** — Coordinates in the Virtual World coordinate system 3-element vector

Coordinates of a point in VRML notation, specified as a 3-element row
vector.

**Data Types:** `single` | `double`
### Output

### **M** — Coordinates in the MATLAB coordinate system 3-element vector

Coordinates of a point in MATLAB notation, returned as a 3-element row vector.

**Data Types:** `single` | `double`

## Parameters

Not documented in R2025b.

## Libraries

Simulink 3D Animation / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

### R2023b: To be removed

The `VR to MATLAB Coordinates` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB and Simulink® with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Convert VR coordinates to MATLAB coordinates

The VR to MATLAB Coordinates block converts a point with coordinates in
the Virtual World coordinate system (Znear) to the MATLAB® coordinate system (Zup).

The following relation holds between the two coordinate systems:

[*xm*,
*ym*,
*zm*] =
[*xv*,
-*zv*,
*yv*]

where MATLAB coordinates are denoted with the *m* subscript and
Virtual World coordinates are denoted with the *v* subscript.
