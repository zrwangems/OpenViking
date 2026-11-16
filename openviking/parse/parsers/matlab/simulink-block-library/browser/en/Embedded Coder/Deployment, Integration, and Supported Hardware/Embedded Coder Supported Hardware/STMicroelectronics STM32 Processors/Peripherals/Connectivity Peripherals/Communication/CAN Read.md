---
type: simulink-block
title: 'CAN Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'canread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/canread.html'
language: en
---

# CAN Read

## Ports

### Output

### **Data** — Message data scalar

The block outputs messages in `uint8` or `CAN
Msg` format.

The maximum size of the data is [8x1] of uint8 format. The number of bytes defined
in the length signifies the valid data of the output.

- If **Output type** is set to
  `Unpacked`, the received message data is an 8-by-1
  array of type `uint8`.
- If **Output type** is set to
  `Packed`, the data port is renamed to **Msg** and the received message data is output as a
  Simulink bus signal.

This port outputs `0` if the received CAN message is a remote
frame.

**Data Types:** `uint8` | `CAN Msg`

### **Status** — Status of received message scalar

The port outputs message read status.

- `1` - Unsuccessful.
- `0` - Successful.

#### Dependencies

To enable this parameter, select **Output Status**
parameter.

**Data Types:** `uint8`

### **Length** — CAN message length scalar

The port outputs the length of the received CAN message in bytes.

#### Dependencies

To enable this parameter, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

### **Id** — CAN message identifier scalar

The port outputs CAN message identifier.

#### Dependencies

To enable this parameter, set **Output type** to
`Unpacked`.

**Data Types:** `uint32`

### **ID Type** — CAN message identifier type scalar

The port outputs CAN message identifier type

- `0` - if its 11-bit standard identifier
- `1` - if its 29-bit standard identifier

#### Dependencies

To enable this parameter, set **Output type** to
`Unpacked`.

**Data Types:** `uint32`

### **Remote** — Remote message flag scalar

Remote message flag. The port outputs `1` if the received CAN
message is a remote frame.

#### Dependencies

To enable this parameter, select **Output remote**
parameter.

### **FIFO Level** — FIFO fill level scalar

The port outputs the received FIFO fill level.

The FIFO level provides the RX FIFO level after reading the message. TX FIFO
provides how much of TX FIFO is empty.

#### Dependencies

To enable this parameter, select **Output receive FIFO
level** parameter.

## Parameters

### **Module** — Module used for communication `CAN1` (default) | `CAN2` | `CAN3`

Module to which the CAN device is connected.

### **Operation mode** — Select CAN read operation mode `Data` (default) | `Read sleep status` | `Read last error code`

Select the CAN read operation mode.

- `Data` - Data to read CAN message
- `Read sleep status` - Read the sleep status of CAN module. In
  Read sleep status operation mode, the block outputs a logical status if the CAN
  peripheral is in sleep mode.
- `Read last error code` - Provides the status set by hardware
  for last message sent or received on CAN bus.

  The following are the error codes and there respective status.

  - `000` - No Error
  - `001` - Stuff Error
  - `010` - Form Error
  - `011` - Acknowledgment Error
  - `100` - Bit recessive Error
  - `101` - Bit dominant Error
  - `110` - CRC Error
  - `111` - Set by software

### **Output type** — Data output type `Unpacked` (default) | `Packed`

Select an output type to read message.

- `Unpacked` – In Unpacked output type, the block
  outputs values received as [8x1] array of type uint8. In unpacked type for the CAN
  Read block, you can enable all the output ports(ID, ID type, Data, Status, Remote,
  Length, FIFO level).
- `Packed` – In Packed output type, the block outputs
  Simulink bus signal.

### **Read source** — CAN message read source `FIFO 0` (default) | `FIFO 1`

The CAN Read block outputs a CAN message from read source. You can configure read
source filter configuration in the configuration parameters.

### **Output Identifier Type** — Enable identifier type `off` (default) | `on`

When you select the Output Identifier Type parameter, the block configures an output
port, `Id Type`. The port outputs the standard or extended message
status.

#### Dependencies

To enable this parameter, set the **Output type** as
`unpacked`.

### **Output Remote** — Enable remote messages `off` (default) | `on`

When you select the **Output Remote** parameter, the block
configures an output port, **Remote**. The port outputs the message
remote frame status.

#### Dependencies

To enable this parameter, set the **Output type** as
`unpacked`.

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

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Read message from CAN network

The CAN Read block reads messages from a Controller Area Network (CAN)
network connected to the hardware.

The CAN Read block outputs a CAN data when operation mode is set to
`Data`. The block outputs values received as `[8x1]` array
of type `uint8` when output type is set to
`Unpacked`.

The block outputs Simulink® bus signal when output type is set to `Packed`. To extract data
from Simulink bus signal, connect it to CAN Unpack block. The CAN Unpack block
is available from the Vehicle Network Toolbox™.

Select the Operation mode and its properties using the block parameters dialog box. Configure the properties of CAN
module in the Model Configuration Parameters for STM32 Processor Based Boards.
