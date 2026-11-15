---
type: simulink-block
title: 'Analog to Digital Converter'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'analogtodigitalconverter'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/analogtodigitalconverter.html'
language: en
---

# Analog to Digital Converter

## Ports

### Input

### **Trigger** — Port to trigger conversion scalar

Convert analog signal on ADC input pin to
digital signal.

#### Dependencies

To enable this port, set the **Block
action** parameter to `Trigger
via input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Data** — ADC digital data scalar

The block outputs converted digital data of
analog channel.

#### Dependencies

To enable this port, set the **Block
action** parameter to `Trigger,
wait and read results`.

**Data Types:** `uint16`

## Parameters

The Analog to Digital Converter dialog box contains
three tabs:

- **Configuration** —
  Identify the configuration settings for the block.
- **Channel Selection** —
  Specify the channel details for conversion.
- **Interrupts and Status flags** —
  Set the interrupt and the flag status.

### Configuration

### **ADC module** — ADC module for conversion `ADC1` (default) | `ADC2` | `ADC3`

Select an ADC module for conversion.

### **ADC conversion group** — Option for ADC conversion `Injected group` (default) | `Regular group`

Select one of the following options for conversion.

- `Injected group` —
  You can convert up to 4 analog signals. In this mode, you can ‘inject’
  the ADC conversion during the conversion of regular group channels.
- `Regular group` —
  You can convert up to 16 analog signals.

### **Block configuration** — Option to trigger analog to digital conversion `Software start of conversion` (default) | `External start of conversion` | `Trigger start of conversion after regular group (JAUTO)` | `Only read results`

Select one of the following options for conversion.

- `Software start of conversion` –
  Select this option to start the ADC conversion based on the software
  request.
- `External start of conversion` –
  Select this option to start the ADC conversion based on the external
  event.
- `Trigger start of conversion after regular
  group (JAUTO)` – Select this option to start the
  injected group conversion after completion of the regular group channels.
  This option is available only when you select `Injected
  group` in **ADC conversion group**.
- `Only read results` —
  In this mode, the block output emits the analog to digital conversion
  result for the selected analog channel only. The block does not configure
  the selected ADC module.

### **Block action** — Option to trigger the ADC conversion for ‘Software start of conversion’ option in ‘Block configuration’ parameter `Trigger, wait and read results` (default) | `Trigger via input port`

Select the option to trigger the ADC conversion for ‘Software
start of conversion’ option in ‘Block configuration’
parameter.

- `Trigger, wait and read results` —
  Select this option to trigger ADC conversion every sample time. The
  block output waits until the conversion is completed and emits the
  results. This option is enabled when you select ‘Software start
  of conversion’ in ‘Block configuration’ parameter.
- `Trigger via input port`  —
  Select this option to trigger ADC conversion on input 'Trigger'. The
  ADC conversion is triggered when input is true. As the ADC block does
  not emit the conversion result, use another ADC block with 'Only read
  results' for ‘Block configuration’ parameter. This option
  helps to read the ADC conversion results in triggered or enabled subsystems.

### **Enable continuous conversion** — Option to configure ADC for continuous conversion mode off (default) | on

The ADC is configured for continuous conversion mode. This
option is available only when you select `Regular group` for **ADC
conversion group**.

### **Enable EOC signal at the end of each channel conversion** — Option to indicate the end of conversion after each channel conversion off (default) | on

The option that you select to indicate the end of conversion
after each channel conversion. This option is available only when
you select `Regular group` for **ADC
conversion group**.

### **External trigger event selection** — ADC module for conversion Timer 1 CC1 (default) | Timer 1 CC2 | Timer 1 CC3 | Timer 2 CC2 | Timer 2 CC3 | Timer 2 CC4 | Timer 2 TRGO | Timer 3 CC1 | Timer 3 TRGO | Timer 4 CC4 | Timer 5 CC1 | Timer 5 CC2 | Timer 5 CC3 | Timer 8 CC1 | Timer 8 TRGO | EXTI line 11

Select the polarity of the external event based on which the
ADC is triggered.

### **Sample time** — The frequency at which the block reads pin value -1 (default)

Specify how often this block reads the pin value, in seconds.
Enter a value greater than zero.

### Channel Selection

### **Number of channels to be converted** — Number of channels for conversion 1 (default) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16

Select the number of channels for conversion.

### **1st Conversion** — The first channel for conversion ADC Channel 0 (default) | ADC Channel 1 | ADC Channel 2 | ADC Channel 3 | ADC Channel 4 | ADC Channel 5 | ADC Channel 6 | ADC Channel 7 | ADC Channel 8 | ADC Channel 9 | ADC Channel 10 | ADC Channel 11 | ADC Channel 12 | ADC Channel 13 | ADC Channel 14 | ADC Channel 15 | ADC Channel 16 (Temp. sensor) | ADC Channel 17 (V\_REFINT) | ADC Channel 18 (V\_BAT)

Select the channel for the first conversion.

### **2nd Conversion** — The second channel for conversion ADC Channel 0 (default) | ADC Channel 1 | ADC Channel 2 | ADC Channel 3 | ADC Channel 4 | ADC Channel 5 | ADC Channel 6 | ADC Channel 7 | ADC Channel 8 | ADC Channel 9 | ADC Channel 10 | ADC Channel 11 | ADC Channel 12 | ADC Channel 13 | ADC Channel 14 | ADC Channel 15 | ADC Channel 16 (Temp. sensor) | ADC Channel 17 (V\_REFINT) | ADC Channel 18 (V\_BAT)

Select the channel for the second conversion. You can select
an ADC channel for second conversion, if the **Number of channels
to be converted** is more than 1.

### **nth Conversion** — The nth channel for conversion ADC Channel 0 (default) | ADC Channel 1 | ADC Channel 2 | ADC Channel 3 | ADC Channel 4 | ADC Channel 5 | ADC Channel 6 | ADC Channel 7 | ADC Channel 8 | ADC Channel 9 | ADC Channel 10 | ADC Channel 11 | ADC Channel 12 | ADC Channel 13 | ADC Channel 14 | ADC Channel 15 | ADC Channel 16 (Temp. sensor) | ADC Channel 17 (V\_REFINT) | ADC Channel 18 (V\_BAT)

Select the channel for the nth conversion
where n = 4 for the Injected group and n = 16 for the Regular group.
You can select an ADC channel for nth conversion
if the **Number of channels to be converted** is
more than 1.

### Interrupts and Status flags

### **Post over run interrupt** — Option to emit overrun status off (default) | on

Select the option to emit the overrun status in the block output.

### **Post watchdog interrupt** — Option to emit watchdog interrupt off (default) | on

Select the option to emit the watchdog interrupt.

### **Post end of conversion interrupt** — Option to emit the end of conversion interrupt off (default) | on

Select the option to emit the end of conversion interrupt.

### **Output over run status** — Option to emit the over run status off (default) | on

Select the option to emit the over run status.

### **Output watchdog status** — Option to emit the conversion status out of watchdog thresholds

Select the option to emit the status about the conversion being
out of the watchdog thresholds.

### **Output start of conversion status** — Option to emit the status about the beginning of conversion off (default) | on

Select the option to emit the status about the start of conversion.

### **Output end of conversion status** — Option to emit the status about the end of conversion off (default) | on

Select the option to emit the status about the end of conversion.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Convert analog signal on ADC input pin to digital signal

Measure the voltage of an analog pin relative to the analog input reference voltage on the
STM32F4-Discovery™ board. The block output emits analog voltage in varying ranges
based on the conversion resolution selected for the ADC in Configuration
parameters > Hardware Implementation > Hardware board > Target
hardware resources > ADCx > Conversion resolution.

**Note**

The conversion time for ADC channels is configured based on
the ADC resolution and sample time specified in **Configuration parameters** > **Hardware Implementation** > **Hardware board** > **Target hardware resources** >  **ADCx**.

For example: When you select 12-bits as resolution for ADC1,
the block output emits the analog voltage ranging from 0 to 4095.
If the measured voltage equals the ground voltage, the block output
emits 0. If the measured voltage equals the analog reference voltage,
the block output emits 4095.

You can read up to 16 channels of analog signals from ADC1,
ADC2, or ADC3 modules in single, continuous, scan, or discontinuous
modes.

The table shows the analog pins corresponding to the channels
of the ADC modules that can use these pins to measure the voltage.

For example, ADC modules 1, 2, and 3 that corresponds to channel
12 can use the PC2 pin to measure the voltage. Here, PC2 refers to
pin 2 on port C.

ADC pin mapping
