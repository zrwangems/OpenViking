---
type: simulink-block
title: 'Direction Cosine Matrix Body to Wind'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixbodytowind'
documentation_source_path: 'directioncosinematrixbodytowind.html'
language: en
---

# Direction Cosine Matrix Body to Wind

## Ports

### Input

### **ɑ β** — Angle of attack and sideslip angle 2-by-1 vector

Angle of attack and sideslip angle, specified as a 2-by-1 vector, in
radians.

**Data Types:** `double`
### Output

### **DCMwb** — Direction cosine matrix 3-by-3 direction cosine matrix

Direction cosine matrix, returned as 3-by-3 direction cosine matrix.

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

Convert angle of attack and sideslip angle to direction cosine matrix

The Direction Cosine Matrix Body to Wind block converts angle
of attack and sideslip angles into a 3-by-3 direction cosine matrix (DCM). This
direction cosine matrix is helpful for vector body axes to wind axes coordinate
transformations. To transform the coordinates of a vector in body axes
(*ox*0,
*oy*0,
*oz*0) to a vector in wind axes
(*ox*2,
*oy*2,
*oz*2), multiply the block output direction
cosine matrix with a vector in body axes. For information on the axis rotations for this
transformation, see Algorithms.
