---
type: simulink-block
title: 'State-Space'
family: 'simulink-extras'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Additional Linear'
documentation_page: 'statespace'
documentation_source_path: 'slref/statespace.html'
language: en
---

# State-Space

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Real-valued input vector of type `double`, where the
width equals the number of columns in the **B** and
**D** matrices. For more information, see Description.

**Data Types:** `double`
### Output

### **Port\_1** — Output vector scalar | vector

Real-valued output vector of data type `double`, with
width equal to the number of rows in the **C** and
**D** matrices. For more information, see Description.

**Data Types:** `double`

## Parameters

### **A** — Matrix coefficient, A `1` (default) | scalar | vector | matrix | sparse matrix

Specify the matrix coefficient `A`, as a real-valued
*n*-by-*n* matrix, where
*n* is the number of states. For more information on
the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `A` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix | sparse matrix |
| **Default:** `'1'` |

### **B** — Matrix coefficient, B `1` (default) | scalar | vector | matrix | sparse matrix

Specify the matrix coefficient `B`, as a real-valued
*n*-by-*m* matrix, where
*n* is the number of states and *m* is
the number of inputs. For more information on the matrix coefficients, see
Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `B` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix | sparse matrix |
| **Default:** `'1'` |

### **C** — Matrix coefficient, C `1` (default) | scalar | vector | matrix | sparse matrix

Specify the matrix coefficient **C** as a real-valued
*r*-by-*n* matrix, where
*r* is the number of outputs and *n*
is the number of states. For more information on the matrix coefficients,
see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `C` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix | sparse matrix |
| **Default:** `'1'` |

### **D** — Matrix coefficient, D `1` (default) | scalar | vector | matrix | sparse matrix

Specify the matrix coefficient **D** as a real-valued
*r*-by-*m* matrix, where
*r* is the number of outputs and *m*
is the number of inputs. For more information on the matrix coefficients,
see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `D` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix | sparse matrix |
| **Default:** `'1'` |

### **Initial conditions** — Initial state vector `0` (default) | scalar | vector

Specify the initial state vector.

#### Limitations

The initial conditions of this block cannot be `inf`
or `NaN`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector, string |
| **Values:** scalar | vector |
| **Default:** `'0'` |

Alternatively, use
`X0`.

### **Parameter tunability** — Choose tunable representation of block parameters `Auto` (default) | `Optimized` | `Unconstrained`

Tunability level of the state-space matrices (A,B,C, and D ) for accelerated simulation
modes and deployed simulations using the Simulink
Compiler™. When set to `Auto`, Simulink chooses the appropriate parameter tunability level.

For sparse matrix coefficients, set the parameter to
`Optimized` to allow tunability of non-zero
elements while keeping the pattern and number of non-zero elements constant.
Set this parameter to `Unconstrained` to allow all
elements to be tunable, so long as the number of non-zero elements is kept
constant, that is, you can change the pattern of the sparse matrix.

For dense matrix coefficients, select `Optimized` to allow
tunability of all matrix elements, provided the number of non-zero elements
initially specified in the matrix is kept constant. Set this parameter to
`Unconstrained` to allow full tunability of all
matrix elements.

**Note**

To tune the **D** matrix of the block when D = 0, you
must enable the **Allow non-zero values for D matrix initially
specified as zero** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ParameterTunability` |
| **Type:** character vector | string |
| **Values:** `'Auto'` | `'Optimized'` | `'Unconstrained'` |
| **Default:** `'Auto'` |

### **Allow non-zero values for D matrix initially specified as zero** — Allow tunability of D matrix when D = 0 `off` (default) | `on`

Enable this parameter to support tunability of **D** even when D = 0.

**Note**

Enabling this parameter enables direct feedthrough for the
State-Space block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AllowTunableDMatrix` |
| **Type:** character vector | string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Absolute tolerance** — Absolute tolerance for computing block states `auto` (default) | scalar | vector

