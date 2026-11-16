---
type: simulink-block
title: 'Complex Divide HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'complexdividehdloptimized'
documentation_source_path: '../fixedpoint/ref/complexdividehdloptimized.html'
language: en
---

# Complex Divide HDL Optimized

## Ports

### Input

### **num** — Numerator scalar | vector | matrix

Numerator, specified as a scalar, vector, or matrix. **num** and **den** must
have the same dimensions.

Slope-bias representation is not supported for fixed-point data types.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **den** — Denominator scalar | vector | matrix

Denominator, specified as a scalar, vector, or matrix. **num** and
**den** must have the same dimensions.

Slope-bias representation is not supported for fixed-point data types.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **validIn** — Whether input is valid `Boolean` scalar

Whether input is valid, specified as a Boolean scalar. This control signal
indicates when the data from the **num** and
**den** input
ports are valid. When this value is `1` (`true`),
the block captures the values at the input ports **num** and
**den**. When this value is `0` (`false`),
the block ignores the input samples.

**Data Types:** `Boolean`
### Output

### **y** — Output computed by dividing inputs complex scalar

Output computed by dividing **num** by
**den**, such
that **y** = **num**/**den**, returned as a complex
scalar.

#### Tips

The data type at the output port **y** is specified by the **Output
datatype** parameter.

**Data Types:** `single` | `double` | `fixed point`

### **divideByZero** — Whether the value at output is the result of division by zero `Boolean` scalar

*Since R2024b*

Whether the value at the **y** output
port is the result of a division by zero operation, returned as a Boolean scalar. When
the value of this signal is `1` (`true`), the
corresponding output value at the **y** port is the result of division by
zero. When the value of this signal is `0`
(`false`), the corresponding output value at the **y** port
is the result of division by a nonzero value.

See Division by Zero Behavior for a
description of the default divide by zero behavior.

#### Dependencies

To enable this port, select the **Show divide by
zero port** parameter.

**Data Types:** `Boolean`

### **validOut** — Whether output data is valid `Boolean` scalar

Whether the output data is valid, returned as a Boolean scalar. When the value of
this control signal is `1` (`true`), the block has
successfully computed the output at port **y**. When
this value is `0` (`false`), the output data is not
valid.

**Data Types:** `Boolean`

## Parameters

### **Output datatype** — Data type of output `fixdt(1,18,10)` (default) | `single` | `double` | `fixdt(1,16,0)` | `<data type expression>`

Data type of output **y**,
specified as `fixdt(1,18,10)`, `single`,
`double`, `fixdt(1,16,0)`, or as a user-specified
data type expression. The type can be specified directly or expressed as a data type
object, such as `Simulink.NumericType`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputType` |
| **Values:** | `fixdt(1,18,10)` (default) | `single` | `double` | `fixdt(1,16,0)` | `<data type expression>` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,"OutputType","fixdt(1,16,0)")`

### **Show divide by zero port** — Whether to show the `divideByZero` port `off` (default) | `on`

*Since R2024b*

Select this parameter to show the **divideByZero** port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `dbzPort` |
| **Values:** | `0` (false) (default) | `1` (true) |
| **Data Types:** | `logical` |

**Example:** `set_param(gcb,"dbzPort",1)`

### **Automatically select CORDIC maximum shift value based on input word length** — Automatically select CORDIC maximum shift value based on input word length `on` (default) | `off`

*Since R2024b*

Automatically select the CORDIC maximum shift value based on input word length. When
this parameter is selected, the default CORDIC `maximumShiftValue` is
equal to `wl - 1`, where `wl = max(num.WordLength +
~issigned(num), den.WordLength + ~issigned(den))`.

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

**Example:** `set_param(gcb,"autoMaximumShiftVal","off")`

### **CORDIC maximum shift value** — Maximum shift value of hyperbolic vectoring CORDIC `wl - 1` (default) | `10` | positive integer-valued scalar

*Since R2024b*

Maximum shift value of hyperbolic vectoring CORDIC, specified as a positive
integer-valued scalar. The default value for this parameter is `wl -
1`, where `wl = max(num.WordLength + ~issigned(num), den.WordLength +
~issigned(den))`.

#### Dependencies

To enable this parameter, clear the **Automatically
select CORDIC maximum shift value based on input word length**
parameter.

#### Tips

See Customizable Pipelining for more
information.

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

**Example:** `set_param(gcb,"maximumShiftValue","10")`

### **Number of iterations per pipeline register** — Number of CORDIC iterations to perform per pipeline stage `1` (default) | positive integer-valued scalar

*Since R2024b*

Number of CORDIC iterations to perform per pipeline stage, specified as a positive
integer-valued scalar.

See Customizable Pipelining for more
information. See How to Interface with the Complex Divide HDL Optimized Block and Hardware Resource Utilization for more
information and examples showing how this parameter impacts latency and hardware
resource utilization.

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

**Example:** `set_param(gcb,"nIterPerReg","2")`

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
| *In R2024b: **FlattenHierarchy*** | Remove PWM Reference Generator block hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

Supports binary-point scaled fixed-point data types only.

## Version History

**Introduced in R2021a**

### R2024b: Custom pipelining, improved latency and resource utilization, optional divide by zero port

Several improvements have been made to the Complex Divide HDL Optimized block:

- Custom pipelining is supported via the new **CORDIC maximum
  shift value** and **Number of
  iterations per pipeline register** parameters.
- The latency of this block has been reduced. Latency depends on the specified data
  type and pipeline configuration. See How to Interface with the Complex Divide HDL Optimized Block for more
  information.
- HDL resource utilization has been further optimized to require fewer hardware
  resources. See Hardware Resource Utilization for example
  synthesis results.
- An optional **divideByZero** port has been added to output a flag when the corresponding
  output is a result of division by zero.

## Description

Divide one input by another using CORDIC algorithm and generate optimized HDL code

The Complex Divide HDL Optimized block outputs the result of dividing the
scalar **num** by the scalar **den**, such that **y** =
**num**/**den**.
