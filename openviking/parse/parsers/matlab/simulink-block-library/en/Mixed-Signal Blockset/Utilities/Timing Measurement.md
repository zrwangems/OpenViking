---
type: simulink-block
title: 'Timing Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'timingmeasurement'
documentation_source_path: 'ref/timingmeasurement.html'
language: en
---

# Timing Measurement

## Ports
```yaml
ports:
- name: reference
  summary: Input signal scalar
  direction: input
  data_types: double
- name: test
  summary: Test signal scalar
  direction: input
  data_types: double
- name: period
  summary: Period of input signal scalar
  direction: output
  data_types: double
- name: frequency
  summary: Frequency of input signal scalar
  direction: output
  data_types: double
- name: rise time
  summary: Rise time of input signal scalar
  direction: output
  data_types: double
- name: fall time
  summary: Fall time of input signal scalar
  direction: output
  data_types: double
- name: duty cycle
  summary: Duty cycle of input signal scalar
  direction: output
  data_types: double
- name: delay
  summary: Delay of input signal scalar
  direction: output
  data_types: double
```

### Input

### **reference** — Input signal scalar

Input signal whose timing metrics are being measured, specified as a
scalar.

**Data Types:** `double`

### **test** — Test signal scalar

Test signal against which the delay of the input signal is measured, specified as
a scalar.

#### Dependencies

To enable this port, select **Delay** as a measurement option
in the **Selection** tab.

**Data Types:** `double`
### Output

### **period** — Period of input signal scalar

Period of the input signal, returned as a scalar.

**Data Types:** `double`

### **frequency** — Frequency of input signal scalar

Frequency of the input signal, returned as a scalar.

#### Dependencies

To enable this port, select **Frequency** as a measurement
option in the **Selection** tab.

**Data Types:** `double`

### **rise time** — Rise time of input signal scalar

Rise time of the input signal, returned as a scalar.

#### Dependencies

To enable this port, select **Rise Time** as a measurement
option in the **Selection** tab.

**Data Types:** `double`

### **fall time** — Fall time of input signal scalar

Fall time of the input signal, returned as a scalar.

#### Dependencies

To enable this port, select **Fall time** as a measurement
option in the **Selection** tab.

**Data Types:** `double`

### **duty cycle** — Duty cycle of input signal scalar

Duty cycle of the input signal, returned as a scalar.

#### Dependencies

To enable this port, select **Duty Cycle** as a measurement
option in the **Selection** tab.

**Data Types:** `double`

### **delay** — Delay of input signal scalar

Delay of the input signal, returned as a scalar.

#### Dependencies

To enable this port, select **Delay** as a measurement option
in the **Selection** tab.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Period
  summary: Measure period of input signal on (default) | off
  group: Selection
- name: Frequency
  summary: Measure frequency of input signal off (default) | on
  group: Selection
- name: Rise Time
  summary: Measure rise time of input signal off (default) | on
  group: Selection
- name: Fall Time
  summary: Measure fall time of input signal off (default) | on
  group: Selection
- name: Duty Cycle
  summary: Measure duty cycle of input signal off (default) | on
  group: Selection
- name: Delay
  summary: Measure delay of input signal off (default) | on
  group: Selection
- name: Use same reference threshold for all measurements
  summary: Use the same reference threshold for measuring all timing metrics on (default) | off
  group: Configuration
- name: Reference threshold (V)
  summary: Reference threshold used for measuring timing metrics 0 (default) | scalar
  group: Configuration
- name: Reference threshold (V)
  summary: Reference threshold voltage used to measure period and/or frequency 0 (default) | scalar
  group: Configuration
- name: Input range (V)
  summary: Peak-to-peak value of input signal [-1 1] (default) | 2-element row vector
  group: Configuration
- name: Type
  summary: Input threshold levels to measure rise/fall times 80%/20% (default) | 90%/10%
  group: Configuration
- name: Reference threshold (V)
  summary: Reference threshold voltage used to measure duty cycle 0 (default) | scalar
  group: Configuration
- name: Reference threshold (V)
  summary: Threshold voltage level in signal of interest used to measure delay 0 (default) | scalar
  group: Configuration
- name: Test threshold (V)
  summary: Threshold voltage level in test signal used to measure delay 0 (default) | scalar
  group: Configuration
