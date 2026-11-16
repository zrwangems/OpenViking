---
type: simulink-block
title: 'PWM Generator (Vienna Rectifier)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgeneratorviennarectifier'
documentation_source_path: 'ref/pwmgeneratorviennarectifier.html'
language: en
---

# PWM Generator (Vienna Rectifier)

## Ports

### Input

### **Vabc** — Three-phase sinusoidal reference signal vector

Three sinusoidal voltages, one per phase.

### **Iabc** — Three-phase current reference signal vector

Three currents, one per phase.

### **vdc** — DC link voltage signal positive scalar

DC link voltage of the converter. The value of the signal must be
greater than 0.

### **vneutral** — DC link neutral point balance control scalar

Output of the feedback-control loop that balances the DC supply. The
value of the signal must be between `–1` and
`+1`.
### Output

### **g** — Gate control vector

Three-pulse waveforms that determine the switching behavior in the attached power
converter.

## Parameters

### **Sampling mode** — Wave sampling method `Natural` (default) | `Asymmetric` | `Symmetric`

Sampling mode that determines whether the block samples the modulation
waveform when the waves intersect or when the carrier wave is at one or both
of its boundary conditions.

### **Switching frequency (Hz)** — Switching rate `1e3` `Hz` (default) | positive number

Rate at which the switches in the power converter switch, in Hz.

### **Sample time (s)** — Block sample time `5e-5` `s` (default) | positive number

Time interval between successive block executions, in s. To ensure adequate resolution in
the generated signal, set this value to be less than or equal to
`1/(50*Fsw)`,
where *F*sw is the
**Switching frequency (Hz)**.

## Libraries

Simscape / Electrical / Control / Pulse Width Modulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Vienna rectifier pulse-width modulation waveform generator

The PWM Generator (Vienna Rectifier) block:

1. Calculates on-gating and off-gating times based on the block inputs:

   - Three sinusoidal reference voltages, one per phase, that must
     be generated at the AC side of the Vienna rectifier, one per
     phase
   - Three filtered input sinusoidal current measurements of the
     Vienna rectifier, one per phase
   - A DC-link voltage
   - A DC-link neutral point balance control signal
2. Uses the gating times to generate three switch-controlling pulses.

The block uses a simplified space vector modulation method based on the equivalence
between two-level and three-level converters to generate the control pulses [1].

The three-phase filtered input currents are used to identify the active voltage vector
hexagons. The switching sequence selection and on-gating and off-gating times are
determined by simplifying the space-vector diagram of a three-level inverter into that
of a two-level inverter [2].

The DC link neutral point balance control signal that comes from the external DC link
neutral control loop is used to adjust the time distribution of the redundant voltage
vectors within one single switching period.

### Sampling Mode

The block allows you to choose natural, symmetric, or asymmetric sampling of the modulation
wave.

The PWM Generator (Vienna Rectifier) block does not perform carrier-based
pulse-width modulation (PWM). Instead, the block uses input signals to calculate
gating times and uses the gating times to generate the switch-controlling
pulses.

For more information about the sampling modes, see PWM Generator (Three-phase, Two-level).
