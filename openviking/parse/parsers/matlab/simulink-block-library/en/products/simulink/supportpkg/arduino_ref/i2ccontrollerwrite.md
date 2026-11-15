---
type: simulink-block
title: 'I2C Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / I2C'
documentation_page: 'i2ccontrollerwrite'
documentation_source_path: 'supportpkg/arduino_ref/i2ccontrollerwrite.html'
language: en
---

# I2C Write

## Ports

### Input

### **Data** — Input port to write data to I2C peripheral device [1xN] and [Nx1] array

The input port write data to the I2C peripheral device or I2C peripheral device
register.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Status** — Status of write operation scalar

Output port to display error status. For more information, see Output error status

#### Dependencies

This port appears only when you select the **Output error
status** parameter.

**Data Types:** `uint8`

## Parameters

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino hardware to communicate with sensor peripherals. For more information on
the Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **Peripheral address** — Address of I2C peripheral device 10 (default) | scalar

Enter the I2C peripheral device address to which you want to write the data. The I2C
peripheral device address is a 7-bit address.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example hex2dec(‘20’).

### **Peripheral byte order** — Byte order supported by the I2C peripheral device `BigEndian` (default) | `LittleEndian`

Select the byte ordering that your I2C peripheral supports, to write the
data.

The two byte ordering options are:

- `BigEndian` — The most significant byte is
  written first over the I2C bus. This option is the default option.
- `LittleEndian` — The least significant byte is
  written first over the I2C bus.

### **Enable register access** — Option to enable writing to the register on I2C peripheral device on (default) | off

Select this check box to write data to a specific I2C peripheral register.

When you clear this parameter, the **Remove stop bit at the end of data
transfer**  parameter is displayed. Using this parameter, you can modify the
write operation according to your requirements. For more information, Support for I2C Communication

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

### **Output error status** — Option to display output error status off (default) | on

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

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Write data to an I2C peripheral device or an I2C peripheral device register

Write data to an I2C device on the Arduino® hardware. Using this block, you can also write data to a specific register on
the I2C peripheral.

Click **View pin map** to open the Arduino Pin Mapping table.

To know how to assign pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.
