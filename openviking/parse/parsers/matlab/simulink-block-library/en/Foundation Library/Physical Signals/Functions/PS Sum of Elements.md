---
type: simulink-block
title: 'PS Sum of Elements'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'pssumofelements'
documentation_source_path: 'ref/pssumofelements.html'
language: en
---

# PS Sum of Elements

## Ports

### Input

### **I** — Input physical signal, untyped physical signal

Input physical signal specified as a row or column vector or a matrix.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, untyped physical signal

Output physical signal. If the input signal is a vector, then the output signal is
a scalar. If the input signal is a matrix, then by default the block computes the
column-wise sum for each dimension. For example, if the input signal is a
two-dimensional matrix, then by default the output signal is a vector. If you select
the **Sum all elements** check box, then the output signal is a
scalar.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

## Parameters

### **Sum all elements** — Specify summing method for matrices `Off` (default) | `On`

If the input signal is a matrix, then by default the block computes the column-wise
sums of elements for each dimension. To sum all the elements of the matrix, select the
**Sum all elements** check box.

## Libraries

Simscape / Foundation Library / Physical Signals / Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Calculate sum of elements of vector or matrix input physical signal

The PS Sum of Elements block calculates the sum of elements
of a vector or matrix input physical signal:

y=sum(u)

where:

- *y* is the physical signal at the output port
  **O**.
- *u* is the physical signal at the input port
  **I**.
