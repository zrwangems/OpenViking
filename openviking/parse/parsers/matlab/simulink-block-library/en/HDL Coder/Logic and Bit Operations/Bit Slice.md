---
type: simulink-block
title: 'Bit Slice'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitslice'
documentation_source_path: 'ref/bitslice.html'
language: en
---

# Bit Slice

## Ports
```yaml
ports:
- name: Port_1
  summary: Input Signal scalar | vector
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Output Signal scalar | vector
  direction: output
  data_types: uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Input Signal scalar | vector

Input signal on which the bit-slice is performed. The input signal has a maximum
bit width of 128.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output Signal scalar | vector

Output signal that is bit-sliced. The word length of the output is computed as
`(MSB Position - LSB Position) + 1`, where **MSB
Position** and **LSB Position** are block
parameters.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: MSB Position
  summary: Most significant bit position 7 (default)
  group: ''
  block_parameter: lidk
  type: string scalar | character vector
  values: positive integer value such that satisfies the constraints mentioned previously
  default: '''7'''
- name: LSB Position
  summary: Least significant bit position 0 (default)
  group: ''
  block_parameter: ridk
  type: string scalar | character vector
  values: positive integer value such that satisfies the constraints mentioned previously
  default: '''0'''
```

### **MSB Position** — Most significant bit position 7 (default)

Specifies the bit position (zero-based) of the most significant bit (MSB) of the
field to extract.

For an input word size `WS`,**MSB Position** must
satisfy these constraints:

`WS > MSB Position >= LSB Position >= 0`

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `lidk` |
| **Type:** string scalar | character vector |
| **Value:** positive integer value such that satisfies the constraints mentioned previously |
| **Default:** `'7'` |

### **LSB Position** — Least significant bit position 0 (default)

Specifies the bit position (zero-based) of the least significant bit (LSB) of the
field to extract.

For an input word size `WS`, **LSB Position** must
satisfy these constraints:

`WS > MSB Position >= LSB Position >= 0`

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ridk` |
| **Type:** string scalar | character vector |
| **Value:** positive integer value such that satisfies the constraints mentioned previously |
| **Default:** `'0'` |
## Libraries

HDL Coder / Logic and Bit Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |

## Version History

**Introduced in R2014a**

## Description

Return field of consecutive bits from input signal

The Bit Slice block returns a field of consecutive bits from the input
signal. Specify the lower and upper boundaries of the bit field by using zero-based indices in
the **LSB Position** and **MSB Position** parameters. For an
input word size `WS`, **LSB Position** and **MSB
Position** must satisfy these constraints:

`WS > MSB Position >= LSB Position >= 0`
