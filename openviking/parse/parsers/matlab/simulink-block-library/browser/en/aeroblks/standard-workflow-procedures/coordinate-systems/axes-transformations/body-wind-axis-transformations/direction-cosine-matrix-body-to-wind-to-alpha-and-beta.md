---
type: simulink-block
title: 'Direction Cosine Matrix Body to Wind to Alpha and Beta'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixbodytowindtoalphaandbeta'
documentation_source_path: 'directioncosinematrixbodytowindtoalphaandbeta.html'
language: en
---

# Direction Cosine Matrix Body to Wind to Alpha and Beta

## Ports

### Input

### **DCMwb** — Direction cosine matrix 3-by-3 direction cosine matrix

Direction cosine matrix to transform body-fixed vectors to wind-fixed
vectors, specified as a 3-by-3 direct cosine matrix.

**Data Types:** `double`
### Output

### **α β** — Angle of attack and sideslip angle 2-by-1 vector

Angle of attack and sideslip angle, returned as a vector, in
radians.

**Data Types:** `double`

## Parameters

### **Action for invalid DCM** — Block behavior `None` (default) | `Warning` | `Error`

Block behavior when the direction cosine matrix is invalid (not orthogonal).

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

Tolerance of the direction cosine matrix validity, specified as a scalar. The block
considers the direction cosine matrix valid if these conditions are
true:

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

Convert direction cosine matrix to angle of attack and sideslip angle

The Direction Cosine Matrix Body to Wind to Alpha and Beta
block converts a 3-by-3 direction cosine matrix (DCM) to angle of attack and sideslip
angle. The DCM performs the coordinate transformation of a vector in body axes
(*ox*0,
*oy*0,
*oz*0) into a vector in wind axes
(*ox*2,
*oy*2,
*oz*2). For more information on the
direction cosine matrix, see Algorithms.
