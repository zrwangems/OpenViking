---
type: simulink-block
title: 'Timer Capture'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Timer Peripherals'
documentation_page: 'timercapture'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/timercapture.html'
language: en
---

# Timer Capture

## Ports

### Output

### **CH#** — Channel port `scalar`

The channel port output the capture compare register value of the
corresponding selected channel.

**Data Types:** `uint16` | `uint32`

### **Status** — Status of overrun `scalar`

Outputs if overrun occurs during reading the capture compare
register.

- `1` - overrun occurs
- `0` - no overrun

#### Dependencies

To enable this port, select the **Output status**
parameter.

**Data Types:** `uint8`

### **Dir** — Counter direction output `scalar`

The block outputs the current direction of the counter as one of the following:

- `0` - Up counter
- `1` - Down counter

#### Dependencies

To enable this port, select the **Enable timer counter
direction output** parameter.

**Data Types:** `Boolean`

### **Length** — Length of read data `scalar`

The port outputs the length of the data read from the capture compare
register of selected channel.

#### Dependencies

To enable this port, select the **Output data
length** parameter.

**Data Types:** `uint32`

## Parameters

### Main

### **Timer module** — Select timer module `TIM1` (default) | `TIM2` | `TIM3` | `...`

Select the timer module. Number of timer module available will vary
for different processors.

**Note**

Ensure that `Timer module` is also configured
in the STM32CubeMX project.

### **Channel #** — Select channel `CH1` (default) | `CH2` | `CH3` | `CH4`

Select the channel for which you want to read the capture compare
register value.

**Note**

- Ensure that the channels you want to enable are
  configured for `Input mode` in the
  STM32CubeMX project.

  In STM32CubeMX, go to **Timers** > **TIM#** > **Mode** > **Channel#**
- You can configure the selected channel input mode as
  one of the following depending upon your requirement:

  - Input Capture direct mode or Input Capture
    indirect mode or Input Capture triggered by
    TRC(for channels 1-4)
  - PWM input on CH1 or CH2(1 & 2)
  - XOR ON/Hall sensor mode(channel 1-3)

  In STM32CubeMX, go to **Timers** > **TIM#** > **Mode** > **Channel#**

### **Capture data length** — Specify length of data to be read from capture compare register `off` (default) | `on`

Length of data to be read from capture compare register.

- If length is `1` - capture compare register
  is read in polling mode.
- if length is greater than `1` - DMA is used
  to read the specified data length from capture compare
  register.

Ensure to configure the **DMA** in STM32CubeMX
project. In STM32CubeMX, go to**Timers** > **TIM#** > **Configuration** > **DMA settings** and add the DMA for the selected channels.

.

### **Enable timer counter direction output** — Select to Enable timer counter direction output port `off` (default) | `on`

Enable this parameter to output the current direction of the
counter.

### **Output data length** — Select to output length port `off` (default) | `on`

Select this parameter to output the length of read data.

When you select the Output data length parameter, the block
configures an output port, Length.

### **Output status** — Select to enable output status port `off` (default) | `on`

Select this parameter to output status of read data. Status output
`1` indicates overrun error.

When you select the Output Status parameter, the block configures an
output port, Status.

### **Sample time** — Frequency at which enabled output ports are read `-1` (default) | `non-negative real value`

Specify how often (in seconds) the status of enabled output ports are
read if no input ports are selected. Enter a value greater than zero.
When you specify this parameter as -1, Simulink® determines the best sample time for the block based on the
block context within the model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Output the capture compare register value

Output the capture compare register value of the selected timer module and channel
when configured in input mode.

Specify the length of data to be read from the capture compare register in
**Capture data length**. For data length greater than
`1`, DMA must be added for the selected timer module and channel in
STM32CubeMX project.

- Select **Output data length** to output the length of read
  data.
- Select **Output status** to output status of read data.
  Status output `1` indicates overrun error.
- Select **Output direction** to output counter
  direction.

To avoid overrun error while reading capture compare register values, you can place
the timer capture block within function call subsystem connected to Hardware Interrupt block with one of the following events.

- `Capture compare event of the selected timer and channel`
  - If length of capture compare data to be read is equal
  `1`. This ensures block outputs data when capture compare
  event interrupt of the selected timer and channel occurs.

  Ensure that the interrupt for the capture compare event is configured in **Configuration Parameters** > **timers** > **show TIM#** > **Configurations**
- `Transfer complete event of the DMA configured for selected timer
  and channel` - If length of capture compare data to be read is
  greater than `1`. This ensures block outputs data once DMA
  has read the specified length of data from capture compare register and
  transfer complete event Interrupt is generated.
