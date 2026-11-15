---
type: simulink-block
title: 'Fixed-Point State-Space'
family: additional-math-and-discrete
documentation_release: R2025b
official_category: 'Additional Math and Discrete'
documentation_page: 'fixedpointstatespace'
language: en
---

# Fixed-Point State-Space

Implement discrete-time state space

## Libraries

Simulink / Additional Math & Discrete / Additional Discrete

## Description

The Fixed-Point State-Space block implements the system described by

y(n)=Cx(n)+Du(n)

x(n+1)=Ax(n)+Bu(n)

where *u* is the input, *x* is the state, and
*y* is the output. Both equations have the same data type.

- **A** must be an *n*-by-*n*
  matrix, where *n* is the number of states.
- **B** must be an *n*-by-*m*
  matrix, where *m* is the number of inputs.
- **C** must be an *r*-by-*n*
  matrix, where *r* is the number of outputs.
- **D** must be an *r*-by-*m*
  matrix.

In addition:

- The state x must be an *n*-by-1 vector.
- The input u must be an *m*-by-1 vector.
- The output y must be an *r*-by-1 vector.

The block accepts one input and generates one output. The width of the input vector is
the number of columns in the **B** and **D** matrices.
The width of the output vector is the number of rows in the **C** and
**D** matrices. To define the initial state vector, use the
**Initial conditions** parameter.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input vector, where the width equals the number of columns in the
**B** and **D** matrices. For more
information, see Description.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal, with width equal to the number of rows in the
**C** and **D** matrices. For more
information, see Description.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **State Matrix A** — Matrix of states `[2.6020 -2.2793 0.6708; 1 0 0; 0 1 0]` (default) | scalar | vector | matrix

Specify the matrix of states as an
*n*-by-*n* matrix of real or
complex values, where *n* is the number of states. For
more information on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `A` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[2.6020 -2.2793 0.6708; 1 0 0; 0 1 0]'` |

### **Input Matrix B** — Column vector of inputs `[ 1; 0; 0]` (default) | scalar | vector | matrix

Specify the column vector of inputs as an
*n*-by-*m* matrix of real or
complex values, where *n* is the number of states, and
*m* is the number of inputs. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `B` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[ 1; 0; 0]'` |

### **Output Matrix C** — Column vector of outputs `[0.0184 0.0024 0.0055]` (default) | scalar | vector | matrix

Specify the column vector of outputs as an
*r*-by-*n* matrix of real or
complex values, where *r* is the number of outputs, and
*n* is the number of states. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `C` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[0.0184 0.0024 0.0055]'` |

### **Direct Feedthrough Matrix D** — Matrix for direct feedthrough `[0.0033]` (default) | scalar | vector | matrix

Specify the matrix for direct feedthrough as an
*r*-by-*m* matrix of real or
complex values, where *r* is the number of outputs, and
*m* is the number of inputs. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `D` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[0.0033]'` |

### **Initial condition for state** — Initial state vector `0.0` (default) | scalar | vector | matrix

Specify the initial condition for the state.

#### Limitations

The initial state cannot be `inf` or
`NaN`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0.0'` |

Alternatively, use `X0`.

### Signal Attributes

### **Data type for internal calculations** — Data type for internal calculations `fixdt('double')` (default) | data type string

Specify the data type the block uses for internal calculations.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InternalDataType` |
| **Type:** character vector |
| **Values:** data type string |
| **Default:** `'fixdt('double')'` |

### **Scaling for State Equation AX+BU** — Scaling for state equations `2^0` (default) | scalar

Specify the scaling for the state equation
**AX+BU**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateEqScaling` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'2^0'` |

### **Scaling for Output Equation CX+DU** — Scaling for output equations `2^0` (default) | scalar

Specify the scaling for the output equation
**CX+DU**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputEqScaling` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'2^0'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock the output data type setting of this block against changes
by the Fixed-Point Tool and the Fixed-Point Advisor. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LockScale` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations.
For more information, see Rounding Modes (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate to max or min when overflows occur** — Method of overflow action `off` (default) | `on`

When you select this check box, overflows saturate to the maximum or minimum value
that the data type can represent. Otherwise, overflows wrap.

When you select this check box, saturation applies to every internal operation on the
block, not just the output or result. In general, the code generation process can detect
when overflow is not possible. In this case, the code generator does not produce
saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DoSatur` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block is not recommended for use with Boolean signals. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

By default, the following HDL block property is available.

| General | |
| --- | --- |
| **SharingFactor** | Use SharingFactor to specify the number of functionally equivalent resources to map to a single shared resource. The default is 0. See Resource Sharing (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
