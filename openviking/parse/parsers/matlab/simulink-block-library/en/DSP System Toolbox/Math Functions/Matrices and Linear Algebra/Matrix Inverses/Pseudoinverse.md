---
type: simulink-block
title: 'Pseudoinverse'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Inverses'
documentation_page: 'pseudoinverse'
documentation_source_path: 'ref/pseudoinverse.html'
language: en
---

# Pseudoinverse

## Ports

### Input

### **A** — Input vector | matrix

Specify the input as a vector or a matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **X** — Pseudoinverse output vector | matrix

Pseudoinverse output, returned as a vector or a matrix. If the
pseudoinverse calculation fails to converge, the output on this port is
an undefined matrix of the correct size.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **E** — Error status `0` | `1`

The possible values of error status you can receive on this port
are:

- `0` — The pseudoinverse calculation
  converges.
- `1` — The pseudoinverse calculation
  does not converge.

If the pseudoinverse calculation fails to converge, the output at port
**X** is an undefined matrix of the correct
size.

**Data Types:** `Boolean`

## Parameters

### **Show error status port (E)** — Show error status port `off` (default) | `on`

Select to enable the **E** output port, which reports a
failure to converge. For more details, see the description for the
**E** output port.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate
  model using the MATLAB interpreter. This option shortens startup time.
  For this block, the simulation speed in this mode is faster than
  in `Code generation`.
- `Code generation` –– Simulate model
  using generated C code. The first time you run a simulation,
  Simulink® generates C code for the block. The C code is
  reused for subsequent simulations, as long as the model does not
  change. This option requires additional startup time but the
  simulation speed increases with subsequent simulations.

## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Inverses

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Compute Moore-Penrose pseudoinverse of matrix

The Pseudoinverse block computes the Moore-Penrose pseudoinverse of
input matrix *A*.

The equivalent MATLAB® code is given by:

```
[U,S,V] = svd(A,0)
```
