---
type: simulink-block
title: 'Controlled Current Source (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'controlledcurrentsourcethreephase'
documentation_source_path: 'ref/controlledcurrentsourcethreephase.html'
language: en
---

# Controlled Current Source (Three-Phase)

## Ports

### Input

### **S** — Control physical signal

Physical signal input port associated with the control signal.

#### Dependencies

To enable this port, set **Input type** to
`Instantaneous`.

### **I** — RMS current physical signal

Physical signal input port associated with the RMS current.

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

### **~** — Three-phase current electrical

Expandable three-phase
port.

#### Dependencies

To enable this port, set **Modeling option** to
`Composite three-phase ports`.

### **a** — *a*-phase current electrical

Electrical conserving port associated with the
*a*-phase output current.

#### Dependencies

To enable this port, set **Modeling option** to
`Expanded three-phase ports`.

### **b** — *b*-phase current electrical

Electrical conserving port associated with the
*b*-phase output current.

#### Dependencies

To enable this port, set **Modeling option** to
`Expanded three-phase ports`.

### **c** — *c*-phase current electrical

Electrical conserving port associated with the
*c*-phase output current.

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
  currents, [*ia*
  *ib*
  *ic*], are equal to the
  values of the input port **S**.
- `Sinusoidal magnitude and phase
  shift` — The output currents are equal
  to:

  ia=(2 I)sin(2πFrated+ph)ib=(2 I)sin(2πFrated+ph−2π3)ic=(2 I)sin(2πFrated+ph+2π3)

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

**Introduced in R2018b**

## Description

Ideal three-phase controlled current source

The Controlled Current Source (Three-Phase) block
represents an ideal three-phase current source that is powerful enough to maintain the
specified current through it regardless of the voltage across it. The output currents
are [*ia*
*ib*
*ic*] = *S*, where
*S* is a vector containing the numerical values presented at the
physical signal port.

The figure shows the equivalent circuit for the expanded implementation of the
Controlled Current Source (Three-Phase) block.

To use the Controlled Current Source (Three-Phase)
block as an abstracted current controller in an electrical drive, connect the conserving
ports for the output current directly to the machine.

To choose the input type of this block, set the **Input type**
parameter to `Instantaneous` or `Sinusoidal
magnitude and phase shift`. If you select
`Instantaneous`, this block works only in time simulation
mode. If you select `Sinusoidal magnitude and phase shift`,
this block works in both time and frequency-time simulation modes. For more information,
see Frequency and Time Simulation Mode.

To access the implementation with an expanded, three-phase port, double-click the block and
set the **Modeling option** parameter to `Expanded
three-phase ports`.
