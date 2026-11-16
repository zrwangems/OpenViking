---
type: simulink-block
title: 'Divide by Constant HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'dividebyconstanthdloptimized'
documentation_source_path: '../fixedpoint/ref/dividebyconstanthdloptimized.html'
language: en
---

# Divide by Constant HDL Optimized

## Ports

### Input

### **X** — Dividend real scalar

Dividend, specified as a real scalar.

Slope-bias representation is not supported for fixed-point data types.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **validIn** — Whether input is valid boolean scalar

Whether input is valid, specified as a Boolean scalar. This control signal
indicates when the data from the **X** input port is valid. When this
value is `1` (`true`), the block captures the value
on the **X** input port. When this value is `0`
(`false`), the block ignores the input samples.

**Data Types:** `Boolean`
### Output

### **Y** — Result of division and round operation scalar

Result of division and round operation, returned as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **validOut** — Whether output data is valid boolean scalar

Whether the output data is valid, returned as a Boolean scalar. When the value of
this control signal is `1` (`true`), the block has
successfully computed the output **Y**. When this value is
`0` (`false`), the output data is not
valid.

**Data Types:** `Boolean`

## Parameters

### **Denominator for rational division** — Divisor 10 (default) | scalar

Divisor, specified as a positive, real-valued, finite scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Denominator` |
| **Type:** character vector |
| **Values:** MATLAB® expression that evaluates to a positive, real-valued, finite fixed point or numeric value |
| **Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **Default:** `'10'` |

### **Rounding Method** — Rounding method to use `Floor` (default) | `Ceiling` | `Nearest` | `Zero` | `Convergent`

Rounding method to use, specified as one of these values:

- `Floor` — Round to nearest integer in the direction of
  negative infinity.
- `Ceiling` — Round to nearest integer in the direction
  of positive infinity.
- `Nearest` — Round to the nearest integer. Ties are
  rounded to the nearest integer in the direction of positive infinity.
- `Zero` — Round to the nearest integer in the direction
  of zero.
- `Convergent` — Round to the nearest integer. Ties are
  rounded to the nearest even integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Floor'` | `'Ceiling'` | `'Nearest'` | `'Zero'` | `'Convergent'` |
| **Default:** `'Floor'` |

## Libraries

Fixed-Point Designer HDL Support / Math Operations

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

Slope-bias representation is not supported for fixed-point data types.

## Version History

**Introduced in R2021a**

## Description

Divide input by a constant and round to integer and generate optimized HDL code

The Divide by Constant HDL Optimized block outputs the result of dividing
the input by a constant and rounds the result to an integer using the specified rounding
method using an HDL-optimized architecture with cycle-true latency.

The Divide by Constant HDL Optimized block uses an algorithm that is
functionally similar to the Granlund-Montgomery-Warren Method. The division operation is
computed via a multiplication by inverse, which generally results in better performance on
embedded systems.
