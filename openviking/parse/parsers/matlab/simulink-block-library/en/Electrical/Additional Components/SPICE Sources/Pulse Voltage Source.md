---
type: simulink-block
title: 'Pulse Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pulsevoltagesource'
documentation_source_path: 'ref/pulsevoltagesource.html'
language: en
---

# Pulse Voltage Source

## Ports
```yaml
ports:
- name: +
  summary: Positive voltage electrical
  direction: conserving
- name: '-'
  summary: Negative voltage electrical
  direction: conserving
```

### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the
pulse voltage source positive voltage

### **-** — Negative voltage electrical

Electrical conserving port associated with the
pulse voltage source negative voltage
## Parameters
```yaml
parameters:
- name: Initial value, V1
  summary: Initial output voltage 0 V (default)
  group: ''
- name: Pulse value, V2
  summary: High output voltage 0 V (default)
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
```

### **Initial value, V1** — Initial output voltage `0` `V` (default)

Value of the output voltage at time zero, in V.

### **Pulse value, V2** — High output voltage `0` `V` (default)

Value of the output voltage when the output is high,
in V.

### **Pulse delay time, TD** — Pulse delay time `0` `s` (default)

Time at which the pulse first starts, in s.

### **Pulse rise time, TR** — Pulse rise time `1e-9` `s` (default) | nonnegative scalar

Time it takes the output voltage to rise from the
**Initial value, V1** value to
the **Pulse value, V2** value. The
value must be greater than or equal to
`0`.

### **Pulse fall time, TF** — Pulse fall time `1e-9` `s` (default) | nonnegative scalar

Time it takes the output voltage to fall from the
**Pulse value, V2** value to the
**Initial value, V1** value. The
value must be greater than or equal to
`0`.

### **Pulse width, PW** — Output pulse time width `Inf` `s` (default) | positive scalar

Time width of the output pulse. The value must be
greater than `0`.

### **Pulse period, PER** — Output pulse period `Inf` `s` (default) | positive scalar

Period of the output pulse. For the default value,
`Inf``s`,
the block produces a single pulse with an infinite
period.
## Libraries

Simscape / Electrical / Sources Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Periodic square wave voltage source

The Pulse Voltage Source block represents a
voltage source whose output voltage value is a periodic square pulse as a
function of time and is independent of the current through the source. The
following equations describe the output voltage as a function of time:

Vout(0)=V1

Vout(TD)=V1

Vout(TD+TR)=V2

Vout(TD+TR+PW)=V2

Vout(TD+TR+PW+TF)=V1

Vout(TD+PER)=V1

where:

- *V1* is the
  output voltage at time zero.
- *V2* is the
  output voltage when the output is high.
- *TD* is the time at which the pulse
  first starts.
- *TR* is the time that it takes the
  output voltage to rise from
  *V1* to
  *V2*.
- *TF* is the time that it takes the
  output voltage to fall from
  *V2* to
  *V1*.
- *PW* is the time width of the output
  pulse.
- *PER* is the period of the output
  pulse.

The block determines the values at intermediate time points
by linear interpolation.

The specified values for *PW* and *PER* have
the following effect on the block output:

- If both *PW* and
  *PER* are infinite, the block
  produces a step response at time
  *TD*.
- If *PER* is infinite and
  *PW* is finite, the block
  produces a single pulse of width
  *PW* and infinite period.
- If *PW* is infinite and
  *PER* is finite, the block
  produces a step response with pulses of width
  *TR* to a value
  *V1* every *PER*
  seconds.
- If *PW* > *PER*,
  the block produces a step response with pulses of
  width *TR* to a value
  *V1* every *PER*
  seconds.
