---
type: simulink-block
title: 'Polynomial'
family: 'libsb2sl'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'ALG'
documentation_page: 'polynomial'
documentation_source_path: 'slref/polynomial.html'
language: en
---

# Polynomial

## Ports

### Input

### **Port\_1** — Input signal real scalar or vector

Value at which to evaluate the polynomial *P(u)*.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Evaluated polynomial value real scalar or vector

Value of the polynomial *P(u)* evaluated at the input
signal.

**Data Types:** `single` | `double`

## Parameters

### **Polynomial coefficients** — Coefficients of polynomial to be evaluated `[ +2.081618890e-019, -1.441693666e-014, +4.719686976e-010, -8.536869453e-006, +1.621573104e-001, -8.087801117e+001 ]` (default) | real array

Specify polynomial coefficients in MATLAB
`polyval` form. The first coefficient corresponds to
*xN* and the remaining coefficients
correspond to decreasing orders of *x*. The last coefficient represents
the constant for the polynomial.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `coefs` |
| **Type:** real array |
| **Default:** `[ +2.081618890e-019, -1.441693666e-014, +4.719686976e-010, -8.536869453e-006, +1.621573104e-001, -8.087801117e+001 ]` |

## Libraries

Simulink / Math Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**

## Description

Perform evaluation of polynomial coefficients on input values

The Polynomial block evaluates *`P(u)`* at each time
step for the input *u*. You define a set of polynomial coefficients in the
form that the MATLAB®
`polyval` command accepts.
