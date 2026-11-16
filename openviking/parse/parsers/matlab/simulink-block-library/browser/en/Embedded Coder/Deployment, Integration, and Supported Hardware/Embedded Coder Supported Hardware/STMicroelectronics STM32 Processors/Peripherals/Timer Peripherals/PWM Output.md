---
type: simulink-block
title: 'PWM Output'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Timer Peripherals'
documentation_page: 'pwmoutputblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/pwmoutputblock.html'
language: en
---

# PWM Output

## Ports

### Input

### **CH#** — Channel port `scalar`

The input port considers the duty cycle of the corresponding
channel.

If you set the **Duty cycle units** parameter to
`Percentage`, specify a value range between
`0` to `100`. If you set the duty
cycle unit to `Counts`, specify a value range for 32
bit timers between `0` to `0xFFFFFFFF`
and for 16 bit timers between `0` to
`0xFFFF`.

#### Dependencies

To enable this port, select the **Enable
channel** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CC#E** — Capture/compare enable input port `scalar`

The input port considers capture/compare enable input of the
corresponding channel.

#### Dependencies

To enable this port, select the **Enable Capture/Compare
Enable (CC#E) input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CC#NE** — Capture/compare complementary enable input port `scalar`

The input port considers capture/compare complementary enable input of
the corresponding channel.

#### Dependencies

To enable this port, select the **Enable Capture/Compare
Complementary Enable (CC#NE) input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **OC#M** — Output compare mode input port `scalar`

The input port considers output compare mode input of the
corresponding channel.

#### Dependencies

To enable this port, select the **Enable Output Compare
Mode (OC#M) input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CEN** — Port to enable counter `scalar`

Use this port to enable input port counter. Set the port to one of
these values.

- `0` - Disable counter
- `1` - Enable counter

#### Dependencies

To enable this port, select the **Enable input to
enable/disable timer** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **MOE** — Main output enable `scalar`

This main output enable (MOE) bit is cleared asynchronously by the
hardware as soon as the break input is active.

If input is `1`, then the MOE bit is set as
`1`.

#### Dependencies

To enable this port, select the **Enable main output
enable (MOE) input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **freq count** — Frequency count of timer `scalar`

The input at this port determines the frequency of the counter. This
value is written directly to the auto reload register.

The frequency count for 32 bit timers is between `0`
to `0xFFFFFFFF` and for 16 bit timers is between
`0` to `0xFFFF`.

#### Dependencies

To enable this port, select the **Enable frequency
input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **UG** — Input to generate update event `scalar`

Use this port to generate an update event. When you specify a value of
`1`, the port generates an update event.

#### Dependencies

To enable this port, select the **Enable update generation
event input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CC#G** — Capture compare generation event input `scalar`

Use this port to generate capture compare generation event. When you
specify a value of `1`, the port generates an capture
compare event.

#### Dependencies

To enable this port, select the **Enable capture compare #
generation event input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **TG** — Trigger generation `scalar`

Use this port to generate trigger event. When you specify a value of
`1`, the port generates an trigger event.

#### Dependencies

To enable this port, select the **Enable trigger
generation event input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **BG** — Break generation `scalar`

Use this port to generate break generation event. When you specify a
value of `1`, the port generates an break generation
event.

#### Dependencies

To enable this port, select the **Enable break generation
event input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **B2G** — Break generation 2 event `scalar`

Use this port to generate break 2 generation event. When you specify a
value of `1`, the port generates an break 2 generation
event and MOE status is cleared.

#### Dependencies

To enable this port, select the **Enable break generation
2 event input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`
### Output

### **direction** — Counter direction output `scalar`

The block outputs the current direction of the counter as one of the following:

- 0 - Up counter
- 1 - Down counter

#### Dependencies

To enable this port, select the **Enable timer counter
direction output** parameter.

**Data Types:** `Boolean`

### **MOE status** — Status of main output enable bit `scalar`

Status of the main output enable (MOE) bit.

#### Dependencies

To enable this port, select the **Enable main output
enable (MOE) status output** parameter.

**Data Types:** `Boolean`

### **msg CH *`n`*** — SoC Blockset™ simulation message scalar | vector

The simulation-only message output port, when connected to an PWM
Interface (SoC Blockset) block, acts as pass-through with the output
emitted on the output of the PWM Interface block during
simulation.

**Note**

- The PWM Interface (SoC Blockset) does not use the frequency input
  of this block and must be set manually in the PWM
  Interface block mask.
- For STM32F7xx, STM32H7xx, and STM32G4xx based boards,
  channel 5 and channel 6 are not supported for simulation.
  However, code generation is supported for all
  channels.

#### Dependencies

To enable this port, select the **Enable simulation
port** parameter.

**Data Types:** `SoCData`

## Parameters

### Main

### **Timer module** — Select timer module `TIM1` (default) | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM9` | `TIM10` | `TIM11` | `TIM12` | `TIM13` | `TIM14`

Select the timer module. Number of timer module available will vary
for different processors.

**Note**

Ensure that `Timer module` is also configured
in the STM32CubeMX project.

### **Duty cycle unit** — Select duty cycle unit `Percentage` (default) | `Counts`

The block input controls the duty cycle of the square waveform for
each channel.

If **Duty Cycle unit** is
`Percentage`, an input value of 0 produces
a 0 percent duty cycle and an input of 100 produces a 100 percent duty
cycle output on the corresponding channel. If **Duty Cycle
unit** is `Counts`, the input
value is written to the Capture Compare register of the corresponding
channel.

### **Enable channel #** — Select channel `Enable channel 1` (default) | `Enable channel 2` | `Enable channel 3` | `Enable channel 4` | `Enable channel 5` | `Enable channel 6`

Enable the channels on which you want the block to generate the PWM
output. The input considers the duty cycle of the corresponding
channels.

Each **Timer module** can have one to six channels.
Number of channels available vary based on the timer module selected.
Enable the channel supported for the corresponding timer. By default,
the block enables **channel 1**.

**Note**

Ensure that the channels you want to enable are configured for
PWM generation in the STM32CubeMX project.

#### Dependencies

The number of channels available depends on the module you select
in the **Timer module** parameter.

### **Enable Capture/Compare # Enable (CC#E) input** — Enable capture/compare through input port `off` (default) | `on`

Enable this parameter to generate a capture/compare input through the
input port.

#### Dependencies

To enable this parameter, select the corresponding
**Enable channel#** parameter.

### **Enable Capture/Compare # Complementary Enable (CC#NE) input** — Enable capture/compare complementary through input port `off` (default) | `on`

Enable this parameter to generate a capture/compare complementary
input through the input port.

#### Dependencies

To enable this parameter, select the corresponding
**Enable channel#** parameter.

### **Enable Output Compare # Mode (OC#M) input** — Enable output compare mode through input port `off` (default) | `on`

Enable this parameter to generate a output compare mode input through
the input port.

#### Dependencies

To enable this parameter, select the corresponding
**Enable channel#** parameter.

### **Enable input to enable/disable timer** — Enable counter through input port `off` (default) | `on`

Enable or disable the counter through the input port. If you do not
select this parameter, then the counter is enabled during model
initialization.

### **Enable main output enable (MOE) input** — Enable main output through input port `off` (default) | `on`

Enable this parameter to set the main output enable (MOE) bit to
recover from a break.

#### Dependencies

To enable this parameter, set the **Timer
module** parameter to either `TIM1` or
`TIM8`.

### **Enable frequency input** — Enable frequency through input port `off` (default) | `on`

Enable this parameter to set the frequency of the timer. All the
channel outputs have the same frequency.

### **Set the repetition counter after counter is enabled** — Enable repetition counter through input `off` (default) | `on`

For odd values in the repetition counter, the update event occurs on
underflow or overflow depending on when you set the repetition
counter.

By default, the block sets repetition counter before you enable the
timer counter, so an update event occurs on underflow.

If you enable this parameter, the block sets repetition counter after
you enable the time counter, so an update events occur on
overflow.

#### Dependencies

To enable this parameter, set the **Timer
module** parameter to either `TIM1` or
`TIM8`.

### **Enable timer counter direction output** — Select output counter direction `off` (default) | `on`

Enable this parameter to output the current direction of the
counter.

### **Enable main output enable (MOE) status output** — Select main output enable `off` (default) | `on`

Enable this parameter to output the main output enable (MOE) bit
status.

#### Dependencies

To enable this parameter, set the **Timer
module** parameter to either `TIM1` or
`TIM8`.

### **Enable simulation port** — Enable simulation ports to block `off` (default) | `on`

Select this parameter to add an SoC Blockset compatible simulation output port.

### Events

### **Enable update generation event input** — Generate update event `off` (default) | `on`

Enable this parameter to generate an update event through input
port.

### **Enable capture compare # generation event input** — Generate capture compare event `off` (default) | `on`

Enable this parameter to generate a capture compare event through the
input port.

#### Dependencies

The number of **Enable capture compare # generation event
input** parameters available depends on the module you
select in the **Timer module**.

### **Enable trigger generation event input** — Generate trigger event `off` (default) | `on`

Enable this parameter to generate a trigger event through the input
port.

### **Enable break generation event input** — Generate break event `off` (default) | `on`

Enable this parameter to generate a break event through the input
port.

#### Dependencies

To enable this parameter, set the **Timer
module** parameter to either `TIM1`,
`TIM8`, `TIM15`,
`TIM16`, `TIM17` or
`TIM20`.

### **Enable break generation 2 event input** — Generate break 2 event `off` (default) | `on`

Enable this parameter to generate a break 2 event through the input
port.

#### Dependencies

To enable this parameter, set the **Timer
module** parameter to either `TIM1`,
`TIM8` or `TIM20`.

### **Sample time** — Frequency at which enabled output ports are read `-1` (default) | `non-negative real value`

Specify how often (in seconds) the status of enabled output ports are
read if no input ports are selected. Enter a value greater than zero.
When you specify this parameter as -1, Simulink determines the best
sample time for the block based on the block context within the
model.

#### Dependencies

To enable the **Sample time** parameter, deselect
all the input ports.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Generate square waveform on enabled channels using timer module

Use the PWM Output block to generate a square waveform on the enabled
channels using the timer module.

The block input controls the duty cycle of the square waveform for each
channel.

If you set **Duty Cycle unit** parameter to
`Percentage`, an input value of 0 produces a 0 percent duty
cycle and an input of 100 produces an output with 100 percent duty cycle on the
corresponding channel. If you set the **Duty Cycle unit** parameter to
`Counts`, the block writes input value to the capture
compare register of the corresponding channel.

If you select the **Enable frequency input**, the block writes the
corresponding input to the autoreload register of the timer to set the counter
period.

**Note**

You can run a Simulink® model containing PWM Output block in Connected IO mode
on STM32 Processor Based Boards. For more information, see Communicate with Hardware Using Connected IO.
