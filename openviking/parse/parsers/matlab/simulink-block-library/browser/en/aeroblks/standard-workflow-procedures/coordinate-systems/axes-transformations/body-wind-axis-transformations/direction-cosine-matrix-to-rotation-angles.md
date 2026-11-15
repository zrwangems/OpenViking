---
type: simulink-block
title: 'Direction Cosine Matrix to Rotation Angles'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixtorotationangles'
documentation_source_path: 'directioncosinematrixtorotationangles.html'
language: en
---

# Direction Cosine Matrix to Rotation Angles

## Ports

### Input

### **DCM** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix from which to determine the rotation angles,
specified as a 3-by-3 matrix.

**Data Types:** `double`
### Output

### **[R1,R2,R3]** — Rotation angles 3-by-1 vector

Rotation angles, returned as a 3-by-1 vector, in radians.

**Data Types:** `double`

## Parameters

### **Rotation Order** — Block output rotation order `ZYX` (default) | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

Rotation order for three wind rotation angles.

For the `ZYX`, `ZXY`,
`YXZ`, `YZX`,
`XYZ`, and `XZY`
rotations, the block generates an R2 angle that lies between ±pi/2
radians, and R1 and R3 angles that lie between ±pi radians.

For the `'ZYZ'`,
`'ZXZ'`, `'YXY'`,
`'YZY'`, `'XYX'`, and
`'XZX'` rotations, the block generates an R2
angle that lies between 0 and pi radians, and R1 and R3 angles that lie
between ±pi radians. However, in the latter case, R3 is set to 0
radians.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rotationOrder` |
| **Type**: character vector |
| **Values**: `'ZYX'` | `'ZYZ'` |`'ZXY'` | `'ZXZ'` | `'YXZ'` | `'YXY'` | `'YZX'` | `'YZY'` | `'XYZ'` | `'XYX'` | `'XZY'` | `'XZX'` |
| **Default**: `'ZYX'` |

### **Action for invalid DCM** — Block behavior `None` (default) | `Warning` | `Error`

Block behavior when the direction cosine matrix is invalid (not
orthogonal).

- `Warning` — Displays warning indicating
  that the direction cosine matrix is invalid.
- `Error` — Displays error indicating that
  the direction cosine matrix is invalid.
- `None` — Does not display warning or
  error (default).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'None'` |

**Data Types:** `char` | `string`

### **Tolerance for DCM validation** — Tolerance `eps(2)` (default) | scalar

Tolerance of the direction cosine matrix validity, specified as a scalar.
The block considers the direction cosine matrix valid if these conditions
are true:

- The transpose of the direction cosine matrix times itself equals
  `1` within the specified tolerance
  (`transpose(n)*n == 1±tolerance`).
- The determinant of the direction cosine matrix equals
  `1` within the specified tolerance
  (`det(n) == 1±tolerance`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `tolerance` |
| **Type**: character vector |
| **Values**: `'eps(2)'` | scalar |
| **Default**: `'eps(2)'` |

**Data Types:** `double`

## Libraries

Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

## Description

Convert direction cosine matrix to rotation angles

The Direction Cosine Matrix to Rotation Angles block converts
a 3-by-3 direction cosine matrix (DCM) into the rotation angles R1, R2, and R3,
respectively. The block **Rotation Order** parameter specifies the
order of the block output rotations. For example, if **Rotation Order**
has a value of `ZYX`, the block outputs are in the rotation order
*`z-y-x`* (psi theta phi). The direction cosine matrix
represents a passive transformation from frame A to frame B. The resulting rotation
angles represent a series of right-hand intrinsic passive rotations from frame A to
frame B.
