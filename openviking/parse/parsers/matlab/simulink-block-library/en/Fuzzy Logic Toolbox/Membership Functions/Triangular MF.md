---
type: simulink-block
title: 'Triangular MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'triangularmf'
documentation_source_path: 'triangularmf.html'
language: en
---

# Triangular MF

## Ports

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

### **Left base point a** — Left foot of triangle `1` (default) | scalar

Left foot *a* of the triangle.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a` |
| **Type:** string, character vector |
| **Default:** `"1"` |

### **Peak location b** — Triangle peak `3` (default) | scalar

Triangle peak *b*.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `b` |
| **Type:** string, character vector |
| **Default:** `"3"` |

### **Right base point c** — Right foot of triangle `6` (default) | scalar

Right foot *c* of the triangle.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `c` |
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

**Introduced before R2006a**

## Description

Triangular membership function

The Triangular MF block implements a triangle-shaped membership
function.

f(x;a,b,c)={0,x≤ax−ab−a,a≤x≤bc−xc−b,b≤x≤c0,c≤x}

More compactly, the function is as follows.

f(x;a,b,c)=max(min(x−ab−a,c−xc−b),0)

The parameters *a* and *c* set the left and right
*feet* or base points of the triangle. The parameter *b*
sets the location of the triangle peak.

This block is related to the Trapezoidal MF, Linear S-shaped MF, and
Linear Z-shaped MF
blocks.
