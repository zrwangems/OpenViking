---
type: simulink-block
title: 'Three-Winding Nonlinear Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'threewindingnonlineartransformer'
documentation_source_path: 'ref/threewindingnonlineartransformer.html'
language: en
---

# Three-Winding Nonlinear Transformer

## Ports

### Conserving

### **1+** — Line 1 positive terminal electrical

Electrical conserving port associated with the positive terminal of
line 1.

### **1-** — Line 1 negative terminal electrical

Electrical conserving port associated with the negative terminal of
line 1.

### **2+** — Line 2 positive terminal electrical

Electrical conserving port associated with the positive terminal of
line 2.

### **2-** — Line 2 negative terminal electrical

Electrical conserving port associated with the negative terminal of
line 2.

### **3+** — Line 3 positive terminal electrical

Electrical conserving port associated with the positive terminal of
line 3.

### **3-** — Line 3 negative terminal electrical

Electrical conserving port associated with the negative terminal of
line 3.

## Parameters

### Main

### **Primary number of turns** — Winding 1 primary turns number `100` (default) | positive scalar integer

Number of turns of wire on the first primary winding of the
transformer.

### **First secondary number of turns** — Winding 2 turns number `200` (default) | positive scalar integer

Number of turns of wire on the first secondary winding of the
transformer.

### **Second secondary number of turns** — Winding 3 turns number `200` (default) | positive scalar integer

Number of turns of wire on the second secondary winding of the
transformer.

### **Primary winding resistance** — Winding 1 resistance `0.01` `Ohm` (default) | nonnegative scalar

Resistance for *R1*, which represents the power loss
of the primary winding.

### **Primary leakage inductance** — Winding 1 leakage inductance `0.0001` `H` (default) | nonnegative scalar

Inductance for *L1*, which represents the magnetic flux loss of the
primary winding.

### **First secondary winding resistance** — Winding 2 resistance `0.01` `Ohm` (default) | nonnegative scalar

Resistance for *R2*, which represents the power loss
of the first secondary winding.

### **First secondary leakage inductance** — Winding 2 leakage inductance `0.0001` `H` (default) | nonnegative scalar

Inductance for *L2*, which represents the magnetic flux loss of the
first secondary winding.

### **Second secondary winding resistance** — Winding 3 resistance `0.01` `Ohm` (default) | nonnegative scalar

Resistance for *R3*, which represents the power loss
of the second secondary winding.

### **Second secondary leakage inductance** — Winding 3 leakage inductance `0.0001` `H` (default) | nonnegative scalar

Inductance for *L3*, which represents the magnetic flux loss of the
second secondary winding.

### Magnetization

### **Magnetization resistance** — Magnetization resistance `100` `Ohm` (default)

Resistance for *Rm*, which represents the magnetic losses in the
transformer core.

### **Magnetization inductance parameterized by** — Nonlinear magnetization inductance parameterization `Single saturation point` (default) | `Single inductance (linear)` | `Magnetic flux versus current characteristic` | `Magnetic flux density versus field strength characteristic` | `Magnetic flux density versus field strength characteristic with hysteresis`

Method of the nonlinear magnetization inductance parameterization:

- `Single inductance (linear)`
  — Provide the unsaturated inductance value.
- `Single saturation point`
  — Provide the values for the unsaturated and
  saturated inductances, as well as saturation magnetic
  flux.
- `Magnetic flux versus current
  characteristic` — Provide the
  current vector and the magnetic flux vector, and then
  populate the magnetic flux versus current lookup table.
- `Magnetic flux density versus field strength
  characteristic` — Provide the values
  for effective core length, cross-sectional area, magnetic
  field strength vector and the magnetic flux density vector,
  and then populate the magnetic flux density versus magnetic
  field strength lookup table.
