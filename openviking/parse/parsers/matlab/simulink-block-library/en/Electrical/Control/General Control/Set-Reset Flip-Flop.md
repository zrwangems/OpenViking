---
type: simulink-block
title: 'Set-Reset Flip-Flop'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'setresetflipflop'
documentation_source_path: 'ref/setresetflipflop.html'
language: en
---

# Set-Reset Flip-Flop

## Ports
```yaml
ports:
- name: Set
  summary: Set input signal 0 | 1
  direction: input
  data_types: Boolean
- name: Reset
  summary: Reset input signal 0 | 1
  direction: input
  data_types: Boolean
- name: Q
  summary: Output signal 0 | 1
  direction: output
  data_types: Boolean
- name: '!Q'
  summary: Complement output signal 0 | 1
  direction: output
  data_types: Boolean
```

### Input

### **Set** — Set input signal `0` | `1`

Input signal that triggers a state change.

**Data Types:** `Boolean`

### **Reset** — Reset input signal `0` | `1`

Input signal that resets a state change.

**Data Types:** `Boolean`
### Output

### **Q** — Output signal `0` | `1`

Output signal **Q**, with the same
dimensions and data type as the input **signal**.

**Data Types:** `Boolean`

### **!Q** — Complement output signal `0` | `1`

Output signal **!Q**, with the same
dimensions and data type as the input **signal**.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Priority when undefined state
  summary: State priority Set (default) | Reset
  group: ''
- name: Initial condition for Q state
  summary: Initial value of the output Q 0 (default) | 1
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | 0 | positive scalar
  group: ''
```

### **Priority when undefined state** — State priority `Set` (default) | `Reset`

Priority for the undefined state, that is, when both
*Set* and *Reset* are
`true`.

### **Initial condition for Q state** — Initial value of the output Q `0` (default) | `1`

Initial condition for *Q* state.

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

Set-reset flip-flop or bistable multivibrator

The Set-Reset Flip-Flop block implements a set-reset flip-flop or bistable
multivibrator.

The block maintains the output signals, Q and !Q, unless an external trigger is
applied. An external trigger (*Set*) produces a change of state, which
is maintained until a second external trigger (*Reset*) is
applied.

The table shows the relationship between the block input and output signals.

| Set | Reset | Q | !Q |
| --- | --- | --- | --- |
| 0 | 0 | Last Q | Last !Q |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | Undefined | Undefined |

When the state is undefined, the priority is provided as an external parameter.
