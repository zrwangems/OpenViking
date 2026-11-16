---
type: simulink-block
title: 'Nonlinear Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'nonlineartransformer'
documentation_source_path: 'ref/nonlineartransformer.html'
language: en
---

# Nonlinear Transformer

## Ports

### Conserving

### **1+** — Primary winding positive polarity electrical

Electrical conserving port associated with the primary winding positive
polarity.

### **1-** — Primary winding negative polarity electrical

Electrical conserving port associated with the primary winding negative
polarity.

### **2+** — Secondary winding positive polarity electrical

Electrical conserving port associated with the secondary winding positive
polarity.

### **2-** — Secondary winding negative polarity electrical

Electrical conserving port associated with the secondary winding negative
polarity.

## Parameters

### Main

### **Primary number of turns** — Primary number of turns `100` (default)

Number of turns of wire on the primary winding of the transformer.

### **Secondary number of turns** — Secondary number of turns `200` (default)

Number of turns of wire on the secondary winding of the transformer.

### **Winding parameterized by** — Winding leakage parameterization `Combined primary and secondary values` (default) | `Separate primary and secondary values`

Parameterization option for winding leakage. Choose one of these methods:

- `Combined primary and secondary values` —
  Use the lumped resistance and inductance values to represent the combined
  leakage in the primary and secondary windings.
- `Separate primary and secondary values` —
  Use separate resistances and inductances to represent leakages in the primary
  and secondary windings.

### **Combined winding resistance** — Combined winding resistance `0.01` `Ohm` (default)

Lumped equivalent resistance *Req*, which represents the combined
power loss of the primary and secondary windings.

#### Dependencies

To enable this parameter, set **Winding parameterized by** to
`Combined primary and secondary values`.

### **Combined leakage inductance** — Combined leakage inductance `0.0001` `H` (default)

Lumped equivalent inductance *Leq*, which represents the combined
magnetic flux loss of the primary and secondary windings.

#### Dependencies

To enable this parameter, set **Winding parameterized by** to
`Combined primary and secondary values`.

### **Primary winding resistance** — Primary winding resistance `0.01` `Ohm` (default)

Resistance *R1*, which represents the power loss of the primary
winding.

#### Dependencies

To enable this parameter, set **Winding parameterized by** to
`Separate primary and secondary values`.

### **Primary leakage inductance** — Primary leakage inductance `0.0001` `H` (default)

Inductance *L1*, which represents the magnetic flux loss of the
primary winding.

#### Dependencies

To enable this parameter, set **Winding parameterized by** to
`Separate primary and secondary values`.

### **Secondary winding resistance** — Secondary winding resistance `0.01` `Ohm` (default)

Resistance *R2*, which represents the power loss of the secondary
winding.

#### Dependencies

To enable this parameter, set **Winding parameterized by** to
`Separate primary and secondary values`.

### **Secondary leakage inductance** — Secondary leakage inductance `0.0001` `H` (default)

Inductance *L2*, which represents the magnetic flux loss of the
secondary winding.

#### Dependencies

To enable this parameter, set **Winding parameterized by** to
`Separate primary and secondary values`.

### **Averaging period for power logging** — Averaging period for power logging `0` `s` (default)

Averaging period for power logging.

### Magnetization

### **Magnetization resistance** — Magnetization resistance `100` `Ohm` (default)

Resistance *Rm*, which represents the magnetic losses in the
transformer core.

### **Magnetization inductance parameterized by** — Nonlinear magnetization inductance parameterization `Single saturation point` (default) | `Single inductance (linear)` | `Magnetic flux versus current characteristic` | `Magnetic flux density versus field strength characteristic` | `Magnetic flux density versus field strength characteristic with hysteresis`

Select one of the following methods for the nonlinear magnetization inductance parameterization:

- `Single inductance (linear)` — Provide the
  unsaturated inductance value.
- `Single saturation point` — Provide the
  values for the unsaturated and saturated inductances, as well as saturation
  magnetic flux.
- `Magnetic flux versus current characteristic`
  — Provide the current vector and the magnetic flux vector, to populate
  the magnetic flux versus current lookup table.
- `Magnetic flux density versus field strength
  characteristic` — Provide the values for effective core
  length and cross-sectional area, as well as the magnetic field strength vector
  and the magnetic flux density vector, to populate the magnetic flux density
  versus magnetic field strength lookup table.
- `Magnetic flux density versus field strength characteristic with
  hysteresis` — In addition to the number of turns and the
  effective core length and cross-sectional area, provide the values for the
  initial anhysteretic *B*-*H* curve gradient,
  the magnetic flux density and field strength at a certain point on the
  *B*-*H* curve, as well as the coefficient
  for the reversible magnetization, bulk coupling coefficient, and inter-domain
  coupling factor, to define magnetic flux density as a function of both the
  current value and the history of the field strength.