- `Magnetic flux density versus field strength
  characteristic with hysteresis` —
  Define magnetic flux density as a function or both the
  current value and the history of the field strength by
  providing the number of turns, the effective core length and
  cross-sectional area, the initial anhysteretic B-H curve
  gradient, the magnetic flux density and field strength at a
  certain point on the B-H curve, the coefficient for the
  reversible magnetization, the bulk coupling coefficient, and
  the inter-domain coupling factor.

### **Unsaturated inductance** — Unsaturated inductance `4e-2` `H` (default)

Inductance when the magnetization inductance *Lm* operates in its
linear region.

#### Dependencies

To enable this parameter, set the **Magnetization inductance parameterized
by** parameter to `Single inductance
(linear)` or `Single saturation
point`.

### **Saturated inductance** — Saturated inductance `1e-2` `H` (default)

Inductance when the magnetization inductance *Lm* operates beyond its
saturation point.

#### Dependencies

To enable this parameter, set the **Magnetization
inductance parameterized by** parameter to
`Single saturation point`.

### **Saturation magnetic flux** — Saturation magnetic flux `1.6e-04` `Wb` (default)

Magnetic flux at which the magnetization inductance *Lm*
saturates.

#### Dependencies

To enable this parameter, set the **Magnetization
inductance parameterized by** parameter to
`Single saturation point`.

### **Current vector, i** — Current data `[0, .4, .8, 1.2, 1.6, 2]` `A` (default)

Current data that the block uses to populate the magnetic flux versus current lookup
table.

#### Dependencies

To enable this parameter, set the **Magnetization
inductance parameterized by** parameter to
`Magnetic flux versus current
characteristic`.

### **Magnetic flux vector, phi** — Magnetic flux vector `[0, .161, .25, .284, .295, .299] .* 1e-3` `Wb` (default)

Magnetic flux data that the block uses to populate the magnetic flux versus current
lookup table.

#### Dependencies

To enable this parameter, set the **Magnetization
inductance parameterized by** parameter to
`Magnetic flux versus current
characteristic`.

### **Magnetic field strength vector, H** — Magnetic field strength vector `[0, 200, 400, 600, 800, 1000]` `A/m` (default) | vector

Magnetic field intensity *H*, specified as a vector with the same
number of elements as the magnetic flux density vector
*B*.

#### Dependencies

To enable this parameter, set the **Magnetization
inductance parameterized by** parameter to
`Magnetic flux density versus field strength
characteristic`.

### **Magnetic flux density vector, B** — Magnetic flux density vector `[0, .81, 1.25, 1.42, 1.48, 1.49]` `T` (default) | vector

Magnetic flux density *B*, specified as a vector with
the same number of elements as the magnetic field strength vector
*H*.

#### Dependencies

To enable this parameter, set the **Magnetization
inductance parameterized by** parameter to
`Magnetic flux density versus field strength
characteristic`.

### **Effective length** — Effective core length `0.2` `m` (default) | positive finite scalar

Effective core length. This parameter represents the average length of the magnetic
path around the core.

#### Dependencies

To enable this parameter, set the **Magnetization inductance parameterized
by** parameter to `Magnetic flux density versus field
strength characteristic` or `Magnetic flux density
versus field strength characteristic with hysteresis`.

### **Effective cross-sectional area** — Effective core cross-sectional area `2e-4` `m^2` (default) | positive finite scalar

Effective core cross-sectional area. This parameter
represents the average area of the magnetic path
around the core.

#### Dependencies

To enable this parameter, set the
**Magnetization inductance parameterized
by** parameter to `Magnetic
flux density versus field strength
characteristic` or
`Magnetic flux density versus field
strength characteristic with
hysteresis`.

### **Anhysteretic B-H gradient when H is zero** — Gradient of anhysteretic B-H curve around zero field strength `0.005` `m*T/A` (default) | scalar

Gradient of the anhysteretic *B*-*H* curve around
zero field strength. Set this parameter to the average gradient of the ascending and
descending hysteresis curves.

#### Dependencies

To enable this parameter, set the **Magnetization inductance parameterized
by** parameter to `Magnetic flux density versus field
strength characteristic with hysteresis`.

