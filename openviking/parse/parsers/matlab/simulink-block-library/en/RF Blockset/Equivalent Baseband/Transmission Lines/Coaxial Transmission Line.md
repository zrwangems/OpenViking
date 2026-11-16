---
type: simulink-block
title: 'Coaxial Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Transmission Lines'
documentation_page: 'coaxialtransmissionline'
documentation_source_path: 'ref/coaxialtransmissionline.html'
language: en
---

# Coaxial Transmission Line

## Ports

Not documented in R2025b.

## Parameters

### Main

### **Outer radius (m)** — Radius of outer conductor `2.57e-3` (default) | scalar

Radius of the outer conductor of the coaxial transmission line,
specified as a scalar in meters.

### **Inner radius(m)** — Radius of Inner conductor `0.725e-3` (default) | scalar

Radius of the inner conductor of the coaxial transmission line,
specified as a scalar in meters.

### **Relative permeability constant** — Relative permeability of dielectric `1` (default) | real scalar

Relative permeability of the dielectric, expressed as the ratio of the
permeability of the dielectric to permeability in free space
*μ*0, specified as a real
scalar.

### **Relative permittivity constant** — Relative permittivity of dielectric `2.3` (default) | real scalar

Relative permittivity of the dielectric, expressed as the ratio of the
permittivity of the dielectric to permittivity in free space
*ε*0, specified as a real
scalar.

### **Loss tangent of dielectric** — Dielectric loss tangent `0` (default) | nonnegative scalar

Loss tangent of the dielectric, specified as a nonnegative scalar.

### **Conductivity of the conductor (S/m)** — Conductivity of conductor `inf` (default) | positive scalar

Conductivity of the conductor, specified as a positive scalar in
Siemens/meters.

### **Transmission line length (m)** — Physical length of transmission line `0.01` (default) | positive scalar

Physical length of the transmission line, specified as a positive
scalar in meters.

### **Stub mode** — Type of stub `Not a stub` (default) | `Shunt` | `Series`

The block enables you to model the transmission line as a stub or as a
stubless line.

#### Stubless Transmission Line

- `Not a stub`—**Not
  a stub**

  If you model a coaxial transmission line as stubless line,
  the Coaxial Transmission Line block first calculates the
  ABCD-parameters at each frequency contained in the modeling
  frequencies vector. It then uses the `abcd2s` function
  to convert the ABCD-parameters to S-parameters. For more
  information, see Stub Mode - Not a Stub.

#### Shunt Transmission Line

- `Shunt`—This parameter
  provides a two-port network that consists of a stub
  transmission line that you can terminate with either a short
  circuit or an open circuit as shown in these
  diagrams.

  Shunt transmission line

  *Zin* is the input
  impedance of the shunt circuit and it is calculated as
  follows:

  for a short circuited transmission line

  Zin=jZ0tanγl

  and for the open circuited transmission line

  Zin=−jZ0cotγl

  where

  - *Z0*
    is the characteristic impedance and
  - γ is the propagation
    constant

  The ABCD-parameters for the shunt stub are
  calculated as

  A=1B=0C=1/ZinD=1

#### Series Transmission Line

- `Series`—This mode
  parameter provides a two-port network that consists of a
  series transmission line that you can terminate with either
  a short circuit or an open circuit as show in these
  diagrams.

  Series transmission line

  *Zin* is the input
  impedance of the series circuit. The ABCD-parameters for the
  series stub are calculated as

  A=1B=ZinC=0D=1

### **Termination of stub** — Stub termination `Open` (default) | `Short`

Stub termination for stub modes `Shunt` and
`Series`. Choices are `Open` or
`Short`

#### Dependencies

To enable this parameter, select `Shunt`
or `Series` in **Stub
mode**

### Visualization

### **Source of frequency data** — Frequency data source `User-specified` (default)

Frequency data source, specified as
`User-specified`.

### **Frequency data (Hz)** — Frequency data range `[1e9:1e6:3e9]` (default) | vector

Frequency data range, specified as a vector in hertz.

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

Plot the specified data using the plot button.

## Libraries

RF Blockset / Equivalent Baseband / Transmission Lines

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2009a**

## Description

Model coaxial transmission line

The Coaxial Transmission Line block uses S-parameters to model its
frequency behavior. A cross-section of the Coaxial Transmission Line is shown in the
following figure. Its physical characteristics include the radius of the inner conductor
*a* and the radius of the outer conductor *b*.

Cross-section of coaxial transmission line
