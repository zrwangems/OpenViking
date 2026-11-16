---
type: simulink-block
title: 'Phase Noise Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Measurements & Testbenches'
documentation_page: 'phasenoisemeasurement'
documentation_source_path: 'ref/phasenoisemeasurement.html'
language: en
---

# Phase Noise Measurement

## Ports

### Input

### **sig** — Input signal scalar

Input time domain signal to the Phase Noise Measurement block,
specified as a scalar.

**Data Types:** `double`

## Parameters

### **Resolution bandwidth (Hz)** — Smallest positive frequency that can be resolved `30e3` (default) | real positive scalar

Smallest positive frequency that can be resolved, specified as a real positive
scalar. The **Resolution bandwidth (Hz)** is used to determine window
length for spectral analysis using the Welch method. For more information, see Welch's Method of Averaged Modified Periodograms.

In general, **Resolution bandwidth (Hz)** should be less than the
lowest offset frequency value.

#### Programmatic Use

- Use `get_param(gcb,'ResBandwidth')` to view the current
  value of **Resolution bandwidth (Hz)**.
- Use `set_param(gcb,'ResBandwidth',value)` to set
  **Resolution bandwidth (Hz)** to a specific value.

### **No. of spectral averages** — Number of spectral averages `4` (default) | positive integer scalar

Number of spectral averages, specified as a positive integer scalar. The `dsp.SpectrumEstimator`
System object™ used by the Phase Noise Measurement block computes the
current power spectrum or power density spectrum estimate by averaging over the number
specified by **No. of spectral averages**.

#### Programmatic Use

- Use `get_param(gcb,'SpectralAverages')` to view the current
  value of **No. of spectral averages**.
- Use `set_param(gcb,'SpectralAverages',value)` to set
  **No. of spectral averages** to a specific value.

### **Hold off time (s)** — Delays measurement analysis to avoid transients `0` (default) | real nonnegative scalar

Delays measurement analysis by the specified amount of time to avoid corruption by
transients, specified as a real nonnegative scalar in s.

#### Programmatic Use

- Use `get_param(gcb,'HoldOffTime')` to view the current
  value of **Hold off time (s)**.
- Use `set_param(gcb,'HoldOffTime',value)` to set
  **Hold off time (s)** to a specific value.

### **Frequency offset vector (Hz)** — Frequency points relative to fundamental frequency where phase noise is calculated `[30e3 100e3 1e6 3e6 10e6]` (default) | real valued vector

Frequency points relative to fundamental frequency where phase noise is calculated,
specified as a real valued vector in Hz.

#### Programmatic Use

- Use `get_param(gcb,'PhaseNoiseFreqOffset')` to view the
  current value of **Frequency offset vector (Hz)**.
- Use `set_param(gcb,'PhaseNoiseFreqOffset',value)` to set
  **Frequency offset vector (Hz)** to a specific value.

### **Specify target** — Specify target phase noise vector off (default) | on

Specify the target phase noise vector for a given frequency offset vector. By
default, this option is deselected

### **Phase noise vector (dBc/Hz)** — Target phase noise profile for given frequency offset vector `[-300 -300 -300 -300 -300]` (default) | real valued vector

Target phase noise profile for given frequency offset vector, specified as a real
valued vector in dBc/Hz. **Phase noise vector (dBc/Hz)** is the phase
noise power in a 1 Hz bandwidth centered at the specified frequency offsets relative to
the carrier.

#### Dependencies

To enable this parameter, select the **Specify target**
parameter.

#### Programmatic Use

- Use `get_param(gcb,'TargetPhaseNoise')` to view the current
  value of **Phase noise vector (dBc/Hz)**.
- Use `set_param(gcb,'TargetPhaseNoise',value)` to set
  **Phase noise vector (dBc/Hz)** to a specific value.

### **Set stop time** — Set recommended minimum simulation stop time as model stop time button

Click to set the **Recommended min. simulation stop time (s)**
reported by the Phase Noise Measurement block as the model stop
time.

### **Plot phase noise** — Plot phase noise profile of input signal button

Click to plot the measured phase noise profile of the input signal. Target phase
noise profile is also overlaid if the **Specify target** option is
selected. You can plot the phase noise profile any time during simulation.

### **Export measurement results** — Export measurement results after simulation button

Click to export measurement results to an excel spreadsheet (XLS) or as
comma-separated values (CSV) after the simulation is complete.

## Libraries

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Compute phase noise at specific frequency offset vectors

The Phase Noise Measurement block measures and plots the phase noise
profile for a time domain signal. It also displays the phase noise values for the specified
frequency offset vector on the icon of the block.
