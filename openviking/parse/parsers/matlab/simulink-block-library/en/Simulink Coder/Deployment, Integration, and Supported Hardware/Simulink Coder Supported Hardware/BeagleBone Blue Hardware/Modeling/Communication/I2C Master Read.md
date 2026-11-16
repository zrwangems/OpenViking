---
type: simulink-block
title: 'I2C Master Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'i2ccontrollerread'
documentation_source_path: 'beagleboneblue/ref/i2ccontrollerread.html'
language: en
---

# I2C Master Read

## Ports

### Output

### **Data** — Output port to read data from the I2C peripheral device [Nx1] array

Output port to read data from an I2C peripheral device. The size of the data that
the port emits is based on the **Data size (N)** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Status** — Status of the read operation scalar

Output port to display error status. For more information, see Output error
status.

#### Dependencies

This port appears only when you select the **Output error
status** parameter.

**Data Types:** `uint8`

## Parameters

### **Peripheral address** — I2C peripheral device address 10 (default) | scalar

Enter the I2C peripheral device address from which you want to read data. You can
specify this address in hexadecimal format hex2dec(), for example, hex2dec(‘10').

### **Peripheral byte order** — Byte order supported by the I2C peripheral device BigEndian (default) | LittleEndian

Select the byte ordering that your I2C peripheral supports.

The two byte ordering options are:

- Big Endian — The most significant byte is read first over the I2C bus.
  This option is the default option.
- Little Endian — The least significant byte is read first over the I2C
  bus.

### **Enable register address** — Option to enable reading from the register on I2C peripheral register On (default) | Off

Select this check box to enable reading data from a specific register on the I2C
peripheral device.

When you clear this parameter, the **Send NACK at the end of
data transfer**  and **Remove stop bit at the end of data
transfer** parameters are displayed. Using these parameters, you can modify
the read operation according to your requirements.

### **Send NACK at the end of data transfer** — Option to send Not Acknowledge bit at the end of data transfer off (default) | on

When you select this parameter, the I2C Controller Read block sends a
NACK (Not Acknowledge) bit to the peripheral device with the final byte.

When the peripheral device receives the NACK, it waits for a STOP condition from the
I2C controller block. The controller block generates either a STOP condition to abort
the transfer or a repeated START condition to start a new transfer.

When you clear this parameter, the I2C Controller Read block sends an
ACK (Acknowledge) bit to the peripheral device at the end of every byte. The ACK
indicates that the I2C Controller Read block is ready to read the next
byte from the peripheral device.

#### Dependencies

This parameter appears only when you clear the **Enable register
access** parameter.

### **Remove stop bit at the end of data transfer** — Option to remove STOP bit at the end of data transfer off (default) | on

When you clear this parameter, the block sends a STOP condition. This condition
indicates that the block has terminated the data transmission and the I2C bus is free
for any other I2C controller block to initiate the new read/write operation.

When you select this parameter, the block sends another START condition followed by
an address and read/write bit. The block sends any number of start conditions
recursively. Such a repeated START condition allows write operations to the peripheral
devices without releasing the bus. No other controller block interrupts the
operation.

#### Dependencies

This parameter appears only when you clear **Enable register
access** parameter.

### **Peripheral register address** — I2C peripheral device register address to read data 0 (default) | scalar

Enter the peripheral device register address from which you want to read the data.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example, hex2dec(‘10’).

#### Dependencies

This parameter is enabled only when you select the **Enable register
access** parameter.

### **Data type** — Data type to read from I2C peripheral device uint8 (default) | int8 | int16 | uint16 | int32 | uint32 | single | double

Select the data type to read from I2C peripheral device.

### **Data size (N)** — Data size to read from the I2C peripheral device 1 (default) | scalar

Enter the data size that you want to read from the I2C peripheral device for the
selected data type.

### **Output error status** — Option to display the error status during data transmission Off (default) | On

Select this option to display the error status during data transmission.

When you select the **Output error status** parameter, the block
configures an output port. The port on the block is labeled as
`Status`, indicating that the block outputs the status of the read
operation at the output port.

The block outputs the status as a `uint8` value. Each value
corresponds to a data transfer status.

| Status Value | Status Description |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `BUS_ERROR` |
| `16` | `BUS_NOT_IN_USE` |

### **Sample time** — Frequency at which block reads data 0.1 (default) | scalar

Specify how often this block reads the data from the I2C peripheral. Enter a value
greater than zero.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read data from I2C peripheral device or I2C peripheral device register

Read serial data from an I2C peripheral. Using this block, you can also read data from a
specific register on the I2C peripheral device.

For more information on I2C Communication, refer to Support I2C Communication.

To open the pin map of the BeagleBone® Blue board, click **View pin map** button.
