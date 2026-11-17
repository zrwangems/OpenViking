---
type: simulink-block
title: 'C28x SCI Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c28xscitransmit'
documentation_source_path: 'ref/c28xscitransmit.html'
language: en
---

# C28x SCI Transmit

## Ports
```yaml
ports:
- name: Data
  summary: Data written to serial bus scalar | vector
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single
- name: Status
  summary: Data transmitted at given time step scalar
  direction: output
  data_types: uint8 | uint16
```

### Input

### **Data** — Data written to serial bus scalar | vector

Input data written to the serial communication bus.

If the input port of SCI Transmit is of variable data
size and If the length of variable data is `0`, then
the block will transmit only the header and terminator.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single`
### Output

### **Status** — Data transmitted at given time step scalar

The port outputs `0` if the data is transmitted at a
given time step. Otherwise, it outputs value `1`,
indicating that transmit FIFO is full and data transmission is not
successful.

#### Dependencies

To enable this port, select the **Output
status** parameter.

**Data Types:** `uint8` | `uint16`
## Parameters
```yaml
parameters:
- name: SCI module
  summary: SCI module for communication A (default) | B | C | D
  group: ''
- name: Additional package header
  summary: Indicates start of data 'S' (default) | string | char | number from 0 to 255
  group: ''
- name: Additional package terminator
  summary: Indicates end of data 'E' (default) | string | char | number from 0 to 255
  group: ''
- name: Frame size
  summary: Specify length of data to be received 600 (default) | any positive integer
  group: ''
- name: Wait until previous data transmitted
  summary: Wait until data received in previous time step is sent on (default) | off
  group: ''
- name: Output status
  summary: Option to display the transmit status during data transmission off (default) | on
  group: ''
```

### **SCI module** — SCI module for communication `A` (default) | `B` | `C` | `D`

The SCI module used for communication.

### **Additional package header** — Indicates start of data `'S'` (default) | string | char | number from 0 to 255

The data located at the beginning of the sent data package, which is not
part of the data being transmitted, and indicates the start of data. The
additional package header must be represented using ASCII characters. Use a
string or a number (0–255). You must add single quotes around strings
entered for this parameter, but the quotes are not sent or included in the
total byte count. To specify a null value (no package header), enter two
single quotes only.

The data type of header is not related to the data type mentioned on the
block.

**Note**

Match additional package headers or terminators with those
specified in the host SCI Receive block.

### **Additional package terminator** — Indicates end of data `'E'` (default) | string | char | number from 0 to 255

The data located at the end of the sent data package, which is not part of
the data being transmitted, and indicates the end of data. The additional
package terminator must be represented using ASCII characters. Use a string
or a number (0–255). You must put single quotes around strings entered in
this field, but the quotes are not sent or included in the total byte count.
To specify a null value (no package terminator), enter two single quotes
only.

The data type of terminator is not related to the data type mentioned on
the block.

### **Frame size** — Specify length of data to be received `600` (default) | any positive integer

Specify the data bytes to be transferred. This parameter can be used when
transmit rate is more than the receive rate.

Frame size is calculated by: Receive rate/Transmit rate. For example, if a
signal is transmitted at `50` micro sec, and frame size is
`600`, you can receive the data at
`0.03` sec.

When the frame size is more than `1`, the additional
package header and terminator are added at the start and end of the frame.
For example, `<Header>DATA(1:frame
size)<Terminator>`

Where, `DATA(1:frame size)` indicates the signal to be
transmitted of length to frame size.

### **Wait until previous data transmitted** — Wait until data received in previous time step is sent `on` (default) | `off`

- `on` — When you select this parameter, the
  transmit operation runs in the blocking mode. In this mode, if
  transmit FIFO is full then it will wait for previous data to be
  transmitted and verifies if space is available in the FIFO to
  transmit the current data.

  A task overrun occurs if the target hardware is still waiting for
  the requested data to be sent when the next transmit operation is
  scheduled to begin. To fix overruns increase the time step by using
  the **Sample time** parameter.
- `off` — When you clear this parameter, the
  transmit operation runs in the non-blocking mode. In this mode, if
  the block is still transmitting the data received in the previous
  time step, the data at the input port in the current time step is
  dropped.

  In either mode, if the block is yet to establish the connection
  between the transmitting and receiving hosts. or if the connection
  is lost, the data at the input port is dropped.

### **Output status** — Option to display the transmit status during data transmission `off` (default) | `on`

Select this option to display the transmit status during data
transmission.

When you select the Output status parameter, the block configures an
output port. The port on the block is labeled as Status, indicating that the
block outputs the status of the transmit operation at the output
port.
## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Transmit data from target via serial communication interface (SCI) to host

The SCI Transmit block transmits scalar or vector data using the
specified SCI hardware module. The sampling rate and data type are inherited from the
input port.

A model can only contain one SCI Transmit block for each module. The
C28x processor has four SCI modules — A, B, C, and D. The number of SCI modules
available varies depending on the processor selected. You can configure the SCI modules
by navigating to **Hardware Implementation** > **Target hardware resources**. Verify that these settings meet the requirements of your application.
Verify that these settings meet the requirements of your application.

**Note**

- Fixed-point inputs are not supported by this block, but you can use a
  Data Type Conversion block to convert the
  fixed-point format to native data type. In the Data Type
  Conversion block, set the **Input and output to
  have equal** parameter to `Stored Integer
  (SI)`.
- Serial External mode with similar SCI module blocks results in
  conflict check error.

The block outputs data either in blocking mode or in non-blocking mode. In blocking
mode, the model blocks the execution while it waits if transmit FIFO is full. In
non-blocking mode, the model runs continuously. To set the block in blocking mode,
select the **Wait until previous data transmitted** option.

**Note**

You might encounter data loss, when you try to send data greater than the FIFO
length in Non-Blocking mode.
