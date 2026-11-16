---
type: simulink-block
title: 'Quaternion Interpolation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternioninterpolation'
documentation_source_path: 'quaternioninterpolation.html'
language: en
---

# Quaternion Interpolation

## Ports

### Input

### **q0** — First normalized quaternion 4-by-1 vector | 1-by-4 vector

First normalized quaternion for which to calculate the interpolation.
This quaternion must be a normalized quaternion

**Data Types:** `double`

### **q1** — Second normalized quaternion 4-by-1 vector | 1-by-4 vector

Second normalized quaternion for which to calculate the interpolation,
specified as a 4-by-1 vector or 1-by-4 vector. This quaternion must be a
normalized quaternion.

**Data Types:** `double`

### **f** — Interval fraction scalar

Interval fraction by which to calculate the quaternion interpolation. This value varies
between 0 and 1. It represents the intermediate rotation of the
quaternion to be calculated. This fraction affects the interpolation
method rotational velocities.

#### Dependencies

The interval fraction affects the rotational velocities of the interpolation methods
for the **Methods** parameter. For more information
on interval fractions, see [1].

**Data Types:** `double`
### Output

### **qf** — Natural logarithm vector

Natural logarithm of quaternion, returned as a vector.

**Data Types:** `double`

## Parameters

### **Methods** — Quaternion interpolation method `SLERP` (default) | `LERP` | `NLERP`

Quaternion interpolation method to calculate the quaternion interpolation,
specified as:

- `SLERP`

  Quaternion slerp. Spherical linear quaternion interpolation
  method.
- `LERP`

  Quaternion lerp. Linear quaternion interpolation method.
- `NLERP`

  Normalized quaternion linear interpolation method.

#### Dependencies

These methods have different rotational velocities, depending on the
interval fraction from input port f. For more information on interval
fractions, see [1].

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `method` |
| **Type**: character vector |
| **Values**: `'SLERP'` | `'LERP'` | `'NLERP'` |
| **Default**: `'SLERP'` |

### **Action for out-of-range input** — Out-of-range block behavior `None` (default) | `Warning` | `Error`

Out-of-range block behavior, specified as:

| Action | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. |
| `Error` (default) | Error in the Diagnostic Viewer, model simulation stops. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Warning'` |

## Libraries

Aerospace Blockset / Utilities / Math Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Quaternion interpolation between two quaternions

The Quaternion Interpolation block calculates the quaternion interpolation
between two normalized quaternions by an interval fraction. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention.
Select the interpolation method from SLERP, LERP, or NLERP. For equations used for the
interpolation methods, see Algorithms.

The two normalized quaternions are the two extremes between which the block calculates the quaternion.
