---
type: simulink-block
title: 'Translational Power Sensor'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'translationalpowersensor'
documentation_source_path: 'ref/translationalpowersensor.html'
language: en
---

# Translational Power Sensor

## Ports
```yaml
ports:
- name: P
  summary: Translational power, W physical signal
  direction: input
- name: S
  summary: Driving source mechanical translational
  direction: conserving
- name: R
  summary: Rod mechanical translational
  direction: conserving
- name: C
  summary: Case mechanical translational
  direction: conserving
```

### Input

### **P** — Translational power, W physical signal

Physical signal input port associated with the translational power, in
W.
### Conserving

### **S** — Driving source mechanical translational

Mechanical translational conserving port associated with the driving
source.

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with the rod or
shaft.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the
case.
## Parameters
```yaml
parameters:
- name: Measurement type
  summary: Option to measure power Instantaneous power (default) | Average power over a specified period | Average power over
    a vibration
  group: ''
- name: Averaging period
  summary: Power averaging period 1 s (default) | positive scalar
  group: ''
- name: Maximum vibration frequency
  summary: Maximum vibration frequency 1000 Hz (default) | positive scalar
  group: ''
```

### **Measurement type** — Option to measure power `Instantaneous power` (default) | `Average power over a specified period` | `Average power over a vibration`

Whether to measure instantaneous power, average power over a specified
period, or average power over a vibration.

- `Instantaneous power` — Output the power
  measured for the current time step.
- `Average power over a specified period` —
  Output the power averaged over a fixed time period.
- `Average power over a vibration` — Output
  the power averaged over one vibration period.

### **Averaging period** — Power averaging period `1` `s` (default) | positive scalar

Time period over which to average the power. Typical values include the
cycle length of a reciprocating device or the actuation force.

### **Maximum vibration frequency** — Maximum vibration frequency `1000` `Hz` (default) | positive scalar

Maximum vibration frequency over which to average the power. Very high
values tend to reduce simulation speed. Very low values tend to result in
lower power measurements.
## Libraries

Simscape / Driveline / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Average or instantaneous translational power sensor

The Translational Power Sensor block represents a
sensor that measures the translational power change due to one or more driveline
components connected between ports **R** and **C**.
The power output can be an instantaneous or average value. Two averaging options are
available: period and vibration averaging.

The instantaneous power is the product of the current velocity and force. Use the
instantaneous power to analyze peak power transmission and identify heavily loaded
components.

The time-averaged power is the integral of the instantaneous power over one sample
period, divided by that period. For simulation times smaller than the sample period, the
average power is zero. The power is constant for each sample period.

The vibration-averaged power is the integral of the power over one vibration period,
divided by that period. The vibration period is the time between two consecutive
crossings from negative to positive velocity values. Use this averaging method only for
oscillations with velocity passing through zero. If the vibration has a variable
frequency, the averaging period can change. For simulation times smaller than the
vibration period, the average power is zero. The power output is constant for each
vibration period.
