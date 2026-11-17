---
type: simulink-block
title: 'Interval Test Dynamic'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'intervaltestdynamic'
documentation_source_path: 'slref/intervaltestdynamic.html'
language: en
---

# Interval Test Dynamic

## Ports

### Input

### **up** — Upper limit of interval scalar | vector | matrix | N-D array

Upper limit of interval, specified as a scalar, vector, matrix, or N-D
array.

#### Limitations

When the input signal is an enumerated type, the
**up** and **lo** signals must
be of the same enumerated type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **u** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D
array.

#### Limitations

When the input signal is an enumerated type, the
**up** and **lo** signals must
be of the same enumerated type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **lo** — Lower limit of interval scalar | vector | matrix | N-D array

Lower limit of interval, specified as a scalar, vector, matrix, or N-D
array.

#### Limitations

When the input signal is an enumerated type, the
**up** and **lo** signals must
be of the same enumerated type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **y** — Output signal scalar | vector | matrix | N-D array

Output signal indicating whether the input values fall within the
specified interval. You can specify the **Output data
type** as `boolean` or
`uint8`.

**Data Types:** `uint8` | `Boolean`

## Parameters

### **Interval closed on right** — Include upper limit value `on` (default) | `off`

When you select this check box, the value of the signal connected to the
**up** input port is included in the interval for which
the block outputs true (`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `IntervalClosedRight` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Interval closed on left** — Include lower limit value `on` (default) | `off`

When you select this check box, the value of the signal connected to the
**lo** input port is included in the interval for which
the block outputs true (`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `IntervalClosedLeft` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Output data type** — Output data type `boolean` (default) | `uint8`

Specify the output data type as `boolean` or
`uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'boolean' | 'uint8'` |
| **Default:** `'boolean'` |

## Libraries

Simulink / Logic and Bit Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Determine if signal is in specified interval

The Interval Test Dynamic block outputs true (`1`) if
the input is between the values of the external signals **up** and
**lo**. The block outputs false (`0`) if the input
is outside those values. To control how the block handles input values that are equal to
the signal **lo** or the signal **up**, use the
**Interval closed on left** and **Interval closed on
right** check boxes.
