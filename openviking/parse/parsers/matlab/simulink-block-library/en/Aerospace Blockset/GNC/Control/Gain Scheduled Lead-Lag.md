---
type: simulink-block
title: 'Gain Scheduled Lead-Lag'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Control'
documentation_page: 'gainscheduledleadlag'
documentation_source_path: 'gainscheduledleadlag.html'
language: en
---

# Gain Scheduled Lead-Lag

## Ports
```yaml
ports:
- name: e
  summary: Filter input scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated | bus
- name: a
  summary: Numerator coefficient scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated | bus
- name: b
  summary: Denominator coefficient positive scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated | bus
- name: u
  summary: Filter output scalar
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated | bus
```

### Input

### **e** — Filter input scalar

Filter input, specified as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **a** — Numerator coefficient scalar

Numerator coefficient, specified as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **b** — Denominator coefficient positive scalar

Denominator coefficient, specified as a positive scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **u** — Filter output scalar

Filter output, specified as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
## Parameters
```yaml
parameters:
- name: Initial state, x_initial
  summary: Initial internal state 0 (default) | vector
  group: ''
  block_parameter: initial state, x_initial
  type: character vector
  values: vector
  default: '''0'''
```

### **Initial state, x\_initial** — Initial internal state `0` (default) | vector

Initial internal state, specified as a vector, for the filter
`x_initial`. Given this initial state, the initial
output is given by

u|t=0=x\_initial+aeb

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `initial state, x_initial` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'0'` |
## Libraries

Aerospace Blockset / GNC / Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement first-order lead-lag with gain-scheduled coefficients

The Gain Scheduled Lead-Lag block implements a first-order
lag of the form

u=1+as1+bse

where *e* is the filter input, and *u* is the filter
output.

The coefficients *a* and *b* are inputs to the block.
These values can depend on the flight condition or operating point. For example, you can
produce them from the Lookup Table
(n-D)
Simulink® block.
