---
type: simulink-block
title: 'PX4 CAN Receive'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4canreceive'
documentation_source_path: 'px4/ref/px4canreceive.html'
language: en
---

# PX4 CAN Receive

## Ports

### Output

### **Data** — Message data vector | bus

The block outputs messages in `uint8` and
`CAN Msg` format.

- `uint8` – To output the message
  as a `uint8` vector array, select
  **Data is output as** to
  `Raw data`.
- `CAN Msg` – To output the message
  in CAN message format, select **Data is input
  as** to `CAN Msg`. For
  more information, see Data is input as.

**Data Types:** `uint8` | `CAN Msg`

### **Length** — Length of message scalar

The length of the message, in bytes.

**Data Types:** `uint8` | `CAN Msg`

### **Status** — Status of received message scalar

The port outputs the message received status.

The port outputs one of these values:

- `0` for a successful CAN receive.
- `1` for a failure in opening the CAN.
- `2` for a failure in setting Baud rate.
- `3` for a failure in setting CAN Test
  mode.
- `4` for a failure in CAN receive.

#### Dependencies

This port appears only when you select the **Output Status** parameter.

**Data Types:** `uint8`

### **Remote** — Enable remote message scalar

The port sends request for remote frames.

#### Dependencies

This port appears only when you select the **Output Remote** parameter.

## Parameters

### **Data is input as** — Data input type `Raw data` (default) | `CAN Msg`

Select a type to receive message.

- `Raw data` – To receive message as a
  1-by-*N*
  `uint8` array, select **Data is input
  as** to `Raw data`.
- `CAN Msg` – To receive message in CAN
  message format, select **Data is input as** to
  `CAN Msg` and then perform these steps:

  1. Add a CAN Unpack block from the
     Embedded Coder® / Vehicle Network Toolbox™ to your model.
  2. Connect the output of the CAN
     Receive block to the input of the
     CAN Unpack block.
  3. Using the options in the **Data is input
     as** list of the CAN
     Unpack block, specify if you want to
     create your messages or you want to upload a CAN
     database file. If you choose to upload a CAN
     database file, the CAN Unpack
     inherits the message properties from the uploaded
     file.

  **Note**

  To use the CAN Unpack block, you must have
  a Embedded Coder / Vehicle Network Toolbox license.

### **Message ID** — Message identifier 100 (default) | numeric identifier of length 11 or 29 bits

Message identifier, which is 11 bits long for the standard frame size or
29 bits long for the extended frame size, specified in decimal, binary, or
hex. For binary and hex formats, use `bin2dec(' ')` and
`hex2dec(' ')`, respectively, to convert the entry. The
message identifier is coded into a message that is sent to the CAN
bus.

#### Dependencies

This parameter appears only when you select **Data is input
as** to `Raw data`. To output the
identifier of the `CAN Msg`, select
**Output identifier** of the CAN
Unpack block.

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The type of message identifier.

#### Dependencies

This parameter appears only when you select **Data is input
as** to `Raw data`.

### **Sample Time** — Time interval to read message 0.1 (default) | -1 | nonnegative real value

Specify how often the block receives message, in seconds. When you specify
this parameter as `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

### **Output Status** — Enable remote messages `off` (default) | `on`

When you select the **Output Status** parameter, the
block configures an output port, **Status**. The port
outputs the message remote frame status.

### **Output Remote Flag** — Enable remote messages `off` (default) | `on`

When you select the **Output Remote Flag** parameter, the
block configures an output port, **Remote**. The port
outputs the message remote frame status.

#### Dependencies

This parameter appears only when you select **Data is input
as** to `Raw data`.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Receive message from CAN network

The PX4 CAN Receive block receives messages from a Controller Area
Network (CAN) network by using the PX4 Autopilot CAN port connected to the
hardware.

Specify the message type and its properties using the block parameters dialog
box.

If you simulate a model that contains the PX4 CAN Receive block without
connecting the hardware, the block outputs zeros. For more information, see Block Produces Zeros or Does Nothing in Simulation (Simulink).

Also, if there are no messages on the CAN bus, the block outputs zeros.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.

**Note**

To avoid conflict with PX4 UAVCAN, disable UAVCAN before working with PX4 CAN
blocks. To disable, set the PX4 parameter, `UAVCAN_ENABLE` to `0`. For more
information, see Finding/Updating Parameters.
