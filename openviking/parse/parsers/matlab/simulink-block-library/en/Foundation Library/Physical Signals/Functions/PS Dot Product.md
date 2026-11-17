---
type: simulink-block
title: 'PS Dot Product'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'psdotproduct'
documentation_source_path: 'ref/psdotproduct.html'
language: en
---

# PS Dot Product

## Ports
```yaml
ports:
- name: I1
  summary: Input physical signal, untyped physical signal
  direction: input
- name: I2
  summary: Input physical signal, untyped physical signal
  direction: input
- name: O
  summary: Output physical signal, untyped physical signal
  direction: output
```

### Input

### **I1** — Input physical signal, untyped physical signal

First input physical signal specified as a row or column vector or a
matrix.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **I2** — Input physical signal, untyped physical signal

Second input physical signal specified as a vector or matrix of the same size as
**I1**.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, untyped physical signal

Output physical signal, scalar.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Physical Signals / Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Calculate scalar dot product of two vector or matrix physical signals

The PS Dot Product block calculates the scalar dot product
of two vector or matrix physical signals:

y=dot(u1,u2)

where:

- *y* is the physical signal at the output port
  **O**.
- *u1* is the physical signal at the input port
  **I1**.
- *u2* is the physical signal at the input port
  **I2**.

The two input physical signals can be either vectors or matrices:

- If *u1* and *u2* are vectors, then they must have
  the same length.
- If *u1* and *u2* are matrices, then they must have
  the same size and the block computes the column-wise dot product.

The unit at the output port is determined by unit propagation rules. For more information,
see Physical Signal Unit Propagation.
