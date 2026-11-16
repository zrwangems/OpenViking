---
type: simulink-block
title: 'IO Data Sink'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Testbench'
documentation_page: 'iodatasink'
documentation_source_path: 'ref/iodatasink.html'
language: en
---

# IO Data Sink

## Ports

### Input

### **msg** — SoC message data numeric vector

This port receives the data vector from the **msg** port of the
processor I/O blocks, which includes Stream
WriteTCP Write,
UDP Write, or
Register Write
blocks.

**Data Types:** `SoCData`
### Output

### **data** — Output data numeric vector

Output data, returned as a numeric vector. The block converts the received input
message into a data signal.

#### Dependencies

To enable this port, set the **Output** parameter to
`To output port`.

**Data Types:** `uint32` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `Boolean` | `fixedpoint`

### **length** — Length of output data nonnegative scalar

Length of output data, returned as a nonnegative scalar.

#### Dependencies

To enable this port, set the **Output** parameter to
`To output port`.

**Data Types:** `double`

### **valid** — Indication of valid data `Boolean` scalar

Control signal that indicates whether the output data is valid. When this value is
`1` (true), the value on the output **data** port
is valid.

#### Dependencies

To enable this port, set the **Output** parameter to
`To output port`.

**Data Types:** `Boolean`

### **done** — Completion of data streaming `Boolean` scalar

When **done** is `1`, the block has no more
stream output data to return in the **data** port. When
**done** is `0`, the block has more stream data to
return in the **data** port.

#### Dependencies

To enable this port, set the **Device type** parameter to
`Stream`.

**Data Types:** `Boolean`

### **event** — Task event signal scalar

This port sends a task event signal that triggers the Task Manager
block to execute the associated event-driven task.

#### Dependencies

To enable this port, set the **Show port** parameter to
`Data and Event`.

**Data Types:** `rteEvent`

## Parameters

### **Output** — Sink of output data from block `To file` (default) | `To output port` | `To terminator`

Set the sink of output data from the block by selecting one of these values.

- `To file` — Save output data to a file.
- `To output port` — Output data and signals by using
  output ports on the block.
- `To terminator` — Terminate the received input
  signal.

### **Device type** — Device type selection `UDP` (default) | `TCP` | `Register` | `Stream`

Select a device type to enable the corresponding input data port.

- `UDP` — Enable the **msg** input
  port to receive UDP data as message from a **msg** port of UDP Write
  block.
- `TCP` — Enable the **msg** input
  port to receive TCP data as message from a **msg** port of TCP Write
  block.
- `Register` — Enable the **msg**
  input port to receive Register data as message from a **msg**
  port of Register
  Write block.
- `Stream` — Enable the **msg** input
  port to receive Stream data as message from a **msg** port of
  Stream
  Write block.

### **Show port** — Enable output ports `Data` (default) | `Data and Event`

Select one of these values to enable the corresponding output ports towards the
writing source.

- `Data` — Enable only the **msg** input
  port.
- `Data and event` — Enable the **msg**
  input and **event** output ports.

### **Number of buffers** — Number of data buffers `8` (default) | nonnegative scalar

Specify the number of data elements to store in the data queue. This parameter must
match the **Number of buffers** parameter specified in the
Memory Channel block.

#### Dependencies

To enable this parameter, set the **Device type** parameter to
`Stream`.

### **Sample time** — Time interval of sampling `-1` (default) | nonnegative numeric scalar

Specify a discrete time interval, in seconds, at which the block outputs data. The
default value `-1` inherits the sample time from the solver used for
simulating the model.

### **Dataset name** — Name of data file no default | file path

Specify the full path to where you want to save the file on the host PC. This block
saves the output data as a TGZ file. You can import this file into the model by using
the IO Data Source
block.

#### Dependencies

To enable this parameter, set the **Output** parameter to
`To file`.

### **Source name** — Name of dataset no default

Specify a name for the output data source in which to save the data in the dataset
file.

#### Dependencies

To enable this parameter, set the **Output** parameter to
`To file`.

### **Data type** — Data type of output data `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `boolean` | `fixedpoint`

Select the data type of the output data. This value must match the data type of the
input data.

#### Dependencies

To enable this parameter, set the **Output** parameter to
`To file` or `To output
port`.

## Libraries

SoC Blockset / I/O Data Source and Sink

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To automatically generate C code for your design, and execute
on an SoC device, use the SoC Builder tool. To
generate and execute C code for your SoC models, Embedded Coder® features are required. For more information on generating code for SoC designs,
see Use SoC Builder to Generate SoC Design.

Embedded Coder does not generate code for this block. In the
generated code, the device I/O connects directly to the TCP Write, UDP Write, or Register Write
block.

## Version History

**Introduced in R2019a**

## Description

Record, output, or terminate input message

The IO Data Sink block records, outputs, or terminates the received input
message signal. The input of this block connects to the output of the TCP Write, UDP Write, or Register Write block.
This block enables you to save the received input data to a file that you can play back using
the IO Data Source block in
the model. You can also terminate the signal or output the signals through an output port
which can be fed as an input to IO Data Source block.
