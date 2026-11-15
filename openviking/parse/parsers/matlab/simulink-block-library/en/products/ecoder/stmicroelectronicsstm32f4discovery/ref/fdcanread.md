---
type: simulink-block
title: 'FDCAN Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'fdcanread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/fdcanread.html'
language: en
---

# FDCAN Read

## Ports

### Output

### **Data** — Message data vector | scalar

The block outputs messages in `uint8` or `CAN
Msg` format.

The maximum size of the data is [64x1] of uint8 format. The number of bytes
defined in the length signifies the valid data of the output.

- If **Output type** is set to
  `Unpacked`, the received message data is an 64-by-1
  array of type `uint8`.
- If **Output type** is set to
  `Packed`, the data port is renamed to **Msg** and the received message data is output as a
  Simulink bus signal.

This port outputs `0` if the received CAN message is a remote
frame.

**Data Types:** `uint8` | `CAN Msg`

### **Restricted Mode** — Status of restricted message scalar

The port outputs FDCAN module status.

- The status is `1`, if FDCAN module in
  restricted operation mode.
- The status is `0`, if FDCAN module is not in restricted
  operation mode.

#### Dependencies

To enable this parameter, set operation mode to **Read
restricted operation mode status**.

**Data Types:** `uint8`

### **Status** — Status of received message scalar

The port outputs message read status.

- The status is `0`, if the block reads new message.
- The status is `1`, if the block reads no new
  message.

#### Dependencies

To enable this parameter, select **Output Status**
parameter.

**Data Types:** `uint8`

### **Sleep** — Status of FDCAN module scalar

The port outputs FDCAN module status.

- The status is `1`, if FDCAN module in sleep mode.
- The status is `0`, if FDCAN module is not in sleep
  mode.

#### Dependencies

To enable this parameter, set operation mode to **Read
sleep status**.

**Data Types:** `uint8`

### **Msg** — Status of received message scalar

The CAN receive block outputs the CAN received message in Simulink bus signal. To extract data from Simulink bus signal, connect it to CAN FD Unpack block.

The port outputs message read status.

- The status is `1`, if the message read is not
  successful
- The status is `0`, if the message read is
  successful.

#### Dependencies

To enable this parameter, set **Output type** to
`Packed`.

**Data Types:** `CAN Msg`

### **Length** — CAN message length scalar

The port outputs the length of the received CAN message in bytes.

#### Dependencies

To enable this parameter, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

### **ID** — CAN message identifier scalar

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

### **Frame Type** — Frame type message scalar

Frame type output message. The port outputs `1`, if it receives
FDCAN message frame and `0`, if it receives Classic message
frame.

#### Dependencies

To enable this parameter, select **Output frame
type** parameter.

**Data Types:** `uint8`

### **Bitrate Switching** — Bitrate switching message scalar

Bitrate switching output message.

- `0` - when CAN FD frames are transmitted without bit rate
  switching.
- `1` - when CAN FD frames are transmitted with bit rate
  switching.

#### Dependencies

To enable this parameter, select **Output bitrate
switching** parameter.

**Data Types:** `uint8`

### **FIFO Level** — FIFO fill level scalar

The port outputs the received FIFO fill level.

#### Dependencies

To enable this parameter, select **Output receive FIFO
level** parameter.

## Parameters

### **Module** — Module used for communication `FDCAN1` (default) | `FDCAN2` | `FDCAN3`

Module to which the FDCAN device is connected.

### **Operation mode** — Select FDCAN read operation mode `Data` (default) | `Read sleep status` | `Read restricted operation mode status` | `Read last error code`

Select the CAN read operation mode.

- `Data` - Data to read FDCAN data/message
- `Read sleep status` - Read the sleep/power status of FDCAN
  module. In Read sleep status operation mode, the block outputs a logical status if
  the FDCAN peripheral is in sleep mode.

  In this operation mode, the block configures an output port
  `Sleep`.
- `Read restricted operation mode status` - To read if the CAN
  module is in restricted mode. In `Read restricted operation mode
  status` operation mode, the block outputs a logical status if the FDCAN
  peripheral in restricted operation mode.

  In this operation mode, the block configures an output port
  `Restricted mode`.
- `Read last error code` - Provides the status set by hardware
  for last message sent or received on CAN bus. In Read last error code operation
  mode, the block outputs a logical status if the CAN peripheral is in wakeup
  state.

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
  outputs values received as [8x1] array of type uint8. In unpacked type for the
  FDCAN Read block, you can enable all the output ports(ID, ID type, Data, Status,
  Remote, Frame type, bitrate switching, Length, FIFO level).
- `Packed` – In Packed output type, the block outputs
  Simulink bus signal. To extract data from Simulink bus signal, connect it to CAN
  Unpack block.

### **Read source** — FDCAN message read source `FIFO 0` (default) | `FIFO 1` | `Buffers`

The CAN Read block outputs a CAN message from read source. You can configure read
source filter configuration in the configuration parameters.

### **Buffer number** — Specify buffer number `0` (default) |

Specify the FDCAN Read block buffer number.

#### Dependencies

To enable this parameter, set the **read source** to
`Buffers`.

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

### **Output frame type** — Enable frame type messages `off` (default) | `on`

When you select the **Output Remote** parameter, the block
configures an output port, **Frame Type**. The port outputs the
`0` (Classic) or `1` (FD) message status.

#### Dependencies

To enable this parameter, set the **Output type** as
`unpacked`.

### **Output bit rate switching** — Enable bit rate switch `off` (default) | `on`

When you select the **Output bit rate switching** parameter, the
block configures an output port, **Bitrate switching**. The port
outputs the `0` (disabled) or `1` (enabled) message
status.

#### Dependencies

To enable this parameter, set the **Output type** as
`unpacked`.

### **Output receive FIFO fill level** — Enable receive FIFO fill level `off` (default) | `on`

When you select the **Output receive FIFO fill level** parameter,
the block configures an output port, **FIFO level**. The port outputs
the received FIFO level message.

### **Output Status** — Enable output status `off` (default) | `on`

When you select the **Output Status** parameter, the block
configures an output port, **Status**. The port outputs the status
message.

### **Sample Time** — Time interval to read message `-1` (default) | `0.1` | `non-negative real value`

Specify how often the block receives message, in seconds. When you specify this
parameter as `-1`, Simulink determines the best sample time for the block based on the block context
within the model.

### **Timeout** — Specify waiting time to complete read operation `0.001` (default) | 0.1 | non-negative real value

Specify the time in seconds to block the FDCAN read. For nonblocking, set to
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

Read data from CAN FD Bus

The FDCAN Read block reads messages from a Controller Area Network (CAN)
network connected to the hardware.

The FDCAN Read block outputs a CAN data when operation mode is set to
`Data`. The block outputs values received as `[64x1]`
array of type `uint8` when output type is set to
`Unpacked`.

The block outputs Simulink® bus signal when output type is set to `Packed`. To extract data
from Simulink bus signal, connect it to CAN FD Unpack block.

Select the Operation mode and its properties using the block parameters dialog box. Configure the properties of FDCAN module in the configuration parameters.
