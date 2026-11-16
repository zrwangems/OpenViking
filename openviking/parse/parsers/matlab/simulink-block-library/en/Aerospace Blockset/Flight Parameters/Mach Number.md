---
type: simulink-block
title: 'Mach Number'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'machnumber'
documentation_source_path: 'machnumber.html'
language: en
---

# Mach Number

## Ports

### Input

### **V** — Velocity 3-element vector

Velocity vector, specified as an 3-element vector.

**Data Types:** `double`

### **a** — Speed of sound 1-by-1 array

Speed of sound, specified as a 1-by-1 array.

**Data Types:** `double`
### Output

### **Mach** — Mach number scalar

Mach number, returned as a scalar.

**Data Types:** `double`

## Parameters

Not documented in R2025b.

## Libraries

Aerospace Blockset / Flight Parameters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Compute Mach number using velocity and speed of sound

The Mach Number block computes the Mach number. The Mach
number is defined as

Mach=V⋅Va,

where *a* is the speed of sound and *V* is the velocity
vector.
