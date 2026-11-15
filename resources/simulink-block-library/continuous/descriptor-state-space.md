---
type: simulink-block
title: 'Descriptor State-Space'
family: continuous
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'descriptorstatespace'
---

# Descriptor State-Space

Model linear implicit system

## Libraries

Simulink / Continuous

## Description

The Descriptor State-Space block allows you to model linear implicit systems
described in the implicit form Ex˙=Ax+Bu, where *E* is the mass matrix of the system. When
*E* is nonsingular and therefore invertible, you can describe the
system in the explicit form, x˙=E−1Ax+E−1Bu, and model the system using the State-Space block.

When the mass matrix *E* is singular, the equations do not contain
derivatives for one or more of the dependent variables in the system. Dependent
variables in the system are also called *algebraic variables*, and
differential equations that contain algebraic variables are called
*differential algebraic equations*. The state-space
representation of a system described by differential algebraic equations has this
form:

Ex˙=Ax+Buy=Cx+Du

where:

- *x* is the state vector.
- *u* is the input vector.
- *y* is the output vector.

## Ports

### Input

### **Input 1** — Input signal scalar | vector

Real-valued scalar or vector input signal of the implicit system. The
input signal data type must be `double`. For vector
input signals, the signal width must match the number of columns in the
*B* and *D* matrices for the
system.

This port has direct feedthrough when:

- You set the **Direct Feedthrough**
  parameter to `True`.
- You set the **Direct Feedthrough**
  parameter to `Auto` and the
  software determines that the block has direct
  feedthrough.

**Data Types:** `double`
### Output

### **Output 1** — Output signal scalar | vector

Output signal of implicit system.

**Data Types:** `double`

## Parameters

### **E** — Mass matrix *E* of implicit system `1` (default) | scalar | matrix

Specify the mass matrix *E* as a real-valued
*n*-by-*n* matrix, where
*n* is the number of states in the system. The mass
matrix can be singular or nonsingular and must have the same dimensions as
the *A* matrix.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `E` |
| **Values:** | `'1'` (default) | scalar | matrix |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor State-Space",E="[1 2;3
4]")`

### **A** — *A* matrix of implicit system `1` (default) | scalar | matrix

Specify the matrix *A* as a real-valued
*n*-by-*n* matrix, where
*n* is the number of states in the system. The matrix
*A* must have the same dimensions as the mass matrix
*E*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `A` |
| **Values:** | `'1'` (default) | scalar | matrix |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor State-Space",A="[1 2;3
4]")`

### **B** — *B* matrix of implicit system `1` (default) | scalar | vector | matrix

Specify the matrix *B* as a real-valued
*n*-by-*m* matrix, where
*n* is the number of states in the system and
*m* is the number of inputs.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `B` |
| **Values:** | `'1'` (default) | scalar | vector | matrix |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor State-Space",B="[1
2]")`

### **C** — *C* matrix of implicit system `1` (default) | scalar | vector | matrix

Specify the matrix *C* as a real-valued
*r*-by-*n* matrix, where
*n* is the number of states in the system and
*r* is the number of outputs.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `C` |
| **Values:** | `'1'` (default) | scalar | vector | matrix |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor State-Space",C="[3
4]")`

### **D** — *D* matrix of implicit system `1` (default) | scalar | vector | matrix

Specify the matrix *D* as a real-valued
*r*-by-*m* matrix, where
*r* is the number of system outputs and
*m* is the number of system inputs.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `D` |
| **Values:** | `'1'` (default) | scalar | vector | matrix |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor
State-Space",D="5")`

### **Initial condition** — Initial state values `0` (default) | scalar | vector | matrix

Specify the initial values for states of the implicit system. States
cannot have `Inf` or `NaN` values.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InitialCondition` |
| **Values:** | `'0'` (default) | scalar | vector | matrix |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor State-Space",InitialCondition="[2
3]")`

### **Direct feedthrough** — Whether output signal value depends on input signal value `True` (default) | `False` | `Auto`

Specify whether the implicit system has direct feedthrough. A block has direct
feedthrough when the value of one or more output signals directly depends on
the value of one or more input signals.

- `True` — The output signal value
  directly depends on the input signal value.
- `False` — The output signal value
  does not directly depend on input signal value.
- `Auto` — The software determines
  whether the output signal value directly depends on the input
  signal value based on the characteristics of the specified
  matrices.

When this block implements a system with more than 500 continuous states, specifying this
parameter as `True` or
`False` can speed up the simulation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `DirectFeedthrough` |
| **Values:** | `'True'` (default) | `'False'` | `'Auto'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor
State-Space",DirectFeedthrough="False")`

### **Linearize to sparse model** — Linearize states to sparse matrices `on` (default) | `off`

For Simulink®
Control Design™
workflows, linearize the system represented by the Descriptor
State-Space block to a sparse model during linearization.

Disable this parameter to linearize the system to a non-sparse explicit state-space
model.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LinearizeToSparse` |
| **Values:** | `'off'` (default) | `'on'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor
State-Space",LinearizeToSparse="on")`

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

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Direct feedthrough characteristics for this block depend on block parameter values. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

*Before R2024b: The Descriptor State-Space block
supports only C code generation and does not support C++ code generation.*

Consider using the Model Discretizer to map continuous blocks such as the
Descriptor State-Space block to discrete equivalents that support
code generation. To open the Model Discretizer, in the
**Apps** tab, under **Control Systems**, click
**Model Discretizer**.

## Version History

**Introduced in R2018b**

### R2024b: C++ code generation support

You can generate C++ code for implicit systems that have a mass matrix, such as
those implemented using the Descriptor State-Space block. Use the
**Language (Simulink Coder)** parameter to specify the
language for code generation.
