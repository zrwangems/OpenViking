---
type: simulink-block
title: 'Determinant of 3x3 Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'determinantof3x3matrix'
documentation_source_path: 'determinantof3x3matrix.html'
language: en
---

# Determinant of 3x3 Matrix

## Ports
```yaml
ports:
- name: Port_1
  summary: Input matrix 3-by-3 matrix
  direction: input
  data_types: double
- name: Port_1
  summary: Determinant scalar
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Input matrix 3-by-3 matrix

Input matrix, specified as a 3-by-3 matrix.

**Data Types:** `double`
### Output

### **Port\_1** — Determinant scalar

Determinant, output as a scalar.

**Data Types:** `double`
## Parameters
```yaml
parameters: []
```

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

Compute determinant of matrix

The Determinant of 3x3 Matrix block computes the determinant
for the input matrix. For related equations, see Algorithms.
