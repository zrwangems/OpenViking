---
type: simulink-block
title: 'Demux'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Routing'
documentation_page: 'demux'
documentation_source_path: 'slref/demux.html'
language: en
---

# Demux

## Ports

### Input

### **Port\_1** — Accept nonbus vector signal to extract and output signals from real or complex values of any nonbus data type supported by Simulink® software

Vector input signal from which the Demux block selects
scalar signals or smaller vectors.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`
### Output

### **Port\_1** — Output signals extracted from input vector signal nonbus signal with real or complex values of any data type supported by Simulink software

Output signals extracted from the input vector. The output signal
ports are ordered from top to bottom. For a description of the port order for various
block orientations, see Identify Port Location on Rotated or Flipped Block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

## Parameters

### **Number of outputs** — Number of outputs 2 (default) | scalar | vector

Specify the number of outputs and, optionally, the dimensionality of each output
port.

The value can be a scalar specifying the number of outputs or a vector whose elements
specify the widths of the block output ports. The block determines the size of its
outputs from the size of the input signal and the value of the **Number of
outputs** parameter.

If you specify a scalar for the **Number of outputs** parameter, and all
of the output ports are connected, as you draw a new signal line close to the output
side of a Demux block, the software adds a port and updates the
**Number of outputs** parameter.

For an input vector of width `n`, this table describes what the
block outputs.

| Parameter Value | Block Output | Examples and Comments |
| --- | --- | --- |
| `p = n` | `p` scalar signals | If the input is a three-element vector and you specify three outputs, the block outputs three scalar signals. |
| `p > n` | Error | This value is not supported. |
| `p < n`  `n mod p = 0` | `p` vector signals each having `n/p` elements | If the input is a six-element vector and you specify three outputs, the block outputs three two-element vectors. |
| `p < n`  `n mod p = m` | `m` vector signals each having `(n/p)+1` elements and `p-m` signals having `n/p` elements | If the input is a five-element vector and you specify three outputs, the block outputs two two-element vector signals and one scalar signal. |
| `[p`1`p`2 `... p`m`]`  `p`1`+p`2`+...+p`m`=n`  `p`i`> 0` | `m` vector signals having widths `p1`, `p2`, ... `pm` | If the input is a five-element vector and you specify `[3, 2]` as the output, the block outputs three of the input elements on one port and the other two elements on the other port. |
| An array that has one or more of `m` elements with a value of `-1`, which specifies that the software infers the size for the element.  For example, suppose that you have a four-element array with a total width of 14 and you specify the parameter to be `[p`1`p`2 `-1``p`4`]`.  The value for the third element (the `-1` element) is `14 -` `(p1 + p2 + p4)` | `m` vector signals | If `p`i is greater than zero, the corresponding output has width `p`i. If `p`i is -1, the width of the corresponding output is computed dynamically. |
| `[p`1`p`2 `... p`m`]`  `p`1`+p`2`+...+p`m`!=n`  `p`i`= > 0` | Error | This value is not supported. |

If you specify a number of outputs that is smaller than the number of input elements, the
block distributes the elements as evenly as possible over the outputs.

Specifying
a nondouble value, such as `single(3)`, is not
supported.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Outputs` |
| **Values:** | `'2'` (default) | scalar in quotes | vector in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'Outputs','4')`

### **Display option** — Displayed block icon `bar` (default) | `none`

By default, the block icon is a solid bar of the block foreground color.
To display the icon as a box containing the block type name, select
`none`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `DisplayOption` |
| **Values:** | `'bar'` (default) | `'none'` |

**Example:** `set_param(gcb,'DisplayOption','none')`

## Libraries

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

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

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced before R2006a**

## Description

Extract and output elements of virtual vector signal

The Demux block extracts the components of an input vector signal and
outputs separate signals. The output signal ports are ordered from top to bottom.
