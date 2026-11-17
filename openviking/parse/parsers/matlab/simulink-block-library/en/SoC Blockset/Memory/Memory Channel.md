---
type: simulink-block
title: 'Memory Channel'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'memorychannel'
documentation_source_path: 'ref/memorychannel.html'
language: en
---

# Memory Channel

## Ports
```yaml
ports:
- name: wrData
  summary: Writer data bus signal scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    SoCData
- name: wrCtrlIn
  summary: Writer input control signal bus
  direction: input
  data_types: StreamM2SBusObj | pixelcontrol | WritecontrolM2SBusObj
- name: rdCtrlIn
  summary: Reader input control signal bus
  direction: input
  data_types: StreamS2MBusObj | StreamVideoS2MBusObj | StreamVideoFSyncS2MBusObj | ReadControlM2SBusObj
- name: rdDone
  summary: Notification message of completed read scalar
  direction: input
  data_types: Boolean
- name: wrBurstDone
  summary: Writer control input from memory controller scalar
  direction: input
  data_types: BurstRequest2BusObj
- name: rdBurstDone
  summary: Reader control input from memory controller scalar
  direction: input
  data_types: BurstRequest2BusObj
- name: rdData
  summary: Output data signal to data consumer scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    SoCData
- name: rdEvent
  summary: Task read event signal scalar
  direction: output
  data_types: rteEvent
- name: wrEvent
  summary: Task write event signal scalar
  direction: output
  data_types: rteEvent
- name: wrDone
  summary: Notification of freed buffer in memory scalar
  direction: output
  data_types: Boolean
- name: rdCtrlOut
  summary: Reader control signal from memory channel to data consumer bus
  direction: output
  data_types: StreamM2SBusObj | ReadControlS2MBusObj | pixelcontrol
- name: wrCtrlOut
  summary: Writer control signal from memory channel to data producer bus
  direction: output
  data_types: StreamS2MBusObj | WriteControlS2MBusObj | StreamVideoS2MBusObj
- name: wrBurstReq
  summary: Write burst request scalar
  direction: output
  data_types: BurstRequestBusObj
- name: rdBurstReq
  summary: Read burst request scalar
  direction: output
  data_types: BurstRequestBusObj
```

### Input

### **wrData** — Writer data bus signal scalar | vector | matrix

This signal contains the data to the memory.

**Note**

When the **Channel type** parameter is set to
`Software to AXI4-Stream via DMA`, this
port receives the input data, as a message, from the connected
Stream Write block. For more information on messages,
see Messages.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `SoCData`

### **wrCtrlIn** — Writer input control signal bus

This port represents the protocol from the data producer to the memory
channel. The Memory
Channel block checks this signal when using
**wrData**. The signals on the bus depend on the **Channel
type** parameter. Use the SoC Bus Creator block to
create this control bus. For more information about bus types, see External Memory Channel Protocols.

| Channel Type Configuration | Bus Type |
| --- | --- |
| `AXI4-Stream to Software via DMA` | `StreamM2SBusObj` |
| `AXI4 Stream FIFO` | `StreamM2SBusObj` |
| `AXI4 Stream Video FIFO` | `pixelcontrol` |
| `AXI4 Stream Video Frame Buffer` | `pixelcontrol` |
| `AXI4 Random Access` | `WriteControlM2SBusObj` |

#### Dependencies

To enable this port, set the **Channel type**
parameter to a value other than `Software to AXI4-Stream
via DMA`.

**Data Types:** `StreamM2SBusObj` | `pixelcontrol` | `WritecontrolM2SBusObj`

### **rdCtrlIn** — Reader input control signal bus

This port accepts a bus from a data consumer block, signaling that the
consumer block is ready to accept read data. For streaming protocols,
the **rdCtrlIn** port is a backpressure signal from a data
consumer to the Memory Channel block. For the
`AXI4 Random Access` protocol, this input is a
read-request from the reader. The signals on the bus depend on the
**Channel
type** parameter. Use the SoC Bus Creator block to
create this control bus.

| Channel Type Configuration | Bus Type |
| --- | --- |
| `Software to AXI4-Stream via DMA` | `StreamS2MBusObj` |
| `AXI4 Stream FIFO` | `StreamS2MBusObj` |
| `AXI4 Stream Video FIFO` | `StreamVideoS2MBusObj` |
| `AXI4 Stream Video Frame Buffer` | `StreamVideoFSyncS2MBusObj` |
| `AXI4 Random Access` | `ReadControlM2SBusObj` |

#### Dependencies

To enable this port, set the **Channel type**
parameter to a value other than `AXI4-Stream to Software
via DMA`.

**Data Types:** `StreamS2MBusObj` | `StreamVideoS2MBusObj` | `StreamVideoFSyncS2MBusObj` | `ReadControlM2SBusObj`

### **rdDone** — Notification message of completed read scalar

This message port receives a notification from the connected Stream
Read block. The notification indicates that a read
transaction completed. For more information on messages, see Messages.

#### Dependencies

To enable this port, set the **Channel type**
parameter to `AXI4-Stream to Software via
DMA`.

**Data Types:** `Boolean`

### **wrBurstDone** — Writer control input from memory controller scalar

This message port receives control messages from a connected Memory
Controller block that the requested burst transaction
completed. Connect the **burstDone** output signal from the
Memory Controller block to this port. For more
information on messages, see Messages.

