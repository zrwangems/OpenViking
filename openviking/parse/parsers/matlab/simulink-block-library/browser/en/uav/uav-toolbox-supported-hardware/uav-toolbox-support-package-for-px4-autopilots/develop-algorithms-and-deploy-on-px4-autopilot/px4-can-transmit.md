---
type: simulink-block
title: 'PX4 CAN Transmit'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4cantransmit'
documentation_source_path: 'px4/ref/px4cantransmit.html'
language: en
---

# PX4 CAN Transmit

## Ports

### Input

### **Port1** — Message data vector | scalar

The block accepts messages in `Raw data` and
`CAN Msg` formats.

- `Raw data` – To accept the
  message as a `uint8` vector array, set
  **Data is input as** to
  `Raw data`.
- `CAN Msg` – To accept the message
  in CAN message format, set **Data is input
  as** to `CAN Msg`. You
  can create a message or upload a CAN database file. For more
  information, see Data is input as.

#### Dependencies

This port appears only when you select the **Remote Frame** parameter.

**Data Types:** `uint8` | `CAN Msg`
### Output

### **Port1** — Status of data transmission scalar

Output port to display status of data transmission.

The port outputs one of these values:

- `0` for a successful CAN transmission.
- `1` for a failure in opening the CAN.
- `2` for a failure in setting Baud rate.
- `3` for a failure in setting CAN Test
  mode.
- `4` for a failure in CAN transmission.

For more information, see Output Status.

#### Dependencies

This port appears only when you select the **Output Status** parameter.

## Parameters

### **Data is input as** — Data input type `Raw data` (default) | `CAN Msg`

Select the type of the message at the input port.

- `Raw data` – To accept the message as
  a `uint8` vector array, set **Data is
  input as** to `Raw
  data`.
- `CAN Msg` – To accept the message in
  CAN message format, set **Data is input as** to
  `CAN Msg` and then perform these steps:

  1. Add a CAN Pack (Vehicle Network Toolbox) block
     from the Embedded Coder® / Vehicle Network Toolbox™ to your model.
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

  To use CAN Pack block, you must have an
  Embedded Coder / Vehicle Network Toolbox license.

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The type of message identifier.

#### Dependencies

This parameter appears only when you select **Data is input
as** to `Raw data`. For
`CAN Msg`, **Identifier
Type** is inherited from the type specified in the CAN Pack
block.

### **Message ID** — Message identifier 100 (default) | numeric identifier of length 11 or 29 bits

Message identifier, which is 11 bits long for the standard frame or 29
bits long for the extended frame, specified in decimal, binary, or hex. For
binary and hex formats, use `bin2dec(' ')` and
`hex2dec(' ')`, respectively, to convert the entry. The
message identifier is coded into a message that is sent to the CAN
bus.

#### Dependencies

This parameter appears only when you select **Data is input
as** to `Raw data`. For
`CAN Msg`, **Message ID**
is inherited from the identifier specified in the CAN
Pack block.

### **Data Field Length** — Length of message 3 (default) | positive integer

The length of the message, in bytes.

#### Dependencies

This parameter appears only when you select **Data is input
as** to `Raw data`. For
`CAN Msg`, **Message
Length** is inherited from the length of the CAN
Pack block.

### **Output Status** — Status of data transmission `off` (default) | `on`

When you select the **Output Status** parameter, the
block configures an output port. The port outputs the status of the data
transmission as a `uint8` integer. Each bit in the integer
corresponds to the type of error occurred during data transmission. An
output of `0` indicates successful transmission.

### **Remote Frame** — Enable remote message `off` (default) | `on`

When you select the **Remote Frame** parameter, the
remote frame of the message is set to 1 indicating that the block is
requesting the transmission of a specific identifier.

#### Dependencies

This parameter appears only when you select **Data is input
as** to `Raw data`. For
`CAN Msg`, the **Remote
Frame** is inherited from the request specified in the
CAN Pack block.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Transmit message to CAN network

The PX4 CAN Transmit block transmits message to a Controller Area
Network (CAN) network by using the PX4 Autopilot CAN port.

Specify the message type and its properties using the block parameters dialog box.

If you simulate a model that contains the PX4 CAN Transmit block
without connecting the hardware, the block does nothing. For more information, see Block Produces Zeros or Does Nothing in Simulation (Simulink).

During Connected I/O simulation, this block writes data to the peripherals of the
hardware.

**Note**

To avoid conflict with PX4 UAVCAN, disable UAVCAN before working with PX4 CAN
blocks. To disable, set the PX4 parameter, `UAVCAN_ENABLE` to `0`. For more
information, see Finding/Updating Parameters.
