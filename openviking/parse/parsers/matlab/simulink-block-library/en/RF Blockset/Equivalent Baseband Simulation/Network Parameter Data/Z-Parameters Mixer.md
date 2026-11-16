---
type: simulink-block
title: 'Z-Parameters Mixer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband Simulation / Cascaded Subsystems / Mixers'
documentation_page: 'zparametersmixer'
documentation_source_path: 'ref/zparametersmixer.html'
language: en
---

# Z-Parameters Mixer

## Ports

Not documented in R2025b.

## Parameters

### Main

### **Z-Parameters** — Z-parameters for nonlinear mixer `[0.0200,0;-0.0400, 0.0200]` (default) | 2-by-2-by-*M* array

Z-parameters for the nonlinear mixer, specified as a
2-by-2-by-*M* array where *M* is the number of
Z-parameters.

### **Frequency (Hz)** — Frequency of Z-parameters `2.0e9` (default) | *M*-element vector

Frequency of the Z-parameters, specified as an *M*-element vector
with each element unit in hertz. All frequencies must be positive.

### **Interpolation method** — Method to interpolate network parameters `Linear` (default) | `Spline` | `Cubic`

Method to interpolate the network parameters, specified as one of the
following:

| Method | Description |
| --- | --- |
| `Linear` | Linear interpolation |
| `Spline` | Cubic spline interpolation |
| `Cubic` | Piecewise cubic Hermite interpolation |

### **Mixer Type** — Type of mixer `Downconverter` (default) | `Upconverter`

Type of mixer, specified as `Downconverter` or
`Upconverter`.

### **LO frequency (Hz)** — Local oscillator frequency `0.9e9` (default) | *M*-element vector

Local oscillator frequency, specified as an *M*-element vector with
each element unit in hertz.

- If you choose **Mixer Type** as
  `Downconverter`, then the blockset computes the
  mixer output frequency, *fout*, from
  the mixer input frequency, *fin*,
  and the local oscillator frequency,
  *flo*, as *fout* =
  *fin* –
  *flo*.
- If you **Mixer Type** as
  `Upconverter`, then *fout* =
  *fin* +
  *flo*.

**Note**

For a downconverting mixer, the local oscillator frequency must satisfy the
condition *fin* –
*flo* ≥
1/(2*ts*), where *ts* is the sample
time specified in the Input Port block. Otherwise, an error
appears.

### Noise Data

### **Phase noise frequency offset (Hz)** — Phase noise frequency offset `[0.1 1 10 100]*1e3` (default) | numeric vector

Phase noise frequency offset, specified as a numeric vector with units in
hertz.

**Data Types:** `double`

### **Phase noise level (dBc/Hz)** — Phase noise level `[-70 -120 -140 -150]` (default) | numeric vector

Phase noise level, specified as a numeric vector with units in decibels relative to
the carrier per hertz.

**Data Types:** `double`

### **Noise type** — Type of noise data `Noise figure` (default) | `Spot noise data` | `Noise factor` | `Noise temperature`

Type of noise data, specified as one of the following:

- `Noise figure`
- `Spot noise data`
- `Noise factor`
- `Noise temperature`

This parameter is disabled if the data source contains noise data.

### **Noise figure (dB)** — Available signal-to-noise ratio at the input to available signal-to-noise ratio at the output `0` (default) | scalar ratio | vector of ratios

Available signal-to-noise ratio at the input to available signal-to-noise ratio at the
output, specified as a scalar ratio or a vector of ratios.

#### Dependencies

To enable this parameter, select `Noise figure` in
**Noise type**.

### **Minimum noise figure** — Minimum ratio of available signal-to-noise ratio at input to available signal-to-noise ratio at output `0` (default) | scalar ratio | vector of ratios

Minimum ratio of available signal-to-noise ratio at the input to available
signal-to-noise ratio at the output, specified as a scalar ratio or a vector of
ratios.

#### Dependencies

To enable this parameter, select `Spot noise data` in
**Noise type**.