### **Flux density point on anhysteretic B-H curve** — Flux density point on anhysteretic B-H curve `1.49` `T` (default) | scalar

Flux density of the point for field strength measurement. You must specify a point on the anhysteretic curve by providing its flux density value. To obtain accurate results, pick a point at high field strength where the ascending and descending hysteresis curves align.

#### Dependencies

To enable this parameter, set the **Magnetization inductance parameterized by** parameter to `Magnetic flux density versus field strength characteristic with hysteresis`.

### **Corresponding field strength** — Field strength at measurement point `1000` `A/m` (default) | scalar

Field strength that corresponds to the point that you define using the **Flux density
point on anhysteretic B-H curve** parameter.

#### Dependencies

To enable this parameter, set **Magnetization inductance parameterized by** to `Magnetic flux density versus field strength characteristic with hysteresis`.

### **Coefficient for reversible magnetization, c** — Coefficient for reversible magnetization `0.1` (default) | scalar in the range [0,1]

Coefficient for reversible magnetization in the Jiles-Atherton
equations, *c*. This parameter represents the
proportion of the magnetization that you can reverse.

#### Dependencies

To enable this parameter, set **Magnetization
inductance parameterized by** to
`Magnetic flux density versus magnetic
field strength characteristic with
hysteresis`.

### **Bulk coupling coefficient, K** — Bulk coupling coefficient `200` `A/m` (default) | finite positive scalar

Bulk coupling coefficient in the Jiles-Atherton equations, *K*. This
parameter primarily controls the field strength magnitude at which the
*B*-*H* curve crosses the zero flux density
line.

#### Dependencies

To enable this parameter, set **Magnetization inductance parameterized by** to `Magnetic flux density versus field strength characteristic with hysteresis`.

### **Inter-domain coupling factor, alpha** — Inter-domain coupling factor `1e-4` (default) | scalar

Inter-domain coupling factor in the Jiles-Atherton equations, *α*. This
parameter primarily affects the points at which the
*B*-*H* curves intersect the zero field strength
line. Typical values are in the range of `1e-4` to
`1e-3`.

#### Dependencies

To enable this parameter, set the **Magnetization inductance parameterized by** parameter to `Magnetic flux density versus field strength characteristic with hysteresis`.

### **Interpolation option** — Interpolation option `Linear` (default) | `Smooth`

Lookup table interpolation option. Select one of these interpolation methods:

- `Linear` — Select this option
  to get the best performance.
- `Smooth` — Produce a
  continuous curve with continuous first-order derivatives.

For more information on interpolation algorithms, see the
PS Lookup Table
(1D) block reference page.

#### Dependencies

To enable this parameter, set the **Magnetization
inductance parameterized by** parameter to
`Magnetic flux versus current
characteristic` or `Magnetic flux
density versus field strength characteristic`
.

### Initial Conditions

### **Primary leakage inductance initial current** — Primary leakage inductance initial current `0` `A` (default)

Current through the primary leakage inductance *L1* at time
zero.

### **First secondary leakage inductance initial current** — First secondary leakage inductance initial current `0` `A` (default)

Current through the first secondary leakage inductance *L2* at time
zero.

### **Second secondary leakage inductance initial current** — Second secondary leakage inductance initial current `0` `A` (default)

Current through the second secondary leakage inductance *L3* at time
zero.

### **Specify magnetization inductance initial state by** — Initial state specification option `Current` (default) | `Magnetic flux`

Initial state specification. Choose one of these options:

- `Current` — Specify the
  initial state of the magnetization inductance
  *Lm* by the initial current.
- `Magnetic flux` — Specify
  the initial state of the magnetization inductance
  *Lm* by the magnetic flux.

#### Dependencies

To enable this parameter, on the
**Magnetization** setting, set the
**Magnetization inductance parameterized by**
parameter to:

- `Single inductance
  (linear)`
- `Single saturation
  point`
- `Magnetic flux versus current
  characteristic`
- `Magnetic flux density versus field
  strength characteristic`

