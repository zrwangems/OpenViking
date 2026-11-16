---
type: simulink-block
title: 'FDCAN Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'fdcanwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/fdcanwrite.html'
language: en
---

# FDCAN Write

## Ports

### Input

### **Data** — Input data port vector | scalar

The block accepts messages in `Raw` data format. To accept the
message as a uint8 vector array, set Data Format to `Raw
data`.

#### Dependencies

To enable this port, set the **Data format** to
`Raw data`.

**Data Types:** `uint8`

### **Msg** — Input FDCAN message vector | scalar

The block accepts messages in `CAN Message` format.

You can create your messages or you can upload a CAN database file to FDCAN Pack
block.

#### Dependencies

To enable this port, set the **Data format** to
`CAN Message`.

**Data Types:** `CAN Message`

### **Length** — CAN message length scalar

The port accepts the length of the received CAN message in bytes.

#### Dependencies

To enable this parameter, set **Data format** to
`Raw data` and **Data length via** to
`Inport`.

**Data Types:** `uint8`

### **ID** — FDCAN message identifier scalar

The port accepts FDCAN message identifier. The ID can be:

- `0-2047`: for Standard (11-bit identifier)
- `0-536870911`: for Extended (29-bit identifier)

#### Dependencies

To enable this parameter, set **Data format** to
`Raw data` and **Identifier via** to
`Inport`.

**Data Types:** `uint32`

### **ID Type** — CAN message identifier type scalar

The port accepts CAN message identifier type

- `0` - if its 11-bit standard identifier
- `1 or any value other than 0` - if its 29-bit standard
  identifier

#### Dependencies

To enable this parameter, set **Data format** to
`Raw data` and **Identifier type via** to
`Inport`.

**Data Types:** `uint8`

### **Sleep** — FDCAN in sleep state scalar

The port accepts a logical value to put the FDCAN peripheral in sleep mode.

#### Dependencies

To enable this port, set **Operation mode** to
`sleep`.

**Data Types:** `uint8`

### **Wakeup** — FDCAN in wakeup state scalar

The port accepts a logical value to put the FDCAN peripheral in wakeup
mode.

#### Dependencies

To enable this port, set **Operation mode** to
`wakeup`.

**Data Types:** `uint8`

### **Restricted Mode** — FDCAN in restricted mode scalar

The port accepts a logical value to put the FDCAN peripheral in restricted
mode.

#### Dependencies

To enable this port, set **Operation mode** to
`Exit restricted operation mode`.

**Data Types:** `uint8`
### Output

### **Status** — Status of received message scalar

The port outputs message read status.

- The status is `0`, if the block reads new message.
- The status is `1`, if the block reads no new
  message.

#### Dependencies

To enable this port, select **Output Status**
parameter.

**Data Types:** `uint8`

### **FIFO Level** — FIFO fill level scalar

The port outputs the received FIFO fill level.

#### Dependencies

To enable this parameter, select **Output transmit FIFO
level** parameter.

## Parameters

### **Module** — Module used for communication `FDCAN1` (default) | `FDCAN2` | `FDCAN3`

Module to which the FDCAN device is connected.

### **Operation mode** — Select FDCAN read operation mode `Data` (default) | `sleep` | `Wakeup` | `Exit restricted operation mode`

Select the FDCAN read operation mode.

- `Data` - Data to write FDCAN data/message
- `Sleep` - Select to set the FDCAN module in sleep mode. In
  Sleep operation mode, the block accepts a logical value to put the FDCAN
  peripheral in sleep mode. When you set operation mode to sleep, it enables the
  input port `Sleep`.
- `Wakeup` - Select to wakeup the FDCAN module from sleep mode.
  In Wakeup operation mode, the block accepts a logical value to gets the FDCAN
  peripheral in wakeup state. When you set operation mode to wakeup, it enables the
  input port `Wakeup`.
- `Exit restricted operation mode` - Select to exit the FDCAN
  module from restricted mode. In Exit restricted operation mode, the block accepts
  a logical value to exit the FDCAN peripheral from restricted operation mode. When
  you set operation mode to exit restricted operation mode, it enables the input
  port `Restricted Mode`.

### **Data format** — Data output type `Unpacked` (default) | `Packed`

Select an output type to write message.

- `RAW data` – To write message as a 8-by-1
  `uint8` array, select **Data format** as
  `Raw data`.
- `CAN Message` – To write message in CAN Message
  format, select **Data format** as `CAN
  Message`.

