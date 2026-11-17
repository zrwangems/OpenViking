---
type: simulink-block
title: 'Clock Jitter Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'clockjittermeasurement'
documentation_source_path: 'ref/clockjittermeasurement.html'
language: en
---

# Clock Jitter Measurement

## Ports
```yaml
ports:
- name: clock
  summary: Input clock signal scalar
  direction: input
  data_types: double
- name: Period Jitter
  summary: Running RMS value of period jitter scalar
  direction: output
  data_types: double
- name: C2C
  summary: Running RMS value of cycle-to-cycle jitter scalar
  direction: output
  data_types: double
- name: DCD
  summary: Difference between real duty cycle and 50% value scalar
  direction: output
  data_types: double
```

### Input

### **clock** — Input clock signal scalar

Input clock signal, specified as a scalar. The input signal must have only one
threshold crossing per period.

**Data Types:** `double`
### Output

### **Period Jitter** — Running RMS value of period jitter scalar

Running RMS value of the period jitter calculated up to the current time step,
returned as a scalar. Period jitter is the deviation in the cycle time of a clock
signal with respect to the ideal period.

**Data Types:** `double`

### **C2C** — Running RMS value of cycle-to-cycle jitter scalar

Running RMS value of the cycle-to-cycle jitter calculated up to the current time
step, returned as a scalar. Cycle-to-cycle jitter is the difference in the period
between the two consecutive cycles of the clock.

#### Dependencies

To enable this port, select **Cycle-2-Cycle (C2C)
Jitter**.

**Data Types:** `double`

### **DCD** — Difference between real duty cycle and 50% value scalar

Difference between the real duty cycle in percentage and the ideal 50% value,
returned as a scalar.

#### Dependencies

To enable this port, select **Duty Cycle Distortion
(DCD)**.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Clock Frequency
  summary: Frequency of input clock signal 1e6 (default) | positive real scalar
  group: ''
  block_parameter: Frequency
  type: character vector
  values: positive real scalar
  default: 1e6
- name: Threshold
  summary: Threshold signal level 0 (default) | real scalar
  group: ''
  block_parameter: Threshold
  type: character vector
  values: real scalar
  default: '0'
- name: Period Jitter
  summary: RMS period jitter on (default) | off
  group: ''
- name: Cycle-2-Cycle (C2C) Jitter
  summary: RMS cycle-to-cycle jitter off (default) | on
  group: ''
- name: Duty Cycle Distortion (DCD)
  summary: Duty cycle distortion for each cycle off (default) | on
  group: ''
- name: Simulate using
  summary: Select simulation mode Code generation (default) | Interpreted execution
  group: ''
```

### **Clock Frequency** — Frequency of input clock signal `1e6` (default) | positive real scalar

Frequency of the input clock signal, specified as a positive real scalar in Hz.
**Clock Frequency** is used to calculate the ideal value of the
period of the input signal.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Frequency` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e6` |

### **Threshold** — Threshold signal level `0` (default) | real scalar

Threshold signal level to calculate the rising and falling edge of the signal,
specified as a real scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Threshold` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0` |

### **Period Jitter** — RMS period jitter on (default) | off

Select to calculate the RMS period jitter. This option is selected by
default.

Period jitter is the deviation in the cycle time of a clock signal with respect to
the ideal period.

### **Cycle-2-Cycle (C2C) Jitter** — RMS cycle-to-cycle jitter off (default) | on

Select to calculate the RMS cycle-to-cycle (C2C) jitter. This option is deselected
by default.

Cycle-to-cycle jitter is the difference in the period between the two consecutive
cycles of the clock.

### **Duty Cycle Distortion (DCD)** — Duty cycle distortion for each cycle off (default) | on

Select to calculate the duty cycle distortion for each cycle. This option is
deselected by default.

Duty cycle distortion is the difference between the real duty cycle in percentage
and the ideal 50% value.

### **Simulate using** — Select simulation mode `Code generation` (default) | `Interpreted execution`

Select the simulation mode. This choice affects the simulation performance.

Simulating the model using the `Code generation` method
requires additional startup time, but the subsequent simulations run faster. Simulating
the model using the `Interpreted execution` method may reduce
the startup time, but the subsequent simulations run slower. For more information, see
Interpreted Execution vs. Code Generation.
## Libraries

Mixed-Signal Blockset / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Measure jitter in periodic signals

Use the Clock Jitter Measurement block to measure the RMS (root mean
squared) periodic jitter in clock signals. You can also measure cycle-to-cycle (C2C) jitter
and duty cycle distortion (DCD).
