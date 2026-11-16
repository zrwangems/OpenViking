---
type: simulink-block
title: 'Direction Cosine Matrix to Rodrigues'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixtorodrigues'
documentation_source_path: 'directioncosinematrixtorodrigues.html'
language: en
---

# Direction Cosine Matrix to Rodrigues

## Ports

### Input

### **DCM** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix, specified as a 3-by-3 matrix, from which to determine the
Euler-Rodrigues vector.

**Data Types:** `double`
### Output

### **rod** — Euler-Rodrigues vector three-element vector

Euler-Rodrigues vector, returned as a three-element vector.

**Data Types:** `double`

## Parameters

### **Action for invalid DCM** — Block behavior `None` (default) | `Warning` | `Error`

Block behavior when direction cosine matrix is invalid (not orthogonal).

- `Warning` — Displays warning and
  indicates that the direction cosine matrix is invalid.
- `Error` — Displays error and indicates
  that the direction cosine matrix is invalid.
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

Tolerance of direction cosine matrix validity, specified as a scalar. The
block considers the direction cosine matrix valid if these conditions are
true:

- The transpose of the direction cosine matrix times itself equals
  `1` within the specified tolerance
  (`transpose(n)*n == 1±tolerance`)
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

**Introduced in R2017a**

## Description

Convert direction cosine matrix to Euler-Rodrigues vector

The Direction Cosine Matrix to Rodrigues block determines the 3-by-3 direction cosine matrix
from a three-element Euler-Rodrigues vector. The input direction cosine matrix and
resulting Euler-Rodrigues vector represent a right-hand passive transformation from
frame A to frame B. For more information on the direction cosine matrix, see Algorithms.