**Data Types:** `BurstRequest2BusObj`

### **rdBurstDone** — Reader control input from memory controller scalar

This message port receives control messages from a connected Memory
Controller block that the requested burst transaction
completed. Connect the **burstDone**  output signal from the
Memory Controller block to this port. For more
information on messages, see Messages.

**Data Types:** `BurstRequest2BusObj`
### Output

### **rdData** — Output data signal to data consumer scalar | vector | matrix

This signal contains the data read from the memory.

**Note**

When the **Channel type** parameter is set to
`AXI4-Stream to Software via DMA`, this
port sends the output data, as a message, to the connected Stream Read block. For more information on messages,
see Messages.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `SoCData`

### **rdEvent** — Task read event signal scalar

This port sends a task event signal that triggers the Task
Manager block to execute the associated event-driven
read.

#### Dependencies

To enable this port, set the **Channel type**
parameter to `AXI4-Stream to Software via
DMA`.

**Data Types:** `rteEvent`

### **wrEvent** — Task write event signal scalar

This port sends a task event signal that triggers the Task
Manager block to execute the associated event-driven
write.

#### Dependencies

To enable this port, set the **Channel type**
parameter to `Software to AXI4-Stream via
DMA`.

**Data Types:** `rteEvent`

### **wrDone** — Notification of freed buffer in memory scalar

This message port sends a notification to the connected Stream
Write block. This notification indicates that a read
transaction completed, and that a buffer in memory is available for
writing.

#### Dependencies

To enable this port, set the **Channel type**
parameter to `Software to AXI4-Stream via
DMA`.

**Data Types:** `Boolean`

### **rdCtrlOut** — Reader control signal from memory channel to data consumer bus

Control signal from channel to data consumer. The contents of this
signal depend on the `Channel
type` parameter. Connect this signal to the data consumer.
Use the SoC Bus Selector block to
separate the signal from the bus.

| Channel Type Configuration | Bus Type |
| --- | --- |
| `Software to AXI4-Stream via DMA` | `StreamM2SBusObj` |
| `AXI4 Stream FIFO` | `StreamM2SBusObj` |
| `AXI4 Stream Video FIFO` | `pixelcontrol` |
| `AXI4 Stream Video Frame Buffer` | `pixelcontrol` |
| `AXI4 Random Access` | `ReadControlS2MBusObj` |

#### Dependencies

To enable this port, set the **Channel type**
parameter to a value other than `AXI4-Stream to Software
via DMA`.

**Data Types:** `StreamM2SBusObj` | `ReadControlS2MBusObj` | `pixelcontrol`

### **wrCtrlOut** — Writer control signal from memory channel to data producer bus

This bus represents the protocol bus from the memory channel to the
data producer. The signals on the bus depend on the **Channel
type** parameter. Use the SoC Bus Selector block to
separate the signal from the bus.

| Channel Type Configuration | Bus Type |
| --- | --- |
| `AXI4-Stream to Software via DMA` | `StreamS2MBusObj` |
| `AXI4 Stream FIFO` | `StreamS2MBusObj` |
| `AXI4 Stream Video FIFO` | `StreamVideoS2MBusObj` |
| `AXI4 Stream Video Frame Buffer` | `StreamVideoS2MBusObj` |
| `AXI4 Random Access` | `WriteControlS2MBusObj` |

#### Dependencies

To enable this port, set the **Channel type**
parameter to a value other than `Software to AXI4-Stream
via DMA`.

**Data Types:** `StreamS2MBusObj` | `WriteControlS2MBusObj` | `StreamVideoS2MBusObj`

### **wrBurstReq** — Write burst request scalar

This message port sends control signal requesting burst access from
the memory controller. Connect it to the **burstReq** input of
the Memory
Controller block. For more information on messages, see
Messages.

**Data Types:** `BurstRequestBusObj`

### **rdBurstReq** — Read burst request scalar

This message port sends control signal requesting burst access from
the memory controller. Connect it to the **burstReq** input of
the Memory
Controller block. For more information on messages, see
Messages.

