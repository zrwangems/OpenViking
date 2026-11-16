---
type: simulink-block
title: 'Sinusoidal Measurement (PLL, Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'sinusoidalmeasurementpllthreephase'
documentation_source_path: 'ref/sinusoidalmeasurementpllthreephase.html'
language: en
---

# Sinusoidal Measurement (PLL, Three-Phase)

## Ports

### Input

### **abc** — Input signal vector

Three-phase input signal.

**Data Types:** `single` | `double`
### Output

### **freq** — Frequency, Hz scalar

Estimated frequency of the input signal, in Hz.

**Data Types:** `single` | `double`

### **angle** — Phase angle, rad scalar

Estimated phase angle of the first phase of the input signal, in
rad.

**Data Types:** `single` | `double`

### **mag** — Magnitude, unitless scalar

Magnitude of the input signal.

**Data Types:** `single` | `double`

## Parameters

### **Enable moving average filter on input** — Option to enable frequency-dependent moving average filter `On` (default) | `Off`

*Since R2025a*

Option to enable the frequency-dependent moving average filter on the
input signal. When you select this parameter, the block filters out the
noise that comes from negative and zero sequence.

### **Enable input normalization** — Option to enable normalization of input `Off` (default) | `On`

*Since R2025a*

Option to enable the normalization of the input.

### **Loop filter proportional gain** — LF proportional gain `1` (default) | positive scalar

Proportional gain for the loop filter. Increase this value to increase the
rate at which steady-state error is eliminated in the phase angle. This
value also determines the aggressiveness of the PLL in tracking and locking
to the phase angle.

### **Loop filter integral gain** — LF integral gain `10` (default) | positive scalar

Integral gain for the loop filter. This parameter determines the
aggressiveness of the PLL in tracking and locking to the phase. Increase
this value to reduce and eliminate steady-state error in the phase
angle.

### **Initial frequency (Hz)** — Initial estimate of input frequency `60 Hz` (default) | scalar

Initial estimate of the input frequency.

### **Initial phase angle (rad)** — Initial estimate of phase angle `0 rad` (default) | scalar or vector

Initial estimate of the phase angle.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `0` | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set this parameter to `-1`.
For discrete-time operation, set this parameter to a positive integer. For
continuous-time operation, set this parameter to `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote this parameter to ensure
correct switching between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / Measurements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2025a: Enable frequency-dependent moving average filter and input normalization

You can now enable or disable the frequency-dependent moving average filter on the
input signal by using the **Enable moving average filter on input**
parameter.

You can also enable or disable the normalization of the input signal by using the
**Enable input normalization** parameter.

## Description

Estimate three-phase sinusoidal characteristics using a phase-locked loop

The Sinusoidal Measurement (PLL, Three-Phase) block estimates the
frequency characteristics of a balanced three-phase sinusoidal signal. The block uses a
standard phase-locked loop (PLL) strategy to estimate the frequency and phase angle of
the input signal. It also outputs the magnitude of the input signal.

Use this block in control applications when the frequency, phase angle, or magnitude
are required and cannot be measured directly. To estimate the frequency characteristics
of a non-three-phase or unbalanced sinusoidal signal, use the Sinusoidal Measurement
(PLL) block instead.

### Equations

The phase-locked loop generates a sinusoid that approximates the input signal
*u(t)* with the form:

y(t)=A(t)sin(ϕ0+∫2πf(t)dt),

where:

- *y* is the estimate of the input signal.
- *A* is the amplitude of the input signal.
- *ϕ0* is the initial phase
  angle of the input signal.

Because the input signal is assumed to be balanced, the block
calculates the amplitude directly from the instantaneous amplitude of the three
phases. The estimated phase angle *ϕ* is the angle of this
generated sinusoid:

ϕ(t)=ϕ0+∫2πf(t)dt,

where *f* if the frequency of the sinusoid, and
*ϕ0* is the initial phase
angle.

This diagram shows the overall structure of the phase-locked loop.

In the diagram:

- The phase detector produces an error signal relative to the phase
  difference *eϕ* between the
  input sinusoid *u* and the synthesized sinusoid
  *y*. It also outputs the amplitude
  *A*.
- The loop filter provides an estimate of the input angular frequency
  *ω* by filtering out the high-frequency components
  of the phase difference. The block also outputs the converted frequency
  *f* in Hz.
- The voltage-controlled oscillator integrates the angular speed to
  produce the phase estimate *ϕ* which it sends to the
  Phase Detector for comparison.
