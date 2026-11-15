---
type: simulink-block
title: 'Viewpoint Direction to VRML Orientation'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'viewpointdirectiontovrorientation'
documentation_source_path: 'viewpointdirectiontovrorientation.html'
language: en
---

# Viewpoint Direction to VRML Orientation

## Ports

### Input

### **Input 1** — Viewpoint direction 3-element vector

Viewpoint direction, specified as a 3-element vector.

**Data Types:** `single` | `double`
### Output

### **Port 1** — Axis/Angle Rotation 4 element vector

Output rotation, returned as a 4-element vector in axis/angle notation, The first
three elements specify the axis of rotation and the fourth element specifies the
angle.

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

The `Viewpoint Direction to VR Orientation` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB® and Simulink® with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Convert viewpoint direction to virtual world orientation

The Viewpoint Direction to VR Orientation takes a viewpoint direction
(a 3 element vector) as input and outputs the corresponding virtual world viewpoint
orientation (a 4-element rotation vector).

To open the Block Parameters dialog box, double-click the block.
