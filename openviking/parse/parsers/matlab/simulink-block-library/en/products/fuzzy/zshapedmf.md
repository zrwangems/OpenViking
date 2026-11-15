---
type: simulink-block
title: 'Z-shaped MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic in Simulink'
documentation_page: 'zshapedmf'
documentation_source_path: 'zshapedmf.html'
language: en
---

# Z-shaped MF

## Ports

### Input

### **x** — Input value scalar | vector

Input value for which to compute membership values, specified as a scalar or
vector.
### Output

### **Z MF** — Membership value scalar | vector

Membership value, returned as a scalar or a vector. The dimensions of **Z
MF** match the dimensions of **x**. Each element of
**Z MF** is the membership value computed for the corresponding
element of **x**.

## Parameters

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

Z-shaped membership function

The Z-shaped MF block implements a z-shaped membership function.

f(x;a,b)={1,x≤a1−2(x−ab−a)2,a≤x≤a+b22(x−bb-a)2,a+b2≤x≤b0x≥b

Going from left to right the function decreases from 1 to 0. The parameters
*a* and *b* control the left and right extremes of the
sloped portion of the curve.

This block is related to the S-shaped MF and Pi-shaped
MF blocks.
