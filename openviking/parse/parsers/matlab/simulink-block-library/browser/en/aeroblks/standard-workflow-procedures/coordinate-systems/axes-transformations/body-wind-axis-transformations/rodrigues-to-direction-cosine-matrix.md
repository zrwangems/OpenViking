---
type: simulink-block
title: 'Rodrigues to Direction Cosine Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rodriguestodirectioncosinematrix'
documentation_source_path: 'rodriguestodirectioncosinematrix.html'
language: en
---

# Rodrigues to Direction Cosine Matrix

## Ports

### Input

### **rod** — Euler-Rodrigues vector three-element vector

Euler-Rodrigues vector from which to determine the direction
cosine matrix.

**Data Types:** `double`
### Output

### **DCM** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix determined from the Euler-Rodrigues
vector.

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

**Introduced in R2017a**

## Description

Convert Euler-Rodrigues vector to direction cosine matrix

The Rodrigues to Direction Cosine Matrix block determines the 3-by-3 direction cosine matrix
from a three-element Euler-Rodrigues vector. The Euler-Rodrigues vector input and
resulting direction cosine matrix represent a right-hand passive transformation from
frame A to frame B. The resulting direction cosine matrix represent a series of
right-hand intrinsic passive rotations from frame A to frame B. For more information on
Euler-Rodrigues vectors, see Algorithms.
