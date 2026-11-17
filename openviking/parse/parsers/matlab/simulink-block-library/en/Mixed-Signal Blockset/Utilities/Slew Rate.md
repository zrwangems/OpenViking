---
type: simulink-block
title: 'Slew Rate'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'slewrate'
documentation_source_path: 'ref/slewrate.html'
language: en
---

# Slew Rate

## Ports
```yaml
ports:
- name: events
  summary: Input signal scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
- name: wave
  summary: Output signal scalar
  direction: output
  data_types: double
```

### Input

### **events** — Input signal scalar

Variable step, event driven input signal, specified as a scalar. The signal at
**events** port comes from the output of a logic gate such as
Variable Pulse
Delay block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### Output

### **wave** — Output signal scalar

Fixed step, uniformly sampled output signal, returned as a scalar. You can define
the finite slew rate and propagation delay for the signal at the
**wave** port.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Output step size calculation
  summary: Defines how to calculate output step size Default (default) | Advanced
  group: ''
- name: Maximum frequency of interest (Hz)
  summary: Maximum frequency of interest at output 11e9 (default) | scalar
  group: ''
- name: Output sample interval
  summary: Output sample interval 23ps (default) | scalar
  group: ''
- name: Minimum 20%-80% rise/fall time
  summary: Minimum rise/fall time required at the output for meaningful simulation 23ps (default) | scalar
  group: ''
- name: Rise/fall time (s)
  summary: 20%-80% rise time at the output 30e-12 (default) | scalar
  group: ''
- name: Slew rate for 20%-80% edge of unit amplitude signal
  summary: Slew rate for the 20%-80% edge at the output 56GHz (default) | scalar
  group: ''
- name: Minimum propagation delay
  summary: Minimum propagation delay for meaningful simulation 48ps (default) | scalar
  group: ''
- name: Propagation delay (s)
  summary: Propagation delay of a rising edge 48e-12 (default) | scalar
  group: ''
- name: Enable increased buffer size
  summary: Enable increased buffer size button
  group: ''
- name: Buffer size
  summary: Buffer size of the blocks 10 (default) | positive integer scaler
  group: ''
