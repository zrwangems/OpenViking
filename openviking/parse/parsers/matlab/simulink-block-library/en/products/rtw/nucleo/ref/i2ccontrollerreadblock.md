---
type: simulink-block
title: 'I2C Controller Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'i2ccontrollerreadblock'
documentation_source_path: 'nucleo/ref/i2ccontrollerreadblock.html'
language: en
---

# I2C Controller Read

## Ports

### Output

### **Data** — Data from the I2C Peripheral devices vector

The port reads vector data from an I2C device on the board. The size
of the data is the value that you specify in the **Data
size** parameter.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — Status of the read operation scalar

When you select the **Output error status**
parameter, an output port, labeled as `Status`, becomes
available.

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

**Data Types:** `uint8`

## Parameters

### **I2C module** — I2C module to read data `0` (default)

Specify the I2C module on the board to read data from the I2C Peripheral
devices.

### **Peripheral address** — The I2C register Peripheral address from which to read data `10` (default) | `integer greater than or equal to 0`

Specify the I2C Peripheral address to read the data. You can specify this
address in hexadecimal format `hex2dec()`, for example,
‘hex2dec(‘20’)’.

### **Peripheral byte order** — Byte ordering that your I2C Peripheral devices supports `BigEndian` (default) | `LittleEndian`

The 2-byte ordering options are:

- BigEndian - The most significant byte is sent first over the I2C
  bus.
- LittleEndian - The least significant byte is sent first over the
  I2C bus.

### **Enable register access** — Option to read from a specific I2C Peripheral register on (default) | off

When you select this parameter, the block reads data from the I2C
Peripheral register that you specify in the **Peripheral register
address** parameter.

When you clear this parameter, the **Send NACK at the end of data
transfer** and **Remove stop bit at the end of data
transfer**  parameters are displayed. Using these parameters,
you can modify the read operation according to your requirements.

### **Peripheral register address** — The I2C Peripheral register address to read data `0` (default) | `integer between 0 and 255`

Specify the I2C register address to read the data.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example, ‘hex2dec(‘20’)’.

For more information on register read/write, see I2C Register Read/Write.

#### Dependencies

This parameter appears only when you select **Enable register
access** parameter.

### **Data type** — Data type of data from the I2C Peripheral devices `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

Select the data type in which you want to read from the I2C Peripheral
devices.

### **Data size (N)** — Data size to read from the I2C Peripheral devices `1` (default) | `integer greater than or equal to 0`

Specify the data size that you want to read from the I2C Peripheral
devices for the selected data type.

### **Send NACK at the end of data transfer** — Option to send Not Acknowledge bit at the end of data transfer off (default) | on

When you select this parameter, the I2C Controller Read
block sends a NACK (Not Acknowledge) bit to the Peripheral devices with the
final byte.

When the Peripheral devices receives the NACK, it waits for a STOP
condition from the I2C Controller block. The Controller block generates
either a STOP condition to abort the transfer or a repeated START condition
to start a new transfer.

When you clear this parameter, the I2C Controller Read
block sends an ACK (Acknowledge) bit to the Peripheral devices at the end of
every byte. The ACK indicates that the I2C Controller Read
block is ready to read the next byte from the Peripheral devices.

#### Dependencies

This parameter appears only when you clear **Enable register
access** parameter.

### **Remove stop bit at the end of data transfer** — Option to remove STOP bit at the end of data transfer off (default) | on

When you clear this parameter, the block sends a STOP condition. This
condition indicates that the block has terminated the data transmission and
that the I2C bus is free for any other I2C Controller block to initiate the
new read/write operation.

When you select this parameter, the block sends another START condition
followed by an address and read/write bit. The block sends any number of
start conditions recursively. Such a repeated START condition allows write
operations to the Peripheral devices without releasing the bus. No other
Controller block interrupts the operation.

#### Dependencies

This parameter appears only when you clear **Enable register
access** parameter.

### **Output error status** — Option to display the error status during data transmission off (default) | on

When you select this parameter, an output port, labeled as
`Status`, becomes available.

The port outputs `0` for a successful read
operation.

### **Sample time** — Frequency to read data from the I2C Peripheral devices `0.1` (default)

Specify how often the I2C Controller Read block reads data
from the I2C Peripheral devices. When you specify this parameter
as`-1`, the block inherits its sample time based on the
context of the block within the model.

## Libraries

Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F746G-Discovery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Read data from I2C Peripheral devices or I2C Peripheral devices register

The I2C Controller Read block reads serial data from an I2C Peripheral
devices that is connected to the board. Using this block, you can read data from a
specific register on the I2C Peripheral devices.

For more information on I2C communication, see Support I2C Communication.
