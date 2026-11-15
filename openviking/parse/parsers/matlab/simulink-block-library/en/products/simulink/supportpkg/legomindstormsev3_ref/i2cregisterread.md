---
type: simulink-block
title: 'I2C Register Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Communication Protocol Blocks'
documentation_page: 'i2cregisterread'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/i2cregisterread.html'
language: en
---

# I2C Register Read

## Ports

### Output

### **Data** — Output data vector

The block outputs the data read by the controller from the peripheral device or
peripheral device register(s) as a *N*-by-1 vector, where
*N* represents the data size.

**Data Types:** `uint8` | `uint16` | `uint32`

### **Status** — Status of controller read operation `0` | `1`

The block outputs the status of the controller read operation on the peripheral
device or the peripheral device register.

- `0`: Indicates a successful read operation, which means
  that the data received on the **Data** port is valid.
- `1`: Indicates an unsuccessful read operation, which means
  that the data received on the **Data** port is invalid.

#### Dependencies

To enable this port, select **Output error status**.

**Data Types:** `uint8`

## Parameters

### **EV3 brick input port number** — Input port connected to peripheral device `4` (default) | `1` | `2` | `3`

Select the input port on the EV3 brick to which the peripheral device is connected.
There are four ports on the hardware and you can select any one of the ports. If
connecting multiple peripheral devices, specify a unique port for each peripheral
device.

### **Peripheral address** — I2C peripheral device address or identifier `10` (default) | scalar in the range [`0`, `127`]

Enter the I2C peripheral device address (decimal format) on which the master
performs the read operation.

### **Peripheral register address** — I2C peripheral device register address `0` (default) | scalar in the range [`0`, `255`]

Enter the register address (decimal format) of the I2C peripheral device on which
the controller performs the read operation.

### **Data type** — Type of data read by controller `uint8` (default) | `uint16` | `uint32`

Select the type of data read by the controller from the peripheral device or
peripheral device register. The controller can read only a maximum of 32 bytes of data
in a single read operation.

### **Data size (N)** — Size of data `1` (default) | scalar

Enter the size of data that the controller reads from the peripheral device or
peripheral device register.

For example, when you specify a value of 5, the controller reads data from five
contiguous peripheral device registers starting from the register address specified in
the **Peripheral register address** parameter.

**Note**

The controller can perform a group read operation only on contiguous peripheral
device registers.

### **Sample time** — Time interval at which controller reads data `0.1` (default) | scalar in the range [`0.01`, `1`]

Enter the time interval (in seconds) at which the controller reads data from the
peripheral device or peripheral device register.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Controller device reads data from the I2C peripheral device or I2C peripheral device register(s)

In the I2C Register Read block, the controller device reads data from the
I2C peripheral device or the I2C peripheral device register. The EV3 brick acts as the
controller device. Any I2C device, such as a color sensor, can act as the peripheral device.
Both the controller and the peripheral device must be connected over the same I2C network for
successful communication.

Simulink® Support Package for LEGO®
MINDSTORMS® EV3 Hardware supports the I2C serial data communication protocol, where each device on the
I2C network is referenced by a unique 8-bit address or identifier.