```

### **Output step size calculation** — Defines how to calculate output step size `Default` (default) | `Advanced`

Defines how to calculate output step size.

- Choose `Default` to calculate **Output step size
  calculation** based on rise/fall time. The **Output sample
  interval** (ΔT) is given by ΔT=(Rise/fall time)26 · 0.22.
- Choose `Advanced` to calculate **Output step size
  calculation** based on frequency of interest. The **Output
  sample interval** (ΔT) is given by ΔT=Rise/fall time6 · Maximum frequency of interest.

#### Programmatic Use

- Use `get_param(gcb,'DefaultOrAdvanced')` to determine how
  the output step size is being calculated.

### **Maximum frequency of interest (Hz)** — Maximum frequency of interest at output `11e9` (default) | scalar

Maximum frequency of interest at output, specified as a scalar in Hz.
**Maximum frequency of interest** is used to calculate
**Output sample interval** and **Minimum 20%-80% rise/fall
time**.

#### Dependencies

This parameter is only available when `Advanced` is selected for
**Output step size calculation**.

#### Programmatic Use

- Use `get_param(gcb,'MaxFreqInterest')` to view the
  current value of **Maximum frequency of interest**.
- Use `set_param(gcb,'MaxFreqInterest',value)` to set
  **Maximum frequency of interest** to a specific value.

### **Output sample interval** — Output sample interval `23ps` (default) | scalar

Output sample interval, specified as a scalar in s. This parameter is
nontunable.

The **Output sample interval** (ΔT) is given by ΔT=Rise/fall time6 · Maximum frequency of interest.

#### Dependencies

This parameter is only available when `Advanced` is selected for
**Output step size calculation**.

#### Programmatic Use

- Use `get_param(gcb,'OutputSampleTime')` to view the
  current value of **Output sample interval**.
- Use `set_param(gcb,'OutputSampleTime',value)` to set
  **Output sample interval** to a specific value.

### **Minimum 20%-80% rise/fall time** — Minimum rise/fall time required at the output for meaningful simulation 23ps (default) | scalar

Minimum rise/fall time required at the output for meaningful simulation, specified
as a scalar in ps. This is a nontunable parameter.

#### Dependencies

This parameter is only available when `Advanced` is selected for
**Output step size calculation**.

#### Programmatic Use

- Use `get_param(gcb,'ConversionRiseFall')` to view the
  current value of **Minimum 20%-80% rise/fall time**.
- Use `set_param(gcb,'ConversionRiseFall',value)` to set
  **Minimum 20%-80% rise/fall time** to a specific
  value.

### **Rise/fall time (s)** — 20%-80% rise time at the output `30e-12` (default) | scalar

Time required for signal to change from 20% to 80% in a full amplitude edge at the
output, specified as a scalar.

#### Programmatic Use

- Use `get_param(gcb,'RiseTime')` to view the current value
  of **Rise/fall time**.
- Use `set_param(gcb,'RiseTime',value)` to set
  **Rise/fall time** to a specific value.

### **Slew rate for 20%-80% edge of unit amplitude signal** — Slew rate for the 20%-80% edge at the output `56GHz` (default) | scalar

Slew rate for the 20%-80% edge at the output, specified as a scalar. This parameter
is nontunable.

#### Programmatic Use

- Use `get_param(gcb,'RisingSlewRate')` to view the current
  value of **Slew rate for 20%-80% edge of unit amplitude
  signal**.
- Use `set_param(gcb,'RisingSlewRate',value)` to set
  **Slew rate for 20%-80% edge of unit amplitude signal** to a
  specific value.

### **Minimum propagation delay** — Minimum propagation delay for meaningful simulation `48ps` (default) | scalar

Minimum propagation delay for meaningful simulation, specified as a scalar. This
parameter is nontunable.

Minimum propagation delay is calculated from **Maximum frequency of
interest** where Minimum propagation delay =0.269Maximum frequency of interest.

#### Programmatic Use

- Use `get_param(gcb,'ConversionDelay')` to view the
  current value of **Minimum propagation delay**.
- Use `set_param(gcb,'ConversionDelay',value)` to set
  **Minimum propagation delay** to a specific value.

### **Propagation delay (s)** — Propagation delay of a rising edge `48e-12` (default) | scalar

Propagation delay of a rising edge, specified as a scalar in s.
**Propagation delay** is measured at a threshold equal to the half of
the amplitude.

#### Programmatic Use

- Use `get_param(gcb,'RisepropDelay')` to view the current
  value of **Propagation delay**.
- Use `set_param(gcb,'RisePropDelay',value)` to set
  **Propagation delay** to a specific value.

### **Enable increased buffer size** — Enable increased buffer size button

Select to enable increased buffer size during the simulation. This increases the
buffer size of all the blocks in the PLL model that belong to the Mixed-Signal Blockset™/Utilities Simulink® library. By default, this option is deselected.

### **Buffer size** — Buffer size of the blocks `10` (default) | positive integer scaler

Buffer size of all the blocks in the PLL model that belong to the Mixed-Signal Blockset/Utilities Simulink library.

Selecting different simulation solver or sampling strategies can change the number
of input samples needed to produce an accurate output sample. Set the **Buffer
size** to a large enough value so that the input buffer contains all the
input samples required.

#### Dependencies

This parameter is only available when the **Enable increased buffer
size** option is selected.

#### Programmatic Use

- Use `get_param(gcb,'NBuffer')` to view the current value of
  **Buffer size**.
- Use `set_param(gcb,'NBuffer',value)` to set
  **Buffer size** to a specific value.
## Libraries

Mixed-Signal Blockset / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Model amplitude, rise and fall times, and propagation delay of logic gates

The Slew Rate block converts a logical signal to a signal with user-defined
finite slew rate and propagation delay.
