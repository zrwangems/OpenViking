---
type: simulink-block
title: 'Vector plot'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'vectorplot'
documentation_source_path: 'ref/vectorplot.html'
language: en
---

# Vector plot

## Ports
```yaml
ports:
- name: Vabc
  summary: Three-phase voltages vector
  direction: input
  data_types: single | double
- name: Iabc
  summary: Three-phase currents vector
  direction: input
  data_types: single | double
- name: Theta
  summary: Angle of transformation scalar
  direction: input
  data_types: single | double
- name: Vdq
  summary: Voltages in *dq* reference frame vector
  direction: input
  data_types: single | double
- name: Idq
  summary: Currents in *dq* reference frame vector
  direction: input
  data_types: single | double
- name: Magnitude
  summary: Vector magnitudes vector
  direction: input
  data_types: single | double
- name: Angle
  summary: Vector angle vector
  direction: input
  data_types: single | double
```

### Input

### **Vabc** — Three-phase voltages vector

Voltage components in the three-phase system in the *abc*
reference frame. The port accepts three voltage components multiplexed by using
Mux.

#### Dependencies

To enable this port, set **Select input types** to
`Vabc Iabc Theta`.

**Data Types:** `single` | `double`

### **Iabc** — Three-phase currents vector

Current components in the three-phase system in the *abc*
reference frame. The port accepts three current components multiplexed by using
Mux.

#### Dependencies

To enable this port, set **Select input types** to
`Vabc Iabc Theta`.

**Data Types:** `single` | `double`

### **Theta** — Angle of transformation scalar

Angle value (in radians, per-unit, or degrees for `Vabc` and
`Iabc`) between the rotating reference frame and the
*α*-axis.

The figures show the angle of transformation when:

- The *d*-axis aligns with the
  *α*-axis.
- The *q*-axis aligns with the
  *α*-axis.

  In both cases, the angle is *Theta = ωt*, where:

  - *Theta* is the angle between the *α*-
    and *d*-axes for the *d*-axis alignment or
    the angle between the *α*- and *q*-axes for
    the *q*-axis alignment. It indicates the angular position of
    the rotating *dq* reference frame with respect to the
    *α*-axis.
  - *ω* is the rotational speed in the *d-q*
    reference frame.
  - *t* is the time in seconds from the initial
    alignment.

#### Dependencies

To enable this port, set **Select input types** to
`Vabc Iabc Theta` and set **Select reference
frame** to `Rotating Reference Frame`.

**Data Types:** `single` | `double`

### **Vdq** — Voltages in *dq* reference frame vector

Direct and quadrature axis voltage components in the rotating
*dq* reference frame. The port accepts two voltage components
multiplexed by using Mux.

#### Dependencies

To enable this port, set **Select input types** to
`Vdq Idq`.

**Data Types:** `single` | `double`

### **Idq** — Currents in *dq* reference frame vector

Direct and quadrature axis current components in the rotating
*dq* reference frame. The port accepts two currents components
multiplexed by using Mux.

#### Dependencies

To enable this port, set **Select input types** to
`Vdq Idq`.

**Data Types:** `single` | `double`

### **Magnitude** — Vector magnitudes vector

Magnitudes of vectors that you want to plot. The port accepts up to six vector
magnitudes multiplexed by using Mux. The vector magnitudes correspond
to the angle values input to the **Angle** port.

**Note**

The number of multiplexed vector magnitudes should be same as the number of
multiplexed angles input to the **Angle** port.

#### Dependencies

To enable this port, set **Select input types** to
`Mag Angle`.

**Data Types:** `single` | `double`

### **Angle** — Vector angle vector

Angle values (in radians, per-unit, or degrees) of vectors that you want to plot.
The port accepts up to six vector angles multiplexed by using Mux. The
angle values correspond to the vector magnitudes input to the
**Magnitude** port.

**Note**

The number of multiplexed vector angles should be same as the number of
multiplexed magnitudes input to the **Magnitude** port.

#### Dependencies

To enable this port, set **Select input types** to
`Mag Angle`.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Select input types
  summary: Input port types Vabc Iabc Theta (default) | Vdq Idq | Mag Angle
  group: ''
- name: Select reference frame
  summary: Reference frame for vectors Rotating Reference Frame (default) | Stationary Reference Frame
  group: ''
