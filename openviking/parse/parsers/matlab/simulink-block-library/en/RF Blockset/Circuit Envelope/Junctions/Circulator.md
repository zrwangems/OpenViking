---
type: simulink-block
title: 'Circulator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Junctions'
documentation_page: 'circulator'
documentation_source_path: 'ref/circulator.html'
language: en
---

# Circulator

## Ports

Not documented in R2025b.

## Parameters

### **Select component** — Circulator direction `Circulator clockwise` (default) | `Circulator counter clockwise` | `Tee H-plane (S11=0)` | `Reciprocal phase shifter`

Circulator direction, specified as:

- `Circulator clockwise`

  The default option is `Circulator clockwise`.
  The s-parameter matrix for `Circulator clockwise` is:

  [001100010]

  `Circulator counter clockwise`

  The s-parameter matrix for `Circulator counter clockwise` is:

  [010001100]
- `Tee H-plane (S11=0)`

  The s-parameter matrix for `Tee H-plane (S11=0)`
  is:

  (010100001)
- `Reciprocal phase shifter`

  The s-parameter matrix for `Reciprocal phase
  shifter` is:

  (0phase120phase120000phase33)(−j2)

### **Reference impedances (Ohm)** — Reference impedance of circulator `50` (default) | positive scalar | three-tuple vector

Reference impedance of circulator, specified as a positive scalar or three-tuple vector.

**Note**

When the reference impedances of all the ports are not equal, the
model inside the Circulator block is normalized to 50 ohms.

### **Phase shift, ports 1 and 2 (rad)** — Angle to shift phase of signal in port 1 and port 2 `0` (default) | positive scalar

Angle to shift the phase of the signal in port 1 and port 2, specified as
a positive scalar in radians.

### **Phase shift, ports 3 (rad)** — Angle to shift phase of signal in port 3 `0` (default) | positive scalar

Angle to shift the phase of the signal in port 3, specified as a positive
scalar in radians.

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Select this parameter to ground and hide the negative terminals.
To expose the negative terminals, clear this parameter. By exposing
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

## Description

Model ideal frequency-independent circulators with S-parameters

Use the Circulator block to model ideal passive
three-port circulators in a circuit envelope environment. Circulators
are used to control signal direction and flow inside an RF circuit.
The Circulator block can circulate the signal in clockwise
or counterclockwise direction depending on the parameter selection.
