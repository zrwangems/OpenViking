---
type: simulink-block
title: 'Direction Cosine Matrix to Wind Angles'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixtowindangles'
documentation_source_path: 'directioncosinematrixtowindangles.html'
language: en
---

# Direction Cosine Matrix to Wind Angles

## Ports

### Input

### **DCMwe** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix, specified as a 3-by-3 matrix, to transform Earth-fixed vectors
to wind-fixed vectors.

**Data Types:** `double`
### Output

### **μ γ x** — Wind angles 3-by-1 vector

Wind angles (bank, flight path, heading), returned as a 3-by-1 vector, in
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

Convert direction cosine matrix to wind angles

The Direction Cosine Matrix to Wind Angles block converts a 3-by-3 direction
cosine matrix (DCM) into three wind rotation angles. The DCM matrix performs the
coordinate transformation of a vector in earth axes
(*ox*0,
*oy*0,
*oz*0) into a vector in wind axes
(*ox*3,
*oy*3,
*oz*3). For more information on the
direction cosine matrix, see Algorithms.

This implementation generates a flight path angle that lies between ±90 degrees,
and bank and heading angles that lie between ±180 degrees.
