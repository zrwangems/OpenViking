---
type: simulink-block
title: 'AXI4-Stream to Software'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Memory Model'
documentation_page: 'axi4streamtosoftware'
documentation_source_path: 'ref/axi4streamtosoftware.html'
language: en
---

# AXI4-Stream to Software

## Ports

### Input

### **wrData** — Writer data bus signal scalar | vector | matrix

This signal contains the data to the memory.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **wrCtrlIn** — Writer input control signal bus

This port represents the protocol from the data producer to the processor. The
AXI4-Stream to Software block checks this signal when using
**wrData**. The signals on the control bus are of type
`StreamM2SBusObj`. To create this control bus, use the SoC Bus Creator block. For more information about bus types, see External Memory Channel Protocols.

**Data Types:** `StreamM2SBusObj`

### **done** — Notification message of completed read scalar

This message port receives a notification from the connected Stream Read
block. The notification indicates that a read transaction completed. For more
information on messages, see Messages.

**Data Types:** `Boolean`
### Output

### **event** — Task read event signal scalar

This port sends a task event signal that triggers the Task Manager
block to execute the associated event-driven read.

**Data Types:** `rteEvent`

### **msg** — Output data signal to software scalar | vector | matrix

This signal contains the data read from the memory, sent as a message to the
connected Stream Read
block. For more information on messages, see Messages.

**Data Types:** `SoCData`

### **wrCtrlOut** — Writer control signal to data producer bus

This bus represents the protocol bus from the memory channel to the data producer.
The signals on the bus are of type `StreamS2MBusObj`. To separate the
signal from the bus, use the SoC Bus Selector block.

**Data Types:** `StreamS2MBusObj`

## Parameters

### **Memory simulation** — Set simulation timing accuracy `Burst accurate` (default) | `Protocol accurate` | `Behavioral`

Memory simulation provides three levels of timing resolution. Select one of these
options:

- **Burst accurate** — Simulates memory contention and
  high-resolution timing.
- **Protocol accurate** — Simulates AXI4 protocol hand-shaking
  sequencing and low-resolution timing.
- **Behavioral** — Simulates data transactions only and no
  timing.

  When this parameter is set to **Behavioral** mode, the value of
  the `TLAST` signal is ignored.

### Main

### **Memory selection** — Choose between memory regions `PS memory` (default) | `PL memory`

Select between processing subsystem (PS) or programming logic (PL) memory.

- If the selected board supports only PL memory, then the default value is
  `PL memory`.
- If the selected board supports only PS memory or only PL memory, then this
  parameter is read-only.
- If the selected board is not a supported SoC board, then this parameter is not
  visible.

### **Region size (bytes)** — Size of the allocated memory region, in bytes Read-only: calculated

This parameter is read-only.

The of the region size in bytes. This value is calculated as the number of buffers
multiplied by the size of the buffer. The size of the buffer is defined as the size of
the data multiplied by the software frame size. Define this value by setting the
**Data type** and **Dimensions** parameters on the
**Signal Attributes** tab.

**Example:** A software frame size of 1024 uint32 defines a buffer of 4096 Bytes. If
the number of buffers is set to 2, the region size is 8192 bytes.

### **Number of buffers** — Number of buffers in region `8` (default) | integer

Define the number of buffers in the memory.

The memory access has a ring-buffer pattern. The writer can continually write as
long as buffers are available. When a buffer is completed, it becomes available for
the reader. The writer and reader traverse the buffers in a circular pattern. As long
as the writer and reader maintain similar rates, the buffering prevents
blockage.

A disparate rate between a reader and a writer slows down the faster device. For
example, a slow reader causes the writer to run out of buffers and blocks the writer,
effectively slowing down the writer to the reader rate. Likewise, a slow writer causes
the reader to run out of buffers and blocks the reader, effectively slowing down the
reader to the writer rate.

The **Number of buffers** parameter must be an integer from 3 to
64.

### **Burst length** — Burst length for memory transactions `256` (default) | scalar

The length of bursts for this connection on the memory bus in units of scalar
data. The scalar unit is the packed data type. Specify the burst size for both writer
and reader access to the channel.

