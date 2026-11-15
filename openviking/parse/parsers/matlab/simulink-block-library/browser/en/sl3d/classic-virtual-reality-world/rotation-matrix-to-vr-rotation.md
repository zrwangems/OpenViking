---
type: simulink-block
title: 'Rotation Matrix to VR Rotation'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'rotationmatrixtovrrotation'
documentation_source_path: 'rotationmatrixtovrrotation.html'
language: en
---

# Rotation Matrix to VR Rotation

## Ports

### Input

### **input 1** — Rotation matrix 3-by-3 matrix

3D rotation, specified as a 3-by-3 columnwise-defined matrix, also
known as a direction cosine matrix.

A representation of a three-dimensional spherical rotation as a 3-by-3
real, orthogonal matrix *R*:
*R*T*R*
= *RR*T =
*I*, where I is the 3-by-3 identity and
*R*T is the transpose of *R*. This matrix
is also known as the direction cosine matrix (DCM). The DCM is the
orientation of the object in space, relative to its parent node.

R=(R11R12R13R21R22R23R31R32R33)=(RxxRxyRxzRyxRyyRyzRzxRzyRzz)

**Data Types:** `single` | `double`
### Output

### **Port 1** — Axis/Angle Rotation 4 element vector

Output rotation, returned as a 4-element vector in axis/angle notation, The first
three elements specify the axis of rotation and the fourth element specifies the
angle.

## Parameters

### **Maximum value to treat input value as zero** — Effective zero value `1e-12` (default) | scalar

Input signal value is considered to be zero if it is equal to or lower than the
value set in this parameter. By default, the parameter is set to ε = 1e-12.

## Libraries

Simulink 3D Animation / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

### R2023b: To be removed

The `Rotation Matrix to VR Rotation` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB® and Simulink® with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Convert rotation matrix to axis/angle rotation

The Rotation Matrix to VR Rotation converts Rotation Matrix (defined
columnwise as 3-by-3 matrix or as a 9-element column vector) into the Axis / Angle
rotation representation used for defining rotations in VR.
