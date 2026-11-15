---
type: simulink-block
title: 'Wind Angles to Direction Cosine Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'windanglestodirectioncosinematrix'
documentation_source_path: 'windanglestodirectioncosinematrix.html'
language: en
---

# Wind Angles to Direction Cosine Matrix

## Ports

### Input

### **μ γ χ** — Wind rotation angles 3-by-1 vector

Wind rotation angles, specified as a 3-by-1 vector, in radians.

**Data Types:** `double`
### Output

### **DCMwe** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix, returned as a 3-by-3 matrix.

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

Convert wind angles to direction cosine matrix

The Wind Angles to Direction Cosine Matrix block converts
three wind rotation angles into a 3-by-3 direction cosine matrix (DCM). The DCM matrix
performs the coordinate transformation of a vector in earth axes
(*ox*0,
*oy*0,
*oz*0) into a vector in wind axes
(*ox*3,
*oy*3,
*oz*3). For more information on the
direction cosine matrix, see Algorithms.

This implementation generates a flight path angle that lies between ±90 degrees,
and bank and heading angles that lie between ±180 degrees.
