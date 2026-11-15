---
type: simulink-block
title: 'Create Diagonal Matrix'
family: matrix-operations
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'creatediagonalmatrix'
language: en
---

# Create Diagonal Matrix

Create square diagonal matrix from diagonal elements

## Libraries

Simulink / Matrix Operations

## Description

The Create Diagonal Matrix block populates the diagonal of the
*M*-by-*M* matrix output with the elements
contained in the length-*M* vector input `D`. The
elements off the diagonal are zero.

Equivalent MATLAB® code is given by:

```
A = diag(D)
```

## Ports

### Input

### **Port\_1** — Input signal vector

Input to convert into a diagonal matrix, specified as an
*M*-element vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output signal matrix

Output specified as an *M*-by-*M*
matrix, where *M* is the length of the input
vector.

The output is equivalent to:

```
A = diag(D)		% Equivalent MATLAB code
```

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
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

### R2021b: Create Diagonal Matrix Block Moved to Simulink Matrix Operations Library

The Create Diagonal Matrix block has been moved from the **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** library to the **Simulink** > **Matrix Operations**library. All existing models continue to work.
