---
type: simulink-block
title: 'Parallel-Plate Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Transmission Lines'
documentation_page: 'parallelplatetransmissionline'
documentation_source_path: 'ref/parallelplatetransmissionline.html'
language: en
---

# Parallel-Plate Transmission Line

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Plate width (m)
  summary: Width of parallel-plate transmission line 5e-3 (default) | scalar
  group: ''
- name: Plate separation (m)
  summary: Dielectric spacing in parallel-plate transmission line 1e-3 (default) | scalar
  group: ''
- name: Relative permeability constant
  summary: Relative permeability of the dielectric material in the parallel-plate transmission line 1 (default) | scalar
  group: ''
- name: Relative permittivity constant
  summary: Relative permittivity of the dielectric material in the parallel-plate transmission line 2.3 (default) | scalar
  group: ''
- name: Loss tangent of dielectric
  summary: Loss tangent of dielectric in the parallel-plate transmission line 0 (default) | scalar
  group: ''
- name: Conductivity of the conductor (S/m)
  summary: Conductivity of conductor inf (default) | scalar
  group: ''
- name: Transmission line length(m)
  summary: Physical length of the transmission line 0.01 (default) | positive scalar
  group: ''
- name: Stub mode
  summary: Type of stub Not a stub (default) | Shunt | Series
  group: ''
- name: Termination of stub
  summary: Stub termination Open (default)
  group: ''
- name: Source of frequency data
  summary: Frequency data source User-specified (default)
  group: ''
- name: Frequency data (Hz)
  summary: Frequency data range [1e9:1e6:3e9] (default) | vector
  group: ''
- name: Reference impedance (ohms)
  summary: Reference impedance 50 (default) | nonnegative scalar
  group: ''
- name: Plot type
  summary: Type of data plot X-Y plane (default) | Composite data | Polar plane | Z Smith chart | Y Smith chart | ZY Smith
    chart
  group: ''
- name: Y parameter1
  summary: Type of parameters to plot S11 (default) | S12 | S21 | S22 | GroupDelay | OIP3 | IIP3 | NF | ...
  group: ''
- name: Y parameter2
  summary: Type of parameters to plot S11 (default) | S12 | S21 | S22 | GroupDelay | OIP3 | IIP3 | NF | ...
  group: ''
- name: Y format1
  summary: Plot format Magnitude (decibels) (default) | Mag | Magnitude (linear) | Angle | Real | Imaginary | ...
  group: ''
- name: Y format2
  summary: Plot format Magnitude (decibels) (default) | Mag | Magnitude (linear) | Angle | Real | Imaginary | ...
  group: ''
- name: X parameter
  summary: Frequency plot Freq (default)
  group: ''
- name: X format
  summary: Frequency plot format Hz (default) | Auto | kHz | MHz | GHz | THz
  group: ''
- name: Y scale
  summary: Y-axis scale Linear (default) | Log
  group: ''
- name: X scale
  summary: X-axis scale Linear (default) | Log
  group: ''
- name: Plot
  summary: Plot specified data button
  group: ''
```

#### Main

### **Plate width (m)** — Width of parallel-plate transmission line `5e-3` (default) | scalar

Physical width of the parallel-plate transmission line, specified as a
scalar in meters.

### **Plate separation (m)** — Dielectric spacing in parallel-plate transmission line `1e-3` (default) | scalar

Thickness of the dielectric separating the plates, specified as a scalar
in meters.

### **Relative permeability constant** — Relative permeability of the dielectric material in the parallel-plate transmission line `1` (default) | scalar

Relative permeability of the dielectric expressed as the ratio of the
permeability of the dielectric to permeability in free space
*μ*0, specified as a scalar.

### **Relative permittivity constant** — Relative permittivity of the dielectric material in the parallel-plate transmission line `2.3` (default) | scalar

Relative permittivity of the dielectric expressed as the ratio of the
permittivity of the dielectric to permittivity in free space
*ε*0, specified as a scalar.

### **Loss tangent of dielectric** — Loss tangent of dielectric in the parallel-plate transmission line `0` (default) | scalar

Loss angle tangent of the dielectric, specified as a scalar.

### **Conductivity of the conductor (S/m)** — Conductivity of conductor `inf` (default) | scalar

Conductivity of the conductor, specified as a scalar in siemens per meter.
Conductivity is a metric to measure the flow of current in a
conductor.

### **Transmission line length(m)** — Physical length of the transmission line `0.01` (default) | positive scalar

Physical length of the transmission line in meters, specified as positive
scalar in meters.

### **Stub mode** — Type of stub `Not a stub` (default) | `Shunt` | `Series`

The block enables you to model the transmission line as a stub or as a
stubless line.

#### Stubless Transmission Line

- `Not a stub`—**Not a
  stub**

  If you model a parallel-plate transmission line as stubless
  line, the Parallel-Plate Transmission Line block first
  calculates the ABCD-parameters at each frequency contained in
  the modeling frequencies vector. It then uses the `abcd2s` function to
  convert the ABCD-parameters to S-parameters. For more
  information, see Stub Mode- Not a stub.

#### Shunt and Series Stubs

- The stub mode of the parallel-plate transmission line is
  classified as following:

  `Shunt`—**Shunt**
  parameter provides the users with the two-port network consists
  of a stub transmission line that you can terminate with either a
  short circuit or an open circuit as shown here.

  Shunt transmission line

  *Zin* is the input
  impedance of the shunt circuit. The ABCD-parameters for the
  shunt stub are calculated as

  A=1B=0C=1/ZinD=1

- `Series`—**Series**
  parameter provides the user with the two-port network consists
  of a series transmission line that you can terminate with either
  a short circuit or an open circuit as shown here.

  Series transmission line

  *Zin* is the input
  impedance of the series circuit. The ABCD-parameters for the
  series stub are calculated as

  A=1B=ZinC=0D=1

### **Termination of stub** — Stub termination `Open` (default)

Stub termination for stub modes `Shunt` and
`Series`. Choices are `Open` or
`Short`

#### Dependencies

To enable this parameter, select `Shunt`, or
`Series`, or in **Stub
mode**

#### Visualization

### **Source of frequency data** — Frequency data source `User-specified` (default)

Frequency data source, specified as
`User-specified`.

### **Frequency data (Hz)** — Frequency data range `[1e9:1e6:3e9]` (default) | vector

Frequency data range, specified as a vector in Hz.

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

Type of parameters to plot, specified as one of the following.

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

**Y parameter1** is disabled when you select **Plot type** to `Composite data`.

### **Y parameter2** — Type of parameters to plot `S11` (default) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

Type of parameters to plot, specified as one of the following.

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

**Y parameter2** is disabled when you select **Plot type** to `Composite data`.

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

To enable **Y format1**, set **Plot type** to `X-Y plane`.

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

To enable **Y format2**, set **Plot type** to `X-Y plane`.

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

Plot specified data using plot button.
## Libraries

RF Blockset / Equivalent Baseband / Transmission Lines

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2009a**

## Description

Model parallel-plate transmission line

The Parallel-Plate Transmission Line block models the parallel-plate transmission line
described in the block dialog box in terms of its frequency-dependent S-parameters. A
parallel-plate transmission line is shown in cross-section in the following figure. Its
physical characteristics include the plate width *w* and the plate
separation *d*.

Cross-section of a parallel-plate transmission line
