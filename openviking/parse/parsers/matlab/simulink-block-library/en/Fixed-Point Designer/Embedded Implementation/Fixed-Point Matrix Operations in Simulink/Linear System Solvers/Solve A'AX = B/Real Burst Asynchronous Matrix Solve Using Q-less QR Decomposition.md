---
type: simulink-block
title: 'Real Burst Asynchronous Matrix Solve Using Q-less QR Decomposition'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: "Embedded Implementation / Fixed-Point Matrix Operations in Simulink / Linear System Solvers / Solve A'AX = B"
documentation_page: 'realburstasynchronousmatrixsolveusingqlessqrdecomposition'
documentation_source_path: 'ref/realburstasynchronousmatrixsolveusingqlessqrdecomposition.html'
language: en
---

# Real Burst Asynchronous Matrix Solve Using Q-less QR Decomposition

## Ports

### Input

### **A(i,:)** — Rows of real matrix *A* vector

Rows of real matrix *A*, specified as a vector.
*A* is an *m*-by-*n* matrix where *m* ≥ 2 and *m* ≥ *n*. If *B* is single or double, *A*
must be the same data type as *B*. If *A* is a
fixed-point data type, *A* must be signed, use binary-point scaling,
and have the same word length as *B*. Slope-bias representation is
not supported for fixed-point data types.

**Data Types:** `single` | `double` | `fixed point`

### **B** — Rows of real matrix *B* vector

Rows of real matrix *B*, specified as a vector.
*B* is an *n*-by-*p* matrix where *n* ≥ 2. If *A* is single or double, *B*
must be the same data type as *A*. If *B* is a
fixed-point data type, *B* must be signed, use binary-point scaling,
and have the same word length as *A*. Slope-bias representation is
not supported for fixed-point data types.

**Data Types:** `single` | `double` | `fixed point`

### **validInA** — Whether `A(i,:)` input is valid `Boolean` scalar

Whether `A(i,:)` input is valid, specified as a Boolean scalar.
This control signal indicates when the data from the `A(i,:)` input
port is valid. When this value is `1` (`true`) and
the `readyA` value is `1` (`true`),
the block captures the values at the `A(i,:)` input port. When this
value is `0` (`false`), the block ignores the input
samples.

After sending a `true`
`validInA` signal, there may be some delay before
`readyA` is set to `false`. To ensure all data is
processed, you must wait until `readyA` is set to
`false` before sending another `true`
`validInA` signal.

**Data Types:** `Boolean`

### **validInB** — Whether `B` input is valid `Boolean` scalar

Whether `B` input is valid, specified as a Boolean scalar. This
control signal indicates when the data from the `B` input port is
valid. When this value is `1` (`true`) and the
`readyB` value is `1` (`true`),
the block captures the values at the `B` input port. When this value
is `0` (`false`), the block ignores the input
samples.

After sending a `true`
`validInB` signal, there may be some delay before
`readyB` is set to `false`. To ensure all data is
processed, you must wait until `readyB` is set to
`false` before sending another `true`
`validInB` signal.

**Data Types:** `Boolean`

### **restart** — Whether to clear internal states `Boolean` scalar

Whether to clear internal states, specified as a Boolean scalar. When this value
is 1 (`true`), the block stops the current calculation and clears all
internal states. When this value is 0 (`false`) and the value at
`validIn` is 1 (`true`), the block begins a new
subframe.

**Data Types:** `Boolean`
### Output

### **X** — Matrix *X* matrix | vector

Matrix *X*, returned as a matrix or vector.

**Data Types:** `single` | `double` | `fixed point`

### **validOut** — Whether output data is valid `Boolean` scalar

Whether the output data is valid, specified as a Boolean scalar. This control
signal indicates when the data at output port `X` is valid. When this
value is 1 (`true`), the block has successfully computed the matrix
*X*. When this value is 0 (`false`), the output
data is not valid.

**Data Types:** `Boolean`

### **readyA** — Whether block is ready for input `A(i,:)` `Boolean` scalar