**Data Types:** `BurstRequestBusObj`
## Parameters
```yaml
parameters:
- name: Hardware board
  summary: 'View or modify current hardware settings Read-only: name of selected hardware board'
  group: ''
- name: Show implementation info
  summary: 'View channel information Read-only: text window'
  group: ''
- name: Enable memory simulation
  summary: Control memory simulation accuracy on (default) | off
  group: ''
- name: Channel type
  summary: Choose channel protocol AXI4-Stream FIFO (default) | AXI4-Stream to Software via DMA | Software to AXI4-Stream
    via DMA | AXI4-Stream Video FIFO | AXI4-Stream Video Frame Buffer | AXI4 Random Access
  group: Main
- name: Region size (bytes)
  summary: 'Size of memory allocated for region, in bytes Read-only: calculated'
  group: Main
- name: Buffer size (bytes)
  summary: Size of buffer, in bytes 1024 (default) | scalar
  group: Main
- name: Number of buffers
  summary: Number of buffers in region 8 (default) | integer
  group: Main
- name: Burst length
  summary: Burst length for memory transactions 1 (default) | scalar
  group: Main
- name: Use hardware board settings
  summary: Use the Hardware Implementation settings from the configuration parameters on (default) | off
  group: Main
- name: Reader/Writer use same values
  summary: Reader and writer use the same values on (default) | off
  group: Main
- name: FIFO depth (number of bursts)
  summary: Depth of FIFO for data 12 (default) | scalar
  group: Main
- name: Almost full depth
  summary: Depth of FIFO when backpressure is asserted 8 (default) | scalar
  group: Main
- name: Clock frequency (MHz)
  summary: Interconnect frequency of master datapath 100 (default)
  group: Main
- name: Data width (bits)
  summary: Data width of master datapath 64 (default) | scalar
  group: Main
- name: Dimensions
  summary: Dimensions of input data signal scalar | array
  group: Signal Attributes
- name: Data type
  summary: Data type of writer data double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean
    | fixed point
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
  summary: Data type of reader data double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean
    | fixed point
  group: Signal Attributes
- name: Sample time
  summary: Time interval of sampling 1 (default) | positive scalar | vector
  group: Signal Attributes
- name: Enable sample packing (last signal dimension as channel)
  summary: Pack data on the last dimension of the signal off (default) | on
  group: Signal Attributes
- name: Inherit sample time offset
  summary: Make reader inherit sample time from writer on (default) | off
  group: Signal Attributes
- name: Use pixel clock sample times
  summary: Use the pixel clock sample time on (default) | off
  group: Signal Attributes
- name: Frame size
  summary: Frame dimensions 480p SDTV (720x480p) (default) | ...
  group: Signal Attributes
- name: Launch performance plots
  summary: Display performance metrics button
  group: Performance
```

### **Hardware board** — View or modify current hardware settings Read-only: name of selected hardware board

This parameter is read-only.

This parameter shows a link to the currently selected hardware board.
Click the link to open the configuration parameters, and adjust the
settings, or choose a different board.

To learn more about configuration parameters, see FPGA design (mem channels).

### **Show implementation info** — View channel information Read-only: text window

This parameter is read-only.

This parameter shows a link to the implementation information specific to
the model. Click the link to view the information (opens in new
window).

### **Enable memory simulation** — Control memory simulation accuracy `on` (default) | `off`

Select this parameter to enable memory simulation with high accuracy.
Clear for faster simulation performance.

- `on` — The block simulates memory transactions
  with burst accuracy. Bursts are constructed and arbitrated for
  access to memory.
- `off` — Memory transactions are purely
  behavioral, allowing fast simulation.

To see an example that uses this feature go to Accelerate SoC Simulation by Varying Abstraction Levels.

### Main

### **Channel type** — Choose channel protocol `AXI4-Stream FIFO` (default) | `AXI4-Stream to Software via DMA` | `Software to AXI4-Stream via DMA` | `AXI4-Stream Video FIFO` | `AXI4-Stream Video Frame Buffer` | `AXI4 Random Access`

Specify the protocol for the channel. Choose one of the following values:

- AXI4-Stream to Software via DMA
- Software to AXI4-Stream via DMA
- AXI4 Stream FIFO
- AXI4 Stream Video FIFO
- AXI4 Stream Video Frame Buffer
- AXI4 Random Access

**Note**

You can use a simplified memory block for the following
configurations (recommended):

- AXI4-Stream to Software via DMA — Use an AXI4-Stream to Software block.
- Software to AXI4-Stream via DMA — Use a Software to AXI4-Stream block.
- AXI4 Stream Video Frame Buffer — Use an AXI4 Video Frame Buffer block.
- AXI4 Random Access — Use an AXI4 Random Access Memory block.

These blocks provide a preconfigured and
simplified view per each channel type.

For additional information about memory channel protocols, see
External Memory Channel Protocols.

### **Region size (bytes)** — Size of memory allocated for region, in bytes Read-only: calculated

This parameter is read-only.

The size in bytes of the region. This value is calculated as the
number of buffers multiplied by buffer size.

**Example:** If Buffer size is 1024, and the number of buffers is set to 8,
then Region size is 8192.

### **Buffer size (bytes)** — Size of buffer, in bytes 1024 (default) | scalar

Specify the size in bytes of each buffer in the region.

The following rules apply when setting burst and buffer sizes.

1. The Burst Length of a given channel interface, calculated in
   bytes, must be less than 4096 bytes. To calculate the burst size
   in bytes, the channel interface scalar datatype is converted to
   bytes and then multiplied by the Burst Length.
2. The Burst Length can be set above 256, but will warn if
   generating to an AXI-based target platform. AXI-based memory
   systems have a maximum burst length of 256.
3. The Channel Length must be an integer multiple of burst length
   or the burst length must be an integer multiple of channel
   length. That is, it must be possible to either chunk the
   incoming channel data to a whole number of bursts or to gather a
   whole number of incoming channel data to a single burst.
4. The Buffer Size must be a whole number of bursts. This must be
   true for both the writer’s burst size (after conversion of its
   Burst Length to bytes) and the reader’s burst size (after
   conversion of its Burst Length to bytes).
5. The calculated number of bursts in a buffer must not exceed
   5000. This is a temporary restriction based on the event
   processing internal to the memory model. This can happen with
   shared memory regions that have large buffer sizes (such as for
   1080p video frames) and channel interfaces that specify smaller
   burst sizes. Generally, with larger frames, bursts sizes near
   the 4096 byte limit must be used.
