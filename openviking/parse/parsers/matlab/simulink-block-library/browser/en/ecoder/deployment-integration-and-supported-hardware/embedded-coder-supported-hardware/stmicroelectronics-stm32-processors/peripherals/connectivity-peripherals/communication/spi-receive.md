---
type: simulink-block
title: 'SPI Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'spireceive'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/spireceive.html'
language: en
---

# SPI Receive

## Ports

### Output

### **Rx** — SPI receive data vector

The data read from the device over the SPI interface.

**Data Types:** `uint8` | `uint16` | `uint32`

### **Status** — SPI receive status `0` | `1` | `2`

Status of receipt of data. Error status values indicate:

- 0 — No errors.
- 1 — Data loss occurred because of overflow.
- 2 — Data not ready. A time out occurred while the block was
  waiting to receive data.

#### Dependencies

To enable this port, select **Enable status
output** parameter.

**Data Types:** `uint8` | `uint16` | `uint32`

## Parameters

### Main

### **SPI module** — SPI module to read data `SPI1` (default) | `SPI2` | `SPI3` | `SPI4` | `SPI5` | `SPI6`

The SPI module to which the SPI peripheral device is connected. Each
processor has a different number of modules.

### **Clock polarity** — SPI clock polarity `Low` (default) | `High`

The clock polarity used for SPI communication mode. This parameter
must be the same for both transmit and receive blocks.

### **Clock phase** — SPI clock phase `1 Edge` (default) | `2 Edge`

The clock phase used for SPI communication mode. This parameter must
be the same for both transmit and receive blocks.

### **Output data length** — SPI output data length `1` (default) | positive integer

The received data is a vector of type `uint8`,
`uint16` or `uint32` and the data
length is as specified in this parameter (not bytes).

### **Enable status output** — Enable SPI status mode `off` (default) | `on`

When you select the **Enable status
output** parameter, the block configures an output port,
**Status**. The port outputs the SPI
status message.

### **Enable blocking mode** — Enable SPI blocking mode `off` (default) | `on`

When this option is selected, the algorithm waits until data is
received before continuing processing.

### **Sample time** — SPI sample time selection `–1` (default) | `0.1` | scalar

Sample time for the block in seconds. To execute this block
asynchronously, set this parameter to `-1`.

### Advanced

### **Data bits** — Number of bits in SPI transfer `4` (default) | 5 to 32

Length in bits of each transmitted or received character. For example,
if you select `8`, the maximum value that can be
transmitted using SPI is 28–1. If you send
data greater than this value, the buffer overflows. This parameter must
be the same for both transmit and receive blocks.

### **Chip select calling method** — Method to select SPI peripheral device `Provided by the SPI peripheral` (default) | `Explicit GPIO calls`

The SPI controller uses the following methods to select SPI peripheral
devices:

- `Provided by the SPI peripheral` —
  The SPI controller uses the pin provided by the SPI peripheral.
  Peripheral select and deselect are handled by the SPI
  peripheral.
- `Explicit GPIO calls` — The SPI
  controller uses the general purpose input/output pins instead of
  the STE pin of the SPI peripheral to select/deselect SPI
  peripheral devices. The SPI Receive block
  deselects the peripheral using GPIO pins after receiving data.
  To select the peripheral, the SPI Transmit block must be used along with the SPI Receive
  block. Use this option only in controller mode. Select the
  **Enable blocking mode** option to
  ensure that the SPI transmission is complete before the
  peripheral is deselected.

### **Chip select pin polarity** — SPI chip select pin polarity `Active low` (default) | `Active high`

The logic levels supported by the chip select pin to select the SPI
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

### **Chip select pin** — SPI chip select pin `0` (default) | positive integer scalar

The general purpose input/output pin that serves as the peripheral
select for SPI.

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

Receive data through Serial Peripheral Interface (SPI) on target

The SPI Receive block outputs the values received as an
`[Nx1]` array of the `uint8`,
`uint16` or `uint32` data types.

The SPI Receive block supports synchronous, serial peripheral
input/output port communications between the processor and external peripherals or other
controllers. The block can run in either peripheral or controller mode. In controller
mode, the SPI\_MOSI pin transmits data, and the SPI\_MISO pin receives the data. When
controller mode is selected, the SPI initiates the data transfer by sending a serial
clock signal (SPICLK), which is used for the entire serial communications link. Data
transfers are synchronized to this SPICLK, which enables both controller and peripheral
to send and receive data simultaneously. The maximum frequency for the clock is one
quarter of the processor clock frequency.

The SPI device receives data and places the data in the receive buffer. The SPI
Receive block reads the data from the receive buffer. In controller mode,
SPI Transmit the block initiates SPI transmission by writing data to the transmit buffer. Then,
the data received in the receive buffer is read by the SPI Receive block.
In peripheral mode, the SPI Receive block is used to read the data in the
receive buffer, which is received from the controller. Then, the data is written into
the transmit buffer using the SPI Transmit block. From the transmit
buffer, the data is sent to the controller.

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
