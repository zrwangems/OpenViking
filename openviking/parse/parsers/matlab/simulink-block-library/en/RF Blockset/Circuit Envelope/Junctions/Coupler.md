---
type: simulink-block
title: 'Coupler'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Junctions'
documentation_page: 'coupler'
documentation_source_path: 'ref/coupler.html'
language: en
---

# Coupler

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Select component
  summary: Coupler type Directional coupler (default) | Coupler symmetrical | Coupler antisymmetrical | Hybrid quadrature
    (90 deg) | Hybrid rat-race | Magic tee
  group: ''
- name: Coupling (dB)
  summary: Fraction of input signal power coupled to output port 0 (default) | nonnegative and real scalar
  group: ''
- name: Directivity (dB)
  summary: Ratio of power at coupled port to power at isolated port inf (default) | nonnegative and real scalar
  group: ''
- name: Insertion loss (dB)
  summary: Loss of signal power between input and output ports inf (default) | nonnegative and real scalar
  group: ''
- name: Return loss (dB)
  summary: Loss of signal power due to impedance mismatch inf (default) | nonnegative and real scalar
  group: ''
- name: Power transmission coefficient
  summary: Transmitted signal power 0 (default) | real scalar
  group: ''
- name: Reference impedances (Ohm)
  summary: Reference impedance of coupler 50 (default) | positive scalar | positive three-tuple vector
  group: ''
- name: Ground and hide negative terminals
  summary: Ground RF circuit terminals on (default) | off
  group: ''
```

### **Select component** — Coupler type `Directional coupler` (default) | `Coupler symmetrical` | `Coupler antisymmetrical` | `Hybrid quadrature (90 deg)` | `Hybrid rat-race` | `Magic tee`

Coupler type, specified as:

- `Directional coupler`

  The default option is `Directional coupler`. The S-parameters matrix for the
  `Directional coupler` is:

  [rliliscilrlcisiscrlilcisilrl]

  where:

  - rl =
    10(-ReturnLoss/20)
  - il =
    j10(-InsertionLoss/20)
  - is =
    j10(-(Coupling+Directivity)/20)
  - c =
    10(-Coupling/20)

  **Note**

  In release 2019a, the S-parameters representation of the
  Directional Coupler block is altered to permit a valid
  implementation for all specified mask values. This
  implementation adds a 90 degree phase shift to s12, s13,
  s21, s24, s31, s34, s42, and s43 terms. In addition, a -180
  phase shift is added to the s14, s23, s32 and s41
  terms.

  Use this option to model coupler parameters from data
  sheets.
- `Coupler symmetrical`

  The S-parameters matrix for the `Coupler symmetrical` is:

  [0α0jβα0jβ00jβ0αjβ0α0]

  where:

  - |α| ≤ 1 =
    Power transmission coefficient
  - β = sqrt(1– α\*α)
- `Coupler antisymmetrical`

  The S-parameters matrix for the `Coupler antisymmetrical` is:

  [0α0βα0−β00−β0αβ0α0]

  where:

  - |α| ≤ 1 =
    Power transmission coefficient.
  - β = sqrt (1– α\*α)
- `Hybrid quadrature (90deg)`

  The S-parameters matrix for the `Hybrid quadrature(90deg)` is:

  [0-j/20-1/2-j/20-1/200-1/20-j/2-1/20-j/20]
- `Hybrid rat-race`

  The S-parameters matrix for the `Hybrid rat-race` is:

  [0−j/20−j/2−j/20j/200j/20−j/2−j/20−j/20]
- `Magic tee`

  The S-parameters matrix for the `Magic
  tee` is:

  [0011001−111001−100]2

The Divider block uses the `ispassive` function to test the passivity of the S-parameters
matrix.

### **Coupling (dB)** — Fraction of input signal power coupled to output port 0 (default) | nonnegative and real scalar

Fraction of input signal power coupled to output port of the `Directional
coupler`, specified as a nonnegative and real scalar. The
default value is `0` dB.

#### Dependencies

To enable this parameter, select `Directional coupler` in **Select
component** tab.

### **Directivity (dB)** — Ratio of power at coupled port to power at isolated port `inf` (default) | nonnegative and real scalar

Ratio of power at coupled port to power at isolated port of
the `Directional coupler`, specified as a nonnegative
and real scalar. The default value is `inf`.

#### Dependencies

To enable this parameter, select `Directional coupler` in **Select
component** tab.

### **Insertion loss (dB)** — Loss of signal power between input and output ports `inf` (default) | nonnegative and real scalar

Loss of signal power between input and output ports of the `Directional
coupler`, specified as a nonnegative and real scalar. The
default value is `inf`.

#### Dependencies

To enable this parameter, select `Directional coupler` in **Select
component** tab.

### **Return loss (dB)** — Loss of signal power due to impedance mismatch `inf` (default) | nonnegative and real scalar

Loss of signal power due to impedance mismatch of the `Directional
coupler`, specified as a nonnegative, and real scalar. The
default value is `inf`.

#### Dependencies

To enable this parameter, select `Directional coupler` in **Select
component** tab.

### **Power transmission coefficient** — Transmitted signal power 0 (default) | real scalar

Transmitted signal power of the `Directional coupler`,
specified as a real scalar. The default value is 0.

#### Dependencies

To enable this parameter, select `Coupler
symmetrical` or `Coupler
antisymmetrical` in **Select
component** tab.

### **Reference impedances (Ohm)** — Reference impedance of coupler `50` (default) | positive scalar | positive three-tuple vector

Reference impedance of coupler, specified as a scalar or positive three-tuple vector.

**Note**

When the reference impedances of all the ports are not equal, the
model inside the Coupler block is normalized to 50 ohms.

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

Model ideal frequency-independent couplers with S-parameters

The Coupler block models four port directional
couplers in a circuit envelope environment as an ideal S-parameter
model. The four ports of the coupler are `Input port` (Port
1), `Through port` (Port 2), `Isolated port` (Port
3), `Coupled port` (Port 4).

Directional couplers are used to sample forward and reflected
waves propagating along a transmission line. Directional couplers
find uses in many RF design applications such as line power sensors
and transmitter automatic level controls.

Hybrid couplers are used to split or combine signals with specific
phase relations.
