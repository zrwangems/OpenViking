---
type: simulink-block
title: 'Execution Profiler'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Utilities'
documentation_page: 'executionprofiler'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/executionprofiler.html'
language: en
---

# Execution Profiler

## Ports

### Output

### **f()** — Function call port scalar

Connect a function call subsystem to this port. When the subsystem executes,
it is profiled using the selected measurement technique.

### **cnt** — Count port scalar

Displays the execution time in number of cycles.

#### Dependencies

To enable this port, set the **Measurement
mode** parameter to either `Data Watchpoint Trace (DWT)
Timer` or `Timer`.

**Data Types:** `uint32`

## Parameters

### **Measurement mode** — Select execution profiling technique `Data Watchpoint Trace (DWT) Timer` (default) | `Digital Port Write (GPIO)` | `Timer`

Select the measurement techniques to profile function-call subsystem on the
target hardware.

- **Data Watchpoint Trace (DWT) Timer**:
  Measure and analyze the execution times of start-to-end downstream
  function-call subsystems.
- **Digital Port Write (GPIO)**: Utilize GPIO
  pins to set and clear signals before and after executing downstream
  function-call subsystems.
- **Timer**: Use timers to measure execution
  time by calculating the duration between pre-execution and post-execution
  timer counts. When you select **Timer** measurement,
  `Timer 2` is used for timer based profiling.

### **GPIO port name** — Specify GPIO port name `GPIOC` (default) | `GPIOA` | `GPIOB` | `…`

Specify the GPIO port name for the block.

#### Dependencies

To enable this parameter, set the **Measurement
mode** parameter to `Digital Port Write
(GPIO)`.

### **GPIO pin number** — Specify GPIO pin number `0` (default)

Specify the GPIO pin number for the block.

#### Dependencies

To enable this parameter, set the **Measurement
mode** parameter to `Digital Port Write
(GPIO)`.

### **Timer module** — Select timer module `TIM2` (default) | `TIM1` | `TIM3` | `...`

Select the timer module for the block.

#### Dependencies

To enable this parameter, set the **Measurement
mode** parameter to `Timer`.

### **Sample time** — Sample time at which block reads data from execution profiler `1` (default)

Sample time at which the **Execution Profiler** blocks
triggers downstream function-call subsystem.

Use this parameter to specify the time interval between 2 function-call
triggers. The count data is also updated at the mentioned sample time. To inherit
sample time, set this parameter to -1.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Profile execution time of functions using either DWT Timer, GPIO or Timer measurement modes

The **Execution Profile** block enables you to profile the execution
time of functions using either Data Watchpoint Trace (DWT) Timer, GPIO, or Timer
measurement modes.

- **DWT Timer:** Measure timing of tasks by recording the cycle
  count at the start and end of a function.
- **GPIO:** Set and clear GPIO pins before and after the execution
  of downstream function-call subsystems.
- **Timer:** Measure execution time of events by calculating the
  duration between pre-execution and post-execution timer counts.

These techniques enable you to accurately profile and optimize the performance of your
code running on STM32 processors.
