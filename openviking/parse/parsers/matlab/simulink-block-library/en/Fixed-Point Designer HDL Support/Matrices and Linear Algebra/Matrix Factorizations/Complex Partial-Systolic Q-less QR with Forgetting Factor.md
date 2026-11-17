---
type: simulink-block
title: 'Complex Partial-Systolic Q-less QR with Forgetting Factor Decomposition'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'complexpartialsystolicqlessqrdecompositionwithforgettingfactor'
documentation_source_path: '../fixedpoint/ref/complexpartialsystolicqlessqrdecompositionwithforgettingfactor.html'
language: en
---

# Complex Partial-Systolic Q-less QR with Forgetting Factor Decomposition

## Ports
```yaml
ports:
- name: A(i,:)
  summary: Rows of matrix *A* vector
  direction: input
  data_types: single | double | fixed point
- name: validIn
  summary: Whether inputs are valid Boolean scalar
  direction: input
  data_types: Boolean
- name: restart
  summary: Whether to clear internal states Boolean scalar
  direction: input
  data_types: Boolean
- name: R
  summary: Matrix *R* scalar | vector
  direction: output
  data_types: single | double | fixed point
- name: validOut
  summary: Whether output data is valid Boolean scalar
  direction: output
  data_types: Boolean
- name: ready
  summary: Whether block is ready Boolean scalar
  direction: output
  data_types: Boolean
```

### Input

### **A(i,:)** — Rows of matrix *A* vector

Rows of matrix *A*, specified as a vector. *A*
is an infinitely tall matrix of streaming data. If *A* is a
fixed-point data type, *A* must be signed, use binary-point scaling,
and have the same word length as *B*. Slope-bias representation is
not supported for fixed-point data types.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **validIn** — Whether inputs are valid `Boolean` scalar

Whether inputs are valid, specified as a Boolean scalar. This control signal
indicates when the data at the `A(i,:)` input port is valid. When
this value is 1 (`true`) and the value at `ready`
is 1 (`true`), the block captures the values at the
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
internal states. When this value is 0 (`false`) and the
`validIn` value is 1 (`true`), the block begins
a new subframe.

**Data Types:** `Boolean`
### Output

### **R** — Matrix *R* scalar | vector

Economy size QR decomposition matrix *R*, returned as a scalar or
vector. *R* is an upper triangular matrix. The size of matrix
*R* is *n*-by-*n*.
*R* has the same data type as *A*.

**Data Types:** `single` | `double` | `fixed point`

### **validOut** — Whether output data is valid `Boolean` scalar

Whether the output data is valid, specified as a Boolean scalar. This control
signal indicates when the data at output port `R` is valid. When
this value is 1 (`true`), the block has successfully computed the
matrix *R*. When this value is 0 (`false`), the
output data is not valid.

**Data Types:** `Boolean`

### **ready** — Whether block is ready `Boolean` scalar

Whether the block is ready, returned as a Boolean scalar. This control signal
indicates when the block is ready for new input data. When this value is
`1` (`true`) and the `validIn`
value is `1` (`true`), the block accepts input data
in the next time step. When this value is `0`
(`false`), the block ignores input data in the next time
step.

After sending a `true`
`validIn` signal, there may be some delay before
`ready` is set to `false`. To ensure all data is
processed, you must wait until `ready` is set to
`false` before sending another `true`
`validIn` signal.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Number of columns in matrix A
  summary: Number of columns in input matrix *A* 4 (default) | positive integer-valued scalar
  group: ''
  block_parameter: n
  type: character vector
  values: positive integer-valued scalar
  default: '4'
- name: Forgetting factor
  summary: Forgetting factor applied after each row of matrix is factored 0.99 (default) | real positive scalar
  group: ''
  block_parameter: forgettingFactor
  type: character vector
  values: positive integer-valued scalar
  default: '0.99'
- name: Regularization parameter
  summary: Regularization parameter 0 (default) | real nonnegative scalar
  group: ''
  block_parameter: regularizationParameter
  type: character vector
  values: real nonnegative scalar
  default: '0'
```

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

### **Forgetting factor** — Forgetting factor applied after each row of matrix is factored 0.99 (default) | real positive scalar

Forgetting factor applied after each row of the matrix is factored, specified as a
real positive scalar. The output is updated as each row of *A* is input
indefinitely.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `forgettingFactor` |
| **Type:** character vector |
| **Values:** positive integer-valued scalar |
| **Default:** `0.99` |

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

| Resource | R2022b | R2023a |
| --- | --- | --- |
| LUT | 162888 | 91496 |
| LUTRAM | 3620 | 2000 |
| Flip Flop | 100309 | 54609 |
| BRAM | 45 | 31 |

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

### R2022a: Support for Tikhonov regularization parameter

The Complex Partial-Systolic Q-less QR Decomposition with Forgetting
Factor block supports the Tikhonov Regularization parameter.

### R2021a: Reduced HDL resource utilization

This block now has an improved algorithm to reduce resource utilization on
hardware-constrained target platforms.

## Description

Q-less QR decomposition for complex-valued matrices with infinite number of rows

The Complex Partial-Systolic Q-less QR Decomposition with Forgetting Factor
block uses QR decomposition to compute the economy size upper-triangular *R*
factor of the QR decomposition *A* = *Q**R*, without computing *Q*. *A* is an
infinitely tall complex-valued matrix representing streaming data.

When the regularization parameter is nonzero, the Complex Partial-Systolic Q-less
QR Decomposition with Forgetting Factor block initializes the first upper-triangular
factor *R* to *λIn* before factoring
in the rows of *A*, where *λ* is the regularization
parameter and *In* =
`eye(n)`.
