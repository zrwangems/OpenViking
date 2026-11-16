---
type: simulink-block
title: 'Transfer Fcn Direct Form II'
family: additional-math-and-discrete
documentation_release: R2025b
official_category: 'Additional Math and Discrete'
documentation_page: 'transferfcndirectformii'
language: en
---

# Transfer Fcn Direct Form II

Implement Direct Form II realization of transfer function

## Libraries

Simulink / Additional Math & Discrete / Additional Discrete

## Description

The Transfer Fcn Direct Form II block implements a Direct Form II realization
of the transfer function that the **Numerator coefficients** and
**Denominator coefficients excluding lead** parameters specify. The
block supports only single input-single output (SISO) transfer functions.

The block automatically selects the data types and scalings of the output, the coefficients, and any temporary variables.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal, specified as a scalar or vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal, specified as a scalar or vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Numerator coefficients** — Numerator coefficients `[0.2 0.3 0.2]` (default) | vector

Specify the numerator coefficients as a vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumCoefVec` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[0.2 0.3 0.2]'` |

### **Denominator coefficients excluding lead** — Denominator coefficient `[-0.9 0.6]` (default) | vector

Specify the denominator coefficients, excluding the leading coefficient,
which must be `1.0`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenCoefVec` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[-0.9 0.6]'` |

### **Initial condition** — Initial condition `0.0` (default) | scalar

Specify the initial condition as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vinit` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0.0'` |

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
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The code generator does not explicitly group primitive blocks
that constitute a nonatomic masked subsystem block in the generated code. This
flexibility allows for more efficient code generation. In certain cases, you can
achieve grouping by configuring the masked subsystem block to execute as an atomic
unit by selecting the **Treat as atomic unit** option.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
