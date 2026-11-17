---
type: simulink-block
title: 'Extract Triangular Matrix'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'extracttriangularmatrix'
documentation_source_path: 'ref/extracttriangularmatrix.html'
language: en
---

# Extract Triangular Matrix

## Ports
```yaml
ports:
- name: A
  summary: Input vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: U
  summary: Lower or upper triangle output vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### Input

### **A** — Input vector | matrix

Specify the input as a vector or a matrix of size
*M*-by-*N*. The block treats
length-*M* unoriented vector inputs as an
*M*-by-1 matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **U** — Lower or upper triangle output vector | matrix

Extract the lower triangle or the upper triangle of the input matrix. When you set the
**Extract** parameter to:

- `Upper` — The block copies
  the elements on and above the main diagonal of the input
  matrix to an output matrix of the same size. The first row
  of the output matrix is identical to the first row of the
  input matrix. The elements below the main diagonal of the
  output matrix are zero.
- `Lower` — The block copies
  the elements on and below the main diagonal of the input
  matrix to an output matrix of the same size. The first
  column of the output matrix is identical to the first column
  of the input matrix. The elements above the main diagonal of
  the output matrix are zero.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Extract
  summary: Component of matrix to extract Upper (default) | Lower
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Extract** — Component of matrix to extract `Upper` (default) | `Lower`

Specify the component of the matrix to copy to the output:

- `Upper` — The block copies the
  elements on and above the main diagonal of the input matrix to an
  output matrix of the same size. The first row of the output matrix
  is identical to the first row of the input matrix. The elements
  below the main diagonal of the output matrix are zero.
- `Lower` — The block copies the
  elements on and below the main diagonal of the input matrix to an
  output matrix of the same size. The first column of the output
  matrix is identical to the first column of the input matrix. The
  elements above the main diagonal of the output matrix are
  zero.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.
## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

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

## Version History

**Introduced before R2006a**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

## Description

Extract lower or upper triangle from input matrices

The Extract Triangular Matrix block creates a triangular matrix output
from the upper or lower triangular elements of an
*M*-by-*N* input matrix. The block treats
length-*M* unoriented vector inputs as an *M*-by-1
matrix.
