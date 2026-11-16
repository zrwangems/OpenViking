---
type: simulink-block
title: 'PWM Gate Signal Generator (Five-phase, Two-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgatesignalgeneratorfivephasetwolevel'
documentation_source_path: 'ref/pwmgatesignalgeneratorfivephasetwolevel.html'
language: en
---

# PWM Gate Signal Generator (Five-phase, Two-level)

## Ports

### Input

### **TgabcdeON** — Switch-on gating time vector

Switch-on gating time, specified as a vector of five elements with one element for each
phase.

### **TgabcdeOFF** — Switch-off gating time vector

Switch-off gating time, specified as a vector of five elements with one element for each
phase.
### Output

### **g** — Gate control vector

Ten pulse waveforms that determine the switching behavior in the
attached power converter, returned as a vector.

## Parameters

### **Sampling mode** — Wave-sampling method `Natural` (default) | `Asymmetric` | `Symmetric`

Wave-sampling method. The sampling mode determines whether the block
samples the modulation waveform when the waves intersect or when the carrier
wave is at one or both of its boundary conditions.

### **Switching frequency (Hz)** — Switching rate `1e3` (default) | positive scalar

Rate at which the switches in the power converter switch, in Hz.

### **Sample time (s)** — Block sample time `5e-5` (default) | positive scalar

Time interval between successive block executions, in seconds. To ensure adequate
resolution in the generated signal, set this value to be less than or equal
to `1/(50*Fsw)`,
where *F*sw is the value of the
**Switching frequency (Hz)** parameter.

## Libraries

Simscape / Electrical / Control / Pulse Width Modulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Generate ten switch-controlling pulses for five-phase, two-level gating switching devices

The PWM Gate Signal Generator (Five-phase, Two-level) block controls
the switching behavior for a five-phase, two-level power converter. The block uses the
gating times provided as inputs to generate ten switch-controlling pulses. You can
obtain the gating time information using the PWM Timing and Waveform
Generator (Five-phase, Two-level) block.

### Sampling Mode

This block allows you to choose natural, symmetric, or asymmetric sampling of the
modulation wave.

The PWM Gate Signal Generator (Five-phase, Two-level) block does
not perform carrier-based pulse width modulation (PWM). Instead, the block uses the
gating times to generate both the switch-controlling pulses and the modulation
waveforms that the block outputs.

Carrier-based PWM is, however, useful for showing how the sampling mode that you
select relates to the switch-on and switch-off behavior of the pulses that the block
generates. A generator that uses a three-level, carrier-based PWM method:

1. Samples a reference wave
2. Compares the sample to two parallel triangle carrier waves, separated
   by one level
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