6. The scalar datatype of the channel interface as converted to a
   flattened channel data width (i.e. *tdata* in
   the implementation) cannot exceed 128 bits.

The following table provides examples of good and bad parameter
sets.

**Burst and Buffer parameter examples**

| Channel Datatype | Channel Dimensions | Burst Length | Burst Size | Good / Bad | Why? |
| --- | --- | --- | --- | --- | --- |
| uint8 | [1 1] | 1024 | 2048 | Good | This is a simple 8-bit data transaction. |
| uint8 | [1 3] | 1024 | 4096 | Good | This might represent an RGB pixel from a Vision HDL Toolbox block. It is converted to 24-bit packed data and padded with 8 bits to become a 32-bit (4-Byte) *tdata* bus to the memory. The Burst size is 1024\*4B = 4096B. |
| fixdt(0,10,0) | [1 3] | 1024 | 4096 | Good | This is converted to a 30-bit packed pixel with 2 bits of padding. |
| fixdt(0,12,0) | [1 3] | 1024 | 8192 | Good | This results in a 36-bit packed pixel which extends to 64-bit *tdata*. This data is compliant with the current limit of 128-bit *tdata*. |
| fixdt(0,48,0) | [1 3] | 1024 | 8192 | Bad | This results in a 144-bit packed pixel violates the current limit of 128-bit *tdata*. |
| uint8 | [120 160 3] | 1024 | 4096 | Bad | The scalar data is 24-bit, padded to a 32-bit *tdata*. The Channel Length is 120\*160=19200. The burst length of 1024 does not evenly divide 19200. |
| uint8 | [120 160 3] | 120 | 480 | Good | The scalar data is 24-bit, padded to a 32-bit *tdata*. The Channel Length is 120\*160, and since the burst length is 120, Channel length is 160 bursts in size. The buffer size is exactly 1 frame (120\*160\*4) as calculated in bytes. |

### **Number of buffers** — Number of buffers in region 8 (default) | integer

Divide the region into buffers. A disparate rate between a reader and
a writer slows down the faster device. For example, a slow reader causes
the writer to run out of buffers and block the writer, effectively
slowing down to the reader rate. Likewise, a slow writer causes the
reader to run out of buffers and block the reader, effectively slowing
it down to the writer rate.

- Specifying `1` – With a single buffer, access
  is controlled to ensure that a buffer is written, then it is
  read, then the next buffer is written, and so on.
- Specifying `2`: With two buffers, memory
  access switches in a back-and-forth pattern. The writer writes
  the first buffer, then, while the reader is reading it, the
  writer can write the second buffer.
- Specifying `N` –
  With *`N`* buffers, the memory access has
  a ring-buffer pattern. The writer can continually write as long
  as buffers are available. When a buffer is completed, it becomes
  available for the reader. The writer and reader traverse the N
  buffers in a circular pattern. As long as the writer and reader
  maintain similar rates, the buffering prevents blockage.

#### Limitations

When you set the **Channel type** parameter to
`AXI4-Stream to Software via DMA` or
`Software to AXI4-Stream via DMA`, the
**Number of buffers** parameter must be an
integer from 3 to 64.

### **Burst length** — Burst length for memory transactions 1 (default) | scalar

The length of bursts for this connection on the memory bus in units of
scalar data. The scalar unit is the packed data type. Specify the burst
size for both **Writer** and
**Reader** access to the channel.

The channel data is always transferred to the memory model using burst
transactions, regardless of the channel-type. For the AXI4
configuration, the algorithm-logic is responsible for defining the burst
through the protocol signals.

For the streaming data configurations, the **Burst
Length** parameter determines the burst size to the memory,
and the channel **data** signal defines the size of
each transfer on the interface.

When setting burst length, you must consider the Buffer size (bytes)
parameter.

#### Dependencies

To enable this parameter, select **Enable memory
simulation**.

- This parameter is not visible when the
  **Channel type** parameter is set
  to `AXI4 Random Access`.
- The writer **Burst length** parameter
  is not visible when the **Channel
  Type** parameter is set to
  `Software to AXI4-Stream via
  DMA`
- The reader **Burst length** parameter
  is not visible when the **Channel
  Type** parameter is set to
  `AXI4-Stream to Software via
  DMA`

### **Use hardware board settings** — Use the Hardware Implementation settings from the configuration parameters on (default) | off

To use the same model-wide setting as in configuration parameters,
select this box. Clear the box to customize the setting for this
channel. When using channel-specific settings, values are still checked
against hardware-specific constraints. For setting these values in the
configuration parameters, see FPGA design (mem channels).

#### Dependencies

To enable this parameter, select **Enable memory
simulation**.

This parameter is not visible when **Channel
type** is set to `AXI4 Random
Access`.

### **Reader/Writer use same values** — Reader and writer use the same values on (default) | off

Select this box to use the same interconnect setting for the reader
and the writer of this channel. Clear the box to customize different
settings for the reader and the writer. Clearing the
**Reader/Writer use same values** allows you to
enter a value for the writer side and a value for the reader side, for
the following parameters:

- **FIFO depth (number of bursts)**
- **Almost-full depth**
- **Clock Frequency (MHz)**
- **Data width (bits)**

