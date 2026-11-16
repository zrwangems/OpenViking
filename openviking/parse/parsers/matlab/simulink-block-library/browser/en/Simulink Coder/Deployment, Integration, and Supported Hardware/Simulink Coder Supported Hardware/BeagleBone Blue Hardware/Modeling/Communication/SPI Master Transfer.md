---
type: simulink-block
title: 'SPI Master Transfer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'spicontrollertransfer'
documentation_source_path: 'beagleboneblue/ref/spicontrollertransfer.html'
language: en
---

# SPI Master Transfer

## Ports

### Input

### **Port\_1** — Input port to write data to SPI peripheral [Nx1] or [1xN] array

The input port through which the block accepts a single dimensional array of
values to write to the peripheral device.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Output port to read data from an SPI peripheral device [Nx1] array

Output port from which the block receives data from SPI peripheral device.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **SPI select** — Peripheral select pin to which the SPI peripheral device is connected S1.1 (default) | S1.2

Select the pin number on the BeagleBoneBlue board to which the SPI peripheral device is connected.

### **Mode (Clock polarity and phase)** — Mode of SPI communication 0 (default) | 1 | 2 | 3

Select the mode for SPI communication.

For more information on mode, refer to SPI Transfer Modes.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Write data to and read data from SPI peripheral device

Write data to and read data from an SPI peripheral device. To open the pin map of the
BeagleBone® Blue board, click the **View pin map** button.

For more information on SPI Communication, refer to Support SPI Communication.

The block can be used along with Byte Pack or Byte Unpack
block to support heterogeneous data type transfers.
