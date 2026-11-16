---
type: simulink-block
title: 'PFC Rectifier Controller (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Converter Control\u200b'
documentation_page: 'pfcrectifiercontrollerthreephase'
documentation_source_path: 'ref/pfcrectifiercontrollerthreephase.html'
language: en
---

# PFC Rectifier Controller (Three-Phase)

## Ports

### Input

### **VdcRef (V)** — Output DC-link voltage reference, V scalar

Output DC-link voltage reference, in volts.

**Data Types:** `single` | `double`

### **QRef (pu)** — Reactive power reference, pu scalar

Per-unit reactive power reference.

**Data Types:** `single` | `double`

### **VdcSens (V)** — DC-link voltage, V scalar

Measured DC-link voltage, in volts.

**Data Types:** `single` | `double`

### **VabcSens (pu)** — Measured AC phase voltage, pu vector

Per-unit measured AC phase voltage.

**Data Types:** `single` | `double`

### **IabcSens (pu)** — Measured AC phase current, pu vector

Per-unit measured AC phase current.

**Data Types:** `single` | `double`
### Output

### **VabcRef (pu)** — Reference voltage, pu vector

Per-unit reference voltage.

**Data Types:** `single` | `double`

### **Visualization** — Visualization bus bus

Bus containing internal signals for visualization. For a list of signals, see
Visualization.

