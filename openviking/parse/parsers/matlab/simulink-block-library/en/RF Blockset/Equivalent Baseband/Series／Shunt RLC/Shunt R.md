---
type: simulink-block
title: 'Shunt R'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Series/Shunt RLC'
documentation_page: 'shuntr'
documentation_source_path: 'ref/shuntr.html'
language: en
---

# Shunt R

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Resistance (Ohms)
  summary: Resistance of the shunt element 1 (default) | scalar
  group: Main
- name: Source of frequency data
  summary: Frequency data source User-specified (default)
  group: Visualization
- name: Frequency data (Hz)
  summary: Frequency data range [1:1.0e5:4e6] (default) | vector
  group: Visualization
- name: Reference impedance (ohms)
  summary: Reference impedance 50 (default) | nonnegative scalar
  group: Visualization
- name: Plot type
  summary: Type of data plot X-Y plane (default) | Composite data | Polar plane | Z Smith chart | Y Smith chart | ZY Smith
    chart
  group: Visualization
- name: Y parameter1
  summary: Type of parameters to plot S11 (default) | S12 | S21 | S22 | GroupDelay | OIP3 | NF | ...
  group: Visualization
- name: Y parameter2
  summary: Type of parameters to plot S11 (default) | S12 | S21 | S22 | GroupDelay | OIP3 | NF | ...
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
  summary: Frequency plot format Auto (default) | Hz | kHz | MHz | GHz | THz
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

### **Resistance (Ohms)** — Resistance of the shunt element `1` (default) | scalar

Scalar value for the resistance. The value must be
non-negative.

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

### **X format** — Frequency plot format `Auto` (default) | `Hz` | `kHz` | `MHz` | `GHz` | `THz`

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

RF Blockset / Equivalent Baseband / Series / Shunt RLC

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Model shunt resistor

The Shunt R block models the shunt resistor described in the block dialog box, in
terms of its frequency-dependent S-parameters.

The shunt R object is a two-port network, as shown in the following circuit
diagram.

Two-port shunt L network
