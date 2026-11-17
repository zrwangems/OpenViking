---
type: simulink-block
title: 'F2837xD/F2838x/F2838x-M4 IPC Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F2837xD'
documentation_page: 'f2837xdf2838xf2838xm4ipcreceive'
documentation_source_path: 'ref/f2837xdf2838xf2838xm4ipcreceive.html'
language: en
---

# F2837xD/F2838x/F2838x-M4 IPC Receive

## Ports
```yaml
ports:
- name: Out
  summary: IPC receive vector | scalar
  direction: output
- name: Status
  summary: IPC receive status 0 | 1 | 2 | 3 | 4 | 6
  direction: output
```

### Output

### **Out** — IPC receive vector | scalar

Data read from the other Core.

### **Status** — IPC receive status 0 | 1 | 2 | 3 | 4 | 6

The status port outputs one of these values:

- 0 — No errors
- 1 — Data not available
- 2 — Data type mismatch
- 4 — Data length mismatch
- 6 — Data type and Data length mismatch

**Note**

When no data is transmitted, the IPC receive block receives 0 of uint16 data
type and data type mismatch status is displayed
## Parameters
```yaml
parameters:
- name: Source
  summary: Source selected to receive data C28x (CPU1/CPU2)/CPU1 (default) | ARM Cortex-M4 (CM)/CPU2
  group: ''
- name: Channel
  summary: Channel selected to receive data 0 (default) | 0–31
  group: ''
- name: Data type
  summary: Type of data to be received uint16 (default) | single | int8 | uint8 | int16 | int32 | uint32 | boolean
  group: ''
- name: Data length
  summary: Size of data to be received 1 (default) | positive integer
  group: ''
- name: Enable blocking
  summary: Specify if Core must wait to read data off (default) | on
  group: ''
- name: Sample time
  summary: Interval at which block reads data 0.001 (default) | –1 | positive scalar
  group: ''
```

### **Source** — Source selected to receive data `C28x (CPU1/CPU2)/CPU1` (default) | `ARM Cortex-M4 (CM)/CPU2`

The source at which you want to receive data. The source selection is based on the
processor you choose. For F2838x(C28x) processor, the source is either C28x
(CPU1/CPU2) or ARM Cortex-M4 (CM). For F2838x-M4 ARM core processor, the source is
CPU1 or CPU2.

The IPC Receive block mask displays the current source and the channel selected.
For example, if the block displays `C28x_Ch0`, then the source is
`C28x (CPU1/CPU2)` and channel is `0`. Similarly
if the IPC Receive block displays `CM_Ch1`, then the source is
`ARM Cortex-M4 (CM)` and channel is `1`.

**Note**

This parameter is only available for F2838x(C28x) and F2838x-M4 ARM core
processors.

### **Channel** — Channel selected to receive data `0` (default) | 0–31

The channel at which you want to receive data. Each channel is a separate memory
location in the shared memory.

**Note**

The transmitter and receiver have 32 channels each to transmit and receive data.
For data transmission and reception, the transmitter and receiver must be set to the
same channel number.

### **Data type** — Type of data to be received `uint16` (default) | single | int8 | uint8 | int16 | int32 | uint32 | boolean

The type of data the block receives.

Vector data is stored in the global shared RAM, and the address of the data is
stored in the MSGRAM.

### **Data length** — Size of data to be received `1` (default) | positive integer

The number of data units received at each sample time. If the data length is 1,
the block interprets each incoming piece of data as a scalar value; if the data length
is greater than 1, the block interprets each incoming piece of data as a vector with
length equal to **Data length**. The maximum size for scalar and
vector data is 32 bits.

### **Enable blocking** — Specify if Core must wait to read data `off` (default) | on

When enabled, the Core waits until data is available from the other Core.

### **Sample time** — Interval at which block reads data `0.001` (default) | `–1` | positive scalar

The time between data samples, measured in seconds. When you set this parameter to
`-1`, Simulink® determines the best sample time for the block based on the block context
within the model.
## Libraries

C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28p65x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Receive data from either core while using separate model for each core

The IPC Receive block receives and outputs data sent from one Core to the
other.

**Note**

Use IPC Receive and IPC Transmit blocks to receive or sent data to either core for
multi-core processors. Use these blocks for flat model approach where you are using
separate models for each core.

If you are using multiprocessor modeling approach with single model triggering
multiple cores using Task Manager, use the Interprocess Data Read and Interprocess Data Write blocks to send and
receive data between cores.

Core1 transmits data to its allocated memory (Core1-to-Core2 Message RAM) and receives
data from the allocated memory of Core2 (Core2-to-Core1 Message RAM). Similarly Core2
transmits data to its allocated memory (Core2-to-Core1 Message RAM) and receives data from
allocated memory of Core1 (Core1-to-Core2 Message RAM). For F2838xD, Core1/Core2 can be
CPU1,CPU2 or ARM Cortex-M4 (CM) and for F2837xD, Core1/Core2 can be CPU1 or CPU2.

If Core1 and Core2 are both C28x core, then the data and channel structure between two
cores are allocated in Message RAM and the data array is allocated in Global Shared RAM. In
C28x core, by default all the channel structures are created in Message RAM.

