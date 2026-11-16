---
type: simulink-block
title: 'Pi-shaped MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'pishapedmf'
documentation_source_path: 'pishapedmf.html'
language: en
---

# Pi-shaped MF

## Ports

### Input

### **x** — Input value scalar | vector

Input value for which to compute membership values, specified as a scalar or
vector.
### Output

### **Pi MF** — Membership value scalar | vector

Membership value, returned as a scalar or a vector. The dimensions of **Pi
MF** match the dimensions of **x**. Each element of
**Pi MF** is the membership value computed for the corresponding
element of **x**.

## Parameters

### **Left base point a** — Foot of left transition area `-9` (default) | scalar

Foot *a* of the left transition area.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a` |
| **Type:** string, character vector |
| **Default:** `"-9"` |

### **Left top point b** — Shoulder of left transition area `-7` (default) | scalar

Shoulder *b* of the left transition area.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `b` |
| **Type:** string, character vector |
| **Default:** `"-7"` |

### **Right top point c** — Shoulder of right transition area `-9` (default) | scalar

Shoulder *c* of the right transition area.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `c` |
| **Type:** string, character vector |
| **Default:** `"2"` |

### **Right base point d** — Foot of right transition area `-7` (default) | scalar

Foot *d* of the right transition area.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `d` |
| **Type:** string, character vector |
| **Default:** `"8"` |

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

Pi-shaped membership function

The Pi-shaped MF block implements a pi-shaped membership function.

f(x;a,b,c,d)={0,x≤a2(x−ab−a)2,a≤x≤a+b21−2(x−bb-a)2,a+b2≤x≤b1,b≤x≤c1−2(x−cd−c)2,c≤x≤c+d22(x−dd-c)2,c+d2≤x≤d0,x≥d}

The parameters *a* and *d* control the left and right
base points or *feet* of the curve. The parameters *b* and
*c* control the left and right top points or *shoulders*
of the curve.

This block is related to the Z-shaped MF and S-shaped
MF blocks.
