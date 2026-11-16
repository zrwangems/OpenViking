---
type: simulink-block
title: 'Sparse Second Order'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Dynamic System Models / Linear System Representation / Sparse State-Space Models'
documentation_page: 'sparsesecondorder'
documentation_source_path: 'ref/sparsesecondorder.html'
language: en
---

# Sparse Second Order

## Ports

### Input

### **Input 1** — Input signal scalar | vector

Real-valued input vector of type `double` whose size is equal the
number of columns in the **B** and **D**
matrices.

**Data Types:** `double`
### Output

### **Output 1** — Output vector scalar | vector

Real-valued output vector of type `double` whose size is equal to
the number of rows in the **F**, **G** and
**D** matrices.

**Data Types:** `double`

## Parameters

### **M (mass)** — Mass matrix 1 (default) | scalar | `Nq`-by-`Nq` sparse matrix

Mass matrix, specified as an `Nq`-by-`Nq` sparse
matrix where, `Nq` is the number of nodes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`M` |
| **Type:** scalar, square sparse matrix |
| **Default:** `1` |

### **C (damping)** — Damping matrix 0 (default) | scalar | `Nq`-by-`Nq` sparse matrix

Damping matrix, specified as an `Nq`-by-`Nq`
sparse matrix where, `Nq` is the number of nodes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`C` |
| **Type:** scalar, square sparse matrix |
| **Default:** `0` |

### **K (stiffness)** — Stiffness matrix 1 (default) | scalar | `Nq`-by-`Nq` sparse matrix

Stiffness matrix, specified as an `Nq`-by-`Nq`
sparse matrix where, `Nq` is the number of nodes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`K` |
| **Type:** scalar, square sparse matrix |
| **Default:** `1` |

### **B** — Input-to-state matrix 1 (default) | scalar | `Nq`-by-`Nu` sparse matrix

Input-to-state matrix, specified as an
`Nq`-by-`Nu` sparse matrix where,
`Nq` is the number of nodes and `Nu` is the number
of inputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`B` |
| **Type:** scalar, sparse matrix |
| **Default:** `1` |

### **F** — Displacement-to-output matrix 1 (default) | scalar | `Ny`-by-`Nq` sparse matrix

Displacement-to-output matrix, specified as an
`Ny`-by-`Nq` sparse matrix where,
`Nq` is the number of nodes and `Ny` is the number
of outputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`F` |
| **Type:** scalar, sparse matrix |
| **Default:** `1` |

### **G** — Velocity-to-output matrix 0 (default) | scalar | `Ny`-by-`Nq` sparse matrix

Velocity-to-output matrix, specified as an
`Ny`-by-`Nq` sparse matrix where,
`Nq` is the number of nodes and `Ny` is the number
of outputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`G` |
| **Type:** scalar, sparse matrix |
| **Default:** `0` |

### **D** — Input-to-output matrix 0 (default) | scalar | `Ny`-by-`Nu` sparse matrix

Input-to-output matrix, specified as an
`Ny`-by-`Nu` sparse matrix where,
`Ny` is the number of outputs and `Nu` is the number
of inputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`D` |
| **Type:** scalar, sparse matrix |
| **Default:** `0` |

### **Initial position q(0)** — Initial values for displacement vector 0 (default) | scalar | vector of doubles

Initial values for displacement vector q, specified as a vector of doubles. q and q˙ are the displacement and velocity vectors that make up the state
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`q0` |
| **Type:** scalar, vector of doubles |
| **Default:** `0` |

### **Initial velocity q'(0)** — Initial values for velocity vector 0 (default) | scalar | vector of doubles

Initial values for velocity vector q˙, specified as a vector of doubles. q and q˙ are the displacement and velocity vectors that make up the state
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`dq0` |
| **Type:** scalar, vector of doubles |
| **Default:** `0` |

**Note**

For linearization with Simulink
Control Design, the linearized model is a `mechss` model
object when the `Sparse Second Order` block is present in your Simulink model.

For more information, see Sparse Model Basics.

For an example, see Linearize Simulink Model to a Sparse Second-Order Model Object.

## Libraries

Control System Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

## Version History

**Introduced in R2020b**

## Description

Represent sparse second-order models in Simulink

The Sparse Second Order block lets you represent second-order sparse
state-space models, in Simulink®. Such sparse models arise from finite element analysis (FEA) and are useful in
fields like structural analysis, fluid flow, heat transfer and electromagnetics. The resultant
matrices from this type of modeling are quite large with a sparse pattern. In continuous time,
a second-order sparse mass-spring-damper state-space model is represented in the following form:

M q¨(t)+C q˙(t)+K q(t) = B u(t)y(t) = F q(t)+G q˙(t)+D u(t)

Here, the full state vector is given by [q,q˙], where q and q˙ are the displacement and velocity vectors. `u` and
`y` represent the inputs and outputs, respectively. `M`,
`C`, and `K` represent the mass, damping and stiffness
matrices, respectively. `B` is the input matrix, while `F`
and `G` are the output matrices resulting from the two components of the
state vector. `D` is the input-to-output matrix.