#### Dependencies

To enable this parameter, select **Enable memory
simulation**.

This parameter is visible when **Channel type**
is set to `AXI4-Stream FIFO`,
`AXI4-Stream Video FIFO`, or
`AXI4-Stream Video Frame
Buffer`.

### **FIFO depth (number of bursts)** — Depth of FIFO for data `12` (default) | scalar

Specify depth of data FIFO, in units of bursts. When the writer has no
buffers to write to, the FIFO can absorb data until a buffer becomes
available. This value is the maximum number of bursts that can be
buffered before data gets dropped.

#### Dependencies

- To enable this parameter, clear the **Use
  hardware board settings** check box and select
  **Enable memory simulation**.

  .
- When **Reader/Writer use same values**
  is cleared, there are two text boxes: one for
  **Writer** and one for
  **Reader**.
- This parameter is not visible when the **Channel
  type** parameter is set to `AXI4
  Random Access`.
- The writer **FIFO depth** parameter is
  not visible when the **Channel Type**
  parameter is set to `Software to AXI4-Stream via
  DMA`
- The reader **FIFO depth** parameter is
  not visible when the **Channel Type**
  parameter is set to `AXI4-Stream to Software via
  DMA`

### **Almost full depth** — Depth of FIFO when backpressure is asserted `8` (default) | scalar

Specify a number that asserts a backpressure signal from the channel
to the data source. To avoid dropping data, set a high watermark,
allowing the data producer enough time to react to backpressure. This
number must be smaller than the FIFO depth.

#### Dependencies

- To enable this parameter, clear the **Use
  hardware board settings** check box and select
  **Enable memory simulation**.
- When **Reader/Writer use same values**
  is cleared, there are two text boxes: one for
  **Writer** and one for
  **Reader**.
- This parameter is not visible when the **Channel
  type** parameter is set to `AXI4
  Random Access`.
- The writer **Almost full depth**
  parameter is not visible when the **Channel
  Type** parameter is set to
  `Software to AXI4-Stream via
  DMA`
- The reader **Almost full depth**
  parameter is not visible when the **Channel
  Type** parameter is set to
  `AXI4-Stream to Software via
  DMA`

### **Clock frequency (MHz)** — Interconnect frequency of master datapath `100` (default)

Frequency of the master datapath to the interconnect controller in
MHz.

#### Dependencies

- To enable this parameter, clear the **Use
  hardware board settings** check box and select
  **Enable memory simulation**.
- When **Reader/Writer use same values**
  is cleared, there are two text boxes: one for
  **Writer** and one for
  **Reader**.
- This parameter is not visible when the **Channel
  type** parameter is set to `AXI4
  Random Access`.
- The writer **Clock frequency (MHz)**
  parameter is not visible when the **Channel
  Type** parameter is set to
  `Software to AXI4-Stream via
  DMA`
- The reader **Clock frequency (MHz)**
  parameter is not visible when the **Channel
  Type** parameter is set to
  `AXI4-Stream to Software via
  DMA`

### **Data width (bits)** — Data width of master datapath `64` (default) | scalar

Data width of master datapath to interconnect controller in
bits.

#### Dependencies

- To enable this parameter, clear the **Use
  hardware board settings** check box and select
  **Enable memory simulation**.
- When **Reader/Writer use same values**
  is cleared, there are two text boxes: one for
  **Writer** and one for
  **Reader**.
- When the **Channel type** parameter is
  set to `AXI4 Random Access`, the
  **Data width (bits)** parameter is set
  to the bit width corresponding to the **Data
  type** parameter, and the **Enable
  sample packing** parameter.
- The writer **Data width (bits)**
  parameter is not visible when the **Channel
  Type** parameter is set to
  `Software to AXI4-Stream via
  DMA`
- The reader **Data width (bits)**
  parameter is not visible when the **Channel
  Type** parameter is set to
  `AXI4-Stream to Software via
  DMA`

### Signal Attributes

#### Write data signal

### **Dimensions** — Dimensions of input data signal scalar | array

**wrData** can be a multidimensional array. Specify the
dimension for the array as a whole number.

When **Channel type** is set to
`Software to AXI4-Stream via DMA`, the
**Dimensions** parameter must be scalar.

**Example:** 1 – a scalar sample.

**Example:** [10 1] – a vector of ten scalars.

**Example:** [1080 1920 3] – a 1080p frame. The frame includes 1080 lines
of 1920 pixels per line, and each pixel is represented by three values
(for red, green and blue).

### **Data type** — Data type of writer data double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean | fixed point

Specify the data type of the **wrData** port. For help, click
the **...** button. This expands the menu and shows a
**Data Type Assistant**.

When the **Channel
type** parameter is set to `Software to AXI4-Stream
via DMA`, the data type must be set to
`uint16`, `uint32`,
`uint64`, or
`fixdt(0,128,0)`.

### **Sample time** — Time interval of sampling 1 (default) | positive scalar | vector

Specify a time interval in seconds to define how often the block
updates.

Specify the **Sample time** parameter as a scalar
when you do not want the output to have a time offset. To add a time
offset to the output, specify the **Sample time**
parameter as a `1`-by-`2` vector where
the first element is the sampling period and the second element is the
offset. For more information about sample times in Simulink®, see Specify Sample Time.

