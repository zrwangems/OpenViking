---
type: simulink-block
title: 'Extract Diagonal'
family: matrix-operations
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'extractdiagonal'
---

# Extract Diagonal

Extract main diagonal of input matrix

## Libraries

Simulink / Matrix Operations

## Description

The Extract Diagonal block populates the unoriented output vector with
the elements on the main diagonal of the *M*-by-*N*
input matrix `A`.

Equivalent MATLAB® code is given by:

```
D = diag(A)
```

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input matrix to extract the diagonal from, specified as a scalar,
vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output signal vector

Output vector of each diagonal element.

The output is the same data type and complexity as the input. The
output vector has length `min(M,N)`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2021b: Extract Diagonal Block Moved to Simulink Matrix Operations Library

The Extract Diagonal block has been moved from the **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** library to the **Simulink** > **Matrix Operations**library. All existing models continue to work.
