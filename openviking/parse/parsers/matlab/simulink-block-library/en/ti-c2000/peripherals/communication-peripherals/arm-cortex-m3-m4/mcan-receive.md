---
type: simulink-block
title: 'MCAN Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'mcanreceive'
documentation_source_path: 'ref/mcanreceive.html'
language: en
---

# MCAN Receive

## Ports

### Output

### **Msg** — CAN Message vector | scalar

The MCAN Receive block outputs the received CAN message (data and header) the
Simulink bus signal. The CAN message received from the bus will be stored in a
FIFO or buffer.

#### Dependencies

To enable this port, set **Output type** to
`Packed`.

**Data Types:** `CAN Msg`

### **Data** — Message data vector | scalar

The block outputs data from the received CAN message. The maximum size of the
data is `64` of `uint8` format.

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

### **Status** — Status of received message scalar

The port outputs the message read status. The block outputs the status as
`0` if it reads new message and `1` if it does
not.

#### Dependencies

To enable this port select the **Output Status**
parameter.

**Data Types:** `uint8`

### **CAN identifier(ID)** — CAN message identifier scalar

The port outputs a standard or extended from the received CAN message.

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint32`

### **Length(LEN)** — CAN message length scalar

The port outputs the length of the received CAN message in bytes.

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

### **Remote transmission request(RTR)** — Remote frame status scalar

The port outputs the remote transmission status as one of these values.

- `1` - if the received CAN message is a remote
  frame
- `0` - if the received CAN message is a data frame

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

### **Bit rate switch(BRS)** — Bit rate switch status scalar

The port outputs:

- `0` - when CAN FD frames are transmitted without bit rate
  switching
- `1` - when CAN FD frames are transmitted with bit rate
  switching

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

### **Extended identifier(XTD)** — Extended or standard identifier scalar

The port outputs:

- `0` - if its 11-bit standard identifier
- `1` - if its 29-bit extended identifier

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

### **Frame data format(FDF)** — CAN frame data format scalar

The port outputs the CAN frame data format as:

- `0` - Classic CAN
- `1` - CAN-FD

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

## Parameters

### **MCAN module** — CAN module `A` (default) | `B`

Select the MCAN module from which you want to read the data.

### **Read source** — CAN receive message source `Buffers` (default) | `FIFO 0` | `FIFO 1`

The CAN message received from the bus will be stored in FIFO or buffer.

The MCAN Receive block stores the message in a FIFO0, FIFO1 or buffer depending on
the filter configuration you set in the hardware configuration parameters.

### **Buffer number (0-63)** — Buffer number `0` (default) | `1` | `2``...`

Specify the number of the buffer in which you want the MCAN Receive block to store
the received CAN message.

#### Dependencies

To enable this parameter, set **Read source** to
`Buffers`.

### **Output Type** — Message output type `Packed` (default) | `Unpacked`

The output type of the MCAN Receive block is either `Packed` or
`Unpacked`.

In the Unpacked mode, the block outputs the different fields of unpacked CAN
message. In the unpacked mode, the MCAN Receive block has `7 (ID, XTD, FDF,
BRS, LEN, RTR, Data)` output ports.

In the Packed mode, the block outputs a Simulink bus signal. To extract data from
Simulink bus signal, connect it to the CAN-FD Unpack block.

### **Output Status** — Enable output status `off` (default) | `on`

When you select the **Output Status** parameter, the block
configures the **Status** output port. The port outputs the read
status.

### **Sample Time** — Time interval to read message 0.1 (default) | -1 | nonnegative real value

Specify how often the block receives message, in seconds. When you specify this
parameter as `-1`, Simulink determines the best sample time for the block based on the block context
within the model.

## Libraries

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F28p65x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Read data from CAN bus

The MCAN Receive block reads messages from a Controller Area Network
(CAN) connected to the hardware.

In the Unpacked mode, the block outputs different fields of unpacked CAN
Messages.

In the Packed mode, the block outputs a Simulink® bus signal. To extract data from the Simulink bus signal, connect it to a CAN-FD Unpack block.

The MCAN Receive block receives messages from the CAN and delivers them to the
Simulink model. It outputs one message or all messages at each time step, depending on
the block parameters. The MCAN Receive block stores CAN messages received from the bus in a
first-in, first-out (FIFO) or buffer. The FIFO or buffer delivers the messages to your model
in the queued order at every time step.

**Note**

- For MCAN Receive block, if the data is not available, the output
  status shows the previously received data.
- When the **Output type** is packed and MCAN
  Receive block is connected to CAN FD Unpack block, the
  values of the `error`, `error state indicator
  (ESI)`, `reserved`, and `timestamp`
  fields of the received message are set to `0` and these values are
  reflected on the output of CAN FD Unpack block.

In receive output status we should mention the current behavior when data is not
available. The output data will be retained to its previously received value in case of data
is not available.

The number of elements to be stored in FIFO is configured in configuration parameters.
In case of buffers, the new data will not be stored unless the old data is read.

The FIFO, blocking or overwrite mode settings are configured in the MCAN.

Specify the **Output type** and its properties using the block
parameters dialog box. Configure additional properties of the CAN module in the
Configuration Parameters. For more refer to Model Configuration Parameters for Texas Instruments C2000 Processors.
