---
type: simulink-block
title: 'Direction Cosine Matrix to Quaternions'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixtoquaternions'
documentation_source_path: 'directioncosinematrixtoquaternions.html'
language: en
---

# Direction Cosine Matrix to Quaternions

## Ports

### Input

### **DCMbe** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix to transform the direction cosine matrix to quaternions,
specified as a 3-by-3.

**Data Types:** `double`
### Output

### **q** — Quaternion 4-by-1 vector

Quaternion returned by transformation as a 4-by-1 vector.

**Data Types:** `double`

## Parameters

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

**Introduced before R2006a**

## Description

Convert direction cosine matrix to quaternion vector

The Direction Cosine Matrix to Quaternions block transforms a
3-by-3 direction cosine matrix (DCM) into a four-element unit quaternion vector
(*q*0,
*q*1,
*q*2,
*q*3). Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. The
direction cosine matrix represents a passive transformation from frame A to frame B. The
resulting quaternions represent a series of intrinsic right-hand passive transformations
from frame A to frame B. For more information on the direction cosine matrix, see Algorithms.
