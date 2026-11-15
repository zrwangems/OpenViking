---
type: simulink-block
title: 'Quaternions to Rodrigues'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'quaternionstorodrigues'
documentation_source_path: 'quaternionstorodrigues.html'
language: en
---

# Quaternions to Rodrigues

## Ports

### Input

### **Quaternion** — Quaternion 4-by-1 matrix

Quaternion from which to determine Euler-Rodrigues vector. Quaternion
scalar is the first element.

**Data Types:** `double`
### Output

### **rod** — Euler-Rodrigues vector three-element vector

Euler-Rodrigues vector determined from the quaternion.

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

Convert quaternion to Euler-Rodrigues vector

The Quaternions to Rodrigues block converts the 4-by-1 quaternion to the three-element
Euler-Rodrigues (Rodrigues) vector. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. This
block normalizes all quaternion inputs. The quaternion input and the resulting
Euler-Rodrigues vector represent a right-hand passive transformation from frame A to
frame B. For more information on Euler-Rodrigues vectors, see Algorithms.
