---
type: simulink-block
title: 'Start-Stop Generator'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Signal Generation'
documentation_page: 'startstopgenerator'
documentation_source_path: 'ug/startstopgenerator.html'
language: en
---

# Start-Stop Generator

## Ports
```yaml
ports:
- name: enable
  summary: Enable and disable start-stop signal generation scalar
  direction: input
  data_types: single | double
- name: start times
  summary: Start times scalar | vector
  direction: input
  data_types: single | double
- name: y
  summary: Steady-state value scalar | vector
  direction: input
  data_types: single | double
- name: start/stop
  summary: Start-stop signal scalar
  direction: output
  data_types: single | double
```

### Input

### **enable** — Enable and disable start-stop signal generation scalar

Specify a signal to enable (`1`) or disable
(`0`) the block action.

**Data Types:** `single` | `double`

### **start times** — Start times scalar | vector

Specify the start times for the signals as a scalar or vector.

The block generates a signal that goes from 0 to 1 at the specified start times
for a duration specified using the **Duration (sec)** parameter.
After the duration has passed, the signal goes from 1 to 0.

**Data Types:** `single` | `double`

### **y** — Steady-state value scalar | vector

Connect the output of your plant to this port. The block determines the current
operating state of the system and generates the start-stop signal using this
signal.

**Data Types:** `single` | `double`
### Output

### **start/stop** — Start-stop signal scalar

Start-stop signal. The value of the signal changes from:

- Negative or zero to positive at the values specified using **start
  times** or at steady-state times determined using
  **Steady-state settings**.
- Positive to negative or zero after the duration specified in
  **Duration (sec)** has passed.

Typically, you use this signal to start and stop frequency response estimation,
signal generation, or autotuning processes. When the **enable** port
is set to 0, the block does not generate a start-stop signal.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Sample time (Ts)
  summary: Sample time 0.1 (default) | positive scalar
  group: ''
- name: Data Type
  summary: Floating point precision double (default) | single
  group: ''
- name: Source of start time points
  summary: Source of start time points External time vector (default) | Time after reaching steady-state
  group: ''
- name: Duration (sec)
  summary: Start-stop signal duration 10 (default) | scalar
  group: ''
- name: Number of samples after reaching steady-state to generate start-stop signal
  summary: Delay for starting signal generation 2 (default) | nonnegative integer
  group: ''
- name: Settling time upper bounds
  summary: Upper bound for settling time [1.1 2.1 3.1] (default) | vector
  group: ''
- name: Settling time lower bounds
  summary: Lower bound for settling time [0.9 1.9 2.9] (default) | vector
  group: ''
- name: Settling time interval
  summary: Settling time interval 5 (default) | scalar | vector
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Sample time (Ts)** — Sample time `0.1` (default) | positive scalar

Specify the sample time of the generated start-stop signal.

### **Data Type** — Floating point precision `double` (default) | `single`

Specify the floating-point precision based on simulation environment or hardware
requirements.

### **Source of start time points** — Source of start time points `External time vector` (default) | `Time after reaching steady-state`

Specify the source of start time points as one of the following:

- `External time vector` — Use the **start
  times** output port to specify explicit values of start times.
- `Time after reaching steady-state` — Use the plant
  output signal **y** and **Steady-state settings**
  to determine the times to start generating the start-stop signal.

### **Duration (sec)** — Start-stop signal duration `10` (default) | scalar

Specify the duration of the start stop signal.

### **Number of samples after reaching steady-state to generate start-stop signal** — Delay for starting signal generation `2` (default) | nonnegative integer

Specify the number of samples after reaching steady-state for which the block delays
generating a start-stop signal.

### **Settling time upper bounds** — Upper bound for settling time `[1.1 2.1 3.1]` (default) | vector

Specify the upper bound for the operating value used to determine settling time and
steady state of the operating point.

Each value of this vector corresponds to the upper bound for the operating point
value at that index.

### **Settling time lower bounds** — Lower bound for settling time `[0.9 1.9 2.9]` (default) | vector

Specify the lower bound for the operating value used to determine settling time and
steady state of the operating point.

Each value of this vector corresponds to the lower bound for the operating point
value at that index.

### **Settling time interval** — Settling time interval `5` (default) | scalar | vector

Specify the time interval for which the operating condition remains in steady
state.

Use a vector to specify different time intervals for different operating
points.
## Libraries

Simulink Control Design / Signal Generation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Generate start-stop signal used by signal generation, estimation, and autotuning blocks

Use this block to generate a signal for the **start/stop**
input port of signal generation, frequency response estimation, and PID autotuning blocks in
Simulink®
Control Design™ library. This port determines when to start and stop generating the perturbation
signal in these blocks. The Start-Stop Generator block generates a signal that
changes from 0 to 1 at the specified time values to enable the blocks, and from 1 to 0 to
disable after the specified duration has passed.

This block is helpful when you to generate start-stop signal to enable estimation or
autotuning process at different operating conditions.
