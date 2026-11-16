---
type: simulink-block
title: 'RF PCB'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / RF PCB'
documentation_page: 'rfpcb'
documentation_source_path: 'ref/rfpcb.html'
language: en
---

# RF PCB

## Ports

Not documented in R2025b.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Object** — RF PCB object `pcbobj` (default) | PCB components catalog

Specify one of the PCB component objects from the workspace. You can use any one
of the objects from the PCB Components Catalog (RF PCB Toolbox) except the
`viaSingleEnded` object.

**Note**

Analyze the RF PCB objects in the workspace for at least one frequency before
using them in the block. To analyze an RF PCB object, input the RF PCB object to
an `sparameters` (RF PCB Toolbox) object.

#### RF PCB Geometry

### **Layout** — RF PCB component layout button

Click this button to visualize all the metal layers and the PCB shape of the RF
PCB component in the figure window. The filled red circle corresponds to PCB feed
points and the blue filled circles correspond to vias.

#### Dependencies

To enable the **Layout** button, input a PCB object from your
workspace to the **Object** parameter and then click
**Apply**.

### **3D Geometry** — RF PCB component geometry button

Select this button to visualize the 3-D geometry of the RF PCB component in the
figure window.

#### Dependencies

To enable the **Layout** button, input a PCB object from your
workspace to the **Object** parameter and then click
**Apply**.

#### Noise and RF Terminals

### **Simulate noise** — Simulate thermal noise `'off'` (default) | `'on'`

Select this parameter to simulate thermal noise in the antenna due to real
impedance at the antenna terminals.

#### Dependencies

To simulate thermal noise in this block, first select **Simulate
noise** in the Configuration block.

### **Ground and hide negative terminals** — Ground RF circuit terminals `'on'` (default) | `'off'`

Select this option to ground and hide the negative terminals. Clear this parameter
to expose the negative terminals. By exposing these terminals, you can connect them to
other parts in your model.

### Modeling

To enable this tab, analyze the RF PCB objects in the workspace for at least one
frequency.

### **Modeling options** — Model S-parameters `Time domain` (default) | `Frequency domain`

Model S-parameters, specified as:

- `Time domain` — This option creates an analytical
  rational model that approximates the whole range of the data.
- `Frequency domain` — This option computes the
  baseband impulse response for each carrier frequency independently. This
  technique is based on convolution. For more information, see Compare Time and Frequency Domain Simulation Options for S-parameters.

#### Time Domain Modeling

### **Fitting options** — Data fitting options `Share all poles` (default) | `Fit individually` | `Share poles by column`

Data fitting options, specified as `Fit individually`,
`Share poles by column`, or `Share all
poles`. This parameter enables you to fit your data using a
`rational` object.

The fitting results are displayed in the Rational fitting results section. The
block displays the **Number of independent fits**, **Number
of required poles**, and **Relative error achieved (dB)**
fields.

#### Dependencies

To enable this parameter, select `Time domain` in
**Modeling options**.

### **Relative error desired (dB)** — Relative error acceptable for rational fit `-40` (default) | scalar

Relative error acceptable for the rational fit, specified as a scalar in
decibels.

#### Dependencies

To enable this parameter, select `Time domain` in
**Modeling options**.

#### Frequency Domain Modeling

### **Automatically estimate impulse response duration** — Option to automatically calculate impulse response `on` | `off`

Select this parameter to automatically calculate impulse response. Clear this
parameter to manually specify the impulse response duration using **Impulse
response duration**.

#### Dependencies

To enable this parameter, select `Frequency domain` in
**Modeling options**.

### **Impulse response duration** — Impulse response duration `1e-10` (default) | scalar

Impulse response duration, specified as a scalar in seconds.

#### Dependencies

To enable this parameter:

- Select `Frequency domain` in **Modeling
  options**
- Clear `Automatically estimate impulse response
  duration`.

### Visualization

To enable this tab, analyze the RF PCB objects in the workspace for at least one
frequency.

