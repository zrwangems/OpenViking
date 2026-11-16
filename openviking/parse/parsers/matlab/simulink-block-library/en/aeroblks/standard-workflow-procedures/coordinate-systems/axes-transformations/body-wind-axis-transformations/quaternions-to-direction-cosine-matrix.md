---
type: simulink-block
title: 'Quaternions to Direction Cosine Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'quaternionstodirectioncosinematrix'
documentation_source_path: 'quaternionstodirectioncosinematrix.html'
language: en
---

# Quaternions to Direction Cosine Matrix

## Ports

### Input

### **q** — Quaternion 4-by-1 vector

Quaternion, specified as a 4-by-1 vector.

**Data Types:** `double`
### Output

### **DCMbe** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix, returned as a 3-by-3 matrix.

**Data Types:** `double`

## Parameters

Not documented in R2025b.

## Libraries

Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert quaternion vector to direction cosine matrix

The Quaternions to Direction Cosine Matrix block transforms a
four-element unit quaternion vector (*q*0,
*q*1,
*q*2,
*q*3) into a 3-by-3 direction cosine matrix
(DCM). The outputted DCM performs the coordinate transformation of a vector in inertial
axes to a vector in body axes. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention. This
block normalizes all quaternion inputs. The quaternion input and the resulting direction
cosine matrix represent a right-hand passive transformation from frame A to frame B. For
more information, see Algorithms.