#### Dependencies

This parameter is not visible when the **Channel
type** parameter is set to `Software to
AXI4-Stream via DMA`.

### **Enable sample packing (last signal dimension as channel)** — Pack data on the last dimension of the signal `off` (default) | `on`

Select this parameter to enable data packing across the last dimension
of the signal. The Memory Channel block packs the data
along the last dimension of the signal. For example, if the channel data
type is `uint32`, the dimensions are `[1024
4]`, and if you select this parameter, then the memory
channel generates 1024 read or write transactions of 128 bits. For this
example, if you clear this sample packing parameter, the memory channel
generates 4096 transactions of 32 bits each.

This figure shows how data is aligned for a signal with data type
`fixdt10[4x3]`. When the data is packed, three
10-bit words are concatenated and extended by 2 bits to a 32-bit word.
When the data is not packed, each 10-bit word is extended to a 16-bit
word.

The top row shows packed data aligned in samples of 10,10,10, and 2 to make 32 bits. The bottom row shows unpacked data aligned in samples of 10 and 6 to make 16 bits.

This figure shows how data is aligned for a signal with data type
`uint8[8x3]`. When the data is packed, three 8-bit
words are concatenated and extended by 8 bits to a 32-bit word. When the
data is not packed, each 8-bit word is represented as an 8-bit sample.

The top row shows packed data aligned in samples of 8,8,8, and 8 to make 32 bits. The bottom row shows unpacked data aligned in samples of 8 bits.

The combined width of the flattened signal must not exceed 512
bits.

#### Dependencies

This parameter is not visible when the **Channel
type** parameter is set to `Software to
AXI4-Stream via DMA`.

#### Read data signal

### **Output data signal matches input** — Reader and writer use the same values on (default) | off

Select this box to use the same dimensions and data type for the
reader and the writer of this channel. Clear the box to customize
different settings for the reader and the writer. Clear the box to
customize different dimensions and data type for the reader and writer
interfaces.

### **Dimensions** — Dimensions of output data signal scalar | array

**rdData** can be a multidimensional array. Specify the
dimension for the array as a whole number.

When **Channel type** is set to
`AXI4-Stream to Software via DMA`, the
**Dimensions** parameter must be scalar.

**Example:** 1 – a scalar sample.

**Example:** [10 1] – a vector of ten scalars.

**Example:** [1080 1920 3] – a 1080p frame. The frame includes 1080 lines
of 1920 pixels per line, and each pixel is represented by three values
(for red, green and blue).

#### Dependencies

To enable this parameter, clear the **Output data signal
matches input** check box.

### **Data type** — Data type of reader data double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean | fixed point

Specify the data type of the **rdData** port. For help, click
the **...** button. This expands the menu and shows a
**Data Type Assistant**.

When the **Channel
type** parameter is set to `AXI4-Stream to
Software via DMA`, the data type must be set to
`uint16`, `uint32`,
`uint64`, or
`fixdt(0,128,0)`.

#### Dependencies

To enable this parameter, clear the **Output data signal
matches input** check box.

### **Sample time** — Time interval of sampling 1 (default) | positive scalar | vector

Specify a time interval in seconds to define how often the block
updates.

Specify the **Sample time** parameter as a scalar
when you do not want the output to have a time offset. To add a time
offset to the output, specify the **Sample time**
parameter as a `1`-by-`2` vector where
the first element is the sampling period and the second element is the
offset. For more information about sample times in Simulink, see Specify Sample Time.

#### Dependencies

To enable this parameter, do one of the following:

- Set **Channel type** to
  `Software to AXI4-stream via
  DMA`.
- Set **Channel type** to
  `AXI4 Random Access` and
  clear the **Output data signal matches
  input** check box.

### **Enable sample packing (last signal dimension as channel)** — Pack data on the last dimension of the signal `off` (default) | `on`

Select this parameter to enable data packing across the last dimension
of the signal. The Memory Channel block packs the data
along the last dimension of the signal. For example, if the channel data
type is `uint32`, the dimensions are `[1024
4]`, and if you select this parameter, then the memory
channel generates 1024 read or write transactions of 128 bits. For this
example, if you clear this sample packing parameter, the memory channel
generates 4096 transactions of 32 bits each.

This figure shows how data is aligned for a signal with data type
`fixdt10[4x3]`. When the data is packed, three
10-bit words are concatenated and extended by 2 bits to a 32-bit word.
When the data is not packed, each 10-bit word is extended to a 16-bit
word.

The top row shows packed data aligned in samples of 10,10,10, and 2 to make 32 bits. The bottom row shows unpacked data aligned in samples of 10 and 6 to make 16 bits.

This figure shows how data is aligned for a signal with data type
`uint8[8x3]`. When the data is packed, three 8-bit
words are concatenated and extended by 8 bits to a 32-bit word. When the
data is not packed, each 8-bit word is represented as an 8-bit sample.

The top row shows packed data aligned in samples of 8,8,8, and 8 to make 32 bits. The bottom row shows unpacked data aligned in samples of 8 bits.

The combined width of the flattened signal must not exceed 512
bits.

#### Dependencies

To enable this parameter, clear **Output data signal
matches input** check box, and set **Channel
type** to a value other than `AXI4-Stream
to Software via DMA`.