### **Unsaturated inductance** — Unsaturated inductance `4e-2` `H` (default)

Inductance when the magnetization inductance *Lm* operates in its
linear region.

#### Dependencies

To enable this parameter, set **Magnetization inductance parameterized
by** to `Single inductance (linear)` or
`Single saturation point`.

### **Saturated inductance** — Saturated inductance `1e-2` `H` (default)

Inductance when the magnetization inductance *Lm* operates beyond
its saturation point.

#### Dependencies

To enable this parameter, set **Magnetization inductance parameterized
by** to `Single saturation point`.

### **Saturation magnetic flux** — Saturation magnetic flux `1.6e-04` `Wb` (default)

Magnetic flux at which the magnetization inductance *Lm*
saturates.

#### Dependencies

To enable this parameter, set **Magnetization inductance parameterized
by** to `Single saturation point`.

### **Current vector, i** — Current data `[0, .4, .8, 1.2, 1.6, 2]` `A` (default)

Current data that the block uses to populate the magnetic flux versus current
lookup table.

#### Dependencies

To enable this parameter, set **Magnetization inductance parameterized
by** to `Magnetic flux versus current
characteristic`.

### **Magnetic flux vector, phi** — Magnetic flux vector `[0, .161, .25, .284, .295, .299] .* 1e-3` `Wb` (default)

Magnetic flux data that the block uses to populate the magnetic flux versus
current lookup table.

#### Dependencies

To enable this parameter, set **Magnetization inductance parameterized
by** to `Magnetic flux versus current
characteristic`.

### **Magnetic field strength vector, H** — Magnetic field strength `[0, 200, 400, 600, 800, 1000]` `A/m` (default) | vector

Magnetic field intensity *H*, specified as a vector with the same
number of elements as the magnetic flux density vector *B*.

#### Dependencies

To enable this parameter, set **Magnetization inductance parameterized
by** to `Magnetic flux density versus field strength
characteristic`.

### **Magnetic flux density vector, B** — Magnetic flux density `[0, .81, 1.25, 1.42, 1.48, 1.49]` `T` (default) | vector

Magnetic flux density *B*, specified as a vector with the same
number of elements as the magnetic field strength vector *H*.

#### Dependencies

