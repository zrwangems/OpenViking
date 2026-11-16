---
type: simulink-block
title: 'PLL Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Measurements & Testbenches'
documentation_page: 'plltestbench'
documentation_source_path: 'ref/plltestbench.html'
language: en
---

# PLL Testbench

## Ports

### Input

### **from pll** — Input clock signal scalar

Input clock signal to the PLL Testbench, specified as a scalar. The
**from pll** port is connected to the output of a PLL
system.

**Data Types:** `double`
### Output

### **to pll** — Output clock signal scalar

Output clock signal, returned as a sine or square wave as specified in the
**Signal type** parameter. The signal at the **to
pll** port provides the stimulus to a PLL system.

**Data Types:** `double`

## Parameters

### **Set stop time** — Set recommended minimum simulation stop time as model stop time button

Click to set the **Recommended min. simulation stop time (s)**
reported by the PLL Testbench block as the model stop time.

#### Dependencies

This button is only available when **Phase noise** measurement
option is selected in the **Setup** tab.

### **Plot phase noise profile** — Plot phase noise profile of the PLL DUT button

Click to plot the phase noise profile of the PLL device (DUT) and to compare it with
the user-defined phase noise profile after simulation is complete.

#### Dependencies

This button is only available when **Phase noise** measurement
option is selected in the **Setup** tab.

### **Export measurement results** — Export measurement results after simulation button

Click to export measurement results to an excel spreadsheet (XLS) or as
comma-separated values (CSV) after the simulation is complete.

### Stimulus

### **Amplitude (V)** — Maximum value of stimulus signal at PLL input `1` (default) | real positive scalar

Maximum value of the stimulus signal at PLL input, specified as a real positive
scalar.

#### Programmatic Use

- Use `get_param(gcb,'InputAmplitude')` to view the current
  value of **Amplitude (V)**.
- Use `set_param(gcb,'InputAmplitude',value)` to set
  **Amplitude (V)** to a specific value.

### **Frequency (Hz)** — Frequency of stimulus signal at PLL input `30e6` (default) | real positive scalar

Frequency of the stimulus signal at PLL input, specified as a real positive
scalar.

#### Programmatic Use

- Use `get_param(gcb,'Fo')` to view the current value of
  **Frequency (Hz)**.
- Use `set_param(gcb,'Fo',value)` to set
  **Frequency (Hz)** to a specific value.

### **Add phase noise** — Add phase noise as function of frequency off (default) | on

Select to introduce phase noise as a function of frequency. By default, this
option is deselected.

### **Phase noise frequency offset (Hz)** — Frequency offsets of phase noise from carrier frequency `[500 1e3 10e3 100e3]` (default) | real valued vector

Frequency offsets of the phase noise from the carrier frequency, specified as a
real valued vector in Hz.

#### Dependencies

To enable this parameter, select **Add phase noise** in the
**Stimulus** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Foffset` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[500 1e3 10e3 100e3]` |

**Data Types:** `double`

### **Phase noise level (dBc/Hz)** — Phase noise power at specified frequency offsets relative to the carrier `[-115 -122 -142 -161]` (default) | real valued vector

Real valued vector specifying the phase noise power in a 1 Hz bandwidth centered
at the specified frequency offsets relative to the carrier. The value is specified in
dBc/Hz.

#### Dependencies

To enable this parameter, select **Add phase noise** in the
**Stimulus** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PhaseNoise` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[-115 -122 -142 -161]` |

**Data Types:** `double`

### **Estimate phase noise parameters** — Automatically estimate phase noise parameters on (default) | off

Select to automatically estimate the phase noise parameters. By default, this
option is selected.

You can deselect this option to define custom period jitter and flicker corner
frequency.

#### Dependencies

To enable this parameter, select **Add phase noise** in the
**Stimulus** tab.

**Data Types:** `double`

### **Period jitter (S)** — Standard deviation of period jitter `4.8666e-15` (default) | positive real scalar

Standard deviation of the period jitter, specified as a positive real scalar in
seconds. Period jitter is the deviation in cycle time of a clock signal with respect
to the ideal period.