### **Inherit sample time offset** — Make reader inherit sample time from writer `on` (default) | `off`

Select this box to make the reader inherit the sample time offset from
the writer. Clear the box to use a different sample time offset from the
writer. For more information about sample time offsets, see Sample Time Offset.

#### Dependencies

To enable this parameter, clear the **Output data signal
matches input** check box and set **Channel
type** to one of the following values:

- `AXI4-Stream FIFO`
- `AXI4-Stream Video
  FIFO`
- `AXI4-Stream Video Frame
  Buffer`

### **Use pixel clock sample times** — Use the pixel clock sample time on (default) | off

Select this box to use the pixel clock sample time. To use the pixel
clock sample time, you must use scalar pixel dimensions. It is only
relevant when streaming pixels. If both the reader and the writer are
streaming frames, you get an error when checking this box.

**Note**

If both reader and writer are using framed signals, the signal
dimensions are not scalar and pixel timing cannot be inferred.
Selecting **Use pixel clock sample times** in
this case creates an error.

#### Dependencies

To enable this parameter, set **Channel type**
to `AXI4-Stream Video FIFO` or
`AXI4-Stream Video Frame
Buffer`.

### **Frame size** — Frame dimensions `480p SDTV (720x480p)` (default) | ...

For video-streaming applications, **Frame size**
can often be inferred, and this parameter shows as a read-only value.
When it cannot be inferred, select the **Frame size**
from a drop-down menu.

- When the reader or the writer are using framed signals of a
  frame with known porch and blanking timings, the
  **Frame size** is inferred from those
  timings. When the reader or the writer is a scalar and the other
  is a non-standard frame size, the **Frame
  size** cannot be inferred and you get an error.
- When **Channel type** is set to
  `AXI4-Stream Video Frame Buffer`
  and both reader and writer are using scalar dimensions for pixel
  streams, **Frame size** is inferred from
  **BufferSize** and TDATA and it is then a
  read-only value.
- When **Channel type** is set to
  `AXI4-Stream Video FIFO` and both
  reader and writer are using scalar dimensions for pixel streams,
  select the **Frame size** as one of these
  values:

  - `160x120p`
  - `480p SDTV (720x480p)`
  - `576p SDTV (720x576p)`
  - `720p HDTV
    (1280x720p)`
  - `1080p HDTV
    (1920x1080p)`
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
  - `16x12p (test mode)`

#### Dependencies

To enable this parameter, set **Channel type**
to `AXI4-Stream Video FIFO` or
`AXI4-Stream Video Frame Buffer`, and
select **Use pixel clock sample times**.

### Performance

### **Launch performance plots** — Display performance metrics button

Clicking the button opens Performance plots for the memory channel in
a new window. For more information about performance graphs, see Simulation Diagnostics.

#### Dependencies

To enable this parameter, select **Enable memory
simulation**.
## Libraries

SoC Blockset / Memory

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design, and execute
on an SoC device, use the **SoC Builder** tool. See Use SoC Builder to Generate SoC Design.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2019a**

### R2023b: Support for multiple AXI streams

Use multiple AXI4-Stream to
Software, Software to
AXI4-Stream, or Memory Channel blocks to model, simulate,
and deploy designs with multiple streams to and from software. In previous releases,
SoC Blockset™ supported multiple streams for modeling only. This release adds the
ability to generate binaries and software and deploy it on SoC devices.

### R2022b: Simplified memory blocks

SoC Blockset adds four blocks that replace a Memory Channel block
connected to a Memory Controller block. These new blocks enhance
simulation performance by streamlining your model with the introduction of a simple
parameter set and fewer connections.

- AXI4-Stream
  to Software — Use this block to replace a Memory
  Channel block with the **Channel type**
  parameter set to `AXI4-Stream to Software via DMA`
  connected to a Memory Controller block.
- Software to
  AXI4-Stream — Use this block to replace a Memory
  Channel block with the **Channel type**
  parameter set to `Software to AXI4-Stream via DMA`
  connected to a Memory Controller block.
- AXI4 Random
  Access Memory — Use this block to replace a Memory
  Channel block with the **Channel type**
  parameter set to `AXI4 Random Access` connected to
  a Memory Controller block.
- AXI4 Video
  Frame Buffer — Use this block to replace a Memory
  Channel block with the **Channel type**
  parameter set to `AXI4 Video Frame Buffer`
  connected to a Memory Controller block.

### R2022a: Support for sample time offset

Specify a sample time offset in the **Sample time** parameter of
this block. Use the format `[period,offset]`. Previously, you could
specify only a period and not an offset.

The block mask also has a new **Inherit sample time offset**
parameter in the **Signal Attributes** tab. Select this parameter
when the read data has the same offset as the write data.

### R2022a: Simulation time improvements

When simulating a model with a Memory Channel block, you can
improve simulation speed when a high-fidelity simulation is not required. In the
block mask, select **Enable memory simulation** to simulate an
accurate memory data path, or clear that parameter for faster simulation speed when
debugging an algorithm. For an example that uses this feature, see Accelerate SoC Simulation by Varying Abstraction Levels.

### R2021a: Support for vectors up to 512 bits

The Memory Channel block supports vectors up to 512 bits. This
feature enables you to create a:

- Multichannel frame
- Multichannel sample
- Video frame with multiple pixels
- Video sample with multiple pixels
- Vectorized frame
- Vectorized pixel

