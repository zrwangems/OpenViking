---
type: simulink-block
title: 'PWM Generator (Three-phase, Three-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgeneratorthreephasethreelevel'
documentation_source_path: 'ref/pwmgeneratorthreephasethreelevel.html'
language: en
---

# PWM Generator (Three-phase, Three-level)

## Ports

### Input

### **Vabc** — Three-phase sinusoidal reference signal vector

Specify the three sinusoidal voltages, one per phase, that you want
the attached converter to output.

### **vdc** — DC-link voltage signal scalar

Specify a positive real number for the DC-link voltage of the
converter.

### **vneutral** — DC-link neutral point balance control scalar

This signal is the output from a feedback-control loop that balances
the DC supply. The value of the signal must be a real number between
`–1` and `+1`.
### Output

### **g** — Gate control vector

12 pulse waveforms that determine switching behavior in the attached
power converter.

### **ModWave** — Modulation wave vector

If you are generating code for a platform that has hardware with PWM
capability, you can deploy the modulation wave to the hardware.
Otherwise, this data is for reference only.

## Parameters

### **Continuous PWM** — Continuous pulse width modulation method `SPWM: sinusoidal PWM` (default) | `SVM: space vector modulation`

Specify the waveform technique.

### **Sampling mode** — Wave-sampling method `Natural` (default) | `Asymmetric` | `Symmetric`

The sampling mode determines whether the block samples the modulation
waveform when the waves intersect or when the carrier wave is at one or both
of its boundary conditions.

### **Switching frequency (Hz)** — Switching rate `1e3` (default) | positive number

Specify the rate at which you want the switches in the power converter to
switch.

### **Sample time (s)** — Block sample time `5e-5` (default) | positive number

Specify the time interval between successive block executions (output
calculations). To ensure adequate resolution in the generated signal, set
this value to be less than or equal to
`1/(10*Fsw)`,
where *F*sw is the
**Switching frequency (Hz)**.

## Libraries

Simscape / Electrical / Control / Pulse Width Modulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Generate three-phase, three-level pulse width modulated signal or waveform for gating switching devices

The PWM Generator (Three-phase, Three-level) block controls switching
behavior for a three-phase, three-level power converter. The block:

1. Calculates on- and off-gating times based on the block inputs:

   - Three sinusoidal reference voltages
   - A DC-link voltage
   - A DC-link neutral point balance control signal
2. Uses the gating times to generate 12 switch-controlling pulses.
3. Uses the gating times to generate modulation waveforms.

### Sampling Mode

This block allows you to choose natural, symmetric, or asymmetric sampling of the
modulation wave.

The PWM Generator (Three-phase, Two-level) block does not perform
carrier-based pulse width modulation (PWM). Instead, the block uses input signals to
calculate gating times and then uses the gating times to generate both the
switch-controlling pulses and the modulation waveforms that it outputs.

Carrier-based PWM is, however, useful for showing how the sampling mode that you
select relates to the switch-on and switch-off behavior of the pulses that the block
generates. A generator that uses a three-level, carrier-based PWM method:

1. Samples a reference wave.
2. Compares the sample to two parallel triangle carrier waves, separated
   by one level.
3. Generates a switch-on pulse if a sample is higher than the carrier
   signal or a switch-off pulse if a sample is lower than the carrier
   wave.

To determine switch-on and switch-off pulse behavior, a three-level carrier-based
PWM generator uses these methods to sample each of the triangle waves:

- Natural — The sampling and comparison occur at the intersection
  points of the modulation wave and the carrier wave.
- Asymmetric — Sampling occurs at the upper and lower boundaries
  of the carrier wave. The comparison occurs at the intersection that
  follows the sampling.
- Symmetric — Sampling occurs only at the upper boundary of the
  carrier wave. The comparison occurs at the intersection that follows the sampling.

### Overmodulation

The modulation index, which measures the ability of the power converter to output
a given voltage, is defined as

m=VMVC,

where

- *m* is the modulation index.
- *Vm* is the peak value of the
  modulation wave.
- *Vc* is the peak value of the
  triangle carrier wave.

For three-phase SPWM,

Vpeak=mvdc2,

where

- *Vpeak* is the peak value of
  the fundamental component of the phase-to-neutral voltage.
- *vdc* is the DC-link
  voltage.

For three-phase space-vector PWM (SVM),

Vpeak=mvdc3.

For normal steady-state operation, `0` <*m* ≤
`1`. If a transient, such as a load increase, causes the
amplitude of *Vm* to exceed the amplitude of
*Vc*, overmodulation
(*m* > `1`) occurs

If overmodulation occurs, the output voltage of the power converter clamps to the
positive or negative DC rail.

In the Three-Phase Three-Level PWM
Generator example, the **Three-Level Controller**
subsystem contains a 1800–V DC-link input, and a modulation index,
*m*, of 0.8. For SVM, the maximal input voltage is 1800/3V, that is 1039.23 V. To demonstrate overmodulation, a transient is
added at the beginning of the simulation. The transient forces the amplitudes of the
reference voltages to exceed the amplitude of 1/3 of the DC-link voltage. To highlight overmodulation, the scope
includes simulation results for only one of the 12 output pulses and only the
*a*-phase of the reference voltages, modulation waveforms, and
output voltages.

The modulation index is greater than one between 0.03–0.09 seconds.
During overmodulation:

- The pulse remains in the on or off position.
- The output voltage clamps to the positive or negative DC rail.
