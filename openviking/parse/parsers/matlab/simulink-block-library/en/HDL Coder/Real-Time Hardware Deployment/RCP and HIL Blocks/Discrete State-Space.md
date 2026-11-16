---
type: simulink-block
title: 'Discrete State-Space'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Real-Time Hardware Deployment / RCP and HIL Blocks'
documentation_page: 'discretestatespace'
documentation_source_path: '../simulink/slref/discretestatespace.html'
language: en
---

# Discrete State-Space

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input vector, where the width equals the number of columns in the
**B** and **D** matrices. For more
information, see Description.

**Tip**

For integer and fixed-point input signals, use the Fixed-Point
State-Space block.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output vector scalar | vector

Output vector, with width equal to the number of rows in the
**C** and **D** matrices. For
more information, see Description.

**Data Types:** `single` | `double`

## Parameters

### Main

### **A** — Matrix coefficient A `1` (default) | scalar | vector | matrix

Specify the matrix coefficient `A`, as a real-valued
*n*-by-*n* matrix, where
*n* is the number of states. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `A` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'1'` |

### **B** — Matrix coefficient B `1` (default) | scalar | vector | matrix

Specify the matrix coefficient `B`, as a real-valued
*n*-by-*m* matrix, where
*n* is the number of states, and
*m* is the number of inputs. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `B` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'1'` |

### **C** — Matrix coefficient, C `1` (default) | scalar | vector | matrix

Specify the matrix coefficient **C**, as a real-valued
*r*-by-*n* matrix, where
*r* is the number of outputs, and
*n* is the number of states. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `C` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'1'` |

### **D** — Matrix coefficient, D `1` (default) | scalar | vector | matrix

Specify the matrix coefficient **D**, as a real-valued
*r*-by-*m* matrix, where
*r* is the number of outputs, and
*m* is the number of inputs. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `D` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'1'` |

### **Initial conditions** — Initial state vector 0 (default) | scalar | vector

Specify the initial state vector as a scalar or vector. The initial state vector cannot
include `inf` or `NaN` values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'0'` |

### **Sample time (–1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. See Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

### State Attributes

### **State name** — Unique name for block state `''` (default) | alphanumeric string

Use this parameter to assign a unique name to the block state. The default is `' '`. When this field is blank, no name is assigned. When using this parameter, remember these considerations:

- A valid identifier starts with an alphabetic or underscore character, followed by alphanumeric or underscore characters.
- The state name applies only to the selected block.

This parameter enables **State name must resolve to Simulink signal object** when you click **Apply**.

For more information, see C Data Code Interface Configuration for Model Interface Elements (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateName` |
| **Type:** character vector |
| **Values:** unique name |
| **Default:** `''` |

### **State name must resolve to Simulink signal object** — Require state name resolve to a signal object `off` (default) | `on`

Select this check box to require that the state name resolves to a Simulink® signal object.

#### Dependencies

To enable this parameter, specify a value for **State name**. This parameter appears only if you set the model configuration parameter **Signal resolution** to a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateMustResolveToSignalObject` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Libraries

Simulink / Discrete Simulink / Quick Insert / Discrete HDL Coder / RCP and HIL

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or `memset`
functions (`string.h`) under certain conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

By default, the following HDL block property is available.

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement discrete state-space system

### Block Behavior for Non-Empty Matrices

The Discrete State-Space block implements the system described by

x(n+1)=Ax(n)+Bu(n)y(n)=Cx(n)+Du(n),

where *u* is the input, *x* is the state, and
*y* is the output. The matrix coefficients must have these
characteristics, as illustrated in the following diagram:

- **A** must be an
  *n*-by-*n* matrix, where
  *n* is the number of states.
- **B** must be an
  *n*-by-*m* matrix, where
  *m* is the number of inputs.
- **C** must be an
  *r*-by-*n* matrix, where
  *r* is the number of outputs.
- **D** must be an
  *r*-by-*m* matrix.

The block accepts one input and generates one output. The width of the input
vector is the number of columns in the **B** and
**D** matrices. The width of the output vector is the number of
rows in the **C** and **D** matrices. To define
the initial state vector, use the **Initial conditions**
parameter.

To specify a vector or matrix of zeros for **A**,
**B**, **C**, **D**, or
**Initial conditions**, use the `zeros` function.

### Block Behavior for Empty Matrices

When the matrices **A**, **B**,
and **C** are empty (for example, `[]`),
the functionality of the block becomes `y(n) = Du(n)`.
If the **Initial conditions** vector is also empty, the block uses an initial state vector of zeros.
