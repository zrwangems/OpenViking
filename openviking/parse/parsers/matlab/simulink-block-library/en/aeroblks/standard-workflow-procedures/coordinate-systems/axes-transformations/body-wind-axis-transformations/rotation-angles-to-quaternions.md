---
type: simulink-block
title: 'Rotation Angles to Quaternions'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rotationanglestoquaternions'
documentation_source_path: 'rotationanglestoquaternions.html'
language: en
---

# Rotation Angles to Quaternions

## Ports

### Input

### **[R1,R2,R3]** — Rotation angles 3-by-1 vector

Rotation angles, specified as a 3-by-1 vector, in radians.

**Data Types:** `double`
### Output

### **q** — Quaternion 4-by-1 vector

Quaternion, specified as a 4-by-1 vector.

**Data Types:** `double`

## Parameters

### **Rotation order** — Rotation order `ZYX` (default) | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

Specifies the rotation order for the three input rotation angles.

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

**Introduced in R2007b**

## Description

Calculate quaternion from rotation angles

The Rotation Angles to Quaternions block converts the rotation described by
the three rotation angles (R1, R2, R3) into the four-element quaternion vector
(*q*0,
*q*1,
*q*2,
*q*3), where quaternion is defined using the
scalar-first convention. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. The
rotation angles represent a series of right-hand intrinsic passive transformation from
frame A to frame B. The resulting quaternion represents a right-hand passive rotation
from frame A to frame B. For more information on quaternions, see Algorithms.
