---
type: simulink-block
title: 'Y-Parameters Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Amplifiers'
documentation_page: 'yparametersamplifier'
documentation_source_path: 'ref/yparametersamplifier.html'
language: en
---

# Y-Parameters Amplifier

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Y-Parameters
  summary: Y-parameters for nonlinear amplifier [0.0200,0;-0.0400, 0.0200] (default) | 2-by-2-by-*M* array
  group: Main
- name: Frequency (Hz)
  summary: Frequency of Y-parameters 2.0e9 (default) | *M*-element vector
  group: Main
- name: Interpolation method
  summary: Method to interpolate network parameters Linear (default) | Spline | Cubic
  group: Main
- name: Noise type
  summary: Type of noise data Noise figure (default) | Spot noise data | Noise factor | Noise temperature
  group: Noise Data
- name: Noise figure (dB)
  summary: Available signal-to-noise ratio at the input to available signal-to-noise ratio at the output 0 (default) | scalar
    ratio | vector of ratios
  group: Noise Data
- name: Minimum noise figure
  summary: Minimum ratio of available signal-to-noise ratio at input to available signal-to-noise ratio at output 0 (default)
    | scalar ratio | vector of ratios
  group: Noise Data
- name: Optimal reflection coefficient
  summary: Optimal source impedance 1+0i (default) | complex scalar | complex vector
  group: Noise Data
- name: Equivalent normalized noise resistance
  summary: Normalized resistance values used to take noise measurement 1 (default) | positive scalar | positive vector
  group: Noise Data
- name: Noise factor
  summary: Ratio of available signal-to-noise power at input to available signal-to-noise power at output 1 (default) | scalar
    ratio | vector of ratios
  group: Noise Data
- name: Noise temperature (K)
  summary: Equivalent temperature that produces the same amount of noise as amplifier 0 (default) | nonnegative scalar | nonnegative
    vector
  group: Noise Data
- name: Frequency (Hz)
  summary: Domain of frequencies to express noise data 2.0e9 (default) | nonnegative scalar | nonnegative vector
  group: Noise Data
- name: IP3 type
  summary: Type of third order intercept OIP3 (default) | IIP3
  group: Nonlinearity Data
- name: IP3 (dBm)
  summary: IP3 value inf (default) | scalar | vector
  group: Nonlinearity Data
- name: 1dB gain compression power (dBm)
  summary: Output power value at which gain has decreased by 1 dB inf (default) | scalar | vector
  group: Nonlinearity Data
- name: Output saturation power (dBm)
  summary: Output power value that amplifier produces when fully saturated inf (default) | scalar | vector
  group: Nonlinearity Data
- name: Gain compression at saturation (dB)
  summary: Decrease in gain value 3 (default) | scalar | vector
  group: Nonlinearity Data
- name: Frequency (Hz)
  summary: Frequency points corresponding to third-order intercept or power data 2.0e9 (default) | positive scalar | positive
    vector
  group: Nonlinearity Data
- name: Source of frequency data
  summary: Frequency data source Same as the Y-Parameters (default) | User-specified
  group: Visualization
- name: Frequency data (Hz)
  summary: Frequency data range [1.9e9:1.0e8:2.2e9] (default) | vector
  group: Visualization
- name: Reference impedance (ohms)
  summary: Reference impedance 50 (default) | nonnegative scalar
  group: Visualization
- name: Plot type
  summary: Type of data plot X-Y plane (default) | Composite data | Polar plane | Z Smith chart | Y Smith chart | ZY Smith
    chart
  group: Visualization
- name: Y parameter1
  summary: Type of parameters to plot S11 (default) | S12 | S21 | S22 | GroupDelay | OIP3 | IIP3 | NF | ...
  group: Visualization
- name: Y parameter2
  summary: Type of parameters to plot S11 (default) | S12 | S21 | S22 | GroupDelay | OIP3 | IIP3 | NF | ...
  group: Visualization
- name: Y format1
  summary: Plot format Magnitude (decibels) (default) | Mag | Magnitude (linear) | Angle | Real | Imaginary | ...
  group: Visualization
