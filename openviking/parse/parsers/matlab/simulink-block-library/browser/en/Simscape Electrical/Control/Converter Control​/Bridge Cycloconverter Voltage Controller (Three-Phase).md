---
type: simulink-block
title: 'Bridge Cycloconverter Voltage Controller (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Converter Control\u200b'
documentation_page: 'bridgecycloconvertervoltagecontrollerthreephase'
documentation_source_path: 'ref/bridgecycloconvertervoltagecontrollerthreephase.html'
language: en
---

# Bridge Cycloconverter Voltage Controller (Three-Phase)

## Ports

### Input

### **VRef** — Reference voltage scalar

Reference line-to-neutral RMS voltage, expressed in per-unit
representation.

**Data Types:** `single` | `double`

### **fRef** — Reference frequency scalar

Reference electrical frequency, in Hz.

**Data Types:** `single` | `double`

### **vabc** — Phase voltages vector

Measured phase voltages of the source, in V.

**Data Types:** `single` | `double`

### **Vcyc** — Cycloconverter voltages vector

Measured cycloconverter phase voltages, in V.

**Data Types:** `single` | `double`

### **Icyc** — Cycloconverter currents vector

Measured cycloconverter phase currents, in A.

**Data Types:** `single` | `double`
### Output

### **P** — Pulses vector

Thyristor pulse vector to control a three-phase bridge
cycloconverter.

**Data Types:** `single` | `double`

### **Visualization** — Visualization bus bus

Bus containing internal signals for visualization. For a full list of
signals, refer to the Visualization
section.

**Data Types:** `single` | `double`

## Parameters

### **Rated voltage (phase-to-phase RMS)** — Rated RMS voltage `6000` (default) | positive number

Rated RMS voltage for per-unit conversion calculations, in V.

### **Loop filter proportional gain** — LF proportional gain `2` (default) | positive number

Loop filter proportional gain for the phase-locked loop (PLL) estimating
the phase of the input signal. This value determines the aggressiveness of
the PLL in tracking and locking to the phase angle. Increase this value to
improve reaction time of the tracking to step changes in the phase
angle.

### **Loop filter integral gain** — LF integral gain `20` (default) | positive number

Loop filter integral gain for the phase-locked loop (PLL) estimating the
phase of the input signal. Increase this value to increase the rate at which
steady-state error is eliminated in the phase angle. This value also
determines the aggressiveness of the PLL in tracking and locking to the
phase.

### **Filters time constant (s)** — Time constant `1e-2` (default) | positive number

Time constant of the low-pass filters in the Signal Conditioning block of
the controller. These filters reduce undesired high-frequency noise in the
cycloconverter phase voltage and current measurements.

### **Controller proportional gain** — Proportional gain `1` (default) | positive number

Proportional gain for the PI-controller that generates the reference phase
voltage for the cycloconverter. Increase this value to increase the
aggressiveness of the controller.

### **Controller integral gain** — Integral gain `12` (default) | positive number

Integral gain of the PI-controller that generates the reference phase
voltage for the cycloconverter. Increase this value to increase the rate at
which steady-state error is eliminated in the phase voltage signal.

### **Controller anti-windup gain** — Anti-windup gain `10` (default) | positive number

Anti-windup gain of the PI-controller that generates the reference phase
voltage for the cycloconverter.

### **Thyristor pulse width (rad)** — Pulse width `5*pi/6` (default) | positive number

Angular width of pulses sent to the cycloconverter.

### **Bank selector current threshold (A)** — Current threshold `5` (default) | positive number

Current threshold for switching between positive and negative
converters.

### **Pulse ordering** — Pulse ordering rule `Sequential device order` (default) | `Natural order of commutation`

Strategy used for the ordering of generated pulses.

### **Sample time (-1 for inherited)** — Sample time `-1` (default) | positive number

Sample time for the block (-1 for inherited). If you use this block inside
a triggered subsystem, set the sample time to `-1`. If you
use this block in a continuous variable-step model, set the sample time
explicitly.

## Libraries

Simscape / Electrical / Control / Converter Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

RMS Voltage PI control for three-phase bridge cycloconverters

The Bridge Cycloconverter Voltage Controller (Three-Phase) block
implements a PI-based root-mean-square (RMS) voltage controller for three-phase bridge
cycloconverters.

To convert a three-phase signal directly from a higher frequency to a lower frequency,
use this block with a three-phase bridge cycloconverter. Refer to Three-Phase Bridge Cycloconverter for an example of such a
conversion.

### Operating Principle

The controller regulates the cycloconverter line-to-neutral RMS voltage to a given
value and a given electrical frequency. The structure of the cycloconverter
controller is illustrated in this diagram.

In the diagram:

- The controller integrates the desired output frequency
  *fref* to produce the
  reference electrical angle
  *θe\_ref*.
- The Signal Conditioning block filters the cycloconverter
  line-to-neutral voltage *vcyc*
  and current *icyc* to produce
  the per-unit RMS voltage
  *vrms\_cyc* and smoothed
  current signal
  *icyc\_lpf*.
- The PI Controller generates a reference phase voltage in the
  *q*-axis from the error between the desired
  output RMS voltage *Vref* and
  *vrms\_cyc*.
- The Inverse
  Park Transform block converts the reference phase voltage in
  *dq0*-coordinates to a phase voltage
  *vabc\_ref* in
  *abc*-coordinates.
- The Sinusoidal Power Measurement (PLL, Three-Phase) block
  estimates the phase angle *θ* of the input voltage
  signal *vabc*.

  The Modulator and Bank Selector blocks create the 36 pulses to drive
  the cycloconverter using the reference phase voltage
  *vabc\_ref*, estimated
  phase angle *θ*, and filtered cycloconverter current
  *icyc\_lpf*. To generate
  the firing angles, the controller uses the cosine wave crossing
  method.

This diagram shows the signal conditioning logic.

In the diagram:

- The Park
  Transform blocks convert the measured cycloconverter voltage
  *vcyc* and current
  *icyc* into
  *d*- and *q*-axis components
  (*vd*,*vq*,*id*,*iq*)
  using the reference electrical angle
  *θe\_ref*.
- The Low-Pass Filter (LPF) blocks remove the high-frequency
  noise from each of the *d*- and
  *q*-axis voltage and currents to produce the
  filtered components (*vd\_lpf*,
  *vq\_lpf*,
  *id\_lpf*,
  *iq\_lpf*).
- The block calculates the cycloconverter per-unit RMS voltage
  *vrms\_cyc* by taking the
  squared sum of the *dq* components, dividing by 2, and finally converting from SI to per-unit
  representation.
- The Inverse
  Park Transform converts the *dq* filtered
  current back to the *abc*-axis and outputs it as
  *icyc\_lpf*.

The cycloconverter reference line-to-neutral rms voltage output is
given in per-unit representation.

### Visualization

The block outputs a bus containing six signals for visualization:

- The estimated phase angle *θ* of the input voltage
  signal *vabc*
- The desired RMS voltage *Vref*
  of the output signal
- The reference phase voltages
  *vabc\_ref* of the desired
  output signal
- The filtered line-to-neutral cycloconverter RMS voltage
  *vrms\_cyc*
- The filtered cycloconverter phase currents
  *icyc\_lpf*
- The filtered cycloconverter phase voltages
  *vcyc\_lpf*
