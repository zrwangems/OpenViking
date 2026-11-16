---
type: simulink-block
title: 'Flat Earth to LLA'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'flatearthtolla'
documentation_source_path: 'flatearthtolla.html'
language: en
---

# Flat Earth to LLA

## Ports

### Input

### **Xe** — Position in flat Earth frame 3-by-1 vector

Position in flat Earth frame, specified as a 3-by-1 vector.

**Data Types:** `double`

### **href** — Reference height scalar

Reference height from surface of Earth to flat Earth frame with regard to Earth frame,
specified as a scalar in the same units as the flat Earth
position.

**Data Types:** `double`

### **μref lref** — Reference location 2-by-1 vector

Reference location, specified as a 2-by-1 vector, in degrees of
latitude and longitude, for the origin of the estimation and the origin
of the flat Earth coordinate system. Use this port if you want to
specify the reference location as a dynamic value.

#### Dependencies

This port is enabled if the **Input reference position and
orientation** check box is selected.

**Data Types:** `double`

### **ψref** — Direction of flat Earth *x*-axis scalar

Angle, specified as a scalar, for converting flat Earth
*x* and *y* coordinates to North
and East coordinates. Use this port if you want to specify the angle as
a dynamic value.

#### Dependencies

This port is enabled if the **Input reference position and
orientation** check box is selected.

**Data Types:** `double`
### Output

### **μ l** — Geodetic latitude and longitude 2-by-1 vector

Geodetic latitude and longitude, returned as a 2-by-1 vector, in degrees.

**Data Types:** `double`

### **h** — Altitude scalar

Altitude above the input reference altitude, returned as a scalar, in the same units as
the flat Earth position.

**Data Types:** `double`

## Parameters

### **Units** — Units `Metric (MKS)` (default) | `English`

Parameter and output units.

| Units | Position | Equatorial Radius | Altitude |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Meters | Meters |
| `English` | Feet | Feet | Feet |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Planet model** — Planet model `Earth (WGS84)` (default) | `Custom`

Planet model to use, specified as either `Custom` or `Earth (WGS84)`.

#### Dependencies

Selecting the `Custom` option enables these parameters:

- **Flattening**
- **Equatorial radius of planet**

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
| **Default**: `1/298.257223563` |

### **Equatorial radius of planet** — Radius of planet at equator `6378137` (default) | scalar

Radius of the planet at its equator, specified as a double scalar, in the same units
as the **Units** parameter.

#### Dependencies

This parameter is enabled when **Planet model** is
set to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `R` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `6378137` |

### **Input reference position and orientation** — Input reference position and orientation as ports `off` (default) | `on`

- To enable input ports for reference position and angle to convert flat Earth, select this check box.
- To specify the reference positions and angle as static values, clear this check box.

Select this check box if you want

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `refPosPort` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Reference geodetic latitude and longitude (deg)** — Initial geodetic latitude and longitude `[0 10]` (default) | 2-by-1 vector

Reference location in latitude and longitude, specified as 2-by-1 vector, in
degrees.

#### Dependencies

To enable this parameter, clear the **Input reference position and
orientation** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LL0` |
| **Type**: character vector |
| **Values**: 2-by-1 vector |
| **Default**: `[0 10]` |

### **Direction of local tangent plane x-axis (degrees clockwise from north)** — Angle `0` (default) | scalar

Angle to convert flat Earth (local tangent plane) *x*
and *y* coordinates to North and East
coordinates, specified as a scalar double, in degrees.

#### Dependencies

To enable this parameter, clear **Input reference
position and orientation**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `psi` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `0` |

## Libraries

Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Estimate geodetic latitude, longitude, and altitude from flat Earth position

The Flat Earth to LLA block converts a 3-by-1 vector of flat
Earth position(p¯) into geodetic latitude (μ¯), longitude (ι¯), and altitude (*h*). For more information on the flat
Earth (local tangent plane) coordinate system, see Algorithms.
