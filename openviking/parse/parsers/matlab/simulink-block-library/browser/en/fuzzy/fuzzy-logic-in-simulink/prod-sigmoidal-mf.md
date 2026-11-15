---
type: simulink-block
title: 'Prod. Sigmoidal MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic in Simulink'
documentation_page: 'prod.sigmoidalmf'
documentation_source_path: 'prod.sigmoidalmf.html'
language: en
---

# Prod. Sigmoidal MF

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

### **Left curve a1** — Transition area shape parameter for left curve `2` (default) | scalar

Parameter *a*1 that controls the transition
area shape for the left curve. The magnitude of
*a*1 controls the width of the transition
area.

When the sign of *a*1 is positive, the curve
increases from left to right. Conversely, when the sign of
*a*1 is negative, the curve decreases from
left to right.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a1` |
| **Type:** string, character vector |
| **Default:** `"2"` |

### **Left curve c1** — Transition area center for left curve `-5` (default) | scalar

Transition area center *c*1 for the left
curve.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `c1` |
| **Type:** string, character vector |
| **Default:** `"-5"` |

### **Right curve a2** — Transition area shape parameter for right curve `-5` (default) | scalar

Parameter *a*2 that controls the transition
area shape for the right curve. The magnitude of
*a*2 controls the width of the transition
area.

When the sign of *a*2 is positive, the curve
increases from left to right. Conversely, when the sign of
*a*2 is negative, the curve decreases from
left to right.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a2` |
| **Type:** string, character vector |
| **Default:** `"-5"` |

### **Right curve c2** — Transition area center for right curve `5` (default) | scalar

Transition area center *c*2 for the right
curve.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `c2` |
| **Type:** string, character vector |
| **Default:** `"5"` |

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

Product of two sigmoid membership functions

The Prod. Sigmoidal MF block implements a membership function based on the
product of two sigmoidal curves. The sigmoidal curves are defined by the following equation.

f(x;ak,ck)=11+e−ak(x−ck)

where *k* = 1,2 The parameters
*a*1 and
*a*2 control the slopes of the left and right
curves. The parameters *c*1 and
*c*2 control the points of inflection for the left
and right curves.

To define a unimodal membership function with a maximum value of `1`,
specify opposite signs for *a*1 and
*a*2, and select *c* values far
enough apart to allow for both transition areas to reach `1`.

This block is related to the Diff. Sigmoidal MF and Sigmoidal
MF blocks.
