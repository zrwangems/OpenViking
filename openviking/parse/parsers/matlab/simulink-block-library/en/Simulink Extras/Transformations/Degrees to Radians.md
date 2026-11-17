---
type: simulink-block
title: 'Degrees to Radians'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'degreestoradians'
documentation_source_path: '../simulink/ref_extras/degreestoradians.html'
language: en
---

# Degrees to Radians

## Ports
```yaml
ports:
- name: Port_1
  summary: Input angle in degrees scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: Output angle in radians scalar
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### Input

### **Port\_1** — Input angle in degrees scalar

Input signal specifying the input angle in degrees.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### Output

### **Port\_1** — Output angle in radians scalar

Output signal specifying the angle in radians.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simulink Extras / Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2008b**

## Description

Convert degrees to radians

The Degrees to Radians block computes the output angle in radians from the
input angle in degrees.

*radians*  = (*n*/180) ×
*degrees*

*radians* is the angle in radians and *degrees* is the angle in degrees.
