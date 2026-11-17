---
type: simulink-block
title: 'Quaternion Multiplication'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternionmultiplication'
documentation_source_path: 'quaternionmultiplication.html'
language: en
---

# Quaternion Multiplication

## Ports
```yaml
ports:
- name: q
  summary: First quaternion quaternion | vector of quaternions
  direction: input
  data_types: double
- name: r
  summary: Second quaternion quaternion | vector of quaternions
  direction: input
  data_types: double
- name: q\*r
  summary: Product vector | vector of quaternion products
  direction: output
  data_types: double
```

### Input

### **q** — First quaternion quaternion | vector of quaternions

First quaternion, specified as a vector or vector of quaternions. A
vector of quaternions has this form, where *q* and
*p* are quaternions:

`[ q
0 , p
0 , ..., q
1 , p
1 , ... , q
2 , p
2 , ... , q
3 , p
3 , ...]`

**Data Types:** `double`

### **r** — Second quaternion quaternion | vector of quaternions

Second quaternion, specified as a vector or vector of quaternions. A
vector of quaternions has this form, where *s* and
*r* are quaternions:

`[ s
0 , r
0 , ..., s
1 , r
1 , ... , s
2 , r
2 , ... , s
3 , r
3 , ...]`

**Data Types:** `double`
### Output

### **q\*r** — Product vector | vector of quaternion products

Product of two quaternions, output as a vector or vector of quaternion
products.

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

Calculate product of two quaternions

The Quaternion Multiplication block calculates the product
for two given quaternions. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. For
more information on the quaternion forms, see Algorithms.
