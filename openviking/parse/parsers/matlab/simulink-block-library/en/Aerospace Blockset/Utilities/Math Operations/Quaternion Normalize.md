---
type: simulink-block
title: 'Quaternion Normalize'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternionnormalize'
documentation_source_path: 'quaternionnormalize.html'
language: en
---

# Quaternion Normalize

## Ports
```yaml
ports:
- name: q
  summary: Quaternion quaternion | vector of quaternions
  direction: input
  data_types: double
- name: normal(q)
  summary: Normalized quaternion normalized quaternion | vector of normalized quaternions
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

### **normal(q)** — Normalized quaternion normalized quaternion | vector of normalized quaternions

Normalized quaternion or vector of normalized quaternions.

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

Normalize quaternion

The Quaternion Normalize block calculates a normalized quaternion for a
given quaternion. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. For
the equations used for the quaternion and normalized quaternion, see Algorithms.