Variable-step solvers use absolute and relative tolerances when choosing the step size to
determine whether the error in state calculations is acceptable.

To inherit the absolute tolerance from the **Absolute tolerance** configuration parameter, specify this parameter
value as `auto` or `-1`.

To specify an absolute tolerance for this block that overrides the value specified for
the **Absolute tolerance** configuration parameter:

- Enter a real, positive scalar value to use to compute all block
  states.
- Enter a real vector with dimensions that match the dimensions of the
  continuous states for the block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AbsoluteTolerance` |
| **Values:** | `'auto'` (default) | `'-1'` | positive real scalar number | vector of positive real scalar numbers |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor
State-Space",AbsoluteTolerance="-1")`

### **State Name (e.g., 'position')** — Option to assign unique names to states `''` (default) | character vector | cell array of character vectors | MATLAB® variable | ...

Use this parameter to optionally assign names to the states of this block. The
names you assign apply only to the states of this block.

- To use default state names, leave this field blank
  (`''`).
- To assign a single name to a single state, enter the
  name between quotes. For example, to name a single
  state `position`, enter
  `'position'`.
- To assign names to multiple states, specify this
  parameter value as a cell array of character
  vectors. Each name in the cell array must be unique.
  For example, to assign the names
  `a`, `b`, and
  `c`, enter
  `{'a','b','c'}`.
- To specify the names using a MATLAB variable, enter the name of the
  variable without quotes. For example, to use the
  variable `names` to specify the
  state names, enter `names`.

You can specify a number of names that is less than the number of states in
the block. In this case, the state names are used for multiple states, and
the number of states must divide evenly into the number of state names. For
example, when you specify two names for a block that has four states, the
first name is used for the first two states, and the second name is used for
the last two states.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ContinuousStateAttributes` |
| **Values:** | `''` (default) | valid MATLAB variable name |
| **Data Types:** | `char` | `string` | `cell` |

**Example:** `set_param("MyModel/Descriptor
State-Space",ContinuousStateAttributes={'position','velocity'})`

## Libraries

Simulink / Continuous

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production-quality code. Relates to resource limits and restrictions on speed and memory often found in embedded systems. The code generated can contain dynamic allocation and freeing of memory, recursion, additional memory overhead, and widely-varying execution times. While the code is functionally valid and generally acceptable in resource-rich environments, smaller embedded targets often cannot support such code.

In general, consider using the Simulink Model Discretizer to map continuous blocks into discrete equivalents that support production code generation. To start the Model Discretizer, in the Simulink Editor, on the **Apps** tab, under **Apps**, under **Control Systems**, click **Model Discretizer**. One exception is the Second-Order Integrator block because, for this block, the Model Discretizer produces an approximate discretization.

## Version History

**Introduced before R2006a**

## Description

Implement linear state-space system

The State-Space block implements a system whose behavior you
define as

x˙=Ax+Buy=Cx+Dux|t=t0=x0,

where *x* is the state vector, *u* is the input vector,
*y* is the output vector, and *x0* is the initial
condition of the state vector. The A, B, C, and D matrices can be specified as either
sparse matrices or dense matrices. The matrix coefficients must have these
characteristics:

- *A* must be an *n*-by-*n*
  matrix, where *n* is the number of states.
- *B* must be an *n*-by-*m*
  matrix, where *m* is the number of inputs.
- *C* must be an *r*-by-*n*
  matrix, where *r* is the number of outputs.
- *D* must be an *r*-by-*m*
  matrix.

In general, the block has one input port and one output port. The number of rows in C or D matrix is the same as the width of the output port. The number of columns in the B or D matrix are the same as the width of the input port. If you want to model an autonomous linear system with no inputs, set the B and D matrices to empty. In this case, the block acts as a source block with no input port and one output port, and implements the following system:

x˙=Axy=Cxx|t=t0=x0.

Simulink® software converts a matrix containing zeros to a sparse matrix for efficient multiplication.