To enable this parameter, select **Add phase noise** and deselect
**Estimate phase noise parameters** in the
**Stimulus** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PeriodJitter` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `4.8666e-15` |

**Data Types:** `double`

### **Flicker corner frequency (Hz)** — Corner frequency of flicker noise `517103.8168` (default) | scalar

Corner frequency of the flicker noise, specified as a scalar in hertz.
**Flicker corner frequency (Hz)** is defined as the frequency at
which the phase noise transitions from
1/*f*2 to
1/*f*3 due to flicker noise. At this
frequency, the spectral densities of period jitter and flicker noise are equal.

#### Dependencies

To enable this parameter, select **Add phase noise** and
deselect **Estimate phase noise parameters** in the
**Stimulus** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CornerFrequency` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `517103.8168` |

**Data Types:** `double`

### **Plot fit** — Plot specified and expected output phase noise density button

Click to plot the specified phase noise density and realizable expected output
phase noise density.

### Setup

### **Frequency of operation** — Measure operating frequency of PLL DUT on (default) | off

Select to measure the operating frequency of the PLL DUT. By default, this option
is selected.

### **Lock time** — Measure locking time of PLL DUT off (default) | on

Select to measure the locking time of the PLL DUT with user-specified error
tolerance. By default, this option is deselected.

### **Target frequency of operation (Hz)** — Target operating frequency of PLL DUT to calculate lock time `2.1e9` (default) | real positive scalar

Target operating frequency of the PLL DUT to calculate the lock time of the PLL,
specified as a real positive scalar in Hz.

#### Dependencies

To enable this parameter, select the **Lock time** measurement
option in the **Setup** tab.

#### Programmatic Use

- Use `get_param(gcb,'ExpectedFreq')` to view the current
  value of **Target frequency of operation(Hz)**.
- Use `set_param(gcb,'ExpectedFreq',value)` to set
  **Target frequency of operation (Hz)** to a specific
  value.

### **Error tolerance (Hz)** — Error tolerance for lock time measurement `1e6` (default) | real positive scalar

Error tolerance for lock time measurement, specified as a real positive scalar in
Hz.

#### Dependencies

To enable this parameter, select the **Lock time** measurement
option in the **Setup** tab.

#### Programmatic Use

- Use `get_param(gcb,'FreqErrorTol')` to view the current
  value of **Error tolerance (Hz)**.
- Use `set_param(gcb,'FreqErrorTol',value)` to set
  **Error tolerance (Hz)** to a specific value.

### **Phase noise** — Measure phase noise level of PLL DUT off (default) | on

Select to measure the phase noise level of the PLL DUT at user defined frequency
offset points. By default, this option is deselected.

### **Resolution bandwidth (Hz)** — Smallest positive frequency that can be resolved `200e3` (default) | real positive scalar

Smallest positive frequency that can be resolved, specified as a real positive
scalar. The **Resolution bandwidth (Hz)** is used to determine window
length for spectral analysis using the Welch method. For more information, see Welch's Method of Averaged Modified Periodograms.

In general, **Resolution bandwidth (Hz)** should be less than or
equal to the lowest offset frequency value.

#### Dependencies

To enable this parameter, select the **Phase noise**
measurement option in the **Setup** tab.

#### Programmatic Use

- Use `get_param(gcb,'ResBandwidth')` to view the current
  value of **Resolution bandwidth (Hz)**.
- Use `set_param(gcb,'ResBandwidth',value)` to set
  **Resolution bandwidth (Hz)** to a specific value.

### **No. of spectral averages** — Number of spectral averages `4` (default) | positive integer scalar

Number of spectral averages, specified as a positive integer scalar. The `dsp.SpectrumEstimator`
System object™ used by the Phase Noise Measurement subsystem inside the PLL
Testbench block computes the current power spectrum or power density
spectrum estimate by averaging over the number specified by **No. of spectral
averages**.

#### Dependencies

To enable this parameter, select the **Phase noise**
measurement option in the **Setup** tab.

#### Programmatic Use

