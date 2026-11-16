---
type: simulink-block
title: 'DPD'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments Correction'
documentation_page: 'dpd'
documentation_source_path: 'ref/dpd.html'
language: en
---

# DPD

## Ports

### Input

### **In** — Input baseband signal column vector

Input baseband signal, specified as a column vector. This port is unnamed until
the **Coefficient source** parameter is set to `Input
port`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Coef** — Memory-polynomial coefficients matrix

Memory-polynomial coefficients, specified as a matrix. The number of rows in the
matrix must equal the memory depth of the memory polynomial.

- If the **Polynomial type** parameter is set to
  `Memory polynomial`, the number of columns in the matrix is
  the degree of the memory polynomial.
- If **Polynomial type** is set to `Cross-term memory
  polynomial`, the number of columns in the matrix must equal *m*(*n*-1)+1. *m* is the memory depth of the polynomial,
  and *n* is the degree of the memory polynomial.

**Example:** `complex([1 0 0 0 0; 0 0 0 0 0; 0 0 0 0
0])`

#### Dependencies

To enable this port, set the **Coefficient source** parameter
to `Input port`.

**Data Types:** `double`
**Complex Number Support:** Yes
### Output

### **Out** — Predistorted baseband signal column vector

Predistorted baseband signal, returned as a column vector of the same length as
the input signal.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Polynomial type** — Polynomial type `Memory polynomial` (default) | `Cross-term memory polynomial`

Polynomial type used for predistortion, specified as one of these values:

- `Memory polynomial` — Computes predistortion coefficients by
  using a memory polynomial without cross terms
- `Cross-term memory polynomial` — Computes predistortion
  coefficients by using a memory polynomial with cross terms

For more information, see Digital Predistortion.

### **Coefficient source** — Source of memory-polynomial coefficients `Property` (default) | `Input port`

Source of the memory polynomial coefficients, specified as one of these values:

- `Property` — Specify this value to use the
  **Coefficients** parameter to define the memory-polynomial
  coefficients
- `Input port` — Specify this value to use the
  **Coef** input port to define the memory-polynomial
  coefficients

### **Coefficients** — Memory-polynomial coefficients `complex([1 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0])` (default) | matrix

Memory-polynomial coefficients, specified as a matrix. The number of rows must equal
the memory depth of the memory polynomial.

- If the **Polynomial type** is set to `Memory
  polynomial`, the number of columns is the degree of the memory
  polynomial.
- If the **Polynomial type** is set to `Cross-term
  memory polynomial`, the number of columns must equal *m*(*n*-1)+1. *m* is the memory depth of the polynomial, and
  *n* is the degree of the memory polynomial.

For more information, see Digital Predistortion.

#### Dependencies

To enable this parameter, set **Coefficient source** to
`Property`.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code generation` or
`Interpreted execution`.

- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.
- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option shortens startup time, but the speed
  of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.

For more information, see Interpreted Execution vs. Code Generation (Simulink).

## Libraries

Communications Toolbox / RF Impairments Correction

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Digital predistorter

Apply digital predistortion (DPD) to a complex baseband signal using a memory polynomial
to compensate for nonlinearities in a power amplifier. For more information, see Digital Predistortion and Optimizing Estimator Polynomial Degree and Memory Depth.

This icon shows the block with all ports enabled.
