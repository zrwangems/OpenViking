---
type: simulink-block
title: 'Accelerometer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'accelerometer'
documentation_source_path: 'ref/accelerometer.html'
language: en
---

# Accelerometer

## Ports
```yaml
ports:
- name: R
  summary: Translational port mechanical
  direction: conserving
- name: +
  summary: Positive port electrical
  direction: conserving
- name: '-'
  summary: Negative port electrical
  direction: conserving
```

### Conserving

### **R** — Translational port mechanical

Mechanical conserving port associated with the accelerometer
translational port.

### **+** — Positive port electrical

Electrical conserving port associated with the accelerometer positive
terminal.

### **-** — Negative port electrical

Electrical conserving port associated with the accelerometer negative
terminal.
## Parameters
```yaml
parameters:
- name: Output type
  summary: Block output type Voltage level (default) | PWM duty cycle
  group: ''
- name: Sensitivity
  summary: Sensitivity 1000 mV/gee (default)
  group: ''
- name: Output voltage for zero acceleration
  summary: Output voltage for zero acceleration 2.5 V (default)
  group: ''
- name: Maximum output voltage
  summary: Maximum output voltage 4 V (default)
  group: ''
- name: Minimum output voltage
  summary: Minimum output voltage 1 V (default)
  group: ''
- name: Duty cycle sensitivity (percent per unit acceleration)
  summary: Duty cycle sensitivity 10 1/gee (default)
  group: ''
- name: Duty cycle for zero acceleration (percent)
  summary: Duty cycle for zero acceleration 50 (default)
  group: ''
- name: Maximum duty cycle (percent)
  summary: Maximum duty cycle 75 (default)
  group: ''
- name: Minimum duty cycle (percent)
  summary: Minimum duty cycle 25 (default)
  group: ''
- name: PWM frequency
  summary: PWM frequency 1000 Hz (default)
  group: ''
- name: Output voltage amplitude
  summary: Output voltage amplitude 5 V (default)
  group: ''
- name: Dynamics
  summary: Dynamics No dynamics — Suitable for HIL (default) | Model sensor bandwidth
  group: ''
- name: Bandwidth
  summary: Bandwidth 3 kHz (default)
  group: ''
```

### **Output type** — Block output type `Voltage level` (default) | `PWM duty cycle`

Select one of the following options to define the block output type:

- `Voltage level` — The
  amplitude of the output voltage is proportional to the measured
  acceleration. This is the default option.
- `PWM duty cycle` — The duty
  cycle (on time divided by the pulse total time) is proportional
  to the measured acceleration.

### **Sensitivity** — Sensitivity `1000` `mV/gee` (default)

Change in output voltage level per unit change in acceleration when the
output is not being limited.

#### Dependencies

This parameter is visible only when you select `Voltage
level` for the **Output type**
parameter.

### **Output voltage for zero acceleration** — Output voltage for zero acceleration `2.5` `V` (default)

The output voltage from the sensor when the acceleration is zero.

#### Dependencies

This parameter is visible only when you select `Voltage
level` for the **Output type**
parameter.

### **Maximum output voltage** — Maximum output voltage `4` `V` (default)

The maximum output voltage from the sensor, which determines the sensor
maximum measured positive acceleration.

#### Dependencies

This parameter is visible only when you select `Voltage
level` for the **Output type**
parameter.

### **Minimum output voltage** — Minimum output voltage `1` `V` (default)

The minimum output voltage from the sensor, which determines the sensor
maximum measured negative acceleration. This parameter is only visible when
you select `Voltage level` for the **Output
type** parameter. The default value is `1`
V.

### **Duty cycle sensitivity (percent per unit acceleration)** — Duty cycle sensitivity `10` `1/gee` (default)

The change in duty cycle per unit acceleration. Duty cycle is expressed as
a percentage of the PWM period.

#### Dependencies

This parameter is visible only when you select `PWM duty
cycle` for the **Output type**
parameter.

### **Duty cycle for zero acceleration (percent)** — Duty cycle for zero acceleration `50` (default)

The duty cycle output by the sensor when the acceleration is zero.

#### Dependencies

This parameter is visible only when you select `PWM duty
cycle` for the **Output type**
parameter.

### **Maximum duty cycle (percent)** — Maximum duty cycle `75` (default)

The maximum duty cycle output by the sensor. Increasing acceleration
levels beyond this point will not register an increase in duty cycle.

#### Dependencies

This parameter is visible only when you select `PWM duty
cycle` for the **Output type**
parameter.

### **Minimum duty cycle (percent)** — Minimum duty cycle `25` (default)

The minimum duty cycle output by the sensor. Decreasing acceleration
levels beyond this point will not register a decrease in duty cycle.

#### Dependencies

This parameter is visible only when you select `PWM duty
cycle` for the **Output type**
parameter.

### **PWM frequency** — PWM frequency `1000` `Hz` (default)

The frequency of the output pulse train.

#### Dependencies

This parameter is visible only when you select `PWM duty
cycle` for the **Output type**
parameter.

### **Output voltage amplitude** — Output voltage amplitude `5` `V` (default)

The amplitude of the output pulse train when high.

#### Dependencies

This parameter is visible only when you select `PWM duty
cycle` for the **Output type**
parameter.

### **Dynamics** — Dynamics `No dynamics — Suitable for HIL` (default) | `Model sensor bandwidth`

Select one of the following options for modeling sensor dynamics:

- `No dynamics — Suitable for
  HIL` — Do not model sensor dynamics. Use
  this option when running your simulation fixed step or
  generating code for hardware-in-the-loop testing, because this
  avoids the need for a small simulation time step if the sensor
  bandwidth is high. This is the default option.
- `Model sensor bandwidth` —
  Model sensor dynamics with a first-order lag approximation,
  based on the **Bandwidth** parameter value. You
  can control the initial condition for the lag by specifying the
  **Measured acceleration** variable
  target.

### **Bandwidth** — Bandwidth `3` `kHz` (default)

Specifies the 3dB bandwidth for the measured acceleration assuming a
first-order time constant.

#### Dependencies

This parameter is visible only when you select `Model
sensor bandwidth` for the **Dynamics**
parameter.
## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

## Description

Behavioral model of MEMS accelerometer

The Accelerometer block implements a behavioral model
of a MicroElectroMechanical Systems (MEMS) accelerometer. For the default output type
`Voltage level`, the accelerometer provides an output
voltage that is proportional to the acceleration rate presented at the mechanical
translational physical port R. The output voltage is limited according to the values
that you provide for maximum and minimum output voltage.

The block also has an alternative output type, `PWM duty
cycle`. With this choice, the output of the block is a PWM signal with
a duty cycle that is proportional to the measured acceleration. You can limit the
variation in duty cycle to a specified range.

Optionally, you can model sensor dynamics by setting the **Dynamics**
parameter to `Model sensor bandwidth`. Including dynamics adds
a first-order lag between the angular rate presented at port R and the corresponding
voltage applied to the electrical + and - ports.

If running your simulation with a fixed-step solver, or generating code for
hardware-in-the-loop testing, MathWorks recommends that you set the
**Dynamics** parameter to `No dynamics —
Suitable for HIL`, because this avoids the need for a small simulation
time step if the sensor bandwidth is high.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

The **Measured acceleration** variable target specifies the
initial output for the sensor.
