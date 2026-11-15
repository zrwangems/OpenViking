---
type: simulink-block
title: 'I2C Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / I2C'
documentation_page: 'i2ccontrollerread'
documentation_source_path: 'supportpkg/arduino_ref/i2ccontrollerread.html'
language: en
---

# I2C Read

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

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino® hardware to communicate with sensor peripherals. For more information on
the Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **Peripheral address** — I2C peripheral device address 10 (default) | scalar

Enter the I2C peripheral device address from which you want to read data. You can
specify this address in hexadecimal format hex2dec(), for example, hex2dec(‘10').

### **Peripheral byte order** — Byte order supported by the I2C peripheral device `BigEndian` (default) | `LittleEndian`

Select the byte ordering that your I2C peripheral supports.

The two byte ordering options are:

- `BigEndian` — The most significant byte is read
  first over the I2C bus. This option is the default option.
- `LittleEndian` — The least significant byte is
  read first over the I2C bus.

### **Enable register address** — Option to enable reading from the register on I2C peripheral register `on` (default) | `off`

Select this check box to enable reading data from a specific register on the I2C
peripheral device.

When you clear this parameter, the **Send NACK at the end of
data transfer**  and **Remove stop bit at the end of data
transfer** parameters are displayed. Using these parameters, you can modify
the read operation according to your requirements.

### **Peripheral register address** — I2C peripheral device register address to read data `0` (default) | scalar

Enter the peripheral device register address from which you want to read the data.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example, hex2dec(‘10’).

#### Dependencies

This parameter is enabled only when you select the **Enable register
access** parameter.

### **Data type** — Data type to read from I2C peripheral device `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

Select the data type to read from I2C peripheral device.

### **Data size (N)** — Data size to read from the I2C peripheral device `1` (default) | scalar

Enter the data size that you want to read from the I2C peripheral device for the
selected data type.

### **Output error status** — Option to display the error status during data transmission off (default) | on

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

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015a**

## Description

Read data from I2C peripheral device or I2C peripheral device register

Read serial data from an I2C peripheral. Using this block, you can also read data from a
specific register on the I2C peripheral device.

For more information on I2C Communication, refer to I2C Read/Write.

Click **View pin map** to open the Arduino Pin Mapping table.

To know how to assign pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.