### **Optimal reflection coefficient** — Optimal source impedance `1+0i` (default) | complex scalar | complex vector

Optimal source impedance, specified as a complex scalar or a complex vector.

#### Dependencies

To enable this parameter, select `Spot noise data` in
**Noise type**.

### **Equivalent normalized noise resistance** — Normalized resistance values used to take noise measurement `1` (default) | positive scalar | positive vector

Normalized resistance values used to take noise measurement, specified as a positive
scalar or a positive vector.

#### Dependencies

To enable this parameter, select `Spot noise data` in
**Noise type**.

### **Noise factor** — Ratio of available signal-to-noise power at input to available signal-to-noise power at output `1` (default) | scalar ratio | vector of ratios

Ratio of available signal-to-noise power at the input to available signal-to-noise
power at the output, specified as a scalar ratio or a vector of ratios.

#### Dependencies

To enable this parameter, select `Noise factor` in
**Noise type**.

### **Noise temperature (K)** — Equivalent temperature that produces same amount of noise as mixer `0` (default) | nonnegative scalar | nonnegative vector

Equivalent temperature that produces the same amount of noise as the mixer, specified
as a nonnegative scalar or nonnegative vector with units in kelvins.

#### Dependencies

To enable this parameter, select `Noise temperature` in
**Noise type**.

### Nonlinearity Data

### **IP3 type** — Type of third order intercept `OIP3` (default) | `IIP3`

Type of third order intercept, specified as `OIP3` (output intercept
point) or `IIP3` (input intercept point). This parameter is disabled if
the data source contains power data or IP3 data.

### **IP3 (dBm)** — IP3 value `inf` (default) | scalar | vector

IP3 value, specified as a scalar in dBm for frequency independent nonlinear data or a
vector with each element unit in dBm for frequency dependent nonlinear data. This
parameter is disabled if the data source contains power data or IP3 data.

### **1dB gain compression power (dBm)** — Output power value at which gain has decreased by 1 dB `inf` (default) | scalar | vector

Output power value (P1dB,out) at which the gain has decreased by 1 dB, specified as a scalar in dBm
for frequency independent nonlinear data or vector with each element unit in dBm for
frequency dependent nonlinear data. This parameter is disabled if the data source
contains power data or IP3 data.

### **Output saturation power (dBm)** — Output power value that mixer produces when fully saturated `inf` (default) | scalar | vector

Output power value (Psat,out) that the mixer produces when fully saturated, specified as a scalar
in dBm for frequency independent nonlinear data or a vector with each element unit in
dBm for frequency dependent nonlinear data. This parameter is disabled if the data
source contains output saturation power data.

### **Gain compression at saturation (dB)** — Decrease in gain value `3` (default) | scalar | vector

Decrease in gain value (GCsat) when the power is fully saturated, specified as a scalar in dB for
frequency independent nonlinear data or a vector with each element unit in dB for
frequency dependent nonlinear data.

### Visualization

### **Source of frequency data** — Frequency data source `Same as the Z-Parameters` (default) | `User-specified`

Frequency data source, specified as `Same as the
Z-Parameters` or `User-specified`.

### **Frequency data (Hz)** — Frequency data range `[1e9:1e8:2.9e9]` (default) | vector

Frequency data range, specified as a vector with each element unit in hertz.

#### Dependencies

To enable this parameter, set **Source of frequency data** to
`User specified`.

### **Reference impedance (ohms)** — Reference impedance `50` (default) | nonnegative scalar

Reference impedance, specified as a nonnegative scalar in ohms.

### **Plot type** — Type of data plot `X-Y plane` (default) | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

Type of data plot to visualize using the given data, specified as one of the
following:

- `X-Y plane` — Generate a Cartesian plot of the
  data versus frequency. To create linear, semilog, or log-log plots, set the
  **Y-axis scale** and **X-axis scale**
  accordingly.
- `Composite data` — Plot the composite data.
  For more information, see Create Plots Using Equivalent Baseband Library Blocks.
- `Polar plane` — Generate a polar plot of the
  data. The block plots only the range of data corresponding to the specified
  frequencies.
