---
type: simulink-block
title: 'Solar PV Controller (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Renewables Control'
documentation_page: 'solarpvcontrollerthreephase'
documentation_source_path: 'ref/solarpvcontrollerthreephase.html'
language: en
---

# Solar PV Controller (Three-Phase)

## Ports

### Input

### **Qref (pu)** — Reactive power reference, pu scalar

Per-unit reactive power reference.

**Data Types:** `single` | `double`

### **ipv (A)** — DC-side current, A scalar

DC-side current, in amps.

**Data Types:** `single` | `double`

### **vdc (V)** — DC-side voltage, V scalar

DC-side voltage, in volts.

**Data Types:** `single` | `double`

### **vabc (pu)** — AC-side voltage, pu vector

AC-side per-unit voltage.

**Data Types:** `single` | `double`

### **iabc (pu)** — AC-side current, pu vector

AC-side per-unit current.

**Data Types:** `single` | `double`
### Output

### **vabcRef (pu)** — Per-unit reference voltage wave, pu vector

Per-unit reference voltage wave.

**Data Types:** `single` | `double`

### **visualization** — Visualization bus bus

Bus containing internal signals for visualization. For a list of signals, see
Visualization.

**Data Types:** `single` | `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### General

### **AC filter inductance (H)** — AC filter inductance `3e-3` (default) | positive scalar

AC filter inductance, in henries.

### **System frequency (Hz)** — System frequency `60` (default) | positive scalar

System frequency, in hertz.

### **Inverter current limit (pu)** — Inverter current limit `1.2` (default) | positive scalar

The per-unit inverter current limit.

### **Base impedance on AC side (Ohm)** — AC-side base impedance `0.34` (default) | positive scalar

AC-side base impedance, in ohms.

### **Base power on AC side (V\*A)** — AC-side base power `6e5` (default) | scalar

AC-side base power in volt-amperes.

### **DC bus base voltage (V)** — DC bus base voltage `1000` (default) | positive scalar

DC bus base voltage, in volts.

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

### MPPT

### **Algorithm** — MPPT algorithm `Perturb and observe (P&O)` (default) | `Incremental conductance (INC)`

Maximum power point tracking algorithm. Choose one of these options:

- `Perturb and observe (P&O)` — The P&O
  algorithm perturbs the operating voltage of the solar panel. The algorithm then
  observes the change in power output. If the power increases, the perturbation
  continues in the same direction. If the power decreases, the algorithm reverses
  the perturbation. To prioritize simulation speed, use this option.
- `Incremental conductance (INC)` — The INC algorithm
  calculates the incremental change in current and voltage to determine the slope
  of the power-voltage curve. If the slope is close to zero, the MPP is reached.
  If the slope is positive, the operating point moves to a higher voltage. If the
  slope is negative, the operating point moves to a lower voltage. To prioritize
  accuracy in tracking the MPP, use this option.

### **Initial voltage for MPPT (V)** — Initial voltage for MPPT `2000` (default) | scalar

Initial voltage for the MPPT algorithm, in volts.

### **Voltage step of MPPT (V)** — Voltage step of MPPT `3` (default) | nonnegative scalar

Voltage step of the MPPT algorithm, in volts.

### **Settling time of MPPT (s)** — Settling time of MPPT `5e-4` (default) | nonnegative scalar

Settling time of the MPPT algorithm, in seconds.

### PLL

### **Proportional gain** — Proportional gain `200` (default) | positive scalar

Proportional gain of the phase-locked loop.

### **Integral gain** — Integral gain `2000` (default) | positive scalar

Integral gain of the phase-locked loop.

### **Initial phase angle (deg)** — Initial phase angle `0` (default) | scalar

Initial phase angle for the phase-locked loop, in degrees.

### Voltage Controller

### **Proportional gain** — Proportional gain `0.4` (default) | positive scalar

Proportional gain of the voltage controller.

### **Integral gain** — Integral gain `3` (default) | positive scalar

Integral gain of the voltage controller.

### **Derivative gain** — Derivative gain `0` (default) | nonnegative scalar

Derivative gain of the voltage controller.

### Current Controller

### **D-axis proportional gain** — D-axis proportional gain `1` (default) | positive scalar

Proportional gain of the *D*-axis current controller.

### **D-axis integral gain** — D-axis integral gain `250` (default) | positive scalar

Integral gain of the *D*-axis current controller.

### **D-axis derivative gain** — D-axis derivative gain `0` (default) | nonnegative scalar

Derivative gain of the *D*-axis current controller.

### **Q-axis proportional gain** — Q-axis proportional gain `1` (default) | positive scalar

Proportional gain of the *Q*-axis current controller.

### **Q-axis integral gain** — Q-axis integral gain `250` (default) | positive scalar

Integral gain of the *Q*-axis current controller.

### **Q-axis derivative gain** — Q-axis derivative gain `0` (default) | nonnegative scalar

Derivative gain of the *Q*-axis current controller.

## Libraries

Simscape / Electrical / Control / Renewables Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Solar photovoltaic (PV) grid-following (GF) controller

The Solar PV Controller (Three-Phase) block implements a photovoltaic (PV)
grid-following (GF) controller that uses a maximum power point tracking (MPPT) algorithm. The
inputs to the block are the:

- Per-unit reactive power reference *Qref*
- DC-side current in amps *ipv*
- DC-side voltage in volts *vdc*
- AC-side per-unit voltage *vabc*
- AC-side per-unit current *iabc*

The outputs of the block are the per-unit reference voltage wave for the solar inverter
*vabcRef* and a bus containing signals for visualization. This figure shows
the top-level structure of the controller.

The Volt-VAR controller calculates the per-unit *q*-axis current
reference *i*q ref.

The MPPT algorithm calculates the DC-side reference voltage
*V*dc ref in volts.

The DC voltage controller calculates the per-unit *d*-axis current
reference *i*d ref.

The phase-locked loop (PLL) calculates the:

- Phase angle *θ* of the input voltage signal
  *v*abc
- Per-unit *d*-axis voltage
  *V*d
- Per-unit *q*-axis voltage
  *V*q

The Park transform converts *iabc* and *θ* into the:

- Per-unit *d*-axis current
  *i*d
- Per-unit *q*-axis current
  *i*q

The current controller calculates the:

- Per-unit *d*-axis voltage reference
  *V*d ref
- Per-unit *q*-axis voltage reference
  *V*q ref

The inverse Park transform converts *V*d ref and
*V*q ref into *vabcRef*.

For discrete-time simulation, set **Sample time (-1 for inherited)** to a
positive value or to `-1` to inherit the sample time. For continuous-time
simulation, set **Sample time (-1 for inherited)** to
`0`.

To choose the MPPT algorithm, in the **MPPT** tab, set the
**Algorithm** parameter to one of these options:

- `Perturb and observe (P&O)` — The P&O algorithm
  perturbs the operating voltage of the solar panel. The algorithm then observes the
  change in power output. If the power increases, the perturbation continues in the same
  direction. If the power decreases, the algorithm reverses the perturbation. To
  prioritize simulation speed, use this option.
- `Incremental conductance (INC)` — The INC algorithm
  calculates the incremental change in current and voltage to determine the slope of the
  power-voltage curve. If the slope is positive, the operating point moves to a higher
  voltage. If the slope is negative, the operating point moves to a lower voltage. If the
  slope is close to zero, the algorithm has reached the maximum power point (MPP). To
  prioritize accuracy in tracking the MPP, use this option.

### Visualization

The block outputs a bus containing these nine signals for visualization:

- Estimated phase angle *θ* of the input voltage signal
  *v*abc
- DC-side voltage *V*dc in volts
- Per-unit *q*-axis current reference
  *i*q ref
- Per-unit *d*-axis current reference
  *i*d ref
- DC-side reference voltage *V*dc ref in
  volts
- Per-unit *d*-axis voltage
  *V*d
- Per-unit *q*-axis voltage
  *V*q
- Per-unit *d*-axis current
  *i*d
- Per-unit *q*-axis current
  *i*q