- name: Y format2
  summary: Plot format Magnitude (decibels) (default) | Mag | Magnitude (linear) | Angle | Real | Imaginary | ...
  group: Visualization
- name: X parameter
  summary: Frequency plot Freq (default)
  group: Visualization
- name: X format
  summary: Frequency plot format Hz (default) | Auto | kHz | MHz | GHz | THz
  group: Visualization
- name: Y scale
  summary: Y-axis scale Linear (default) | Log
  group: Visualization
- name: X scale
  summary: X-axis scale Linear (default) | Log
  group: Visualization
- name: Plot
  summary: Plot specified data button
  group: Visualization
```

### Main

### **Y-Parameters** — Y-parameters for nonlinear amplifier `[0.0200,0;-0.0400, 0.0200]` (default) | 2-by-2-by-*M* array

Y-parameters for a nonlinear amplifier, specified as a
2-by-2-by-*M* array where *M* is
the number of Y-parameters.

### **Frequency (Hz)** — Frequency of Y-parameters `2.0e9` (default) | *M*-element vector

Frequency of Y-parameters, specified as an
*M*-element vector with each element unit in
hertz.

### **Interpolation method** — Method to interpolate network parameters `Linear` (default) | `Spline` | `Cubic`

Method to interpolate the network parameters, specified as one of the
following:

| Method | Description |
| --- | --- |
| `Linear` | Linear interpolation |
| `Spline` | Cubic spline interpolation |
| `Cubic` | Piecewise cubic Hermite interpolation |

### Noise Data

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

### **Noise temperature (K)** — Equivalent temperature that produces the same amount of noise as amplifier `0` (default) | nonnegative scalar | nonnegative vector

Equivalent temperature that produces the same amount of noise as the amplifier,
specified as a nonnegative scalar in kelvins or nonnegative vector with each element
unit in kelvins.

#### Dependencies

To enable this parameter, select `Noise temperature` in
**Noise type**.

### **Frequency (Hz)** — Domain of frequencies to express noise data `2.0e9` (default) | nonnegative scalar | nonnegative vector

Domain of frequencies to express noise data, specified as a nonnegative scalar in
hertz or nonnegative vector with each element unit in hertz. If you provide a scalar
value for your noise data, the block ignores the **Frequency (Hz)**
parameter and uses the same noise data for all frequencies. If you provide a vector of
values for your noise data, it must be the same size as the vector of frequencies. The
block uses the **Interpolation method** specified in the
**Main** tab to interpolate noise data.

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

### **Output saturation power (dBm)** — Output power value that amplifier produces when fully saturated `inf` (default) | scalar | vector

Output power value (Psat,out) that the amplifier produces when fully saturated, specified as a
scalar in dBm for frequency independent nonlinear data or a vector with each element
unit in dBm for frequency dependent nonlinear data. This parameter is disabled if the
data source contains output saturation power data.

### **Gain compression at saturation (dB)** — Decrease in gain value `3` (default) | scalar | vector

Decrease in gain value (GCsat) when the power is fully saturated, specified as a scalar in dB for
frequency independent nonlinear data or a vector with each element unit in dB for
frequency dependent nonlinear data.

### **Frequency (Hz)** — Frequency points corresponding to third-order intercept or power data `2.0e9` (default) | positive scalar | positive vector

Frequency points corresponding to third-order intercept or power data, specified as a
positive scalar or positive vector in units of hertz. This parameter is disabled if the
data source contains power data or IP3 data.

#### Dependencies

- If you specify the frequency as a scalar, then the **IP3
  (dBm)**, **1 dB gain compression power
  (dBm)**, and **Output saturation power
  (dBm)** parameters must all be scalars.
- If you specify the frequency as a vector, then or more of the
  **IP3 (dBm)**, **1 dB gain compression
  power (dBm)**, and **Output saturation power
  (dBm)** parameters must also be a vector.

### Visualization

### **Source of frequency data** — Frequency data source `Same as the Y-Parameters` (default) | `User-specified`

Frequency data source, specified as `Same as the
Y-Parameters` or `User-specified`.

### **Frequency data (Hz)** — Frequency data range `[1.9e9:1.0e8:2.2e9]` (default) | vector

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

### **Y parameter1** — Type of parameters to plot `S11` (default) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

Type of parameters to plot, specified as one of the following:

|  |  |  |  |
| --- | --- | --- | --- |
| `S11` | `S12` | `S21` | `S22` |
| `GroupDelay` | `GammaIn` | `GammaOut` | `VSWRIn` |
| `VSWROut` | `OIP3` | `IIP3` | `NF` |
| `NFactor` | `NTemp` | `TF1` | `TF2` |
| `TF3` | `Gt` | `Ga` | `Gp` |
| `Gmag` | `Gmsg` | `GammaMS` | `GammaML` |
| `K` | `Delta` | `Mu` | `MuPrime` |

**Note**

**Y parameter1** is disabled when you select **Plot
type** to `Composite data`.

### **Y parameter2** — Type of parameters to plot `S11` (default) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

Type of parameters to plot, specified as one of the following:

|  |  |  |  |
| --- | --- | --- | --- |
| `S11` | `S12` | `S21` | `S22` |
| `GroupDelay` | `GammaIn` | `GammaOut` | `VSWRIn` |
| `VSWROut` | `OIP3` | `IIP3` | `NF` |
| `NFactor` | `NTemp` | `TF1` | `TF2` |
| `TF3` | `Gt` | `Ga` | `Gp` |
| `Gmag` | `Gmsg` | `GammaMS` | `GammaML` |
| `K` | `Delta` | `Mu` | `MuPrime` |

**Note**

**Y parameter2** is disabled when you select **Plot
type** to `Composite data`.

### **Y format1** — Plot format `Magnitude (decibels)` (default) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

Plot format, specified as one of the following.

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`, `S12`, `S21`, `S22`, `GammaIn`, `GammaOut`, `TF1`, `TF2`, `TF3`, `GammaMS`, `GammaML`, and `Delta`. | `dB`, `Magnitude (decibels)`, `Abs`, `Mag`, `Magnitude (linear)`, `Angle`, `Angle(degrees)`, `Angle(radians)`, `Real`, `Imag`, and `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, and `ps`. |
| `VSWRIn` and `VSWROut`. | `Magnitude (decibels)` and `None`. |
| `OIP3` and `IIP3`. | `dBm`, `W`, and `mW`. |
| `NF` | `dB` and `Magnitude (decibels)`. |
| `NFactor`, `K`, `Mu`, and `MuPrime`. | `None` |
| `NTemp` | `Kelvin` |
| `Gt`, `Ga`, `Gp`, `Gmag`, and `Gmsg`. | `dB`, `Magnitude (decibels)`, and `None`. |

#### Dependencies

To enable **Y format1**, set **Plot type** to
`X-Y plane`.

### **Y format2** — Plot format `Magnitude (decibels)` (default) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

Plot format, specified as one of the following.

| Y parameter2 | Y format2 |
| --- | --- |
| `S11`, `S12`, `S21`, `S22`, `GammaIn`, `GammaOut`, `TF1`, `TF2`, `TF3`, `GammaMS`, `GammaML`, and `Delta`. | `dB`, `Magnitude (decibels)`, `Abs`, `Mag`, `Magnitude (linear)`, `Angle`, `Angle(degrees)`, `Angle(radians)`, `Real`, `Imag`, and `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, and `ps`. |
| `VSWRIn` and `VSWROut`. | `Magnitude (decibels)` and `None`. |
| `OIP3` and `IIP3`. | `dBm`, `W`, and `mW`. |
| `NF` | `dB` and `Magnitude (decibels)`. |
| `NFactor`, `K`, `Mu`, and `MuPrime`. | `None` |
| `NTemp` | `Kelvin` |
| `Gt`, `Ga`, `Gp`, `Gmag`, and `Gmsg`. | `dB`, `Magnitude (decibels)`, and `None`. |

#### Dependencies

To enable **Y format2**, set **Plot type** to
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

RF Blockset / Equivalent Baseband / Amplifiers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Model nonlinear amplifier using Y-parameters

The Y-Parameters Amplifier block models the nonlinear amplifier
described in the block dialog box, in terms of its frequency-dependent Y-parameters, the
frequencies of the Y-parameters, noise data, and nonlinearity data
