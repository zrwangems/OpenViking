---
type: simulink-block
title: 'PWM Generator (Five-phase, Two-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgeneratorfivephasetwolevel'
documentation_source_path: 'ref/pwmgeneratorfivephasetwolevel.html'
language: en
---

# PWM Generator (Five-phase, Two-level)

## Ports

### Input

### **Vabcde** — Five-phase sinusoidal reference signal vector

Sinusoidal voltages that you want the attached converter to output, specified as a
vector of five elements with one element for each phase.

### **vdc** — DC-link voltage signal scalar

Positive real number for the DC-link voltage of the converter,
specified as a scalar.
### Output

### **g** — Gate control vector

Ten pulse waveforms that determine the switching behavior in the
attached power converter, returned as a vector.

### **ModWave** — Modulation wave vector

Modulation waves, returned as a vector of five elements, with one
element for each phase.

## Parameters

### **Continuous PWM** — Continuous pulse width modulation method `SPWM: sinusoidal PWM` (default) | `SVM: space vector modulation`

Continuous pulse width modulation method.

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

Generate five-phase, two-level pulse width modulated waveform

The PWM Generator (Five-phase, Two-level) block controls switching
behavior for a five-phase, two-level power converter. The block:

1. Calculates on-gating and off-gating times based on the block inputs:

   - Five sinusoidal reference voltages, one per phase
   - A DC-link voltage
2. Uses the gating times to generate ten switch-controlling pulses.
3. Uses the gating times to generate modulation waveforms.

### Continuous PWM

The block only provides continuous pulse width modulation (PWM). The figure shows
the general difference between continuous sinusoidal pulse width modulation (SPWM)
and continuous space vector modulation (SVM) waveforms.

### Sampling Mode

This block allows you to choose natural, symmetric, or asymmetric sampling of the
modulation wave.

The PWM Generator (Five-phase, Two-level) block does not perform
carrier-based PWM. Instead, the block uses input signals to calculate gating times
and then uses the gating times to generate both the switch-controlling pulses and
the modulation waveforms that it outputs.

Carrier-based PWM is, however, useful for showing how the sampling mode that you
select relates to the switch-on and switch-off behavior of the pulses that the block
generates. A generator that uses a two-level, carrier-based PWM method:

1. Samples a reference wave.
2. Compares the sample to a triangle carrier wave.
3. Generates a switch-on pulse if a sample is higher than the carrier
   signal or a switch-off pulse if a sample is lower than the carrier
   wave.

To determine switch-on and switch-off pulse behavior, a two-level carrier-based
PWM generator uses these methods to sample the triangle wave:

- Natural — The sampling and comparison occur at the intersection
  points of the modulation wave and the carrier wave.
- Asymmetric — Sampling occurs at the upper and lower boundaries
  of the carrier wave. The comparison occurs at the intersection that
  follows the sampling.
- Symmetric — Sampling occurs at only the upper boundary of the
  carrier wave. The comparison occurs at the intersection that follows the sampling.
