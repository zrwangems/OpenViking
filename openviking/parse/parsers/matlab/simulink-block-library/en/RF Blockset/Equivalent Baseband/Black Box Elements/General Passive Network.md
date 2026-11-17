---
type: simulink-block
title: 'General Passive Network'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Black Box Elements'
documentation_page: 'generalpassivenetwork'
documentation_source_path: 'ref/generalpassivenetwork.html'
language: en
---

# General Passive Network

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Data source
  summary: Data source that describes the passive device behaviour Data file (default) | RFDATA object
  group: Main
- name: Data file
  summary: Name of file that contains passive device data passive.s2p (default) | string | character vector
  group: Main
- name: RFDATA object
  summary: RF data object that contains passive device data read(rfdata.data, 'passive.s2p') (default) | rfdata.data object
  group: Main
- name: Interpolation method
  summary: Method to interpolate network parameters Linear (default) | Spline | Cubic
  group: Main
- name: Source of frequency data
  summary: Frequency data source Extracted from data source (default) | User-specified
  group: Visualization
- name: Frequency data
  summary: Frequency data range [0.3e6:1e:6e9] (default) | vector
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

### **Data source** — Data source that describes the passive device behaviour `Data file` (default) | `RFDATA` object

Data source that describes the passive device behaviour, specified as
a `Data file` or an `RFDATA` object.
The data source must contain network parameters and may also include
noise data, nonlinearity data, or both.

### **Data file** — Name of file that contains passive device data `passive.s2p` (default) | string | character vector

Name of file that contains the passive device data, specified as a
string or a character vector. The file name must include the extension.
If the file is not in your MATLAB® path, specify the full path to the file or click the
**Browse** button to find the file.

#### Dependencies

To enable this parameter, choose `Data
file` in **Data source**.

### **RFDATA object** — RF data object that contains passive device data `read(rfdata.data, 'passive.s2p')` (default) | `rfdata.data` object

RF data object that contains passive device data, specified as an
RF Toolbox
`rfdata.data` object. You can also use an expression such as
the default value to create an `rfdata.data` object
from an `.s2p` file.

### **Interpolation method** — Method to interpolate network parameters `Linear` (default) | `Spline` | `Cubic`

Method to interpolate the network parameters, specified as one of the
following:

| Method | Description |
| --- | --- |
| `Linear` | Linear interpolation |
| `Spline` | Cubic spline interpolation |
| `Cubic` | Piecewise cubic Hermite interpolation |

### Visualization

### **Source of frequency data** — Frequency data source `Extracted from data source` (default) | `User-specified`

Frequency data source, specified as `Extracted from data
source` or `User-specified`.

### **Frequency data** — Frequency data range `[0.3e6:1e:6e9]` (default) | vector

Frequency data range, specified as a vector with each element unit in
hertz.

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

RF Blockset / Equivalent Baseband / Black Box Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Model two-port passive network described by rfdata object

The General Passive Network block models the two-port passive network
described by an RF Toolbox™ data (`rfdata.data`)
object.

If network parameter data and their corresponding frequencies exist as S-parameters in
the `rfdata.data` object, the General Passive Network
block interpolates the S-parameters to determine their values at the modeling
frequencies. If the block contains network Y- or Z-parameters, the block first converts
them to S-parameters. See Map Network Parameters to Modeling Frequencies for more details.

To learn how you can use General Passive Network block to model 2-port
bandpass filter, see *Import Data Files into RF Blocks* section of
Specify or Import Component Data example.
