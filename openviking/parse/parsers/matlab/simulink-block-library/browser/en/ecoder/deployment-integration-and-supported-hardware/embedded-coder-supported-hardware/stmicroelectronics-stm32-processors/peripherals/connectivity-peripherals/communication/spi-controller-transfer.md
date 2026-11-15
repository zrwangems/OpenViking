---
type: simulink-block
title: 'SPI Controller Transfer'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'spicontrollertransfer'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/spicontrollertransfer.html'
language: en
---

# SPI Controller Transfer

## Ports

### Input

### **Tx** — Data written to registers of SPI peripheral device serial data out (SDO) vector

The data written by the block to the registers of a peripheral device
over the SPI interface.

**Data Types:** `uint8` | `uint16` | `uint32`
### Output

### **Rx** — Data read from registers of SPI peripheral device serial data in (SDI) vector

The data read by the block from the registers of a peripheral device
over the SPI interface.

**Data Types:** `uint8` | `uint16` | `uint32`

## Parameters

### Main

### **SPI module** — SPI module to write and read data `SPI1` (default) | `SPI2` | `SPI3` | `SPI4` | `SPI5` | `SPI6`

The SPI peripheral module to which the SPI peripheral device is
connected. Each processor has a different number of modules.

### **Clock polarity** — SPI clock polarity `Low` (default) | `High`

The clock polarity (CPOL) for SPI communication mode.

### **Clock phase** — SPI clock phase `1 Edge` (default) | `2 Edge`

The clock phase (CPHA) for SPI communication mode.

### **Enable register address** — Enables SPI register address `on` (default) | `off`

Enables the **Register address** parameter.

### **Register address** — SPI register address `0` (default) | positive integer scalar | positive integer vector

The peripheral register address from which the block reads data.

**Note**

The positive integer vector is specified as, `[2 0
32]` for Write Data to Memory and `[3 0
32]` for Read Data from Memory. For more
information, refer to the example Using SPI to Read and Write Data to SPI EEPROM (C2000 Microcontroller Blockset).

#### Dependencies

This parameter appears only when you select **Enable
register address**.

### Advanced

### **Data bits** — Number of bits in SPI transfer `4` (default) | integer in the range [1 32]

Length in bits of each transmitted or received character, specified as
an integer in [1 32]. For example, if you select `8`,
the maximum value that can be transmitted using SPI is
28 – 1. If you send data values greater
than this value, the buffer overflows.

### **Chip select calling method** — Method to select SPI peripheral device `Provided by the SPI peripheral` (default) | `Explicit GPIO calls`

The SPI controller uses these methods to select SPI peripheral
devices.

- `Provided by the SPI peripheral` —
  The SPI controller uses the pin provided by the SPI peripheral.
  Peripheral select and deselect are handled by the SPI
  peripheral.
- `Explicit GPIO calls` — The SPI
  controller uses the general purpose input/output pins explicitly
  to select/deselect SPI peripheral devices. The SPI
  controller Transfer block selects the peripheral
  before data is transmitted and deselects the peripheral after
  data is received using GPIO pins.

### **Chip select pin polarity** — SPI peripheral select pin polarity `Active low` (default) | `Active high`

The logic levels supported by the chip select pin to select the SPI
peripheral device.

- `Active low` — The device is enabled
  on logic low. The SPI peripheral device is enabled when its chip
  select pin is set to low.
- `Active high` — The device is enabled
  on logic high. The SPI peripheral device is enabled when its
  chip select pin is set to high.

#### Dependencies

This parameter appears only when **Chip select calling
method** is set to `Explicit GPIO
calls`.

### **Chip select port name** — SPI chip select port name `GPIOA` (default) | `GPIOB` | `GPIOC`

Select the general purpose port name that serves as the chip select
for SPI.

#### Dependencies

This option appears only when **Chip select calling
method** is set to `Explicit GPIO
calls`.

### **Chip select pin** — SPI peripheral select pin `1` (default) | positive integer scalar

The general purpose input/output pin that serves as chip select for
SPI.

#### Dependencies

This parameter appears only when **Chip select calling
method** is set to `Explicit GPIO
calls`.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Write data to and read data from SPI peripheral device

The SPI Controller Transfer block accepts a 1-D array and outputs an
array of the same size of the `uint8`, `uint16` or
`uint32` data types

The SPI Controller Transfer block writes data to and reads data from a
peripheral device over the Serial Peripheral Interface (SPI). The block runs in
controller mode. The block outputs an array of the same size and data type as the input
values. You can use this block with the Byte Pack and Byte
Unpack blocks for heterogeneous data type transfers.

Using this block, you can access an SPI device to measure quantities such as
temperature and pressure.

The SPI receive interrupt is configured for a specific hardware board by navigating to **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources**.

SPI Module is configured in STM32CubeMX project.

- Launch the STM32CubeMX project. For more information, see Configure STM32 Processor-Based Boards using STM32CubeMX with Simulink.
- Navigate to **Pinout & Configuration** > **Connectivity** > **SPI#**

Verify that these settings meet the requirements of your application.

**Note**

The following are the limitations for SPI block:

- Number of bytes of data to be sent to the transmit block should be
  less than the FIFO length.
- On running SPI Controller Transfer block in Monitor & Tune,
  you might observe the junk data. To resolve, reconnect and start
  Monitor & Tune.
- If SPI Controller Transfer block is used in a model don’t use the
  SPI Transmit and SPI Receive blocks for the same module.
- Avoid using same modules of SPI in multiple tasks, which can lead
  to issues.
- SPI blocks do not support Master Receive Only, Slave Receive Only,
  Master Transmit Only, and Slave Transmit only for SPI mode
  configuration in STM32CubeMX file.
