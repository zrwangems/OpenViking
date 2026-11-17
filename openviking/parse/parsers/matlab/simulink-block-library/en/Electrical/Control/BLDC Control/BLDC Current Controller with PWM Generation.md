---
type: simulink-block
title: 'BLDC Current Controller with PWM Generation'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / BLDC Control'
documentation_page: 'bldccurrentcontrollerwithpwmgeneration'
documentation_source_path: 'ref/bldccurrentcontrollerwithpwmgeneration.html'
language: en
---

# BLDC Current Controller with PWM Generation

## Ports
```yaml
ports:
- name: IsRef
  summary: Reference current scalar
  direction: input
  data_types: single | double
- name: Is
  summary: Measured current scalar
  direction: input
  data_types: single | double
- name: Reset
  summary: External reset scalar
  direction: input
  data_types: single | double
- name: Hall
  summary: Hall sensor vector
  direction: input
  data_types: single | double
- name: Direction
  summary: Motor direction scalar
  direction: input
  data_types: single | double
- name: G
  summary: Gate pulses vector
  direction: output
  data_types: single | double
```

### Input

### **IsRef** — Reference current scalar

Reference current for control.

**Data Types:** `single` | `double`

### **Is** — Measured current scalar

Actual current.

**Data Types:** `single` | `double`

### **Reset** — External reset scalar

External reset signal (rising edge) for the integrator.

**Data Types:** `single` | `double`

### **Hall** — Hall sensor vector

Hall sensor data.

**Data Types:** `single` | `double`

### **Direction** — Motor direction scalar

Direction of motor rotation.

**Data Types:** `single` | `double`
### Output

### **G** — Gate pulses vector

Pulse waveforms that determine switching behavior in the attached
block.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Proportional gain
  summary: Controller proportional gain, *Kp* 1 (default) | positive scalar
  group: Control Parameters
- name: Integral gain
  summary: Integral gain, *Ki* 5 (default) | positive scalar
  group: Control Parameters
- name: Anti-windup gain
  summary: Anti-windup gain, *Kaw* 1 (default) | positive scalar
  group: Control Parameters
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | positive scalar
  group: Control Parameters
- name: Discretization sample time
  summary: Sample time for discretization 0.001 (default) | positive scalar
  group: Control Parameters
- name: Enable zero cancellation
  summary: Feedforward zero cancellation off (default) | on
  group: Control Parameters
- name: Carrier counter
  summary: Carrier counter model Up (default) | Down | Up-Down
  group: PWM Generator
- name: Timer period (s)
  summary: PWM timer period 0.001 (default) | positive scalar
  group: PWM Generator
- name: Fundamental sample time (s)
  summary: Sample time for PWM generation 0.0001 (default) | positive scalar
  group: PWM Generator
```

### Control Parameters

### **Proportional gain** — Controller proportional gain, *Kp* `1` (default) | positive scalar

Proportional gain, *Kp*, of the
controller.

### **Integral gain** — Integral gain, *Ki* `5` (default) | positive scalar

Integral gain, *Ki*, of the controller.

### **Anti-windup gain** — Anti-windup gain, *Kaw* `1` (default) | positive scalar

Anti-windup gain, *Kaw*, of the
controller.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

#### Dependencies

If you set **Sample time (-1 for inherited)** to
`-1` and select the **Enable zero
cancellation** option, the **Discretization sample
time** parameter becomes visible.

### **Discretization sample time** — Sample time for discretization `0.001` (default) | positive scalar

Time, in s, between consecutive discretizations. Discretization is required for zero
cancellation.

#### Dependencies

This parameter is only visible when both these conditions are met:

- **Sample time** is set to
  `-1`.
- **Enable zero cancellation** is selected.

### **Enable zero cancellation** — Feedforward zero cancellation off (default) | on

Option to use zero cancellation on the feedforward path.

#### Dependencies

If you select the **Enable zero cancellation** option and set
**Sample time (-1 for inherited)** to `-1`,
the **Discretization sample time** parameter becomes
visible.

### PWM Generator

### **Carrier counter** — Carrier counter model `Up` (default) | `Down` | `Up-Down`

Use the carrier counter strategy to change the initial behavior of the PWM output:

- Up counter — PWM output begins at the start of the on state.
- Down counter — PWM output begins at the start of the off state.
- Up-down counter — PWM output begins in the middle of the on state.

### **Timer period (s)** — PWM timer period `0.001` (default) | positive scalar

Pulse width modulation timer period, *Tper*,
in seconds.

### **Fundamental sample time (s)** — Sample time for PWM generation `0.0001` (default) | positive scalar

Time, in s, between
consecutive PWM generator executions. During execution, the block produces PWM output
and, if appropriate, updates its internal state. For more information, see What Is Sample Time? and Specify Sample Time.

To ensure adequate resolution in the generated PWM signal,
set the fundamental sample time so that 0<Ts\_pwm≤10Tper, where:

- *Ts\_pwm* is the
  **Fundamental sample time (s)**.
- *Tper* is the **Timer
  period (s)**.
## Libraries

Simscape / Electrical / Control / BLDC Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Discrete-time brushless DC Motor current PI controller with pulse width modulation generation

The BLDC Current Controller with PWM Generation block generates a pulse width
modulation (PWM) signal and controls current in a brushless DC motor. The controller
uses this algorithm.

### Equations

The BLDC Current Controller with PWM Generation produces the duty cycle for
a BLDC block by implementing
proportional-integral (PI) current control using this equation

D=(Kp+KiTszz−1)(Is\_ref−Is)

where:

- *D* is the duty cycle.
- *Kp* is the proportional
  gain.
- *Ki* is the integral
  gain.
- *Ts* is the time
  period.
- *Is\_ref* is the reference
  current.
- *Is* is the measured
  current.
- *Gzc* is the zero cancellation
  polynomial.

The closed-loop transfer function for the PI control algorithm yields a zero that can be
cancelled by using zero-cancellation block in the feedforward path. The
zero-cancellation transfer function in discrete-time is:

GZC(z)=TsKiKpz+(Ts−KpKiKpKi).

The block obtains control signals for the three phases by multiplying the duty cycle by the
commutation signals. The resulting three control signals are normalized over the
interval [-1, 1].

The PWM generator outputs a 1 when the value of the control signal is greater than
the carrier counter value. Otherwise, the PWM generator outputs a 0.