**Data Types:** `single` | `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### General

### **System frequency (Hz)** — System frequency `60` (default) | positive scalar

System frequency, in hertz.

### **AC filter inductance (H)** — AC filter inductance `1e-4` (default) | positive scalar

AC filter inductance, in henry.

### **AC side base impedance (Ohm)** — AC-side base impedance `1.722` (default) | positive scalar

AC-side base impedance, in ohms.

### **PLL proportional gain** — Proportional gain `0.05` (default) | positive scalar

Proportional gain of the phase-locked loop.

### **PLL integral gain** — Integral gain `1` (default) | positive scalar

Integral gain of the phase-locked loop.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | nonnegative scalar or `-1`

Time, in seconds, between consecutive block executions. During execution, the
block produces outputs and, if appropriate, updates its internal state. For more
information, see What Is Sample Time? and Specify Sample Time.

For discrete-time simulation:

- To specify the sample time explicitly, set this parameter to a positive
  value. This value defines the sample time in seconds.
- To inherit the sample time, set this parameter to
  `-1`.

For continuous-time simulation, set this parameter to `0`.

For more information about continuous and discrete sample times, see Types of Sample Time.

### Voltage Controller

### **Proportional gain** — Proportional gain `0.4` (default) | positive scalar

Proportional gain of the voltage controller.

### **Integral gain** — Integral gain `3` (default) | positive scalar

Integral gain of the voltage controller.

### **Derivative gain** — Derivative gain `0` (default) | nonnegative scalar

Derivative gain of the voltage controller.

### **Derivative controller filter coefficient (N)** — Derivative controller filter coefficient `3` (default) | nonnegative scalar

Derivative voltage controller filter coefficient.

### **DC bus base voltage (V)** — DC bus base voltage `700` (default) | positive scalar

DC bus base voltage, in volts.

### **Controller output upper limit (pu)** — Controller output upper limit `1.5` (default) | nonnegative scalar

Upper limit on the per-unit output of the voltage controller.

### **Controller output lower limit (pu)** — Controller output lower limit `-1.5` (default) | nonpositive scalar

Lower limit on the per-unit output of the voltage controller.

### Current Controller

### **Id proportional gain** — Id proportional gain `10` (default) | positive scalar

Proportional gain of the *d*-axis current controller.

### **Id integral gain** — Id integral gain `350` (default) | positive scalar

Integral gain of the *d*-axis current controller.

### **Id derivative gain** — Id derivative gain `0` (default) | nonnegative scalar

Derivative gain of the *d*-axis current controller.

### **Id controller output upper limit (pu)** — Id controller output upper limit `1.2` (default) | nonnegative scalar

Upper limit on the per-unit output of the *d*-axis current
controller.

### **Id controller output lower limit (pu)** — Id controller output lower limit `-1.2` (default) | nonpositive scalar

Lower limit of the per-unit output of the *d*-axis current
controller.

### **Iq proportional gain** — Iq proportional gain `10` (default) | positive scalar

Proportional gain of the *q*-axis current controller.

### **Iq integral gain** — Iq integral gain `350` (default) | positive scalar

Integral gain of the *q*-axis current controller.

### **Iq derivative gain** — Iq derivative gain `0` (default) | nonnegative scalar

Derivative gain of the *q*-axis current controller.

### **Derivative current controller filter coefficient (N)** — Derivative current controller filter coefficient `100` (default) | nonnegative scalar

Derivative current controller filter coefficient.

### **Iq controller output upper limit (pu)** — Iq controller output upper limit `1.2` (default) | nonnegative scalar

Upper limit on the per-unit output of the *q*-axis current
controller.

### **Iq controller output lower limit (pu)** — Iq controller output lower limit `-1.2` (default) | nonpositive scalar

Lower limit on the per-unit output of the *q*-axis current
controller.

## Libraries

Simscape / Electrical / Control / Converter Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

PID-based power factor correction (PFC) rectifier controller

The PFC Rectifier Controller (Three-Phase) block implements a
proportional-integral-derivative (PID)-based power factor correction (PFC) rectifier
controller. This block converts a three-phase AC supply into the required stable DC-link
voltage and controls the reactive power drawn from the supply. To reduce harmonics, the block
draws sinusoidal current. The block has an inbuilt phase-locked-loop (PLL) that tracks the
angle and magnitude of the supply voltage.

For discrete-time simulation, set **Sample time (-1 for inherited)** to a
positive value or to `-1` to inherit the sample time. For continuous-time
simulation, set **Sample time (-1 for inherited)** to
`0`.

This figure shows the circuit configuration of the PFC rectifier.

- *V*S is the supply voltage.
- *I*S is the supply-side current.
- *X*L is the inductive reactance.
- *V*i is the inverter-side AC phase
  voltage.
- *V*dc is the DC-link voltage.

This equation defines the supply voltage
*V*S,

VS(t)=ISRL+LdiS(t)dt+Vi(t),

where:

- *R*L is the resistance of the filter
  inductor.
- *L* is the filter inductance.
- *i*s is the inverter-side AC phase
  current.

### Controller Structure

This diagram shows the structure of the controller.

The inputs to the block are:

- The output DC-link voltage reference *VdcRef*, measured in
  volts.
- The per-unit reactive power reference *QRef*.
- The measured DC-link voltage *VdcSens*, in volts.
- The per-unit measured AC phase voltage *VabcSens*.
- The per-unit measured AC phase current *IabcSens*.

The outputs are the per-unit reference voltage *VabcRef* and
a bus containing signals for visualization.

The DC voltage controller calculates:

- The per-unit *d*-axis reference current
  *IdRef*.
- The per-unit error of the DC voltage controller
  *VdcCntrlError*.

The PLL calculates:

- The phase angle *pllAngle*, in radians, of the measured AC phase
  voltage.
- The per-unit magnitude *pllVmag* of the measured AC phase
  voltage.
- The per-unit *d*-axis component of the measured AC phase
  voltage *Vd*.
- The per-unit *q*-axis component of the measured AC phase
  voltage *Vq*.

The reactive power reference calculates the per-unit *q*-axis
reference current *IqRef*.

The current controller calculates:

- The per-unit reference voltage *VabcRef*.
- The per-unit error of the *d*-axis current controller
  *IdCntrlError*.
- The per-unit error of the *q*-axis current controller
  *IqCntrlError*.

### Visualization

The block outputs a bus containing these seven signals for visualization:

- The phase angle *pllAngle*, in radians, of the measured AC phase
  voltage.
- The per-unit voltage magnitude *pllVmag* of the measured AC phase
  voltage.
- The per-unit *d*-axis reference current
  *IdRef*.
- The per-unit *q*-axis reference current
  *IqRef*.
- The per-unit error of the DC voltage controller
  *VdcCntrlError*.
- The per-unit error of the *d*-axis current controller
  *IdCntrlError*.
- The per-unit error of the *q*-axis current controller
  *IqCntrlError*.
