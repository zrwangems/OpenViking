---
type: simulink-block
title: 'I2C Controller Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Communication'
documentation_page: 'i2ccontrollerwriteblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2ccontrollerwriteblock.html'
language: en
---

# I2C Controller Write

## Ports

### Input

### **Data** — Data to write to the I2C peripheral devices scalar | vector

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### Output

### **Status** — Status of the write operation scalar

When you select the **Output error status**
parameter, an output port, labeled as `Status`, becomes
available.

The port outputs `0` for a successful write
operation.

**Data Types:** `uint8`

## Parameters

### **I2C module** — I2C module to write data `0` (default) | `integer greater than or equal to 0`

Specify the I2C module on the board to write data to the I2C peripheral
devices.

### **Peripheral address** — The I2C peripheral address to write data `hex2dec('48')` (default)

Specify the I2C peripheral address to write the data. The I2C peripheral
devices address is a 7-bit address.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example, ‘hex2dec(‘61’)’.

### **Peripheral byte order** — Byte ordering that your I2C peripheral devices supports `BigEndian` (default) | `LittleEndian`

The 2-byte ordering options are:

- BigEndian - The most significant byte is sent first over the
  I2C bus.
- LittleEndian - The least significant byte is sent first over
  the I2C bus.

### **Enable register access** — Option to write to a specific I2C peripheral register on (default) | off

When you select this parameter, the block writes data to the I2C
peripheral register that you specify in the **Peripheral register
address** parameter.

When you clear this parameter, the **Send NACK at the end of data
transfer** and **Remove stop bit at the end of data
transfer**  parameters are displayed. Using these parameters,
you can modify the write operation according to your requirements.

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
access** parameter.

### **Send NACK at the end of data transfer** — Option to send Not Acknowledge bit at the end of data transfer off (default) | on

When you select this parameter, the I2C Controller Write
block sends a NACK (Not Acknowledge) bit to the peripheral devices with the
final byte.

When the peripheral devices receives the NACK, it waits for a STOP
condition from the I2C controller block. The controller block generates
either a STOP condition to abort the transfer or a repeated START condition
to start a new transfer.

When you clear this parameter, the I2C Controller Write
block sends an ACK (Acknowledge) bit to the peripheral devices at the end of
every byte. The ACK indicates that the I2C Controller Write
block is ready to read the next byte from the peripheral devices.

#### Dependencies

This parameter appears only when you clear **Enable register
access** parameter.

### **Remove stop bit at the end of data transfer** — Option to remove STOP bit at the end of data transfer off (default) | on

When you clear this parameter, the block sends a STOP condition. This
condition indicates that the block has terminated the data transmission and
the I2C bus is free for any other I2C controller block to initiate the
read/write operation.

When you select this parameter, the block sends another START condition
followed by an address and read/write bit. The block sends any number of
start conditions recursively. Such a repeated START condition allows write
operations to the peripheral devices without releasing the bus. No other
controller block interrupts the operation.

#### Dependencies

This parameter appears only when you clear **Enable register
access** parameter.

### **Output error status** — Option to display the error status during data transmission off (default) | on

When you select this parameter, an output port, labeled as
`Status`, becomes available.

The port outputs `0` for a successful write
operation.

## Libraries

Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F746G-Discovery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Write data to I2C peripheral devices or I2C peripheral devices register

The I2C Controller Write block writes data to an I2C peripheral devices
that is connected to the board. Using this block, you can write data to a specific
register on the I2C peripheral devices.

For more information on I2C communication, see Support I2C Communication.
