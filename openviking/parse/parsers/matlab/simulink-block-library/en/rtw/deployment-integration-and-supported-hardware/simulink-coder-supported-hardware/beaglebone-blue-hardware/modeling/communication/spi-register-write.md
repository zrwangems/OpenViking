---
type: simulink-block
title: 'SPI Register Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'spiregisterwrite'
documentation_source_path: 'beagleboneblue/ref/spiregisterwrite.html'
language: en
---

# SPI Register Write

## Ports

### Input

### **Port\_1** — Input port to accept data [Nx1] or [1xN] array

The input port to accept data to write the data to the SPI peripheral register.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **SPI Select** — Pin connected to the SPI peripheral device S1.1 (default) | S1.2

Select the pin number on the BeagleBone Blue board to which the SPI peripheral
device is connected.

### **Mode (Clock polarity and phase)** — Mode of SPI communication 0 (default) | 1 | 2 | 3

Select the SPI communication mode.

### **Register address** — Register address to write the data 0 (default) | uint8 array

Enter the peripheral register address to write the data.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Write data to registers of an SPI peripheral device

The SPI Register Write block writes the block input data to specified
register address. To open the pin map of the BeagleBone® Blue board, click the **View pin map** button.