To enable sample packing, open the block mask, and on the **Signal
Attributes** tab, select the **Enable sample packing (last
signal dimension as channel)** parameter.

### R2021a: Pipelined Read and Write Operations

The Memory Channel block simulates pipelined random access read and
write operations when you set the **Channel type** parameter to
`AXI4 Random Access`. This feature enables a higher
simulation fidelity of the memory random access throughput.

### R2021a: Extended Data Types

The Memory Channel block supports 16-bit and 128-bit integer data
types when you set the **Channel type** parameter to
`Software to AXI4 Stream via DMA` or `AXI4
Stream to Software via DMA`.

## Description

Stream data through a memory channel

The Memory Channel block streams data through external memory.
Conceptually, it models data transfer between one algorithm and another, through shared
memory. The algorithm can be hardware logic (HW), a processor model, or I/O devices. The
writer algorithm requests access to memory from the Memory Controller
block. After access is granted the writer algorithm writes to a memory buffer. In the
model, the data storage is modeled as buffers in the channel. When deploying on
hardware, the data is routed to an external shared memory.

This block can be configured to support any of these protocols:

- **AXI4-Stream to Software via DMA** – Model a connection
  between hardware logic and a software task through external memory. The
  writer puts data into the channel using a MathWorks® simplified AXI stream protocol and the reader (processor) gets
  data from a DMA driver interface. The channel models the datapath and
  software stack of that connection including a FIFO, DMA engine, interconnect
  and external memory, interrupts, kernel buffer management of the DMA driver,
  and data transfers to the software task. For more information about
  MathWorks simplified AXI stream protocol, see AXI4-Stream Interface.

  This image is a conceptual view of a Memory Channel block,
  streaming data from an FPGA algorithm to a processor algorithm.

  Conceptual view of Memory Channel block, streaming data from an FPGA Algorithm, through a FIFO, to memory. The data stream is then read by the processor via a DMA Driver block.
- **Software to AXI4-Stream via DMA** – Model a connection
  between hardware logic and a software task through external memory. The
  writer (processor) streams data into the channel via a DMA driver using a
  MathWorks simplified AXI stream protocol. The channel models the
  datapath and software stack of that connection including a FIFO, DMA engine,
  interconnect and external memory, interrupts, kernel buffer management of
  the DMA driver, and data transfers from the software task. For more
  information about the MathWorks simplified AXI stream protocol, see AXI4-Stream Interface.

  This image is a conceptual view of a Memory Channel block,
  streaming data from a processor algorithm to an FPGA algorithm.

  Conceptual view of a Memory Channel block, streaming data from a processor algorithm, through a DMA driver, to memory. Then, the FPGA algorithm reads the data stream.
- **AXI4-Stream FIFO** – Model a connection between two
  FPGA algorithms through external memory. The writer puts data into the
  channel as a master using the MathWorks simplified AXI stream protocol and the reader receives data
  from the channel as a slave using the same protocol. The channel behaves as
  a first in first out (FIFO) memory. The channel models the datapath of the
  connection. The Memory Channel block includes an intermediate
  burst-level FIFO, DMA engine, interconnect, and external memory. The
  external memory itself is managed as a circular buffer, where a buffer must
  be written before it can be read. For more information about the MathWorks simplified AXI stream protocol, see AXI4-Stream Interface.

  This image is a conceptual view of a Memory Channel block,
  streaming data from one FPGA algorithm to another FPGA algorithm.

  Conceptual view of Memory Channel block, streaming data from an FPGA Algorithm, through a FIFO, to memory. The data stream is then read by a receiving FPGA algorithm from the memory through a DMA Controller and a FIFO.
- **AXI4-Stream Video FIFO** – Model a connection between
  two hardware algorithms through external memory. This channel structure is
  similar to the **AXI4 Stream FIFO** configuration, but the
  writer and reader are using the MathWorks streaming pixel protocol, along with a back-pressure signal.
  For more information, see AXI4-Stream Video Interface.
- **AXI4-Stream Video Frame Buffer** – Model a connection
  between two hardware algorithms through external memory, using full video
  frame buffers. The protocol is the MathWorks streaming pixel protocol with back pressure. Also, the reader
  can ensure that the frame buffer is synchronized with downstream video
  timings by asserting an FSYNC protocol signal. The datapath includes a
  Video-DMA (VDMA) engine and the external memory buffers are managed as a
  circular buffer of full video frames. The channel structure is identical to
  the structure of **AXI4 Stream FIFO** channel type.
- **AXI4-Random Access** – Model a connection between two
  hardware algorithms through external memory, using the MathWorks simplified AXI4-Master protocol. Both the writer and the
  reader are masters, the channel is a slave in both cases. The external
  memory is unmanaged (there are no logical buffers, and no circular buffer).
  It is up to the reader and writer to coordinate timing on accesses to ensure
  the integrity of the data. For more information, see Simplified AXI4 Master Interface.

  This image is a conceptual view of a Memory Channel block,
  with random-access to the memory for writing, and random-access to the
  memory for reading.

  Conceptual view of a Memory Channel block, where an FPGA algorithm performs random write operations an a processor algorithm performs random read operations from memory.

For more information on the available protocols, see External Memory Channel Protocols.
