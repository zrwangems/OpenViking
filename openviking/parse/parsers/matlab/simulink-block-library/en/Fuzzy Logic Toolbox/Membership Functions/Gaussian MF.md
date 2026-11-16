---
type: simulink-block
title: 'Gaussian MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'gaussianmf'
documentation_source_path: 'gaussianmf.html'
language: en
---

# Gaussian MF

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

### **Standard deviation sigma** — Standard deviation `1` (default) | scalar

Standard deviation *σ* of the Gaussian function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sigma` |
| **Type:** string, character vector |
| **Default:** `"1"` |

### **Mean c** — Mean `0` (default) | scalar

Mean *c* of the Gaussian function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mu` |
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

Gaussian membership function

The Gaussian MF block implements a membership function based on a symmetric
Gaussian function.

f(x;σ,c)=e−(x−c)22σ2

Here, *c* is the mean and *σ* is the standard deviation
of the Gaussian function.

A Gaussian membership function is not the same as a Gaussian probability distribution. For
example, a Gaussian membership function always has a maximum value of `1`.
For more information on Gaussian probability distributions, see Normal Distribution (Statistics and Machine Learning Toolbox).
