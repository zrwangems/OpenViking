---
type: simulink-block
title: 'Julian Epoch to Besselian Epoch'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Reference System Transformations'
documentation_page: 'julianepochtobesselianepoch'
documentation_source_path: 'julianepochtobesselianepoch.html'
language: en
---

# Julian Epoch to Besselian Epoch

## Ports

### Input

### **rJ2000** — Position 3-by-1 vector

Position in Standard Julian Epoch (J2000), specified as a 3-by-1
vector.

**Data Types:** `double`

### **vJ2000** — Velocity 3-by-1 vector

Velocity in Standard Julian Epoch (J2000), specified as a 3-by-1
vector.

**Data Types:** `double`
### Output

### **rB1950** — Position 3-by-1 vector

Position in Standard Besselian Epoch (B1950), returned as a 3-by-1
vector.

**Data Types:** `double`

### **vB1950** — Velocity 3-by-1 vector

Velocity in Standard Besselian Epoch (B1950), returned as a 3-by-1
vector.

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

Transform position and velocity components from Standard Julian Epoch (J2000) to discontinued Standard Besselian Epoch (B1950)

The Julian Epoch to Besselian Epoch block transforms two 3-by-1 vectors of
Julian Epoch position (r¯J2000), and Julian Epoch velocity (v¯J2000) into Besselian Epoch position (r¯B1950), and Besselian Epoch velocity (v¯B1950). For more information on the transformation, see Algorithms.
