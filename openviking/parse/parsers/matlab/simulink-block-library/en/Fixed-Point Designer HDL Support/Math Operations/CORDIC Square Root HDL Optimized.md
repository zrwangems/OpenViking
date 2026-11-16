---
type: simulink-block
title: 'CORDIC Square Root HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'cordicsquareroothdloptimized'
documentation_source_path: '../fixedpoint/ref/cordicsquareroothdloptimized.html'
language: en
---

# CORDIC Square Root HDL Optimized

## Ports

### Input

### **u** — Value to take square root of non-negative real-valued scalar

Value to take square root of, specified as a non-negative real-valued
scalar.

If **u** is a fixed-point or scaled double data type, **u** must
use binary-point scaling. Slope-bias representation is not supported for fixed-point
data types. Only binary-point scaled fixed-point data types are supported for code
generation.

**Data Types:** `single` | `double` | `fixed point`

### **validIn** — Whether input is valid `Boolean` scalar

Whether input is valid, specified as a Boolean scalar. This control signal
indicates when the data from the **u** input port is valid. When this value
is `1` (`true`), the block captures the values at
the **u** input port. When this value is `0`
(`false`), the block ignores input samples.

**Data Types:** `Boolean`

### **restart** — Whether to clear internal registers `Boolean`

Whether to clear internal registers, specified as a Boolean scalar. When this
value is `1` (`true`), the block stops the current
calculation and clears all internal registers. When this value is `0`
(`false`) and the **validIn** value is
`1` (`true`), the block begins a new
subframe.

**Data Types:** `Boolean`
### Output

### **y** — CORDIC-based approximation of square root of input real-valued scalar

CORDIC-based approximation of square root of input, returned as a real-valued
scalar.

**Data Types:** `single` | `double` | `fixed point`

### **validOut** — Whether output data is valid `Boolean`

Whether output data is valid, returned as a Boolean scalar. This control signal
indicates when the data at the output port **y** is valid. When this value is
`1` (`true`), the output data is valid. When this
value is `0` (`false`), the output data is not
valid.

**Data Types:** `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Automatically select CORDIC maximum shift value based on input word length** — Automatically select CORDIC maximum shift value based on input word length `on` (default) | `off`

Automatically select CORDIC maximum shift value based on input word length. When
this parameter is selected, the default CORDIC maximum shift value depends on the word
length of the input **u**:

- If the input **u** is fixed-point or scaled double, the default is
  the word length minus 1.
- If the input **u** is `single`, the default is
  `23`.
- If the input **u** is `double`, the default is
  `52`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `autoMaximumShiftVal` |
| **Values:** | `on` (default) | `off` |
| **Data Types:** | `char` | `string` |

### **CORDIC maximum shift value** — Maximum shift value of hyperbolic vectoring CORDIC `10` (default) | positive integer-valued scalar

Maximum shift value of hyperbolic vectoring CORDIC, specified as a positive
integer-valued scalar.

#### Dependencies

- To enable this parameter, clear the **Automatically select CORDIC maximum shift value based on input word
  length** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `maximumShiftValue` |
| **Values:** | `10` (default) | positive integer-valued scalar |
| **Data Types:** | `char` | `string` |

### **Number of iterations per pipeline register** — Number of CORDIC iterations to perform in pipeline stage `1` (default) | positive integer-valued scalar

Number of CORDIC iterations to perform in pipeline stage, specified as a positive
integer-valued scalar. For more information, see Customizable Pipelining.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `nIterPerReg` |
| **Values:** | `1` (default) | positive integer-valued scalar |
| **Data Types:** | `char` | `string` |

## Libraries

Fixed-Point Designer HDL Support / Math Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

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

Only binary-point scaled fixed-point data types are supported for code
generation.

## Version History

**Introduced in R2024a**

## Description

CORDIC-based approximation of square root

The CORDIC Square Root HDL Optimized block returns the square root of
`u`, computed using a CORDIC-based implementation optimized for HDL code
generation.
