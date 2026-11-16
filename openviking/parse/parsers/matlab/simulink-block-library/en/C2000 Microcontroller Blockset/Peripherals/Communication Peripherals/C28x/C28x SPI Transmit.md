---
type: simulink-block
title: 'C28x SPI Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xspitransmit'
documentation_source_path: 'ref/c28xspitransmit.html'
language: en
---

# C28x SPI Transmit

## Ports

### Input

### **Tx** — SPI Transmit data vector

The data written to the device over the SPI interface.

**Data Types:** `uint16`
### Output

### **Status** — SPI transmit status 0 | 1 | 2

Status of SPI data transmission. Error status values indicate:

- 0 — No errors.
- 1 — A time-out occurred while the block was transmitting
  data.
- 2 — The transmitted data contains an error.

#### Dependencies

This port appears only when **Enable blocking
mode** is not selected.

**Data Types:** `uint16`

## Parameters

### Main

### **SPI module** — SPI module to write data `SPI_A` (default) | `SPI_B` | `SPI_C` | `SPI_D`

The SPI module to which the SPI peripheral device is connected. Each
processor has a different number of modules.

### **Clock polarity** — SPI clock polarity `Rising_edge` (default) | `Falling_edge`

The clock polarity used for SPI communication mode. This parameter
must be the same for both transmit and receive blocks.

### **Clock phase** — SPI clock phase `No_delay` (default) | `Delay_half_cycle`

The clock phase used for SPI communication mode. This parameter must
be the same for both transmit and receive blocks.

### **Enable blocking mode** — SPI blocking mode enable `off` (default) | `on`

When this option is selected, the algorithm waits until data is sent
before continuing processing.

### Advanced

### **Data bits** — Number of bits in SPI transfer `8` (default) | integer in [1 16]

Length in bits of each transmitted or received character. For example,
if you select `8`, the maximum value that can be
transmitted using SPI is 28–1. If you send
data greater than this value, the buffer overflows. This parameter must
be the same for both transmit and receive blocks.

### **Chip select calling method** — Method to select SPI peripheral device `Provided by the SPI peripheral` (default) | `Explicit GPIO calls`

The SPI controller uses these methods to select SPI peripheral
devices:

- `Provided by the SPI peripheral` —
  The SPI controller uses the STE pin assignment provided in **Hardware Implementation** > **Target hardware resources** > **SPI** to select the peripheral device. peripheral select
  and deselect are handled by the SPI peripheral.
- `Explicit GPIO calls` — The SPI
  controller uses the general purpose input/output pins instead of
  the STE pin of the SPI peripheral to select/deselect SPI
  peripheral devices. The SPI Transmit block
  selects the peripheral using GPIO pins before transmitting data.
  To deselect the peripheral, you must use the C28x SPI Receive block along with the SPI Transmit block. Use
  this option only in controller mode. Select the
  **Enable blocking mode** option to
  ensure that the SPI transmission is complete before the
  peripheral is deselected.

### **Chip select pin polarity** — SPI chip select pin polarity `Active low` (default) | `Active high`

The logic levels supported by chip select pin to select the SPI
peripheral device.

- `Active low` — The device is enabled
  on logic low. The SPI peripheral device is enabled when its
  peripheral select pin is set to low.
- `Active high` — The device is enabled
  on logic high. The SPI peripheral device is enabled when its
  peripheral select pin is set to high.

#### Dependencies

This option appears only when **Chip select calling
method** is set to `Explicit GPIO
calls`.

### **Chip select pin** — SPI peripheral select pin `0` (default) | positive integer scalar

The general purpose input/output pin that serves as the peripheral
select for SPI.

#### Dependencies

This option appears only when **Chip select calling
method** is set to `Explicit GPIO
calls`.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Transmit data through Serial Peripheral Interface (SPI) on target

The SPI Transmit block supports synchronous, serial peripheral
input/output port communications between the processor and external peripherals or other
controllers. The block can run in either peripheral or controller mode. In controller
mode, the SPISIMO pin transmits data, and the SPISOMI pin receives the data. When
controller mode is selected, the SPI initiates the data transfer by sending a serial
clock signal (SPICLK), which is used for the entire serial communications link. Data
transfers are synchronized to this SPICLK, which enables both controller and peripheral
to send and receive data simultaneously. The maximum frequency for the clock is one
quarter of the processor clock frequency.

The SPI Transmit block writes data to the transmit buffer, and the data
is transmitted to the SPI device. In controller mode, the SPI Transmit
block initiates SPI transmission by writing the data to the SPI transmit buffer. The
C28x SPI Receive block must be used
along with the SPI Transmit block to read the data received in the
receive buffer. In peripheral mode, the SPI Receive block is used to read
the data in the receive buffer, which is received from the controller. Then, the data is
written into the transmit buffer using the SPI Transmit block. From the
transmit buffer, the data is sent to the controller.

**Note**

To communicate with multiple peripherals using the same SPI module, use
multiple instances of the SPI block with the same module and configure a unique
chip select for each instance.

The sampling rate is inherited from the input port. The supported data type is
`uint16`.

When the SPI transmit interrupt is configured, the transmit FIFO interrupt flags are
cleared in the step function instead of the interrupt service routine. After the data is
placed in the transmit buffer, the transmit FIFO interrupt is set and the previous
transmit interrupt FIFO flags are cleared. Configure the SPI modules for a specific
hardware board by navigating to **Hardware Implementation** > **Target hardware resources**. Verify that these settings meet the requirements of your
application.