The channel data is always transferred to the memory model using burst
transactions. For the AXI4 configuration, the algorithm logic is responsible for
defining the burst through the protocol signals.

The **Burst length** parameter determines the burst size to the
memory, and the **wrData** signal defines the size of each transfer
on the interface.

### **FIFO depth (number of bursts)** — Depth of FIFO for data `8` (default) | scalar

Specify the depth of the data FIFO, in units of bursts. When the writer has no
buffers to write to, the FIFO can absorb data until a buffer becomes available. This
value is the maximum number of bursts that the FIFO can buffer before it drops
data.

#### Dependencies

To enable this parameter, select **Burst accurate** under
**Memory simulation**.

### **FIFO almost-full depth (number of bursts)** — Depth of FIFO when backpressure is asserted `6` (default) | scalar

Specify a number that asserts a backpressure signal from the channel to the data
source. To avoid dropping data, set a high watermark, allowing the data producer
enough time to react to backpressure. This number must be smaller than the FIFO
depth.

#### Dependencies

To enable this parameter, select **Burst accurate** under
**Memory simulation**.

### **Clock frequency (MHz)** — Interconnect frequency of manager datapath `100` (default)

Specify the frequency of the manager datapath in MHz.

#### Dependencies

To enable this parameter, select **Burst accurate** under
**Memory simulation**.

### **Data width (bits)** — Data width of manager datapath `64` (default) | scalar

Specify the data width of the manager datapath to the interconnect controller in
bits.

#### Dependencies

To enable this parameter, select **Burst accurate** under
**Memory simulation**.

### Signal Attributes

#### Stream data signal

### **Dimensions** — Dimensions of input data signal 1 (default) | scalar | array

**wrData** can be a multidimensional array. Specify the dimension
for the array as a whole number.

**Example:** 1 — A scalar sample.

**Example:** [10 1] — A vector of ten scalars.

**Example:** [1080 1920 3] — A 1080p frame. The frame includes 1080 lines of 1920
pixels per line, and each pixel is represented by three values (for red, green, and
blue).

### **Data type** — Data type of writer data `uint32` (default) | `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint64` | `Boolean` | `fixed point`

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
signal. The AXI4-Stream to Software block packs the data along the last
dimension of the signal. For example, if the channel data type is
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

#### Software data signal

### **Dimensions** — Dimensions of software data scalar

Specify the dimension for the software data (reader) as a whole number.

The default value is `1024`.

### **Data type** — Data type of software data `Inherit: Same as input` (default) | `uint16` | `uint32` | `uint64` | `fixdt(0,128,0)`

Specify the data type of the software data (reader). For help, click the
**...** button and select **Data Type Assistant**.
By default, this value is set to inherit the data type from the source signal.

### Performance

#### Local master

### **View performance plots** — Display performance metrics button

Clicking the button opens performance plots for the local master in a new window.
For more information about performance graphs, see Memory Channel Latency Plots.

#### Dependencies

To enable this parameter, select **Burst accurate** under
**Memory simulation**.

#### Memory Controller

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

### R2023b: Support for multiple AXI streams

Use multiple AXI4-Stream to Software, Software to
AXI4-Stream, or Memory Channel blocks
to model, simulate, and deploy designs with multiple streams to and from software. In
previous releases, SoC Blockset™ supported multiple streams for modeling only. This release adds the ability to
generate binaries and software and deploy it on SoC devices.

## Description

Stream AXI4 data from FPGA to software

The AXI4-Stream to Software block models a connection between hardware
logic and a software task through external memory. The writer puts data into the channel using
a MathWorks® simplified AXI stream protocol and the reader (processor) gets data from a DMA
driver interface. The block models the datapath and software stack of that connection,
including a FIFO, DMA engine, interconnect and external memory, interrupts, kernel buffer
management of the DMA driver, and data transfers to the software task.

This block is equivalent to a Memory Channel block with the
**Channel type** parameter set to `AXI4-Stream to Software via
DMA` connected to a Memory Controller block.

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

Memory Channel block connected to a Memory Controller block, replaced by an AXI4-Stream to Software block

For more information about the MathWorks simplified AXI stream protocol, see AXI4-Stream Interface.
