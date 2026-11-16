---
type: simulink-block
title: 'SPI Controller Transfer'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'spicontrollertransfer'
documentation_source_path: '../simulink/supportpkg/raspberrypi_ref/spicontrollertransfer.html'
language: en
---

# SPI Controller Transfer

## Ports

### Input

### **Port\_1** — Input port to write data to SPI peripheral [Nx1] or [1xN] array

The input port through which the block accepts
a single dimensional array of values to write to
the peripheral device.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Output port to read data from an SPI peripheral device [Nx1] array

Output port from which the block receives data
from SPI peripheral device.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Board** — Specific board used for SPI communication `Pi 2 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

Select the specific board that you are using. Changing the board
updates the pin choices that you get.

### **Chip select pin** — Chip select pin to which the SPI peripheral device is connected `SPI0_CE0` (default) | `SPI0_CE1` | `SPI1_CE0` | `SPI1_CE1` | `SPI1_CE2`

Select the pin number on the Raspberry Pi® board to which the SPI peripheral
device is connected.

To enable the secondary SPI bus on your Raspberry Pi hardware, follow the steps as
mentioned in Enable Secondary SPI Bus of Raspberry Pi Hardware.

### **Mode (Clock polarity and phase)** — Mode of SPI communication 0 (default) | 1 | 2 | 3

Select the mode for SPI communication.

For more information on mode, refer to SPI Transfer Modes

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Write data to and read data from SPI peripheral device

Write data to and read data from an SPI peripheral device. To open the pin map of the
Raspberry Pi board, click the **View pin map**
button.

For more information on SPI communication refer to Support SPI Communication and Raspberry Pi SPI Interface
