---
type: simulink-block
title: 'Digital to Analog Converter'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Analog Peripherals'
documentation_page: 'digitaltoanalogconverter'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/digitaltoanalogconverter.html'
language: en
---

# Digital to Analog Converter

## Ports

### Input

### **dln/dInCh#** — Data input port scalar

The port accepts the input range of :

- `0-4095` - 12-bit data
  length and right alignment of data.
- `0-65520` - 12-bit data
  length and left alignment of data
- `0-255` - 8-bit data length

Selecting dual channel enables 2 **dInCh#** input ports.

#### Dependencies

To enable this port, set the
`Mode` to **Write
only** or **Write and
trigger** parameter.

**Data Types:** `uint8` | `uint16`

### **baseValue** — Base value scalar

This port sets the offset value for the DAC
channel.

#### Dependencies

To enable this port, set the
**Mode** to `Trigger
only` and set the **Waveform
type** to
`Noise/Triangular`.

**Data Types:** `uint16`

### **stepData** — Step data scalar

This port sets the step value for sawtooth
waveform in `12.4` bit
format.

#### Dependencies

To enable this port, set the
**Mode** to `Trigger
only` and set the **Waveform
type** to
`Sawtooth`.

**Data Types:** `uint16`

### **trigln/trigInCh#** — Trigger input port boolean

Triggers conversion on the specified
channel.

Selecting dual channel enables 2 **trigInCh#** input
ports.

#### Dependencies

To enable this port, set the
`Mode` to **Write and
trigger** or **Trigger
only** parameter.

**Data Types:** `Boolean`

### **stepTrigIn/stepTrigInCh#** — Software step trigger boolean

This port triggers the change of DAC output by
a value specified in the step data.

Selecting dual channel enables 2 **stepTrigInCh#** input
ports.

#### Dependencies

To enable this port, select **Enable
software step trigger (Trigger 2)**
parameter. Ensure to set the
**Mode** to `Trigger
only` parameter and set
**Waveform type** to
`sawtooth`.

**Data Types:** `Boolean`

### **rstTrigIn/rstTrigInCh#** — Software reset step trigger boolean

This port resets the DAC value to the value
specified in the STM32 CubeMX project.

Selecting dual channel enables 2 **rstTrigInCh#** input
ports.

#### Dependencies

To enable this port, select **Enable
software reset trigger (Trigger 1)**
parameter. Ensure to set the
**Mode** to `Trigger
only` parameter and set
**Waveform type** to
`sawtooth`.

**Data Types:** `Boolean`

### **dacEnable** — DAC enable boolean

This port allows the user to enable and
disable the DAC in runtime.

#### Dependencies

To enable this port, select the
**Control input for DAC enable**
parameter.

**Data Types:** `Boolean`
### Output

### **Status** — Status of DAC boolean

With the DAC block, the DAC module can now be
disabled after it has been enabled. Additionally,
the status output now has three states indicating
the following:

- `0` - the DAC has been
  enabled and is operating as expected
- `1` - the DAC has been
  disabled successfully
- `2` - an error occurred
  during command execution

#### Dependencies

To enable this port, select the
**Output status**
parameter.

**Data Types:** `uint8`

## Parameters

### **DAC module** — DAC module for conversion `DAC1` (default) | `DAC2` | `DAC3` | `DAC4`

Select an digital analog converter module for
conversion.

### **Mode** — Option to trigger DAC start of conversion `Write only` (default) | `Write and trigger` | `Trigger only`

Select the mode of conversion.

- `Write only`
  —

  Write only option enables user to write the
  data on to the data holding register of DAC.

  - Convert data to analog value without any
    involvement of trigger. This requires trigger
    source to be `None`.
  - Write the digital value to a channel that is
    triggered by an internal trigger source. This
    requires the trig source to be one of the timer
    based trig sources available in the STM32 CubeMX
    project.

  This option also enables the input port
  **dIn**.
- `Write and trigger`
  — Write and trigger enables user to write
  data to DHR of DAC and control the point of
  conversion. This requires the trigger source to be
  set to software.

  This option enables the input port
  **TrigIn** and
  **dIn**.
