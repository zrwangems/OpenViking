---
type: simulink-block
title: 'I2C Controller Write'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'i2ccontrollerwrite'
documentation_source_path: 'px4/ref/i2ccontrollerwrite.html'
language: en
---

# I2C Controller Write

## Ports

### Input

### **Data** — Data to write to I2C peripheral device scalar | vector

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### Output

### **Status** — Status of write operation scalar

When you select the **Output error status**
parameter, an output port, labeled as `Status`, becomes
available.

The port outputs one of these values:

- `0` for a successful write operation.
- `1` for a failure in opening the bus.
- `2` for a failure in write operation.

**Data Types:** `uint8`

## Parameters

### **I2C Bus** — I2C bus on the board to which the I2C peripheral device is connected to `1` (default) | `nonnegative integer`

Specify the I2C bus on the board to write data to the I2C peripheral
device.

### **Peripheral address** — I2C peripheral address to write data `10` (default)

Specify the I2C peripheral address to write the data. The I2C peripheral
device address is a 7-bit address.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example,
`0x61`.

### **Peripheral byte order** — Byte ordering that your I2C peripheral device supports `BigEndian` (default) | `LittleEndian`

The 2-byte ordering options are:

- `BigEndian` - The most significant byte is
  sent first over the I2C bus.
- `LittleEndian` - The least significant byte
  is sent first over the I2C bus.

### **Enable register access** — Option to write to specific I2C peripheral register on (default) | off

When you select this parameter, the block writes data to the I2C
peripheral register that you specify in the **Peripheral register
address** parameter.

### **Peripheral register address** — I2C peripheral register address to write data `uint8(1)` (default)

Specify the I2C peripheral register address to write the data.

Specify this address in 8-bit unsigned integer or in hexadecimal format.
To specify the address in 8-bit unsigned integer, use
`uint8()`, for example,
‘`uint8(20)`’. To specify the address in hexadecimal
format, use `hex2dec()`, for example,
`0x20`.

#### Dependencies

This parameter appears only when you select **Enable register
access** parameter.

### **Output error status** — Option to display the error status during data transmission `off` (default) | `on`

When you select this parameter, an output port, labeled as
`Status`, becomes available.

The port outputs the status of the write operation.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Write data to I2C peripheral device or I2C peripheral device register

The I2C Controller Write block writes data to an I2C peripheral device
that is connected to the board. Using this block, you can write data to a specific
register on the I2C peripheral device.

To view the mapping between the Bus number and the port label on hardware board, click
**View I2C Bus map**. For more information on the Bus mapping, see
I2C Bus Port Numbers for Labels on PX4 Autopilots.

During Connected I/O simulation, this block writes data to the peripherals of the
hardware.
