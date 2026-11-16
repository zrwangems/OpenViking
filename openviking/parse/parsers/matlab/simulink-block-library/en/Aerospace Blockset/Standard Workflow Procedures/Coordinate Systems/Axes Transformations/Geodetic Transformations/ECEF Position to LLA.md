---
type: simulink-block
title: 'ECEF Position to LLA'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'ecefpositiontolla'
documentation_source_path: 'ecefpositiontolla.html'
language: en
---

# ECEF Position to LLA

## Ports

### Input

### **Xf** — Position 3-by-1 vector

Position in ECEF frame, specified as a 3-by-1 vector.

**Data Types:** `double`
### Output

### **μ l** — Geodetic latitude and longitude 2-by-1 vector

Geodetic latitude and longitude, returned as a 2-by-1 vector, in
degrees.

**Data Types:** `double`

### **h** — Altitude scalar

Altitude above the planetary ellipsoid, returned as a scalar, in the
same units as the ECEF position.

**Data Types:** `double`

## Parameters

### **Units** — Output units `Metric (MKS)` (default) | `English`

Output units, specified as:

| Units | Position | Equatorial Radius | Altitude |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Meters | Meters |
| `English` | Feet | Feet | Feet |

#### Dependencies

To enable this parameter, set **Planet
model** to `Earth (WGS84)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Planet model** — Planet model `Earth (WGS84)` (default) | `Custom`

Planet model to use, `Custom` or `Earth (WGS84)`.

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

To enable this parameter, set **Planet model** to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `F` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1/298.257223563'` |

### **Equatorial radius of planet** — Radius of planet at equator `6378137` (default) | scalar

Radius of the planet at its equator, specified as a double scalar, in the same units
as the desired units for the ECEF position.

#### Dependencies

To enable this parameter, set **Planet model** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `R` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'6378137'` |

## Libraries

Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate geodetic latitude, longitude, and altitude above planetary ellipsoid from Earth-centered Earth-fixed (ECEF) position

The ECEF Position to LLA block converts a 3-by-1 vector of ECEF position (p¯) into geodetic latitude (μ¯), longitude (ι¯), and altitude (h¯) above the planetary ellipsoid. For more information on the ECEF
position, see Algorithms.
