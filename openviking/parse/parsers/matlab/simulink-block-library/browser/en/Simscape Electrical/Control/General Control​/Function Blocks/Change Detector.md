---
type: simulink-block
title: 'Change Detector'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Function Blocks'
documentation_page: 'changedetector'
documentation_source_path: 'ref/changedetector.html'
language: en
---

# Change Detector

## Ports

### Input

### **u** — Boolean input `0` or `1`

Input Boolean signal. If false, `0`. If true,
`1`.

**Data Types:** `Boolean`
### Output

### **y** — Change report `0` or `1`

Output is true, `1`, when the block detects a change that corresponds
to the specified criteria (rising, falling, or either edge). Otherwise,
output is false, `0`.

**Data Types:** `Boolean`

## Parameters

### **Change detection** — Change criteria `Rising edge` (default) | `Falling edge` | `Either edge`

Criteria for change detection.

### **Initial condition** — Initial Boolean value `0` (default) | 1

Initial value of the previous input. If the input at the start of simulation is different
from the initial condition value, the block detects an edge.

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

Boolean signal change detector

The Change Detector block outputs a Boolean response of
`true` when it detects a change in the Boolean input signal that
meets one of these change criteria:

- Rising edge — The input goes from false to true.
- Falling edge — The input goes from true to false.
- Either edge — The input goes from true to false or from false to
  true.
