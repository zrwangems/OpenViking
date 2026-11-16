---
type: simulink-block
title: 'Rodrigues to Quaternions'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rodriguestoquaternions'
documentation_source_path: 'rodriguestoquaternions.html'
language: en
---

# Rodrigues to Quaternions

## Ports

### Input

### **rod** — Euler-Rodrigues vector three-element vector

Euler-Rodrigues vector from which to determine the quaternion.

**Data Types:** `double`
### Output

### **q** — Quaternion 4-by-1 matrix

Quaternion determined from the Euler-Rodrigues vector.

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

Convert Euler-Rodrigues vector to quaternion

The Rodrigues to Quaternions block determines the 4-by-1 quaternion from a three-element
Euler-Rodrigues vector. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. The
Euler-Rodrigues vector input and the resulting quaternion represent a right-hand passive
transformation from frame A to frame B. The resulting quaternion represents a series of
right-hand intrinsic passive rotations from frame A to frame B. For more information on
Euler-Rodrigues vectors, see Algorithms.