### **Source of frequency data** — Frequency data source `Extracted from data source` (default) | `User-defined`

Frequency data source, specified as:

- `Extracted from data source` — To enable this option,
  set **Data source** to `Data file`.
  Verify that the file contains frequency data.
- `User-specified` — Select this option to specify a
  vector of frequencies in **Frequency data** and the frequency
  units in a corresponding drop-down list.

When **Source of frequency data** is `Extracted from
data source`, the **Data source** must be set to
`Data file`. Verify that the specified **Data
file** contains frequency data.

When **Source of frequency data** is
`User-specified`, specify a vector of frequencies in the
**Frequency data** parameter. Also, specify units from the
corresponding drop-down list.

### **Frequency data** — Frequency data range `[1e9:1e6:3e9]` (default) | finite vector

Frequency data range, specified as a finite vector. Select the frequency units
from the corresponding drop-down list.

#### Dependencies

To enable this parameter, set **Source of frequency data** to
`User-specified`.

### **Plot type** — Type of data plot `X-Y plane` (default) | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

Type of data plot, specified as one of the following:

- `X-Y plane` — Generate a Cartesian plot of
  your data versus frequency. To create linear, semilog, or log-log plots, set
  **Y-axis scale** and **X-axis scale**
  accordingly.
- `Polar plane` — Generate a polar plot of your
  data. The block plots only the data corresponding to the specified
  frequencies.
- `Z smith chart`, `Y smith
  chart`, and `ZY smith chart` —
  Generate a Smith® chart. The block plots
  only the data corresponding to the specified frequencies.

### **Parameter 1** — Type of S-Parameters to plot `S(1,1)` (default) | `S(1,2)` | `S(2,1)` | `S(2,2)`

Type of S-Parameters to plot, specified as `S(1,1)`,
`S(1,2)`, `S(2,1)`, or `S(2,2)`.
For an N-port device, **Parameter 1** lists all options to plot
N-port S-parameters.

### **Parameter 2** — Type of S-Parameters to plot `None` (default) | `S(1,1)` | `S(1,2)` | `S(2,1)` | `S(2,2)` | ...

Type of S-Parameters to plot, specified as `S(1,1)`,
`S(1,2)`, `S(2,1)`, or `S(2,2)`.

### **Format1** — Plot format `Magnitude (dB)` (default) | `Magnitude (linear)` | `Angle(degrees)` | `Real` | `Imaginary`

Plot format, specified as `Magnitude (dB)`,
`Angle(degrees)`, `Real`, or
`Imaginary`.

#### Dependencies

To enable this parameter, set **Plot type** to `X-Y
plane`.

### **Format2** — Plot format `Magnitude (dB)` (default) | `Magnitude (linear)` | `Angle(degrees)` | `Real` | `Imaginary`

Plot format, specified as `Magnitude (dB)`,
`Angle(degrees)`, `Real`, or
`Imaginary`.

#### Dependencies

To enable this parameter, set **Plot type** to `X-Y
plane`.

### **Y-axis scale** — Y-axis scale `Linear` (default) | `Logarithmic`

Y-axis scale, specified as `Linear` or
`Logarithmic`.

#### Dependencies

To enable this parameter, set **Plot type** to `X-Y
plane`.

### **X-axis scale** — X-axis scale `Linear` (default) | `Logarithmic`

X-axis scale, specified as `Linear` or
`Logarithmic`.

#### Dependencies

To enable this parameter, set **Plot type** to `X-Y
plane`.

### **Plot** — Plot specified data button

Click this button to plot the data.

## Libraries

RF Blockset / Circuit Envelope / PCB

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Model RF PCB Component

The RF PCB block enables you to create, visualize, and analyze characteristics of
components used on a printed circuit board (PCB) in RF Blockset™ circuit envelope simulation environment. You can create components such as
transmission lines, splitters, couplers, baluns, and others from the PCB Components Catalog (RF PCB Toolbox) except the
`viaSingleEnded` object.

**Note**

To use this block, you need a RF PCB Toolbox™ license.
