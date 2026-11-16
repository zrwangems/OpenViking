---
type: simulink-block
title: 'VCO Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Measurements & Testbenches'
documentation_page: 'vcotestbench'
documentation_source_path: 'ref/vcotestbench.html'
language: en
---

# VCO Testbench

## Ports

### Input

### **from vco** — Input signal scalar

Input signal, which flows from the output of the VCO
DUT. This input signal is used to calculate either the phase noise
metric, or the voltage sensitivity and free running frequency of the
VCO, depending on the **Measurement** option
chosen.

**Data Types:** `double`
### Output

### **to vco** — Output signal scalar

Output signal, which provides control voltage stimulus to the input of
VCO DUT.

**Data Types:** `double`

## Parameters

### **Measurement** — Target metric to be measured `Phase noise` (default) | `Kvco and Fo`

Determines which of the two given target metrics is being measured.

Select `Phase noise` if you want the testbench to
measure and compare phase noise to a target phase noise profile.

Select `Kvco and Fo` if you want the testbench to
compute voltage sensitivity (*K*vco)
and quiescent frequency (*F*o) using
a range of control voltages.

#### Programmatic Use

- Use `get_param(gcb,'MeasureOptions')` to
  view the current **Measurement** option.
- Use `set_param(gcb,'MeasureOptions',value)`
  to set **Measurement** to a specific
  option.

### **Set stop time** — Set recommended minimum simulation stop time as model stop time button

Click to set the **Recommended min. simulation stop time
(s)** reported by the VCO Testbench block as the
model stop time.

#### Dependencies

This button is only available when you select `Phase
noise` as the **Measurement**
option.

### **Plot measurement** — Plot measurements button

Plots the relevant VCO metrics based on the
**Measurement** options.

Selecting `Phase noise` in
**Measurement** plots phase noise profile of
VCO.

Selecting `Kvco and Fo` in
**Measurement** plots the VCO characteristics and
*K*vco.

### **Export measurement results** — Export measurement results button

Exports the relevant VCO metrics based on the
**Measurement** options to an excel file.

Selecting `Phase noise` in
**Measurement** exports the phase noise profile of
VCO.

Selecting `Kvco and Fo` in
**Measurement** exports the VCO characteristics and
*K*vco.

### Stimulus

### **Control voltage (V)** — VCO control voltage `2` (default) | scalar

Control voltage provided by VCO Testbench, expressed as
a scalar in V. The value specified in **Control Voltage
(V)** flows through the **to vco** port
that provides the input of VCO.

#### Dependencies

To enable this parameter, select `Phase
noise` as the **Measurement**
option.

#### Programmatic Use

- Use `get_param(gcb,'ControlVoltage')`
  to view current **Control Voltage (V)**
  value.
- Use
  `set_param(gcb,'ControlVoltage',value)`
  to set **Control Voltage (V)** to a
  specific value.

**Data Types:** `double`

### **Range of control voltage (V)** — Range of VCO control voltages `[2 7]` (default) | two-element row vector

Control voltage provided by VCO Testbench, expressed as
a two-element row vector in V. This parameter specifies the minimum and
maximum values of control voltage, which is used to generate ten control
voltage value points, including the provided values. These ten values of
control voltage are sent to VCO input to measure
*K*vco and
*F*o.

#### Dependencies

To enable this parameter, select `Kvco and
Fo` as the **Measurement**
option.

#### Programmatic Use

- Use
  `get_param(gcb,'ControlVoltageRange')` to
  view the current **Range of control voltage
  (V)** values.
- Use
  `set_param(gcb,'ControlVoltage',value)`
  to set **Range of control voltage (V)** to
  specific values.

**Data Types:** `double`

### Setup

### **Autofill setup parameters** — Automatically calculate setup parameters for phase noise measurement button

Click this button to automatically populate setup parameters (
**Resolution bandwidth (Hz)** and **No. of
spectral averages**) for phase noise measurement.

If the DUT is a VCO from Mixed-Signal Blockset, the `dsp.SpectrumEstimator`
System object™ used by the VCO Testbench block for phase
noise measurement automatically calculates setup parameters based on the
VCO specifications.

#### Dependencies

- This button only works if the VCO DUT is a VCO block from
  Mixed-Signal Blockset.

- This button is only available when you select
  `Phase noise` as the
  **Measurement** option.

### **Resolution bandwidth (Hz)** — Smallest positive frequency that can be resolved `30e3` (default) | real positive scalar

Smallest positive frequency that can be resolved, specified as a real
positive scalar. The **Resolution bandwidth (Hz)** is
used to determine window length for spectral analysis using the Welch
method. For more information, see Welch's Method of Averaged Modified Periodograms.

In general, **Resolution bandwidth (Hz)** should be
less than or equal to the lowest offset frequency value.

If the DUT is a VCO block from the Mixed-Signal Blockset library, you can use the **Autofill setup
parameters** button to automatically calculate
**Resolution bandwidth (Hz)**.

