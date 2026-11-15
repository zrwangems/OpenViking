---
type: simulink-block
title: 'Moving Average'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Function Blocks'
documentation_page: 'movingaverage'
documentation_source_path: 'ref/movingaverage.html'
language: en
---

# Moving Average

## Ports

### Input

### **u** — Moving average input scalar | vector

Input signal.

**Data Types:** `single` | `double`
### Output

### **Mean** — Moving average output scalar | vector

Moving average of the input signal.

**Data Types:** `single` | `double`

## Parameters

### **Fundamental frequency (Hz)** — Signal fundamental frequency `60` (default) | positive scalar | vector with positive values

Fundamental frequency of the signal, in Hz. If you specify the fundamental frequency
using a vector, it must match the input vector dimension.

### **Initial value** — Initial input signal value `0` (default) | scalar

Initial value of the input signal.

### **Buffer size** — Size of buffer `8192` (default) | scalar

Size of the buffer.

#### Dependencies

To enable this parameter, set **Sample time (-1 for
inherited)** to `0`.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `0` | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set this parameter to `-1`.
For discrete-time operation, set this parameter to a positive integer. For
continuous-time operation, set this parameter to `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote this parameter to ensure
correct switching between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Moving average-value computation

The Moving Average block computes the moving average value of the input
signal. Use this block to filter higher frequency signal components and to smooth noisy
signals.

### Equations

The block computes the moving average based on a moving time window. The moving average for
continuous-time is equal to

u¯=1T0∫t0t0+T0u(t)dt,

where:

- *u(t)* is the input signal.
- *T0* is equal to 1f.
- *f* is the fundamental frequency of the
  signal.
- *t0* is the initial time for
  integration in a time window.

The moving average for discrete-time is equal to:

u¯(k)=1T0∑i=0n−1u(k−i).

**Note**

If you use this block for continuous-time operations and set the
**Sample time (-1 for inherited)** parameter to
`0`, you should also specify the value of the
**Buffer size** parameter to ensure it covers the
moving time window.

### Assumptions

The block initializes the output with the initial condition in the time interval
`[0, T0]`.
