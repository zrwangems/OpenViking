---
type: simulink-block
title: 'Generalized Bell MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'generalizedbellmf'
documentation_source_path: 'generalizedbellmf.html'
language: en
---

# Generalized Bell MF

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

### **a** — Function shape parameter `5` (default) | scalar

Parameter that, together with **b**, defines the shape of the
membership function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a` |
| **Type:** string, character vector |
| **Default:** `"5"` |

### **b** — Function shape parameter `4` (default) | positive scalar

Parameter that, together with **a**, defines the shape of the
membership function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `b` |
| **Type:** string, character vector |
| **Default:** `"4"` |

### **c** — Center point `0` (default) | scalar

Function center point.

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

Generalized bell membership function

The Generalized Bell MF block implements a membership function based on a
generalized bell-shaped function.

f(x;a,b,c)=11+|x−ca|2b

Here, *a* and *b* control the width of the function and
*c* controls the center of the function.
