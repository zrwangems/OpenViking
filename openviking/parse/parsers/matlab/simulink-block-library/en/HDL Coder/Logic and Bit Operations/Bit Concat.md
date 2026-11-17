---
type: simulink-block
title: 'Bit Concat'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitconcat'
documentation_source_path: 'ref/bitconcat.html'
language: en
---

# Bit Concat

## Ports
```yaml
ports:
- name: H
  summary: Highest-order Input Word scalar | vector
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: L
  summary: Lowest-order Input Word scalar | vector
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Output
  summary: Concatenated Word scalar | vector
  direction: output
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **H** — Highest-order Input Word scalar | vector

The highest-order input word for the block to concatenate that becomes the
left-most value in the concatenated output signal.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **L** — Lowest-order Input Word scalar | vector

The lowest-order input word for the block to concatenate that becomes the
right-most value in the concatenated output signal.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Output** — Concatenated Word scalar | vector

The output is the concatenated word in low-to-high ordering of the input words.
The maximum concatenated output word size is 65535 bits.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Number of Inputs
  summary: Number of input signals 2 (default) | positive integer value less than or equal to 128
  group: ''
  block_parameter: numInputs
  type: string scalar | character vector
  values: A positive integer value less than or equal to 128
  default: '''2'''
```

### **Number of Inputs** — Number of input signals 2 (default) | positive integer value less than or equal to 128

Enter an integer specifying the number of input signals. The number of block input
ports updates when you change **Number of Inputs**.

- Default: 2
- Minimum: 1
- Maximum: 128

**Caution**

Make sure that the **Number of Inputs** is equal to the number of
signals you connect to the block. If the block has unconnected inputs, an error occurs
during code generation.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `numInputs` |
| **Type:** string scalar | character vector |
| **Value:** A positive integer value less than or equal to 128 |
| **Default:** `'2'` |
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

### R2024b: Maximum output word size is 65535 bits

The maximum concatenated output word size is 65535 bits. Prior to R2024b, the maximum
word size was 128 bits.

## Description

Concatenates up to 128 input words into single output

The Bit Concat block concatenates up to 128 input words into a single
output. The input port labeled `L` designates the lowest-order input word.
The input port labeled `H` designates the highest-order input word. For
scalar inputs, two or more input signals should be connected to the block. For vector inputs,
at least one input should be connected to the block. The block uses the `bitconcat` function such that the right-to-left ordering of words in the output
follows the low-to-high ordering of input signals. To learn how the block operates, see Algorithms.