#### Dependencies

To enable this parameter, select `Phase
noise` as the **Measurement**
option.

#### Programmatic Use

- Use `get_param(gcb,'ResBandwidth')` to
  view current **Resolution bandwidth (Hz)**
  value.
- Use
  `set_param(gcb,'ResBandwidth',value)` to
  set **Resolution bandwidth (Hz)** to a
  specific value.

**Data Types:** `double`

### **No. of spectral averages** — Number of spectral averages `8` (default) | positive integer scalar

Number of spectral averages, specified as a positive integer scalar.
The `dsp.SpectrumEstimator`
System object used by the Phase Noise Measurement subsystem inside the
VCO Testbench block computes the current power
spectrum or power density spectrum estimate by averaging over the number
specified by **No. of spectral averages**.

If the DUT is a VCO block from the Mixed-Signal Blockset library, you can use the **Autofill setup
parameters** button to automatically calculate number of
spectral averages.

#### Dependencies

To enable this parameter, select `Phase
noise` as the **Measurement**
option.

#### Programmatic Use

- Use `get_param(gcb,'SpectralAverages')`
  to view current **No. of spectral
  averages** value.
- Use
  `set_param(gcb,'SpectralAverages',value)`
  to set **No. of spectral averages** to a
  specific value.

**Data Types:** `double`

### **Hold-off time (s)** — Delays measurement analysis to avoid transients `0` (default)

Hold-off period, specified as a nonnegative scalar in s.
**Hold-off time** delays measurement analysis by
the specified amount of time to avoid corrupting simulation results due
to transients.

#### Programmatic Use

- Use `get_param(gcb,'HoldOffTime')` to
  view the current **Hold-off time (s)**
  value.
- Use
  `set_param(gcb,'HoldOffTime',value)` to
  set **Hold-off time (s)** to a specific
  value.

### Target Metric

### **Autofill target metric** — Automatically populate target phase noise metric button

Click this button to automatically populate the target phase noise
metric from VCO specifications.

#### Dependencies

- This button will only work if the VCO DUT is a
  VCO block from Mixed-Signal Blockset.
- This button is only available when you select
  `Phase noise` as
  **Measurement** option.

### **Phase noise frequency offset vector (Hz)** — Phase noise frequency offset vector `[30e3 100e3 1e6 3e6 10e6]` (default) | real valued vector

The frequency offsets of phase noise from the carrier frequency,
collected from the data sheet, specified as a real valued vector in
Hz.

If the DUT is a VCO block from the Mixed-Signal Blockset library, you can use the **Autofill target
metric** button to automatically transfer
VCO phase noise frequency offset vector values to the
VCO Testbench.

#### Dependencies

To enable this parameter, select `Phase
noise` as the **Measurement**
option.

#### Programmatic Use

- Use
  `get_param(gcb,'PhaseNoiseFreqOffset')`
  to view the current **Phase noise frequency offset
  vector (Hz)** value.
- Use
  `set_param(gcb,'PhaseNoiseFreqOffset',value)`
  to set **Phase noise frequency offset vector
  (Hz)** to a specific value.

**Data Types:** `double`

### **Phase noise vector (dBc/Hz)** — Phase noise vector `[-45 -55 -65 -75 -100]` (default) | real valued vector

The phase noise power in a 1 Hz bandwidth centered at the specified
frequency offsets relative to the carrier, collected from the data
sheet, specified as a real valued vector in dBc/Hz. The elements of
**Phase noise vector (dBc/Hz)** corresponds to
relative elements in the **Phase noise frequency offset vector
(Hz)**.

If the DUT is a VCO block from the Mixed-Signal Blockset library, you can use the **Autofill target
metric** button to automatically transfer
VCO phase noise vector values to the
testbench.

#### Dependencies

To enable this parameter, select `Phase
noise` as the **Measurement**
option.

#### Programmatic Use

- Use `get_param(gcb,'PhaseNoiseVector')`
  to view the current **Phase noise vector
  (dBc/Hz)** value.
- Use
  `set_param(gcb,'PhaseNoiseVector',value)`
  to set **Phase noise vector (dBc/Hz)** to a
  specific value.

## Libraries

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Validate voltage controlled oscillator (VCO) by measuring phase noise metrics or VCO characteristics

The VCO Testbench block validates the VCO device under test (DUT) by
measuring one of the two target metrics: phase noise, or voltage sensitivity and
quiescent frequency. You can use the testbench to validate a VCO of your own
implementation, or you can use the VCO block
from the Mixed-Signal Blockset™.

The VCO Testbench block generates the stimulus (control voltage) to
drive the device under test (DUT) from the **Stimulus** tab. The setup
parameters for validating the DUT are defined in the **Setup** tab and
the target validation metrics are defined in the **Target Metric**
tab.

To take the full advantage of the VCO testbench capabilities by using autofill
parameters options, use only two blocks, the VCO DUT and the VCO
Testbench in the Simulink® model.