- `Z smith chart`, `Y smith
  chart`, and `ZY smith chart` —
  Generate a Smith® chart. The block
  plots only the range of data corresponding to the specified frequencies.

### **Y parameter1** — Type of parameters to plot `S11` (default) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | `NFactor` | `NTemp` | `PhaseNoise` | ...

Type of parameters to plot based on the **Plot type** you set,
specified as one of the following.

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`, `S12`, `S21`, `S22`, `GroupDelay`, `OIP3`, `NF`, `NFactor`, `NTemp`, and `PhaseNoise`. |
| `Composite data` | No **Y parameter1** to set. |
| `Polar plane` | `S11`, `S12`, `S21`, and `S22` |
| `Z Smith chart` | `S11` and `S22`. |
| `Y Smith chart` | `S11` and `S22`. |
| `ZY smith chart` | `S11` and `S22`. |

### **Y parameter2** — Type of parameters to plot `S11` | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | `NFactor` | `NTemp` | ...

Type of parameters to plot based on the **Plot type** you set,
specified as one of the following.

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`, `S12`, `S21`, `S22`, `GroupDelay`, `OIP3`, `NF`, `NFactor`, `NTemp`, and `PhaseNoise`. |
| `Composite data` | No **Y parameter1** to set. |
| `Polar plane` | `S11`, `S12`, `S21`, and `S22` |
| `Z Smith chart` | `S11` and `S22`. |
| `Y Smith chart` | `S11` and `S22`. |
| `ZY smith chart` | `S11` and `S22`. |

### **Y format1** — Plot format `Magnitude (decibels)` (default) | `Magnitude (linear)` | `Angle(degrees)` | `Angle(radians)` | `Real` | `Imaginary`

Plot format, specified as one of the following.

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`, `S12`, `S21`, and `S22`. | `Magnitude (decibels)`, `Magnitude (linear)`, `Angle(degrees)`, `Angle(radians)`, `Real`, and `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, and `ps`. |
| `OIP3` | `dB`, `dBm`, `W`, and `mW`. |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |
| `PhaseNoise` | `dBc/Hz` |

#### Dependencies

To enable **Y format1**, set **Plot type** to
`X-Y plane`.

### **Y format2** — Plot format `Magnitude (decibels)` (default) | `Magnitude (linear)` | `Angle(degrees)` | `Angle(radians)` | `Real` | `Imaginary`

Plot format, specified as one of the following.

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`, `S12`, `S21`, and `S22`. | `Magnitude (decibels)`, `Magnitude (linear)`, `Angle(degrees)`, `Angle(radians)`, `Real`, and `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, and `ps`. |
| `OIP3` | `dB`, `dBm`, `W`, and `mW`. |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |
| `PhaseNoise` | `dBc/Hz` |

#### Dependencies

To enable **Y format1**, set **Plot type** to
`X-Y plane`.

### **X parameter** — Frequency plot `Freq` (default)

Frequency plot, specified as `Freq`.

### **X format** — Frequency plot format `Hz` (default) | `Auto` | `kHz` | `MHz` | `GHz` | `THz`

Frequency plot format, specified as one of the following.

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y scale** — Y-axis scale `Linear` (default) | `Log`

Y-axis scale, specified as `Linear` or `Log`.

#### Dependencies

To enable this parameter, set **Plot type** to `X-Y
plane`.

### **X scale** — X-axis scale `Linear` (default) | `Log`

X-axis scale, specified as `Linear` or `Log`.

#### Dependencies

To enable this parameter, set **Plot type** to `X-Y
plane`.

### **Plot** — Plot specified data button

Plot specified data using the plot button.

## Libraries

RF Blockset / Equivalent Baseband / Mixers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Model mixer and local oscillator using Z-parameters

The Z-Parameters Mixer block models the nonlinear mixer described in the
block dialog box in terms of its frequency-dependent Z-parameters, the frequencies of the
Z-parameters, noise data (including phase noise data), and nonlinearity data.
