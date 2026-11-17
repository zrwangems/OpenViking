---
type: simulink-block
title: 'AXI4 Random Access Memory'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'axi4randomaccessmemory'
documentation_source_path: 'ref/axi4randomaccessmemory.html'
language: en
---

# AXI4 Random Access Memory

## Ports
```yaml
ports:
- name: wrData
  summary: Writer data bus signal scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: rdCtrlIn
  summary: Reader input control signal bus
  direction: input
  data_types: ReadControlM2SBusObj
- name: wrCtrlIn
  summary: Writer input control signal bus
  direction: input
  data_types: WriteControlM2SBusObj
- name: rdData
  summary: Output data signal to data consumer scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: rdCtrlOut
  summary: Reader control signal from memory channel to data consumer bus
  direction: output
  data_types: ReadControlS2MBusObj
- name: wrCtrlOut
  summary: Writer control signal from memory channel to data producer bus
  direction: output
  data_types: WriteControlS2MBusObj
```

### Input

### **wrData** — Writer data bus signal scalar | vector | matrix

This signal contains the data to the memory.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **rdCtrlIn** — Reader input control signal bus

This port accepts a control bus from a data consumer block, signaling that the
consumer block is ready to accept read data. This input is a read-request from the
reader. To create the control bust, use the SoC Bus Creator block.

**Data Types:** `ReadControlM2SBusObj`

### **wrCtrlIn** — Writer input control signal bus

This port accepts a control bus from a data producer block, signaling that the
producer block is ready to send data. This input is a write-request from the writer.
To create the control bus, use the SoC Bus Creator block.

**Data Types:** `WriteControlM2SBusObj`
### Output

### **rdData** — Output data signal to data consumer scalar | vector | matrix

This signal contains the data read from the memory.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **rdCtrlOut** — Reader control signal from memory channel to data consumer bus

This bus represents the protocol bus from the memory channel to the data consumer.
To separate the signal from the bus, use the SoC Bus Selector block.

**Data Types:** `ReadControlS2MBusObj`

### **wrCtrlOut** — Writer control signal from memory channel to data producer bus

This bus represents the protocol bus from the memory channel to the data producer.
To separate the signal from the bus, use the SoC Bus Selector block.

**Data Types:** `WriteControlS2MBusObj`
## Parameters
```yaml
parameters:
- name: Memory simulation
  summary: Set simulation timing accuracy Burst accurate (default) | Protocol accurate
  group: ''
- name: Memory selection
  summary: Choose between memory regions PS memory (default) | PL memory
  group: Main
- name: Region size (bytes)
  summary: Size of buffer, in bytes 4096 (default) | scalar
  group: Main
- name: Initialize memory content
  summary: Initialize memory for simulation off (default) | on
  group: Main
- name: Initial value
  summary: Initial memory value 0 (default) | scalar | vector
  group: Main
- name: Log memory content
  summary: Log memory contents off (default) | on
  group: Main
- name: Log variable name
  summary: Variable name for memory log string | character vector
  group: Main
- name: Dimensions
  summary: Dimensions of input data signal scalar | array
  group: Signal Attributes
- name: Data type
  summary: Data type of writer data uint32 (default) | double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint64
    | boolean | fixed point
  group: Signal Attributes
- name: Sample time
  summary: Time interval of sampling 1 (default) | positive scalar | vector
  group: Signal Attributes
- name: Enable sample packing (last signal dimension as channel)
  summary: Pack data on the last dimension of the signal off (default) | on
  group: Signal Attributes
- name: Output data signal matches input
  summary: Reader and writer use the same values on (default) | off
  group: Signal Attributes
- name: Dimensions
  summary: Dimensions of output data signal scalar | array
  group: Signal Attributes
- name: Data type
  summary: Data type of reader data uint32 (default) | double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint64
    | boolean | fixed point
  group: Signal Attributes
- name: Sample time
  summary: Time interval of sampling 1 (default) | positive scalar | vector
  group: Signal Attributes
- name: Enable sample packing (last signal dimension as channel)
  summary: Pack data on last dimension of the signal off (default) | on
  group: Signal Attributes
- name: View performance plots
  summary: Display performance metrics button
  group: Performance
```

### **Memory simulation** — Set simulation timing accuracy `Burst accurate` (default) | `Protocol accurate`

Memory simulation provides two levels of timing resolution. Select one of these
options:

- **Burst accurate** — Simulates memory contention and
  high-resolution timing.
- **Protocol accurate** — Simulates AXI4 protocol hand-shaking
  sequencing and low-resolution timing.

### Main

### **Memory selection** — Choose between memory regions `PS memory` (default) | `PL memory`

