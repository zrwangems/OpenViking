---
type: simulink-block
title: 'Digital Filter Design'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'digitalfilterdesign'
documentation_source_path: 'ref/digitalfilterdesign.html'
language: en
---

# Digital Filter Design

## Ports

### Input

### **Port\_1** — Input signal vector | matrix

Signal to filter, specified as a vector or matrix of real values. When
given matrix input, the block treats each column as an independent
channel.

The sample rate, `Fs`, that you specify in the
filter designer app must be identical to the sample rate of the input to
the Digital Filter Design block. When the sampling frequencies do not
match, the Digital Filter Design block returns a warning message and
inherits the sample rate of the input block.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output signal vector | matrix

Filtered signal, returned as a vector or a matrix of real
values.

**Data Types:** `single` | `double`

## Parameters

### Dialog Box

For more information about the parameters in this dialog box, see Using Filter Designer.

## Libraries

DSP System Toolbox / Filtering / Filter Designs

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

**Generate SIMD code using Intel AVX2 code replacement
library**

**Note**

Requires Embedded Coder® license

The Digital Filter Design block supports SIMD code generation using
Intel AVX2 code replacement library under these conditions:

- **Input processing** is set to `Columns
  as channels (frame based)`.
- **Filter Structure** (in **Import Filter from
  Workspace** pane) is set to `Direct-Form
  FIR`. You can generate SIMD code even when the filter
  is a `Direct-Form FIR Transposed` filter. To
  create a `Direct-Form FIR Transposed` filter,
  select **Edit** > **Convert
  Structure**, and click **Direct-Form FIR
  Transposed**.
- Input signal has a data type of `single` or
  `double`.

**Generate SIMD code by leveraging target hardware instruction
set extensions**

**Note**

Requires Simulink®
Coder™ or Embedded Coder license

You can generate SIMD code for the Digital Filter Design block on
all Intel® platforms, ARM®
Cortex®-A processors, and Apple silicon processors by using the model configuration parameter
**Leverage target hardware instruction set extensions** under
these conditions:

- **Input processing** is set to `Columns
  as channels (frame based)`.
- **Filter Structure** (in **Import Filter from
  Workspace** pane) is set to `Direct-Form
  FIR`.
- Data type of the input signal is `single`
  (ARM
  Cortex-A processors)
- Data type of the input signal is `single` or
  `double` (Intel platforms)

The SIMD technology significantly improves the performance of the generated code.
For more information, see SIMD Code Generation. To
generate SIMD code from this block, see:

- Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks
- Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Intel Platforms
- Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon
- Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for ARM Cortex-A Processors

## Version History

**Introduced before R2006a**

### R2024b: Generate SIMD code for Apple silicon processors

In R2024b, if you have Embedded Coder, you can generate SIMD code for the Digital Filter
Design block for Apple silicon processors by using the model configuration parameter
**Leverage target hardware instruction set extensions**. For
more information, see Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon.

## Description

Design and implement digital FIR and IIR filters

Use this block to design, analyze, and efficiently implement floating-point
filters.

The Digital Filter Design block implements a digital Finite Impulse Response (FIR) or
Infinite Impulse Response (IIR) filter that you design by using the Filter
Designer (`filterDesigner`) app. This block provides
the same filter implementation as the Discrete FIR Filter or Biquad Filter
blocks.

You must specify whether the block performs frame-based or sample-based processing on the input
by setting the **Input processing** parameter. The block applies the
specified filter to each channel of a discrete-time input signal and outputs the result.
The outputs of the block numerically match the outputs of the Discrete FIR Filter or
Biquad Filter block and the MATLAB®
`filter` function. For more information,
see Getting Started with Filter Designer.

The Discrete FIR Filter (Simulink) and Biquad Filter blocks also implement digital filters, but serve a slightly
different purpose. Use these blocks to efficiently implement floating-point or
fixed-point filters that you have already designed. These blocks provide the same exact
filter implementation as the Digital Filter Design block.
