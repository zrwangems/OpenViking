---
type: simulink-block
title: 'SPI Register Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'spiregisterread'
documentation_source_path: 'supportpkg/raspberrypi_ref/spiregisterread.html'
language: en
---

# SPI Register Read

## Ports

### Output

### **Port\_1** — Output port to read data [Nx1] array

This port is the output port to read data from an SPI peripheral register.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Board** — Specific board used for SPI communication `Pi 2 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

Select the specific board that you are using. Changing the board
updates the pin choices that you get.

### **Chip select pin** — Pin connected to the SPI peripheral device `SPI0_CE0` (default) | `SPI0_CE1` | `SPI1_CE0` | `SPI1_CE1` | `SPI1_CE2`

Select the pin number on the Raspberry Pi board to
which the SPI peripheral device is connected.

To enable the secondary SPI bus on your Raspberry Pi® hardware, follow the steps as
mentioned in Enable Secondary SPI Bus of Raspberry Pi Hardware.

### **Mode (Clock polarity and phase)** — Mode of SPI communication 0 (default) | 1 | 2 | 3

Select the mode of SPI communication.

### **Register address** — Register address to read the data 0 (default) | uint8 array

Enter the SPI peripheral register address to read the data.

### **Output data type** — Data type for output int8 (default) | uint8 | int16 | uint16 | int32 | uint32 | single | double

Select the data type for SPI communication.

### **Output data length** — Data length for SPI communication 1 (default) | scalar

Enter the output data length of the selected data type to read from the SPI peripheral
register.

### **Sample time** — Interval at which block reads data from SPI peripheral device `0.1` (default) | `-1` | any nonnegative value

Specify how often this block reads the data from the
SPI peripheral device, in seconds. When you set this
parameter to `-1`, Simulink® determines the best sample time for
the block based on the block context within the
model.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Read data from SPI peripheral device register

The SPI Register Read block initiates an SPI read operation from an SPI
peripheral register. You can specify the data type and data length to get
data from the peripheral registers. To open the pin map of the Raspberry Pi
board, click the **View pin map** button.

For more information on SPI communication, refer to Support SPI Communication and Raspberry Pi SPI Interface
