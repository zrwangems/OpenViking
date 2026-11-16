---
type: simulink-block
title: 'Monostable Flip-Flop'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'monostableflipflop'
documentation_source_path: 'ref/monostableflipflop.html'
language: en
---

# Monostable Flip-Flop

## Ports

### Input

### **Trigger** — Flip-flop trigger `0` | `1`

Input trigger signal to the flip-flop.

**Data Types:** `Boolean`
### Output

### **Q** — Flip-flop output `0` | `1`

Flip-flop output signal.

**Data Types:** `Boolean`

## Parameters

### **Change detection** — Change in trigger signal `Rising edge` (default) | `Falling edge` | `Either edge`

Change detection strategy for output pulse generation.

### **Initial output** — Flip-flop initial output `0` (default) | scalar

The initial output of the flip-flop.

### **Pulse duration (s)** — Output pulse duration `0.01` (default) | positive scalar

Duration of the output pulse, in s.

### **Sample time** — Block sample time `0.001` (default) | 0 | positive scalar

Time between consecutive block executions. During execution,
the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and
Specify Sample Time.

For discrete-time operation, set the sample time to a positive value. For continuous-time
operation, set the sample time to `0`.

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

Raising edge, falling edge, either edge monostable flip-flop

The Monostable Flip-Flop (or monostable multivibrator) block generates a
single output pulse of a specified duration when it is triggered externally. The
external trigger is a Boolean signal. Pulse generation is triggered when a change is
detected in the external trigger signal. The change detection can be:

- Rising edge
- Falling edge
- Either edge

When the output is true, a change in the external trigger signal has no
effect.

The operation of a monostable flip-flop is represented in the following figure:
