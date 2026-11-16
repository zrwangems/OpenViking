---
type: simulink-block
title: 'HDL FIFO'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / RAM and ROM Blocks'
documentation_page: 'hdlfifo'
documentation_source_path: 'ref/hdlfifo.html'
language: en
---

# HDL FIFO

## Ports

### Input

### **In** — Data input signal `scalar`

Data input signal to the FIFO block. When you write data into the
FIFO, the newest data is pushed to the end of the FIFO register. The
block pushes subsequent data entries below this entry.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **Push** — Write control signal `scalar`

When this port receives a value of `1`, the block
pushes the input at the `In` port onto the end of the
FIFO register.

**Data Types:** `Boolean`

### **Pop** — Read control signal `scalar`

When this port receives a value of `1`, the block
pops the first element off the FIFO register and holds the
`Out` port at that value.

**Data Types:** `Boolean`

**Note**

If two or more of the control input ports are triggered in the same time step,
the pop operation executes first, followed by the push operation.

### **rst** — Reset control signal `scalar`

When the reset port receives a value of `1`, it
resets the Empty, Full, and Num outputs of the HDL FIFO block.

#### Dependencies

To enable this port, select the block parameter **Local
reset port**.

**Data Types:** `Boolean`
### Output

### **Out** — Data output signal `scalar`

Data output signal from the FIFO block. When you read data from the
FIFO, the data that you wrote first into the FIFO register comes off the
FIFO and is held at the output.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **Empty** — Data output signal `scalar`

Control signal output from the FIFO that becomes `1`
when the FIFO register is empty and does not contain data
entries.

#### Dependencies

To enable this port, **Show empty register indicator port
(Empty)** must be selected.

**Data Types:** `Boolean`

### **Full** — Data output signal `scalar`

Control signal output from the FIFO that becomes `1`
when the FIFO register is full and cannot take more data entries.

#### Dependencies

To enable this port, **Show full register indicator port
(Full)** must be selected.

**Data Types:** `Boolean`

### **Num** — Number of entries `scalar`

Number of data entries that are currently inside the FIFO register.
**Num** increments by `1` for
every data that you write into the FIFO. **Num**
decrements by `1` for every data that you read from the
FIFO.

#### Dependencies

To enable this port, **Show number of entries register
port (Num)** must be selected.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Register size** — Number of entries `10` (default)

Specify the number of entries that the FIFO register can hold. The default
value for **Register size** is `10`. The
minimum value for **Register size** is
`4`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `fifo_size` |
| **Type:** character vector |
| **Value:** An integer greater than or equal to four |
| **Default:** `'10'` |

### **Mode** — Operation mode `'Classic'` (default) | `'FWFT'`

Specify the operation mode of the FIFO. By default, the
**Mode** is set to `Classic`. You see
that the block icon displays `Classic FIFO`. You can change
the **Mode** to `FWFT`. When you change
the **Mode**, the block icon displays `FWFT
FIFO`. By using the `FWFT` mode, you can
lookahead and see the first word written to the FIFO register without
placing a read request. The FWFT mode is especially useful when you apply
the back-pressure with AXI4-Stream interfaces.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `mode` |
| **Type:** character vector |
| **Value:** `'Classic'` | `'FWFT'` | |
| **Default:** `'Classic'` |

### **The ratio of output sample time to input sample time** — Sample rate ratio `1` (default)

Specify the ratio of output sample time to input sample time. The default
ratio is `1`, which means that the inputs
`In` and `Push`, and outputs
`Out` and `Pop`, run at the same
sample rate. The inputs and outputs can run at different sample times. Use a
positive integer or `1/N`, where `N` is a
positive integer. For example, if you enter `1/2`, the
output sample time is half the input sample time, or the outputs run faster.
The `Full`, `Empty`, and
`Num` signals run at the faster rate.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ratio` |
| **Type:** character vector |
| **Value:** An integer greater than or equal to one |
| **Default:** `'1'` |

### **Push onto full register** — Overflow condition `'Warning'` (default) | `'Ignore'` | `'Error'`

Specify how you want the block to respond when you write to a FIFO that is
full. The default is `Warning`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `push_msg` |
| **Type:** character vector |
| **Value:** `'Warning'` | `'Ignore'` | `'Error'` |
| **Default:** `'Warning'` |

### **Pop empty register** — Underflow condition `'Warning'` (default) | `'Ignore'` | `'Error'`

Specify how you want the block to respond when you read from a FIFO that
is empty. The default is `Warning`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `pop_msg` |
| **Type:** character vector |
| **Value:** `'Warning'` | `'Ignore'` | `'Error'` |
| **Default:** `'Warning'` |

### **Show empty register indicator port (Empty)** — Optional empty port on (default) | off

Specify whether to enable the `Empty` output port. This
port outputs a `1` when the FIFO register is empty and
`0` when the FIFO contains one or more data
entries.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `show_empty` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Show full register indicator port (Full)** — Optional full port on (default) | off

Specify whether to enable the `Full` output port. This
port outputs a `1` when the FIFO register is full.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `show_full` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Show number of register entries port (Num)** — Optional num port on (default) | off

Specify whether to enable the `Num` output port. This
port outputs the number of data entries that are currently available in the
FIFO queue.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `show_num` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Local reset port** — Optional reset port off (default) | on

Specify whether to insert an additional `rst` input port.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `rst_port` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |

## Libraries

HDL Coder / HDL RAMs

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized
logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **General** | |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |
| **RAMDirective** | Specify whether to map RAM blocks in your design to the memory blocks, such as distributed RAMs, block RAMs, or UltraRAM, on the target FPGA. The default value is `empty string`. See also RAMDirective. |

## Version History

**Introduced in R2014a**

### R2024a: Half-Precision and Boolean Data Support

The block now supports HDL code generation with input data of type
`Half` or
`Boolean`.

## Description

Stores sequence of input samples in first in, first out (FIFO) register

The HDL FIFO block stores a sequence of input samples in a first in, first
out (FIFO) register. The data written first into the FIFO register comes out first. The
block implementation resembles the FIFO unit in hardware platforms in terms of
functionality and behavior.

The HDL FIFO block uses the Simple Dual Port
RAM System block internally. You can use the HDL FIFO block
to generate HDL code that maps to RAM in most FPGAs.
