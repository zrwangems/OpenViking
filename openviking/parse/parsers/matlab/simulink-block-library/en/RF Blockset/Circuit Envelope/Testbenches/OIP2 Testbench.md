---
type: simulink-block
title: 'OIP2 Testbench'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Testbenches'
documentation_page: 'oip2testbench'
documentation_source_path: 'ref/oip2testbench.html'
language: en
---

# OIP2 Testbench

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Use Internal Configuration block
  summary: Use testbench internal configuration block on (default) | off
  group: ''
- name: Simulate noise (both stimulus and DUT internal)
  summary: Enable noise modeling in stimulus signal on (default) | off
  group: ''
- name: Input power amplitude (dBm)
  summary: Input power to DUT -30 (default) | scalar
  group: ''
- name: Input frequency (Hz)
  summary: Carrier frequency of DUT 2.1e9 (default) | scalar
  group: ''
- name: Output frequency (Hz)
  summary: Output frequency of DUT 2.1e9 (default) | scalar
  group: ''
- name: Baseband bandwidth (Hz)
  summary: Baseband bandwidth of input signal 10e6 (default) | scalar
  group: ''
- name: Ratio of test tone frequency to baseband bandwidth
  summary: Position of the test tones 1/8 (default) | scalar
  group: ''
- name: Source resistance (Ohm)
  summary: Source resistance to measure DUT 50 (default) | positive finite scalar
  group: ''
- name: Load resistance (Ohm)
  summary: Load resistance to measure DUT 50 (default) | positive finite scalar
  group: ''
- name: Show Response spectrum
  summary: View response spectrum using a spectrum scope during simulation on (default) | off
  group: ''
- name: Ground and hide negative terminals
  summary: Internally ground and hide RF circuit terminals on (default) | off
  group: ''
```

#### Parameters

### **Use Internal Configuration block** — Use testbench internal configuration block on (default) | off

Select to use testbench internal configuration block. Clear this parameter
to specify your own configuration block.

**Note**

When using your own configuration block, parameters such as step size,
fundamental tones, harmonic order, and simulate noise may affect the
measured results.

### **Simulate noise (both stimulus and DUT internal)** — Enable noise modeling in stimulus signal on (default) | off

Select to enable noise modeling in the stimulus signal entering the DUT
and inside the DUT.

#### Dependencies

To enable this parameter, select **Use internal Configuration
block**.

### **Input power amplitude (dBm)** — Input power to DUT `-30` (default) | scalar

Input power to DUT, specified as a scalar in dBm. You can change the input
power by entering the value in the text box or selecting a value using the
knob. The specified input power represents the power available at the input
ports of the DUT. The valid values are between -90 dBm and 60 dBm.

### **Input frequency (Hz)** — Carrier frequency of DUT `2.1e9` (default) | scalar

Carrier frequency of the DUT, specified as a scalar in Hz. Input frequency
must be greater than baseband bandwidth.

### **Output frequency (Hz)** — Output frequency of DUT `2.1e9` (default) | scalar

Output frequency of DUT, specified as a scalar in Hz. Output frequency
must be greater than baseband bandwidth.

### **Baseband bandwidth (Hz)** — Baseband bandwidth of input signal `10e6` (default) | scalar

Baseband bandwidth of input signal, specified as a scalar in Hz. The value
must be greater than zero.

### **Ratio of test tone frequency to baseband bandwidth** — Position of the test tones `1/8` (default) | scalar

Position of the test tones, specified as a scalar.

### **Source resistance (Ohm)** — Source resistance to measure DUT `50` (default) | positive finite scalar

Source resistance to measure DUT, specified as a positive finite scalar in
ohms.

### **Load resistance (Ohm)** — Load resistance to measure DUT `50` (default) | positive finite scalar

Load resistance to measure DUT, specified as a positive finite scalar in
ohms.

### **Show Response spectrum** — View response spectrum using a spectrum scope during simulation on (default) | off

Select to view response spectrum using a spectrum scope during simulation.

**Note**

To view the response spectrum using a Spectrum Analyzer, you need a
DSP System Toolbox™ license.

### **Ground and hide negative terminals** — Internally ground and hide RF circuit terminals on (default) | off

Select to internally ground and hide the negative terminals. Clear to
expose the negative terminals. By exposing these terminals, you can connect
them to other parts of your model.
## Libraries

RF Blockset / Circuit Envelope / Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Measure output second intercept point of system

Use the `OIP2 Testbench` block to measure the output second intercept
point (OIP2) of an RF device under test (DUT).