### **Magnetization inductance initial current** — Magnetization inductance initial current `0` `A` (default)

Initial current value that the block uses to calculate the magnetic flux within the
magnetization inductance *Lm* at time zero. This
parameter is the current passing through the magnetization inductance
*Lm*. Total magnetization current consists of
current passing through the magnetization resistance
*Rm* and current passing through the magnetization
inductance *Lm*.

#### Dependencies

To enable this parameter, set the **Specify magnetization
inductance initial state by** parameter to
`Current`

### **Magnetization inductance initial magnetic flux** — Magnetization inductance initial magnetic flux `0` `Wb` (default)

Magnetic flux in the magnetization inductance *Lm* at time zero.

#### Dependencies

To enable this parameter, set the **Specify magnetization
inductance initial state by** parameter to
`Magnetic flux`

### **Magnetization inductance initial magnetic flux density** — Magnetization inductance initial magnetic flux density `0` `T` (default)

Magnetic flux density at time zero.

#### Dependencies

To enable this parameter, on the
**Magnetization** setting, set the
**Magnetization inductance parameterized by**
parameter to `Magnetic flux density versus field
strength characteristic with hysteresis`

### **Magnetization inductance initial field strength** — Magnetization inductance initial field strength `0` `A/m` (default)

Magnetic field strength at time zero.

#### Dependencies

To enable this parameter, on the
**Magnetization** setting, set the
**Magnetization inductance parameterized by**
parameter to `Magnetic flux density versus field
strength characteristic with hysteresis`

### Parasitics

### **Primary leakage inductance parasitic parallel conductance** — Winding 1 leakage inductance parasitic parallel conductance `1e-9` `1/Ohm` (default) | nonneagative scalar

Small parasitic effects in parallel to the primary leakage inductance
*L1*. To simulate some circuit topologies, you need
a small parallel conductance.

### **First secondary leakage inductance parasitic parallel conductance** — Winding 2 leakage inductance parasitic parallel conductance `1e-9` `1/Ohm` (default) | nonneagative scalar

Small parasitic effects in parallel to the first secondary leakage inductance
*L2*. To simulate some circuit topologies, you
need a small parallel conductance.

### **Second secondary leakage inductance parasitic parallel conductance** — Winding 3 leakage inductance parasitic parallel conductance `1e-9` `1/Ohm` (default) | nonneagative scalar

Small parasitic effects in parallel to the second secondary leakage inductance
*L3*. To simulate some circuit topologies, you
need a small parallel conductance.

## Libraries

Simscape / Electrical / Passive / Transformers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Single-phase nonlinear three-winding transformer

The Three-Winding Nonlinear Transformer block represents a
single-phase, nonlinear, three-winding transformer with a nonideal core. A core may be
nonideal due to its magnetic properties or dimensions. This figure shows the equivalent
circuit topology,

where:

- *R1* is the primary winding resistance.
- *L1* is the primary leakage inductance.
- *R2* is the first secondary winding resistance.
- *L2* is the first secondary leakage inductance.
- *R3* is the second secondary winding resistance.
- *L3* is the second secondary leakage inductance.
- *Rm* is the magnetization resistance.
- *Lm* is the magnetization inductance.

To parameterize the nonlinear magnetization inductance, set the
**Magnetization inductance parameterized by** parameter to one of
these options:

- `Single inductance (linear)`
- `Single saturation point`
- `Magnetic flux versus current characteristic`
- `Magnetic flux density versus magnetic field strength
  characteristic`
- `Magnetic flux density versus magnetic field strength
  characteristic with hysteresis`

For more information about these parameterization options including the equations that the
block uses to model nonlinear magnetization inductance, see the Nonlinear Inductor block reference page.

Simscape™ and Simscape
Electrical™ libraries include several blocks than can model the same type of transformer device. However, these blocks make different modeling assumptions. To choose the right block for your application, you must understand how these assumptions impact the block behavior as a function of frequency. For more information, see Choose Blocks to Model Transformers.
