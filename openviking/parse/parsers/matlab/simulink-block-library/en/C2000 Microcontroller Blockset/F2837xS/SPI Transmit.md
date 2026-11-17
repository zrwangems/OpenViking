---
type: simulink-block
title: 'SPI Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'spitransmit'
documentation_source_path: '../ecoder/stmicroelectronicsstm32f4discovery/ref/spitransmit.html'
language: en
---

# SPI Transmit

## Ports
```yaml
ports:
- name: Tx
  summary: SPI Transmit data vector
  direction: input
  data_types: uint8 | uint16 | uint32
- name: Status
  summary: SPI transmit status 0 | 1 | 2
  direction: output
  data_types: uint8 | uint16 | uint32
```

### Input

### **Tx** — SPI Transmit data vector

The data written to the device over the SPI interface.

**Data Types:** `uint8` | `uint16` | `uint32`
### Output

### **Status** — SPI transmit status 0 | 1 | 2

Status of SPI data transmission. Error status values indicate:

- 0 — No errors.
- 1 — A time-out occurred while the block was transmitting
  data.
- 2 — The transmitted data contains an error.

#### Dependencies

To enable this port, select **Enable status
output** parameter.

**Data Types:** `uint8` | `uint16` | `uint32`
## Parameters
```yaml
parameters:
- name: SPI module
  summary: SPI module to write data SPI1 (default) | SPI2 | SPI3 | SPI4 | SPI5 | SPI6
  group: Main
- name: Clock polarity
  summary: SPI clock polarity Low (default) | High
  group: Main
- name: Clock phase
  summary: SPI clock phase 1 Edge (default) | 2 Edge
  group: Main
- name: Enable status output
  summary: Enable SPI status mode off (default) | on
  group: Main
- name: Enable blocking mode
  summary: SPI blocking mode enable off (default) | on
  group: Main
- name: Data bits
  summary: Number of bits in SPI transfer 8 (default) | 5 to 32
  group: Advanced
- name: Chip select calling method
  summary: Method to select SPI peripheral device Provided by the SPI peripheral (default) | Explicit GPIO calls
  group: Advanced
- name: Chip select pin polarity
  summary: SPI chip select pin polarity Active low (default) | Active high
  group: Advanced
- name: Chip select port name
  summary: SPI chip select port name GPIOA (default) | GPIOB | GPIOC
  group: Advanced
- name: Chip select pin
  summary: SPI peripheral select pin 0 (default) | positive integer scalar
  group: Advanced
```

### Main

### **SPI module** — SPI module to write data `SPI1` (default) | `SPI2` | `SPI3` | `SPI4` | `SPI5` | `SPI6`

The SPI module to which the SPI peripheral device is connected. Each
processor has a different number of modules.

### **Clock polarity** — SPI clock polarity `Low` (default) | `High`

The clock polarity used for SPI communication mode. This parameter
must be the same for both transmit and receive blocks.

### **Clock phase** — SPI clock phase `1 Edge` (default) | `2 Edge`

The clock phase used for SPI communication mode. This parameter must
be the same for both transmit and receive blocks.

### **Enable status output** — Enable SPI status mode `off` (default) | `on`

When you select the **Enable status
output** parameter, the block configures an output port,
**Status**. The port outputs the SPI
status message.

### **Enable blocking mode** — SPI blocking mode enable `off` (default) | `on`

When this option is selected, the algorithm waits until data is sent
before continuing processing.

### Advanced

### **Data bits** — Number of bits in SPI transfer `8` (default) | 5 to 32

Length in bits of each transmitted or received character. For example,
if you select `8`, the maximum value that can be
transmitted using SPI is 28–1. If you send
data greater than this value, the buffer overflows. This parameter must
be the same for both transmit and receive blocks.

### **Chip select calling method** — Method to select SPI peripheral device `Provided by the SPI peripheral` (default) | `Explicit GPIO calls`

The SPI controller uses these methods to select SPI peripheral
devices:

- `Provided by the SPI peripheral` —
  The SPI controller uses the pin provided by the SPI peripheral.
  Peripheral select and deselect are handled by the SPI
  peripheral.
- `Explicit GPIO calls` — The SPI
  controller uses the general purpose input/output pins instead of
  the STE pin of the SPI peripheral to select/deselect SPI
  peripheral devices. The SPI Transmit block
  selects the peripheral using GPIO pins before transmitting data.
  To deselect the peripheral, you must use the SPI Receive block along with the SPI Transmit block. Use
  this option only in controller mode. Select the
  **Enable blocking mode** option to
  ensure that the SPI transmission is complete before the
  peripheral is deselected.

### **Chip select pin polarity** — SPI chip select pin polarity `Active low` (default) | `Active high`

The logic levels supported by chip select pin to select the SPI
peripheral device.

- `Active low` — The device is enabled
  on logic low. The SPI peripheral device is enabled when its chip
  select pin is set to low.
- `Active high` — The device is enabled
  on logic high. The SPI peripheral device is enabled when its
  chip select pin is set to high.

#### Dependencies

This option appears only when **Chip select calling
method** is set to `Explicit GPIO
calls`.

### **Chip select port name** — SPI chip select port name `GPIOA` (default) | `GPIOB` | `GPIOC`

Select the general purpose port name that serves as the chip select
for SPI.

#### Dependencies

This option appears only when **Chip select calling
method** is set to `Explicit GPIO
calls`.

### **Chip select pin** — SPI peripheral select pin `0` (default) | positive integer scalar

The general purpose input/output pin that serves as the chip select
for SPI.

#### Dependencies

This option appears only when **Chip select calling
method** is set to `Explicit GPIO
calls`.
## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Transmit data through Serial Peripheral Interface (SPI) on target

The SPI Transmit block accepts the values as an [Nx1] or [1xN] array of
`uint8`, `uint16` or `uint32`
data types.

The SPI Transmit block supports synchronous, serial peripheral
input/output port communications between the processor and external peripherals or other
controllers. The block can run in either peripheral or controller mode. In controller
mode, the SPI\_MOSI pin transmits data, and the SPI\_MISO pin receives the data. When
controller mode is selected, the SPI initiates the data transfer by sending a serial
clock signal (SPICLK), which is used for the entire serial communications link. Data
transfers are synchronized to this SPICLK, which enables both controller and peripheral
to send and receive data simultaneously.

The SPI Transmit block writes data to the transmit buffer, and the data
is transmitted to the SPI device. In controller mode, the SPI Transmit
block initiates SPI transmission by writing the data to the SPI transmit buffer. The
SPI Receive block must be used along with the SPI Transmit block to read the data
received in the receive buffer. In peripheral mode, the SPI Receive block
is used to read the data in the receive buffer, which is received from the controller.
Then, the data is written into the transmit buffer using the SPI Transmit
block. From the transmit buffer, the data is sent to the controller.

The sampling rate is inherited from the input port. The supported data type is
`uint8`, `uint16`, and
`uint32`.

The SPI transmit interrupt is configured for a specific hardware board by navigating
to **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources**.

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
