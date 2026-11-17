---
type: simulink-block
title: 'Rotational Power Sensor'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'rotationalpowersensor'
documentation_source_path: 'ref/rotationalpowersensor.html'
language: en
---

# Rotational Power Sensor

## Ports
```yaml
ports:
- name: P
  summary: Change in rotational power, W physical signal
  direction: conserving
- name: C
  summary: Follower port mechanical rotational
  direction: conserving
- name: R
  summary: Base port mechanical rotational
  direction: conserving
- name: S
  summary: Source port mechanical rotational
  direction: conserving
```

### Physical Signal

### **P** — Change in rotational power, W physical signal

Physical signal port that outputs the change in rotational
power.
### Conserving

### **C** — Follower port mechanical rotational

Mechanical rotational conserving port associated with the case.

### **R** — Base port mechanical rotational

Mechanical rotational conserving port associated with the load.

### **S** — Source port mechanical rotational

Mechanical rotational conserving port associated with driving source.
## Parameters
```yaml
parameters:
- name: Measurement type
  summary: Power measuring method Instantaneous power (default) | Average power over a specified period | Average power over
    a vibration | Average power over a revolution
  group: ''
- name: Averaging period
  summary: Timespan for power averaged over a specified period 1 s (default) | positive scalar
  group: ''
- name: Maximum vibration frequency
  summary: Highest frequency to use when averaging power over a vibration 1000 Hz (default) | positive scalar
  group: ''
- name: Maximum rotational speed
  summary: Highest angular velocity to use when averaging power over revolution 1000 rpm (default) | positive scalar
  group: ''
```

### **Measurement type** — Power measuring method `Instantaneous power` (default) | `Average power over a specified period` | `Average power over a vibration` | `Average power over a revolution`

Option to measure the instantaneous power or an average power measurement.

- `Instantaneous power` — Output the
  rotational power measured at the current simulation time
  step.
- `Average power over a specified
  period` — Output the rotational power averaged
  over a fixed time period.
- `Average power over a vibration` —
  Output the rotational power averaged over one vibration
  period.
- `Average power over a revolution` —
  Output the rotational power averaged over one revolution
  period.

### **Averaging period** — Timespan for power averaged over a specified period `1` `s` (default) | positive scalar

Time period that the block uses to compute the average power. For example,
you can set this value to the cycle length of a rotating device.

#### Dependencies

To enable this parameter, set **Measurement type** to
`Average power over a specified
period`.

### **Maximum vibration frequency** — Highest frequency to use when averaging power over a vibration `1000` `Hz` (default) | positive scalar

Highest vibration frequency to use to average the rotational power. Very
high values can reduce simulation speed. Very low values can result in lower
power measurements.

#### Dependencies

To enable this parameter, set **Measurement type** to
`Average power over a vibration`.

### **Maximum rotational speed** — Highest angular velocity to use when averaging power over revolution `1000` `rpm` (default) | positive scalar

Highest speed to use to average the rotational power. Very high values can
reduce simulation speed. Very low values can result in lower power
measurements.

#### Dependencies

To enable this parameter, set **Measurement type** to
`Average power over a revolution`.
## Libraries

Simscape / Driveline / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Measure average or instantaneous rotational power

The Rotational Power Sensor block measures the rotational
power change between ports **R** and **C**. The
physical signal output can be an instantaneous or averaged value depending on what you
select for the **Measurement type** parameter.

When you set:

- **Measurement type** to `Instantaneous
  power`, the instantaneous power is the product of the current
  angular velocity and torque. Use this setting to analyze peak power transmission
  and identify heavily loaded components.
- **Measurement type** to `Average power over a
  specified period`, the time-averaged power is the integral of
  the instantaneous power over one sample period, divided by that period. For
  simulation times smaller than the sample period, the average power is zero. The
  power output is constant for each sample period.
- **Measurement type** to `Average power over a
  vibration`, the average vibration power is the integral of the
  power over one vibration period, divided by that period. The vibration period is
  the time between two consecutive crossings from negative to positive velocity
  values. If the vibration has a variable frequency, the averaging period can
  change. For simulation times smaller than the vibration period, the average
  power is zero. The power output is constant for each vibration period.
- **Measurement type** to `Average power over a
  revolution`, the average revolution power is the integral of
  the instantaneous power over one revolution period, divided by that period. The
  revolution period is defined as the time between two consecutive crossings of
  zero angular position. If the revolution has a variable frequency, the averaging
  period can change. For simulation times smaller than the revolution period, the
  average power is zero. The power output is constant for each revolution
  period.
