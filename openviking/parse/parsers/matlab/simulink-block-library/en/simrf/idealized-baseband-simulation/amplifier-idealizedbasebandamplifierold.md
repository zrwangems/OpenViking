---
type: simulink-block
title: 'Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband Simulation'
documentation_page: 'idealizedbasebandamplifierold'
documentation_source_path: 'ref/idealizedbasebandamplifierold.html'
language: en
---

# Amplifier

## Ports

Not documented in R2025b.

## Parameters

### **Method** — Method used to model nonlinearity `Linear` (default) | `Cubic polynomial` | `Hyperbolic tangent` | `Saleh model` | `Ghorbani model` | `Rapp model`

Method used to model the amplifier nonlinearity, specified as one of the following:

- `Linear`
- `Cubic polynomial`
- `Hyperbolic tangent`
- `Saleh model`
- `Ghorbani model`
- `Rapp model`

**Tunable:** Yes

### **Linear gain (dB)** — Linear gain for output function `0` (default) | real scalar

Linear gain for the output function of the Amplifier block, specified as a real scalar in
decibels.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Linear`, `Cubic polynomial`, `Hyperbolic
tangent`, or `Rapp model`.

### **IIP3 (dBm)** — Third-order input power intercept point `30` (default) | real positive number

Third-order input power intercept point for the cubic polynomial and the hyperbolic
tangent amplifier model, specified as a real positive number in dBm.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Cubic polynomial` or `Hyperbolic tangent`.

### **AM/PM conversion (degrees per dB)** — AM/PM conversion `10` (default) | scalar

AM/PM conversion for the cubic polynomial and the hyperbolic tangent amplifier model,
specified as a scalar in degrees per decibel.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Cubic polynomial` or `Hyperbolic tangent`.

### **Lower input power limit for AM/PM conversion (dBm)** — Minimum input power for which AM/PM conversion scales linearly with input power value `10` (default) | scalar

Minimum input power for which AM/PM conversion scales linearly with the input power
value, specified as a scalar. Below this value, the phase shift resulting from AM/PM
conversion is zero.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Cubic polynomial` or `Hyperbolic tangent`.

### **Upper input power limit for AM/PM conversion (dBm)** — Maximum input power for which AM/PM conversion scales linearly with input power value `inf` (default) | positive scalar

Maximum input power for which AM/PM conversion scales linearly with the input power
value, specified as a positive scalar. Above this value, the phase shift resulting from AM/PM
conversion is constant. The value of this maximum shift is given by:

(AM/PM conversion)⋅(upper input power limit−lower input power limit),

#### Dependencies

To enable this parameter, set **Method** to
`Cubic polynomial` or `Hyperbolic tangent`.

**Tunable:** Yes

### **Input scaling (dB)** — Number that scales input signal level `0` (default) | scalar

Number that scales the input signal level for the Saleh and Ghorbani amplifier model,
specified as scalar in decibels.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Saleh model` or `Ghorbani model`.

### **Output scaling (dB)** — Number that scales output signal level `0` (default) | scalar

Number that scales the output signal level for the Saleh and Ghorbani amplifier model,
specified as scalar in decibels.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Saleh model` or `Ghorbani model`.

### **AM/AM parameters [alpha beta]** — AM/AM parameters for Saleh amplifier model `[2.1587 1.1517]` (default) | vector

AM/AM parameters for the Saleh amplifier model, specified as a vector.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Saleh model`.

### **AM/PM parameters [alpha beta]** — AM/AM parameters for Saleh amplifier model `[4.0033 9.1040]` (default) | vector

AM/PM parameters for the Saleh amplifier model, specified as a vector.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Saleh model`.

### **AM/AM parameters [x1 x2 x3 x4]** — AM/AM parameters for Ghorbani `[8.1081 1.5413 6.5202 -0.0718]` (default) | vector

AM/AM parameters for the Ghorbani amplifier model, specified as a vector.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Ghorbani model`.

### **AM/PM parameters [y1 y2 y3 y4]** — AM/PM parameters for Ghorbani `[4.6645 2.0965 10.88 -0.003]` (default) | vector

AM/PM parameters for the Ghorbani amplifier model, specified as a vector.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Ghorbani model`.

### **Smoothness factor** — Magnitude smoothness factor `0.5` (default) | positive scalar

Magnitude smoothness factor for the Rapp amplifier model, specified as a positive
scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Rapp model`.

### **Output saturation level** — Output saturation level `1` (default) | real positive number

Output saturation level for the Rapp amplifier model , specified as a real positive
number. Scalar specifying the output saturation level.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to
`Rapp model`.

### **Specification method** — Type of noise `Noise factor` (default) | `Noise temperature` | `Noise figure`

Type of noise, specified as `Noise temperature`, `Noise
figure`, and `Noise factor`.

**Tunable:** Yes

### **Noise temperature (K)** — Noise temperature to model the amplifier noise `290` (default) | nonnegative real number

Noise temperature to model the amplifier noise, specified as a nonnegative real number in
kelvin.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Specification
method** to `Noise temperature`.

### **Noise figure (dB)** — Noise figure to model amplifier noise `3.01` (default) | nonnegative real number

Noise figure to model the amplifier noise, specified as a nonnegative real number in
decibels. Setting `Noise figure` to `0` decibels indicates a
noiseless system.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Specification
method** to `Noise figure`.

### **Noise factor** — Noise factor to model amplifier noise `2` (default) | positive integer scalar greater than or equal to 1

Noise factor to model amplifier noise relative to a noise temperature, specified as a
positive integer scalar greater than or equal to 1.

To enable this parameter, set **Specification
method** to `Noise factor`.

**Tunable:** Yes

### **Initial seed** — Seed for random number generator `67987` (default) | nonnegative integer less than 232

Seed for the random number generator, specified as a nonnegative integer less than
232. Use this value to initialize the random number generator the
block uses to generate noise.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Complex baseband model of amplifier with noise

The Amplifier block generates a complex baseband model of an amplifier with thermal noise.
This block provides six methods for modeling nonlinearity and three ways to specify noise.

**Note**

This block assumes a nominal impedance of 1 ohm.
