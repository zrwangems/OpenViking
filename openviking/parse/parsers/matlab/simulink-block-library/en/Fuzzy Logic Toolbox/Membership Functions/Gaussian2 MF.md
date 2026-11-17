---
type: simulink-block
title: 'Gaussian2 MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'gaussian2mf'
documentation_source_path: 'gaussian2mf.html'
language: en
---

# Gaussian2 MF

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

When *c*1 ≤
*c*2, the membership function reaches a
maximum value of `1` over the range
[*c*1,
*c*2].

Otherwise, when *c*1 >
*c*2, the maximum value is less than
one.
## Parameters
```yaml
parameters:
- name: Standard deviation for left curve sigma1
  summary: Left Gaussian standard deviation 3 (default) | scalar
  group: ''
  block_parameter: sigma1
  type: string, character vector
  default: '"3"'
- name: Mean for left curve c1
  summary: Left Gaussian mean -1 (default) | scalar
  group: ''
  block_parameter: mu1
  type: string, character vector
  default: '"-1"'
- name: Standard deviation for right curve sigma2
  summary: Right Gaussian standard deviation 1 (default) | scalar
  group: ''
  block_parameter: sigma2
  type: string, character vector
  default: '"1"'
- name: Mean for right curve c2
  summary: Right Gaussian mean 5 (default) | scalar
  group: ''
  block_parameter: mu2
  type: string, character vector
  default: '"5"'
```

### **Standard deviation for left curve sigma1** — Left Gaussian standard deviation `3` (default) | scalar

Standard deviation *σ*1 of the left Gaussian
function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sigma1` |
| **Type:** string, character vector |
| **Default:** `"3"` |

### **Mean for left curve c1** — Left Gaussian mean `-1` (default) | scalar

Mean *c*1 of the left Gaussian
function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mu1` |
| **Type:** string, character vector |
| **Default:** `"-1"` |

### **Standard deviation for right curve sigma2** — Right Gaussian standard deviation `1` (default) | scalar

Standard deviation *σ*2 of the right
Gaussian function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sigma2` |
| **Type:** string, character vector |
| **Default:** `"1"` |

### **Mean for right curve c2** — Right Gaussian mean `5` (default) | scalar

Mean *c*2 of the right Gaussian
function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mu2` |
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

Combination of two Gaussian membership functions

The Gaussian2 MF block implements a membership function based on a
combination of two Gaussian functions. The two Gaussian functions are given by the following equation.

f(x;σk,ck)=e−(x−ck)22σk2

where *k* = 1,2. The parameters
*c*1 and
*σ*1 are the mean and standard deviation defining
the left-most curve. The parameters *c*2 and
*σ*2 are the mean and standard deviation defining
the right-most curve.
