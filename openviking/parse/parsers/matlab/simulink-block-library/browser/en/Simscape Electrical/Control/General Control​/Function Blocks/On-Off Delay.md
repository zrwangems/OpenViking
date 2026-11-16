---
type: simulink-block
title: 'On-Off Delay'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Function Blocks'
documentation_page: 'onoffdelay'
documentation_source_path: 'ref/onoffdelay.html'
language: en
---

# On-Off Delay

## Ports

### Input

### **u** — Input signal `0` | `1`

Input Boolean signal.

**Data Types:** `Boolean`
### Output

### **y** — Output signal `0` | `1`

Output signal with delays.

**Data Types:** `Boolean`

## Parameters

### **ON delay time (s)** — Input ON delay time `0.01` (default) | `0` | positive scalar

Specify delay time when input is ON.

### **OFF delay time (s)** — Input OFF delay time `0` (default) | positive scalar

Specify delay time when input is OFF.

### **Initial state** — Signal initial state `0` (default) | `1`

Specify initial state.

### **Sample time** — Block sample time `0.001` (default) | 0 | positive scalar

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For discrete-time operation, set the sample time to a positive value. For
continuous-time operation, set the sample time to
`0`.

If this block is in a masked subsystem, or other variant subsystem that
allows either continuous and discrete operation, promote the sample time
parameter. Promoting the sample time parameter ensures correct switching
between the continuous and discrete implementations of the block. For more
information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Boolean-signal delay

The On-Off Delay block applies a delay on the Boolean input signal.

A time delay is added when a transition is detected in the input signal. This block
allows you to add a time delay to the input signal when:

- An ON transition (input change from 0 to 1) is detected,
- An OFF transition (input signal change from 1 to 0) is detected, or
- Either transition is detected.

The operation of the on-off delay is represented in the following figure:
