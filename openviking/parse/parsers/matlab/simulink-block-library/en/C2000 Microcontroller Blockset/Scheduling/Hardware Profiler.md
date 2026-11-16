---
type: simulink-block
title: 'Hardware Profiler'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Scheduling'
documentation_page: 'hardwareprofiler'
documentation_source_path: 'ref/hardwareprofiler.html'
language: en
---

# Hardware Profiler

## Ports

### Output

### **f()** — Function call port scalar

Connect a function call subsystem to this port. When the subsystem executes,
it is profiled using the selected measurement technique.

### **cnt** — Count port scalar

Displays the execution time in number of cycles.

#### Dependencies

To enable this port, set the **Measurement
mode** parameter to either `Embedded Real-time Analysis
& Diagnostic (ERAD)` or `Timer`.

**Data Types:** `uint32`

## Parameters

### **Measurement mode** — Select hardware profiling technique `Embedded Real-time Analysis & Diagnostic (ERAD)` (default) | `General Purpose Input Output (GPIO)` | `Timer`

Select the measurement techniques to profile function-call subsystem on the
target hardware.

- **ERAD**: Measure and analyze the
  execution times of start-to-end downstream function-call
  subsystems.
- **GPIO**: Utilize GPIO pins to set and
  clear signals before and after executing downstream function-call
  subsystems.
- **Timer Measurement**: Use timers to
  measure execution time by calculating the duration between pre-execution
  and post-execution timer counts. When you select Time Measurement, Timer
  2 is used for timr based profiling.

### **ERAD module** — Specify ERAD module `1` (default) | `2` | `3` | `4`

Specify the ERAD module. The ERAD module consists of ERAD counter and 2 ERAD
breakpoints. When you select the ERAD module, the blocks puts breakpoints at
function beginning and end and measures clock cycles for execution between two
breakpoints.

- `Module 1` - ERAD counter 1 and ERAD breakpoint 1 and
  2.
- `Module 2` - ERAD counter 2 and ERAD breakpoint 3 and
  4.
- `Module 3` - ERAD counter 3 and ERAD breakpoint 5 and
  6.
- `Module 4` - ERAD counter 4 and ERAD breakpoint 7 and
  8.

**Note**

The ERAD module is only available in selected TI processors.

#### Dependencies

To enable this parameter, set the **Measurement
mode** parameter to `Embedded Real-time Analysis &
Diagnostic (ERAD)`.

### **GPIO number** — Specify GPIO number `0` (default)

Specify the GPIO number for the block.

#### Dependencies

To enable this parameter, set the **Measurement
mode** parameter to `General Purpose Input Output
(GPIO)`.

### **Sample time** — Sample time at which block reads data from hardware profiler `-1` (default)

Sample time at which the Hardware Profiler blocks triggers downstream
function-call subsystem.

Use this parameter to specify the time interval between 2 function-call
triggers. The count data is also updated at the mentioned sample time. To inherit
sample time, set this parameter to -1.

## Libraries

C2000 Microcontroller Blockset / Scheduling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Profiles function-call subsystem using GPIO, ERAD, or Timer measurement modes

The Hardware Profiler Block enables you to profile function-call subsystem on target
hardware using General Purpose Input Output (GPIO), Embedded Real-time Analysis &
Diagnostic (ERAD), and Timer Measurement modes.

- **ERAD:** Measure and analyze the execution times of
  start-to-end downstream function-call subsystems.
- **GPIO:** Set and clear GPIO pins before and after the
  execution of downstream function-call subsystems.
- **Timer:** Measure execution time of events by calculating the
  duration between pre-execution and post-execution timer counts.

These techniques enable you to accurately profile and optimize the performance of your
code running on TI C2000 processors.

**Hardware Profiler** block with Timer and ERAD mode
provide output in clock cycles. To convert it into seconds, use the following
formula:

**Note**

The Hardware Profiler block in ERAD measurement mode consistently provides the
maximum execution time.
