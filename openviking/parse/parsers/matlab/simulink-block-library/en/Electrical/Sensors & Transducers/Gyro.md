---
type: simulink-block
title: 'Gyro'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'gyro'
documentation_source_path: 'ref/gyro.html'
language: en
---

# Gyro

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

Mechanical conserving port associated with the gyro translational
port.

### **+** — Positive port electrical

Electrical conserving port associated with the gyro positive
terminal.

### **-** — Negative port electrical

Electrical conserving port associated with the gyro negative
terminal.
## Parameters
```yaml
parameters:
- name: Sensitivity
  summary: Sensitivity 12.5 s*mV/deg (default)
  group: ''
- name: Output voltage for zero rotation
  summary: Output voltage for zero rotation 2.5 V (default)
  group: ''
- name: Maximum output voltage
  summary: Maximum output voltage 4 V (default)
  group: ''
- name: Minimum output voltage
  summary: Minimum output voltage 1 V (default)
  group: ''
- name: Dynamics
  summary: Dynamics modeling option No dynamics — Suitable for HIL (default) | Model sensor bandwidth
  group: ''
- name: Bandwidth
  summary: Bandwidth 3 kHz (default)
  group: ''
```

### **Sensitivity** — Sensitivity `12.5` `s*mV/deg` (default)

The change in output voltage level per unit change in rotation rate when
the output is not being limited.

### **Output voltage for zero rotation** — Output voltage for zero rotation `2.5` `V` (default)

The output voltage from the sensor when the rotation rate is zero.

### **Maximum output voltage** — Maximum output voltage `4` `V` (default)

The maximum output voltage from the sensor, which determines the sensor
maximum measured rotational rate.

### **Minimum output voltage** — Minimum output voltage `1` `V` (default)

The minimum output voltage from the sensor, which determines the sensor
minimum measured rotational rate.

### **Dynamics** — Dynamics modeling option `No dynamics — Suitable for HIL` (default) | `Model sensor bandwidth`

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
  **Measured angular rate** variable target.

### **Bandwidth** — Bandwidth `3` `kHz` (default)

Specifies the 3dB bandwidth for the measured rotational rate assuming a
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

Behavioral model of MEMS gyro

The Gyro block implements a behavioral model of a
MicroElectroMechanical Systems (MEMS) gyro. The gyro provides an output voltage that is
proportional to the angular rotation rate presented at the mechanical rotational
physical port R. The output voltage is limited according to the values that you provide
for maximum and minimum output voltage.

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

The **Measured angular rate** variable target specifies the
initial output for the sensor.
