---
type: simulink-block
title: 'S-shaped MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'sshapedmf'
documentation_source_path: 'sshapedmf.html'
language: en
---

# S-shaped MF

## Ports
```yaml
ports:
- name: x
  summary: Input value scalar | vector
  direction: input
- name: S MF
  summary: Membership value scalar | vector
  direction: output
```

### Input

### **x** — Input value scalar | vector

Input value for which to compute membership values, specified as a scalar or
vector.
### Output

### **S MF** — Membership value scalar | vector

Membership value, returned as a scalar or a vector. The dimensions of **S
MF** match the dimensions of **x**. Each element of
**S MF** is the membership value computed for the corresponding
element of **x**.
## Parameters
```yaml
parameters:
- name: Left point a
  summary: Leftmost point of transition area -3 (default) | scalar
  group: ''
  block_parameter: a
  type: string, character vector
  default: '"-3"'
- name: Right point b
  summary: Rightmost point of transition area 3 (default) | scalar
  group: ''
  block_parameter: b
  type: string, character vector
  default: '"3"'
```

### **Left point a** — Leftmost point of transition area `-3` (default) | scalar

Leftmost point *a* of the transition area.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a` |
| **Type:** string, character vector |
| **Default:** `"-3"` |

### **Right point b** — Rightmost point of transition area `3` (default) | scalar

Rightmost point *b* of the transition area.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `b` |
| **Type:** string, character vector |
| **Default:** `"3"` |
## Libraries

Fuzzy Logic Toolbox / Membership Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**

## Description

S-shaped membership function

The S-shaped MF block implements an s-shaped membership function.

f(x;a,b)={0,x≤a2(x−ab−a)2,a≤x≤a+b21-2(x−bb-a)2,a+b2≤x≤b1,x≥b}

Going from left to right the function increases from 0 to 1. The parameters
*a* and *b* control the left and right extremes of the
sloped portion of the curve.

This block is related to the Z-shaped MF and Pi-shaped
MF blocks.
