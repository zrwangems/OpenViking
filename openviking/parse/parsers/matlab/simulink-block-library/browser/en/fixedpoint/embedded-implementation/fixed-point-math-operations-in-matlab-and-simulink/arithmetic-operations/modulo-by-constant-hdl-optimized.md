---
type: simulink-block
title: 'Modulo by Constant HDL Optimized'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Arithmetic Operations'
documentation_page: 'modulobyconstanthdloptimized'
documentation_source_path: 'ref/modulobyconstanthdloptimized.html'
language: en
---

# Modulo by Constant HDL Optimized

## Ports

### Input

### **X** — Dividend real-valued scalar | vector | matrix | multidimensional array

Dividend, specified as a real-valued scalar, vector, matrix, or multidimensional
array.

If **X** is a fixed-point data type, it must use binary-point
scaling. Slope-bias representation is not supported for fixed-point data types.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

### **validIn** — Whether input is valid boolean scalar

Whether input is valid, specified as a Boolean scalar. This control signal
indicates when the data from the **X** input port is valid. When this
value is `1` (`true`), the block captures the value
on the **X** input port. When this value is `0`
(`false`), the block ignores the input samples.

**Data Types:** `Boolean`
### Output

### **Y** — Result of modulus operation scalar | vector | matrix | multidimensional array

Result of modulus operation, returned as a scalar, vector, matrix, or
multidimensional array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

### **validOut** — Whether output data is valid boolean scalar

Whether the output data is valid, returned as a Boolean scalar. When the value of
this control signal is `1` (`true`), the block has
successfully computed the output **Y**. When this value is
`0` (`false`), the output data is not
valid.

**Data Types:** `Boolean`

## Parameters

### **Denominator** — Divisor 10 (default) | real-valued scalar | vector | matrix | multidimensional array

Divisor to use for the modulus operation, specified as a positive, real-valued,
finite scalar, vector, matrix, or multidimensional array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Denominator` |
| **Type:** character vector |
| **Values:** MATLAB® expression that evaluates to a positive, real-valued, finite fixed point or numeric value |
| **Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **Default:** `'10'` |

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

### R2024a: Latency of Modulo by Constant HDL Optimized block reduced

The latency of the Modulo by Constant HDL
Optimized block has been reduced from 9 clock cycles to 4 clock cycles.

### R2023b: Support for vector and matrix input

The Modulo by Constant HDL Optimized block now supports vector and matrix
inputs.

### R2023b: Modulo by Consant block supported for use in For Each Subsystem block

The Modulo by Constant HDL Optimized block is supported for use inside a
For Each Subsystem block.

## Description

Perform mod operation with a constant denominator and generate optimized HDL code

The Modulo by Constant HDL Optimized block performs the modulo operation
(remainder after division) with a constant denominator using an HDL-optimized architecture
with cycle-true latency.

The Modulo by Constant block uses an algorithm that is functionally similar
to a Barrett Reduction. The division operation is computed via a multiplication by inverse,
which generally results in better performance on embedded systems.
