---
type: simulink-block
title: 'Quaternions to Rotation Angles'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'quaternionstorotationangles'
documentation_source_path: 'quaternionstorotationangles.html'
language: en
---

# Quaternions to Rotation Angles

## Ports

### Input

### **q** — Quaternion 4-by-1 vector

Quaternion, specified as a 4-by-1 vector.

**Data Types:** `double`
### Output

### **[R1,R2,R3]** — Rotation angles 3-by-1 vector

Rotation angles, returned 3-by-1 vector, in radians.

**Data Types:** `double`

## Parameters

### **Rotation order** — Rotation order `ZYX` (default) | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

Output rotation order for the three rotation angles.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rotationOrder` |
| **Type**: character vector |
| **Values**: `ZYX` | `ZYZ` |`ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX` |
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

Determine rotation vector from quaternion

The Quaternions to Rotation Angles block converts the four-element
quaternion vector (*q*0,
*q*1,
*q*2,
*q*3), into the rotation described by the
three rotation angles (R1, R2, R3). The block generates the conversion by computing
elements in the direction cosine matrix (DCM) as a function of the rotation angles. The
elements in the DCM are functions of a unit quaternion vector. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. This
block normalizes all quaternion inputs. The resulting rotation angles represent a series
of right-hand intrinsic passive rotations from frame A to frame B. The quaternion
represents a right-hand passive transformation from frame A to frame B. For more
information on the direction cosine matrix, see Algorithms.
