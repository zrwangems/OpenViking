---
type: simulink-block
title: 'Complex Phase Difference'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'complexphasedifference'
documentation_source_path: 'ref/complexphasedifference.html'
language: en
---

# Complex Phase Difference

## Ports

### Input

### **In1** — First input signal scalar | column vector | matrix

First input signal, specified as a scalar, column vector, or matrix.
If both input signals are nonscalar, they must be the same dimension.

**Note**

This block processes complex signals. Real values at the input
ports are type cast to complex values with
`+j0` complex components.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **In2** — Second input signal scalar | column vector | matrix

Second input signal, specified as a scalar, column vector, or matrix.
If both input signals are nonscalar, they must be the same dimension.
**In2** must be the same data type as
**In1**.

**Note**

This block processes complex signals. Real values at the input
ports are type cast to complex values with
`+j0` complex components.

**Data Types:** `double` | `single`
### Output

### **Out1** — Phase shift difference scalar | column vector | matrix

Phase shift difference in radians, returned as a scalar, column
vector, or matrix. If either input signal is nonscalar, the output
signal dimension matches the dimension of the nonscalar input signal.
The output is the phase difference between the second input signal and
the first input signal. The elements of the output signal are between -π
and π and are the same data type as the input signals.

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

Phase difference between two complex signals

The Complex Phase Difference block computes the phase difference in radians between the second
input signal and the first input signal. The elements of the output are between -π and
π. This block independently processes each pair of corresponding elements.
