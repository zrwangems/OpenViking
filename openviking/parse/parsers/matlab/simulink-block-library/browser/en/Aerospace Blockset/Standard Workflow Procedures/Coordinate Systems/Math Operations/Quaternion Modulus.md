---
type: simulink-block
title: 'Quaternion Modulus'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Math Operations'
documentation_page: 'quaternionmodulus'
documentation_source_path: 'quaternionmodulus.html'
language: en
---

# Quaternion Modulus

## Ports

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

### **|q|** — Quaternion modulus quaternion modulus | vector of quaternion moduli

Quaternion modulus or vector of quaternion moduli in the form of [|
*q* |, | *r* |, ...].

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

Calculate modulus of quaternion

The Quaternion Modulus block calculates the magnitude for a
given quaternion. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. For
the equations used for the quaternion and quaternion modulus, see Algorithms.
