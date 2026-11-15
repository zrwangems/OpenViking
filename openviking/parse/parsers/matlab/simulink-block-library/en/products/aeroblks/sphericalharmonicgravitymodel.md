---
type: simulink-block
title: 'Spherical Harmonic Gravity Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'sphericalharmonicgravitymodel'
documentation_source_path: 'sphericalharmonicgravitymodel.html'
language: en
---

# Spherical Harmonic Gravity Model

## Ports

### Input

### **Xff** — Fixed-frame coordinates N-by-3 matrix

Fixed-frame coordinates from center of planet, specified as an N-by-3 matrix, in
selected units. Each row of the matrix is a separate position to
calculate. The *z*-axis is positive toward the North
Pole. If **Central body model** has a value of
`EGM2008` or `EGM96`, this matrix
contains Earth-centered Earth-fixed (ECEF) coordinates.

When inputting a large fixed-frame matrix and a high degree value, you might receive an
out-of-memory error. For more information about avoiding out-of-memory
errors in the MATLAB® environment, see Resolve “Out of Memory” Errors.

When inputting a large fixed-frame matrix, you might receive a maximum matrix size
limitation. To determine the largest matrix or array that you can create
in the MATLAB environment for your platform, see Performance and Memory.

**Data Types:** `double`
### Output

### **gff** — Gravity values N-by-3 matrix

Array of gravity values in the *x*-axis, *y*-axis, and
*z*-axis of the fixed-frame coordinates, in
selected length units per second squared. Each row of the matrix returns
the calculated gravity vector for the corresponding row in the input
matrix.

**Data Types:** `double`

## Parameters

### **Units** — Input and output units `Metric (MKS)` (default) | `English`

Input and output units, specified as:

| Units | Input | Output |
| --- | --- | --- |
| `Metric (MKS)` | Meters (m) | Meters/sec2 (m/s2) |
| `English` | Feet (ft) | Feet/sec2 (ft/s2) |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Action for out-of-range input** — Out-of-range input behavior `Warning` (default) | `Error` | `None`

Out-of-range input behavior, specified as:

| Value | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. |
| `Error` | MATLAB returns an exception, model simulation stops. |

The spherical harmonic gravity model is invalid for radial positions less
than the planetary surface. The Spherical Harmonic Gravity
Model block accepts out of range radial position inputs (less
than planetary equatorial radius) when **Action for out-of-range
input** is set to `None` or
`Warning`. However, the block output might not
be accurate or reliable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Warning'` |

### **Central body model** — Planetary model `EGM2008` (default) | `EGM96` | `LP100K` | `LP165P` | `GMM2B` | `Custom` | `EIGENGL04C`

Planetary model, specified as:

| Central body model | Notes |
| --- | --- |
| `EGM2008` | Earth — Is the latest Earth spherical harmonic gravitational model from National Geospatial-Intelligence Agency (NGA). This block provides the WGS-84 version of this gravitational model. You can use the EGM96 planetary model if you need to use the older standard for Earth. |
| `EGM96` | Earth |
| `LP100K` | Moon — Is best for lunar orbit determination based upon computational time required to compute orbits. This planet model was created in approximately the same year as LP165P with similar data. |
| `LP165P` | Moon — Is best for extended lunar mission orbit accuracy. This planet model was created in approximately the same year as LP100K with similar data. |
| `GMM2B` | Mars |
| `Custom` | Enables you to specify your own planetary model. This option enables the **Central body MAT-file** parameter. |
| `EIGENGL04C` | Earth — Supports the gravity field model, EIGEN-GL04C (`https://icgem.gfz-potsdam.de/tom_longtime`). This model is an upgrade to EIGEN-CG03C. |

For more information on the fixed-frame coordinate system for the central
bodies, see Algorithms.

When defining your own planetary model, the **Degree**
parameter is limited to the maximum value for int16. When inputting a large
degree, you might receive an out-of-memory error. For more information about
avoiding out-of-memory errors in the MATLAB environment, see Resolve “Out of Memory” Errors.

#### Dependencies

Setting this parameter to `Custom` enables
**Central body MAT-file**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ptype` |
| **Type**: character vector |
| **Values**: `'EGM2008'` | `'EGM96'` | `'LP100K'` | `'LP165P'` | `'GMM2B'` | `'Custom'` | `'EIGENGL04C'` |
| **Default**: `'EGM2008'` |

### **Degree** — Degree of harmonic model `120` (default) | scalar

Degree of harmonic model, specified as a scalar:

| Central body model | Recommended Degree | Maximum Degree |
| --- | --- | --- |
| `EGM2008` | 120 | 2159 |
| `EGM96` | 70 | 360 |
| `LP100K` | 60 | 100 |
| `LP165P` | 60 | 165 |
| `GMM2B` | 60 | 80 |
| `EIGENGL04C` | 70 | 360 |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `degree` |
| **Type**: character vector |
| **Values**: `scalar` |
| **Default**: `'120'` |

### **Central body MAT-file** — Central body MAT-file `'aerogmm2b.mat'` (default)

Central body MAT-file that contains definitions for a custom planetary
model. The `aerogmm2b.mat` file in Aerospace Blockset™ is the default MAT-file for a custom planetary model.

This file must contain:

| Variable | Description |
| --- | --- |
| *Re* | Scalar of planet equatorial radius in meters (m). |
| *GM* | Scalar of planetary gravitational parameter in meters cubed per second squared (m3/s2) |
| *degree* | Scalar of maximum degree. |
| *C* | (*degree*+1)-by-(*degree*+1) matrix containing normalized spherical harmonic coefficients matrix, *C*. |
| *S* | (*degree*+1)-by-(*degree*+1) matrix containing normalized spherical harmonic coefficients matrix, *S*. |

When using a large value for **Degree**, you might
receive an out-of-memory error. For more information about avoiding
out-of-memory errors in the MATLAB environment, see Resolve “Out of Memory” Errors.

#### Dependencies

To enable this parameter, set **Central body model**
to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `datafile` |
| **Type**: character vector |
| **Values**: `'aerogmm2b.mat'` | MAT-file |
| **Default**: `'aerogmm2b.mat'` |

## Libraries

Aerospace Blockset / Environment / Gravity

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010a**

## Description

Implement spherical harmonic representation of planetary gravity

The Spherical Harmonic Gravity Model block implements the mathematical
representation of spherical harmonic planetary gravity based on planetary gravitational
potential. It provides a convenient way to describe a planet gravitational field outside
of its surface in spherical harmonic expansion.

You can use spherical harmonics to modify the magnitude and
direction of spherical gravity (-GM/r2). The most significant or largest spherical harmonic term is the second degree zonal harmonic, J2, which accounts for oblateness of a planet.

Use this block if you want more accurate gravity values than spherical gravity models. For example, nonatmospheric flight applications might require higher accuracy.
