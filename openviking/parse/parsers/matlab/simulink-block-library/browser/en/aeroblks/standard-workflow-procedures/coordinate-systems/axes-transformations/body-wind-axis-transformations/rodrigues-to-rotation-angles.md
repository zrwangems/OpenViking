---
type: simulink-block
title: 'Rodrigues to Rotation Angles'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rodriguestorotationangles'
documentation_source_path: 'rodriguestorotationangles.html'
language: en
---

# Rodrigues to Rotation Angles

## Ports

### Input

### **rod** — Euler-Rodrigues vector three-element vector

Euler-Rodrigues vector determined from rotation angles.

**Data Types:** `double`
### Output

### **R1,R2,R3** — Rotation angles three-element vector

Rotation angles, in radians, from which to determine the Euler-Rodrigues
vector. Quaternion scalar is the first element.

**Data Types:** `double`

## Parameters

### **Rotation order** — Rotation order `ZYX` (default) | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

Rotation order for three wind rotation angles.

For the 'ZYX', 'ZXY', 'YXZ', 'YZX', 'XYZ', and 'XZY' rotations, the block
generates an R2 angle that lies between ±pi/2 radians (±90
degrees), and R1 and R3 angles that lie between ±pi radians (±180
degrees).

For the 'ZYZ', 'ZXZ', 'YXY', 'YZY', 'XYX', and 'XZX' rotations, the block
generates an R2 angle that lies between 0 and pi radians (180 degrees), and
R1 and R3 angles that lie between ±pi (±180 degrees). However, in
the latter case, when R2 is 0, R3 is set to 0 radians.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rotationOrder` |
| **Type**: character vector |
| **Values**: `'ZYX'` | `'ZYZ'` |`'ZXY'` | `'ZXZ'` | `'YXZ'` | `'YXY'` | `'YZX'` | `'YZY'` | `'XYZ'` | `'XYX'` | `'XZY'` | `'XZX'` |
| **Default**: `'ZYX'` |

## Libraries

Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Convert Euler-Rodrigues vector to rotation angles

The Rodrigues to Rotation Angles block converts the three-element Euler-Rodrigues vector into
rotation angles. The Euler-Rodrigues angles represent a right-hand passive
transformation from frame A to frame B. The resulting rotation angles represent a series
of right-hand intrinsic passive rotations from frame A to frame B. For more information
on Euler-Rodrigues vectors, see Algorithms.
