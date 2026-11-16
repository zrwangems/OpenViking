---
type: simulink-block
title: 'CAN Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32F7'
documentation_page: 'canreceive'
documentation_source_path: 'nucleo/ref/canreceive.html'
language: en
---

# CAN Receive

## Ports

### Output

### **Id** — CAN message identifier scalar

The port outputs CAN message identifier.

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint32`

### **Length** — CAN message length scalar

The port outputs the length of the received CAN message in bytes.

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

### **Data** — Message data `vector` | `scalar`

The block outputs data from the received CAN message. The maximum size of the data
is `[1x8]` of `uint8` format.

The number of bytes defined in the length signifies the valid data of the
output.

#### Dependencies

To enable this port, set **Output type** to
`Unpacked`.

**Data Types:** `uint8`

### **Status** — Status of received message scalar

The port outputs the message read status.

- The status is `1`, if the block receives new
  message.
- The status is `0`, if the block receives no new
  message.

#### Dependencies

To enable this port select the **Output Status**
parameter.

**Data Types:** `uint8`

### **Id Type** — CAN message identifier type scalar

The port outputs:

- `0` - if its 11-bit standard identifier
- `1` - if its 29-bit extended identifier

#### Dependencies

To enable this port, select the **Output Id Type**
parameter.

**Data Types:** `uint8`

### **Remote** — Output remote message scalar

The port outputs 1 if the received CAN message is a remote frame.

#### Dependencies

To enable this port select the **Output Remote**
parameter.

### **Msg** — CAN Message vector | scalar

The CAN receive block outputs the CAN received message in Simulink bus signal. To extract data from Simulink bus signal, connect it to CAN Unpack block. The CAN message received
from the bus will be stored in a FIFO.

#### Dependencies

To enable this port, set **Output type** to
`Packed`.

**Data Types:** `CAN Msg`

## Parameters

### **Module** — Module used for communication `1` (default) | `Any integer value`

CAN module which is used for communication.

**Note**

- CAN 0 Module on block represents CAN 1 peripheral on hardware.
- CAN 1 Module on block represents CAN 2 peripheral on hardware.

### **Output Type** — Message output type `unpacked` (default) | `packed`

The output type of the CAN Receive block is either `Packed` or
`Unpacked`.

In the Unpacked mode, the block outputs the different fields of unpacked CAN
message. In the unpacked mode, the CAN Receive block has `6 (Id, Id Type,
status, Length, Remote, Data)` output ports.

In the Packed mode, the block outputs a Simulink bus signal. To extract data from Simulink bus signal, connect it to the CAN Unpack block.

### **Read source** — CAN receive message source `FIFO 0` (default) | `FIFO 1`

The CAN Receive block outputs a CAN message from read source. You can set read
source filter configuration in the hardware configuration parameters.

### **Sample Time** — Time interval to read message -1 (default) | 0.1 | non-negative real value

Specify how often the block receives message, in seconds. When you specify this
parameter as `-1`, Simulink determines the best sample time for the block based on the block context
within the model.

### **Output Id Type** — Enable identifier type `off` (default) | `on`

When you select the **Output Id Type** parameter, the block
configures an output port, **Id Type**. The port outputs the standard
or extended message status.

#### Dependencies

To enable this parameter, set the **Output type** as
`unpacked`.

### **Output Remote** — Output remote status `off` (default) | `on`

When you select the **Output Remote** parameter, the block
configures an output port, **Remote**. The port outputs the message
remote frame status.

#### Dependencies

To enable this parameter, set the **Output type** as
`unpacked`.

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

Receive message from CAN network

The CAN Receive block receive messages from a Controller Area Network
(CAN) network connected to the hardware.

In the Unpacked mode, the block outputs different fields of unpacked CAN Messages.

In the Packed mode, the block outputs a Simulink® bus signal. To extract data from the Simulink bus signal, connect it to a CAN Unpack block.

The CAN Receive block receives messages from the CAN and delivers them to the Simulink model. It outputs a message at each time step, depending on the block
parameters. The CAN Receive block stores CAN messages received from the bus in a first-in,
first-out (FIFO). The FIFO delivers the messages to your model in the queued order at every
time step.

Configure the FIFO and other properties of CAN
module in the Configuration Parameters.

**Note**

- **CAN Receive** block is currently supported only for STM32
  Nucleo F767ZI processor.
- CAN 3 peripheral is not supported on the STM32 Nucleo F767ZI processor. Use only
  CAN 1 or CAN 2 peripheral.
