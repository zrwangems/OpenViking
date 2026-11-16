---
type: simulink-block
title: 'Serial-In Parallel-Out Shift Register'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'serialinparalleloutshiftregister'
documentation_source_path: 'ref/serialinparalleloutshiftregister.html'
language: en
---

# Serial-In Parallel-Out Shift Register

## Ports

### Input

### **u** — Serial input scalar | vector

Serial input signal.

**Data Types:** `single` | `double`
### Output

### **y** — Parallel output vector

Parallel output signal.

**Data Types:** `single` | `double`

## Parameters

### **Number of samples** — Number of input samples `4` (default) | positive integer

Number of register stages or samples.

### **Initial condition** — Initial value of the input sample `0` (default) | real number

Initial value of the *N-1* samples preceding simulation start time. The
value must be a scalar or a vector of the same size as the input
signal.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | 0 | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time, specify `-1`. For discrete-time, specify
a positive integer. For continuous-time, specify `0`.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Discrete-time serial-in, parallel-out shift register

The Serial-In Parallel-Out Shift Register block implements a serial-in
parallel-out shift register in discrete time. You can use a shift register to convert
between serial and parallel interfaces or to implement a circuit delay or hardware
stack.

This block outputs a vector of last *N* samples of the input signal.
If the input signal is a vector, the block outputs the last *N* samples
of each input signal.
