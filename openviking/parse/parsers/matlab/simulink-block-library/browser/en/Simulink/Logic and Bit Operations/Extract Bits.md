---
type: simulink-block
title: 'Extract Bits'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'extractbits'
language: en
---

# Extract Bits

Output selection of contiguous bits from input signal

## Libraries

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## Description

The Extract Bits block allows you to output a contiguous selection of
bits from the stored integer value of the input signal. Use the **Bits to
extract** parameter to define the method for selecting the output
bits.

- Select `Upper half` to output the half of the input bits that
  contain the most significant bit. If there is an odd number of bits in the input
  signal, the number of output bits is given by the equation

  ```
  number of output bits = ceil(number of input bits/2)
  ```
- Select `Lower half` to output the half of the input bits that
  contain the least significant bit. If there is an odd number of bits in the
  input signal, the number of output bits is given by the equation

  ```
  number of output bits = ceil(number of input bits/2)
  ```
- Select `Range starting with most significant bit` to output a
  certain number of the most significant bits of the input signal. Specify the
  number of most significant bits to output in the **Number of
  bits** parameter.
- Select `Range ending with least significant bit` to output a
  certain number of the least significant bits of the input signal. Specify the
  number of least significant bits to output in the **Number of
  bits** parameter.
- Select `Range of bits` to indicate a series of contiguous
  bits of the input to output in the **Bit indices** parameter.
  You indicate the range in `[start end]` format, and the indices
  of the input bits are labeled contiguously starting at 0 for the least
  significant bit.

This block does not report wrap on overflow warnings during simulation. To report
these warnings, see the `Simulink.restoreDiagnostic` reference
page. The block does report errors due to wrap on overflow.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D array.
Floating-point inputs are passed through the block unchanged.
`boolean` inputs are treated as
`uint8` signals.

**Note**

Performing bit operations on a signed integer is difficult. You
can avoid difficulty by converting the data type of your input
signals to unsigned integer types.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Extracted bits scalar | vector | matrix | N-D array

Contiguous selection of extracted bits, specified as a scalar, vector,
matrix, or N-D array. Floating-point inputs are passed through the block
unchanged.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Bits to extract** — Method for extracting bits `Upper half` (default) | `Lower half` | `Range starting with most significant bit` | `Range ending with least significant big` | `Range of bits`

Select the method for extracting bits from the input signal.

Consider an input signal that is represented in binary by
`110111001`:

- If you select `Upper half` for the **Bits
  to extract** parameter, the output is
  `11011` in binary.
- If you select `Lower half` for the **Bits
  to extract** parameter, the output is
  `11001` in binary.
- If you select `Range starting with most significant
  bit` for the **Bits to extract**
  parameter, and specify `3` for the **Number
  of bits** parameter, the output is
  `110` in binary.
- If you select `Range ending with least significant
  bit` for the **Bits to extract**
  parameter, and specify `8` for the **Number
  of bits** parameter, the output is
  `10111001` in binary.
- If you select `Range of bits` for the
  **Bits to extract** parameter, and specify
  `[4 7]` for the **Bit indices**parameter, the output is `1011` in
  binary.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `bitsToExtract` |
| **Type:** character vector |
| **Values:** `'Upper half' | 'Lower half' | 'Range starting with most significant bit' | 'Range ending with least significant bit' | 'Range of bits'` |
| **Default:** `'Upper half'` |

### **Number of bits** — Number of bits to output `8` (default) | scalar positive integer

Specify the number of bits to output from the input signal as a scalar
positive integer.

#### Dependencies

To enable this parameter, set **Bits to extract** to
`Range starting with most significant bit` or
`Range ending with least significant bit`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numBits` |
| **Type:** character vector |
| **Values:** scalar positive integer |
| **Default:** `'8'` |

### **Bit indices** — Contiguous range of bits to output [0 7] (default) | two-element vector | scalar positive integer

Specify a two-element vector of bits of the input signal to output as
scalar positive integers. Specify the range in `[start
end]` format.

#### Dependencies

To enable this parameter, set **Bits to extract** to
`Range of bits`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `bitIdxRange` |
| **Type:** character vector |
| **Values:** two-element vector | scalar positive integer |
| **Default:** `'[0 7]'` |

### **Output scaling mode** — Output scaling mode `Preserve fixed-point scaling` (default) | `Treat bit field as an integer`

Select the scaling mode to use on the output bit selection:

- When you select `Preserve fixed-point
  scaling`, the fixed-point scaling of the input is
  used to determine the output scaling during the data type
  conversion.
- When you select `Treat bit field as an
  integer`, the fixed-point scaling of the input is
  ignored, and only the stored integer is used to compute the
  output data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outScalingMode` |
| **Type:** character vector |
| **Values:** `'Preserve fixed-point scaling' | 'Treat bit field as an integer'` |
| **Default:** `'Preserve fixed-point scaling'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
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
