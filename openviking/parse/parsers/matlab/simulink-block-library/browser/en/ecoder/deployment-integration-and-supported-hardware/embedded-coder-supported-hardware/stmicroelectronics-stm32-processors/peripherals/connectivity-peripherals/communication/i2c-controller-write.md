---
type: simulink-block
title: 'I2C Controller Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'i2ccontrollerwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2ccontrollerwrite.html'
language: en
---

# I2C Controller Write

## Ports

### Input

### **Data** — Data to write to I2C peripheral device scalar | vector

The port writes data to the I2C device on the board.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### Output

### **Status** — Status of write operation scalar

The port outputs `0` for a successful write
operation.

#### Dependencies

To enable this port, select the **Output error
status** parameter.

**Data Types:** `uint8`

## Parameters

### **I2C module** — I2C module to write data `I2C1` (default) | `I2C2` | `I23C` | `...`

Specify the I2C module on the board to write data to the I2C peripheral
device.

### **Peripheral byte order** — Byte ordering that your I2C peripheral device supports `BigEndian` (default) | `LittleEndian`

The 2-byte ordering options are:

- BigEndian - The most significant byte is sent first over the
  I2C bus.
- LittleEndian - The least significant byte is sent first over
  the I2C bus.

### **Peripheral address via** — Peripheral address source of I2C `Dialog` (default) | `Inport`

Select the peripheral address source of I2C controller.

### **Peripheral address** — The I2C peripheral address to write data `10` (default)

Specify the I2C peripheral address to write the data. The I2C peripheral
device address is a 7-bit address.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example, ‘hex2dec(‘61’)’.

### **Enable register access address mode** — Option to write to a specific I2C peripheral register on (default) | off

When you select this parameter, the block writes data to the I2C
peripheral register that you specify in the **peripheral register
address** parameter.

When you clear this parameter, the **Send no
acknowledgment at the end of the transfer**
and **Remove stop bit at the end of data
transfer (Repeated start)** parameters are
displayed. Using these parameters, you can modify the
write operation according to your requirements.

### **Peripheral register address** — The I2C peripheral register address to write data `uint8(1)` (default)

Specify the I2C peripheral register address to write the data.

Specify this address in 8-bit unsigned integer or in hexadecimal format.
To specify the address in 8-bit unsigned integer, use
`uint8()`, for example, ‘uint8(20)’. To specify the
address in hexadecimal format, use `hex2dec()`, for
example, ‘hex2dec(‘20’)’.

For more information on register read/write, see I2C Register Read/Write.

#### Dependencies

This parameter appears only when you select **Enable register
access address mode** parameter.

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

### **Output error status** — Option to display the error status during data transmission off (default) | on

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

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

Not documented in R2025b.

## Description

Write data to I2C peripheral device or I2C peripheral device register

The I2C Controller Write block writes data to an I2C peripheral device
that is connected to the board. Using this block, you can write data to a specific
register on the I2C peripheral device. For more information on I2C communication, see
Support I2C Communication.

**Note**

You can run a Simulink® model containing I2C Controller Write block in
Connected IO mode on STM32 Processor based boards. For more information, see
Communicate with Hardware Using Connected IO.
