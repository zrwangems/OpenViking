---
type: simulink-block
title: 'AXI4 Video Frame Buffer'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'axi4videoframebuffer'
documentation_source_path: 'ref/axi4videoframebuffer.html'
language: en
---

# AXI4 Video Frame Buffer

## Ports

### Input

### **wrData** — Writer data bus signal scalar | vector | matrix

This signal contains the data to the memory.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **wrCtrlIn** — Writer input control signal bus

This port represents the protocol from the data producer to the memory channel.
The AXI4 Video Frame Buffer block checks this signal when using
**wrData**. To create this control bus, use the SoC Bus Creator block. For more information about bus types, see External Memory Channel Protocols.

**Data Types:** `pixelcontrol`

### **rdCtrlIn** — Reader input control signal bus

This port accepts a bus from a data consumer block, signaling that the consumer
block is ready to accept read data. The **rdCtrlIn** port is a
backpressure signal from a data consumer to the memory. To create this control bus,
use the SoC Bus Creator block.

**Data Types:** `StreamVideoFSyncS2MBusObj`
### Output

### **rdData** — Output data signal to data consumer scalar | vector | matrix

This signal contains the data read from the memory.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `SoCData`

### **rdCtrlOut** — Reader control signal from memory channel to data consumer bus

This bus represents the protocol bust from the memory channel to the data
consumer. To separate the signal from the bus, use the SoC Bus Selector block.

**Data Types:** `pixelcontrol`

### **wrCtrlOut** — Writer control signal from memory channel to data producer bus

This bus represents the protocol bus from the memory channel to the data producer.
To separate the signal from the bus, use the SoC Bus Selector block.

**Data Types:** `StreamVideoS2MBusObj`

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

The size of the region in bytes. This value is calculated as the number of frames
multiplied by the frame size multiplied by the size of the data. Define this value by
setting the **Frame size** and **Number of Frames**
parameters on the **Main** tab, and the **Data
type** and **Dimensions** parameters on the
**Signal Attributes** tab.

**Example:** A software frame size of 1024 uint32 defines a buffer of 4096 bytes. If
the number of buffers is set to 2, the region size is 8192 bytes.

### **Frame size** — Frame dimensions `1080p HDTV (1920x1080p)` (default)

Select or enter the frame size in a combo box.

Select a frame format from the list or enter frame dimension as a 2 element vector
such as `[1920 1080]`.

- `480p SDTV (720x480p)`
- `576p SDTV (720x576p)`
- `720p HDTV (1280x720p)`
- `1080p HDTV (1920x1080p)`
- `160x120p`
- `320x240p`
- `640x480p`
- `800x600p`
- `1024x768p`
- `1280x768p`
- `1280x1024p`
- `1360x768p`
- `1400x1050p`
- `1600x1200p`
- `1680x1050p`
- `1920x1200p`

### **Number of Frames** — Number of buffers in region 3 (default) | integer

Define the number of video frames in the memory.

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

The **Number of Frames** parameter must be an integer from 3 to
64.

### **Burst length** — Burst length for memory transactions 256 (default) | scalar

The length of bursts for this connection on the memory bus in units of scalar
data. The scalar unit is the packed data type. Specify the burst size for both writer
and reader access to the channel.

The channel data is always transferred to the memory model using burst
transactions. For the AXI4 configuration, the algorithm logic is responsible for
defining the burst through the protocol signals.

The **Burst length** parameter determines the burst size to the
memory, and the **rdData** signal defines the size of each transfer
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

#### Data signal

### **Dimensions** — Dimensions of video data `[1 3]` (default) | scalar | vector

Specify the dimension for the video data as a whole scalar or vector.

**Example:** `[1 3]` — A pixel represented by three values (for red,
green, and blue).

**Example:** `[1080 1920 3]` — A 1080p frame. The frame includes 1080
lines of 1920 pixels per line, and each pixel is represented by three values (for red,
green, and blue).

### **Data type** — Data type of video pixel uint8 (default) | uint16 | uint32 | uint64 | `fixdt(1,16,0)`

Specify the data type of the video pixel. For help, click the
**...** button and select **Data Type Assistant**.
By default, this value is set to inherit the data type from the source signal.

### **Sample time** — Time interval of sampling 1 (default) | positive scalar | vector

Specify a time interval in seconds to define how often the block updates.

When you do not want the output to have a time offset, specify the
**Sample time** parameter as a scalar. To add a time offset to the
output, specify the **Sample time** parameter as a
`1`-by-`2` vector, where the first element is the
sampling period and the second element is the offset. For more information about
sample times in Simulink®, see Specify Sample Time.

### **Enable sample packing (last signal dimension as channel)** — Pack data on last dimension of signal `on` (default) | `off`

Select this parameter to enable data packing across the last dimension of the
signal. For example, if the channel data type is `uint32`, the
dimensions are `[1024 4]`. If you select this sample packing
parameter, then the memory channel generates 1024 read or write transactions of 128
bits. If you clear this sample packing parameter, the memory channel generates 4096
transactions of 32 bits each.

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

### **Inherit sample time offset** — Make reader inherit sample time from writer `on` (default) | `off`

Select this box to make the reader inherit the sample time offset from the writer.
Clear the box to use a different sample time offset from the writer. For more
information about sample time offsets, see Sample Time Offset.

### **Use pixel clock sample times** — Use pixel clock sample time off (default) | on

Select this box to use the pixel clock sample time. To use the pixel clock sample
time, you must use scalar pixel dimensions. The pixel clock sample time is relevant
only when streaming pixels. If both the reader and the writer are streaming frames,
you get an error when checking this box.

### Performance

#### Local Masters

### **View performance plots** — Display performance metrics button

Clicking the button opens performance plots for the local manager in a new
window. For more information about performance graphs, see Memory Channel Latency Plots.

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

## Description

Model connection between two hardware algorithms through external memory

The AXI Video Frame Buffer block models a connection between two hardware
algorithms through external memory, using full video frame buffers. The protocol is the
MathWorks® streaming pixel protocol with back pressure. Also, the reader can ensure that
the frame buffer is synchronized with downstream video timings by asserting an FSYNC protocol
signal. The datapath includes a Video-DMA (VDMA) engine and the external memory buffers are
managed as a circular buffer of full video frames.

This block is equivalent to a Memory Channel block with the
**Channel type** parameter set to `AXI4 Video Frame
Buffer` connected to a Memory Controller block.

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

Memory Channel block connected to a Memory Controller block, replaced by an AXI4 Video Frame Buffer block

For more information, see AXI4-Stream Video Interface.