- Use `get_param(gcb,'SpectralAverages')` to view the
  current value of **No. of spectral averages**.
- Use `set_param(gcb,'SpectralAverages',value)` to set
  **No. of spectral averages** to a specific value.

### **Hold off time (s)** — Delays measurement analysis to avoid transients `0` (default) | real nonnegative scalar

Delays measurement analysis by the specified amount of time to avoid corruption by
transients, specified as a real nonnegative scalar in s.

To enable this parameter, select the **Phase noise** measurement
option in the **Setup** tab.

#### Programmatic Use

- Use `get_param(gcb,'HoldOffTime')` to view the current
  value of **Hold off time (s)**.
- Use `set_param(gcb,'HoldOffTime',value)` to set
  **Hold off time (s)** to a specific value.

### **Frequency offset vector (Hz)** — Frequency points relative to fundamental frequency where phase noise is calculated `[300e3 1e6 3e6 10e6]` (default) | real valued vector

Frequency points relative to fundamental frequency where phase noise is
calculated, specified as a real valued vector in Hz. This values are also reported in
the **Target Metrics** tab as **Phase noise frequency offset
(Hz)**.

To enable this parameter, select the **Phase noise** measurement
option in the **Setup** tab.

#### Programmatic Use

- Use `get_param(gcb,'PhaseNoiseFreqOffset')` to view the
  current value of **Frequency offset vector (Hz)**.
- Use `set_param(gcb,'PhaseNoiseFreqOffset',value)` to set
  **Frequency offset vector (Hz)** to a specific value.

### Target Metrics

### **Frequency of operation** — Target operating frequency at which PLL needs to lock `2.1e9` (default) | real positive scalar

Target operating frequency at which PLL DUT needs to lock, specified as a real
positive scalar in Hz.

If you select the **Lock time** as a measurement option, the
**Frequency of operation** is reported from the **Target
frequency of operation (Hz)** parameter.

#### Dependencies

To enable this parameter, select the **Frequency of operation**
measurement option in the **Setup** tab.

#### Programmatic Use

- Use `get_param(gcb,'TargetFreq')` to view the current
  value of **Frequency of operation**.
- Use `set_param(gcb,'TargetFreq',value)` to set
  **Frequency of operation** to a specific value.

### **Lock time (s)** — Maximum time in which PLL DUT needs to get locked `3e-6` (default) | real nonnegative scalar

Maximum time in which PLL DUT needs to get locked, specified as a real nonnegative
scalar in s.

#### Dependencies

To enable this parameter, select the **Lock time** measurement
option in the **Setup** tab.

#### Programmatic Use

- Use `get_param(gcb,'TargetLockTime')` to view the current
  value of **Lock time**.
- Use `set_param(gcb,'TargetLockTime',value)` to set
  **Lock time** to a specific value.

### **Phase noise (dBc/Hz)** — Target noise power corresponding to frequency offset vector `[-85,-125,-150,-180]` (default) | real valued vector

Target noise power level relative to the carrier in a 1 Hz frequency bandwidth
centered at the frequencies specified in the **Frequency offset vector
(Hz)** parameter, specified as a real valued vector in dBc/Hz.

#### Dependencies

To enable this parameter, select the **Phase noise**
measurement option in the **Setup** tab.

#### Programmatic Use

- Use `get_param(gcb,'TargetPhaseNoiseVector')` to view the
  current value of **Phase noise**.
- Use `set_param(gcb,'TargetPhaseNoiseVector',value)` to
  set **Phase noise** to a specific value.

## Libraries

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Validate PLL system by measuring operating frequency, lock time, and phase noise

The PLL Testbench block provides input stimulus in the form of a clock
signal to a phase-locked loop (PLL) system. The testbench also validates the performance of
the PLL system by comparing the operating frequency, lock time, and phase noise against the
target metrics.

The PLL Testbench block generates the stimulus to drive the device under
test (DUT) from the **Stimulus** tab. The setup parameters for validating the
DUT are defined in the **Setup** tab and the target validation metrics are
defined in the **Target Metric** tab.
