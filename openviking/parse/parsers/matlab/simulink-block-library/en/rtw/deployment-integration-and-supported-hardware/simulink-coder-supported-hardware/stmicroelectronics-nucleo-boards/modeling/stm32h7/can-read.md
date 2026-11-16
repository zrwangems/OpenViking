---
type: simulink-block
title: 'CAN Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32H7'
documentation_page: 'canread'
documentation_source_path: 'nucleo/ref/canread.html'
language: en
---

# CAN Read

## Ports

### Output

### **Data** — Message data vector | scalar

The block outputs messages in `uint8` or `CAN
Msg` format.

- `uint8` – To output the message as a
  `uint8` vector array, select **Data Format**
  as `Raw data`.
- `CAN Msg` – To output the message in CAN message
  format, select **Data Format** as `CAN
  Msg`.

This port outputs `0` if the received CAN message is a remote
frame.

**Data Types:** `uint8` | `CAN Msg`

### **Status** — Status of received message scalar

The port outputs message read status.

- The status is `1`, if the block reads new message.
- The status is `0`, if the block reads no new
  message.

#### Dependencies

This port appears only when you select the **Output
Status** parameter.

**Data Types:** `uint8`

### **Remote** — Enable remote message scalar

The port outputs 1 if the received CAN message is a remote frame.

#### Dependencies

This port appears only when you select **Output
Remote** parameter.

## Parameters

### **Module** — Module used for communication `0` (default) | `Any integer value`

Module to which the CAN device is connected.

**Note**

- CAN 0 Module on block represents CAN 1 peripheral on hardware.
- CAN 1 Module on block represents CAN 2 peripheral on hardware.

### **Data Format** — Data output type `Raw data` (default) | `CAN Msg`

Select a type to read message.

- `Raw data` – To read message as a
  1-by-*N*
  `uint8` array, select **Data Format**  as
  `Raw data`.
- `CAN Msg` – To read message in CAN message format,
  select **Data Format** as `CAN Msg` and
  then perform these steps:

  1. Add a CAN Unpack block from the Vehicle Network Toolbox™ to your model.
  2. Connect the output of the CAN Read block to the input of
     the CAN Unpack block.
  3. Using the options in the **Data to be output as** list
     of the CAN Unpack block, specify if you want to create your
     messages or you want to upload a CAN database file. If you choose to upload
     a CAN database file, the CAN Unpack inherits the message
     properties from the uploaded file.

  **Note**

  To use the CAN Unpack block, you must have a Vehicle Network Toolbox license.

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The type of message identifier.

#### Dependencies

This parameter appears only when you select **Data Format** as
`Raw data`.

### **Identifier** — Message identifier 100 (default) | numeric identifier of length 11 or 29 bits

Identifier, which is 11 bits long for the standard frame size or 29 bits long for
the extended frame size, specified in decimal, binary, or hex. For binary and hex
formats, use `bin2dec(' ')` and `hex2dec(' ')`,
respectively, to convert the entry. The identifier is coded into a message that is sent
to the CAN bus.

#### Dependencies

This parameter appears only when you select **Data Format** as
`Raw data`. To output the identifier of the
`CAN Msg`, select **Output identifier** of
the CAN Unpack block.

### **Length (bytes)** — Length of message 8 (default) | positive integer less than or equal to 8

The length of the message in bytes.

#### Dependencies

This parameter appears only when you select **Data Format** as
`Raw data`. To output the length of the `CAN
Msg`, select **Output length** of the CAN
Unpack block.

### **Sample Time** — Time interval to read message -1 (default) | 0.1 | non-negative real value

Specify how often the block receives message, in seconds. When you specify this
parameter as `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

### **Output Remote** — Enable remote messages `off` (default) | `on`

When you select the **Output Remote** parameter, the block
configures an output port, **Remote**. The port outputs the message
remote frame status.

#### Dependencies

This parameter appears only when you select **Data Format** as
`Raw data`.

### **Output Status** — Enable output status `off` (default) | `on`

When you select the **Output Status** parameter, the block
configures an output port, **Status**. The port outputs the status
message.

## Libraries

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Read message from CAN network

The CAN Read block reads messages from a Controller Area Network (CAN)
network connected to the hardware.

Click **View pin map** to open the Nucleo Pin Mapping table.

Specify the **Data Format** and its properties using the block parameters
dialog box. Configure the properties of CAN
module in the Configuration Parameters.

**Note**

- **CAN Read** block is currently supported only for STM32 Nucleo
  H743ZI2.
- Each instance of CAN Read block configures a CAN filter to accept messages with
  the specified identifier.
- The configured filter accepts and saves the CAN message in a one-element buffer
  which, needs to be read before accepting the new message.
