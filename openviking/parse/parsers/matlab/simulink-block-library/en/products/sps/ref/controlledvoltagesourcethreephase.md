---
type: simulink-block
title: 'Controlled Voltage Source (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sources'
documentation_page: 'controlledvoltagesourcethreephase'
documentation_source_path: 'ref/controlledvoltagesourcethreephase.html'
language: en
---

# Controlled Voltage Source (Three-Phase)

## Ports

### Input

### **S** — Control physical signal | vector

Physical signal input port associated with the control signal. The
output voltages are [*va*
*vb*
*vc*] = *S*.
For an ideal sinusoidal source, input three sine waves that have the
requisite amplitude and phase delays of [0−2π32π3].

#### Dependencies

To enable this port, set **Input type** to
`Instantaneous`.

### **Vt** — Phase-to-phase RMS voltage physical signal

Physical signal input port associated with the phase-to-phase RMS
voltage.

#### Dependencies

To enable this port, set **Input type** to
`Sinusoidal magnitude and phase
shift`.

### **ph** — Phase shift physical signal

Physical signal input port associated with the phase shift, in radians.

#### Dependencies

To enable this port, set **Input type** to
`Sinusoidal magnitude and phase
shift`.
### Conserving

### **n** — Neutral electrical

Electrical conserving port associated with the neutral phase.

### **~** — Three-phase voltage electrical

Expandable three-phase
port associated with the output voltage.

#### Dependencies

To enable this port, set **Modeling option** to
`Composite three-phase ports`.

### **a** — *a*-phase voltage electrical

Electrical conserving port associated with the
*a*-phase output voltage.

#### Dependencies

To enable this port, set **Modeling option** to
`Expanded three-phase ports`.

### **b** — *b*-phase voltage electrical

Electrical conserving port associated with the
*b*-phase output voltage.

#### Dependencies

To enable this port, set **Modeling option** to
`Expanded three-phase ports`.

### **c** — *c*-phase voltage electrical

Electrical conserving port associated with the
*c*-phase output voltage.

#### Dependencies

To enable this port, set **Modeling option** to
`Expanded three-phase ports`.

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### **Input type** — Type of input `Instantaneous` (default) | `Sinusoidal magnitude and phase shift`

Type of physical signal input. Choose between:

- `Instantaneous` — The output
  voltages, [*va*
  *vb*
  *vc*], are equal to the
  values of the input port **S**.
- `Sinusoidal magnitude and phase
  shift` — The output voltages are equal
  to:

  va=(2Vt3)sin(2πFrated+ph)vb=(2Vt3)sin(2πFrated+ph−2π3)vc=(2Vt3)sin(2πFrated+ph+2π3)

### **Rated electrical frequency** — Rated electrical frequency `60` `Hz` | scalar

Rated electrical frequency. The value of this parameter must be equal to
the value of the rated electrical frequencies of other sinusoidal sources in
your model, if present.

#### Dependencies

To enable this parameter, set **Input type** to
`Sinusoidal magnitude and phase
shift`.

## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Ideal three-phase controlled voltage source

The Controlled Voltage Source (Three-Phase) block
represents an ideal three-phase voltage source that maintains the specified voltage
regardless of the current through it.

To choose the input type of this block, set the **Input type**
parameter to `Instantaneous` or `Sinusoidal
magnitude and phase shift`. If you select
`Instantaneous`, this block works only in time simulation
mode. If you select `Sinusoidal magnitude and phase shift`,
this block works in both time and frequency-time simulation modes. For more information,
see Frequency and Time Simulation Mode.

To access the implementation with an expanded, three-phase port, double-click the
block and set the **Modeling option** parameter to
`Expanded three-phase ports`.
