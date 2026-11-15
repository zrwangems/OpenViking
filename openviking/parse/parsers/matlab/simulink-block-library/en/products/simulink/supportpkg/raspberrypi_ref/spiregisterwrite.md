---
type: simulink-block
title: 'SPI Register Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'spiregisterwrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/spiregisterwrite.html'
language: en
---

# SPI Register Write

## Ports

### Input

### **Port\_1** — Input port to accept data [Nx1] or [1xN] array

The input port to accept data to write the data to the SPI peripheral register.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Board** — SPI module used for communication `Pi 2 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

Select the specific board that you are using. Changing the board
updates the pin choices that you get.

### **Chip select pin** — Pin connected to the SPI peripheral device `SPI0_CE0` (default) | `SPI0_CE1` | `SPI1_CE0` | `SPI1_CE1` | `SPI1_CE2`

Select the pin number on the Raspberry Pi board to
which the SPI peripheral device is connected.

To enable the secondary SPI bus on your Raspberry Pi® hardware, follow the steps as
mentioned in Enable Secondary SPI Bus of Raspberry Pi Hardware.

### **Mode (Clock polarity and phase)** — Mode of SPI communication 0 (default) | 1 | 2 | 3

Select the SPI communication mode.

### **Register address** — Register address to write the data 0 (default) | uint8 array

Enter the peripheral register address to write the data.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Write data to registers of an SPI peripheral device

The SPI Register Write block writes the block
input data to specified register address. To open the pin map of the
Raspberry Pi board, click the **View pin map** button.

For more information on SPI communication, refer to Support SPI Communication and Raspberry Pi SPI Interface.
