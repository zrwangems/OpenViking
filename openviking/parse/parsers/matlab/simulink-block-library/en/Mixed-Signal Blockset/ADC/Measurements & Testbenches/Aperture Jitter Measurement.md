---
type: simulink-block
title: 'Aperture Jitter Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Measurements & Testbenches'
documentation_page: 'aperturejittermeasurement'
documentation_source_path: 'ref/aperturejittermeasurement.html'
language: en
---

# Aperture Jitter Measurement

## Ports
```yaml
ports:
- name: clk
  summary: Clock signal input scalar
  direction: input
  data_types: double
- name: jitter
  summary: Jitter output scalar
  direction: output
  data_types: double
```

### Input

### **clk** — Clock signal input scalar

Clock signal input, specified as a scalar in volts.

**Data Types:** `double`
### Output

### **jitter** — Jitter output scalar

Aperture jitter output, returned as a scalar in seconds.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Frequency
  summary: Input clock frequency 1e6 (default) | real positive scalar
  group: ''
- name: Recommended min. simulation stop time
  summary: Minimum time the simulation must run for meaningful result 9.901e-05 (default) | scalar
  group: ''
- name: Min
  summary: Minimum value of clock signal 0 (default) | real scalar
  group: ''
- name: Max
  summary: Maximum value of clock signal 1 (default) | real scalar
  group: ''
- name: Hold off time (s)
  summary: Delay before measurement analysis 0 (default) | nonnegative real scalar
  group: ''
```

### **Frequency** — Input clock frequency `1e6` (default) | real positive scalar

Input clock frequency, specified as a real positive scalar in Hz.

#### Programmatic Use

- Use `get_param(gcb,'Frequency')` to view the current
  value of **Frequency**.
- Use `set_param(gcb,'Frequency',value)` to set
  **Frequency** to a specific value.

### **Recommended min. simulation stop time** — Minimum time the simulation must run for meaningful result `9.901e-05` (default) | scalar

Minimum time the simulation must run for meaningful result, specified as a scalar in
seconds. This is calculated using the JEDEC Standards for measuring aperture
jitter.

#### Signal range

### **Min** — Minimum value of clock signal `0` (default) | real scalar

Minimum value of clock signal, specified as a real scalar in volts.

#### Programmatic Use

- Use `get_param(gcb,'InputMin')` to view the current value
  of **Min**.
- Use `set_param(gcb,'InputMin',value)` to set
  **Min** to a specific value.

### **Max** — Maximum value of clock signal `1` (default) | real scalar

Maximum value of clock signal, specified as a real scalar in volts.

#### Programmatic Use

- Use `get_param(gcb,'InputMax')` to view the current value
  of **Max**.
- Use `set_param(gcb,'InputMax',value)` to set
  **Max** to a specific value.

### **Hold off time (s)** — Delay before measurement analysis `0` (default) | nonnegative real scalar

Delays measurement analysis to avoid corruption by transients, specified as a
nonnegative real scalar in seconds.

#### Programmatic Use

- Use `get_param(gcb,'HoldOffTime')` to view the current
  value of **Hold off time (s)**.
- Use `set_param(gcb,'HoldOffTime',value)` to set
  **Hold off time (s)** to a specific value.

**Data Types:** `double`
## Libraries

Mixed-Signal Blockset / ADC / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Measure aperture jitter of periodic signals

The Aperture Jitter Measurement measure the aperture jitter of periodic
signals. In practical data converters, there is a delay between the sampling edge of the
sample clock signal and when the sample is actually taken. This delay is known as aperture
delay. Aperture jitter is the sample to sample variation between aperture delay.
