---
type: simulink-block
title: 'Fault'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'fault'
documentation_source_path: 'ref/fault.html'
language: en
---

# Fault

## Ports

### Input

### **F** — External fault trigger signal physical

Physical signal input port associated with the external fault trigger
signal.
### Output

### **X** — Fault state physical

Physical signal output port associated with the fault state. It
outputs `1` if the block is faulted,
`0` otherwise.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the fault positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the fault negative
terminal.

## Parameters

### Main

### **Unfaulted resistance** — Resistance with no fault `inf` `Ohm` (default)

Resistance between the **+** and
**–** ports when there is no fault.

### **Faulted resistance** — Resistance with fault `1e-3` `Ohm` (default)

Resistance between the **+** and
**–** ports when the block is in the faulted
state.

### **Reporting when a fault occurs** — Fault occurrence report `None` (default) | `Warn` | `Error`

Choose whether to issue an assertion when a fault occurs:

- `None` — The block does not
  issue an assertion.
- `Warn` — The block issues a
  warning.
- `Error` — Simulation stops
  with an error.

### Temporal Trigger

### **Enable temporal fault trigger** — Temporal fault trigger option `No` (default) | `Yes`

Select `Yes` to enable time-based fault
triggering.

### **Simulation time for fault event** — Simulation time for fault event `1` `s` (default)

Set the simulation time that the block enters the fault state.

#### Dependencies

This parameter is visible only when you set the **Enable
temporal fault trigger** parameter to
`Yes`.

### **Fault duration** — Duration time for the fault `inf` `s` (default)

Set the simulation duration time for the fault. The block exits the
fault state when the duration time is over.

#### Dependencies

This parameter is visible only when you set the **Enable
temporal fault trigger** parameter to
`Yes`.

### Behavioral Trigger

### **Enable behavioral fault trigger** — Behavioral fault trigger option `No` (default) | `Yes`

Select `Yes` to enable behavioral fault
triggering.

### **Permissible voltage range** — Permissible voltage range `[-100, 100]` `V` (default)

Specify a vector of length 2 that defines the permissible voltage
range. If the voltage is outside this range for longer than the
**Time to fail when exceeding voltage range**
parameter value, then the block enters the fault state.

#### Dependencies

This parameter is visible only when you set the **Enable
behavioral fault trigger** parameter to
`Yes`.

### **Time to fail when exceeding voltage range** — Time to fail when exceeding voltage range `1` `s` (default)

Set the maximum length of time that the voltage can be outside the
permissible voltage range without triggering the fault.

#### Dependencies

This parameter is visible only when you set the **Enable
behavioral fault trigger** parameter to
`Yes`.

### **Permissible current range** — Permissible current range `[-1, 1]` `A` (default)

Specify a vector of length 2 that defines the permissible current
range. If the current is outside this range for longer than the
**Time to fail when exceeding current range**
parameter value, then the block enters the fault state.

#### Dependencies

This parameter is visible only when you set the **Enable
behavioral fault trigger** parameter to
`Yes`.

### **Time to fail when exceeding current range** — Time to fail when exceeding current range `1` `s` (default)

Set the maximum length of time that the current can be outside the
permissible current range without triggering the fault.

#### Dependencies

This parameter is visible only when you set the **Enable
behavioral fault trigger** parameter to
`Yes`.

### External Trigger

### **Enable external fault trigger** — External fault trigger option `No` (default) | `Yes`

Select `Yes` to enable external fault
triggering. The physical signal input F provides the external fault
trigger signal.

### **External fault trigger** — External fault trigger condition `Faulted if F >= Fault threshold` (default) | `Faulted if F <= Fault threshold`

Choose the fault condition:

- `Faulted if F >= Fault threshold`
  — The fault occurs when the external signal value becomes
  greater than, or equal to, the **Fault
  threshold** parameter value.
- `Faulted if F <= Fault threshold`
  — The fault occurs when the external signal value becomes
  less than, or equal to, the **Fault threshold**
  parameter value.

#### Dependencies

This parameter is visible only when you set the **Enable
external fault trigger** parameter to
`Yes`.

### **Fault threshold** — Fault threshold `0.5` (default)

The threshold value that triggers the fault when the external signal
crosses it in the direction, specified by the fault condition.

#### Dependencies

This parameter is visible only when you set the **Enable
external fault trigger** parameter to
`Yes`.

### **Fault resets when fault trigger reverts** — Fault resets when fault trigger reverts `No` (default) | `Yes`

Select `Yes` to have the fault reset when the trigger
signal reverts.

#### Dependencies

This parameter is visible only when you set the **Enable
external fault trigger** parameter to
`Yes`.

## Libraries

Simscape / Electrical / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Electrical fault with temporal, behavioral, or external trigger

The Fault block allows you to represent an electrical
fault as an instantaneous change in resistance. You can use it to replicate both
open-circuit and short-circuit fault behaviors. The block can trigger fault
events:

- At a specific time. The block can also stop imposing a temporal fault after a
  specified time duration.
- When a predefined voltage range or current range is exceeded
- When an external trigger signal goes high or low

Optionally, the external trigger option also permits the fault to reset when the
trigger signal reverts. You can enable or disable all three trigger mechanisms
separately. If more than one trigger mechanism is required in a simulation, you can use
them together.

When no fault is triggered, the resistance between the two electrical ports is defined
by the **Unfaulted resistance** parameter value. The default value for
this parameter is `inf` ohms, that is the ports are open-circuit. When
a fault is triggered, the block changes the resistance between the two electrical ports
to the **Faulted resistance** value. The default value for this
parameter is `1e-3` ohms, that is the ports are short-circuited.

You can choose whether to issue an assertion when a fault occurs, by using the
**Reporting when a fault occurs** parameter. The assertion can take
the form of a warning or an error. By default, the block does not issue an
assertion.

The physical output *X* represents the fault state; if the block is
faulted, the output is `1`, otherwise, it is `0`. The
physical signal input *F* is the external fault trigger signal and is
used only if **Enable external fault trigger** is set to
`Yes`.