### **Frame format** — Frame format type `CAN-FD` (default) | `CAN`

Select an output type to write message.

- `RAW data` – To write message as a 8-by-1
  `uint8` array, select **Data format** as
  `Raw data`.
- `CAN Message` – To write message in CAN Message
  format, select **Data format** as `CAN
  Message`.

### **Identifier type via** — Message identifier type `Dialog` (default) | `Inport`

Select the Identifier Type via `Dialog` or `input
port`.

- When you select Identifier Type via `inport`, the block
  configures an input port, `Id Type`.
- When you select Identifier Type via `Dialog`, the block accepts
  CAN message.

#### Dependencies

To enable this parameter, set the **Data format** as `Raw
data`.

### **Identifier type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The type of message identifier.

#### Dependencies

To enable this parameter, set the **Identifier type via** as
`Dialog`.

### **Identifier via** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The type of message identifier.

- `0-2047`: for Standard (11-bit identifier)
- `0-536870911`: for Extended (29-bit identifier)

#### Dependencies

To enable this parameter, set the **Data format** as `Raw
data`.

### **Identifier** — Message identifier `100` (default) | `numeric identifier of length 11 or 29 bits`

Identifier, which is 11 bits long for the standard frame size or 29 bits long for
the extended frame size, specified in decimal, binary, or hex. For binary and hex
formats, use bin2dec(' ') and hex2dec(' '), respectively, to convert the entry. The
identifier is coded into a message that is sent to the CAN bus.

#### Dependencies

To enable this parameter, set the **Data Format** as
`Raw data`. To output the identifier of the `CAN
Msg`, select **Output identifier** of the CAN
Unpack block.

### **Data length via** — Enable remote messages `Inport` (default) | `Dialog`

Select the **Data length via** Inport or Dialog.

- When you select Data length via `inport`, the block
  configures an input port, `Length`.
- When you select Data length via `Dialog`, the block accepts
  specified input data size.

#### Dependencies

To enable this parameter, set the **Data format** as `Raw
data`.

### **Length (bytes)** — Length in bytes `8` (default) | `1-8`

The length of the message, in bytes provided via input.

#### Dependencies

To enable this parameter, set the **Data length via** as
`Dialog`.

### **Enable bitrate switching** — FDCAN bitrate switching `off` (default) | `on`

Select this parameter to enable bitrate switching.

#### Dependencies

To enable this parameter, set the **Data Format** as
`Raw data`, **Operation mode** as
`Data` and **Frame format** as
`CAN-FD`.

### **Transmit remote frame** — Output remote message `off` (default) | `on`

The block sends a remote frame in the CAN message if this parameter is selected. The
data at the input port is not sent in the CAN message.

#### Dependencies

To enable this parameter, set the **Data Format** as
`Raw data` and **Frame format** as
`CAN`. For CAN Msg, the Remote Frame is inherited from the request
specified in the CAN Pack block.

### **Output receive FIFO fill level** — Enable receive FIFO fill level `off` (default) | `on`

When you select the **Output receive FIFO fill level** parameter,
the block configures an output port, **FIFO level**. The port outputs
the received FIFO message level.

### **Output Status** — Enable output status `off` (default) | `on`

When you select the **Output Status** parameter, the block
configures an output port, **Status**. The port outputs the status
message.

### **Sample Time** — Time interval to read message `-1` (default) | `0.1` | `non-negative real value`

Specify how often the block receives message, in seconds. When you specify this
parameter as `-1`, Simulink determines the best sample time for the block based on the block context
within the model.

### **Timeout** — Specify waiting time to complete read operation `0.001` (default) | 0.1 | non-negative real value

Specify the time in seconds to block the CAN read. For nonblocking, set to
`0`. You configure Timeout to be the maximum time (in seconds) to
wait to complete a read operation.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Write data to the FDCAN Bus

The FDCAN Write block writes messages to the Controller Area Network (CAN)
network connected to the hardware.

The FDCAN Write block accepts a CAN data that needs to be sent when
operation mode is set to `Data`. The block accepts a 1-D array of type
`uint8` when data format is set to `Raw data`.

The block accepts input as Simulink® bus signal when data format is set to `CAN Message`. To extract
data from Simulink bus signal, connect it to FDCAN pack block.

Select the Operation mode and its properties using the block parameters dialog box. Configure the properties of FDCAN module in the configuration parameters.
