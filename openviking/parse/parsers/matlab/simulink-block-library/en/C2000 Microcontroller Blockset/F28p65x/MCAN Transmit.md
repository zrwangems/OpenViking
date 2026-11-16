---
type: simulink-block
title: 'MCAN Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F280015x'
documentation_page: 'mcantransmit'
documentation_source_path: 'ref/mcantransmit.html'
language: en
---

# MCAN Transmit

## Ports

### Input

### **TX** — Input data port vector | scalar

The block accepts messages in the `Raw data` or
`CAN Msg` format.

- `Raw data` – To accept the message as a
  `uint8` vector array, set the **Data
  format** as `Raw data`.
- `CAN Msg` – To accept the message in CAN message
  format, set the **Data format** as `CAN
  Msg`. You can create your messages using the CAN FD Pack
  block.

**Data Types:** `uint8` | `CAN Msg`
### Output

### **Status** — Status of CAN message transmission scalar

Output port to display the CAN message transmission status. The status port outputs:

- `0` - When CAN message is added to transmit
  FIFO/Queue
- `1` - When CAN message is not added to transmit to
  FIFO/Queue

#### Dependencies

To enable this port, select the **Output Status**
parameter.

## Parameters

### **Data format** — Data output type `Raw data` (default) | `CAN Msg`

Select a type to the write message to transmit FIFO or queue. This message is
later transmitted to CAN network connected to hardware.

- `Raw data` – To write message as a
  1-by-*N*
  `uint8` array, select **Data Format**  as
  `Raw data`.
- `CAN Msg` – To write message in CAN message format,
  select **Data Format** as `CAN Msg`
  and then perform these steps:

  1. Add a CAN FD Pack block from C2000™ Microcontroller Blockset/Target Communication library to your model.
  2. Connect the output of the CAN FD Pack block to the
     input of the **MCAN Transmit** block
  3. Using the options in the **Data to be input as** list
     of the CAN Pack block, specify if you want to create your
     messages or you want to upload a CAN database file. If you choose to
     upload a CAN database file, the CAN FD Pack block inherits
     the message properties from the uploaded file.

### **Frame format** — Frame format type `CAN-FD` (default) | `Classic CAN`

The CAN frame format.

#### Dependencies

To enable this parameter, set **Data Format** to
`Raw data`.

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The CAN message identifier type.

#### Dependencies

To enable this parameter, set **Data Format** to
`Raw data`.

### **Identifier** — Message identifier `100` (default) | `numeric identifier of length 11 or 29 bits`

Identifier, which is 11 bits long for the standard frame size or 29 bits long for
the extended frame size, specified in decimal, binary, or hex format. For binary and
hex formats, use `bin2dec(' ')` and `hex2dec(' ')`,
respectively, to convert the entry. The identifier is used to create CAN message
transmitted to the CAN bus.

#### Dependencies

To enable this parameter, set **Data Format** to
`Raw data`.

### **Length (bytes)** — Length of message `64` (default) | `positive integer less than or equal to 64(CAN-FD)` | `positive integer less than or equal to 8(Classic CAN)`

The length in bytes of data in the CAN message.

The length of message for the **Classic CAN** frame format is
between `0-8` bytes, and for the **CAN-FD** frame
format the range is between `0-64`. The blocks displays an error when
there is mismatch between the length of data at transmission port and the length you
specify here.

#### Dependencies

To enable this parameter, set **Data Format** to
`Raw data`.

### **Remote Frame** — Enable remote message `off` (default) | `on`

Select this parameter to configure the CAN message as a remote message. The data
at the input port is not considered for transmission.

#### Dependencies

To enable this parameter, set **Data format** to
`Raw data` and **Frame format** to
`Classic CAN`.

### **Enable bit rate switching** — Enable bit rate switch message `off` (default) | `on`

Select this parameter to configure the CAN message as a bit rate switch. The data
in the CAN message will be transmitted at the data rate you specify in the hardware
configuration parameter.

#### Dependencies

To enable this parameter, set **Data format** to
`Raw data` and **Frame format** to
`CAN-FD`.

### **Output Status** — Enable output status `off` (default) | `on`

When you select the **Output Status** parameter, the block
configures the **Status** of the port. The port outputs CAN message
transmission status.

## Libraries

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F28p65x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Send serial data to CAN bus

The MCAN Transmit block sends messages to a Controller Area Network
(CAN) connected to the hardware.

In the Raw data mode, the block accepts a 1-D array of type uint8. In the CAN msg mode,
the block accepts a Simulink® bus signal from CAN-FD Pack block.

**Note**

In MCAN Transmit block, if the transmit FIFO is full, then the data
is not transmitted.

Specify the **Data Format** and its properties using the block
parameters dialog box. Configure the properties of CAN module in the Configuration
Parameters. For more refer to Model Configuration Parameters for Texas Instruments C2000 Processors.
