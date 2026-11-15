---
type: simulink-block
title: 'Higher Resolution Timer'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Timer Peripherals'
documentation_page: 'higherresolutiontimer'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/higherresolutiontimer.html'
language: en
---

# Higher Resolution Timer

## Ports

### Input

### **CMP#** — Counter compare port `scalar`

Use this port to enable input port counter compare.

#### Dependencies

To enable this port, select the **Enable compare# (CMP#)
input** parameter under **Counter
Compare** tab.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **PER** — Frequency count of timer `scalar`

The input at this port determines the frequency of the counter.
Depending on the STM32CubeMX configuration for preload, this value is
either written directly to the active register or preload
register.

The frequency count for 16 bit timers is between `0`
to `0xFFFF`.

#### Dependencies

To enable this port, select the **Enable frequency
input** parameter under **Main**
tab.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CEN** — Port to enable counter `scalar`

Use this port to enable input port counter. Set the port to one of
these values.

- `0` - Disable counter
- `1` - Enable counter

#### Dependencies

To enable this port, select the **Enable input to
enable/disable counter** parameter under
**Main** tab.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CAL** — Port to enable calibration input `scalar`

Use this port to enable calibration input.

#### Dependencies

To enable this port, select the **Enable delayed-locked
loop(DLL) calibration input** parameter under
**Main** tab.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **SWU** — Input to generate update event `scalar`

Use this port to generate an update event. When you specify a value of
`1`, the port generates an update event.

#### Dependencies

To enable this port, select the **Enable update generation
event input** parameter under
**Event** tab.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **SST#** — Software set trigger `scalar`

Use this port to software set trigger event input. When you specify a
value of `1`, the port generates an software set
trigger event.

#### Dependencies

To enable this port, select the **Enable channel# software
set trigger(SST#) event input** parameter under
**Event** tab.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **SRT#** — Software reset trigger `scalar`

Use this port to software reset trigger event input. When you specify
a value of `1`, the port generates an software reset
trigger event.

#### Dependencies

To enable this port, select the **Enable channel# software
reset trigger(SRT#) event input** parameter under
**Event** tab.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`
### Output

### **ODS#** — Status of channel output `scalar`

Output the status of the selected channel.

#### Dependencies

To enable this port, select the **Enable channel# status
output** parameter under **Main**
tab.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

## Parameters

### Main

### **Timer module** — Select timer module `TIMERA` (default) | `TIMERB` | `TIMERC` | `TIMERD` | `TIMERE` | `TIMERF` | `MAINTIMER`

Select the timer module.

**Note**

Ensure that `Timer module` is also configured
in the STM32CubeMX project.

### **Enable channel#** — Select channel `Enable channel 1` (default) | `Enable channel 2`

Enable the channels on which you want the block to generate the PWM
output. The input considers the duty cycle of the corresponding
channels. Depending on the enabled inputs for counter compare and output
set/reset STM32CubeMX configuration for match events, the high
resolution pulse width modulated waveform can be generated on channel1
or channel2 or both.

Each **Timer module** can have one to six channels.
Number of channels available vary based on the timer module selected.
Enable the channel supported for the corresponding timer. By default,
the block enables **channel 1**.

**Note**

Ensure the Timer module whose channels you want to enable are
configured in the STM32CubeMX project

### **Enable frequency input** — Enable frequency through input port `off` (default) | `on`

Enable this parameter to set the frequency of the timer. All the
channel outputs have the same frequency.

When you select the **Enable frequency input**
parameter, the block configures an input port, PER.

**Note**

HRTIM block supports updating the period register via block
input. There is a limit to the minimum frequency that can be
generated for the given pre-scaler settings. For more
information, see STM32H7xx TRM manual.

### **Enable input to enable/disable counter** — Enable counter through input port `off` (default) | `on`

Enable or disable the counter through the input port. If you do not
select this parameter, then the counter is enabled during model
initialization.

When you select the **Enable input to enable/disable
counter** parameter, the block configures an input port,
CEN.

### **Enable channel# status output** — Enable to configure channel output status port `off` (default) | `on`

Select this parameter to output channel status. Status output
`1` indicates overrun error.

When you select the **Enable channel# status output**
parameter, the block configures an output port, ODS. The port outputs
the status of channel output message.

### **Enable delayed-locked loop (DLL) calibration input** — Enable to configure output status port `off` (default) | `on`

Select this parameter to output status of read data. Status output
`1` indicates overrun error.

When you select the **Enable delayed-locked loop (DLL)
calibration input** parameter, the block configures an
input port, CAL.

### Counter Compare

### **CMP unit** — Units used by compare registers `Counts` (default) | `Percentage`

Select the `Counts` or `Percentage`
units used by compare registers.

### **Enable compare# (CMP#) input** — Generate update event `off` (default) | `on`

Enable this parameter to counter compare input port.

When you select the **Enable compare# (CMP#) input**
parameter, the block configures an input port, CMP#.

### Events

### **Enable update generation event input** — Generate update event `off` (default) | `on`

Enable this parameter to generate an update event through input
port.

When you select the **Enable update generation event
input** parameter, the block configures an input port,
SWU.

### **Enable channel# software set trigger(SST#) event input** — Software set trigger `off` (default) | `on`

Enable this parameter to set channel software trigger event
input.

When you select the **Enable channel# software set
trigger(SST#) event input** parameter, the block configures
an input port, SST#.

### **Enable channel# software reset trigger(SRT#) event input** — Software reset trigger `off` (default) | `on`

Enable this parameter to reset channel software trigger event
input.

When you select the **Enable channel# software reset
trigger(SRT#) event input** parameter, the block configures
an input port, SRT#.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Generate high resolution pulse width modulated waveforms

Generate high resolution pulse width modulated waveforms on the enabled outputs using
the high resolution timer module.

The inputs to the Higher Resolution Timer block control the frequency
and duty cycle (via the compare inputs) of the square waveform for each output.

**Note**

Some HRTIM registers are preload enabled. If preload is enabled, ensure at
least one of the update event is configured to enable copying of preload
register to the active register.