- name: Alpha (phase-a) axis alignment
  summary: '*dq* reference frame alignment D-axis (default) | Q-axis'
  group: ''
- name: Theta units
  summary: Unit of Theta input Radians (default) | Degrees | Per-unit
  group: ''
- name: Angle units
  summary: Unit of Angle input Radians (default) | Degrees | Per-unit
  group: ''
- name: Open plot at simulation start
  summary: Open vector plot at simulation start on (default) | off
  group: ''
```

### **Select input types** — Input port types `Vabc Iabc Theta` (default) | `Vdq Idq` | `Mag Angle`

Types of input ports available for the block.

### **Select reference frame** — Reference frame for vectors `Rotating Reference Frame` (default) | `Stationary Reference Frame`

Select type of reference frame that the block uses to plot the input vectors:

- `Rotating Reference Frame` — Select this option to plot
  the three-phase voltage and current vectors in the rotating *dq*
  reference frame.
- `Stationary Reference Frame` — Select this option to
  plot the three-phase voltage and current vectors in the stationary
  *αβ* reference frame.

#### Dependencies

To enable this parameter, set **Select input types** to
`Vabc Iabc Theta`.

### **Alpha (phase-a) axis alignment** — *dq* reference frame alignment `D-axis` (default) | `Q-axis`

Align either the *d*- or *q*-axis of the rotating
reference frame to the *α*-axis of the stationary reference
frame.

#### Dependencies

To enable this parameter, set **Select input types** to
`Vabc Iabc Theta` and **Select reference
frame** to `Rotating Reference Frame`.

### **Theta units** — Unit of Theta input `Radians` (default) | `Degrees` | `Per-unit`

Unit of **Theta** input value.

#### Dependencies

To enable this parameter, set **Select input types** to
`Vabc Iabc Theta` and **Select reference
frame** to `Rotating Reference Frame`.

### **Angle units** — Unit of Angle input `Radians` (default) | `Degrees` | `Per-unit`

Unit of **Angle** input value.

#### Dependencies

To enable this parameter, set **Select input types** to
`Mag Angle`.

### **Open plot at simulation start** — Open vector plot at simulation start `on` (default) | `off`

Select this parameter to automatically open the vector plot window when simulation
begins.

**Showplot** — Click this button to open the vector plot
window.

### Vector Plot Window

This example shows the plot when you set **Select input types** to
`Mag Angle` and provide three multiplexed magnitudes and three
multiplexed angles as inputs.

You can use these buttons on the Vector Plot window:

- (Save Figure) — Click to save the plot to an
  image.
- (Preferences) — Click to open the Preferences dialog
  box.

  - **Display traces (samples)** — Enter the number of samples that
    you want to trace for the vector tip. By default, the field uses the value
    `100`.
  - **Auto-Scale** — Select this field to automatically scale the
    axes limit. The block performs auto-scaling every at every `1000`
    points of simulation.
  - **Axes limit** — Enter the maximum value of the
    *x* and *y* axis that the plot should use. By
    default, the field uses the value `1`. If you select
    **Auto-Scale** and the vector magnitude increases beyond the
    selected axes limit, the limit on the Vector Plot window extends automatically to
    accommodate the vector magnitude.
- (Run Simulation) — Click to simulate the model that
  contains the Vector Plot block.

  (Pause Simulation) — Click to pause simulation.
- (Stop Simulation) — Click to stop simulation.
- (Clear Data History) — Click to clear the vector
  tracing history.
- (Insert Legend) — Click to insert or remove the legend
  describing the vectors. You can manually change the default legend description.
- (Auto Scale) — Click to turn on or turn off the
  auto-scale function.
## Libraries

Motor Control Blockset / Signal Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020b**

## Description

Plot vectors in space domain

The Vector Plot block plots and tracks the changes in vectors in the space
domain. You can use the block to visualize vectors for electrical quantities (such as voltage
and current) and track their changes in real time by using the trace left behind by the vector
tip.

The block accepts vector magnitudes and their angles (in radians, per-unit, or degrees) as
inputs and provides a pictorial representation of the vectors. The block also traces the plot
history of the vector tip according to the selected number of points.

For details about how to use the Vector Plot block, see the model
`mcb_pmsm_foc_qep_f28379d` in Field-Oriented Control of PMSM Using Quadrature Encoder.
