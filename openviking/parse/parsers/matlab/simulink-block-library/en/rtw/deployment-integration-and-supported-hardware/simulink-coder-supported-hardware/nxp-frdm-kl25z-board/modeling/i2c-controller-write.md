---
type: simulink-block
title: 'I2C Controller Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'i2ccontrollerwrite'
documentation_source_path: 'freedomboard/ref/i2ccontrollerwrite.html'
language: en
---

# I2C Controller Write

## Ports

### Input

### **Data** — Data that you want to write to the I2C peripheral device scalar | vector

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### Output

### **Status** — Status of the write operation scalar

When you select the **Output error status**
parameter, the block configures an output port. The port on the block is
labeled as `Status`, indicating that the block outputs
the status of the write operation at the output port.

The block outputs the status as a `uint8` value. Each
value corresponds to a data transfer status.

| Status value | Status description |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `I2C_BUS_ERROR` |

**Data Types:** `uint8`

## Parameters

### **I2C module** — I2C module to write data `0` (default) | 1

Specify the I2C module on the board from which you want to write data to
the I2C peripheral device.

### **Peripheral address** — The I2C peripheral address to which you want to write data `10` (default) | `integer between 0 and 127`

Specify the I2C peripheral address to which you want to write the data.
The I2C peripheral device address is a 7-bit address.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example, ‘hex2dec(‘61’)’.

### **Peripheral byte order** — The byte ordering that your I2C peripheral device supports `BigEndian` (default) | `LittleEndian`

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

### **Peripheral register address** — The I2C peripheral register address to write data `0` (default) | `integer between 0 and 255`

Specify the I2C peripheral register address to which you want to write the
data.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example, ‘hex2dec(‘20’)’.

For more information on register read/write, see I2C Register Read/Write.

#### Dependencies

This parameter appears only when you select **Enable register
access** parameter.

### **Send NACK at the end of data transfer** — Option to send Not Acknowledge bit at the end of data transfer off (default) | on

When you select this parameter, the I2C Controller Write
block sends a NACK (Not Acknowledge) bit to the peripheral device with the
final byte.

When the peripheral device receives the NACK, it waits for a STOP
condition from the I2C Controller block. The Controller block generates
either a STOP condition to abort the transfer or a repeated START condition
to start a new transfer.

When you clear this parameter, the I2C Controller Write
block sends an ACK (Acknowledge) bit to the peripheral device at the end of
every byte. The ACK indicates that the I2C Controller Write
block is ready to read the next byte from the peripheral device.

#### Dependencies

This parameter appears only when you clear **Enable register
access** parameter.

### **Remove stop bit at the end of data transfer** — Option to remove STOP bit at the end of data transfer off (default) | on

When you clear this parameter, the block sends a STOP condition. This
condition indicates that the block has terminated the data transmission and
the I2C bus is free for any other I2C Controller to initiate the read/write
operation.

When you select this parameter, the block sends another START condition
followed by an address and read/write bit. The block sends any number of
start conditions recursively. Such a repeated START condition allows write
operations to the peripheral devices without releasing the bus. No other
Controller block interrupts the operation.

#### Dependencies

This parameter appears only when you clear **Enable register
access** parameter.

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

Simulink Coder Support Package for NXP FRDM-KL25Z Board/FRDM-KL25Z

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Write data to I2C peripheral device or I2C peripheral device register

The I2C Controller Write block writes data to an I2C peripheral device
that is connected to the board. Using this block, you can write data to a specific
register on the I2C peripheral device.

For more information on I2C communication, see Support I2C Communication.
