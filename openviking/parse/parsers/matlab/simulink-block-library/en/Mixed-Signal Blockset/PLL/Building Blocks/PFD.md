---
type: simulink-block
title: 'PFD'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'pfd'
documentation_source_path: 'ref/pfd.html'
language: en
---

# PFD

## Ports
```yaml
ports:
- name: reference
  summary: Reference frequency scalar
  direction: input
  data_types: double
- name: feedback
  summary: Feedback frequency scalar
  direction: input
  data_types: double
- name: up
  summary: Transmits reference frequency scalar
  direction: output
  data_types: double
- name: down
  summary: Transmits feedback frequency scalar
  direction: output
  data_types: double
```

### Input

### **reference** — Reference frequency scalar

Input port that transmits reference frequency to determine phase
error.

**Data Types:** `double`

### **feedback** — Feedback frequency scalar

Output port that transmits the feedback frequency to determine the
phase error. In a PLL system, the output of the VCO is fed back through **feedback** port
to PFD after passing through a clock divider.

**Data Types:** `double`
### Output

### **up** — Transmits reference frequency scalar

Output port that transmits reference frequency to Charge Pump to convert the phase error into current. The
difference in the duty cycle of signals in **up** and
**down** ports is proportional to the phase
difference between the signals in **reference** and
**feedback** ports.

**Data Types:** `double`

### **down** — Transmits feedback frequency scalar

Output port that transmits feedback frequency to Charge Pump to convert the phase error into current. The
difference in the duty cycle of signals in **up** and
**down** ports is proportional to the phase
difference between the signals in **reference** and
**feedback** ports.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Deadband compensation (s)
  summary: Delay added for active output near zero phase offset 30e-12 (default) | positive real scalar
  group: Configuration
- name: Enable increased buffer size
  summary: Enable increased buffer size off (default) | on
  group: Configuration
- name: Buffer size
  summary: Number of samples of the input buffering available during simulation 10 (default) | positive integer scalar
  group: Configuration
- name: Enable impairments
  summary: Add circuit impairments to simulation on (default) | off
  group: Impairments
- name: Output step size calculation
  summary: Determine how output step size is calculated Default (default) | Advanced
  group: Impairments
- name: Maximum frequency of interest (Hz)
  summary: Maximum frequency of interest at output 10e9 (default) | positive real scalar
  group: Impairments
- name: Rise/fall time (s)
  summary: 20% – 80% rise/fall time for up output port of PFD 3e-11 (default) | positive real scalar
  group: Impairments
- name: Propagation Delay (s)
  summary: Delay from input port to output port of PFD 50e-12 (default) | positive real scalar
  group: Impairments
```

### Configuration

### **Deadband compensation (s)** — Delay added for active output near zero phase offset `30e-12` (default) | positive real scalar

Delay added for active output near zero phase offset, specified as a
positive real scalar in seconds. Deadband is the phase offset band near
zero phase offset for which the PFD output is negligible.

#### Programmatic Use

- Use
  `get_param(gcb,'DeadbandCompensation')`
  to view the current value of **Deadband
  compensation**.
- Use
  `set_param(gcb,'DeadbandCompensation',value)`
  to set **up Rise/fall time** to a specific
  value.

**Data Types:** `double`

### **Enable increased buffer size** — Enable increased buffer size off (default) | on

Select to enable increased buffer size during simulation. This
increases the buffer size of the Variable Pulse Delay, Logic Decision, and Slew
Rate blocks inside the PFD block. By default,
this option is deselected.

### **Buffer size** — Number of samples of the input buffering available during simulation `10` (default) | positive integer scalar

Number of samples of the input buffering available during simulation,
specified as a positive integer scalar. This sets the buffer size of the
Variable Pulse Delay, Logic Decision, and Slew
Rate blocks inside the PFD block.

Selecting different simulation solver or sampling strategies can
change the number of input samples needed to produce an accurate output
sample. Set the **Buffer size** to a large enough value
so that the input buffer contains all the input samples required.

#### Dependencies

This parameter is only available when **Enable increased
buffer size** option is selected in the
**Configuration** tab.

#### Programmatic Use

- Use `get_param(gcb,'NBuffer')` to view
  the current value of **Buffer
  size**.
- Use `set_param(gcb,'NBuffer',value)` to
  set **Buffer size** to a specific
  value.

**Data Types:** `double`

### Impairments

### **Enable impairments** — Add circuit impairments to simulation on (default) | off

Select to add circuit impairments such as rise/fall time and
propagation delay to the simulation. By default, this option is
selected.

### **Output step size calculation** — Determine how output step size is calculated `Default` (default) | `Advanced`

Determine how output step size is calculated:

- Select `Default` to calculate output step
  size from rise/fall time. Output step size (ΔT) is given by ΔT=(Rise/fall time)26 · 0.22.
- Select `Advanced` to calculate output step
  size from maximum frequency of interest. Output step size (ΔT)
  is given by ΔT=Rise/fall time6 · Maximum frequency of interest.

#### Dependencies

To enable this parameter, select **Enable
Impairments** in the **Impairments**
tab.

### **Maximum frequency of interest (Hz)** — Maximum frequency of interest at output `10e9` (default) | positive real scalar

Maximum frequency of interest at the output, specified as a positive
real scalar in Hz.

#### Dependencies

To enable this parameter, select **Enable
Impairments** in the **Impairments**
tab and choose **Advanced** for **Output
step size calculation**.

#### Programmatic Use

- Use `get_param(gcb,'MaxFreqInterest')`
  to view the current value of **Maximum frequency of
  interest (Hz)**.
- Use
  `set_param(gcb,'MaxFreqInterest',value)`
  to set **Maximum frequency of interest
  (Hz)** to a specific value.

**Data Types:** `double`

### **Rise/fall time (s)** — 20% – 80% rise/fall time for up output port of PFD `3e-11` (default) | positive real scalar

20% – 80% rise/fall time for the up output port of the PFD, specified
as a positive real scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable
Impairments** in the **Impairments**
tab.

#### Programmatic Use

- Use `get_param(gcb,'RiseFallTime')` to
  view the current value of **Rise/fall time
  (s)**.
- Use
  `set_param(gcb,'RiseFallTime',value)` to
  set **Impairments** to a specific
  value.

**Data Types:** `double`

### **Propagation Delay (s)** — Delay from input port to output port of PFD `50e-12` (default) | positive real scalar

Delay from the input port to output port of the PFD, specified as a
positive real scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable
Impairments** in the **Impairments**
tab.

#### Programmatic Use

- Use `get_param(gcb,'PropDelay')` to
  view the current value of **Propagation Delay
  (s)**.
- Use `set_param(gcb,'PropDelay',value)`
  to set **Propagation Delay (s)** to a
  specific value.

**Data Types:** `double`
## Libraries

Mixed-Signal Blockset / PLL / Building Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Phase/frequency detector that compares phase and frequency between two signals

The PFD block produces two output pulses that differ in duty cycle. The
difference in the duty cycle is proportional to the phase difference between input
signals. In frequency synthesizer circuits, such as phase-locked loops (PLL), the
PFD block compares the phase and frequency between the reference
signal and signal generated by the VCO block
and determines the phase error.
