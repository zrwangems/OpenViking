---
type: simulink-block
title: 'Serializer1D'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Operations'
documentation_page: 'serializer1d'
documentation_source_path: 'ref/serializer1d.html'
language: en
---

# Serializer1D

## Ports

### Input

### **P** — Parallel data input signal `scalar` | `vector`

Input signal to serialize. Bus data types are not supported.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **ValidIn** — Valid input control signal `scalar`

Input control signal that indicates valid input signal. This port is available
when you select the **ValidIn** check box.

**Data Types:** `Boolean`
### Output

### **S** — Serialized data output signal `scalar` | `vector`

Serialized output signal. Bus data types are not supported.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **StartOut** — Start out control signal `scalar`

Output control signal that indicates the start of serialization. You can use this
signal as the **StartIn** input to the Deserializer1D block. To use this
port, select the **StartOut** check box.

**Data Types:** `Boolean`

### **ValidOut** — Valid output control signal `scalar`

Output control signal that indicates valid output signal. You can use this signal
as the **ValidIn** input to the Deserializer1D block. This port is
available when you select the **ValidOut** check box.

**Data Types:** `Boolean`

## Parameters

### **Ratio (Output Vector Size/Input Vector Size)** — Ratio of input vector size to output vector size 1 (default)

Serialization factor, specified as a positive scalar.

The ratio is equal to the size of the input vector divided by the size of the output
vector. Input vector size must be divisible by the ratio.

### **Idle Cycles** — Number of idle cycles 0 (default)

Enter the number of idle cycles added at the end of each output.

### **StartIn** — Enable StartIn control port off (default) | on

Select to activate the StartIn port.

### **ValidIn** — Enable ValidIn control port off (default) | on

Select to activate the ValidIn port.

### **ValidOut** — Enable ValidOut control port off (default) | on

Select to activate ValidOut port.

### **Input data port dimensions (-1 for inherited)** — Size of the input data signal -1 (default)

Size of the input data signal. Input vector size must be divisible by the ratio. By
default, the block inherits size based on the context within the model.

### **Input sample time (-1 for inherited)** — Input sample time -1 (default)

Time interval between sample time hits, or another
appropriate sample time such as continuous. By default,
the block inherits sample time based on context within the model. For more information,
see Sample Time.

### **Input signal type** — Input signal type of the block auto (default) | real | complex

Input signal type of the block, specified as `auto`,
`real`, or `complex`. Default is
`auto`.

## Libraries

HDL Coder / HDL Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized logic.

**HDL Architecture**

**Note**

For simulation results that match the generated HDL code, in the Solver pane of the
Configuration Parameters dialog box, clear the checkbox for **Treat each
discrete rate as a separate task**. When the checkbox is cleared,
single-tasking mode is enabled. If you simulate the block with this check box selected,
the output data can update in the same cycle but in the generated HDL code, the output
data is updated one cycle later.

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |

## Version History

**Introduced in R2014b**

### R2024a: Half-Precision and Boolean Data Support

The block now supports HDL code generation with input data of type
`Half` or `Boolean`.

## Description

Convert vector signal to scalar or smaller vectors

The Serializer1D block converts a slower vector signal into a faster stream
of scalar signals or smaller size vector signals based on the **Ratio** and
**Idle Cycle** values. To match the faster serialized output, the sample
time changes according to this equation:

Output Sample Time=Input Sample Time/(Ratio+Idle Cycles)

Consider this example where the input data is a vector of size 4 and the
**Ratio** is set to 4.

Timing Diagram of the Input and Output of the Serializer Block

The output data serializes each of the vector signals into four scalar signals. The sample
time at the output is: Output Sample Time=Input Sample Time/4.

To add idle cycles at the end of each output, for **Idle Cycles**,
specify an integer greater than zero. Consider this example with **Ratio**
set to 4 and **Idle Cycles** set to 2.

Timing Diagram of the Input and Output of the Serializer Block with Idle Cycles

For each slow vector signal, the output has six fast cycles consisting of the four
serialized scalar signals and two idle cycles. The sample time at the output is Output Sample Time=Input Sample Time/6.

The Serializer1D block provides three control signals:
**ValidIn**, **ValidOut**, and
**StartOut**. You can use **ValidIn** to control
**ValidOut** and **StartOut**. The serialized output does
not depend on **ValidIn**. To determine whether the output serialized data is
valid, use **ValidIn** and **ValidOut**. If you give a high
input to **ValidIn**, and there are no idle
cycles, **ValidOut** gives a high output, which indicates that the output
serialized data is valid.

Consider an example that has input data as a vector of size 4, **Ratio**
set to 4, **Idle Cycles** set to 2, and uses
all three control signals.

Timing Diagram of the Input and Output of the Serializer Block with Idle Cycles and three control signals

For the first input vector, `ABCD`, **ValidIn** is
false. **StartOut** and **ValidOut** become false. This
means that the output data values are not valid. In the waveform, the data values are
represented as `X`, which correspond to *don’t care*
values.

For the second input vector, `ABCE`, **ValidIn** is
true. The output data serializes the vector into four scalar signals. The control signal
**StartOut** becomes true at output `A` to indicate the
start of serialization. In the next cycle, the **StartOut** signal becomes
false. **ValidOut** is true for all four
output signals indicating valid output data for the four cycles. **ValidOut**
becomes false for the idle cycles, and the output data values are *don’t
care* values.
