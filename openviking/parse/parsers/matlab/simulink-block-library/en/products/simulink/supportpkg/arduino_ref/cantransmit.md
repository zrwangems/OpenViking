---
type: simulink-block
title: 'CAN Transmit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / CAN'
documentation_page: 'cantransmit'
documentation_source_path: 'supportpkg/arduino_ref/cantransmit.html'
language: en
---

# CAN Transmit

## Ports

### Input

### **Port1** — Message data vector | scalar

The block accepts messages in `Raw data` and
`CAN Msg` formats.

- `Raw data` – To accept the
  message as a `uint8` vector array, set
  **Data is input as** as
  `Raw data`.
- `CAN Msg` – To accept the message
  in CAN message format, set **Data is input
  as** as `CAN Msg`. You
  can create your messages or you can upload a CAN database
  file. For more information, see Data is input as.

**Data Types:** `uint8` | `CAN Msg`
### Output

### **Port1** — Status of data transmission scalar

Output port to display status of data transmission. For more
information, see Output
Status.

#### Dependencies

This port appears only when you select the **Output Status** parameter.

## Parameters

### **Data is input as** — Data input type `Raw data` (default) | `CAN Msg`

Select the type of the message at the input port.

- `Raw data` – To accept the message as
  a `uint8` vector array, set **Data is
  input as** as `Raw
  data`.
- `CAN Msg` – To accept the message in
  CAN message format, set **Data is input as** as
  `CAN Msg` and then perform these steps:

  1. Add a CAN Pack (Vehicle Network Toolbox) block
     from the Vehicle Network Toolbox™ to your model.
  2. Connect the output of CAN Pack
     block to the input port of the CAN
     Transmit block.
  3. Using the options in the **Data is input
     as** list of the CAN Pack
     block, specify if you want to create your messages
     or you want to upload a CAN database file. If you
     choose to upload a CAN database file, the CAN
     Pack inherits the message properties from
     the uploaded file.

  **Note**

  To use CAN Pack block, you must have a
  Vehicle Network Toolbox license.

### **Output Status** — Status of data transmission `off` (default) | `on`

When you select the **Output Status** parameter, the
block configures an output port. The port outputs the status of the data
transmission as a `uint8` integer. Each bit in the integer
corresponds to the type of error occurred during data transmission. An
output of `0` indicates successful transmission.

### **Wait until data sent** — Wait until the data is sent `off` (default) | `on`

- `on` — When you select this parameter, the block
  operates in the **Blocking mode**. If
  the message received in the previous time step is sent, the block
  accepts message from the input port. If the send operation is in
  progress, the block waits for the time specified in the
  **Time out in seconds** parameter, and then it
  accepts message from the input port.

  A task overrun occurs if the target hardware is still waiting for
  the requested message to be sent when the next send operation is
  scheduled to begin. To fix overruns:

  - Increase the sample time of input message.
  - Reduce the length of message at the input port.
- `off` — When you clear this parameter, the block
  operates in the **Non-blocking mode**.
  If the transmission of the message received in the previous time
  step is still in progress, the message at the input port at the
  given time step is dropped.

### **Time out in seconds** — Waiting time for sending message 1 (default) | integer

Specify the wait time for sending the message. After the specified time,
the block times out.

#### Dependencies

This parameter appears only when you select the **Wait until
data sent** parameter.

### **Message ID** — Message identifier 100 (default) | numeric identifier of length 11 or 29 bits

Message identifier, which is 11 bits long for the standard frame or 29
bits long for the extended frame, specified in decimal, binary, or hex. For
binary and hex formats, use `bin2dec(' ')` and
`hex2dec(' ')`, respectively, to convert the entry. The
message identifier is coded into a message that is sent to the CAN
bus.

#### Dependencies

This parameter appears only when you select **Data is input
as** as `Raw data`. For
`CAN Msg`, **Message ID**
is inherited from the identifier specified in the CAN
Pack block.

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The type of message identifier.

#### Dependencies

This parameter appears only when you select **Data is input
as** as `Raw data`. For
`CAN Msg`, **Identifier
Type** is inherited from the type specified in the CAN Pack
block.

### **Message Length** — Length of message 8 (default) | positive integer less than or equal to 8

The length of the message, in bytes.

#### Dependencies

This parameter appears only when you select **Data is input
as** as `Raw data`. For
`CAN Msg`, **Message
Length** is inherited from the length of the CAN
Pack block.

### **Request Remote Frame** — Enable remote message `off` (default) | `on`

When you select the **Request Remote Frame** parameter,
the remote frame of the message is set to 1 indicating that the block is
requesting the transmission of a specific identifier.

#### Dependencies

This parameter appears only when you select **Data is input
as** as `Raw data`. For
`CAN Msg`, the **Request Remote
Frame** is inherited from the request specified in the
CAN Pack block.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Transmit message to CAN network

The CAN Transmit block transmits message to a Controller Area Network
(CAN) network by using the CAN shield. The CAN shield is connected to the Serial Peripheral Interface (SPI) pins on
the hardware.

Click **View pin map** to open the Arduino Pin Mapping
table.

To know how to assign pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.

Specify the message type and its properties using the block parameters dialog box.
Specify the CAN properties of the model in the Configuration
Parameters dialog box.

This block supports only MCP2515-based CAN shields.

If you simulate a model that contains the CAN Transmit block without
connecting the hardware, the block does nothing. For more information, see Block Produces Zeros or Does Nothing in Simulation.
