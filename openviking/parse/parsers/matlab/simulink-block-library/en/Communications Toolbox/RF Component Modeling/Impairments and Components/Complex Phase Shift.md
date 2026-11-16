---
type: simulink-block
title: 'Complex Phase Shift'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Impairments and Components'
documentation_page: 'complexphaseshift'
documentation_source_path: 'ref/complexphaseshift.html'
language: en
---

# Complex Phase Shift

## Ports

### Input

### **In** — Input signal scalar | column vector | matrix

Input signal, specified as a scalar, column vector, or matrix.

**Note**

This block processes and outputs complex signals. Real values
at the input port are type cast to complex values with
`+j0` complex components.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **Ph** — Phase shift scalar | column vector | matrix

Phase shift in radians, specified as a scalar, column vector, or
matrix. If the phase shift is nonscalar, it must have the same dimension
as the signal at port **In**.

**Data Types:** `double`
### Output

### **Out1** — Phase-shifted signal scalar | column vector | matrix

Phase-shifted signal, returned as a complex-valued scalar, column
vector, or matrix. This output is the same dimension and data type as
the input signal.

## Parameters

Not documented in R2025b.

## Libraries

Communications Toolbox / Utility Blocks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Apply complex phase shift to complex signal

The Complex Phase Shift block applies a complex phase shift to a complex signal. This block
independently processes each pair of corresponding elements.
