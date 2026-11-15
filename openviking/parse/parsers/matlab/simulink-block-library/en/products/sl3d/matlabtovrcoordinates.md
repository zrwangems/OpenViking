---
type: simulink-block
title: 'MATLAB to VR Coordinates'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'matlabtovrcoordinates'
documentation_source_path: 'matlabtovrcoordinates.html'
language: en
---

# MATLAB to VR Coordinates

## Ports

### Input

### **M** — Coordinates in MATLAB notation 3-element vector

Coordinates of a point in MATLAB notation, specified as a 3-element row vector.

**Data Types:** `single` | `double`
### Output

### **VR** — Coordinates in VRML notation 3-element vector

Coordinates of a point in VRML notation, returned as a 3-element row
vector.

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

The `MATLAB to VR Coordinates` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB and Simulink® with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Convert MATLAB coordinates to VR coordinates

The MATLAB to VR Coordinates block converts a point with coordinates in
the MATLAB® coordinate system to the VRML coordinate system.

The following relation holds between the two coordinate systems:

[*xm*,
*ym*,
*zm*] =
[*xv*,
*zv*,
-*yv*]

where MATLAB coordinates are denoted with the *m* subscript and
Virtual World coordinates are denoted with the *v* subscript.
