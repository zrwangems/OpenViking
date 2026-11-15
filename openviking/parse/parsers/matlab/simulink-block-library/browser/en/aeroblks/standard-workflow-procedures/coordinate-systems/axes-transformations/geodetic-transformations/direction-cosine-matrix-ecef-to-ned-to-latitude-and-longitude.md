---
type: simulink-block
title: 'Direction Cosine Matrix ECEF to NED to Latitude and Longitude'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'directioncosinematrixeceftonedtolatitudeandlongitude'
documentation_source_path: 'directioncosinematrixeceftonedtolatitudeandlongitude.html'
language: en
---

# Direction Cosine Matrix ECEF to NED to Latitude and Longitude

## Ports

### Input

### **DCMef** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix from which to geodetic latitude and longitude, specified as a
3-by-3 matrix.

**Data Types:** `double`
### Output

### **μl** — Geodetic latitude and longitude 2-by-1 vector

Geodetic latitude and longitude, returned as a 2-by-1 vector in
degrees.

**Data Types:** `double`

## Parameters

### **Action for invalid DCM** — Block behavior `None` (default) | `Warning` | `Error`

Block behavior when direction cosine matrix is invalid (not orthogonal).

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

Convert direction cosine matrix to geodetic latitude and longitude

The Direction Cosine Matrix ECEF to NED to Latitude and
Longitude block converts a 3-by-3 direction cosine matrix (DCM) into
geodetic latitude and longitude. The DCM matrix performs the coordinate transformation
of a vector in Earth-centered Earth-fixed (ECEF) axes,
(*ox*0,
*oy*0,
*oz*0), into geodetic latitude and
longitude. For more information on the direction cosine matrix, see Algorithms.
