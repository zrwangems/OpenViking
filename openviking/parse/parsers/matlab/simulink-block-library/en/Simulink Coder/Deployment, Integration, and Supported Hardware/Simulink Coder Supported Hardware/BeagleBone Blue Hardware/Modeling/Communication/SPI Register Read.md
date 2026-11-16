---
type: simulink-block
title: 'SPI Register Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'spiregisterread'
documentation_source_path: 'beagleboneblue/ref/spiregisterread.html'
language: en
---

# SPI Register Read

## Ports

### Output

### **Port\_1** — Output port to read data [Nx1] array

This port is the output port to read data from an SPI peripheral register.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

## Parameters

### **Mode (Clock polarity and phase)** — Mode of SPI communication 0 (default) | 1 | 2 | 3

Select the mode of SPI communication.

### **Register address** — Register address to read the data 0 (default) | uint8 array

Enter the SPI peripheral register address to read the data.

### **Output data type** — Data type for output int8 (default) | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | single | double

Select the data type for SPI communication.

### **Output data length** — Data length for SPI communication 1 (default) | scalar

Enter the output data length of the selected data type to read from the SPI
peripheral register.

### **SPI Select** — Pin connected to the SPI peripheral device S1.1 (default) | S1.2

Select the pin number on the BeagleBone Blue board to which the SPI peripheral
device is connected.

### **Sample time** — Frequency to read data from the SPI peripheral device `0.1` (default)

Specify how often the block reads data from the SPI peripheral device. When you
specify this parameter as`-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read data from SPI peripheral device register

The SPI Register Read block initiates an SPI read operation from an SPI
peripheral register. You can specify the data type and data length to get data from the
peripheral registers. To open the pin map of the BeagleBone® board, click the **View pin map** button.
