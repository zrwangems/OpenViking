---
type: simulink-block
title: 'Shift Arithmetic'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'shiftarithmetic'
language: en
---

# Shift Arithmetic

## Ports

### Input

### **u** — Number to be operated on scalar | vector | array

Number to be operated on, specified as a scalar, vector, or
array.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **s** — Number of bits to shift scalar

Number of bits to shift, specified as a scalar.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Result of operation scalar | vector | array

Result of operation, returned as a scalar, vector, or array.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Bits to shift: Source** — Source of bits to shift `Dialog` (default) | `Input port`

Specify whether to enter the bits to shift on the dialog box or to inherit the values
from an input port.

**Tunable:** No

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BitShiftNumberSource` |
| **Type**: character vector, string |
| **Values**: `'Dialog'` | `'Input port'` |
| **Default**: `'Dialog'` |

### **Bits to shift: Direction** — Direction in which to shift bits `Bidirectional` (default) | `Left` | `Right`

Specify the direction in which to shift bits: left, right, or
bidirectional.

**Tunable:** No

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BitShiftDirection` |
| **Type**: character vector, string |
| **Values**: `'Left'` | `'Right'` | `'Bidirectional'` |
| **Default**: `'Bidirectional'` |

### **Bits to shift: Number** — Bits to shift `8` (default) | scalar | vector | array

Specify a scalar, vector, or array of bit shift values.

| If the direction is... | Then... |
| --- | --- |
| `Left` or `Right` | Use positive integers to specify bit shifts. |
| `Bidirectional` | Use positive integers for right shifts and negative integers for left shifts. |

**Tunable:** No

#### Dependencies

To enable this parameter, set **Bits to shift:
Source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BitShiftNumber` |
| **Type**: character vector, string |
| **Values**: scalar | vector | array |
| **Default**: `'8'` |

### **Binary points to shift: Number** — Number of places to shift binary point `0` (default) | scalar

Specify an integer number of places to shift the binary point of the input
signal. A positive value indicates a right shift, while a negative value
indicates a left shift.

**Tunable:** No

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinPtShiftNumber` |
| **Type**: character vector, string |
| **Values**: scalar |
| **Default**: `'0'` |

### **Diagnostic for out of range shift value** — Diagnostic action `None` (default) | `Warning` | `Error`

Specify whether to produce a warning or error during simulation when the
block contains an out-of-range shift value. Options include:

- `None` — The software takes no
  action.
- `Warning` — The software displays a
  warning and continues the simulation.
- `Error` — The software terminates the
  simulation and displays an error.

For more information, see Simulation and Accelerator Mode Results for Out-of-Range Bit Shift Values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DiagnosticForOORShift` |
| **Type**: character vector, string |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'None'` |

### **Check for out-of-range 'Bits to shift' in generated code** — Check for out-of-range bits to shift in generated code `off` (default) | `on`

Select this check box to include conditional statements in the generated
code that protect against out-of-range bit shift values. This check box is
available when **Bits to shift: Source** is
`Input port`.

For more information, see Code Generation for Out-of-Range Bit Shift Values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CheckOORBitShift` |
| **Type**: character vector, string |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Libraries

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

You can generate HDL code when **Bits to shift: Source** is
**Dialog** or **Input port**.

**HDL Architecture**

The generated VHDL code uses the `shift_right` function and
`sll` operator.

The generated Verilog code uses the `>>>` and
`<<<` shift operators.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

**Restrictions**

When **Bits to shift: Source** is **Input
port**, binary point shifting is not supported.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Shift bits or binary point of signal

The Shift Arithmetic block can shift the bits or the binary point of an input
signal, or both.

For example, shifting the binary point on an input of data type `sfix(8)`
by two places to the right and left gives these decimal values.

| Shift Operation | Binary Value | Decimal Value |
| --- | --- | --- |
| No shift (original number) | 11001.011 | –6.625 |
| Binary point shift right by two places | 1100101.1 | –26.5 |
| Binary point shift left by two places | 110.01011 | –1.65625 |

This block performs arithmetic bit shifts on signed numbers. Therefore, the block recycles
the most significant bit for each bit shift. Shifting the bits on an input of data type
`sfix(8)` by two places to the right and left gives these decimal
values.

| Shift Operation | Binary Value | Decimal Value |
| --- | --- | --- |
| No shift (original number) | 11001.011 | –6.625 |
| Bit shift right by two places | 11110.010 | –1.75 |
| Bit shift left by two places | 00101.100 | 5.5 |
