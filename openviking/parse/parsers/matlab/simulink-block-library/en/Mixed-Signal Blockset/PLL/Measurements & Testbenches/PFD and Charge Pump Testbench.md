---
type: simulink-block
title: 'PFD and Charge Pump Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Measurements & Testbenches'
documentation_page: 'pfdandchargepumptestbench'
documentation_source_path: 'ref/pfdandchargepumptestbench.html'
language: en
---

# PFD and Charge Pump Testbench

## Ports
```yaml
ports:
- name: from PFD up
  summary: Measures PFD reference frequency scalar
  direction: input
  data_types: double
- name: from PFD down
  summary: Measures PFD feedback frequency scalar
  direction: input
  data_types: double
- name: from charge pump
  summary: Measures charge pump output current scalar
  direction: input
  data_types: double
- name: to PFD reference
  summary: Provides reference frequency to PFD scalar
  direction: output
  data_types: double
- name: to PFD feedback
  summary: Provides feedback frequency to PFD scalar
  direction: output
  data_types: double
```

### Input

### **from PFD up** — Measures PFD reference frequency scalar

Measures the reference frequency of the PFD block.

**Data Types:** `double`

### **from PFD down** — Measures PFD feedback frequency scalar

Measures the feedback frequency of the PFD block.

**Data Types:** `double`

### **from charge pump** — Measures charge pump output current scalar

Measures the output current of the Charge Pump block.

**Data Types:** `double`
### Output

### **to PFD reference** — Provides reference frequency to PFD scalar

Provides reference frequency to the PFD to determine phase error.

**Data Types:** `double`

### **to PFD feedback** — Provides feedback frequency to PFD scalar

Provides feedback frequency to the PFD block.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Phase sweep (°)
  summary: Maximum phase excursion from phase offset 300 (default) | real positive scalar
  group: Stimulus
- name: Phase offset (°)
  summary: Relative phase value at center of phase sweep 0 (default) | real scalar
  group: Stimulus
- name: Clock frequency (Hz)
  summary: Desired reference clock frequency 2.5e9 Hz (default) | real positive scalar
  group: Stimulus
- name: Number of phases in sweep
  summary: Total number of evenly spaced phase offsets to simulate 2000 (default) | real positive scalar
  group: Stimulus
- name: Duty cycle (%)
  summary: Duty cycle of stimulus clock 50 (default) | real positive scalar
  group: Stimulus
- name: Plot figures on top after simulation
  summary: Plot figures on top after simulation on (default) | off
  group: Setup
- name: Report PFD metrics
  summary: Report PFD metrics on (default) | off
  group: Setup
- name: Report Charge Pump metrics
  summary: Report Charge Pump metrics on (default) | off
  group: Setup
- name: Logic Threshold (V)
  summary: Switching threshold at input of charge pump 0.5 (default) | real scalar
  group: Setup
- name: Enable increased buffer size
  summary: Enable increased buffer size off (default) | on
  group: Setup
- name: Buffer size
  summary: Number of samples of the input buffering available during simulation 5 (default) | positive integer scalar
  group: Setup
- name: Target deadband (°)
  summary: Maximum acceptable size of reduced sensitivity region near zero phase offset 0 (default) | real nonnegative scalar
  group: Target Metrics
- name: Target linear range (°)
  summary: Maximum phase offset at which the output remains approximately equal to the input offset 290 (default) | real positive
    scalar
  group: Target Metrics
- name: Target propagation delay (s)
  summary: Maximum acceptable delay from input to output 60e-12 (default) | real positive scalar
  group: Target Metrics
- name: Target rise/fall time (s)
  summary: Maximum acceptable 20% – 80% rise/fall time 30e-12 (default) | real positive scalar
  group: Target Metrics
- name: Target sensitivity (A/°)
  summary: Maximum acceptable charge pump sensitivity 1e-9 (default) | real positive scalar
  group: Target Metrics
- name: Target phase offset (°)
  summary: Maximum acceptable phase offset at output of charge pump 10 (default) | real positive scalar
  group: Target Metrics
- name: Target spur current (A)
  summary: Charge pump output current magnitude 1e-7 (default)
  group: Target Metrics
