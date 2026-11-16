---
type: simulink-block
title: 'CAN Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'canwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/canwrite.html'
language: en
---

# CAN Write

## Ports

### Input

### **Data** — Input data port scalar

The block accepts messages in `Raw` data format. To accept the
message as a uint8 array, set Data Format to `Raw data`.

#### Dependencies

To enable this port, set the **Data format** to
`Raw data`.

**Data Types:** `uint8`

### **Msg** — Input CAN message scalar

The block accepts messages in `CAN Message` format.

You can create your messages or you can upload a CAN database file to CAN Pack
block.

#### Dependencies

To enable this port, set the **Data format** to
`CAN Message`. Also, enable the output type as bus in
**CAN Pack** block

**Data Types:** `CAN Message`

### **Length** — CAN message length scalar

The port accepts the length of the CAN data to be transmitted in bytes.

#### Dependencies

To enable this parameter, set **Data format** to
`Raw data` and **Data length via** to
`Inport`.

**Data Types:** `uint8`

### **ID** — CAN message identifier scalar

The port accepts CAN message identifier. The ID can be:

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

**Data Types:** `uint32`
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

The port outputs the transmit FIFO fill level.

#### Dependencies

To enable this parameter, select **Output transmit FIFO
level** parameter.

## Parameters

### **Module** — Module used for communication `CAN1` (default) | `CAN2` | `CAN3`

Module to which the CAN device is connected.

### **Operation mode** — Select CAN read operation mode `Data` (default) | `sleep` | `Wakeup`

Select the CAN read operation mode.

- `Data` - Data to write CAN data/message
- `Sleep` - Select to set the CAN module in sleep mode. In
  Sleep operation mode, the block accepts a logical value to put the CAN peripheral
  in sleep mode.
- `Wakeup` - Select to wakeup the CAN module from sleep mode.
  In Wakeup operation mode, the block accepts a logical value to gets the CAN
  peripheral in wakeup state.

### **Data format** — Data output type `Unpacked` (default) | `Packed`

Select a output type to write message.

- `RAW data` – To write message as a N-by-1
  `uint8` array, select **Data format** as
  `Raw data`.
- `CAN Message` – To write message in CAN Message
  format, select **Data format** as `CAN Message`
  and using CAN pack and ensure to select the output type as bus.

### **Identifier type via** — Message identifier type `Dialog` (default) | `Inport`

Select the Identifier Type via `Dialog` or `input
port`.

- When you select Identifier Type via `inport`, the block
  configures an input port, `Id Type`.
- When you select Identifier Type via `Dialog`, the block accepts
  CAN identifier type via Dialog.

#### Dependencies

To enable this parameter, set the **Data format** as `Raw
data`.

### **Identifier type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The type of message identifier.

#### Dependencies

To enable this parameter, set the **Identifier type via** as
`Dialog`.

### **Identifier via** — Message identifier type `Inport` (default) | `Dialog`

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
`Raw data`.

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

### **Transmit remote frame** — Output remote message `off` (default) | `on`

The block sends a remote frame in the CAN message if this parameter is selected. The
data at the input port is not sent in the CAN message.

#### Dependencies

To enable this parameter, set the **Data Format** as
`Raw data`. For CAN Msg, the Remote Frame is inherited from the
request specified in the CAN Pack block.

### **Output receive FIFO fill level** — Enable receive FIFO fill level `off` (default) | `on`

When you select the **Output receive FIFO fill level** parameter,
the block configures an output port, **FIFO level**. The port outputs
the transmit FIFO message level.

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

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Write data to the CAN Bus

The CAN Write block writes messages to the Controller Area Network (CAN)
network connected to the hardware.

The CAN Write block accepts a CAN data that needs to be sent when operation
mode is set to `Data`. The block accepts a 1-D array of type
`uint8` when data format is set to `Raw data`.

The block accepts input as Simulink® bus signal when data format is set to `CAN Message`. To extract
data from Simulink bus signal, connect it to CAN pack block.

**Note**

When the length of data (input array) is different than the length (input scalar), the
number of data transmitted over the CAN module is minimum of length of data or input
length.

Select the Operation mode and its properties using the block parameters dialog box. Configure the properties of CAN
module in the Model Configuration Parameters for STM32 Processor Based Boards.
