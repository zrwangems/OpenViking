---
type: simulink-block
title: 'CORDIC Sigmoid HDL Optimized'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Activation Functions'
documentation_page: 'cordicsigmoidhdloptimized'
documentation_source_path: 'ref/cordicsigmoidhdloptimized.html'
language: en
---

# CORDIC Sigmoid HDL Optimized

## Ports

### Input

### **u** — Input data real-valued scalar

Input data, specified as a real-valued scalar.

If **u** is a fixed-point or scaled double data type, **u** must
use binary-point scaling. Slope-bias representation is not supported for fixed-point
data types. Only binary-point scaled fixed-point data types are supported for code
generation.

**Data Types:** `single` | `double` | `fixed point`

### **validIn** — Whether input is valid `Boolean` scalar

Whether input is valid, specified as a Boolean scalar. This control signal
indicates when the data from the **u** input port is valid. When this value
is `1` (`true`), the block captures the value on the
**u** input port. When this value is `0`
(`false`), the block ignores the input samples.

**Data Types:** `Boolean`
### Output

### **y** — Sigmoid activation of `u` scalar

Sigmoid activation of the value at **u**, returned as a scalar. The value
at **y** is the CORDIC-based approximation of the sigmoid activation of
**u**.

When the input **u** is floating point, the output **y** has the
same data type as the input. When the input is a fixed-point data type, the output has
the same word length as the input and a fraction length equal to 2 less than the word
length.

**Data Types:** `single` | `double` | `fixed point`

### **validOut** — Whether output data is valid `Boolean`

Whether the output data is valid, returned as a Boolean scalar. When the value of
this control signal is `1` (`true`), the block has
successfully computed the output **y**. When this value is
`0` (`false`), the output data is not
valid.

**Data Types:** `Boolean`

### **ready** — Whether block is ready `Boolean`

Whether the block is ready, returned as a Boolean scalar. This control signal
indicates when the block is ready for new input data. When this value is 1
(`true`), and the **validIn** value is 1
(`true`), the block accepts input data in the next clock cycle.
When this value is 0 (`false`), the block ignores input data in the
next clock cycle.

**Data Types:** `Boolean`

## Parameters

Not documented in R2025b.

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

Only binary-point scaled fixed-point data types are supported for code
generation.

## Version History

**Introduced in R2024a**

## Description

Compute CORDIC-based sigmoid activation and generate optimized HDL code

The CORDIC Sigmoid HDL Optimized block returns the sigmoid activation of
*u*, computed using a CORDIC-based implementation optimized for HDL code
generation.
