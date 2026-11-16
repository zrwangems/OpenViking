---
type: simulink-block
title: 'Systolic QR Decomposition'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Matrix Operations in Simulink / Matrix Factorizations / QR Decomposition'
documentation_page: 'systolicqrdecomposition'
documentation_source_path: 'ref/systolicqrdecomposition.html'
language: en
---

# Systolic QR Decomposition

## Ports

### Input

### **A** — Matrix *A* matrix

Matrix *A*, specified as a matrix. *A* is an
*m*-by-*n* matrix where *m* ≥ 2 and *n* ≥ 2. If *B* is single or double, *A*
must be the same data type as *B*. If *A* is a
fixed-point data type, *A* must be signed, use binary-point scaling,
and have the same word length as *B*. Slope-bias representation is
not supported for fixed-point data types.

#### Dependencies

Use the **Signal
type** parameter to specify the complexity of the input data.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **B** — Matrix *B* matrix

Matrix *B*, specified as a matrix. *B* is an
*m*-by-*p* matrix where *m* ≥ 2. If *A* is single or double, *B*
must be the same data type as *A*. If *B* is a
fixed-point data type, *B* must be signed, use binary-point scaling,
and have the same word length as *A*. Slope-bias representation is
not supported for fixed-point data types.

#### Dependencies

Use the **Signal
type** parameter to specify the complexity of the input data.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **validIn** — Whether inputs are valid scalar

Whether inputs are valid, specified as a Boolean scalar. This control signal
indicates when the data from the **A** and **B** input ports are
valid. When this value is 1 (`true`) and the value at
**readyIn** is 1 (`true`), the block captures the values
on the **A** and **B** input ports. When this value is 0
(`false`), the block ignores the input samples.

#### Tips

After sending a `true`
**validIn** signal, there may be some delay before **readyIn** is
set to `false`. To ensure all data is processed, you must wait
until **readyIn** is set to `false` before sending another
`true`
**validIn** signal.

**Data Types:** `Boolean`

### **readyIn** — Whether downstream block is ready scalar

Whether downstream block is ready, specified as a Boolean scalar. This control
signal monitors the **ready** port of the downstream block. When the
**readyIn** value is `1` (`true`), and
the value at **validOut** is `1` (`true`),
the block outputs data to the downstream block. When the **readyIn** value is
`0` (`false`), the downstream block is not ready
to accept data. The Systolic QR Decomposition block pauses on the
output stage and the **ready** signal remains `0`
(`false`) until the **readyIn** signal is high.

**Data Types:** `Boolean`

### **restart** — Whether to clear internal states scalar

Whether to clear internal states, specified as a Boolean scalar. When this value
is `1` (`true`), the block stops the current
calculation and clears all internal states. When this value is `0`
(`false`) and the **validIn** value is 1
(`true`), the block begins a new subframe.

**Data Types:** `Boolean`
### Output

### **R** — Matrix *R* matrix

Economy size QR decomposition matrix *R*, returned as a matrix.
*R* is an upper triangular matrix. The size of matrix
*R* is *n*-by-*n*.
*R* has the same data type as *A*.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **C** — Matrix *C = Q'B* matrix

Economy size QR decomposition matrix *C*=*Q*'*B*, returned as a matrix. *C* has the same number of
rows as *R*. *C* has the same data type as
*B*.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **validOut** — Whether output data is valid scalar

Whether output data is valid, returned as a Boolean scalar. This control signal
indicates when the data at output ports **R** and **C** is valid.
When this value is `1` (`true`), the block has
successfully computed the **R** and **C** matrices. When this value
is `0` (`false`), the output data is not
valid.

**Data Types:** `Boolean`

### **ready** — Whether block is ready scalar

Whether block is ready, returned as a Boolean scalar. This control signal that
indicates when the block is ready for new input data. When this value is
`1` (`true`) and the **validIn** value is
`1` (`true`), the block accepts input data in the
next time step. When this value is `0` (`false`),
the block ignores input data in the next time step.

#### Tips

After sending a `true`
**validIn** signal, there may be some delay before **ready** is
set to `false`. To ensure all data is processed, you must wait
until **ready** is set to `false` before sending another
`true`
**validIn** signal.

**Data Types:** `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Number of rows in matrices A and B** — Number of rows in matrices *A* and *B* `2` (default) | positive integer-valued scalar

Number of rows in input matrices *A* and *B*,
specified as a positive integer-valued scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `m` |
| **Values:** | `2` (default) | positive integer-valued scalar |
| **Data Types:** | `char` |

### **Number of columns in matrix A** — Number of columns in matrix *A* `2` (default) | positive integer-valued scalar

Number of columns in matrix *A*, specified as a positive
integer-valued scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `n` |
| **Values:** | `2` (default) | positive integer-valued scalar |
| **Data Types:** | `char` |

### **Number of columns in matrix B** — Number of columns in matrix *B* `1` (default) | positive integer-valued scalar

Number of columns in matrix *B*, specified as a positive
integer-valued scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `p` |
| **Values:** | `1` (default) | positive integer-valued scalar |
| **Data Types:** | `char` |

### **Signal type** — Complexity of matrices *A* and *B* `real` (default) | `complex`

Complexity of matrices *A* and *B*, specified as
`real` or `complex`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `complexity` |
| **Values:** | `real` (default) | `complex` |
| **Data Types:** | `char` |

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

Supports fixed-point data types only. Fixed-point data types must use signed
binary-point scaling. Slope and bias scaled types are not supported.

## Version History

**Introduced in R2024a**

## Description

QR decomposition for matrices

The Systolic QR Decomposition block uses QR decomposition to compute
*R* and *C* = *Q*'*B*, where *Q**R* = *A*, and *A* and *B* are matrices. The
least-squares solution to *A**X* = *B* is *X* = *R*\*C*. *R* is an upper triangular matrix and *Q*
is an orthogonal matrix. To compute *C* = *Q'*, set *B* to be the identity matrix.

The systolic implementation to minimizes system latency and increases the throughput.
Systolic implementations require more hardware resources than burst or partial-systolic
implementations.
