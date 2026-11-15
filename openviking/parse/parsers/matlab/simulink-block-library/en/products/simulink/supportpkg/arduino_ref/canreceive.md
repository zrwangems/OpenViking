---
type: simulink-block
title: 'CAN Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / CAN'
documentation_page: 'canreceive'
documentation_source_path: 'supportpkg/arduino_ref/canreceive.html'
language: en
---

# CAN Receive

## Ports

### Output

### **Data** — Message data vector | scalar

The block outputs messages in `uint8` and
`CAN Msg` format.

- `uint8` – To output the message
  as a `uint8` vector array, select
  **Data is output as** as
  `Raw data`.
- `CAN Msg` – To output the message
  in CAN message format, select **Data is output
  as** as `CAN Msg`. For
  more information, see Data to be output as.

**Data Types:** `uint8` | `CAN Msg`

### **Status** — Status of received message scalar

The port outputs the message received status. The status is
`1` if the block receives new message and
`0` if it does not.

**Data Types:** `uint8`

### **Error** — Error in received message scalar

The port outputs error codes using which you can identify the type of
error in the received message. For more information, see Output Error.

#### Dependencies

This port appears only when you select the **Output Error** parameter.

### **Remote** — Enable remote message scalar

The port sends request for remote frames.

#### Dependencies

This port appears only when you select the **Output Remote** parameter.

## Parameters

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

  1. Add a CAN Unpack block from the
     Vehicle Network Toolbox™ to your model.
  2. Connect the output of the CAN
     Receive block to the input of the
     CAN Unpack block.
  3. Using the options in the **Data to be
     output as** list of the CAN
     Unpack block, specify if you want to
     create your messages or you want to upload a CAN
     database file. If you choose to upload a CAN
     database file, the CAN Unpack
     inherits the message properties from the uploaded
     file.

  **Note**

  To use the CAN Unpack block, you must have
  a Vehicle Network Toolbox license.

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

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The type of message identifier.

#### Dependencies

This parameter appears only when you select **Data to be
output as** as `Raw data`.

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
this parameter as `-1`, Simulink® determines the best sample time for the block based on the
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

### **Output Remote** — Enable remote messages `off` (default) | `on`

When you select the **Output Remote** parameter, the
block configures an output port, **Remote**. The port
outputs the message remote frame status.

#### Dependencies

This parameter appears only when you select **Data to be
output as** as `Raw data`.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Receive message from CAN network

The CAN Receive block receives messages from a Controller Area Network
(CAN) network by using the CAN shield connected to the hardware. The CAN shield is
connected to the Serial Peripheral
Interface (SPI) pins on the hardware.

Click **View pin map** to open the Arduino Pin Mapping
table.

To know how to assign pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.

Specify the message type and its properties using the block parameters dialog box.
Specify the CAN properties of the model in the Configuration
Parameters dialog box.

This block supports only MCP2515-based CAN shields.

If you simulate a model that contains the CAN Receive block without
connecting the hardware, the block outputs zeros. For more information, see Block Produces Zeros or Does Nothing in Simulation.
