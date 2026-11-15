---
type: simulink-block
title: 'SPI Master Transfer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Basic'
documentation_page: 'spicontrollertransferblock'
documentation_source_path: 'microbit/ref/spicontrollertransferblock.html'
language: en
---

# SPI Master Transfer

## Ports

### Input

### **SDO** — Data to write to registers of an SPI peripheral devices vector

The port accepts the serial data out (SDO) to write to the
registers of a peripheral devices over the SPI
interface.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **SDI** — Data read from registers of an SPI peripheral devices vector

The port outputs the data read from the registers of a
peripheral devices over the SPI interface.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### Main

### **SPI module** — SPI module to write and read data `0` (default)

Specify the SPI module to which the SPI peripheral devices
is connected.

### **Chip select pin** — Pin connected to the SPI peripheral devices

Specify the pin name on the board to which the SPI
peripheral devices is connected. The SPI controller pulls
the SS pin of the selected peripheral devices to a low (0)
value to start the communication. The peripheral devices
is selected depending on the pin polarity that you specify
in the **Chip select pin polarity**
parameter. The controller can select only one peripheral
devices at a time.

### **First bit to transfer** — First bit to transfer for SPI communication `Most significant bit (MSB)` (default) | `Least significant bit (LSB)`

Select the order in which the data is transmitted.

- Most significant bit (MSB) — Select
  MSB to send the most significant bit (MSB)
  first.
- Least significant bit (LSB) — Select
  LSB to send the least significant bit (LSB)
  first.

### **Mode (Clock polarity and phase)** — Mode of SPI communication `0` (default) | `1` | `2` | `3`

An SPI controller sets the clock polarity (CPOL) and the
clock phase (CPHA).

The combination of polarity and phase are referred to as
SPI modes. The SPI modes 0–3 are shown in the
table.

| Mode | Clock Polarity (CPOL) | Clock Phase (CPHA) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 0 |
| 3 | 1 | 1 |

For more information on register read/write, see SPI Transfer Modes.

### Advanced

### **Chip select pin polarity** — Logic level to establish SPI communication `Active low` (default) | `Active high`

The logic levels supported by Chip select pin to select
the SPI peripheral devices.

- Active low — The device is enabled on
  logic low. The SPI peripheral devices gets enabled
  when its SS pin is set to low.
- Active high — The device is enabled on
  logic high. The SPI peripheral devices gets
  enabled when its SS pin is set to high.

## Libraries

Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F746G-Discovery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Write data to and read data from SPI peripheral devices

The SPI controller Transfer block writes data to and reads data
from a peripheral devices over the Serial Peripheral Interface (SPI) interface.
The block outputs an array of the same size and data type as the input values. You
can use this block with Byte Pack and Byte Unpack
blocks to support heterogeneous data type transfers.

Using this block, you can access an SPI device to measure quantities such as
temperature, pressure.

For more information on SPI communication, see Support SPI Communication.
