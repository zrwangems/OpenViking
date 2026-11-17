---
type: simulink-block
title: 'Variable Pulse Delay'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'variablepulsedelay'
documentation_source_path: 'ref/variablepulsedelay.html'
language: en
---

# Variable Pulse Delay

## Ports
```yaml
ports:
- name: in
  summary: Input sample data fixed step discrete sample | variable step discrete sample
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | floating point
- name: delay
  summary: Introduces delay to input signal nonnegative scalar
  direction: input
  data_types: floating point
- name: out
  summary: Delayed output sample fixed step discrete sample | variable step discrete sample
  direction: output
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | floating point
```

### Input

### **in** — Input sample data fixed step discrete sample | variable step discrete sample

Input sample data, whose type and width are inherited from the signal source. The
input port supports data bus operation, but does not support framed inputs.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `floating point`

### **delay** — Introduces delay to input signal nonnegative scalar

Introduces delay to the input signal, specified as a nonnegative scalar. The value
at the **delay** port at the time of the arrival of input signal
determines the amount of delay introduced.

**Data Types:** `floating point`
### Output

### **out** — Delayed output sample fixed step discrete sample | variable step discrete sample

Delayed output sample data, whose type and width are the same as the input signal.
The value at the **delay** port at the time of the arrival of input
signal determines the amount of delay introduced at the **out** port.
The input and output signals must maintain the same order.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `floating point`
## Parameters
```yaml
parameters:
- name: Initial Input
  summary: The value at the output port before simulation 0 (default) | scalar
  group: ''
- name: Buffer Size
  summary: Number of samples of the input buffering available during simulation 1 (default) | positive scalar integer
  group: ''
```

### **Initial Input** — The value at the output port before simulation `0` (default) | scalar

The value at the output port before simulation, specified as a scalar.

At the beginning of the simulation, the value at the **out** port
is equal to the value set by the **Initial Input** parameter. If the
value at the **in** port is not equal to the value of the
**Initial Input** parameter, then the output will transition to the
value at the **in** port after a delay equal to the value at the
**delay** port.

#### Programmatic Use

- Use `get_param(gcb,'InitialOutput')` to view the current
  value of **Initial Input**.
- Use `set_param(gcb,'InitialOutput',value)` to set
  **Initial Input** to a specific value.

### **Buffer Size** — Number of samples of the input buffering available during simulation `1` (default) | positive scalar integer

Number of samples of the input buffering available during simulation, specified as a
positive scalar integer.

#### Programmatic Use

- Use `get_param(gcb,'BufferSize')` to view the current value
  of **Buffer Size**.
- Use `set_param(gcb,'BufferSize',value)` to set
  **Buffer Size** to a specific value.
## Libraries

Mixed-Signal Blockset / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Delay samples by controlled, continuously variable amount

Variable Pulse Delay block introduces a controllable delay in signal
samples. Each sample at the **in** port is delayed by the value at the
**delay** port at the time the input sample arrived. The delayed samples at
the **out** port must maintain the same order as at the
**in** port.

At the beginning of the simulation, the **out** port is set to the value
of the **Initial Input** parameter.
