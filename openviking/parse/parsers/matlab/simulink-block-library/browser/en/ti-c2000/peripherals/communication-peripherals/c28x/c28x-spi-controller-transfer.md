---
type: simulink-block
title: 'C28x SPI Controller Transfer'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xspicontrollertransfer'
documentation_source_path: 'ref/c28xspicontrollertransfer.html'
language: en
---

# C28x SPI Controller Transfer

## Ports

### Input

### **Tx** — Data written to registers of SPI peripheral device (MOSI) vector

The data written by the block to the registers of a peripheral device
over the SPI interface.

**Data Types:** `uint16`
### Output

### **Rx** — Data read from registers of SPI peripheral device (MISO) vector

The data read by the block from the registers of a peripheral device
over the SPI interface.

**Data Types:** `uint16`

## Parameters

### Main

### **SPI module** — SPI module to write and read data `SPI_A` (default) | `SPI_B` | `SPI_C` | `SPI_D`

The SPI peripheral module to which the SPI peripheral device is
connected. Each processor has a different number of modules.

### **Clock polarity** — SPI clock polarity `Rising_edge` (default) | `Falling_edge`

The clock polarity (CPOL) for SPI communication mode.

### **Clock phase** — SPI clock phase `No_delay` (default) | `Delay_half_cycle`

The clock phase (CPHA) for SPI communication mode.

### **Enable register address** — Enables SPI register address `on` (default) | `off`

Enables the **Register address** parameter.

### **Register address** — SPI register address `0` (default) | positive integer scalar | positive integer vector

The peripheral register address from which the block reads data.

For example, if we consider the Using SPI to Read and Write Data to SPI EEPROM
example, to write the EEPROM memory by address `32
(0x0020)` and the write command 2, the entry can be
`[2 0 32]` which corresponds to write command
followed by 16-bit address and the data at the input port.

Here the address is split as `0x00 (0)` and
`0x20 (32)` as two 8-bit numbers and is entered in
the register address. The reason for splitting it as two 8-bit numbers
is the setting in `Data bits` parameter in
`Advanced` tab. Since this is set to 8 bits, the
data in the vector format should not be considered more than 8-bit. If
you select the parameter as `16`, then
`0` and `32` corresponds to 32-bit
address `(0x00000020)` instead of 16-bit.

#### Dependencies

This parameter appears only when you select **Enable
register address**.

### Advanced

### **Data bits** — Number of bits in SPI transfer `8` (default) | integer in the range [1 16]

Length in bits of each transmitted or received character, specified as
an integer in [1 16]. For example, if you select `8`,
the maximum value that can be transmitted using SPI is
28 – 1. If you send data values greater
than this value, the buffer overflows.

### **Chip select calling method** — Method to select SPI peripheral device `Provided by the SPI peripheral` (default) | `Explicit GPIO calls`

The SPI controller uses these methods to select SPI peripheral
devices.

- `Provided by the SPI peripheral` —
  The SPI controller uses the **STE pin
  assignment** parameter in **Hardware Implementation** > **Target Hardware Resources** > **SPI** to select the peripheral device. peripheral select
  and deselect are handled by the SPI peripheral.
- `Explicit GPIO calls` — The SPI
  controller uses the general purpose input/output pins explicitly
  to select/deselect SPI peripheral devices. The SPI
  controller Transfer block selects the peripheral
  before data is transmitted and deselects the peripheral after
  data is received using GPIO pins.

### **Chip select pin polarity** — SPI peripheral select pin polarity `Active low` (default) | `Active high`

The logic levels supported by the peripheral select pin to select the
SPI peripheral device.

- `Active low` — The device is enabled
  on logic low. The SPI peripheral device is enabled when its
  peripheral select pin is set to low.
- `Active high` — The device is enabled
  on logic high. The SPI peripheral device is enabled when its
  peripheral select pin is set to high.

#### Dependencies

This parameter appears only when **Chip select calling
method** is set to `Explicit GPIO
calls`.

### **Chip select pin** — SPI peripheral select pin `1` (default) | positive integer scalar

The general purpose input/output pin that serves as peripheral select
for SPI.

#### Dependencies

This parameter appears only when **Chip select calling
method** is set to `Explicit GPIO
calls`.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Simulink Support Package for Raspberry Pi Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Write data to and read data from SPI peripheral device

The C28x SPI Controller Transfer block writes data to and reads data
from a peripheral device over the Serial Peripheral Interface (SPI). The block runs in
controller mode. The block outputs an array of the same size and data type as the input
values. You can use this block with the Byte Pack and Byte
Unpack blocks for heterogeneous data type transfers.

**Note**

To communicate with multiple peripherals using the same SPI module, use
multiple instances of the SPI block with the same module and configure a unique
chip select for each instance.

Configure the SPI modules for the specific hardware board by navigating to **Hardware Implementation** > **Target hardware resources**. Verify that these settings meet the requirements of your application.

Using this block, you can access an SPI device to measure quantities such as
temperature and pressure.
