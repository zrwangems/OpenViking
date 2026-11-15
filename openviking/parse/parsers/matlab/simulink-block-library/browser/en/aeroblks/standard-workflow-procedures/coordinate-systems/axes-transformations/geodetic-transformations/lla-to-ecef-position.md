---
type: simulink-block
title: 'LLA to ECEF Position'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'llatoecefposition'
documentation_source_path: 'llatoecefposition.html'
language: en
---

# LLA to ECEF Position

## Ports

### Input

### **μ l** — Geodetic latitude and longitude 2-by-1 vector

Geodetic latitude and longitude, specified as a 2-by-1 vector, in
degrees.

**Data Types:** `double`

### **h** — Altitude scalar

Altitude above the planetary ellipsoid, specified as a scalar.

**Data Types:** `double`
### Output

### **Xf** — Position 3-by-1 vector

Position in ECEF frame, returned as a 3-by-1 vector, in the same units as the input at
the **h** port.

**Data Types:** `double`

## Parameters

### **Units** — Units `Metric (MKS)` (default) | `English`

Parameter and output units:

| Units | Radius from CG to Center of Planet | Equatorial Radius |
| --- | --- | --- |
| `Metric (MKS)` | Meters | Meters |
| `English` | Feet | Feet |

#### Dependencies

To enable this, set **Planet model** to
`Earth (WGS84)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Planet model** — Planet model `Earth (WGS84)` (default) | `Custom`

Planet model to use, `Custom` or
`Earth (WGS84)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ptype` |
| **Type**: character vector |
| **Values**: `'Earth (WGS84)'` | `'Custom'` |
| **Default**: `'Earth (WGS84)'` |

### **Flattening** — Flattening of planet `1/298.257223563` (default) | scalar

Flattening of the planet, specified as a double scalar.

#### Dependencies

To enable this parameter, set **Planet
model** to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `F` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `1/298.257223563` |

### **Equatorial radius of planet** — Radius of planet at equator `6378137` (default) | scalar

Radius of the planet at its equator, in the same units as the desired
units for ECEF position.

#### Dependencies

To enable this parameter, set **Planet
model** to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `R` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `6378137` |

## Libraries

Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate Earth-centered Earth-fixed (ECEF) position from geodetic latitude, longitude, and altitude above planetary ellipsoid

The LLA to ECEF Position block converts geodetic latitude (μ¯), longitude (ι¯), and altitude (h¯) above the planetary ellipsoid into a 3-by-1 vector of ECEF position (p¯). Latitude and longitude values can be any value. However, latitude
values of +90 and -90 may return unexpected values because of singularity at the poles.
For more information the ECEF position calculation, see Algorithms.
