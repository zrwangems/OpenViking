---
type: simulink-block
title: 'Signal Sample and Hold'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'signalsampleandhold'
documentation_source_path: 'ref/signalsampleandhold.html'
language: en
---

# Signal Sample and Hold

## Ports
```yaml
ports:
- name: u
  summary: Input signal scalar | vector
  direction: input
  data_types: single | double
- name: S
  summary: Control signal 0 | 1
  direction: input
  data_types: Boolean
- name: y
  summary: Output signal scalar | vector
  direction: output
  data_types: single | double
```

### Input

### **u** — Input signal scalar | vector

Input signal.

**Data Types:** `single` | `double`

### **S** — Control signal `0` | `1`

Sample pulse of `0` for `false` or
`1` for `true`.

**Data Types:** `Boolean`
### Output

### **y** — Output signal scalar | vector

Output signal.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Initial condition
  summary: Initial output value scalar | vector
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | 0 | positive scalar
  group: ''
```

### **Initial condition** — Initial output value scalar | vector

Specify initial condition. The value must be a scalar or a vector of the
same size as the input signal.

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

Discrete-time or Continuous-time sample and hold input signal

The Signal Sample and Hold block implements a signal sample and hold in
either discrete or continuous time.

When input *S* is `true`, output
*y* is equal to input *u*. When input
*S* is `false`, the block holds the output until
*S* becomes `true` again.