Select between processing subsystem (PS) or programming logic (PL) memory.

- If the selected board supports only a PL memory, then the default value is
  `PL memory`.
- If the selected board supports only PS memory or only PL memory, then this
  parameter is read-only.
- If the selected board is not a supported SoC board, then this parameter is not
  visible.

### **Region size (bytes)** — Size of buffer, in bytes 4096 (default) | scalar

Specify the size of the memory buffer in bytes.

### **Initialize memory content** — Initialize memory for simulation `off` (default) | `on`

Select this parameter to enable presimulation memory initialization.

### **Initial value** — Initial memory value 0 (default) | scalar | vector

Specify an initial value for memory simulation, as one of the following:

- Integer scalar value between 0–255 — The block replicates and loads this value
  to all memory locations.
- Vector of `uint8` — The block writes each element of the
  vector into a memory location.

  - If the vector is smaller than the memory region, the vector is padded
    with zeroes to match the size of the memory region.
  - If the vector is larger than the memory region, the vector is truncated
    to match the size of the memory region.

**Example:** `0` — Initializes all memory locations with
zeros.

**Example:** `1:10` — Initializes the first ten memory locations with
values 1–10 and the other locations with zeros.

#### Dependencies

To enable this parameter, select **Initialize
memory**.

### **Log memory content** — Log memory contents `off` (default) | `on`

Select this parameter to enable postsimulation memory logging.

### **Log variable name** — Variable name for memory log string | character vector

Name of variable to hold the data of the memory content, specified as a string or
character vector.

**Example:** `'mem_content'`

#### Dependencies

To enable this parameter, select **Log memory ending
value**.

### Signal Attributes

#### Write data signal

### **Dimensions** — Dimensions of input data signal scalar | array

**wrData** can be a multidimensional array. Specify the dimension for the
array as a whole number.

**Example:** 1 — A scalar sample.

**Example:** [10 1] — A vector of ten scalars.

**Example:** [1080 1920 3] — A 1080p frame. The frame includes 1080 lines of 1920
pixels per line, and each pixel is represented by three values (for red, green, and
blue).

### **Data type** — Data type of writer data uint32 (default) | double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint64 | boolean | fixed point

Specify the data type of the **wrData** port. For help, click the
**...** button and select **Data Type
Assistant**.

### **Sample time** — Time interval of sampling 1 (default) | positive scalar | vector

Specify a time interval in seconds to define how often the block updates.

When you do not want the output to have a time offset, specify the
**Sample time** parameter as a scalar. To add a time offset to
the output, specify the **Sample time** parameter as a
`1`-by-`2` vector, where the first element is the
sampling period and the second element is the offset. For more information about
sample times in Simulink®, see Specify Sample Time.

### **Enable sample packing (last signal dimension as channel)** — Pack data on the last dimension of the signal `off` (default) | `on`

Select this parameter to enable data packing across the last dimension of the
signal. The AXI4-Random Access Memory block packs the data along the
last dimension of the signal. For example, if the channel data type is
`uint32`, the dimensions are `[1024 4]`. If you
select this sample packing parameter, then the memory channel generates 1024 read or
write transactions of 128 bits. If you clear this sample packing parameter, the memory
channel generates 4096 transactions of 32 bits each.

This figure shows how data is aligned for a signal with data type
`fixdt10[4x3]`. When the data is packed, three 10-bit words are
concatenated and extended by 2 bits to a 32-bit word. When the data is not packed,
each 10-bit word is extended to a 16-bit word.

The top row shows packed data aligned in samples of 10, 10, 10, and 2 to make 32 bits. The bottom row shows unpacked data aligned in samples of 10 and 6 to make 16 bits.

This figure shows how data is aligned for a signal with data type
`uint8[8x3]`. When the data is packed, three 8-bit words are
concatenated and extended by 8 bits to a 32-bit word. When the data is not packed,
each 8-bit word is represented as an 8-bit sample.

The top row shows packed data aligned in samples of 8, 8, 8, and 8 to make 32 bits. The bottom row shows unpacked data aligned in samples of 8 bits.

The combined width of the flattened signal must not exceed 512 bits.

#### Read data signal

### **Output data signal matches input** — Reader and writer use the same values on (default) | off

Select this box to use the same dimensions and data type for the reader and the
writer of this channel. Clear the box to customize different dimensions and data type
for the reader and writer interfaces.

### **Dimensions** — Dimensions of output data signal scalar | array

**rdData** can be a multidimensional array. Specify the dimension for the
array as a whole number.

**Example:** 1 — A scalar sample.