However, if one of the core is ARM Cortex M4 (applicable only for F2838x), then the data
array is allocated only using Message RAM as global shared RAM is not available between
cores. In order to accommodate more data, only required channel structures are created in
Message RAM. Hence if the channel number used for transmit block in one core does not match
with the receive block in other core the data transmission will not occur.

A hardware interrupt block can be used along with the IPC Receive block
for receiving data based on hardware interrupts.

- **C28x processor** - Channels 0, 1, 2, and 3 are configured for
  hardware interrupts IPC0, IPC1, IPC2, and IPC3 respectively.
- **F2838x-M4 processor** - Channels 0, 1, 2, 3, 4, 5, 6 and 7 are
  configured for hardware interrupts IPC0, IPC1, IPC2, IPC3, IPC4, IPC5, IPC6 and IPC7
  respectively.

These hardware interrupts can be set in the hardware interrupt block using these
parameters: **CPU interrupt number**
`1` and **PIE interrupt numbers**
`13`, `14`, `15`, and
`16` respectively.

### Memory Allocation for IPC Flat Models

The **Channel assignment**, **Memory usage in CM message
RAM**, and **Memory usage in C28x message RAM** provides
detailed description on how the memory is allocated in IPC blocks for flat models.

- **Channel assignment** - The channel assignment in the C28x-CM
  IPC (Inter-Processor Communication) is a crucial aspect for seamless communication
  between CPU1, CPU2, and the Communication Manager (CM). Internally, channel arrays
  are maintained for each CPU, facilitating data exchange with the CM. This process
  involves sorting the arrays to allocate channels based on a predetermined order,
  maximizing the utilization of message RAM for efficient communication.

  IPC block sorts the array and allocates the channels based on the sorted order
  which may result in channel selection on block not matching with channel selection
  on generated code. This logic helps us to maximize the full use of message RAM to
  communicate with CPUx and CM.

  For example, based on the channel selection on the model:

  - **CM-CPU1 channel selection** - if CM-CPU1 array is
    sorted like `[0_Rx, 0_Tx, 1_Tx, 2_Rx, 4_Rx]` then the
    corresponding entries in generated code would be `[0_Rx, 0_Tx, 1_Tx,
    2_Rx, 3_Rx]`.
  - **CM-CPU2 channel selection** - if CM-CPU2 array is
    sorted like looks like `[0_Rx, 0_Tx, 2_Rx, 3_Tx, 5_Tx, 6_Tx]`
    then the corresponding entries in generated code would be `[0_Rx,
    0_Tx, 1_Rx, 2_Tx, 3_Tx, 4_Tx]`.
- **Memory usage in CM message RAM** - CM message RAM creates the
  following variables with IPC structure and buffers when IPC Transmit or Receive
  block is configured in the model. For example, when **Buffer size =
  2**:

  1. **MW\_IPCCMtoCPUxBuffers** - number of elements
     = (number of channels \* Buffer size) - size = 8 bytes to store datatype, data
     length and data as structure
  2. **MW\_Cpu1PutWriteIndexes** - number of elements
     = number of channels - size = 2 bytes
  3. **MW\_Cpu1GetReadIndexes** - number of elements
     = number of channels - size = 2 bytes
  4. **MW\_CPU1WRITEFLAGBUFF1** - number of elements
     = number of channels - size = 2 bytes
  5. **MW\_CPU1WRITEFLAGBUFF2** - number of elements
     = number of channels - size = 2 bytes
  6. **MW\_CPU1READFLAGBUFF1** - number of elements =
     number of channels - size = 2 bytes
  7. **MW\_CPU1READFLAGBUFF2** - number of elements =
     number of channels - size = 2 bytes

     Buffer allocation based on the channel selection and data length

     - mwCpu1Channel<channelNumber>Buff1
     - mwCpu1Channel<channelNumber>Buff2 - number of elements = length of
       data (datalength) - size 4 bytes
- **Memory usage in C28x message RAM** - C28x message RAM creates
  the following variables with IPC structure and buffers when IPC Transmit or Receive
  block is configured in the model. For example, when **Buffer size =
  2**:

  1. **MW\_IPCCPUtoCMBuffers** - number of elements = (number of
     channels \* Buffer size) - size = 8 bytes to store datatype, data length and data
     as structure.
  2. **MW\_CmPutWriteIndexes** - number of elements = number of
     channels - size = 2 bytes
  3. **MW\_CmGetReadIndexes** - number of elements =
     number of channels - size = 2 bytes
  4. **MW\_CMWRITEFLAGBUFF1** - number of elements =
     number of channels - size = 2 bytes
  5. **MW\_CMWRITEFLAGBUFF2** - number of elements =
     number of channels - size = 2 bytes
  6. **MW\_CMREADFLAGBUFF1** - number of elements =
     number of channels - size = 2 bytes
  7. MW\_CMREADFLAGBUFF2 - number of elements = number of channels - size = 2
     bytes

     Buffer allocation based on the channel selection and data length.

     - mwCmChannel<channelNumber>Buff1
     - mwCmChannel<channelNumber>Buff2 - number of elements = length of
       data (datalength) - size 4 bytes
