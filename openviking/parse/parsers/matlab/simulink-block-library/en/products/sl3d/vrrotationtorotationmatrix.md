---
type: simulink-block
title: 'VR Rotation to Rotation Matrix'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrrotationtorotationmatrix'
documentation_source_path: 'vrrotationtorotationmatrix.html'
language: en
---

# VR Rotation to Rotation Matrix

## Ports

### Input

### **Input 1** — array/Angle rotation 4-element vector

Input rotation, specified as a 4-element vector in array/angle
notation,. The first three elements specify the array of rotation and
the fourth element specifies the angle.

**Data Types:** `single` | `double`
### Output

### **Output 1** — Rotation matrix 3-by-3 matrix

3D rotation, returned as a 3-by-3 columnwise defined matrix, also
known as a direction cosine matrix.

A representation of a three-dimensional spherical rotation as a 3-by-3
real, orthogonal matrix *R*:
*R*T*R*
= *RR*T =
*I*, where *I* is the
3-by-3 identity and
*R*T is the transpose of *R*. This matrix
is also known as the direction cosine matrix (DCM). The DCM is the
orientation of the object in space, relative to its parent node.

R=(R11R12R13R21R22R23R31R32R33)=(RxxRxyRxzRyxRyyRyzRzxRzyRzz)

**Data Types:** `single` | `double`

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

The `VR Rotation to Rotation Matrix` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB® and Simulink® with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Convert array/angle rotation to rotation matrix

The VR Rotation to Rotation Matrix block converts the array / angle
rotation representation used for defining rotations in virtual reality to a 3-by-3
rotation matrix
