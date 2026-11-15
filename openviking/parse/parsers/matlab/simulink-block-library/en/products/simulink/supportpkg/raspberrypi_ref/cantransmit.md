---
type: simulink-block
title: 'CAN Transmit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'cantransmit'
documentation_source_path: 'supportpkg/raspberrypi_ref/cantransmit.html'
language: en
---

# CAN Transmit

## Ports

### Input

### **Port1** — Message data vector | scalar

The block accepts messages in `Raw data` and
`CAN Msg` formats.

- `Raw data` — To accept the message as
  a `uint8` vector array, set **Data is
  input as** to `Raw
  data`.
- `CAN Msg` — To accept the message in
  CAN message format, set **Data is input as** to
  `CAN Msg`.

**Data Types:** `uint8` | `CAN Msg`
### Output

### **Port1** — Status of data transmission scalar

Output port to display status of data transmission. For more
information, see Output Status.

#### Dependencies

To enable this port, select the **Output
Status** parameter.

## Parameters

### **CAN interface** — Name of CAN interface `can0` (default) | `char`

Enter the name of the real or virtual CAN interface. To find the name of
the CAN interface, in the Raspberry Pi terminal, execute the `ifconfig` command. To
configure the CAN interface, see CAN
properties.

### **Data is input as** — Data input type `Raw data` (default) | `CAN Msg`

Data input type used for transmitting messages.

- `Raw data` — To accept the message as
  a `uint8` vector array, set **Data is
  input as** as `Raw
  data`.
- `CAN Msg` — To accept the message in
  CAN message format, set **Data is input
  as** as `CAN Msg` and then
  perform these steps:

  - Add a CAN Pack (Vehicle Network Toolbox) block
    to your Simulink® model.
  - Connect the output of the CAN Pack (Vehicle Network Toolbox) block
    to the input port of the CAN Transmit
    block.
  - Using the options in the **Data is input
    as** list of the CAN Pack (Vehicle Network Toolbox) block,
    specify if you want to create your messages or you want
    to upload a CAN database file. If you choose to upload a
    CAN database file, the CAN Pack (Vehicle Network Toolbox)
    inherits the message properties from the uploaded
    file.

**Note**

To use CAN Pack (Vehicle Network Toolbox) block, you must
have a Vehicle Network Toolbox license.

### **Wait until data sent** — Wait until data is sent `off` (default) | `on`

When selected, the block waits for the time specified in the
**Time out in seconds** parameter before
transferring data.

- `on` — When you select this parameter, the
  block operates in the **Blocking
  mode**. If the message received in the previous
  time step is sent, the block accepts message from the input
  port. If the send operation is in progress, the block waits for
  the time specified in the **Time out in
  seconds** parameter, and then it accepts message
  from the input port.

  A task overrun occurs if the target hardware is still waiting
  for the requested message to be sent when the next send
  operation is scheduled to begin. To fix overruns:

  - Increase the sample time of input message.
  - Reduce the length of message at the input
    port.
- `off` — When you clear this parameter, the
  block operates in the **Non-blocking
  mode**. If the transmission of the message received
  in the previous time step is still in progress, the message at
  the input port at the given time step is dropped.

### **Time out in seconds** — Waiting time for sending data 1 (default) | integer

Specify the wait time for sending the message. After the specified time,
the block times out.

#### Dependencies

To enable this parameter, select **Wait until data
sent**.

### **Output Status** — Output status of message transfer off (default) | on

Select this option to indicate the status of message transfer. Status port
outputs `0` for successful transmit and error codes in case
of failure. Error codes are listed in this table.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 00 | ABTF | MLOA | TXERR | TXBO | TXEP | TXWAR |
| bit7 | bit6 | bit5 | bit4 | bit3 | bit2 | bit1 | bit0 |

ABTF: Message Aborted Flag bit

MLOA: Message Lost Arbitration bit

TXERR: Transmission Error Detected bit

TXBO: Bus-Off Error Flag bit

TXEP: Transmit Error-Passive Flag bit

TXWAR: Transmit Error Warning Flag bit

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

Message identifier type.

#### Dependencies

To enable this parameter, set **Data is input
as** to `Raw data`.

### **Message ID** — Message identifier 100 (default) | numeric identifier of length 11 or 29 bits

Message identifier, which is 11 bits long for the standard frame or 29
bits long for the extended frame, specified in decimal, binary, or hex. For
binary and hex formats, use `bin2dec(' ')` and
`hex2dec(' ')`, respectively, to convert the entry. The
message identifier is coded into a message that is sent to the CAN
bus.

#### Dependencies

To enable this parameter, set **Data is input
as** to `Raw data`. For
`CAN Msg`, the message identifier is
inherited from the identifier specified in the CAN Pack (Vehicle Network Toolbox) block.

### **Message Length** — Value of message length 8 (default) | positive integer less than or equal to 8

The length of the message, in bytes.

#### Dependencies

To enable this parameter, set **Data is input
as** to `Raw data`. For
`CAN Msg`, the message length is inherited
from the length of the CAN Pack (Vehicle Network Toolbox) block.

### **Request Remote Frame** — Enable remote message off (default) | on

When you select this parameter, the remote frame of the message is set to
1 indicating that the block is requesting the transmission of a specific
identifier.

#### Dependencies

To enable this parameter, set **Data is input
as** to `Raw data`.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Transmit message to CAN network

The CAN Transmit block transmits messages to the CAN network. This
block uses SocketCAN which is a device-independent driver for implementing the CAN
interface supporting all CAN shields.

The CAN Transmit block supports `Raw data` and
`CAN Msg` as input types. To use a CANdb (CAN database)
file or to specify signals manually, use `CAN Msg` input type
and the CAN Pack block. The CAN Pack block is available
from Vehicle Network Toolbox™. For more information on the CAN Pack block, see CAN
Pack (Vehicle Network Toolbox).

For more information on how to enable the SPI interface and configure the MCP2515 CAN
controller for CAN communication, see Enable and Configure Raspberry Pi for SPI and CAN Communication Using MCP2515 CAN Controller.

You can use CAN Transmit block to interact with a real or virtual CAN
interface. To bring up the CAN interface with Raspberry Pi®, refer to the user guide of your CAN shield. For more information on how
to set up a virtual CAN interface, see Setup Virtual CAN Interface.

**Note**

To generate C/C++ code for this block, you must have an Embedded Coder® license.
