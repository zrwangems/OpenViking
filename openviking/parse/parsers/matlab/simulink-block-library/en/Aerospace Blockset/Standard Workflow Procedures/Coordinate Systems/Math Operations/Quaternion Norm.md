---
type: simulink-block
title: 'Quaternion Norm'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Math Operations'
documentation_page: 'quaternionnorm'
documentation_source_path: 'quaternionnorm.html'
language: en
---

# Quaternion Norm

## Ports

### Input

### **q** — Quaternion norm quaternion norm | vector of quaternion norms

Quaternions in the form of [ *q*
0 , *r*
0 , ..., *q*
1 , *r*
1 , ... , *q*
2 , *r*
2 , ... , *q*
3 , *r*
3 , ...], specified as a quaternion norm or
vector of quaternion norms.

**Data Types:** `double`
### Output

### **norm(q)** — Quaternion norm quaternion norm | vector of quaternion norms

Quaternion norm or vector of quaternion norms in the form of [
*norm* (q), *norm* (r), ...].

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

Calculate norm of quaternion

The Quaternion Norm block calculates the norm for a given
quaternion. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. For
the equations used for the quaternion and quaternion norm, see Algorithms.
