---
type: simulink-block
title: 'Y-Parameters Passive Network'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Black Box Elements'
documentation_page: 'yparameterspassivenetwork'
documentation_source_path: 'ref/yparameterspassivenetwork.html'
language: en
---

# Y-Parameters Passive Network

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Y-Parameters
  summary: Y-parameters for two-port passive network [0.0200,0;-0.0400, 0.0200] (default) | 2-by-2-by-*M* array
  group: Main
- name: Frequency (Hz)
  summary: Frequency of Y-parameters 2.0e9 (default) | *M*-element vector
  group: Main
- name: Interpolation method
  summary: Method to interpolate network parameters Linear (default) | Spline | Cubic
  group: Main
- name: Source of frequency data
  summary: Frequency data source Same as the Y-Parameters (default) | User-specified
  group: Visualization
- name: Frequency data (Hz)
  summary: Frequency data range [1.9e9:1.0e6:2.2e9] (default) | vector
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

### **Y-Parameters** — Y-parameters for two-port passive network `[0.0200,0;-0.0400, 0.0200]` (default) | 2-by-2-by-*M* array

Y-parameters for a two-port passive network, specified as a
2-by-2-by-*M* array where *M* is
the number of Y-parameters.

### **Frequency (Hz)** — Frequency of Y-parameters `2.0e9` (default) | *M*-element vector

Frequency of Y-parameters, specified as an
*M*-element vector with each element unit in hertz. All
frequencies must be positive.

### **Interpolation method** — Method to interpolate network parameters `Linear` (default) | `Spline` | `Cubic`

Method to interpolate the network parameters, specified as one of the
following:

| Method | Description |
| --- | --- |
| `Linear` | Linear interpolation |
| `Spline` | Cubic spline interpolation |
| `Cubic` | Piecewise cubic Hermite interpolation |

### Visualization

### **Source of frequency data** — Frequency data source `Same as the Y-Parameters` (default) | `User-specified`

Frequency data source, specified as `Same as the
Y-Parameters` or `User-specified`.

### **Frequency data (Hz)** — Frequency data range `[1.9e9:1.0e6:2.2e9]` (default) | vector

Frequency data range, specified as a vector with each element unit in hertz.

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

RF Blockset / Equivalent Baseband / Black Box Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Model passive network using Y-parameters

The Y-Parameters Passive Network block models the two-port passive
network described in the block dialog box, in terms of its Y-parameters and their
associated frequencies.

In the **Y-Parameters** field of the block dialog box, provide the
Y-parameters for each of the *M* frequencies as a
2-by-2-by-*M* array. In the **Frequency** field,
specify the frequencies for the Y-parameters as an *M*-element vector.
The elements of the vector must be in the same order as the Y-parameters. The figure
shows the correspondence between the Y-parameters array and the vector of frequencies.

Y-parameters array vs vector of frequencies

The Y-Parameters Passive Network block uses the RF Toolbox™
`y2s` function to convert the Y-parameters
to S-parameters, and then interpolates the resulting S-parameters to determine their
values at the modeling frequencies. The modeling frequencies are determined by the
Output Port block. See Map Network Parameters to Modeling Frequencies
for more details.
