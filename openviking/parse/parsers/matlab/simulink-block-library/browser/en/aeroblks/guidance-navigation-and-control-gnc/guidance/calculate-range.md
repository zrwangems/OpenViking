---
type: simulink-block
title: 'Calculate Range'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control (GNC) / Guidance'
documentation_page: 'calculaterange'
documentation_source_path: 'calculaterange.html'
language: en
---

# Calculate Range

## Ports

### Input

### **x1** — Vehicle 1 position 3-element vector

Contains the (*x*, *y*, and *z*)
position of vehicle 1, specified as a three-element vector. These values
of the double data type.

**Data Types:** `double`

### **x2** — Vehicle 2 position 3-element vector

The (*x*, *y*, and *z*) position of
vehicle 2, specified as a three-element vector. These values are of the
double data type.

**Data Types:** `double`
### Output

### **R2-1** — Range scalar

Range from vehicle 2 and vehicle 1, returned as a scalar of double data type. The
calculated range is the magnitude of the distance, but not the
direction. It is always positive or zero.

**Data Types:** `double`

## Parameters

Not documented in R2025b.

## Libraries

Aerospace Blockset / GNC / Guidance

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate range between two vehicles given their respective positions

The Calculate Range block computes the range between two
vehicles. The equation used for the range calculation is

Range=(x1−x2)2+(y1−y2)2+(z1−z2)2