**Example:** [10 1] — A vector of ten scalars.

**Example:** [1080 1920 3] — A 1080p frame. The frame includes 1080 lines of 1920
pixels per line, and each pixel is represented by three values (for red, green, and
blue).

### **Data type** — Data type of reader data uint32 (default) | double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint64 | boolean | fixed point

Specify the data type of the **rdData** port. For help, click the
**...** button and select **Data Type
Assistant**.

#### Dependencies

To enable this parameter, clear the **Output data signal matches
input** check box.

### **Sample time** — Time interval of sampling 1 (default) | positive scalar | vector

Specify a time interval in seconds to define how often the block updates.

When you do not want the output to have a time offset, specify the
**Sample time** parameter as a scalar. To add a time offset to
the output, specify the **Sample time** parameter as a
`1`-by-`2` vector, where the first element is the
sampling period and the second element is the offset. For more information about
sample times in Simulink, see Specify Sample Time.

#### Dependencies

To enable this parameter, clear the **Output data signal matches
input** check box.

### **Enable sample packing (last signal dimension as channel)** — Pack data on last dimension of the signal `off` (default) | `on`

Select this parameter to enable data packing across the last dimension of the
signal. The AXI4 Random Access Memory block packs the data along the
last dimension of the signal. For example, if the channel data type is
`uint32`, the dimensions are `[1024 4]`. If you
select this sample packing parameter, then the memory channel generates 1024 read or
write transactions of 128 bits. If you clear this sample packing parameter, the memory
channel generates 4096 transactions of 32 bits each.

This figure shows how data is aligned for a signal with data type
`fixdt10[4x3]`. When the data is packed, three 10-bit words are
concatenated and extended by 2 bits to a 32-bit word. When the data is not packed,
each 10-bit word is extended to a 16-bit word.

The top row shows packed data aligned in samples of 10, 10, 10, and 2 to make 32 bits. The bottom row shows unpacked data aligned in samples of 10 and 6 to make 16 bits.

This figure shows how data is aligned for a signal with data type
`uint8[8x3]`. When the data is packed, three 8-bit words are
concatenated and extended by 8 bits to a 32-bit word. When the data is not packed,
each 8-bit word is represented as an 8-bit sample.

The top row shows packed data aligned in samples of 8, 8, 8, and 8 to make 32 bits. The bottom row shows unpacked data aligned in samples of 8 bits.

The combined width of the flattened signal must not exceed 512 bits.

#### Dependencies

To enable this parameter, clear the **Output data signal matches
input** check box.

### Performance

### **View performance plots** — Display performance metrics button

Clicking the button opens the **Performance Plots for Memory
Controller** window. You can then select to plot bandwidth, bursts, or
latencies. For more information about performance graphs, see Memory Controller Latency Plots.

#### Dependencies

To enable this parameter, select **Burst accurate** under
**Memory simulation**.
## Libraries

SoC Blockset / Memory

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2022b**

### R2023a: Support added for memory initialization and logging

You can now load an initial value before simulation or log memory content after simulation.

- To initialize the memory, open the block mask and select **Initialize
  memory** in the main tab. Then, specify the initial value in the
  **Initial value** box.
- To log the contents of the memory after simulation, open the block mask and select
  **Log memory ending value** in the main tab. Then, specify the
  initial value in the **Initial value** box.

### R2023a: **Buffer size** and **Region size** parameters merged

In previous releases, you can specify the size of the memory region in the
**Buffer size** box, and that was reflected as a read-only
**Region size** parameter. In R2023a, specify that size in the
**Region size (bytes)** parameter.

## Description

Model random access through external memory

The AXI4 Random Access Memory block models a connection between two
hardware algorithms through external memory, using the MathWorks® simplified AXI4 manager protocol. Both the writer and the reader are managers,
sending read and write requests to memory through the block. The external memory is unmanaged
(no logical buffers, no circular buffer). To ensure the integrity of the data, the reader and
writer coordinate timing on accesses.

This block is equivalent to a Memory Channel block with the
**Channel type** parameter set to `AXI4 Random
Access` connected to a Memory Controller block.

Since the memory controller is implicit to the design - you can instantiate several memory
blocks that connect to the same memory unit via a memory controller. Valid blocks are:

- AXI4 Random Access
  Memory
- AXI4-Stream to
  Software
- Software to
  AXI4-Stream
- AXI4 Video Frame
  Buffer
- Memory Traffic
  Generator

The maximum number of manager interfaces in a model is 16.

Memory Channel block connected to a Memory Controller block, replaced by an AXI4 Random Access Memory block

For more information, see Simplified AXI4 Master Interface.
