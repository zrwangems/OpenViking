---
type: simulink-block
title: 'SPI Register Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Basic'
documentation_page: 'spiregisterread'
documentation_source_path: 'microbit/ref/spiregisterread.html'
language: en
---

# SPI Register Read

## Ports

### Output

### **SDI** — Data read from registers of an SPI peripheral devices vector

The port outputs the data read from the registers of a peripheral
devices over the SPI interface.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

## Parameters

### Main

### **SPI module** — SPI module to read data `0` (default)

Specify the SPI module to which the SPI peripheral devices is
connected.

### **Chip select pin** — Pin connected to the SPI peripheral devices `D7`

Specify the pin name on the board to which the SPI peripheral devices
is connected. The SPI controller pulls the SS pin of the selected
peripheral to a low (0) value to start the communication. The peripheral
is selected depending on the pin polarity that you specify in the
**Chip select pin polarity** parameter. The
controller can select only one peripheral at a time.

### **First bit to transfer** — First bit to transfer for SPI communication `Most significant bit (MSB)` (default) | `Least significant bit (LSB)`

Select the order in which the data is transmitted.

- Most significant bit (MSB) — Select MSB to send the
  most significant bit (MSB) first.
- Least significant bit (LSB) — Select LSB to send
  the least significant bit (LSB) first.

### **Mode (Clock polarity and phase)** — Mode of SPI communication `0` (default) | `1` | `2` | `3`

An SPI controller sets the clock polarity (CPOL) and the clock phase
(CPHA).

The combination of polarity and phase are referred to as SPI modes.
The SPI modes 0–3 are shown in the table.

| Mode | Clock Polarity (CPOL) | Clock Phase (CPHA) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 0 |
| 3 | 1 | 1 |

For more information on register read/write, see SPI Transfer Modes.

### **Register address** — The SPI peripheral register address to read data `0` (default)

Specify this address as an integer or in hexadecimal format by using
`hex2dec()`, for example, ‘hex2dec(‘20’)’.

### **Output data type** — Data type of data read from the SPI peripheral devices `int8` (default) | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

Specify the type of data read from the register of the SPI peripheral
devices.

### **Output data length** — Data size to read from the SPI peripheral devices `1` (default) | `integer greater than or equal to 0`

Specify the length of data read from the register of the SPI
peripheral devices.

### **Sample time** — Frequency to read data from the SPI peripheral devices `0.1` (default)

Specify how often the block reads data from the SPI peripheral
devices. When you specify this parameter as`-1`,
Simulink® determines the best sample time for the block based on
the block context within the model.

### Advanced

### **Chip select pin polarity** — Logic level to establish SPI communication `Active low` (default) | `Active high`

The logic levels supported by Chip select pin to select the SPI
peripheral devices.

- Active low — The device is enabled on logic low. The
  SPI peripheral devices gets enabled when its SS pin is set to
  low.
- Active high — The device is enabled on logic high. The
  SPI peripheral devices gets enabled when its SS pin is set to
  high.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Read data from SPI peripheral devices register

The SPI Register Read block reads the data from registers of a
peripheral devices over the Serial Peripheral Interface (SPI) interface. Using this
block, you can access an SPI device to measure quantities such as temperature, pressure
or to support EEPROM.

For more information on SPI communication, see Support SPI Communication.
