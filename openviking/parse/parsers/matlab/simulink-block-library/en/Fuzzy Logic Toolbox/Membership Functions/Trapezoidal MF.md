---
type: simulink-block
title: 'Trapezoidal MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'trapezoidalmf'
documentation_source_path: 'trapezoidalmf.html'
language: en
---

# Trapezoidal MF

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
- name: Left base point a
  summary: Left foot of trapezoid -8 (default) | scalar
  group: ''
  block_parameter: a
  type: string, character vector
  default: '"-8"'
- name: Left top point b
  summary: Left shoulder of trapezoid -4 (default) | scalar
  group: ''
  block_parameter: b
  type: string, character vector
  default: '"-4"'
- name: Right top point c
  summary: Right shoulder of trapezoid 2 (default) | scalar
  group: ''
  block_parameter: c
  type: string, character vector
  default: '"2"'
- name: Right base point d
  summary: Right foot of trapezoid 9 (default) | scalar
  group: ''
  block_parameter: d
  type: string, character vector
  default: '"9"'
```

### **Left base point a** — Left foot of trapezoid `-8` (default) | scalar

Left foot *a* of the trapezoid.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a` |
| **Type:** string, character vector |
| **Default:** `"-8"` |

### **Left top point b** — Left shoulder of trapezoid `-4` (default) | scalar

Left shoulder *b* of the trapezoid.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `b` |
| **Type:** string, character vector |
| **Default:** `"-4"` |

### **Right top point c** — Right shoulder of trapezoid `2` (default) | scalar

Right shoulder *c* of the trapezoid.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `c` |
| **Type:** string, character vector |
| **Default:** `"2"` |

### **Right base point d** — Right foot of trapezoid `9` (default) | scalar

Right foot *d* of the trapezoid.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `d` |
| **Type:** string, character vector |
| **Default:** `"9"` |
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

Trapezoidal membership function

The Trapezoidal MF block implements a trapezoid-shaped membership
function.

f(x;a,b,c,d)=max(min(x−ab−a,1,d−xd−c),0)

The parameters *a* and *d* control the left and right
*feet* or base points of the trapezoid. The parameters
*b* and *c* control the left and right
*shoulders* or top points of the trapezoid.

The shape of the membership function depends on the relative values of
*b* and *c*.

- When *c* is greater than *b*, the resulting
  membership function is trapezoidal.
- When *b* is equal to *c*, the resulting membership
  function is equivalent to a triangular membership function with parameters
  [*a*
  *b*
  *d*].
- When *c* is less than *b*, the resulting membership
  function is triangular with a maximum value less than 1.

This block is related to the Triangular MF, Linear S-shaped MF, and
Linear Z-shaped MF
blocks.
