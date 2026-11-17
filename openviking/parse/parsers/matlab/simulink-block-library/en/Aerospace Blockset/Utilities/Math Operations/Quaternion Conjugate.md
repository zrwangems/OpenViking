---
type: simulink-block
title: 'Quaternion Conjugate'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternionconjugate'
documentation_source_path: 'quaternionconjugate.html'
language: en
---

# Quaternion Conjugate

## Ports
```yaml
ports:
- name: q
  summary: Input quaternion quaternion | vector of quaternions
  direction: input
  data_types: double | bus
- name: q'
  summary: Quaternion conjugate quaternion conjugate | vector of quaternion conjugates
  direction: output
  data_types: double | bus
```

### Input

### **q** — Input quaternion quaternion | vector of quaternions

Quaternions in the form of
[*q*0,
*r*0, ... ,
*q*1,
*r*1, ... ,
*q*2,
*r*2, ... ,
*q*3,
*r*3, ...], specified as a
quaternion or vector.

**Data Types:** `double` | `bus`
### Output

### **q'** — Quaternion conjugate quaternion conjugate | vector of quaternion conjugates

Quaternion conjugates in the form of
[*q*0′,
*r*0′, ... ,
*q*1′,
*r*1′, ... ,
*q*2′,
*r*2′, ... ,
*q*3′,
*r*3′, ...], returned as a
quaternion or vector.

**Data Types:** `double` | `bus`
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

Calculate conjugate of quaternion

The Quaternion Conjugate block calculates the conjugate for a
given quaternion. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. For
more information on quaternion forms, see Algorithms
