---
type: simulink-block
title: 'Pulse Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pulsecurrentsource'
documentation_source_path: 'ref/pulsecurrentsource.html'
language: en
---

# Pulse Current Source

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the pulse current source
positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the pulse current source
negative terminal.
## Parameters
```yaml
parameters:
- name: Initial value, I1
  summary: Initial output current 0 A (default)
  group: ''
- name: Pulse value, I2
  summary: High output current 0 A (default)
  group: ''
- name: Pulse delay time, TD
  summary: Pulse delay time 0 s (default)
  group: ''
- name: Pulse rise time, TR
  summary: Pulse rise time 1e-9 s (default) | nonnegative scalar
  group: ''
- name: Pulse fall time, TF
  summary: Pulse fall time 1e-9 s (default) | nonnegative scalar
  group: ''
- name: Pulse width, PW
  summary: Output pulse time width Inf s (default) | positive scalar
  group: ''
- name: Pulse period, PER
  summary: Output pulse period Inf s (default) | positive scalar
  group: ''
- name: Include parallel conductance, GMIN
  summary: Whether to include parallel conductance Yes (default) | No
  group: ''
```

### **Initial value, I1** — Initial output current `0` `A` (default)

Value of the output current at time zero, in A.

### **Pulse value, I2** — High output current `0` `A` (default)

Value of the output current when the output is high, in A.

### **Pulse delay time, TD** — Pulse delay time `0` `s` (default)

Time at which the pulse first starts, in s.

### **Pulse rise time, TR** — Pulse rise time `1e-9` `s` (default) | nonnegative scalar

Time it takes the output current to rise from the **Initial value,
I1** value to the **Pulse value, I2** value.
The value must be greater than or equal to `0`.

### **Pulse fall time, TF** — Pulse fall time `1e-9` `s` (default) | nonnegative scalar

Time it takes the output current to fall from the **Pulse value,
I2** value to the **Initial value, I1** value.
The value must be greater than or equal to `0`.

### **Pulse width, PW** — Output pulse time width `Inf` `s` (default) | positive scalar

Time width of the output pulse. The value must be greater than
`0`.

### **Pulse period, PER** — Output pulse period `Inf` `s` (default) | positive scalar

Period of the output pulse. For the default value,
`Inf``s`, the block produces a
single pulse with an infinite period.

### **Include parallel conductance, GMIN** — Whether to include parallel conductance `Yes` (default) | `No`

Specify if the current source includes a parallel conductance. The value of the parallel conductance, *GMIN*, depends on whether your model contains an Environment Parameters block.

This table shows the possible values of the parallel conductance,
*GMIN*:

**Values of parallel conductance, GMIN**

| Include parallel conductance, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **Model contains Environment Parameters block** | **Model does not contain Environment Parameters block** | Parallel conductance, *GMIN*, is not included and it does not affect the current source. | | |
| *GMIN* is equal to the value of the **GMIN** parameter in the Environment Parameters block. | *GMIN* = `1e-12` `Ohm` |
## Libraries

Simscape / Electrical / Sources Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Periodic square wave current source

The Pulse Current Source block represents a current
source whose output current value is a periodic square pulse as a function of time and
is independent of the voltage across the terminals of the source. The following
equations describe the current through the source as a function of time:

Iout(0)=I1

Iout(TD)=I1

Iout(TD+TR)=I2

Iout(TD+TR+PW)=I2

Iout(TD+TR+PW+TF)=I1

Iout(TD+PER)=I1

Where:

- *I1* is the output current at time
  zero.
- *I2* is the output current when
  the output is high.
- *TD* is the time at which the pulse first starts.
- *TR* is the time that it takes the output current to rise
  from *I1* to
  *I2*.
- *TF* is the time it takes the output current to fall from
  *I2* to
  *I1*.
- *PW* is the time width of the output pulse.
- *PER* is the period of the output pulse.

The block determines the values at intermediate time points by linear
interpolation.

The specified values for *PW* and *PER* have the
following effect on the block output:

- If both *PW* and *PER* are infinite, the
  block produces a step response at time *TD*.
- If *PER* is infinite and *PW* is
  finite, the block produces a single pulse of width *PW* and
  infinite period.
- If *PW* is infinite and *PER* is finite,
  the block produces a step response with pulses of width
  *TR* to a value
  *I1* every
  *PER* seconds.
- If *PW* > *PER*, the block produces a
  step response with pulses of width *TR* to a value
  *I1* every
  *PER* seconds.

The block uses a small conductance internally to prevent numerical simulation issues.
The conductance connects the + and - ports of the device and has a conductance
*GMIN*:

- By default, *GMIN* matches the **GMIN**
  parameter of the Environment Parameters
  block, whose default value is
  `1e–12``1/Ohm`.
- To change *GMIN*, add an Environment
  Parameters block to your model and set the
  **GMIN** parameter to the desired value.
