---
type: simulink-block
title: 'CAN Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'canreceive'
documentation_source_path: 'supportpkg/raspberrypi_ref/canreceive.html'
language: en
---

# CAN Receive

## Ports

### Output

### **Data** — Message data port vector | scalar

Received message data, returned as a vector or scalar.

**Data Types:** `uint8` | `CAN Msg`

### **Status** — Status of output message scalar

Status of the received output message.

**Data Types:** `uint8`

### **Error** — Error codes scalar

Error codes.

#### Dependencies

To enable this parameter, select **Output
Error**.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 00 | 00 | 00 | 00 | RXWAR | RXEP | RXOVR |
| bit7 | bit6 | bit5 | bit4 | bit3 | bit2 | bit1 | bit0 |

RXOVR: Receive Buffer Overflow Flag bit

RXEP: Receive Error-Passive Flag bit

RXWAR: Receive Error Warning Flag bit

### **Remote** — Remote message flag scalar

Remote message flag.

#### Dependencies

To enable this parameter, select **Output
Remote**.

## Parameters

### **CAN interface** — Name of CAN interface `can0` (default) | `char`

Enter the name of the real or virtual CAN interface. To find the name of
the CAN interface, in the Raspberry Pi terminal, execute the `ifconfig` command. To
configure the CAN interface, see CAN
properties.

### **Data to be output as** — Data output type `Raw data` (default) | `CAN Msg`

Select a type to receive message.

- `Raw data` – To receive message as a
  1-by-*N*
  `uint8` array, select **Data to be
  output as** as `Raw
  data`.
- `CAN Msg` – To receive message in CAN
  message format, select **Data to be output as**
  as `CAN Msg` and then perform these steps:

  1. Add a CAN Unpack (Vehicle Network Toolbox)
     block to your Simulink® model.
  2. Connect the output of the CAN
     Receive block to the input of the CAN Unpack (Vehicle Network Toolbox)
     block.
  3. Using the options in the **Data to be
     output as** list of the CAN Unpack (Vehicle Network Toolbox)
     block, specify if you want to create your messages
     or you want to upload a CAN database file. If you
     choose to upload a CAN database file, the CAN Unpack (Vehicle Network Toolbox)
     inherits the message properties from the uploaded
     file.

  **Note**

  To use the CAN Unpack (Vehicle Network Toolbox) block,
  you must have a Vehicle Network Toolbox license.

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The type of message identifier.

#### Dependencies

This parameter appears only when you select **Data to be
output as** as `Raw data`.

### **Message ID** — Message identifier 100 (default) | numeric identifier of length 11 or 29 bits

Message identifier, which is 11 bits long for the standard frame size or
29 bits long for the extended frame size, specified in decimal, binary, or
hex. For binary and hex formats, use `bin2dec(' ')` and
`hex2dec(' ')`, respectively, to convert the entry. The
message identifier is coded into a message that is sent to the CAN
bus.

#### Dependencies

This parameter appears only when you select **Data to be
output as** as `Raw data`. To
output the identifier of the `CAN Msg`, select
**Output identifier** of the CAN
Unpack block.

### **Message Length** — Length of message 8 (default) | positive integer less than or equal to 8

The length of the message, in bytes.

#### Dependencies

This parameter appears only when you select **Data to be
output as** as `Raw data`. To
output the length of the `CAN Msg`, select
**Output length** of the CAN Unpack
block.

### **Sample Time** — Time interval to read message 0.1 (default) | -1 | nonnegative real value

Specify how often the block receives message, in seconds. When you specify
this parameter as `-1`, Simulink determines the best sample time for the block based on the
block context within the model.

### **Output Error** — Error in received message `off` (default) | `on`

When you select the **Output Error** parameter, the block
configures an output port, **Error**. The port outputs the
error code as a `uint8` integer. Each bit in code
corresponds to the type of error in the received message. An output of
`0` indicates that the message is error-free. Any value
other than `0` indicates that the message is an error
frame.

#### Dependencies

This parameter appears only when you select **Data to be
output as** as `Raw data`. To
output the error in the `CAN Msg`, select
**Output error** of the CAN Unpack
block.

### **Output Remote** — Enable remote messages off (default) | on

Select this parameter to enable the **Remote** output
port. This port outputs the message remote frame status.

#### Dependencies

To enable this parameter, set **Data to be output
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

Receive message from CAN network

The CAN Receive block receives messages from the CAN network. This
block uses SocketCAN which is a device-independent driver for implementing the CAN
interface supporting all CAN shields.

The CAN Receive block supports `Raw data` and
`CAN Msg` as output types. To use a CANdb (CAN database)
file or to specify signals manually, use `CAN Msg` output type
and the CAN Unpack block. The CAN Unpack block is
available from Vehicle Network Toolbox™. For more information on the CAN Unpack block, see CAN
Unpack (Vehicle Network Toolbox).

For more information on how to enable the SPI interface and configure the MCP2515 CAN
controller for CAN communication, see Enable and Configure Raspberry Pi for SPI and CAN Communication Using MCP2515 CAN Controller.

You can use CAN Receive block to interact with a real or virtual CAN
interface. To bring up the CAN interface with Raspberry Pi®, refer to the user guide of your CAN shield. For more information on how
to set up a virtual CAN interface, see Setup Virtual CAN Interface.

**Note**

To generate C/C++ code for this block, you must have an Embedded Coder® license.