Whether block is ready for input `A(i,:)`, returned as a Boolean
scalar. This control signal indicates when the block is ready for new input data. When
this value is `1` (`true`) and
`validInA` is `1` (`true`), the
block accepts input data in the next time step. When this value is
`0` (`false`), the block ignores input data in the
next time step.

After sending a `true`
`validInA` signal, there may be some delay before
`readyA` is set to `false`. To ensure all data is
processed, you must wait until `readyA` is set to
`false` before sending another `true`
`validInA` signal.

**Data Types:** `Boolean`

### **readyB** — Whether block is ready for input `B` `Boolean` scalar

Whether block is ready for input `B`, returned as a Boolean
scalar. This control signal indicates when the block is ready for new input data. When
this value is `1` (`true`) and
`validInB` is `1` (`true`), the
block accepts input data in the next time step. When this value is
`0` (`false`), the block ignores input data in the
next time step.

After sending a `true`
`validInB` signal, there may be some delay before
`readyB` is set to `false`. To ensure all data is
processed, you must wait until `readyB` is set to
`false` before sending another `true`
`validInB` signal.

**Data Types:** `Boolean`

## Parameters

### **Number of rows in matrix A** — Number of rows in matrix *A* `4` (default) | positive integer-valued scalar

Number of rows in matrix *A*, specified as a positive
integer-valued scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `m` |
| **Type:** character vector |
| **Values:** positive integer-valued scalar |
| **Default:** `4` |

### **Number of columns in matrix A and rows in matrix B** — Number of columns in matrix *A* and rows in matrix *B* `4` (default) | positive integer-valued scalar

Number of columns in matrix *A* and rows in matrix
*B*, specified as a positive integer-valued scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `n` |
| **Type:** character vector |
| **Values:** positive integer-valued scalar |
| **Default:** `4` |

### **Number of columns in matrix B** — Number of columns in matrix *B* `1` (default) | positive integer-valued scalar

Number of columns in matrix *B*, specified as a positive
integer-valued scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `p` |
| **Type:** character vector |
| **Values:** positive integer-valued scalar |
| **Default:** `1` |

### **Regularization parameter** — Regularization parameter 0 (default) | real nonnegative scalar

Regularization parameter, specified as a nonnegative scalar. Small, positive values
of the regularization parameter can improve the conditioning of the problem and reduce
the variance of the estimates. While biased, the reduced variance of the estimate often
results in a smaller mean squared error when compared to least-squares estimates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `regularizationParameter` |
| **Type:** character vector |
| **Values:** real nonnegative scalar |
| **Default:** `0` |

### **Output datatype** — Data type of output matrix *X* `fixdt(1,18,14)` (default) | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

Data type of the output matrix *X*, specified as
`fixdt(1,18,14)`, `double`,
`single`, `fixdt(1,16,0)`, or as a user-specified
data type expression. The type can be specified directly, or expressed as a data type
object such as `Simulink.NumericType`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputType` |
| **Type:** character vector |
| **Values:** `'fixdt(1,18,14)'` | `'double'` | `'single'` | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **Default:** `'fixdt(1,18,14)'` |

## Libraries

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Linear System Solvers

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

Compute the value of X in the equation A ' A X = B for real-valued matrices using asynchronous Q-less QR decomposition

The Real Burst Asynchronous Matrix Solve Using Q-less QR Decomposition
block solves the system of linear equations *A*'*A**X* =
*B* using asynchronous Q-less QR decomposition, where *A* and
*B* are real-valued matrices.

When Regularization parameter is nonzero, the
Real Burst Asynchronous Matrix Solve Using Q-less QR Decomposition block
solves the matrix equation

[λInA]'⋅[λInA]X=(λ2In+A'A)X=B

where *λ* is the regularization parameter,
*A* is an *m*-by-*n* matrix, and
*In* =
`eye(n)`.

This block operates asynchronously. The forward- and backward-substitution and Q-less QR
decomposition run independently using the latest *R* and *B*
matrices.
