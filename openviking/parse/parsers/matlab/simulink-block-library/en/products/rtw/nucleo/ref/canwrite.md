---
type: simulink-block
title: 'CAN Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32H7'
documentation_page: 'canwrite'
documentation_source_path: 'nucleo/ref/canwrite.html'
language: en
---

# CAN Write

## Ports

### Input

### **Tx** — Input data port vector | scalar

The block accepts messages in `Raw data` or
`CAN Msg` formats.

- `Raw data` – To accept the message as a
  `uint8` vector array, set **Data is input
  as** as `Raw data`.
- `CAN Msg` – To accept the message in CAN message
  format, set **Data is input as** as `CAN
  Msg`. You can create your messages or you can upload a CAN
  database file.

**Data Types:** `uint8` | `CAN Msg`
### Output

### **Status** — Status of data transmission scalar

Output port to display the status of data transmission.

- `1` - data transmission is successful
- `0` - data transmission is unsuccessful

#### Dependencies

This port appears only when you select the **Output
Status** parameter.

## Parameters

### **Module** — Module used for communication `0` (default) | `Any integer value`

Module to which the CAN device is connected.

**Note**

- CAN 0 Module on block represents CAN 1 peripheral on hardware.
- CAN 1 Module on block represents CAN 2 peripheral on hardware.

### **Data Format** — Data output type `Raw data` (default) | `CAN Msg`

Select a type to write message.

- `Raw data` – To write message as a
  1-by-*N*
  `uint8` array, select **Data Format**  as
  `Raw data`.
- `CAN Msg` – To write message in CAN message format,
  select **Data Format** as `CAN Msg` and
  then perform these steps:

  1. Add a CAN pack block from Vehicle Network Toolbox™ to your model.
  2. Connect the output of the CAN Read pack block to the
     input of the **CAN Write** block
  3. Using the options in the **Data to be input as** list
     of the CAN Pack block, specify if you want to create your
     messages or you want to upload a CAN database file. If you choose to upload
     a CAN database file, the CAN Pack inherits the message
     properties from the uploaded file.

  **Note**

  To use the CAN Pack block, you must have a Vehicle Network Toolbox license.

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

The length of the message, in bytes.

#### Dependencies

This parameter appears only when you select **Data Format** as
`Raw data`. To output the length of the `CAN
Msg`, select **Output length** of the CAN
Unpack block.

### **Remote Frame** — Enable remote message `off` (default) | `on`

The block sends a remote frame in the CAN message if this parameter is selected. The
data at the input port is not sent in the CAN message.

#### Dependencies

This parameter appears only when you select **Data Format** as
`Raw data`. For CAN Msg, the Remote Frame is inherited from
the request specified in the CAN Pack block.

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

Write message to CAN network

The CAN Write block writes message to a Controller Area Network (CAN)
network connected to the hardware.

Click **View pin map** on the block to open the Nucleo Pin Mapping
table.

Specify the **Data Format** and its properties using the block parameters
dialog box. Configure the properties of CAN
module in the Configuration Parameters.

**Note**

**CAN Write** block is currently supported only for STM32 Nucleo
H743ZI2.
