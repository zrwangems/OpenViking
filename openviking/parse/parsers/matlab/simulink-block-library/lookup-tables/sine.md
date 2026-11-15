---
type: simulink-block
title: 'Sine'
family: lookup-tables
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'sine'
---

# Sine

Implement fixed-point sine or cosine wave using lookup table approach that exploits quarter wave symmetry

## Libraries

Simulink / Lookup Tables

## Description

The Sine and Cosine blocks implement a sine wave, cosine
wave, or both in fixed point using a lookup table method that exploits quarter wave
symmetry. The block can output the following functions of the input signal, depending
upon what you select for the **Output formula** parameter:

- sin(2π*u*)
- cos(2π*u*)
- exp(*j*2π*u*)
- sin(2π*u*) and
  cos(2π*u*)

You define the number of lookup table points in the **Number of data points
for lookup table** parameter. The block implementation is most efficient
when you specify the lookup table data points to be
`(2^n)+1`, where *n* is an
integer.

Use the **Output word length** parameter to specify the word length
of the fixed-point output data type. The fraction length of the output is the output
word length minus 2.

## Ports

### Input

### **u** — Input signal to implement as fixed-point sine or cosine wave real-valued signal

Input signal, u, specified as a real-valued scalar, vector, or
matrix.

To obtain meaningful block output, the block input values should fall
within the range [0, 1). For input values that fall outside this range,
the values are cast to an unsigned data type, where overflows wrap. For
these out-of-range inputs, the block output might not be
meaningful.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **sin(2\*pi\*u)** — Fixed-point sine wave real-valued fixed-point signal

Fixed-point sine wave, implemented using a lookup table approach.

#### Dependencies

This port is enabled when the **Output formula**
is set to `sin(2*pi*u)` or
`sin(2*pi*u) and cos(2*pi*u)`.

**Data Types:** `fixed point`

### **cos(2\*pi\*u)** — Fixed-point cosine wave real-valued fixed-point signal

Fixed-point cosine wave, implemented using a lookup table
approach.

#### Dependencies

This port is enabled when the **Output formula**
is set to `cos(2*pi*u)` or
`sin(2*pi*u) and cos(2*pi*u)`.

**Data Types:** `fixed point`

### **exp(j\*2\*pi\*u)** — exp(j\*2\*pi\*u) complex-valued fixed-point signal

`exp(j*2*pi*u)`,
implemented using a lookup table approach.

#### Dependencies

This port is enabled when the **Output formula**
is set to `exp(j*2*pi*u)`.

**Data Types:** `fixed point`

## Parameters

### **Output formula** — Select the signals to output `cos(2*pi*u)` | `sin(2*pi*u)` | `exp(j*2*pi*u)` | `sin(2*pi*u) and cos(2*pi*u)`

Select the signals to output.

For the Sine block, the default value of this parameter is
`sin(2*pi*u)`.

For the Cosine block, the default value of this parameter
is `cos(2*pi*u)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Formula` |
| **Values:** `'sin(2*pi*u)' | 'cos(2*pi*u)' | 'exp(j*2*pi*u)' | 'sin(2*pi*u) and cos(2*pi*u)'` |

### **Number of data points for lookup table** — Specify the number of data points to retrieve from the lookup table `(2^5)+1` (default) | integer greater than or equal to 2

The implementation is most efficient when you specify the lookup table
data points to be `(2^n)+1`, where
*n* is an integer. To be compatible with the
**Output word length** parameter, the **Number
of data points for lookup table** must be less than or equal to (2^(**Output word
length**-2)+1).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumDataPoints` |
| **Type:** scalar |
| **Value:** integer greater than or equal to 2 |
| **Default:** `'(2^5)+1'` |

### **Output word length** — Specify the word length for the fixed-point data type of the output signal `16` (default) | integer from 2 to 53

The fraction length of the output is the output word length minus 2. To be
compatible with the **Number of data points for lookup
table** parameter, (2^(**Output word length** - 2)
+1) must be greater than or equal to **Number of data
points for lookup table**.

**Note**

The block uses double-precision floating-point values to construct
lookup tables. Therefore, the maximum amount of precision you can
achieve in your output is 53 bits. Setting the word length to values
greater than 53 bits does not improve the precision of your
output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputWordLength` |
| **Type:** scalar |
| **Value:** integer from 2 to 53 |
| **Default:** `'16'` |

### **Internal rule priority for lookup table** — Specify the internal rule for intermediate calculations `Speed` (default) | `Precision`

Select `Speed` for faster calculations. If you
do, a loss of accuracy might occur, usually up to 2 bits.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InternalRulePriority` |
| **Values:** `'Speed' | 'Precision'` |
| **Default:** `'Speed'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

The HDL code implements Cosine and Sine blocks
by using the quarter-wave lookup table that you specify in the Simulink block
parameters.

To avoid generating a division operator
(`/`) in the HDL code, for **Number of data points
for lookup table**, enter
`(2^n)+1`.
*`n`* is an integer.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Limitations**

If you use Intel® MAX 10 device, to map the lookup table to RAM, add this Tcl
command when creating the project in the Quartus tool:

`set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE "SINGLE IMAGE
WITH ERAM"`

**Note**

Lookup table-based sine and cosine blocks do not generate
hardware-optimized HDL code. For better synthesis results, use Sine HDL Optimized and Cosine HDL Optimized (HDL Coder) blocks.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
