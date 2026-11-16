---
type: simulink-block
title: 'Dynamic Pressure'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Flight Parameters'
documentation_page: 'dynamicpressure'
documentation_source_path: 'dynamicpressure.html'
language: en
---

# Dynamic Pressure

## Ports

### Input

### **V** — Velocity three-element vector

Velocity, specified as a three-element vector.

**Data Types:** `double`

### **ρ** — Air density scalar

Air density, specified as a scalar.

**Data Types:** `double`
### Output

### **Output 1** — Dynamic pressure scalar

Dynamic pressure, returned as a scalar.

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

Compute dynamic pressure using velocity and air density

The Dynamic Pressure block computes dynamic pressure.

Dynamic pressure is defined as:

q¯=12ρV2,

where  is air density and *V* is velocity.
