---
type: simulink-block
title: 'Real Burst Q-less QR Decomposition Whole R Output'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'realburstqlessqrdecompositionwholeroutput'
documentation_source_path: '../fixedpoint/ref/realburstqlessqrdecompositionwholeroutput.html'
language: en
---

# Real Burst Q-less QR Decomposition Whole R Output

## Ports

### Input

### **A(i,:)** — Rows of real matrix *A* vector

Rows of real matrix *A*, specified as a vector.
*A* is an *m*-by-*n* matrix where *m* ≥ 2 and *n* ≥ 2. If *A* is a fixed-point data type,
*A* must be signed and use binary-point scaling. Slope-bias
representation is not supported for fixed-point data types.

**Data Types:** `single` | `double` | `fixed point`

### **validIn** — Whether inputs are valid `Boolean` scalar

Whether inputs are valid, specified as a Boolean scalar. This control signal
indicates when the data from the `A(i,:)` input port is valid. When
this value is 1 (`true`) and the value of `ready` is
1 (`true`), the block captures the values at the
`A(i,:)` input port. When this value is 0
(`false`), the block ignores the input samples.

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
internal states. When this value is 0 (`false`) and the value at
`validIn` is 1 (`true`), the block begins a new
subframe.

**Data Types:** `Boolean`
### Output

### **R** — Economy size QR decomposition matrix *R* vector

Economy size QR decomposition matrix *R*, returned as a vector.
*R* is an upper triangular matrix. The size of matrix
*R* is `min(m,n)`-by-`n`.
*R* has the same data type as *A*.

**Data Types:** `single` | `double` | `fixed point`

### **validOut** — Whether output data is valid `Boolean` scalar

Whether the output data is valid, specified as a Boolean scalar. This control
signal indicates when the data at output port `R(i,:)` is valid. When
this value is 1 (`true`), the block has successfully computed the
matrix *R*. When this value is 0 (`false`), the
output data is not valid.

**Data Types:** `Boolean`

### **ready** — Whether block is ready `Boolean` scalar

Whether the block is ready, returned as a Boolean scalar. This control signal
indicates when the block is ready for new input data. When this value is
`1` (`true`) and `validIn` is
`1` (`true`), the block accepts input data in the
next time step. When this value is `0` (`false`),
the block ignores input data in the next time step.

After sending a `true`
`validIn` signal, there may be some delay before
`ready` is set to `false`. To ensure all data is
processed, you must wait until `ready` is set to
`false` before sending another `true`
`validIn` signal.

**Data Types:** `Boolean`

## Parameters

### **Number of rows in matrix A** — Number of rows in input matrix *A* `4` (default) | positive integer-valued scalar

Number of rows in input matrix *A*, specified as a positive
integer-valued scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `m` |
| **Type:** character vector |
| **Values:** positive integer-valued scalar |
| **Default:** `4` |

### **Number of columns in matrix A** — Number of columns in input matrix *A* `4` (default) | positive integer-valued scalar

Number of columns in input matrix *A*, specified as a positive
integer-valued scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `n` |
| **Type:** character vector |
| **Values:** positive integer-valued scalar |
| **Default:** `4` |

### **Regularization parameter** — Regularization parameter `0` (default) | real nonnegative scalar

Regularization parameter, specified as a real nonnegative scalar. Small, positive
values of the regularization parameter can improve the conditioning of the problem and
reduce the variance of the estimates. While biased, the reduced variance of the estimate
often results in a smaller mean squared error when compared to least-squares
estimates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `regularizationParameter` |
| **Type:** character vector |
| **Values:** real nonnegative scalar |
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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2022b**

## Description

Q-less QR decomposition for real-valued matrices

The Real Burst Q-less QR Decomposition Whole R Output block uses QR
decomposition to compute the economy size upper-triangular *R* factor of the
QR decomposition *A* = *Q**R*, where *A* is a real-valued matrix, without computing
*Q*. The solution to *A*'*A**x* =
*B* is *x* =
*R*\*R*'\*b*.

When Regularization parameter is nonzero, the
Real Burst Q-less QR Decomposition Whole R Output block computes the
upper-triangular factor *R* of the economy size QR decomposition of [λInA] where *λ* is the regularization parameter.