To enable this parameter, set **Magnetization inductance parameterized
by** to `Magnetic flux density versus field strength
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

Lookup table interpolation option. Select one of the following interpolation
methods:

- `Linear` — Select this option to get the best
  performance.
- `Smooth` — Select this option to produce a
  continuous curve with continuous first-order derivatives.

For more information on interpolation algorithms, see the PS Lookup Table (1D) block reference page.

#### Dependencies

To enable this parameter, set **Magnetization inductance parameterized
by** to `Magnetic flux versus current
characteristic` or `Magnetic flux density versus field
strength characteristic`.

### Initial Conditions

### **Combined leakage inductance initial current** — Combined leakage inductance initial current `0` `A` (default)

Current through the combined leakage inductance *Leq* at time
zero.

#### Dependencies

To enable this parameter, in the **Main** settings, set the
**Winding parameterized by** parameter to `Combined
primary and secondary values`.

### **Primary leakage inductance initial current** — Primary leakage inductance initial current `0` `A` (default)

Current through the primary leakage inductance *L1* at time
zero.

#### Dependencies

To enable this parameter, in the **Main** settings, set the
**Winding parameterized by** parameter to `Separate
primary and secondary values`.

### **Secondary leakage inductance initial current** — Secondary leakage inductance initial current `0` `A` (default)

Current through the secondary leakage inductance *L2* at time
zero.

#### Dependencies

To enable this parameter, in the **Main** settings, set the
**Winding parameterized by** parameter to `Separate
primary and secondary values`.

### **Specify magnetization inductance initial state by** — Initial state specification option `Current` (default) | `Magnetic flux`

Initial state specification method. Choose one of these options:

- `Current` — Specify the initial state of the
  magnetization inductance *Lm* by the initial current.
- `Magnetic flux` — Specify the initial state
  of the magnetization inductance *Lm* by the magnetic flux.

#### Dependencies

To enable this parameter, in the **Magnetization** settings,
set the **Magnetization inductance parameterized by** parameter to
one of these options:

- `Single inductance (linear)`
- `Single saturation point`
- `Magnetic flux versus current
  characteristic`
- `Magnetic flux density versus magnetic field strength
  characteristic`

### **Magnetization inductance initial current** — Magnetization inductance initial current `0` `A` (default)

Initial current value that the block uses to calculate the magnetic flux within
the magnetization inductance *Lm* at time zero. This parameter is the
current passing through the magnetization inductance *Lm*. Total
magnetization current consists of current passing through the magnetization resistance
*Rm* and current passing through the magnetization inductance
*Lm*.

#### Dependencies

To enable this parameter, set **Specify magnetization inductance initial
state by** to `Current`.

### **Magnetization inductance initial magnetic flux** — Magnetization inductance initial magnetic flux `0` `Wb` (default)

Magnetic flux in the magnetization inductance *Lm* at time
zero.

#### Dependencies

To enable this parameter, set **Specify magnetization inductance initial
state by** to `Magnetic flux`.

### **Magnetization inductance initial magnetic flux density** — Magnetization inductance initial magnetic flux density `0` `T` (default)

Magnetic flux density at time zero.

#### Dependencies

To enable this parameter, in the **Magnetization** settings,
set the **Magnetization inductance parameterized by** parameter to
`Magnetic flux density versus field strength characteristic with
hysteresis`.

### **Magnetization inductance initial field strength** — Magnetization inductance initial field strength `0` `A/m` (default)

Magnetic field strength at time zero.

#### Dependencies

To enable this parameter, in the **Magnetization** settings,
set the **Magnetization inductance parameterized by** parameter to
`Magnetic flux density versus field strength characteristic with
hysteresis`.

### Parasitics

### **Combined leakage inductance parasitic parallel conductance** — Combined leakage inductance parasitic parallel conductance `1e-9` `1/Ohm` (default)

Use this parameter to represent small parasitic effects in parallel to the
combined leakage inductance *Leq*. To simulate some circuit
topologies, you need a small parallel conductance.

#### Dependencies

To enable this parameter, in the **Main** settings, set
**Winding parameterized by** to `Combined primary and
secondary values`.

### **Primary leakage inductance parasitic parallel conductance** — Primary leakage inductance parasitic parallel conductance `1e-9` `1/Ohm` (default)

Use this parameter to represent small parasitic effects in parallel to the primary
leakage inductance *L1*. To simulate some circuit topologies, you
need a small parallel conductance.

#### Dependencies

To enable this parameter, in the **Main** settings, set
**Winding parameterized by** to `Separate primary and
secondary values`.

### **Secondary leakage inductance parasitic parallel conductance** — Secondary leakage inductance parasitic parallel conductance `1e-9` (default)

Use this parameter to represent small parasitic effects in parallel to the
secondary leakage inductance *L2*. To simulate some circuit
topologies, you need a small parallel conductance.

#### Dependencies

To enable this parameter, in the **Main** settings, set
**Winding parameterized by** to `Separate primary and
secondary values`.

## Libraries

Simscape / Electrical / Passive / Transformers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

## Description

Transformer with nonideal core

The Nonlinear Transformer block represents a transformer
with a nonideal core. A core may be nonideal due to its magnetic properties and dimensions.
The equivalent circuit topology depends upon the option you choose to parameterize the winding
leakage.

If you set **Winding parameterized by** to `Combined primary
and secondary values`, you use lumped resistance and inductance values to
represent the combined leakage in the primary and secondary windings.

In this diagram:

- *Req* is the combined winding resistance.
- *Leq* is the combined leakage inductance.
- *L2* is the secondary leakage inductance.
- *Rm* is the magnetization resistance.
- *Lm* is the magnetization inductance.

If you set **Winding parameterized by** to `Separate primary
and secondary values`, you use separate resistances and inductances to
represent leakages in the primary and secondary windings.

In this diagram:

- *R1* is the primary winding resistance.
- *L1* is the primary leakage inductance.
- *R2* is the secondary winding resistance.
- *L2* is the secondary leakage inductance.
- *Rm* is the magnetization resistance.
- *Lm* is the magnetization inductance.

To parameterize the nonlinear magnetization inductance, set the **Magnetization
inductance parameterized by** parameter to one of these options:

- `Single inductance (linear)`
- `Single saturation point`
- `Magnetic flux versus current characteristic`
- `Magnetic flux density versus magnetic field strength
  characteristic`
- `Magnetic flux density versus magnetic field strength characteristic with
  hysteresis`

For more information about these parameterization options including the equations that the
block uses to model nonlinear magnetization inductance, see the Nonlinear
Inductor block reference page.

Simscape™ and Simscape
Electrical™ libraries include several blocks than can model the same type of transformer device. However, these blocks make different modeling assumptions. To choose the right block for your application, you must understand how these assumptions impact the block behavior as a function of frequency. For more information, see Choose Blocks to Model Transformers.
