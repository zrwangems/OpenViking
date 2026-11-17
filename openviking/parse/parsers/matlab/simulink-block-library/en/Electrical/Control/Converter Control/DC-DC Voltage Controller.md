---
type: simulink-block
title: 'DC-DC Voltage Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Converter Control'
documentation_page: 'dcdcvoltagecontroller'
documentation_source_path: 'ref/dcdcvoltagecontroller.html'
language: en
---

# DC-DC Voltage Controller

## Ports
```yaml
ports:
- name: vRef
  summary: Reference DC voltage scalar
  direction: input
  data_types: single | double
- name: v
  summary: Measured DC voltage scalar
  direction: input
  data_types: single | double
- name: FF
  summary: Feedforward scalar
  direction: input
  data_types: single | double
- name: Reset
  summary: External reset scalar
  direction: input
  data_types: single | double
- name: Control
  summary: Control signal scalar
  direction: output
  data_types: single | double
```

### Input

### **vRef** — Reference DC voltage scalar

Desired DC output voltage for the plant.

**Data Types:** `single` | `double`

### **v** — Measured DC voltage scalar

Measured DC output voltage for the plant.

**Data Types:** `single` | `double`

### **FF** — Feedforward scalar

Feedforward term.

**Data Types:** `single` | `double`

### **Reset** — External reset scalar

External reset signal (rising edge) for the integrator.

**Data Types:** `single` | `double`
### Output

### **Control** — Control signal scalar

Control signal, *control*, expressed as a duty cycle or a
current.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Proportional gain
  summary: Proportional gain, *Kp* 0.1 (default) | positive scalar
  group: ''
- name: Integral gain
  summary: Integral gain, *Ki* 50 (default) | positive scalar
  group: ''
- name: Anti-windup gain
  summary: Anti-windup gain, *Kaw* 1 (default) | positive scalar
  group: ''
- name: Control action upper limit
  summary: Upper limit for the control signal, *controlmax* 1 (default) | positive scalar
  group: ''
- name: Control action lower limit
  summary: Lower limit for the control signal, *controlmin* 0 (default) | non-negative scalar
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | positive scalar
  group: ''
- name: Time constant voltage filter
  summary: DC voltage filter time constant, *τ* 0.001 (default) | positive scalar
  group: ''
- name: Filter DC voltage
  summary: DC voltage filter option on (default) | off
  group: ''
```

### **Proportional gain** — Proportional gain, *Kp* `0.1` (default) | positive scalar

Proportional gain, *Kp*, of the
controller.

### **Integral gain** — Integral gain, *Ki* `50` (default) | positive scalar

Integral gain, *Ki*, of the controller.

### **Anti-windup gain** — Anti-windup gain, *Kaw* `1` (default) | positive scalar

Anti-windup gain, *Kaw*, of the
controller.

### **Control action upper limit** — Upper limit for the control signal, *controlmax* `1` (default) | positive scalar

Upper limit for the **Control** output signal. The value must be
greater than the value of the **Control action lower limit**
parameter.

### **Control action lower limit** — Lower limit for the control signal, *controlmin* `0` (default) | non-negative scalar

Lower limit for the **Control** output signal.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

### **Time constant voltage filter** — DC voltage filter time constant, *τ* `0.001` (default) | positive scalar

Time constant, *τ*, for the DC voltage filter.

#### Dependencies

The **Time constant voltage filter** parameter is only visible
when the **Filter DC voltage** checkbox is selected.

### **Filter DC voltage** — DC voltage filter option on (default) | off

To enable the filter on voltage measurement path, select the checkbox. To disable the
filter, clear the check box.

#### Dependencies

The **Time constant voltage filter** parameter is only visible
when the **Filter DC voltage** check box is selected.
## Libraries

Simscape / Electrical / Control / General Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Discrete-time DC-DC voltage PI control with feedforward and optional integral anti-windup

The DC-DC Voltage Controller block implements discrete-time
proportional-integral (PI) DC-DC voltage control with feedforward,
*FF*. The feedforward input optimizes the transient response. The block
can output a duty cycle or a current control signal. To avoid saturation of the integral
gain, the block can implement anti-windup gain.

### Equations

The equation that the DC-DC Voltage Controller block uses to calculate the
control signal is

control=(Kp+KiTszz−1)(vref−v)+FF,

where:

- *control* is the control signal, expressed as a duty
  cycle or a current.
- *Kp* is the proportional
  gain.
- *Ki* is the integral
  gain.
- *Ts* is the sample
  time.
- *vref* is the reference
  voltage.
- *v* is the measured voltage.
- *FF* is the feedforward input.

To avoid saturation of the integrator output, the block uses an anti-windup
mechanism. The integrator gain is then equal to

Ki+Kaw(controlsat−controlunsat),

where:

- *Kaw* is the anti-windup
  gain.
- *controlsat* is the saturated
  control signal, which the block calculates as controlsat=min(max(controlunsat,controlmin),controlmax),

  where:

  - *controlunsat* is
    the unsaturated control signal.
  - *controlmin* is
    the lower limit for the control signal.
  - *controlmax* is
    the upper limit for the control signal.
