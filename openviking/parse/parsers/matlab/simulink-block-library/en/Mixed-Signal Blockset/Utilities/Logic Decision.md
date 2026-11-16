---
type: simulink-block
title: 'Logic Decision'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'logicdecision'
documentation_source_path: 'ref/logicdecision.html'
language: en
---

# Logic Decision

## Ports

### Input

### **wave** — Input signal fixed step sampling | variable step sampling | scalar

Input signal, specified as a floating point scalar. The input signal can either be
inherited, or defined by the Logic Decision block as a fixed step
discrete sample time.

**Data Types:** `double` | `Boolean`

### **vth** — Decision threshold value scalar

Decision threshold value, specified as a scalar. The value at
**vth** port determines when the input signal is delayed by a fixed
amount.

**Data Types:** `floating point`
### Output

### **events** — Output signal `0` | `1`

Output signal, returned as either `0` or
`1`.

**Data Types:** `double` | `Boolean`

## Parameters

### **Sample time** — Source of sample time `Inherited` (default) | `Fixed`

Source of sample time.

- Select `Inherited` to inherit sample time from previous
  block.
- Select `Fixed` to set discrete sample time to a fixed
  value.

#### Programmatic Use

- Use `get_param(gcb,'SampleTimeSource')` to view the
  current source of **Sample time**.
- Use `set_param(gcb,'SampleTimeSource',value)` to set
  **Sample time** to a specific value.

### **Sample time value** — Actual value of sample time `20e-12` (default) | real scalar excluding zero

Actual value of sample time, specified as a real scalar excluding zero.

#### Dependencies

To enable this parameter, select `Fixed` in **Sample
time** parameter.

#### Programmatic Use

- Use `get_param(gcb,'SampleTimeIn')` to view the current
  **Sample time value**.
- Use `set_param(gcb,'SampleTimeIn',value)` to set
  **Sample time value** to a specific value.

### **Minimum delay value** — Minimum propagation delay value `1e-15` (default) | positive scalar

The minimum propagation delay for the block, specified as a positive scalar. For a
fixed discrete input sample time, the actual delay is the maximum of this parameter
value and the fixed step size.

#### Programmatic Use

- Use `get_param(gcb,'Delay')` to view the current
  **Minimum delay value**.
- Use `set_param(gcb,'Delay',value)` to set **Minimum
  delay value** to a specific value.

### **Buffer size** — Number of threshold crossings to buffer `1` (default) | positive integer scalar

The number of pending output events that can be stored in the block, specified as a
positive integer scalar.

#### Programmatic Use

- Use `get_param(gcb,'BufferSizeIn')` to view the current
  **Buffer size**.
- Use `set_param(gcb,'BufferSizeIn',value)` to set
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

Threshold crossing detector at input to binary process

Logic Decision block produces an output event at a fixed delay from almost
exactly the time the input signal crosses a decision threshold. This block helps transitioning
from a uniformly sampled input waveform to an event driven digital logic subsystem.
