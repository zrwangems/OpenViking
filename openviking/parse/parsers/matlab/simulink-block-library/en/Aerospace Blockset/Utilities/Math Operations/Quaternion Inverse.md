---
type: simulink-block
title: 'Quaternion Inverse'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternioninverse'
documentation_source_path: 'quaternioninverse.html'
language: en
---

# Quaternion Inverse

## Ports
```yaml
ports:
- name: q
  summary: Quaternion quaternion | vector of quaternions
  direction: input
  data_types: double
- name: Inv(q)
  summary: Quaternion inverse quaternion inverse | vector of quaternion inverses
  direction: output
  data_types: double
```

### Input

### **q** — Quaternion quaternion | vector of quaternions

Quaternions in the form of [ *q*
0 , *r*
0 , ..., *q*
1 , *r*
1 , ... , *q*
2 , *r*
2 , ... , *q*
3 , *r*
3 , ...], specified as a quaternion or vector of
quaternions.

**Data Types:** `double`
### Output

### **Inv(q)** — Quaternion inverse quaternion inverse | vector of quaternion inverses

Quaternion inverse or vector of quaternion inverses.

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

Calculate inverse of quaternion

The Quaternion Inverse block calculates the inverse for a
given quaternion. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. For
the equations used for the quaternion and quaternion inverse, Algorithms.
