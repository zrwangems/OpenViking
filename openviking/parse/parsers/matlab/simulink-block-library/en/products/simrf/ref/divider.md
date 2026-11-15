---
type: simulink-block
title: 'Divider'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Junctions'
documentation_page: 'divider'
documentation_source_path: 'ref/divider.html'
language: en
---

# Divider

## Ports

Not documented in R2025b.

## Parameters

### **Select component** — Divider type `T power divider` (default) | `Resistive power divider` | `Wilkinson power divider` | `Tee H-plane (S33=0)` | `Tee E-plane`

Divider type, specified as:

- `T power divider`

  The S-parameter matrix for `T-power divider`  is :

  [s11s21s31s21s22s32s31s32s33]

  where:

  - s11 = (z23
    –z1) / (z23 +
    z1)
  - s22 = (z13
    –z2) / (z13 +
    z2)
  - s33 = (z12
    –z3) / (z12 +
    z3)
  - s21 = (1+
    s11) \* sqrt(z1 / z2)
  - s31 = (1+
    s11) \* sqrt(z1 / z3)
  - s32 = (1+
    s22) \* sqrt(z2 / z3)
  - z12 = z1 \*
    z2 / (z1 + z2)
  - z13 = z1 \*
    z3 / (z1 + z3)
  - z23 = z2 \*
    z3 / (z2 + z3)
  - z1 = Z0(1),
    z2 = Z0(2), z3 = Z0(3)
  - Reference Impedances: Z0 = [z1,
    z2, z3 ]
- `Resistive power divider`

  The S-parameter matrix for `Resistive power divider` is :

  [01/21/21/201/21/21/20]

  When you select this option, the following parameter is available:
- `Wilkinson power divider`

  The S-parameter matrix for `Wilkinson power divider` is:

  [0-j/2-j/2-j/200-j/200]

  **Note**

  - For DC carrier (0 Hz) frequency, Wilkinson power
    divider is a zero matrix.
  - Starting R2021a, port positions in the Divider
    block when you select the `Wilkinson
    power divider` component have
    changed. For more information, see Version History.
- `Tee H-plane (S33=0)`

  The `Tee H-plane (S33=0)` is symmetrical,
  lossless, and reciprocal. The S-parameter matrix is:

  (−1121−12220)2
- `Tee E-plane`

  The `Tee E-plane` is symmetrical,
  lossless, and reciprocal. The S-parameter matrix is:

  (11211−22−20)2

### **Number of divider outports** — Number of Wilkinson power divider outports `2` (default) | nonnegative integer in the range (`1`, `65`]

Number of Wilkinson power divider outports, specified as a nonnegative
integer in the range (`1`, `65`].

#### Dependencies

To enable this parameter, set **Select Component** to
`Wilkinson power divider`.

### **Reference impedances (Ohm)** — Reference impedance of divider `50` (default) | positive scalar | three-tuple vector

Reference impedance of divider, specified as a positive scalar or three-tuple vector.

**Note**

When the reference impedances of all the ports are not equal, the
model inside the Divider block is normalized to 50 ohms.

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Select this parameter to ground and hide the negative terminals.
To expose the negative terminals, clear the parameter. By exposing
these terminals, you can connect them to other parts of your model.

By default, this option is selected.

## Libraries

RF Blockset / Circuit Envelope / Junctions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

### R2022b: Model Wilkinson power divider with up to 65 ports

Use the Divider block to model a Wilkinson power divider with more than two and up
to 65 outports. Use the **Number of divider
outports** to set the number of outports.

### R2021a: Port positions of Wilkinson power divider component in Divider block changed

The port positions in the Divider block when you select the
`Wilkinson power divider` component have changed. Prior
to this release, Ports 1 and 3 were on the same side opposite that of Port 2. This
release, Ports 2 and 3 appear on one side together opposite the side of Port
1.

Existing models using the Divider block with the `Wilkinson power
divider` component might need to be updated to ensure that there
are no broken connections. Use the RF Blockset check in the
Simulink® Upgrade Advisor to identify and rewire the
broken port connections in your existing models. For more information, see Check model for RF Blockset Divider blocks using Wilkinson power divider component with broken connections.

## Description

Model ideal frequency-independent dividers or combiners with S-parameters

The Divider block models power dividers or combiners in a circuit envelope
environment as an S-parameter model. In a power divider, the input power enters at a
port, splits, and exits at different ports.

To use a power divider to model and simulate a 66 GHz QPSK RF transmit and receive
system with a 32-element hybrid beamforming antenna, see the Transmit Subarrays section
in the Modeling RF mmWave Transmitter with Hybrid Beamforming example.
