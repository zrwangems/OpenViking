---
type: simulink-block
title: 'CAN Transmit'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32F7'
documentation_page: 'cantransmit'
documentation_source_path: 'nucleo/ref/cantransmit.html'
language: en
---

# CAN Transmit

## Ports

### Input

### **Data** — Input data port vector | scalar

The block accepts messages in `Raw data` format.

To accept the message as a `uint8` vector array, set
**Data Format** as `Raw data`.

#### Dependencies

To enable this port, set the **Data Format** to
`Raw data`.

**Data Types:** `uint8`

### **Msg** — Input CAN message vector | scalar

The block accepts messages in `CAN Message`
format.

You can create your messages or you can upload a CAN database file to CAN Pack
block.

#### Dependencies

To enable this port, set the **Data Format** to
`CAN Message`.

**Data Types:** `CAN Msg`
### Output

### **Status** — Status of data transmission scalar

Output port to display the status of data transmission.

- `1` - data transmission is successful
- `0` - data transmission is unsuccessful

#### Dependencies

To enable this port, select the **Output Status**
parameter.

## Parameters

### **Module** — Module used for communication `1` (default) | `Any integer value`

CAN module which is used for communication.

**Note**

- CAN 0 Module on block represents CAN 1 peripheral on hardware.
- CAN 1 Module on block represents CAN 2 peripheral on hardware.

### **Data Format** — Data output type `Raw data` (default) | `CAN Msg`

Select a type to transmit message.

- `Raw data` – To transmit message as a
  1-by-*N*
  `uint8` array, select **Data Format**  as
  `Raw data`.
- `CAN Msg` – To transmit message in CAN message
  format, select **Data Format** as `CAN
  Msg` and then perform these steps:

  1. Add a CAN pack block to your model.
  2. Connect the output of the CAN Receive pack block to the
     input of the **CAN Transmit** block
  3. Using the options in the **Data to be input as** list
     of the CAN Pack block, specify if you want to create your
     messages or you want to upload a CAN database file. If you choose to upload
     a CAN database file, the CAN Pack inherits the message
     properties from the uploaded file.

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The type of message identifier.

#### Dependencies

To enable this parameter, set the **Data Format** as
`Raw data`.

### **Identifier** — Message identifier 100 (default) | numeric identifier of length 11 or 29 bits

Identifier, which is 11 bits long for the standard frame size or 29 bits long for
the extended frame size, specified in decimal, binary, or hex. For binary and hex
formats, use `bin2dec(' ')` and `hex2dec(' ')`,
respectively, to convert the entry. The identifier is coded into a message that is sent
to the CAN bus.

#### Dependencies

To enable this parameter, set the **Data Format** as
`Raw data`. To output the identifier of the
`CAN Msg`, select **Output identifier** of
the CAN Unpack block.

### **Length (bytes)** — Length of message 8 (default) | positive integer less than or equal to 8

The length of the message, in bytes.

#### Dependencies

To enable this parameter, set the **Data Format** as
`Raw data`. To output the length of the `CAN
Msg`, select **Output length** of the CAN
Unpack block.

### **Transmit Remote Frame** — Output remote message `off` (default) | `on`

The block sends a remote frame in the CAN message if this parameter is selected. The
data at the input port is not sent in the CAN message.

#### Dependencies

To enable this parameter, set the **Data Format** as
`Raw data`. For CAN Msg, the Remote Frame is inherited from
the request specified in the CAN Pack block.

### **Output Status** — Enable output status `off` (default) | `on`

When you select the **Output Status** parameter, the block
configures an output port, **Status**. The port outputs the status of
CAN message.

## Libraries

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Transmit message to CAN network

The CAN Transmit block transmits message to a Controller Area Network
(CAN) network connected to the hardware.

Configure the FIFO and other properties of CAN
module in the Configuration Parameters.

**Note**

**CAN Transmit** block is currently supported only for STM32 Nucleo
F767ZI processor.
