---
type: simulink-block
title: 'Sigmoidal MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic in Simulink'
documentation_page: 'sigmoidalmf'
documentation_source_path: 'sigmoidalmf.html'
language: en
---

# Sigmoidal MF

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

### **a** — Transition area shape parameter `1` (default) | scalar

Parameter that controls the transition area shape. The magnitude of
**a** controls the width of the transition area.

When the sign of **a** is positive, the curve increases from left
to right. Conversely, when the sign of **a** is negative, the curve
decreases from left to right.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a` |
| **Type:** string, character vector |
| **Default:** `"1"` |

### **c** — Transition area center `0` (default) | scalar

Transition area center.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `c` |
| **Type:** string, character vector |
| **Default:** `"0"` |

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

Sigmoidal membership function

The Sigmoidal MF block implements a sigmoidal membership function.

f(x;a,c)=11+e−a(x−c)

When the sign of *a* is positive, the curve increases from
left to right. Conversely, when the sign of *a* is negative, the curve
decreases from left to right. The parameter *c* sets the point of inflection
for the curve.

This block is related to the Diff. Sigmoidal MF and Prod. Sigmoidal
MF blocks.
