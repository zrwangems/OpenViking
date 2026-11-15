---
type: simulink-block
title: 'PWM Timing and Waveform Generator (Three-phase, Three-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmtimingandwaveformgeneratorthreephasethreelevel'
documentation_source_path: 'ref/pwmtimingandwaveformgeneratorthreephasethreelevel.html'
language: en
---

# PWM Timing and Waveform Generator (Three-phase, Three-level)

## Ports

### Input

### **Vabc** — Three-phase sinusoidal reference signal vector

Sinusoidal voltages that you want the attached converter to output, specified as a
vector of three elements, with one element for each phase.

### **vdc** — DC-link voltage signal scalar

Positive real number for the DC-link voltage of the converter,
specified as a scalar.

### **vneutral** — DC-link neutral point balance control scalar

Output from a feedback-control loop that balances the DC supply,
specified as a real number between `–1` and
`+1`.
### Output

### **TgabcON** — Switch-on gating time vector

Switch-on gating time, returned as a vector of three elements, with
one element for each phase.

### **TgabcOFF** — Switch-off gating time vector

Switch-off gating time, returned as a vector of three elements, with
one element for each phase.

### **SmallHexNum** — Small hexagon number scalar

Number of the small hexagon that composes the space–vector diagrams of conventional
two-level inverters, returned as a scalar between 1 and 6. For more
information, see the Simplified Space-Vector PWM Method
section in the PWM
Gate Signal Generator (Three-phase, Three-level)
block.

### **ModWave** — Modulation waves vector

Modulation waves, returned as a vector of three elements, with one
element for each phase.

## Parameters

### **Continuous PWM** — Continuous pulse width modulation method `SPWM: sinusoidal PWM` (default) | `SVM: space vector modulation`

Specify the waveform technique.

### **Sampling mode** — Wave-sampling method `Natural` (default) | `Asymmetric` | `Symmetric`

Wave-sampling method. The sampling mode determines whether the block samples the
modulation waveform when the waves intersect or when the carrier wave is at
one or both of its boundary conditions.

### **Switching frequency (Hz)** — Switching rate `1e3` (default) | positive scalar

Rate at which the switches in the power converter switch.

## Libraries

Simscape / Electrical / Control / Pulse Width Modulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Generate three-phase, three-level gating time information

The PWM Timing and Waveform Generator (Three-phase, Three-level) block
controls switching behavior for a three-phase, three-level power converter. The block
calculates on-gating and off-gating times and modulation waves based on these block
inputs:

- Three sinusoidal reference voltages
- A DC-link voltage
- A DC-link neutral point balance control signal

This block can be used with average converters to speed up the
simulation.

### Sampling Mode

This block allows you to choose natural, symmetric, or asymmetric sampling of the
modulation wave.

The PWM Timing and Waveform Generator (Three-phase, Three-level) block does
not perform carrier-based pulse width modulation (PWM). Instead, the block uses
input signals to calculate the gating times.

Carrier-based PWM is, however, useful for showing how the sampling mode that you
select relates to the switch-on and switch-off behavior of the pulses that the block
generates. A generator that uses a three-level, carrier-based PWM method:

1. Samples a reference wave
2. Compares the sample to two parallel triangle carrier waves, separated by one level
3. Generates a switch-on pulse if a sample is higher than the carrier
   signal or a switch-off pulse if a sample is lower than the carrier
   wave

To determine switch-on and switch-off pulse behavior, a three-level carrier-based
PWM generator uses these methods to sample each of the triangle waves:

- Natural — The sampling and comparison occur at the intersection
  points of the modulation wave and the carrier wave.
- Asymmetric — Sampling occurs at the upper and lower boundaries
  of the carrier wave. The comparison occurs at the intersection that
  follows the sampling.
- Symmetric — Sampling occurs only at the upper boundary of the
  carrier wave. The comparison occurs at the intersection that follows the sampling.
