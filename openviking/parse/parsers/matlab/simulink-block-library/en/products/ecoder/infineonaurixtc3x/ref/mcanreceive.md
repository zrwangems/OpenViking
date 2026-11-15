---
type: simulink-block
title: 'MCAN Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'mcanreceive'
documentation_source_path: 'infineonaurixtc3x/ref/mcanreceive.html'
language: en
---

# MCAN Receive

## Ports

### Input

### **Buffer Number** — Buffer number for CAN communication scalar

Specify the buffer number.

#### Dependencies

To enable this port, set the **Read source**
parameter to `Buffers` and select the **Enable
input port for buffer number** parameter.

**Data Types:** `uint8`
### Output

### **Msg** — CAN Message vector | scalar

The block outputs the CAN message (data and header) it receives from the
Simulink bus signal.

#### Dependencies

To enable this port, set **Output type** to
`Packed`.

**Data Types:** `CAN Message`

### **Data** — Message data vector | scalar

The block outputs the data it reads from the FIFO 0 register, FIFO 1
register, or buffer, based on the value of the **Read Source**
parameter. The maximum size of the data is `8` bytes for the
`Classic CAN` frame format and
`64` bytes for `CAN-FD` frame
format.

#### Dependencies

To enable this port, set the **Output type** parameter
to `Unpacked`.

**Data Types:** `uint8`

### **Id** — CAN message identifier value scalar

This port outputs a standard or extended ID value from the received CAN
message.

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint32`

### **Length** — CAN message length scalar

This port outputs the data length of the received CAN message in
bytes.

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

### **Id Type** — CAN message identifier type scalar

This port outputs the identifier type as:

- `0` — If the ID is an 11-bit standard
  identifier
- `1` — If the ID is an 29-bit extended
  identifier

#### Dependencies

To enable this port, set the **Output type** parameter
to `Unpacked` and enable **Output identifier
type** parameter.

**Data Types:** `Boolean`

### **Frame Type** — CAN message frame type scalar

This port outputs the CAN frame data format as:

- `0` — If the format is Classic CAN
- `1` — If the format is CAN-FD

#### Dependencies

To enable this port, set the **Output type** parameter
to `Unpacked` and enable **Output frame
type**.

**Data Types:** `uint32`

### **Bitrate switching** — Bit rate switching status scalar

This port outputs the status as one of these values:

- `0` — When the block receives the CAN FD frames
  without bit rate switching
- `1` — When the block receives the with bit rate
  switching

#### Dependencies

To enable this port, set the **Frame format** parameter
to `CAN-FD`, the **Output type**
parameter to `Unpacked`, and select the **Output
bit rate switching** parameter.

**Data Types:** `uint8`

### **Remote** — Remote frame status scalar

This port outputs the remote reception status as:

- `1` — If the received CAN message is a remote
  frame
- `0` — If the received CAN message is a data
  frame

#### Dependencies

To enable this port, set **Frame format**  to
`Classic CAN`, **Output type**
parameter to `Unpacked`, and enable **Output
remote** parameter.

**Data Types:** `Boolean`

### **FIFO Level** — FIFO fill level scalar

This port outputs the received FIFO fill level.

The FIFO level indicates the receive level of the FIFO 0 or FIFO 1 register
after the block reads the message. Rx FIFO indicates how much of Rx FIFO is
empty.

#### Dependencies

To enable this port, set the **Read source** parameter
to `FIFO 0` or `FIFO 1` and enable
the **Output receive FIFO level** parameter.

**Data Types:** `uint8`

### **Status** — Status of received message scalar

This port outputs the message read status as:

- `1` — If the read CAN message is invalid
- `0` — If the read CAN message is valid

#### Dependencies

To enable this port, select the **Output
Status** parameter.

**Data Types:** `uint8`

## Parameters

### **Frame format** — Frame format type `CAN-FD` (default) | `Classic CAN`

Select the frame type to receive the message.

### **Read source** — Source of received CAN message `FIFO 0` (default) | `FIFO 1` | `Buffers`

Specify the read source as FIFO or buffer.

**Note**

The block reads the message from FIFO 0, FIFO 1, or buffer depending on the
filter configuration you set (see MCAN
Receive Peripheral Configuration).

### **Buffer number** — Buffer number for CAN data reception `0` (default) | scalar in the range (0-63)

Specify the buffer number that the MCAN Receive block uses to read the received
CAN message.

#### Dependencies

To enable this parameter, set **Read source** to
`Buffers` and disable the **Enable input port for
buffer number** parameter.

### **Enable input port for buffer number** — Option to enable input port for buffer number `off` (default) | `on`

Select this parameter to enable the input port to specify the buffer
number.

#### Dependencies

To enable this parameter, set **Read source** to
`Buffers` and select the **Enable input port for
buffer number** parameter.

### **Output Type** — Message output type `Packed` (default) | `Unpacked`

Specify the message output type of the block as `Packed` or
`Unpacked`.

For unpacked messages, the block outputs different fields of the unpacked CAN
message.

For packed messages, the block outputs a Simulink bus signal. To extract the data from the Simulink bus signal, use
the CAN Unpack block if the frame format is Classic CAN or
CAN FD Unpack blocks if the
frame format is CAN-FD.

### **Output identifier type** — Option to enable output identifier type `off` (default) | `on`

Select this parameter to enable the **Id Type** port, which
outputs the standard or extended message status.

#### Dependencies

To enable this parameter, set the **Output type** parameter
to `Unpacked`.

### **Output frame type** — Option to enable output frame type `off` (default) | `on`

Select this parameter to enable the **Frame Type** port, which
outputs the message frame type.

#### Dependencies

To enable this parameter, set the **Output type** parameter
to `Unpacked`.

### **Output bitrate switching** — Option to enable output bitrate switching `off` (default) | `on`

Select this parameter to enable the **Bitrate Switching**
port, which outputs the status of bit rate switching.

#### Dependencies

To enable this parameter, set the **Frame format**
parameter to `CAN-FD` and the **Output
type** parameter to `Unpacked`.

### **Output remote** — Option to enable output frame type `off` (default) | `on`

Select this parameter to enable the **Remote** port, which
outputs the message remote frame status.

#### Dependencies

To enable this parameter, set the **Frame format**
parameter to `Classic CAN` and the **Output
type** parameter to `Unpacked`.

### **Output receive FIFO level** — Enable receive FIFO fill level `off` (default) | `on`

Select this parameter to enable the **FIFO level** port, which
outputs the received FIFO message level.

#### Dependencies

To enable this parameter, set the **Read source** parameter
to `FIFO 0` or `FIFO
1`.

### **Output status** — Option to enable output status `off` (default) | `on`

Select this parameter to enable the **Status** port, which
outputs the read status.

### **Sample Time** — Time interval to read message -1 (default) | nonnegative real value

Specify how often the block receives message, in seconds. When you specify this
parameter as `-1`, Simulink determines the best sample time for the block based on the context
of the block in the model.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Read data from CAN bus

The MCAN Receive block is a Modular CAN (MCAN) that reads data from the controller area
network (CAN) bus.

For unpacked messages, the block outputs the received values as a 64-by-1 array for the
CAN-FD frame format and as a 8-by-1 array for the Classic CAN frame format.

For packed messages, the block outputs a Simulink® bus signal. To extract data from the Simulink bus signal, use the CAN Unpack block
if the frame format is Classic CAN or CAN FD Unpack blocks if the frame
format is CAN-FD.
