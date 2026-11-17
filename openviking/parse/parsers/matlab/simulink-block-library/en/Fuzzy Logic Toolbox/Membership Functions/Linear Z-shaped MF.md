---
type: simulink-block
title: 'Linear Z-shaped MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'linearzshapedmf'
documentation_source_path: 'linearzshapedmf.html'
language: en
---

# Linear Z-shaped MF

## Ports
```yaml
ports:
- name: x
  summary: Input value scalar | vector
  direction: input
- name: MF
  summary: Membership value scalar | vector
  direction: output
```

### Input

### **x** — Input value scalar | vector

Input value for which to compute membership values, specified as a scalar or
vector.
### Output

### **MF** — Membership value scalar | vector

Membership value, returned as a scalar or a vector. The dimensions of
**MF** match the dimensions of **x**. Each element
of **MF** is the membership value computed for the corresponding
element of **x**.
## Parameters
```yaml
parameters:
- name: Left point a
  summary: Leftmost point of transition area 4 (default) | scalar
  group: ''
  block_parameter: a
  type: string, character vector
  default: '"4"'
- name: Right point b
  summary: Rightmost point of transition area 6 (default) | scalar
  group: ''
  block_parameter: b
  type: string, character vector
  default: '"6"'
```

### **Left point a** — Leftmost point of transition area `4` (default) | scalar

Leftmost point *a* of the transition area.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a` |
| **Type:** string, character vector |
| **Default:** `"4"` |

### **Right point b** — Rightmost point of transition area `6` (default) | scalar

Rightmost point *b* of the transition area.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `b` |
| **Type:** string, character vector |
| **Default:** `"6"` |
## Libraries

Fuzzy Logic Toolbox / Membership Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced in R2022a**

## Description

Linear z-shaped saturation membership function

The Linear Z-Shaped MF block implements a linear z-shaped saturation
membership function.

- When *a* < *b*:

  f(x;a,b)={1,x<ab−xb−a,a≤x≤b0,x>b}
- When *a* = *b*:

  f(x;a,b)={1,x<a0,x≥a}

The parameters *a* and *b* control the shoulder and foot
of the membership function, respectively. Setting *a* equal to
*b* produces a crisp membership function.

This block is related to the Triangular MF, Trapezoidal
MF, and Linear S-shaped MF
blocks.
