---
type: simulink-block
title: 'IO Data Source'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Testbench'
documentation_page: 'iodatasource'
documentation_source_path: 'ref/iodatasource.html'
language: en
---

# IO Data Source

## Ports

### Input

### **data** — Input data numeric vector

Input data, specified as a numeric vector. The block converts this data into a bus
signal of the specific device type specified by the **Device type**
parameter. Match the data type of this input data with the data type you select in the
**Data type** parameter. The output bus signal consists of data
values, length of data, and valid status of data.

#### Dependencies

To enable this port, set the **Input** parameter to
`From input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **length** — Length of input data nonnegative scalar

Length of input data, specified as a nonnegative scalar.

#### Dependencies

To enable this port, set the **Input source** parameter to
`From input port`.

**Data Types:** `uint32`

### **valid** — Valid data signal `Boolean` scalar

When **valid** is `1`, the block captures the input data
from the **data** and **length** ports. When **valid** is
`0`, the block considers the input data as invalid and does not
capture it.

#### Dependencies

To enable this port, set the **Input source** parameter to
`From input port`.

**Data Types:** `Boolean`

### **done** — Notification of freed buffer in memory `False` (default) | `True`

This message port receives a notification from the connected Memory Channel
or IO Data Sink
block that a read transaction completed, and that a buffer in memory is available for
writing.

#### Dependencies

To enable this port, set the **Device type** parameter to
`Stream`.

**Data Types:** `Boolean`
### Output

### **event** — Task event signal scalar

This port sends a task event signal that triggers the Task Manager
block to execute the associated event-driven task.

#### Dependencies

To enable this port, set the **Show port** parameter to
`Event` or `Data and
event`.

**Data Types:** `rteEvent`

### **msg** — SoC message data numeric vector

This port sends the data vector as a message to the **msg** input
port of processor I/O blocks, which includes Register Read, Stream Read,
UDP Read, and
TCP Read
blocks.

#### Dependencies

To enable this port, set the **Show port** parameter to
`Data` or `Data and
Event`.

**Data Types:** `SoCData`

## Parameters

### **Input** — Source of input data `From file` (default) | `From dialog` | `From input port` | `From timeseries object`

Set the input data source for the block by selecting one of these values.

- `From file` — Read data from a recorded data file at
  the same time interval at which it was recorded on the hardware board.
- `From dialog` — Input a one-dimensional array of data
  by using a function. Specify this function for the **Value**
  parameter.
- `From input port` — Input data and signals using input
  ports on the block.
- `From timeseries object` — Input data and time values
  using a timeseries object that you created in MATLAB®. For more information see Time Series Objects and Collections.

### **Value** — Value of source data `uint32(1:1024)` (default) | function to generate input data

Specify a MATLAB function that creates a row vector of numeric data. This row vector is
captured as the input data for the block.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`From dialog`.

### **Data type** — Data type of input data `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `boolean` | `fixed point`

Select the data type of the input data to be received by the **data**
port.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`From file`.

### **Device type** — Device type of input data source `UDP` (default) | `TCP` | `Register` | `Stream`

Select a device type to enable the corresponding output data port.

- `UDP` — Enables the **msg** output
  port to output UDP data as a message.
- `TCP` — Enables the **msg** output
  port to output TCP data as a message.
- `Register` — Enables the **msg**
  output port to output Register data as a message.
- `Stream` — Enables the **msg**
  output port to output Stream data as a message.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`From input port` or `From
dialog`.

### **Sample time** — Time interval of sampling `-1` (default) | nonnegative scalar

Specify a discrete time interval, in seconds, at which the block outputs
data.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`From dialog`.

### **Dimensions** — Samples per frame `1024` (default) | nonnegative scalar

Specify the size of the input data. The block reads this number of samples per frame
during reading and playback in simulation.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`From file`.

### **Dataset name** — Name of recorded file no default | file path

Specify the full path to a recorded data file on the host PC or browse and select a
file on the host PC. This block supports only TGZ files created by using the SoC Blockset™ data recording API.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`From file`.

### **Source name** — Name of dataset no default

Specify the dataset source name you want to use as the input source available within
the recorded data specified in the **Dataset name** parameter. You
can either type the name in the **Source name** box or click
**Select** to select the name from the list of sources available in
the recorded data file.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`From file`.

### **Number of buffers** — Number of data buffers `1024` (default) | nonnegative scalar

Specify the number of data elements to store in the input data queue.

#### Dependencies

To enable this parameter, set the **Device type** parameter to
`Stream`.

### **Show port** — Enable output ports `Data` (default) | `Event` | `Data and event`

Select one of these values to enable the corresponding output ports.

- `Data` — Enable only the **msg**
  output port.
- `Event` — Enable only the **event**
  output port.
- `Data and event` — Enable the **msg**
  and **event** output ports.

### **Object name** — Name of timeseries object `[]` (default) | timeseries object

Specify a `timeseries` object. This `timeseries`
object provides the input data for the block. For more information about time series
objects, see Time Series Objects and Collections.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`From timeseries object`.

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
generated code, the device I/O connects directly to the TCP Read, UDP Read, Stream Read, or
Register Read block.

## Version History

**Introduced in R2019a**

## Description

Play back recorded data

The IO Data Source block enables you to import recorded hardware IO data
and play it back in your Simulink® model. The block converts the input data into a message signal that you can give
as input to the TCP Read, UDP Read, Stream Read, or Register Read blocks, depending on the device type you choose. The playback of
hardware IO data in your Simulink model helps you develop models with better accuracy than models developed by
using randomly generated data during simulation.

When you develop models that use real hardware IO data during deployment, you can choose
to use randomly generated synthetic data as hardware IO data in simulation. As physical
hardware data accounts for various effects like data loss, time delay, and so on. If you use
synthetic data as hardware IO data in simulation for such models, it leads to unexpected
results when you deploy it in the hardware board. To evaluate and verify such models, using
real hardware IO data during simulation is recommended. For more information on how to record
hardware IO data and save it to your host computer, see the `DataRecorder` object.

**Note**

If you have a IO Data Source block with **Input** set to
`From file`, associated with a
`Timer-driven`
Task Manager block in
your model and you plan to use a fixed-step solver, then enter a step size value less than
the value set for the **Period** parameter in the Task Manager block.
For example, suppose the value of **Period** specified in the Task Manager block is
`0.1`, then choose a fixed-step size less than
`0.1`.
