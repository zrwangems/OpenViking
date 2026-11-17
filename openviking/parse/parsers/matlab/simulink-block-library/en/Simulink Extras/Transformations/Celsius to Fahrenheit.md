---
type: simulink-block
title: 'Celsius to Fahrenheit'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'celsiustofahrenheit'
documentation_source_path: '../simulink/ref_extras/celsiustofahrenheit.html'
language: en
---

# Celsius to Fahrenheit

## Ports
```yaml
ports:
- name: Port_1
  summary: Celsius degree input scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: Fahrenheit degree output scalar
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### Input

### **Port\_1** — Celsius degree input scalar

Input signal specifying the Celsius degrees.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### Output

### **Port\_1** — Fahrenheit degree output scalar

Output signal specifying the Fahrenheit degrees.

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

Convert degrees Celsius to degrees Fahrenheit

The Celsius to Fahrenheit block computes the output temperature in degrees
Fahrenheit from the input temperature in degrees Celsius.

*T*F =
(9/5)*T*C + 32

*T*C is the temperature in degrees Celsius and
*T*F is the temperature in degrees
Fahrenheit.
