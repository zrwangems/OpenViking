---
type: simulink-block
title: 'Encoder'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Timer Peripherals'
documentation_page: 'encoder'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/encoder.html'
language: en
---

# Encoder

## Ports

### Input

### **Reset** — Input port to reset timer counter `scalar`

Use this port to reset the timer counter.

Providing input as `1`, it sets the counter value to:

- `0` - If the timer counter is counting
  upwards
- `AutoReload Register (ARR) value` - if
  the timer counter is counting downwards.

#### Dependencies

To enable this port, select the **Enable timer counter
reset input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`
### Output

### **Count** — Timer counter output `scalar`

The `Count` port outputs the current timer counter
value as `uint32` data.

**Data Types:** `uint32`

### **Dir** — Counter direction output `scalar`

The block outputs the current direction of the counter as one of the following:

- 0 - Up counter
- 1 - Down counter

#### Dependencies

To enable this port, select the **Enable timer counter
direction output** parameter.

**Data Types:** `Boolean`

### **Status** — Status of encoder `scalar`

The port outputs if any index or transition error are detected.

- `0` - No error is detected
- `1` - Transition error is detected
- `2` - Index error is detected
- `3`- Both Index and transition error are
  detected

Index error is detected when `IERRF` flag is set and
transition error is detected when `TERRF` flag is set
in the `TIMx_SR` status register. For more information,
see Encoder error management section in the STM32G4xx reference
manual.

**Note**

The `Status` port is available only for
STM32G4xx based boards.

#### Dependencies

To enable this port, select the **Output status**
parameter.

**Data Types:** `uint8`

### **Index Recvd** — Status of index pulse `scalar`

Outputs `0` till the first index pulse is received.

- `0` - Until the first index pulse is
  received
- `1` - After the first index pulse is
  received

**Note**

- The `Index Recvd` port is
  available only for STM32G4xx based boards.
- Enable this port only if **Encoder Mode +
  index** is set as `Combined
  Channels` mode in STM32CubeMX project
  (Timer > TIM# > Mode > Combined Channels).

#### Dependencies

To enable this port, select the **Output if first index
pulse is received** parameter.

**Data Types:** `Boolean`

## Parameters

### **Timer module** — Select timer module `TIM1` (default) | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM20`

Select the timer module.

**Note**

- Ensure that `Timer module` is also
  configured in the STM32CubeMX project.
- Ensure the **Combined channels mode**
  in STM32CubeMX project (Timer > TIM# > Mode > Combined
  Channels) is:

  - `Encoder Mode` - for
    STM32H7xx, F7xx and F4xx boards
  - `Encoder Mode or Encoder Mode +
    Index` - for STM32G4xx board

### **Enable timer counter reset input** — Enable input to reset counter `off` (default) | `on`

Enable the input to reset the counter.

Enabling this option adds an input port **Reset**, which
can be used to reset the timer counter value.

### **Enable timer counter direction output** — Select output counter direction `off` (default) | `on`

Enable this parameter to output the current direction of the
counter.

### **Show encoder counts only after first index pulse is received** — Select to show encoder counts only after first index pulse is received `off` (default) | `on`

Enable this parameter to show encoder counts only after first index pulse
is received.

If this parameter is selected, the counts port outputs
`0` till the first index pulse is received. After
receiving the first index pulse, counts port outputs the current timer
counter value.

**Note**

- This parameter is available only for STM32G4xx based
  boards.
- Enable this port only if **Encoder Mode +
  index** is set as `Combined
  Channels` mode in STM32CubeMX project (Timer > TIM#
  > Mode > Combined Channels).

### **Output if first index pulse is received** — Select to show first index pulse is received `off` (default) | `on`

When you select the `Output if first index pulse is
received` parameter, the block configures an output port,
`Index Recvd`. This port outputs `0`
till the first index pulse is received.

**Note**

- This parameter is available only for STM32G4xx based
  boards.
- Enable this port only if **Encoder Mode +
  index** is set as `Combined
  Channels` mode in STM32CubeMX project (Timer > TIM#
  > Mode > Combined Channels).

### **Output status** — Enable to configure output status port `off` (default) | `on`

Select this parameter to output status of read data. Status output
`1` indicates overrun error.

When you select the Output Status parameter, the block configures an
output port, Status. This port outputs if any Index or transition error is
detected.

### **Sample time** — Frequency at which enabled output ports are read `-1` (default) | `non-negative real value`

Specify how often (in seconds) the status of enabled output ports are read
if no input ports are selected. Enter a value greater than zero. When you
specify this parameter as -1, Simulink® determines the best sample time for the block based on the
block context within the model.

#### Dependencies

To enable this port, unselect the **Enable timer counter reset
input** parameter.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Measure rotation of encoder in counts

Measure the rotation of the encoder in counts.

The `Count` port outputs the timer counter value as
`uint32` data.