- `Trigger only`
  — Select this option when you want to
  trigger the conversion.

  - when the data is written by some internal
    mechanism to DHR and user need to control the
    point of triggering.
  - For wave generation

  This option enables the input port
  **Stepdata**

### **Channel select** — Select DAC channel `Channel1` (default) | `Channel2` | `Dual channel`

Select an digital analog converter module channel on
which the conversion should be performed. Select the
dual channel option to control both the channels of
a module together.

Selecting dual channel enables 2
**dIn/dInCh#** input
ports.

### **Trigger configuration** — Select trigger configuration `Independent` (default) | `Simultaneous`

Trigger configuration specifies if both the channels
need to be triggered either simultaneously or
independently.

#### Dependencies

To enable this parameter, set the
**Mode** as `Write and
trigger` or `Trigger
only` and **Channel
select** as `Dual
channel`.

### **Waveform generation enable** — Enable waveform generation `off` (default) | `on`

Select to enable the waveform generation on the
selected channel. If **waveform generation
enable** parameter is not selected and
**software trigger** is not
enabled, then `dacEnable` port
would be a default port.

#### Dependencies

To enable this parameter, set the
**Mode** as `Trigger
only`.

### **Waveform type** — Select DAC waveform type `Noise/Triangular` (default) | `Sawtooth`

Select the waveform type to be generated on the DAC
channel.

- Selecting
  `Noise/Triangular` waveform type,
  enables **baseValue** as default
  port.
- Selecting `sawtooth`
  waveform type, enables **stepData** as default port.

Select dual channel for independent or simultaneous
conversion.

#### Dependencies

To enable this parameter, set the
**Mode** as `Trigger
only`.

### **Enable software trigger (Trigger 1)** — Select software trigger `on` (default) | `off`

Select to trigger the DAC conversion via software
trigger. When you select this parameter, the block
configures an input port, **TrigIn/TriInCh#**.

#### Dependencies

To enable this parameter, set the
**Mode** as `Trigger
only` and **Waveform
type** as
`Noise/Triangular`.

### **Software step trigger enable** — Enable software step trigger `on` (default) | `off`

Triggers the conversion on DAC channel with a value
specified in step data when sawtooth waveform is
selected.

When you select this parameter, the block configures
an input port, **stepTrigIn/stepTrigInCh#**.

#### Dependencies

To enable this parameter, set the
**Mode** as `Trigger
only` and **Waveform
type** as
`Sawtooth`.

### **Software reset trigger enable** — Enable software reset trigger `off` (default) | `on`

Select to enable software reset trigger the digital
analog converter module. When you select this
parameter, the block configures an input port,
**rstTrigIn/rstTrigInCh#**.

#### Dependencies

To enable this parameter, set the
**Mode** as `Trigger
only` and **Waveform
type** as
`Sawtooth`.

### **Data length** — Select data length of DAC `12` (default) | `8`

Select the data length of digital analog converter
module.

#### Dependencies

To enable this parameter, set
**Mode** as `Write
only` or `Write and
Trigger`.

### **Data alignment** — Select data alignment of DAC `Right alignment` (default) | `Left alignment`

Select the data alignment of digital analog converter
module. For 8 bit data length, the right alignment
is the default option.

If data length and alignment is selected as
:

- 12-bit and right alignment, input range is
  `0-4095`
- 12-bit and left alignment, input range is
  `0-65520`
- 8-bit, input range is
  `0-255`

#### Dependencies

To enable this parameter, set the
**Mode** as `Write
only` or `Write and
Trigger`.

### **Output Status** — Enable output status `off` (default) | `on`

When you select the **Output Status**
parameter, the block configures an output port,
**Status**. The port outputs the
status message.

### **Control input for DAC enable** — DAC enable input `off` (default) | `on`

When you select the **Control input for DAC
enable** parameter, the block configures
an output port, **dacEnable**.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Configures the DAC to generate an analog voltage on the specified DAC channel

The Digital to Analog Converter block converts digital value to
equivalent analog voltage on a corresponding channel of the module.

For **STM32xx based board**, the input channels
for the DAC block can be configured in STM32CubeMX project.

**Note**

DMA functionality is not supported in the DAC.
