---
type: simulink-block
title: 'Direction Cosine Matrix ECEF to NED'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'directioncosinematrixeceftoned'
documentation_source_path: 'directioncosinematrixeceftoned.html'
language: en
---

# Direction Cosine Matrix ECEF to NED

## Ports

### Input

### **μl** — Geodetic latitude and longitude 2-by-1 vector

Geodetic latitude and longitude, specified as a 2-by-1 vector, in
degrees. Latitude and longitude values can be any value. However,
latitude values of +90 and -90 may return unexpected values because of
singularity at the poles.

**Data Types:** `double`
### Output

### **DCMef** — Direction cosine matrix 3-by-3 matrix

DCM to perform coordinate transform of a vector in ECEF axes into a vector in NED axes,
returned as a 3-by-3 matrix.

**Data Types:** `double`

## Parameters

Not documented in R2025b.

## Libraries

Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert geodetic latitude and longitude to direction cosine matrix

The Direction Cosine Matrix ECEF to NED block converts
geodetic latitude and longitude into a 3-by-3 direction cosine matrix (DCM). The DCM
matrix performs the coordinate transformation of a vector in Earth-centered Earth-fixed
(ECEF) axes into a vector in north-east-down (NED) axes. For more information on the
direction cosine matrix, see Algorithms.

The implementation of the ECEF coordinate system assumes that the origin is at the center of
the planet, the *x*-axis intersects the Greenwich meridian and the
equator, the *z*-axis is the mean spin axis of the planet, positive to
the north, and the *y*-axis completes the right-hand system. For more
information, see ECI and ECEF Coordinates.
