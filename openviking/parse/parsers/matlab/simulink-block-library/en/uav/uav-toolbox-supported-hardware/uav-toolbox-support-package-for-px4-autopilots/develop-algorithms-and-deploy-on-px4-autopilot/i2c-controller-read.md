---
type: simulink-block
title: 'I2C Controller Read'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'i2ccontrollerread'
documentation_source_path: 'px4/ref/i2ccontrollerread.html'
language: en
---

# I2C Controller Read

## Ports

### Output

### **Data** — Data from I2C peripheral device vector

The port reads vector data from an I2C device that is connected to
the board. The size of the data is the value that you specify in the
**Data size** parameter.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `single` | `double`

### **Status** — Status of read operation scalar

When you select the **Output error status**
parameter, an output port, labeled as `Status`, becomes
available.

The port outputs one of these values:

- `0` for a successful read operation.
- `1` for a failure in opening the bus.
- `2` for a failure in read operation.

**Data Types:** `uint8`

## Parameters

### **I2C Bus** — I2C bus to read data `1` (default)

Specify the I2C bus on the board to read data from the I2C peripheral
device.

### **Peripheral address** — I2C register peripheral address from which to read data `10` (default) | nonnegative integer

Specify the I2C peripheral address to read the data. You can specify this
address in hexadecimal format `hex2dec()`, for example,
`0x20`.

### **Peripheral byte order** — Byte ordering that your I2C peripheral device supports `BigEndian` (default) | `LittleEndian`

The 2-byte ordering options are:

- `BigEndian` -The most significant byte is
  sent first over the I2C bus.
- `LittleEndian` - The least significant
  byte is sent first over the I2C bus.

### **Enable register access** — Option to read from a specific I2C peripheral register `on` (default) | `off`

When you select this parameter, the block reads data from the I2C
peripheral register that you specify in the **Peripheral register
address** parameter.

### **Peripheral register address** — The I2C peripheral register address to read data `2` (default) | `integer between 0 and 255`

Specify the I2C register address to read the data.

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example,
`0x20`.

#### Dependencies

To enable this parameter, select the **Enable register
access** parameter.

### **Data type** — Data type of data from I2C peripheral device `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

Select the data type in which you want to read from the I2C peripheral
device.

### **Data size (N)** — Data size to read from I2C peripheral device `1` (default) | `nonnegative integer`

Specify the data size that you want to read from the I2C peripheral device
for the selected data type.

### **Output error status** — Option to display the error status during data transmission `off` (default) | `on`

When you select this parameter, an output port, labeled as
`Status`, becomes available.

The port outputs one of these values:

- `0` for a successful read operation.
- `1` for a failure in opening bus.
- `0` for a failure in read or write
  operation.

### **Sample time** — Frequency to read data from the I2C peripheral device `0.01` (default)

Specify how often the I2C Controller Read block reads data
from the I2C peripheral device. When you specify this parameter as
`-1`, the block inherits its sample time based on the
context of the block within the model.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Read data from I2C peripheral device or I2C peripheral device register

The I2C Controller Read block reads serial data from an I2C peripheral
device that is connected to the board. Using this block, you can read data from a
specific register on the I2C peripheral device.

To view the mapping between the Bus number and the port label on hardware board, click
**View I2C Bus map**. For more information on the Bus mapping, see
I2C Bus Port Numbers for Labels on PX4 Autopilots.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.
