---
type: simulink-block
title: 'I2C Master Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'i2ccontrollerwrite'
documentation_source_path: 'beagleboneblue/ref/i2ccontrollerwrite.html'
language: en
---

# I2C Master Write

## Ports

### Input

### **Data** — Input port to write data to I2C peripheral device register [1xN] and [Nx1] array

The input port to write data to the I2C peripheral device or I2C peripheral device
register.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Status** — Status of write operation scalar

Output port to display error status.

#### Dependencies

This port appears only when you select the **Output error
status** parameter.

**Data Types:** `uint8`

## Parameters

### **Peripheral address** — Address of I2C peripheral device 10 (default) | scalar

Enter the I2C peripheral device address to which you want to write the data. The I2C
peripheral device address is a 7-bit address.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example hex2dec(‘61’).

### **Peripheral byte order** — Byte order supported by the I2C peripheral device BigEndian (default) | LittleEndian

Select the byte ordering that your I2C peripheral supports.

The two byte ordering options are:

- Big Endian — The most significant byte is written first over the I2C bus.
  This option is the default option.
- Little Endian — The least significant byte is written first over the I2C
  bus.

### **Enable register access** — Option to enable writing to the register on I2C peripheral device On (default) | Off

Select this check box to write data to a specific I2C peripheral register.

When you clear this parameter, the **Send NACK at the end of data
transfer** and **Remove stop bit at the end of data transfer** parameters are displayed. Using these parameters, you can modify the write
operation according to your requirements. For more information, see I2C Register Read/Write

### **Send NACK at the end of data transfer** — Option to send Not Acknowledge bit at the end of data transfer off (default) | on

When you select this parameter, the I2C Controller Write block sends
a NACK (Not Acknowledge) bit to the peripheral device with the final byte.

When the peripheral device receives the NACK, it waits for a STOP condition from the
I2C controller block. The controller block generates either a STOP condition to abort
the transfer or a repeated START condition to start a new transfer.

When you clear this parameter, the I2C Controller Write block sends
an ACK (Acknowledge) bit to the peripheral device at the end of every byte. The ACK
indicates that the I2C Controller Write block is ready to read the next
byte from the peripheral device.

#### Dependencies

This parameter appears only when you clear the **Enable register
access** parameter.

### **Remove stop bit at the end of data transfer** — Option to remove STOP bit at the end of data transfer off (default) | on

When you clear this parameter, the block sends a STOP condition. This condition
indicates that the block has terminated the data transmission and the I2C bus is free
for any other I2C controller block to initiate the read/write operation.

When you select this parameter, the block sends another START condition followed by
an address and read/write bit. The block sends any number of start conditions
recursively. Such a repeated START condition allows write operations to the peripheral
devices without releasing the bus. No other controller block interrupts the operation.

#### Dependencies

This parameter appears only when you clear the **Enable register
access** parameter.

### **Peripheral register address** — I2C peripheral device register address 0 (default) (default) | scalar

Enter the peripheral device register address to which you want to write the data.

#### Dependencies

This parameter is enabled only when you select the **Enable register
access** parameter.

### **Output error status** — Option to display output error status Off (default) | On

Select this option to display the output error status. When you select this
parameter, the block configures an output port. The port on the block is labeled as
`Status`, indicating that the block outputs the status of the write
operation at the output port.

The block outputs the status as a `uint8` value. Each value
corresponds to a data transfer status.

| Status value | Status description |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `BUS_ERROR` |
| `16` | `BUS_NOT_IN_USE` |

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Write data to I2C peripheral device or I2C peripheral device register

Write data to an I2C peripheral device or an I2C peripheral device register. Using this
block, you can also write data to a specific register on the I2C peripheral.

For more information on I2C Communication, refer to Support I2C Communication.To open the pin map of the BeagleBone® Bone Blue board, click the **View pin map**.
