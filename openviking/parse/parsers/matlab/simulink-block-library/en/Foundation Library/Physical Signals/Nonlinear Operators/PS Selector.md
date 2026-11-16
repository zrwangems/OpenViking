---
type: simulink-block
title: 'PS Selector'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psselector'
documentation_source_path: 'ref/psselector.html'
language: en
---

# PS Selector

## Ports

### Input

### **I** — Input physical signal, untyped physical signal

Input physical signal specified as a vector or matrix.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, untyped physical signal

Output physical signal containing the selected elements of the input signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

## Parameters

### **Indices** — Indices of selected signal elements `1` (default) | scalar or vector of integers greater than 1

Select elements of the input signal by specifying their indices. The parameter value
can be a scalar or vector of integers ranging from 1 to the number of elements in the
input signal. The indices can be in any order, to enable construction of permutations
and repeats.

## Libraries

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Select elements from vector or matrix input physical signal

The PS Selector block lets you select one or more elements
from the input vector or matrix. Use the **Indices** parameter to select
elements in the input signal. The indices can be in any order, to enable construction of
permutations and repeats.
