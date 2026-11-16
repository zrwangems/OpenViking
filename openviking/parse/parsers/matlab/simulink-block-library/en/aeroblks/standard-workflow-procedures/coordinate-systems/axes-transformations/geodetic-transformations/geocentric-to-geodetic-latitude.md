---
type: simulink-block
title: 'Geocentric to Geodetic Latitude'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'geocentrictogeodeticlatitude'
documentation_source_path: 'geocentrictogeodeticlatitude.html'
language: en
---

# Geocentric to Geodetic Latitude

## Ports

### Input

### **λ** — Geocentric latitude scalar

Geocentric latitude, specified as a scalar, in degrees. Latitude
values can be any value. However, values of +90 and -90 may return
unexpected values because of singularity at the poles.

**Data Types:** `double`

### **r** — Radius scalar

Radius from center of the planet to the center of gravity, specified
as a scalar.

**Data Types:** `double`
### Output

### **μ** — Geodetic latitude scalar

Geodetic latitude, specified as a scalar, in degrees.

**Data Types:** `double`

### **h** — Ellipsoidal altitude scalar

Ellipsoidal altitude, returned as a scalar.

#### Dependencies

To enable this port, select **Output
altitude**.

**Data Types:** `double`

## Parameters

### **Units** — Units `Metric (MKS)` (default) | `English`

Parameter and output units:

| Units | Radius from CG to Center of Planet | Equatorial Radius |
| --- | --- | --- |
| `Metric (MKS)` | Meters | Meters |
| `English` | Feet | Feet |

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

### **Flattening** — Flattening `1/298.257223563` (default) | scalar

Flattening of the planet, specified as a double scalar.

#### Dependencies

This parameter is enabled when **Planet
model** is set to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `F` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `1/298.257223563` |

### **Equatorial radius of planet** — Radius `6378137.0` (default) | scalar

Radius of the planet at its equator, in the same units as the **Units**
parameter.

#### Dependencies

This parameter is enabled when **Planet
model** is set to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `R` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `6378137` |

### **Output altitude** — Enable ellipsoidal altitude `off` (default) | on

Select this check box to output the ellipsoidal altitude.

#### Dependencies

Select this check box to enable the **h**
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `outputAltitude` |
| **Type**: character vector |
| **Values**: `off` | `on` |
| **Default**: `'off'` |

## Libraries

Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert geocentric latitude to geodetic latitude

The Geocentric to Geodetic Latitude block converts a
geocentric latitude (`λ`) into geodetic latitude
(`μ`) and optional ellipsoidal altitude (`h`)
using geocentric latitude and the radius from the center of the planet to the center of
gravity. The function uses an iteration-method of Bowring's formula to calculate the
geodetic latitude. For more information, see Algorithms.
