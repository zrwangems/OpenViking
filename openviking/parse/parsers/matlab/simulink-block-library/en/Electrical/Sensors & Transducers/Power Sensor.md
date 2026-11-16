---
type: simulink-block
title: 'Power Sensor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'powersensor'
documentation_source_path: 'ref/powersensor.html'
language: en
---

# Power Sensor

## Ports

### Output

### **P** — Measured power physical signal

Physical signal port that outputs the measured power
### Conserving

### **S** — Positive supply rail electrical

Electrical conserving port connected to the positive supply
rail

### **+** — Load positive terminal electrical

Electrical conserving port connected to the positive terminal of the
load

### **-** — Load negative terminal electrical

Electrical conserving port connected to the negative terminal of the
load

## Parameters

### **Measurement type** — Measurement type `Instantaneous power` (default) | `Instantaneous power`

Select whether you want to measure `Instantaneous
power` or `Average power over a specified
period`. The default value is `Instantaneous
power`.

### **Averaging period** — Averaging period `1e-4` `s` (default)

Fixed period of time for measuring the average power.

#### Dependencies

This parameter is visible only when you select `Average
power over a specified period` for the
**Measurement type** parameter.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Ideal instantaneous or cycle-average power measurement

The Power Sensor block calculates the power taken by
the load connected across the + and - terminals under the assumption that only the load
is connected to the + terminal. Refer to the block icon for the arrangement of internal
current and voltage sensors.

The sensor can return either instantaneous power, or power averaged over a fixed time
period. Use the latter option for periodic current and voltage waveforms such as those
associated with PWM control.

The following figure shows how you connect the block to measure power dissipated in a
resistor.

For an alternative workflow using data logging to view component powers, see the Buck Converter example.
