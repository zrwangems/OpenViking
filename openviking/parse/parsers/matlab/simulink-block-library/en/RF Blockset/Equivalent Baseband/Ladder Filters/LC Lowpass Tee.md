---
type: simulink-block
title: 'LC Lowpass Tee'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Ladder Filters'
documentation_page: 'lclowpasstee'
documentation_source_path: 'ref/lclowpasstee.html'
language: en
---

# LC Lowpass Tee

## Ports

Not documented in R2025b.

## Parameters

### Main

### **Inductance (H)** — Inductance of the LC Lowpass Tee `[1.3324e-5 1.3324e-5]` (default) | vector

Vector containing the inductances, in order from source to load, of
all inductors in the network. The inductance vector must contain at
least three elements. All values must be strictly positive.

### **Capacitance (F)** — Capacitance of the LC Lowpass Tee `1.1327e-9` (default) | vector

Vector containing the capacitances, in order from source to load, of
all capacitors in the network. Its length must be equal to the length of
the vector you provide in the **Inductance** parameter.
All values must be strictly positive.

### Visualization

### **Source of frequency data** — Frequency data source `User-specified` (default)

Frequency data source, specified as
`User-specified`.

### **Frequency data (Hz)** — Frequency data range `[1:1.0e5:4e6]` (default) | vector

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

### **Y parameter1** — Type of parameters to plot `S11` (default) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

Type of parameters to plot based on the **Plot type** you set, specified as one of the following.

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`, `S12`, `S21`, `S22`, `GroupDelay`, `OIP3`, `NF`, `NFactor`, and `NTemp`. |
| `Composite data` | No **Y parameter1** to set. |
| `Polar plane` | `S11`, `S12`, `S21`, and `S22` |
| `Z Smith chart` | `S11` and `S22`. |
| `Y Smith chart` | `S11` and `S22`. |
| `ZY smith chart` | `S11` and `S22`. |

### **Y parameter2** — Type of parameters to plot `S11` (default) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

Type of parameters to plot based on the **Plot type** you set, specified as one of the following.

| Plot type | Y parameter2 |
| --- | --- |
| `X-Y plane` | `S11`, `S12`, `S21`, `S22`, `GroupDelay`, `OIP3`, `NF`, `NFactor`, and `NTemp`. |
| `Composite data` | No **Y parameter2** to set. |
| `Polar plane` | `S11`, `S12`, `S21`, and `S22` |
| `Z Smith chart` | `S11` and `S22`. |
| `Y Smith chart` | `S11` and `S22`. |
| `ZY smith chart` | `S11` and `S22`. |

### **Y format1** — Plot format `Magnitude (decibels)` (default) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

Plot format, specified as one of the following.

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`, `S12`, `S21`, and `S22`. | `Magnitude (decibels)`, `Magnitude (linear)`, `Angle(degrees)`, `Angle(radians)`, `Real`, and `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, and `ps`. |
| `OIP3` | `dB`, `dBm`, `W`, and `mW`. |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |

#### Dependencies

To enable **Y format1**, set **Plot type** to `X-Y plane`.

### **Y format2** — Plot format `Magnitude (decibels)` (default) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

Plot format, specified as one of the following.

| Y parameter2 | Y format2 |
| --- | --- |
| `S11`, `S12`, `S21`, and `S22`. | `Magnitude (decibels)`, `Magnitude (linear)`, `Angle(degrees)`, `Angle(radians)`, `Real`, and `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, and `ps`. |
| `OIP3` | `dB`, `dBm`, `W`, and `mW`. |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |

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

RF Blockset / Equivalent Baseband / Ladder Filters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Model LC lowpass tee network

The LC Lowpass Tee block models the LC lowpass tee network described in the block
dialog box in terms of its frequency-dependent S-parameters.

For each inductor and capacitor in the network, the block first calculates the
ABCD-parameters at each frequency contained in the vector of modeling frequencies. For
each series circuit, A = 1, B = *Z*,
C = 0, and D = 1, where *Z* is the impedance of the
series circuit. For each shunt, A = 1, B = 0,
C = *Y*, and D = 1, where *Y*
is the admittance of the shunt circuit.

The LC Lowpass Tee block then cascades the ABCD-parameters for each circuit element at
each of the modeling frequencies, and converts the cascaded parameters to S-parameters
using the RF Toolbox™
`abcd2s` function.

See the Output Port block reference page for
information about determining the modeling frequencies.

The LC lowpass tee network object is a two-port network as shown in the following
circuit diagram.

Two-port LC lowpass tee network

[L1, L2, L3, ...]
is the value of the `'L'` property, and [C1,
C2, C3, ...] is the value of the
`'C'` property.
