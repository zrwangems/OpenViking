---
type: simulink-block
title: 'PS Vector Norm'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psvectornorm'
documentation_source_path: 'ref/psvectornorm.html'
language: en
---

# PS Vector Norm

## Ports
```yaml
ports:
- name: I
  summary: Input physical signal, untyped physical signal
  direction: input
- name: O
  summary: Output physical signal, untyped physical signal
  direction: output
```

### Input

### **I** — Input physical signal, untyped physical signal

Input physical signal specified as a row or column vector or a matrix.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, untyped physical signal

Output physical signal. If the input signal is a vector, then the output signal is
a scalar. If the input signal is a matrix, then the output signal is a vector or
matrix representing the column-wise vector norm of the input matrix.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Compute Euclidean norm of vector or matrix physical signal

The PS Vector Norm block computes the Euclidean norm of a
vector or matrix input physical signal:

y=sqrt(dot(u,u))

where:

- *y* is the physical signal at the output port
  **O**.
- *u* is the physical signal at the input port
  **I**.

If the input signal is a matrix, then the block computes the column-wise vector
norm.
