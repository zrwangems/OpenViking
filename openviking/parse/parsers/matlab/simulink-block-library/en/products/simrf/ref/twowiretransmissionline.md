---
type: simulink-block
title: 'Two-Wire Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband Simulation / Cascaded Subsystems / Transmission Lines'
documentation_page: 'twowiretransmissionline'
documentation_source_path: 'ref/twowiretransmissionline.html'
language: en
---

# Two-Wire Transmission Line

## Ports

Not documented in R2025b.

## Parameters

### Main

### **Wire radius (m)** — Radius of conducting wires `0.67e-3` (default) | scalar

Radius of the conducting wires of the two-wire transmission line,
specified as a scalar in meters.

### **Wire separation (m)** — Separation in two-wire transmission line `1.62e-3` (default) | scalar

Physical distance between the wires, specified as a scalar in
meters.

### **Relative permeability constant** — Relative permeability of dielectric `1` (default) | scalar

Relative permeability of the dielectric, expressed as the ratio of the
permeability of the dielectric to permeability in free space
*μ*0, specified as a scalar.

### **Relative permittivity constant** — Relative permittivity of dielectric `2.3` (default) | scalar

Relative permittivity of the dielectric, expressed as the ratio of the
permittivity of the dielectric to permittivity in free space
*ε*0, specified as a scalar.

### **Loss tangent of dielectric** — Dielectric loss tangent `0` (default) | scalar

Loss tangent of the dielectric, specified as a scalar.

### **Conductivity of the conductor (S/m)** — Conductivity of conductor `inf` (default) | scalar

Conductivity of the conductor, specified as a scalar in siemens per
meter. Conductivity measures the ease with which current flows in the
conductor.

### **Transmission line length (m)** — Physical length of transmission line `0.01` (default) | scalar

Physical length of the transmission line, specified as a scalar in
meters.

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
  information, see Stub Mode- Not a stub.

#### Shunt Transmission Line

- `Shunt`—This parameter
  provides a two-port network that consists of a stub
  transmission line that you can terminate with either a short
  circuit or an open circuit as shown in these
  diagrams.

  Short and open circuit shunt stub

  *Zin* is the input
  impedance of the shunt circuit. The ABCD-parameters for the
  shunt stub are calculated as

  A=1B=0C=1/ZinD=1

#### Series Transmission Line

- `Series`—This mode
  parameter provides a two-port network that consists of a
  series transmission line that you can terminate with either
  a short circuit or an open circuit as show in these
  diagrams.

  Short and open circuit series stub

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

Model two-wire transmission line

The Two-Wire Transmission Line block models the two-wire transmission line described
in the block dialog box in terms of its frequency-dependent S-parameters. A two-wire
transmission line is shown in cross-section in the following figure. Its physical
characteristics include the radius of the wires *a*, the separation
or physical distance between the wire centers *S*, and the relative
permittivity and permeability of the wires. RF Blockset™ Equivalent Baseband software assumes the relative permittivity and
permeability are uniform.

Two-wire transmission line
