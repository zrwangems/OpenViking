---
type: simulink-block
title: 'Complex Partial-Systolic QR Decomposition'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'complexpartialsystolicqrdecomposition'
documentation_source_path: '../fixedpoint/ref/complexpartialsystolicqrdecomposition.html'
language: en
---

# Complex Partial-Systolic QR Decomposition

## Ports

### Input

### **A(i,:)** — Rows of matrix *A* vector

Rows of matrix *A*, specified as a vector. *A*
is an *m*-by-*n* matrix where *m* ≥ 2 and *n* ≥ 2. If *B* is single or double, *A*
must be the same data type as *B*. If *A* is a
fixed-point data type, *A* must be signed, use binary-point scaling,
and have the same word length as *B*. Slope-bias representation is
not supported for fixed-point data types.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **B(i,:)** — Rows of matrix *B* vector

Rows of matrix *B*, specified as a vector. *B*
is an *m*-by-*p* matrix where *m* ≥ 2. If *A* is single or double, *B*
must be the same data type as *A*. If *B* is a
fixed-point data type, *B* must be signed, use binary-point scaling,
and have the same word length as *A*. Slope-bias representation is
not supported for fixed-point data types.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **validIn** — Whether inputs are valid `Boolean` scalar

Whether inputs are valid, specified as a Boolean scalar. This control signal
indicates when the data from the `A(i,:)` and
`B(i,:)` input ports are valid. When this value is 1
(`true`) and the value at `ready` is 1
(`true`), the block captures the values on the
`A(i,:)` and `B(i,:)` input ports. When this
value is 0 (`false`), the block ignores the input samples.

After sending a `true`
`validIn` signal, there may be some delay before
`ready` is set to `false`. To ensure all data is
processed, you must wait until `ready` is set to
`false` before sending another `true`
`validIn` signal.

**Data Types:** `Boolean`

### **restart** — Whether to clear internal states `Boolean` scalar

Whether to clear internal states, specified as a Boolean scalar. When this value
is 1 (`true`), the block stops the current calculation and clears all
internal states. When this value is 0 (`false`), and the
`validIn` value is 1 (`true`), the block begins
a new subframe.

**Data Types:** `Boolean`
### Output

### **R** — Matrix *R* matrix

Economy-size QR decomposition matrix *R*, returned as a matrix.
*R* is an upper triangular matrix. The size of matrix
*R* is *n*-by-*n*.
*R* has the same data type as *A*.

**Data Types:** `single` | `double` | `fixed point`

### **C** — Matrix *C*=*Q*'*B* matrix

Economy-size QR decomposition matrix *C*=*Q*'*B*, returned as a matrix or vector. *C* has the same
number of rows as *R*. *C* has the same data type as
*B*.

**Data Types:** `single` | `double` | `fixed point`

### **validOut** — Whether output data is valid `Boolean` scalar

Whether the output data is valid, returned as a Boolean scalar. This control
signal indicates when the data at output ports `R` and
`C` is valid. When this value is 1 (`true`), the
block has successfully computed the *R* and *C*
matrices. When this value is 0 (`false`), the output data is not
valid.

**Data Types:** `Boolean`

### **ready** — Whether block is ready `Boolean` scalar

Whether the block is ready, returned as a Boolean scalar. This control signal
indicates when the block is ready for new input data. When this value is 1
(`true`), and the `validIn` value is 1
(`true`), the block accepts input data in the next time step. When
this value is 0 (`false`), the block ignores input data in the next
time step.

After sending a `true`
`validIn` signal, there may be some delay before
`ready` is set to `false`. To ensure all data is
processed, you must wait until `ready` is set to
`false` before sending another `true`
`validIn` signal.

**Data Types:** `Boolean`

## Parameters

### **Number of rows in matrices A and B** — Number of rows in input matrices A and B `4` (default) | positive integer-valued scalar

The number of rows in input matrices *A* and *B*,
specified as a positive integer-valued scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `m` |
| **Type:** character vector |
| **Values:** positive integer-valued scalar |
| **Default:** `4` |

### **Number of columns in matrix A** — Number of columns in input matrix A `4` (default) | positive integer-valued scalar

The number of columns in input matrix *A*, specified as a positive
integer-valued scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `n` |
| **Type:** character vector |
| **Values:** positive integer-valued scalar |
| **Default:** `4` |

### **Number of columns in matrix B** — Number of columns in input matrix B `1` (default) | positive integer-valued scalar

The number of columns in input matrix *B*, specified as a positive
integer-valued scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `p` |
| **Type:** character vector |
| **Values:** positive integer-valued scalar |
| **Default:** `1` |

### **Regularization parameter** — Regularization parameter 0 (default) | nonnegative scalar

Regularization parameter, specified as a nonnegative scalar. Small, positive values
of the regularization parameter can improve the conditioning of the problem and reduce
the variance of the estimates. While biased, the reduced variance of the estimate often
results in a smaller mean squared error when compared to least-squares estimates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `regularizationParameter` |
| **Type:** character vector |
| **Values:** positive integer-valued scalar |
| **Default:** `0` |

## Libraries

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Matrix Factorizations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Slope-bias representation is not supported for fixed-point data types.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

Supports fixed-point data types only.

## Version History

**Introduced in R2020b**

### R2023a: Smart unrolling for improved resource utilization

When you update the diagram, the loop which composes the partial-systolic pipeline is
unrolled. This updated internal architecture removes dead operations in simulation and
generated code, resulting in a significant decrease in the number of hardware resources
required. This block simulates with clock and bit-true fidelity with respect to library
versions of these blocks in previous releases.

| Resource | Usage in R2022b | Usage in R2023a |
| --- | --- | --- |
| LUT | 177813 | 108464 |
| LUTRAM | 6620 | 5000 |
| Flip Flop | 113857 | 68404 |

This example data was generated by synthesizing the block on a Xilinx
Zynq-7 ZC706 evaluation board (-2 speed grade).

The following parameters were used for synthesis.

- Block parameters:

  - `m = 10`
  - `n = 10`
  - `p = 1`
  - Matrix *A* dimension: 10-by-10
  - Matrix *B* dimension: 10-by-1
- Input data type: `sfix18_En12`

### R2021a: Reduced HDL resource utilization

This block now has an improved algorithm to reduce resource utilization on
hardware-constrained target platforms.

## Description

QR decomposition for complex-valued matrices

The Complex Partial-Systolic QR Decomposition block uses QR decomposition
to compute *R* and *C* = *Q*'*B*, where *Q**R* = *A*, and *A* and *B* are complex-valued
matrices. The least-squares solution to *A**x* = *B* is *x* = *R*\*C*. *R* is an upper triangular matrix and *Q*
is an orthogonal matrix. To compute *C* = *Q'*, set *B* to be the identity matrix.

When Regularization parameter is nonzero, the
Complex Partial-Systolic QR Decomposition block transforms [λInA] in-place to R=Q'[λInA] and [0n,pB] in-place to C=Q'[0n,pB] where *λ* is the regularization parameter, QR is the
economy size QR decomposition of [λInA], *A* is an *m*-by-*n*
matrix, *p* is the number of columns in *B*,
*In* =
`eye(n)`, and
*0n,p* =
`zeros(n,p)`.