```

### Selection

### **Period** — Measure period of input signal on (default) | off

Select to measure the period of the input signal.

Period is defined as the time required to complete one full cycle of a periodic
signal, specified in seconds.

### **Frequency** — Measure frequency of input signal off (default) | on

Select to measure the frequency of the input signal.

Frequency is defined as the number of cycles completed per unit of time by a
periodic signal, specified in hertz. It is the inverse of
**Period**.

### **Rise Time** — Measure rise time of input signal off (default) | on

Select to measure the rise time of the input signal.

Rise time is defined as the time required by the rising edge of the signal to
reach from 10% to 90% (or 20% to 80%) of its steady state value, specified in
seconds.

### **Fall Time** — Measure fall time of input signal off (default) | on

Select to measure the fall time of the input signal.

Fall time is defined as the time required by the falling edge of the signal to go
from 90% to 10% (or 80% to 20%) of its steady state value, specified in
seconds.

### **Duty Cycle** — Measure duty cycle of input signal off (default) | on

Select to measure the duty cycle of the input signal.

Duty cycle is defined as the ratio of positive pulse width to period, specified as
a fraction.

### **Delay** — Measure delay of input signal off (default) | on

Select to measure the delay of the input signal.

Delay is defined as the time difference between the threshold crossing points
between the signal of interest against a test signal, specified in seconds.

### Configuration

### **Use same reference threshold for all measurements** — Use the same reference threshold for measuring all timing metrics on (default) | off

Select to use the same reference threshold for measuring all timing
metrics.

### **Reference threshold (V)** — Reference threshold used for measuring timing metrics `0` (default) | scalar

Reference threshold voltage used for measuring all timing metrics, specified as a
scalar in volts.

#### Dependencies

To enable this parameter, select **Use same reference threshold for all
measurements** in the **Configuration** tab.

#### Programmatic Use

- Use `get_param(gcb,'SameRefThreshold')` to view the
  current value of **Reference threshold (V)**.
- Use `set_param(gcb,'SameRefThreshold',value)` to set
  **Reference threshold (V)** to a specific value.

#### Period/Frequency

### **Reference threshold (V)** — Reference threshold voltage used to measure period and/or frequency `0` (default) | scalar

Reference threshold voltage used to measure the period and/or the frequency of the
signal of interest, specified as a scalar in volts.

#### Dependencies

To enable this parameter, deselect **Use same reference threshold for
all measurements** in the **Configuration** tab and
select **Period** and/or **Frequency** in the
**Selection** tab.

#### Programmatic Use

- Use `get_param(gcb,'PeriodRefThreshold')` to view the
  current value of **Reference threshold (V)**.
- Use `set_param(gcb,'PeriodRefThreshold',value)` to set
  **Reference threshold (V)** to a specific value.

#### Rise/Fall Time

### **Input range (V)** — Peak-to-peak value of input signal `[-1 1]` (default) | 2-element row vector

Peak-to-peak value of the input signal, specified as a 2-element row vector in
volts. The first element defines the notch value of the input signal and the second
element defines the peak value. **Input range (V)** is used to
calculate the upper and lower threshold levels to calculate the rise/fall
times.

#### Dependencies

To enable this parameter, select **Rise Time** and/or
**Fall Time** in the **Selection** tab.

#### Programmatic Use

- Use `get_param(gcb,'Range')` to view the current value of
  **Reference threshold (V)**.
- Use `set_param(gcb,'Range',value)` to set
  **Reference threshold (V)** to a specific value.

### **Type** — Input threshold levels to measure rise/fall times `80%/20%` (default) | `90%/10%`

Determines the input threshold levels to measure the rise/fall times, specified as
either `80%/20%` or
`90%/10%`.

#### Dependencies

To enable this parameter, select **Rise Time** and/or
**Fall Time** in the **Selection** tab.

#### Programmatic Use

- Use `get_param(gcb,'MeasurementType')` to view the
  current value of **Reference threshold (V)**.
- Use `set_param(gcb,'MeasurementType',value)` to set
  **Reference threshold (V)** to a specific value.

#### Duty Cycle

### **Reference threshold (V)** — Reference threshold voltage used to measure duty cycle `0` (default) | scalar

Reference threshold voltage used to measure the duty cycle of the signal of
interest, specified as a scalar in volts.

#### Dependencies

To enable this parameter, deselect **Use same reference threshold for
all measurements** in the **Configuration** tab and
select **Duty Cycle** in the **Selection**
tab.

#### Programmatic Use

- Use `get_param(gcb,'DcRefThreshold')` to view the current
  value of **Reference threshold (V)**.
- Use `set_param(gcb,'DcRefThreshold',value)` to set
  **Reference threshold (V)** to a specific value.

#### Delay

### **Reference threshold (V)** — Threshold voltage level in signal of interest used to measure delay `0` (default) | scalar

Threshold voltage level in reference signal of interest whose delay is being
measured, specified as a scalar in volts.

#### Dependencies

To enable this parameter, deselect **Use same reference threshold for
all measurements** in the **Configuration** tab and
select **Delay** in the **Selection** tab.

#### Programmatic Use

- Use `get_param(gcb,'DelayRefThreshold')` to view the
  current value of **Reference threshold (V)**.
- Use `set_param(gcb,'DelayRefThreshold',value)` to set
  **Reference threshold (V)** to a specific value.

### **Test threshold (V)** — Threshold voltage level in test signal used to measure delay `0` (default) | scalar

Threshold voltage level in test signal against which the delay of the reference
signal is being measured, specified as a scalar in volts.

#### Dependencies

To enable this parameter, deselect **Use same reference threshold for
all measurements** in the **Configuration** tab and
select **Delay** in the **Selection** tab.

#### Programmatic Use

- Use `get_param(gcb,'DelayTstThreshold')` to view the
  current value of **Reference threshold (V)**.
- Use `set_param(gcb,'DelayTstThreshold',value)` to set
  **Reference threshold (V)** to a specific value.
## Libraries

Mixed-Signal Blockset / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Measure period, frequency, duty cycle, rise time, fall time, and delay of a signal

The Timing Measurement block measures the basic timing metrics such as
period, frequency, duty cycle, rise time, fall time, and delay of a signal.
