---
type: simulink-block
title: 'Rotation Angles to Direction Cosine Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rotationanglestodirectioncosinematrix'
documentation_source_path: 'rotationanglestodirectioncosinematrix.html'
language: en
---

# Rotation Angles to Direction Cosine Matrix

## Ports

### Input

### **[R1,R2,R3]** — Rotation angles 3-by-1 vector

Rotation angles, specified as a 3-by-1 vector, in radians.

**Data Types:** `double`
### Output

### **DCM** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix that performs coordinate transformations based
on rotation angles, returned as a 3-by-3 matrix.

**Data Types:** `double`

## Parameters

### **Rotation Order** — Rotation order `ZYX` (default) | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

Input rotation order for the three rotation angles.

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

Convert rotation angles to direction cosine matrix

The Rotation Angles to Direction Cosine Matrix block
determines the direction cosine matrix (DCM) from a given set of rotation angles, R1,
R2, and R3. For example, the default rotation angle order `ZYX`
represents a sequence where R1 is *z*-axis rotation (yaw), R2 is
*y*-axis rotation (pitch), and R3 is *x*-axis
rotation (roll). Use the **Rotation Order** parameter to change the
sequence. The rotation angles represent a series of right-hand intrinsic passive
transformation from frame A to frame B. The resulting direction cosine matrix represents
a right-hand rotation from frame A to frame B.
