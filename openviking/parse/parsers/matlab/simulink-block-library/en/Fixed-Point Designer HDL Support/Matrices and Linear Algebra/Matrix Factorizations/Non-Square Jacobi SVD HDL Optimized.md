---
type: simulink-block
title: 'Non-Square Jacobi SVD HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'nonsquarejacobisvdhdloptimized'
documentation_source_path: '../fixedpoint/ref/nonsquarejacobisvdhdloptimized.html'
language: en
---

# Non-Square Jacobi SVD HDL Optimized

## Ports
```yaml
ports:
- name: A(i,:)
  summary: Rows of matrix *A* vector
  direction: input
  data_types: single | double | fixed point
- name: validIn
  summary: Whether input is valid scalar
  direction: input
  data_types: Boolean
- name: readyIn
  summary: Whether downstream block is ready scalar
  direction: input
  data_types: Boolean
- name: restart
  summary: Whether to clear internal states scalar
  direction: input
  data_types: Boolean
- name: s
  summary: Singular values column vector
  direction: output
  data_types: single | double | fixed point
- name: U
  summary: Left singular vectors unitary n-by-n matrix
  direction: output
  data_types: single | double | fixed point
- name: V
  summary: Right singular vectors unitary n-by-n matrix
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

Row of matrix *A*, specified as a vector. *A* is
a *m*-by-*n* matrix where *m* > 2, *n* ≥ 2, and *m* > *n*.

If *A* is a fixed-point data type, *A* must be
signed and use binary-point scaling. Slope-bias representation is not supported for
fixed-point data types.

#### Tips

The output **U**
matrix is orthonormal up to the rank of input matrix *A*. For more
information, see Limitations.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **validIn** — Whether input is valid scalar

Whether input is valid, specified as a Boolean scalar. This control signal
indicates when the data from the `A` input port is valid. When this
value is `1` (`true`) and the value at
`ready` is `1` (`true`), the
block captures the values at the `A` input port. When this value is
`0` (`false`), the block ignores the input
samples.

#### Tips

After sending a `true`
`validIn` signal, a delay may occur before the
`ready` signal is `false`. To ensure all data is
processed, you must wait until the `ready` signal is
`false` before sending another `true`
`validIn` signal.

**Data Types:** `Boolean`

### **readyIn** — Whether downstream block is ready scalar

Whether downstream block is ready, specified as a `Boolean`
scalar. This control signal monitors the `ready` port of the
downstream block. When the `readyIn` value is `1`
(`true`), and the value at `validOut` is
`1` (`true`), the block outputs data to the
downstream block. When the `readyIn` value is `0`
(`false`), the downstream block is not ready to accept data. The
Non-Square Jacobi SVD HDL Optimized block pauses on the output stage
and the `ready` signal remains `0`
(`false`) until the `readyIn` signal is
high.

**Data Types:** `Boolean`

### **restart** — Whether to clear internal states scalar

Whether to clear internal states, specified as a Boolean scalar. When this value
is 1 (`true`), the block stops the current calculation and clears all
internal states. When this value is 0 (`false`) and the
`validIn` value is 1 (`true`), the block begins a
new subframe.

**Data Types:** `Boolean`
### Output

### **s** — Singular values column vector

Singular values, returned as a column vector of length `n`. The
Singular Values are nonnegative and returned in descending
order such that `s(1) >= s(2) >= ... >= s(n)`. Singular values are
returned with the same data type as the input matrix `A`.

**Data Types:** `single` | `double` | `fixed point`

### **U** — Left singular vectors unitary `n`-by-`n` matrix

Left singular vectors, returned as a unitary
`n`-by-`n` matrix.

For fixed-point and scaled-double inputs, `U` is returned as a
signed fixed-point or scaled-double `fi` with the same word length as
`A` and fraction length equal to two less than the word length.
One of these integer bits is used for the sign. The other integer bit allows
`+1` to be represented exactly.

For floating-point input, `U` has the same data type as
`A`.

#### Tips

The output **U**
matrix is orthonormal up to the rank of input matrix *A*. For more
information, see Limitations.

#### Dependencies

To enable this port, set the **Select
outputs** parameter to `UsV` or
`Us`.

**Data Types:** `single` | `double` | `fixed point`

### **V** — Right singular vectors unitary `n`-by-`n` matrix

Right singular vectors, returned as a unitary
`n`-by-`n` matrix.

For fixed-point and scaled-double inputs, `V` is returned as a
signed fixed-point or scaled-double `fi` with the same word length as
`A` and fraction length equal to two less than the word length.
One of these integer bits is used for the sign. The other integer bit allows
`+1` to be represented exactly.

For floating-point input, `V` has the same data type as
`A`.

#### Dependencies

To enable this port, set the **Select outputs** parameter to
`UsV` or `sV`.

**Data Types:** `single` | `double` | `fixed point`

### **validOut** — Whether output data is valid `Boolean` scalar

Whether the output data is valid, returned as a Boolean scalar. This control
signal indicates when the data at the output ports `U`,
`S`, and `V` are valid. When this value is
`1` (`true`), the output data is valid. When this
value is `0` (`false`), the output data is not
valid. Transfer of data to the downstream block occurs only when both the
`validOut` and `readyIn` signals are high.

**Data Types:** `Boolean`

### **ready** — Whether block is ready `Boolean` scalar

Whether the block is ready, returned as a Boolean scalar. This control signal
indicates when the block is ready for new input data. When this value is
`1` (`true`) and the `validIn`
value is `1` (`true`), the block accepts input data
in the next time step. When this value is `0`
(`false`), the block ignores input data in the next time
step.

#### Tips

After sending a `true`
`validIn` signal, there may be some delay before the
`ready` signal is `false`. To ensure all data is
processed, you must wait until the `ready` signal is
`false` before sending another `true`
`validIn` signal.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Number of rows in matrix A
  summary: Number of rows in *m*-by-*n* matrix *A* 8 (default) | integer-valued scalar where m > 2 and m > n
  group: ''
  block_parameter: m
  values: 8 (default) | integer-valued scalar where m > 2 and m > n
- name: Number of columns in matrix A
  summary: Number of columns in *m*-by-*n* matrix *A* 4 (default) | integer-valued scalar where n ≥ 2 and m > n
  group: ''
  block_parameter: n
  values: 4 (default) | integer-valued scalar where n ≥ 2 and m > n
- name: Number of Jacobi iterations
  summary: Number of iterations of Jacobi algorithm 10 (default) | positive integer
  group: ''
  block_parameter: nIterations
  values: 10 (default) | positive integer
- name: Select outputs
  summary: Block outputs UsV (default) | Us | sV | s
  group: ''
  block_parameter: outputOption
  values: UsV (default) | Us | sV | s
- name: Signal type
  summary: Complexity of input matrix *A* real (default) | complex
  group: ''
  block_parameter: complexity
  values: real (default) | complex
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Number of rows in matrix A** — Number of rows in *m*-by-*n* matrix *A* `8` (default) | integer-valued scalar where `m > 2` and `m > n`

Number of rows in *m*-by-*n* matrix
*A*, specified as an integer-valued scalar where *m* > 2 and *m* > *n*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `m` |
| **Values:** | 8 (default) | integer-valued scalar where `m > 2` and `m > n` |
| **Data Types:** | `char` | `string` |

### **Number of columns in matrix A** — Number of columns in *m*-by-*n* matrix *A* `4` (default) | integer-valued scalar where `n ≥ 2` and `m > n`

Number of columns in *m*-by-*n* matrix
*A*, specified as an integer-valued scalar where *n* ≥ 2 and *m* > *n*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `n` |
| **Values:** | 4 (default) | integer-valued scalar where `n ≥ 2` and `m > n` |
| **Data Types:** | `char` | `string` |

### **Number of Jacobi iterations** — Number of iterations of Jacobi algorithm `10` (default) | positive integer

Number of iterations of the Jacobi algorithm, specified as a positive
integer.

#### Tips

- Most sources indicate that 10 iterations is sufficient for the Jacobi
  algorithm to converge [7][8][9][10].
- When the input is an *m*-by-2 matrix, the SVD has a
  closed-form solution and does not require iterative computation. In this case, set
  the **Number of Jacobi iterations** to `1` to
  minimize utilization and latency.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `nIterations` |
| **Values:** | `10` (default) | positive integer |
| **Data Types:** | `char` | `string` |

### **Select outputs** — Block outputs `UsV` (default) | `Us` | `sV` | `s`

Block outputs, specified as `UsV`,
`Us`, `sV`, or
`s`.

#### Tips

This parameter determines the number of outputs on the block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `outputOption` |
| **Values:** | `UsV` (default) | `Us` | `sV` | `s` |
| **Data Types:** | `char` | `string` |

### **Signal type** — Complexity of input matrix *A* `real` (default) | `complex`

Complexity of the input matrix *A*, specified as
`real`, or `complex`.

#### Tips

This parameter determines whether the Non-Square Jacobi HDL
Optimized block uses a Real
Partial-Systolic QR Decomposition block or a Complex
Partial-Systolic QR Decomposition block to preprocess the input.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `complexity` |
| **Values:** | `real` (default) | `complex` |
| **Data Types:** | `char` | `string` |
## Libraries

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Matrix Factorizations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**Note**

When generating code for large matrices set the configuration parameter
**HDL Code Generation > Global Settings > Ports** tab
**Check for DUT pin count exceeding I/O Threshold** to
`Warning` or `None`. To learn more about this setting,
see Check for DUT pin count exceeding I/O Threshold (HDL Coder).

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

Supports fixed-point data types only. Fixed-point data types must use signed
binary-point scaling. Slope and bias scaling and unsigned fixed-point types are not
supported.

## Version History

**Introduced in R2023b**

## Description

Fixed-point singular value decomposition

Use the Non-Square Jacobi SVD HDL Optimized block to perform singular value
decomposition (SVD) on non-square matrices using QR decomposition and the two-sided Jacobi
algorithm. This block consists of a Real Partial-Systolic QR
Decomposition or Complex Partial-Systolic
QR Decomposition block, depending on your configuration, and a Square Jacobi SVD HDL
Optimized. Given a matrix *A* with more rows than columns, the
Non-Square Jacobi SVD HDL Optimized block uses QR decomposition to preprocess
the input, then uses the two-sided Jacobi method to produce a vector *s* of
nonnegative elements and unitary matrices *U* and *V* such
that `A =
U*diag(s)*V'`.

**Note**

For square matrices, use the Square Jacobi SVD HDL
Optimized block.
