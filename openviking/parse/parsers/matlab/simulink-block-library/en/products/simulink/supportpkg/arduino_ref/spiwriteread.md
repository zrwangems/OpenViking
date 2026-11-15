---
type: simulink-block
title: 'SPI WriteRead'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / SPI'
documentation_page: 'spiwriteread'
documentation_source_path: 'supportpkg/arduino_ref/spiwriteread.html'
language: en
---

# SPI WriteRead

## Ports

### Input

### **Port\_1** — Input port to write data to SPI peripheral [Nx1] or [1xN] array

The input port through which the block accepts a single dimensional array of
values to write to the peripheral device.

**Data Types:** `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Output port to read data from SPI peripheral device [Nx1] array

Output port from which the block receives data from SPI peripheral device.

**Data Types:** `uint8` | `uint16` | `uint32`

## Parameters

### **SPI module** — SPI communication module `0` (default) | scalar

Specify the SPI module on the Arduino hardware to communicate with SPI peripherals. For more information on
Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **Chip select (CS) pin** — Chip select pin to which SPI peripheral device is connected 10 (default) | target hardware pin

Enter the pin number on the Arduino board to which the SPI peripheral device is connected. The SPI controller
pulls the CS pin of the selected peripheral to a low (0) value to start the
communication. See Pin Mapping for Arduino Timer-Independent Blocks to know the SS pin
restriction with different Arduino boards.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Write data to and read data from an SPI device

Write data to and read data from an SPI device connected to your Arduino board. Using
this block, you can access an SPI device to measure quantities such as temperature, and
pressure. You can also access an SPI device to support Wi-Fi® connectivity, and to access an SD card to store data.

Click **View pin map** to open the Arduino Pin Mapping table.

To know how to assign pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.
