---
type: simulink-block
title: 'I2C Controller Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'i2ccontrollerread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2ccontrollerread.html'
language: en
---

# I2C Controller Read

## Ports

### Output

### **Data** — Data from I2C peripheral device vector

The port reads vector data from an I2C device on the board. The size
of the data is the value that you specify in the **Data
size** parameter.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — Status of read operation scalar

The port outputs the status of each read request as mentioned in the
following table:

**Return status codes**

| **Status** | Description |
| --- | --- |
| `0` | SUCCESS |
| `1` | BUSY |
| `2` | ARBITRATION\_LOST |
| `4` | NO\_ACKNOWLEDGE |
| `8` | BUS\_ERROR |
| `16` | BUS\_NOT\_IN\_USE |

#### Dependencies

To enable this port, select the **Output error
status** parameter.

**Data Types:** `uint8`

## Parameters

### **I2C module** — I2C module to read data `I2C1` (default) | `I2C2` | `I23C` | `...`

Specify the I2C module on the board to read data from the I2C peripheral
device.

### **Peripheral byte order** — Byte ordering that your I2C peripheral device supports `BigEndian` (default) | `LittleEndian`

The 2-byte ordering options are:

- BigEndian - The most significant byte is sent first over the I2C
  bus.
- LittleEndian - The least significant byte is sent first over the
  I2C bus.

### **Peripheral address via** — Peripheral address source of I2C `Dialog` (default) | `Inport`

Select the peripheral address source of I2C controller.

### **Peripheral address** — The I2C register peripheral address from which to read data `10` (default) | `integer greater than or equal to 0`

Specify the I2C peripheral address to read the data. You can specify this
address in hexadecimal format `hex2dec()`, for example,
‘hex2dec(‘20’)’.

### **Enable register access address mode** — Option to read from a specific I2C peripheral register on (default) | off

When you select this parameter, the block reads data from the I2C
peripheral register that you specify in the **peripheral register
address** parameter.

When you clear this parameter, the **Send no
acknowledgment at the end of the transfer**
and **Remove stop bit at the end of data
transfer (Repeated start)** parameters are
displayed. Using these parameters, you can modify the
read operation according to your requirements.

### **Register address via** — Peripheral register address source of I2C `Dialog` (default) | `Inport`

Select the register address source of I2C controller.

#### Dependencies

To enable this parameter, select **Enable register access
address mode** parameter.

### **Peripheral register address** — The I2C peripheral register address to read data `0` (default) | `integer between 0 and 255`

Specify the I2C register address to read the data.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example, ‘hex2dec(‘20’)’.

For more information on register read/write, see I2C Register Read/Write.

#### Dependencies

To enable this parameter, select **Enable register access
address mode** parameter.

### **Data type** — Data type of data from the I2C peripheral device `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

Select the data type in which you want to read from the I2C peripheral
device.

### **Data size (N)** — Data size to read from the I2C peripheral device `1` (default) | `integer greater than or equal to 0`

Specify the data size that you want to read from the I2C peripheral device
for the selected data type.

### **Remove stop bit at the end of data transfer (Repeated start)** — Option to remove STOP bit at the end of data transfer off (default) | on

When the parameter is not selected, the block sends a STOP condition. This
condition indicates that the block has terminated the data transmission and
that the I2C bus is free for any other I2C Controller block to initiate the
new read/write operation.

When you select this parameter, the block sends another START condition
followed by an address and read/write bit. The block sends any number of
start conditions recursively. Such a repeated START condition allows write
operations to the peripheral devices without releasing the bus. No other
Controller block interrupts the operation.

#### Dependencies

To enable this parameter, deselect the **Enable register
access address mode** parameter.

### **Send no acknowledgment at the end of the transfer** — Option to send Not Acknowledge bit at the end of data transfer off (default) | on

When you select this parameter, the I2C
Controller Read block sends a NACK (Not
Acknowledge) bit to the peripheral device with the final
byte.

When the peripheral device receives the NACK, it waits
for a STOP condition from the I2C Controller block. The
controller block generates either a STOP condition to
abort the transfer or a repeated START condition to
start a new transfer.

When you deselect this parameter, the I2C
Controller Read block sends an ACK
(Acknowledge) bit to the peripheral device at the end of
every byte. The ACK indicates that the I2C
Controller Read block is ready to read the
next byte from the peripheral device.

#### Dependencies

To enable this parameter, deselect the
**Enable register access address
mode** parameter.

### **Output error status** — Option to display error status during data transmission off (default) | on

When you select this parameter, the block configures an output port. The
port on the block is labeled as `Status`, indicating that
the block outputs the status of the write operation at the output
port.

The block outputs the status as a `uint8` value. Each
value corresponds to a data transfer status.

| Status value | Status description |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `I2C_BUS_ERROR` |

### **Sample time** — Frequency to read data from the I2C peripheral device `-1` (default)

Specify how often the I2C Controller Read block reads data
from the I2C peripheral device. When you specify this parameter
as`-1`, the block inherits its sample time based on the
context of the block within the model.

### **Timeout** — Specify waiting time to complete read operation `0.001` (default)

You configure `Timeout` to be the maximum time (in
seconds) to wait to complete a read operation.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

Not documented in R2025b.

## Description

Read data from I2C peripheral device or I2C peripheral device register

The I2C Controller Read block reads serial data from an I2C peripheral
device that is connected to the board. Using this block, you can read data from a
specific register on the I2C peripheral device. For more information on I2C
communication, see Support I2C Communication.

**Note**

You can run a Simulink® model containing I2C Controller Read block in
Connected IO mode on STM32 Processor based boards. For more information, see
Communicate with Hardware Using Connected IO.
