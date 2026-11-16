---
type: simulink-block
title: 'Quaternion Division'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaterniondivision'
documentation_source_path: 'quaterniondivision.html'
language: en
---

# Quaternion Division

## Ports

### Input

### **q** — Dividend quaternion quaternion | vector of quaternions

Dividend quaternions in the form of
[*q*0,
*p*0, ...,
*q*1,
*p*1, ... ,
*q*2,
*p*2, ... ,
*q*3,
*p*3, ...], specified as a
quaternion or vector of quaternions.

**Data Types:** `double`

### **r** — Divisor quaternion quaternion | vector of quaternions

Divisor quaternions in the form of
[*s*0,
*r*0, ...,
*s*1,
*r*1, ... ,
*s*2,
*r*2, ... ,
*s*3,
*r*3, ...], specified as a
quaternion or vector of quaternions.

**Data Types:** `double`
### Output

### **q/r** — Output quaternion quaternion | vector

Output quaternion or vector of resulting quaternions from
division.

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

Divide quaternion by another quaternion

The Quaternion Division block divides a given quaternion by
another. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. The
output is the resulting quaternion from the division or vector of resulting quaternions
from division. For the quaternion forms used, see Algorithms.
