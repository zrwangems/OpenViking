---
type: simulink-block
title: 'Induction Machine Field-Oriented Control'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinefieldorientedcontrol'
documentation_source_path: 'ref/inductionmachinefieldorientedcontrol.html'
language: en
---

# Induction Machine Field-Oriented Control

## Ports

### Input

### **imRef** — Current scalar

Magnetizing reference current in the per-unit system.

**Data Types:** `single` | `double`

### **wrRef** — Velocity scalar

Rotor reference velocity in per-unit system.

**Data Types:** `single` | `double`

### **iabc** — Current vector

Measured phase currents in the per-unit system.

**Data Types:** `single` | `double`

### **wr** — Velocity scalar

Measured angular velocity in per-unit system.

**Data Types:** `single` | `double`

### **Vdc** — Voltage scalar

Measured dc-link voltage, in V.

**Data Types:** `single` | `double`
### Output

### **G** — Gate pulses vector | `0` or `1`

Inverter gate pulses. The block does not consider any dead
time.

**Data Types:** `single` | `double`

### **Visualization** — Visualization signals vector

Bus containing signals for visualization.

**Data Types:** `single` | `double` | `bus`

## Parameters

### General

### **Rated voltage, rms line-to-line (V)** — Voltage `550` (default)

Nominal voltage.

### **Rated electrical frequency (Hz)** — Frequency `60` (default)

Nominal electrical frequency.

### **Rotor resistance, referred to the stator side (pu)** — Resistance `0.01` (default)

Rotor, stator-side resistance in the per-unit system.

### **Rotor leakage inductance, referred to the stator side (pu)** — Inductance `0.06` (default)

Rotor stator-side leakage inductance, in the pu-unit system.

### **Magnetizing inductance (pu)** — Inductance `2.7` (default)

Magnetizing inductance in the per-unit system.

### **Time constant for dq currents filters (s)** — Time constant `1e-4` (default)

Time constant for filtering the *d* and
*q* currents.

### **Inverter dc-link voltage threshold (V)** — Voltage `500` (default)

Voltage threshold to activate the power inverter.

### **Fundamental sample time (s)** — Time `5e-6` (default) | positive scalar less than the control sample time

Fundamental sample time must be less than
the control sample time.

### **Control sample time (s)** — Time `5e-5` (default) | positive scalar greater than the fundamental sample time

Control sample time must be greater than
the fundamental sample time.

### Outer Loop

### **Magnetizing current controller proportional gain** — Gain `10` (default)

Proportional gain for the magnetizing current controller.

### **Magnetizing current controller integral gain** — Gain `1000` (default)

Integral gain for the magnetizing current controller.

### **Magnetizing current controller integral anti-windup gain** — Gain `1000` (default)

Integral anti-windup gain for the magnetizing current
controller.

### **Speed controller proportional gain** — Gain `10` (default)

Proportional gain for the speed controller.

### **Speed controller integral gain** — Gain `1000` (default)

Integral gain for the speed controller.

### **Speed controller integral anti-windup gain** — Gain `1000` (default)

Integral anti-windup gain for the speed controller.

### **Maximum d-axis current [pu]** — Current `2` (default)

Maximum current for the *d*-axis.

### **Maximum q-axis current [pu]** — Current `2` (default)

Maximum current for the *q*-axis.

#### Inner Loop

### **Phase-a axis alignment** — *dq0* reference frame alignment `Q-axis` (default) | `D-axis`

Align the *a*-phase vector of the
*abc* reference frame to the *d*-
or *q*-axis of the rotating reference frame.

### **D-axis current proportional gain** — *D*-axis proportional gain `1` (default) | positive number

Proportional gain of the PI controller used for direct-axis current
control.

### **D-axis current integral gain** — *D*-axis integral gain `100` (default) | positive number

Integrator gain of the PI controller used for direct-axis current
control.

### **D-axis current anti-windup gain** — *D*-axis anti-windup gain `1` (default) | positive number

Anti-windup gain of the PI controller used for direct-axis current
control.

### **Q-axis current proportional gain** — *Q*-axis proportional gain `1` (default) | positive number

Proportional gain of the PI controller used for quadrature-axis
current control.

### **Q-axis current integral gain** — *Q*-axis integral gain `100` (default) | positive number

Integrator gain of the PI controller used for quadrature-axis current
control.

### **Q-axis current anti-windup gain** — *Q*-axis anti-windup gain `1` (default) | positive number

Anti-windup gain of the PI controller used for quadrature-axis current
control.

### **Axis prioritization** — Axis prioritization for voltage limiter `Q-axis` (default) | `D-axis` | `D-Q equivalence`

Prioritize or maintain ratio between *d*- and
*q*-axes when block limits voltage.

#### PWM

### **PWM method** — Pulse width modulation method `SVM: space vector modulation` (default) | `SPWM: sinusoidal PWM`

Specify the waveform technique.

### **Sampling mode** — Wave-sampling method `Natural` (default) | `Asymmetric` | `Symmetric`

The sampling mode determines whether the block samples the modulation
waveform when the waves intersect or when the carrier wave is at one or
both of its boundary conditions.

### **Switching frequency (Hz)** — Switching rate `1000` (default) | positive integer

Specify the rate at which you want the switches in the power converter
to switch.

## Libraries

Simscape / Electrical / Control / Induction Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Per-unit discrete-time induction machine FOC

The Induction Machine Field-Oriented Controller block implements an
induction machine field-oriented control (FOC) structure using the per-unit system. To
decouple the torque and flux, FOC uses the rotor
*d*-*q* reference frame. The figure shows the
control structure.

In the diagram:

- *ωr* is the measured
  angular velocity.
- *ωref* is the reference
  angular velocity.
- *id* and
  *iq* are the
  *d*- and *q*-axis stator
  currents.
- *ia*,
  *ib*, and
  *ic* are the
  *a*-, *b*- and
  *c*-phase stator winding currents.
- *imr\_ref* is the reference
  magnetizing current.
- *imr* is the magnetizing
  current.
- *vd* and
  *vq* are the
  *d*- and *q*-axis stator
  voltages.
- *va*,
  *vb*, and
  *vc* are the
  *a*-, *b*- and
  *c*-phase stator winding voltages.
- *θe* is the rotor
  electrical angle.
- *GAH*,
  *GAL*,
  *GBH*,
  *GBL*,
  *GCH*, and
  *GCL* are the
  *a*-, *b*- and
  *c*-phase high (H) and low(L) gate
  pulses.

### Assumptions and Limitations

- The machine parameters are known.
- The implementation uses the per-unit system.
- The control structure implementation uses a single sample rate.
