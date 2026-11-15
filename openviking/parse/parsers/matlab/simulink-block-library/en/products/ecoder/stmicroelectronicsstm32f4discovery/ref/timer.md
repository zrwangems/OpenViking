---
type: simulink-block
title: 'Timer'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Timer Peripherals'
documentation_page: 'timer'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/timer.html'
language: en
---

# Timer

## Ports

### Input

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

### **CEN** — Port to enable timer counter `scalar`

Use this port to enable or disable the timer counter. Set the port to
one of these values.

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

### **COMG** — Capture compare control update generation `scalar`

Use this port to generate capture compare control update generation
event. When you specify a value of `1`, the port
generates capture compare control update generation.

#### Dependencies

To enable this port, select the **Enable COM generation
event input** parameter.

**Data Types:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`
### Output

### **CNT** — Current timer counter value `scalar`

The counter port provides the current timer counter values as output
for the selected timer module.

**Data Types:** `uint32`

### **Dir** — Timer counter direction output `scalar`

The block outputs the current direction of the timer counter as one of
the following:

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

## Parameters

### Main

### **Timer module** — Select timer module `TIM1` (default) | `TIM2` | `TIM3` | `...`

Select the timer module. Number of timer module available will vary
for different processors.

**Note**

Ensure that `Timer module` is also configured
in the STM32CubeMX project.

### **Enable input to enable/disable timer** — Enable counter through input port `off` (default) | `on`

By default, the `Start timer during model
initialization` parameter is enabled in configuration
parameter. This starts the Timer Counter during model
initialization.

If you want to start the timer counter during run time, disable the
`Start timer during model initialization` parameter
in configuration parameter.

**Note**

If both `Enable input to enable/disable timer
parameter (block)` and `Start timer during
model initialization (Configuration Parameter)`
parameters are not enabled, the timer counter will not be
started.

### **Enable main output enable (MOE) input** — Enable main output through input port `off` (default) | `on`

Enable this parameter to set the main output enable (MOE) bit to
recover from a break.

#### Dependencies

To enable this parameter, set the **Timer
module** parameter to either `TIM1`,
`TIM8`, `TIM8`,
`TIM16`, `TIM17`, or
`TIM20`.

### **Enable frequency input** — Set the AutoReload register through input port `off` (default) | `on`

Enable this parameter to set the AutoReload register (ARR) value of
the timer during runtime.

### **Set the repetition counter after timer counter is enabled** — Enable repetition counter through input `off` (default) | `on`

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
module** parameter to either `TIM1`,
`TIM8`, `TIM8`,
`TIM16`, `TIM17`, or
`TIM20`.

### **Enable timer counter direction output** — Select to Enable timer counter direction output port `off` (default) | `on`

Enable this parameter to output the current direction of the timer
counter.

### **Enable main output enable (MOE) status output** — Select to enable MOE status port `off` (default) | `on`

Enable this parameter to output the main output enable (MOE) bit
status.

#### Dependencies

To enable this parameter, set the **Timer
module** parameter to either `TIM1`,
`TIM8`, `TIM8`,
`TIM16`, `TIM17`, or
`TIM20`.

### Events

### **Enable update generation event input** — Select to enable generate update event input port `off` (default) | `on`

Enable this parameter to generate an update event through input
port.

### **Enable capture compare # generation event input** — Select to enable capture compare generation event input `off` (default) | `on`

Enable this parameter to generate a capture compare event through the
input port.

#### Dependencies

The number of **Enable capture compare # generation event
input** parameters available depends on the module you
select in the **Timer module**.

### **Enable trigger generation event input** — Select to enable trigger generation event input `off` (default) | `on`

Enable this parameter to generate a trigger event through the input
port.

### **Enable break generation event input** — Select to enable break generation event input `off` (default) | `on`

Enable this parameter to generate a break event through the input
port.

#### Dependencies

To enable this parameter, set the **Timer
module** parameter to any one of the module
`TIM1`, `TIM8`,
`TIM8`, `TIM16`,
`TIM17`, or `TIM20`.

### **Enable break generation 2 event input** — Select to enable break generation 2 event input `off` (default) | `on`

Enable this parameter to generate a break 2 event through the input
port.

#### Dependencies

To enable this parameter, set the **Timer
module** parameter to any one of the module
`TIM1`, `TIM8`,
`TIM8`, `TIM16`,
`TIM17`, or `TIM20`.

### **Enable COM generation event input** — Select to enable capture compare generation event input `off` (default) | `on`

Enable this parameter to generate a capture compare event through the
input port.

#### Dependencies

To enable this parameter, set the **Timer
module** parameter to any one of the module
`TIM1`, `TIM8`,
`TIM8`, `TIM16`,
`TIM17`, or `TIM20`.

### **Sample time** — Frequency at which enabled output ports are read `-1` (default) | `non-negative real value`

Specify how often (in seconds) the status of enabled output ports are
read if no input ports are selected. Enter a value greater than zero.
When you specify this parameter as -1, Simulink® determines the best sample time for the block based on the
block context within the model.

#### Dependencies

To enable the **Sample time** parameter, deselect
all the input ports.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Starts timer counter and provides current counter value

Starts timer counter and provides the current counter value as output for the selected
timer module. Also enables the interrupts selected in configuration parameters.

Counter is started during model initialization only when `Start Timer during
model initialization` parameter is selected in the configuration
parameters.

To start/stop the counter in runtime, deselect the `Start Timer during model
initialization` parameter in the configuration parameters and select
`Enable input to enable/disable timer` option in the block. An
input of `1` to the corresponding input port will start the counter and
`0` will stop the counter.
