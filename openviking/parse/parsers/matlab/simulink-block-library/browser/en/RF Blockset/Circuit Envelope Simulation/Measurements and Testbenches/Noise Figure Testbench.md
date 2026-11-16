---
type: simulink-block
title: 'Noise Figure Testbench'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / Noise Modeling'
documentation_page: 'noisefiguretestbench'
documentation_source_path: 'ref/noisefiguretestbench.html'
language: en
---

# Noise Figure Testbench

## Ports

Not documented in R2025b.

## Parameters

#### Parameters

### **Use Internal Configuration block** — Use testbench internal configuration block on (default) | off

Select to use testbench internal configuration block. Clear this parameter
to specify your own configuration block.

**Note**

When using your own configuration block, parameters such as step size,
fundamental tones, harmonic order, and simulate noise may affect the
measured results.

### **Simulate noise (both stimulus and DUT internal)** — Enable noise modeling in stimulus signal on (default) | off

Select to enable noise modeling in the stimulus signal entering the DUT
and inside the DUT. In the NF testbench, this parameter is permanently
disabled because stimulus noise is required for meaningful noise
calculation.

#### Dependencies

To enable this parameter, select **Use internal Configuration
block**.

### **Input power amplitude (dBm)** — Input power to DUT `-30` (default) | scalar

Input power to DUT, specified as a scalar in dBm. You can change the input
power by entering the value in the text box or selecting a value using the
knob. The specified input power represents the power available at the input
ports of the DUT. The valid values are between -`90` dBm
and `60` dBm.

### **Input frequency (Hz)** — Carrier frequency of DUT `2.1e9` (default) | scalar

Carrier frequency of the DUT, specified as a scalar in Hz. Input frequency
must greater than baseband bandwidth.

### **Output frequency (Hz)** — Output frequency of DUT `2.1e9` (default) | scalar

Output frequency of DUT, specified as a scalar in Hz. Output frequency
must greater than baseband bandwidth.

### **Baseband bandwidth (Hz)** — Baseband bandwidth of input signal `10e6` (default) | scalar

Baseband bandwidth of input signal, specified as a scalar in Hz. The value
must be greater than zero.

### **Source impedance (Ohm)** — Source impedance to measure DUT `50` (default) | complex finite scalar

Source impedance to measure DUT, specified as a complex finite scalar in
ohms. The real part of the impedance must be positive.

### **Clear noise history** — Clear noise history button (default)

Use this button to clear noise history used for internal noise
measurement. When a DUT has an initial settling time duration, it is
recommended to clear noise history after this duration. This improves the
accuracy and convergence of noise measurement.

### **Show Response spectrum** — View response spectrum using a spectrum scope during simulation on (default) | off

Select to view response spectrum using a spectrum scope during simulation.

### **Ground and hide negative terminals** — Internally ground and hide RF circuit terminals on (default) | off

Select to internally ground and hide the negative terminals. Clear to
expose the negative terminals. By exposing these terminals, you can connect
them to other parts of your model.

## Libraries

RF Blockset / Circuit Envelope / Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Measures noise figure of system

Use the `Noise Figure Testbench` to measure the noise figure (NF) of
an RF device under test (DUT).
