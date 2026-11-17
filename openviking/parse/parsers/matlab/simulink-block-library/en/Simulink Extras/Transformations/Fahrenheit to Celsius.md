---
type: simulink-block
title: 'Fahrenheit to Celsius'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'fahrenheittocelsius'
documentation_source_path: '../simulink/ref_extras/fahrenheittocelsius.html'
language: en
---

# Fahrenheit to Celsius

## Ports
```yaml
ports:
- name: Port_1
  summary: Fahrenheit degree input scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: Celsius degree output scalar
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### Input

### **Port\_1** — Fahrenheit degree input scalar

Input signal specifying the Fahrenheit degrees.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### Output

### **Port\_1** — Celsius degree output scalar

Output signal specifying the Celsius degrees.

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

Convert degrees Fahrenheit to degrees Celsius

The Fahrenheit to Celsius block computes the output temperature in degrees
Celsius from the input temperature in degrees Fahrenheit.

*T*C=
(5/9)(*T*F − 32)

*T*F is the temperature in degrees Fahrenheit
and *T*C is the temperature in degrees
Celsius.
