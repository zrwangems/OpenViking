---
type: simulink-block
title: 'Invert 3x3 Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'invert3x3matrix'
documentation_source_path: 'invert3x3matrix.html'
language: en
---

# Invert 3x3 Matrix

## Ports

### Input

### **Port\_1** — Input matrix 3-by-3 matrix

Input matrix to be inverted, specified as a 3-by-3 matrix.

**Data Types:** `double`
### Output

### **Port\_1** — Matrix inverse 3-by-3 matrix

Matrix inverse of input matrix, returned as a 3-by-3 matrix.

**Data Types:** `double`

## Parameters

Not documented in R2025b.

## Libraries

Aerospace Blockset / Utilities / Math Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Compute inverse of 3-by-3 matrix

The Invert 3x3 Matrix block computes the inverse of 3-by-3
matrix.

If *det*(*A*) = 0, an error occurs and the simulation stops.
