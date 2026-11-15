---
type: simulink-block
title: 'Rotation Angles to Rodrigues'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rotationanglestorodrigues'
documentation_source_path: 'rotationanglestorodrigues.html'
language: en
---

# Rotation Angles to Rodrigues

## Ports

### Input

### **R1,R2,R3** — Rotation angles three-element vector

Rotation angles, in radians, from which to determine the
Euler-Rodrigues vector. Values must be double.
### Output

### **rod** — Euler-Rodrigues vector three-element vector

Euler-Rodrigues vector determined from rotation angles.

**Data Types:** `double`

## Parameters

### **Rotation order** — Rotation order `ZYX` (default) | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

Rotation order for three wind rotation angles.

The default limitations for the `'ZYX'`, `'ZXY'`, `'YXZ'`, `'YZX'`, `'XYZ'`,
and `'XZY'` sequences generate an R2 angle
that lies between ±pi/2 radians (± 90 degrees), and R1 and
R3 angles that lie between ±pi radians (±180 degrees).

The default limitations for the `'ZYZ'`, `'ZXZ'`, `'YXY'`, `'YZY'`, `'XYX'`,
and `'XZX'` sequences generate an R2 angle
that lies between 0 and pi radians (180 degrees), and R1 and R3 angles
that lie between ±pi (±180 degrees).

Rodrigues transformation is not defined for rotation angles
equal to ±pi radians (±180 deg).

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

Convert rotation angles to Euler-Rodrigues vector

The Rotation Angles to Rodrigues block converts the rotation described by the three rotation
angles `R1,R2,R3` into the three-element Euler-Rodrigues vector. The
rotation used in this block is a passive transformation between two coordinate systems.
The rotation angles represent a series of right-hand intrinsic passive rotations from
frame A to frame B. The resulting Euler-Rodrigues vector represents a right-hand passive
rotation from frame A to frame B. For more information on Euler-Rodrigues vectors, see
Algorithms.
