---
type: simulink-block
title: 'Chirp Signal'
family: sources
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'chirpsignal'
language: en
---

# Chirp Signal

## Ports

### Output

### **Port\_1** — Chirp signal scalar | vector | matrix | N-D array

Sine wave whose frequency increases at a linear rate with time. The chirp signal can be
a scalar, vector, matrix, or N-D array.

**Data Types:** `double`

## Parameters

### **Initial frequency** — Initial frequency (Hz) `0.1` (default) | scalar | vector | matrix | N-D array

The initial frequency of the signal, specified as a scalar, vector,
matrix, or N-D array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `f1` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'0.1'` |

### **Target time** — Target time (seconds) `100` (default) | scalar | vector | matrix | N-D array

Time, in seconds, at which the frequency reaches the **Frequency
at target time** parameter value. You specify the
**Target time** as a scalar, vector, matrix, or N-D
array. After the target time is reached, the frequency continues to change
at the same rate.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `T` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'100'` |

### **Frequency at target time** — Frequency (Hz) `1` (default) | scalar | vector | matrix | N-D array

Frequency, in Hz, of the signal at the target time, specified as a scalar, vector,
matrix, or N-D array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `f2` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'1'` |

### **Interpret vector parameters as 1-D** — Treat vector parameters as 1-D `on` (default) | `off`

When you select this check box, any column or row matrix values you
specify for the **Initial frequency**, **Target
time**, and **Frequency at target time**
parameters result in a vector output whose elements are the elements of the
row or column. For more information, see Determine the Output Dimensions of Source Blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParams1D` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

## Libraries

Simulink / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. Relates to resource limits and restrictions
on speed and memory often found in embedded systems. Generated code can contain
dynamic allocation and freeing of memory, recursion, additional memory overhead, and
widely-varying execution times. While the code is functionally valid and generally
acceptable in resource-rich environments, smaller embedded targets often cannot
support such code. Usually, blocks evolve toward being suitable for production code.
Thus, blocks suitable for production code remain suitable.

## Version History

**Introduced before R2006a**

## Description

Generate sine wave with increasing frequency

The Chirp Signal block generates a sine wave whose frequency increases at a
linear rate with time. You can use this block for spectral analysis of nonlinear
systems. The block generates a scalar or vector output.

The parameters, **Initial frequency**, **Target time**, and **Frequency at target time**,
determine the block's output. You can specify any or all of these
variables as scalars or arrays. All the parameters specified as arrays
must have the same dimensions. The block expands scalar parameters
to have the same dimensions as the array parameters. The block output
has the same dimensions as the parameters unless you select the **Interpret vector parameters as 1-D** check box. If you select this check box and the parameters are row or column vectors, the block outputs a vector (1-D array) signal.
