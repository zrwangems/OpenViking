---
type: simulink-block
title: 'Counter'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Function Blocks'
documentation_page: 'counter'
documentation_source_path: 'ref/counter.html'
language: en
---

# Counter

## Ports

### Output

### **T** — Counter value scalar

Counter value.

**Data Types:** `single` | `double`

## Parameters

### **Counter type** — Counter strategy `Up` (default) | `Down` | `Up-Down`

Counter type.

### **Output range** — Range `[0 1]` (default) | `[-1 1]`

Range for the output.

### **Timer period (s)** — Period `0.001` (default) | positive scalar

Timer period, in s.

### **Phase delay (s)** — Delay `0` (default) | `0` or positive scalar

Phase delay, in s. Add a phase delay to change the initial state of the
counter.

### **Sample time** — Block sample time `0.0001` (default) | `0` or positive scalar

Time between consecutive block executions. During execution,
the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and
Specify Sample Time.

For discrete-time simulation, set the sample time to a positive scalar.
For continuous-time simulation, set the sample time to
`0`.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Discrete- or continuous-time counter

The Counter block implements an incremental counter in either discrete or
continuous time. The counter increments in response to one of these criteria:

- Up — The input goes up.
- Down — The input goes down.
- Up-Down — The input goes up or down.
