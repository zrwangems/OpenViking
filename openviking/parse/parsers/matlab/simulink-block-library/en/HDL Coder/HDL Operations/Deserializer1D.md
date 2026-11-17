---
type: simulink-block
title: 'Deserializer1D'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Operations'
documentation_page: 'deserializer1d'
documentation_source_path: 'ref/deserializer1d.html'
language: en
---

# Deserializer1D

## Ports
```yaml
ports:
- name: S
  summary: Serial input data signal scalar
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: ValidIn
  summary: Valid input control signal scalar
  direction: input
  data_types: Boolean
- name: StartIn
  summary: Start In control signal scalar
  direction: input
  data_types: Boolean
- name: P
  summary: Deserialized (Parallel) data output signal scalar | vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
- name: ValidOut
  summary: Valid out control signal scalar
  direction: output
  data_types: Boolean
```

### Input

### **S** — Serial input data signal scalar

Input signal to deserialize. Bus data types are not supported.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **ValidIn** — Valid input control signal scalar

Indicates valid input signal. Use with the Serializer1D block. This port is
available when you select the **ValidIn** check box.

**Data Types:** `Boolean`

### **StartIn** — Start In control signal scalar

Input control signal indicates when to start deserialization. Use with the Serializer1D block. Data collection
begins at the rising edge of the StartIn signal.

This port is available when you select the **StartIn** check
box.

**Data Types:** `Boolean`
### Output

### **P** — Deserialized (Parallel) data output signal scalar | vector

Deserialized output signal. Bus data types are not supported.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **ValidOut** — Valid out control signal scalar

Indicates valid output signal. This port is available when you select the
**ValidOut** check box.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Ratio (Output Vector Size/Input Vector Size)
  summary: Ratio of output vector size to input vector size 1 (default)
  group: ''
- name: Idle Cycles
  summary: Number of idle cycles 0 (default)
  group: ''
- name: Initial condition
  summary: Initial output data signal value 0 (default)
  group: ''
- name: StartIn
  summary: Enable StartIn control port off (default) | on
  group: ''
- name: ValidIn
  summary: Enable ValidIn control port off (default) | on
  group: ''
- name: ValidOut
  summary: Enable ValidOut control port off (default) | on
  group: ''
- name: Input data port dimensions (-1 for inherited)
  summary: Size of the input data signal 0 (default)
  group: ''
- name: Input sample time (-1 for inherited)
  summary: Input sample time -1 (default)
  group: ''
- name: Input signal type
  summary: Input signal type auto (default) | real | complex
  group: ''
```

### **Ratio (Output Vector Size/Input Vector Size)** — Ratio of output vector size to input vector size 1 (default)

Enter the deserialization ratio, specified as positive scalar

The ratio is the output vector size, divided by the input vector size. The ratio
must be divisible by the input vector size.

### **Idle Cycles** — Number of idle cycles 0 (default)

Enter the number of idle cycles added to the end of each serialized input.

The value of **Idle Cycles** affects the deserialized output rate.
For example, if **Ratio** is `2` and the input signal
is `A, B, B, C, D, D, ...`, without idle cycles the output would be
`AB, BC, DD...`. However for the same input and ratio with
**Idle Cycles** set to `1`, the output is
`AB, CD...`. The idle cycles, `B` and
`D`, are dropped.

The Deserializer1D behavior changes if **Idle
Cycles** is not zero, and **ValidIn** or
**StartIn** are on. The idle cycles value affects only the output
rate, while **ValidIn** and **StartIn** control what
input data is deserialized.

### **Initial condition** — Initial output data signal value 0 (default)

Specify the initial output of the simulation.

### **StartIn** — Enable StartIn control port off (default) | on

Select to activate the StartIn port.

### **ValidIn** — Enable ValidIn control port off (default) | on

Select to activate the ValidIn port.

### **ValidOut** — Enable ValidOut control port off (default) | on

Select to activate ValidOut port.

### **Input data port dimensions (-1 for inherited)** — Size of the input data signal 0 (default)

Enter the size of the input data signal. The input size must be divisible by the
ratio plus the number of idle cycles. By default, the block inherits size based on
context within the model.

### **Input sample time (-1 for inherited)** — Input sample time -1 (default)

Enter the time interval between sample time hits or specify another
appropriate sample time such as continuous. By default,
the block inherits its sample time based on context within the model. For more
information, see Sample Time.

### **Input signal type** — Input signal type auto (default) | real | complex

Specify the input signal type of the block as `auto`,
`real`, or `complex`.
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

Convert scalar stream or smaller vectors to vector signal

The Deserializer1D block buffers a faster, scalar stream or vector signals
into a larger, slower vector signal. The faster input signal is converted to a slower signal
based on the **Ratio** and **Idle Cycle** values, the
conversion changes sample time. Also, the output signal is delayed one slow signal cycle
because the serialized data needs to be collected before it can be output as a vector. See the
examples below for more details.

You can configure the deserialization to depend on a valid input signal ValidIn and a
start signal StartIn. If the **ValidIn** and **StartIn**
block parameters are both selected, data collection starts only if both ValidIn and StartIn
signals are true. Consider this example:

Timing diagram illustrates the variations in Output corresponding to the changes in ValidIn, StartIn, and Input signals.

- **Ratio** is `2` and **Idle
  Cycles** is `0`, so each output cycle is two input signals
  long with all data points considered.
- **ValidIn** and **StartIn** are selected, so data
  collection can begin only when both StartIn and ValidIn signals are true.
- **ValidOut** is selected.

In the first cycle, ValidIn and StartIn are true, so data collection begins for A and B.
The block outputs the deserialized vector in the next valid cycle, so the AB vector is output
in the next cycle. This is also true in the second cycle for C and D.

In the third cycle, starting at E, StartIn is true, but ValidIn is not. E is dropped. At
F, ValidIn is true, but StartIn is not, so F is also dropped. Since it cannot collect data for
E or F, Deserializer1D outputs the previous cycle vector, CD, but ValidOut
changes to false.

Another scenario to consider is when the StartIn signal arrives too early. If the length
between two StartIn signals is not long enough to collect a full ratio cycle, the insufficient
signal data is dropped. Consider this example:

Timing diagram illustrates the variations in Output corresponding to the changes in ValidIn, StartIn, and Input signals.

- **Ratio** is `3`, so each cycle is two sections
  long.
- **Idle Cycles** is `0`, so
  all data inputs are considered.
- **ValidIn** and **StartIn** are selected, so data
  collection can begin only when both StartIn and ValidIn signals are true.
- **ValidOut** is selected.

In the first cycle, ValidIn and StartIn are true, so data collection can begin for A and
B. However, at C another StartIn signal arrives before three signals can be collected. Because
the StartIn arrived early, A and B are dropped and no valid
vector is collected during the first cycle. Therefore, the output of the second cycle is still
zero. Deserialization begins at the StartIn at C, for C, D, and E. This vector is output at
the next valid cycle, which is cycle 3. Similarly, deserialization starts again at the StartIn
at F, and outputs the FGH vector in the fourth cycle.

You specify the block output for the first sampling period with the value of the
**Initial condition** parameter.
