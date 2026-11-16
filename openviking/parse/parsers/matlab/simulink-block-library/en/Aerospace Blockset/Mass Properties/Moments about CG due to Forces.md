---
type: simulink-block
title: 'Moments about CG due to Forces'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Mass Properties'
documentation_page: 'momentsaboutcgduetoforces'
documentation_source_path: 'momentsaboutcgduetoforces.html'
language: en
---

# Moments about CG due to Forces

## Ports

### Input

### **F** — Applied forces 3-element vector

Forces applied at point CP, specified as a three-element vector.

**Data Types:** `double`

### **CG** — Center of gravity 3-element vector

Center of gravity, specified as three-element vector.

**Data Types:** `double`

### **CP** — Application point of forces 3-element vector

Application point of forces, specified as a three-element vector.

**Data Types:** `double` | `bus`
### Output

### **M** — Moments at the center of gravity 3-element vector

Moments at the center of gravity in *x*-axis,
*y*-axis and *z*-axis, returned as
a three-element vector.

**Data Types:** `double`

## Parameters

Not documented in R2025b.

## Libraries

Aerospace Blockset / Mass Properties

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Compute moments about center of gravity due to forces applied at a point, not center of gravity

The Moments about CG due to Forces block computes moments
about center of gravity due to forces that are applied at point CP, not at the center of
gravity.
