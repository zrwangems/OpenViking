---
type: simulink-block
title: 'Normalized Reciprocal HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'normalizedreciprocalhdloptimized'
documentation_source_path: '../fixedpoint/ref/normalizedreciprocalhdloptimized.html'
language: en
---

# Normalized Reciprocal HDL Optimized

## Ports
```yaml
ports:
- name: u
  summary: Value to take normalized reciprocal of real scalar
  direction: input
  data_types: single | double | fixed point
- name: validIn
  summary: Whether input is valid Boolean scalar
  direction: input
  data_types: Boolean
- name: y
  summary: Normalized reciprocal scalar
  direction: output
  data_types: single | double | fixed point
- name: e
  summary: Exponent integer scalar
  direction: output
  data_types: int32
- name: divideByZero
  summary: Whether value at output is the result of division by zero Boolean scalar
  direction: output
  data_types: Boolean
- name: validOut
  summary: Whether output data is valid Boolean scalar
  direction: output
  data_types: Boolean
```

### Input

### **u** — Value to take normalized reciprocal of real scalar

Value to take the normalized reciprocal of, specified as a real scalar.

Slope-bias representation is not supported for fixed-point data types.

**Data Types:** `single` | `double` | `fixed point`

### **validIn** — Whether input is valid `Boolean` scalar

Whether input is valid, specified as a Boolean scalar. This control signal
indicates when the data from the **u** input
port is valid. When this value is `1` (`true`), the
block captures the value at the **u** input port. When this value is
`0` (`false`), the block ignores the input
samples.

**Data Types:** `Boolean`
### Output

### **y** — Normalized reciprocal scalar

Normalized reciprocal that satisfies 0.5 < |**y**| ≤ 1 and 2**e****y** =
1/**u**, returned as a scalar.

- If the input at port **u** is a signed fixed-point or scaled-double
  data type with word length *w*, then **y** is a signed
  fixed-point or scaled-double data type with word length *w* and
  fraction length *w* – 2.
- If the input at port **u** is an unsigned fixed-point or
  scaled-double data type with word length *w*, then **y**
  is an unsigned fixed-point or scaled-double data type with word length
  *w* and fraction length *w* – 1.
- If the input at port **u** is a double, then **y** is a
  double.
- If the input at port **u** is a single, the **y** is a
  single.

**Data Types:** `single` | `double` | `fixed point`

### **e** — Exponent integer scalar

Exponent that satisfies 0.5 < |**y**| ≤ 1 and 2*e***y** =
1/**u**, returned as an integer scalar.

**Data Types:** `int32`

### **divideByZero** — Whether value at output is the result of division by zero `Boolean` scalar

*Since R2024b*

Whether the values at the **y** and
**e** output
ports are the result of a division by zero operation, returned as a Boolean scalar.
When the value of this signal is `1` (`true`), the
corresponding output values at the **y** and **e** ports are the
result of division by zero. When the value of this signal is `0`
(`false`), the corresponding output values at the **y**
and **e** ports are the result of division by a non-zero value.

Whether the divisor **u** is
zero, returned as a Boolean scalar. When the value of this signal is
`1` (`true`), the input at the **u** port
is zero, resulting in a divide by zero operation. When the value of this signal is
`0` (`false`), the input at the **u**
port is a non-zero value.

#### Dependencies

- To enable this port, select the **Show
  divide by zero port** parameter.

#### Tips

- See Division by Zero Behavior for a
  description of the default divide by zero behavior.

**Data Types:** `Boolean`

### **validOut** — Whether output data is valid `Boolean` scalar

Whether the output data is valid, returned as a Boolean scalar. When the value of
this control signal is `1` (`true`), the block has
successfully computed the outputs at ports **y** and
**e**. When
this value is `0` (`false`), the output data is not
valid.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Show divide by zero port
  summary: Whether to show the divideByZero port off (default) | on
  group: ''
  block_parameter: dbzPort
  values: 0 (false) (default) | 1 (true)
- name: Automatically select CORDIC maximum shift value based on input word length
  summary: Automatically select CORDIC maximum shift value based on input word length on (default) | off
  group: ''
  block_parameter: autoMaximumShiftVal
  values: on (default) | off
- name: CORDIC maximum shift value
  summary: Maximum shift value of hyperbolic vectoring CORDIC wl - 1 (default) | 10 | positive integer-valued scalar
  group: ''
  block_parameter: maximumShiftValue
  values: 10 (default) | positive integer-valued scalar
- name: Number of iterations per pipeline register
  summary: Number of CORDIC iterations to perform per pipeline stage 1 (default) | positive integer-valued scalar
  group: ''
  block_parameter: nIterPerReg
  values: 1 (default) | positive integer-valued scalar
```

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

Automatically select CORDIC maximum shift value based on input word length. When
this parameter is selected, the default CORDIC `maximumShiftValue` is
equal to `wl - 1`, where `wl = u.WordLength +
~issigned(u)`.

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
1`, where `wl = u.WordLength + ~issigned(u)`.

#### Dependencies

To enable this parameter, deselect the **Automatically
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

#### Tips

- See Customizable Pipelining for more
  information.
- See How to Interface with the Normalized Reciprocal HDL Optimized Block and Hardware Resource Utilization for more
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

Supports fixed-point data types only.

## Version History

**Introduced in R2020a**

### R2024b: Custom pipelining, improved latency and resource utilization, optional divide by zero port

Several improvements have been made to the Normalized Reciprocal HDL
Optimized block:

- Custom pipelining is supported via the new **CORDIC maximum
  shift value** and **Number of
  iterations per pipeline register** parameters.
- The latency of this block has been reduced. Latency depends on the specified data
  type and pipeline configuration. See How to Interface with the Normalized Reciprocal HDL Optimized Block for more
  information.
- HDL resource utilization has been further optimized to require fewer hardware
  resources. See Hardware Resource Utilization for example
  synthesis results.
- An optional **divideByZero** port has been added to output a flag when the corresponding
  output is a result of division by zero.

## Description

Computes normalized reciprocal using CORDIC algorithm and generates optimized HDL code

The Normalized Reciprocal HDL Optimized block computes the normalized
reciprocal of **u**, returned as
**y** and **e** such that 0.5 < |**y**| ≤ 1 and 2*e***y** =
1/**u**.

- If **u** = 0 and **u** is a fixed-point or scaled-double data type, then **y** = 1 – eps(**y**) and **e** =
  2nextpow2(*w*) – *w*
  + *f*, where `w` is the word length of **u** and
  *f* is the fraction length of **u**.
- If **u** = 0 and **u** is a floating-point data type, then **y** = `Inf` and **e** = 1.