```

### Stimulus

### **Phase sweep (°)** — Maximum phase excursion from phase offset `300` (default) | real positive scalar

Maximum phase excursion from phase offset, specified as a real
positive scalar in degrees.

#### Programmatic Use

- Use `get_param(gcb,'PhaseSweep')` to
  view the current value of **Phase
  sweep**.
- Use `set_param(gcb,'PhaseSweep',value)`
  to set **Phase sweep** to a specific
  value.

**Data Types:** `double`

### **Phase offset (°)** — Relative phase value at center of phase sweep `0` (default) | real scalar

Relative phase value at the center of the phase sweep, specified as a
real scalar in degrees.

#### Programmatic Use

- Use `get_param(gcb,'PhaseOffset')` to
  view the current value of **Phase
  offset**.
- Use
  `set_param(gcb,'PhaseOffset',value)` to
  set **Phase offset** to a specific
  value.

**Data Types:** `double`

### **Clock frequency (Hz)** — Desired reference clock frequency `2.5e9 Hz` (default) | real positive scalar

Desired clock frequency for the reference counter output, specified as
a real positive scalar in Hz.

#### Programmatic Use

- Use `get_param(gcb,'ClockFrequency')`
  to view the current value of **Clock
  frequency**.
- Use
  `set_param(gcb,'ClockFrequency',value)`
  to set **Clock frequency** to a specific
  value.

**Data Types:** `double`

### **Number of phases in sweep** — Total number of evenly spaced phase offsets to simulate `2000` (default) | real positive scalar

The number of evenly spaced phase offsets in a sweep of phase offset,
specified as a real positive scalar.

#### Programmatic Use

- Use `get_param(gcb,'NPhases')` to view
  the current value of **Number of phases in
  sweep**.
- Use `set_param(gcb,'NPhases',value)` to
  set **Number of phases in sweep** to a
  specific value.

**Data Types:** `double`

### **Duty cycle (%)** — Duty cycle of stimulus clock `50` (default) | real positive scalar

Duty cycle for the stimulus clock at both reference and feedback
ports, specified as real positive scalar.

#### Programmatic Use

- Use `get_param(gcb,'DutyCycle')` to
  view the current value of **Duty
  cycle**.
- Use `set_param(gcb,'NPhases',value)` to
  set **Duty cycle** to a specific
  value.

**Data Types:** `double`

### Setup

### **Plot figures on top after simulation** — Plot figures on top after simulation on (default) | off

Select to plot the figures on the top of all other windows after
simulation. By default, this option is selected.

### **Report PFD metrics** — Report PFD metrics on (default) | off

Select to display the PFD metrics (Deadband, Linear Range, and Propagation delay)
on the icon of the PFD and Charge Pump Testbench. By
default, this option is selected.

**Data Types:** `double`

### **Report Charge Pump metrics** — Report Charge Pump metrics on (default) | off

Select to display the Charge Pump metrics (Sensitivity, Phase offset, and Spur
current) on the icon of the PFD and Charge Pump
Testbench. By default, this option is selected.

**Data Types:** `double`

### **Logic Threshold (V)** — Switching threshold at input of charge pump `0.5` (default) | real scalar

Switching threshold at the input of a charge pump, specified as a real
scalar in V. It is the voltage at which the timing of rising and falling
edges is measured.

#### Programmatic Use

- Use `get_param(gcb,'VSwitch')` to view
  the current value of **Logic
  Threshold**.
- Use `set_param(gcb,'VSwitch',value)` to
  set **Logic Threshold** to a specific
  value.

**Data Types:** `double`

### **Enable increased buffer size** — Enable increased buffer size off (default) | on

Select to enable increased buffer size during simulation. This
increases the buffer size of the Variable Pulse Delay and Logic Decision blocks inside the PFD and Charge Pump
Testbench. By default, this option is deselected.

### **Buffer size** — Number of samples of the input buffering available during simulation `5` (default) | positive integer scalar

Number of samples of the input buffering available during simulation,
specified as a positive integer scalar. This sets the Variable Pulse Delay and Logic Decision inside the PFD and Charge Pump
Testbench.

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

### Target Metrics

#### PFD Metrics

### **Target deadband (°)** — Maximum acceptable size of reduced sensitivity region near zero phase offset `0` (default) | real nonnegative scalar

Maximum acceptable size of reduced sensitivity region near zero phase
offset, specified as a real nonnegative scalar in degrees. It refers to
the size of the deadband region.

#### Programmatic Use

- Use `get_param(gcb,'TgtDeadband')` to
  view the current value of **Target
  deadband**.
- Use
  `set_param(gcb,'TgtDeadband',value)` to
  set **Target deadband** to a specific
  value.

**Data Types:** `double`

### **Target linear range (°)** — Maximum phase offset at which the output remains approximately equal to the input offset `290` (default) | real positive scalar

Maximum phase offset at which the output remains approximately equal
to the input offset, specified as a real positive scalar in
degrees.

#### Programmatic Use

- Use `get_param(gcb,'TgtRange')` to view
  the current value of **Target linear
  range**.
- Use `set_param(gcb,'TgtRange',value)`
  to set **Target linear range** to a
  specific value.

**Data Types:** `double`

### **Target propagation delay (s)** — Maximum acceptable delay from input to output `60e-12` (default) | real positive scalar

Maximum acceptable delay from the input to output, specified as a real
positive scalar in s.

#### Programmatic Use

- Use `get_param(gcb,'TgtPropDelay')` to
  view the current value of **Target propagation
  delay**.
- Use
  `set_param(gcb,'TgtPropDelay',value)` to
  set **Target propagation delay** to a
  specific value.

**Data Types:** `double`

### **Target rise/fall time (s)** — Maximum acceptable 20% – 80% rise/fall time `30e-12` (default) | real positive scalar

Maximum acceptable 20% – 80% rise/fall time, specified as a real
positive scalar in s.

#### Programmatic Use

- Use `get_param(gcb,'TgtRiseFall')` to
  view the current value of **Target rise/fall
  time**.
- Use
  `set_param(gcb,'TgtRiseFall',value)` to
  set **Target rise/fall time** to a specific
  value.

**Data Types:** `double`

#### Charge Pump Metrics

### **Target sensitivity (A/°)** — Maximum acceptable charge pump sensitivity `1e-9` (default) | real positive scalar

Maximum acceptable charge pump sensitivity, specified as a real
positive scalar in A/°.

#### Programmatic Use

- Use `get_param(gcb,'TgtSensitivity')`
  to view the current value of **Target
  sensitivity**.
- Use
  `set_param(gcb,'TgtSensitivity',value)`
  to set **Target sensitivity** to a specific
  value.

**Data Types:** `double`

### **Target phase offset (°)** — Maximum acceptable phase offset at output of charge pump `10` (default) | real positive scalar

Maximum acceptable phase offset at the output of a charge pump,
specified as a real positive scalar in degrees.

#### Programmatic Use

- Use `get_param(gcb,'TgtOffset')` to
  view the current value of **Target phase
  offset**.
- Use `set_param(gcb,'TgtOffset',value)`
  to set **Target phase offset** to a
  specific value.

**Data Types:** `double`

### **Target spur current (A)** — Charge pump output current magnitude `1e-7` (default)

Magnitude of the output current of the charge pump at the reference
frequency.

#### Programmatic Use

- Use `get_param(gcb,'TgtSpurCurrent')`
  to view the current value of **Target spur
  current**.
- Use
  `set_param(gcb,'TgtSpurCurrent',value)`
  to set **Target spur current** to a
  specific value.

**Data Types:** `double`
## Libraries

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Generic test environment for phase/frequency detectors and charge pumps

The PFD and Charge Pump Testbench block evaluates the behavioral model
of a PFD and charge pump. A single stimulus generator determines whether the PFD is
operating in the phase offset mode or frequency offset mode.

The PFD and Charge Pump Testbench block generates the stimulus to drive
the device under test (DUT) from the **Stimulus** tab. The setup
parameters for validating the DUT are defined in the **Setup** tab and
the target validation metrics are defined in the **Target Metrics**
tab.

The testbench measure PFD performance metrics such as deadband, linear rage, and
timing impairments. It also measures charge pump performance metrics such as
sensitivity, phase offset, and spur current.
