---
type: simulink-block
title: 'Nonlinear Inductor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Basic'
documentation_page: 'nonlinearinductor'
documentation_source_path: 'ref/nonlinearinductor.html'
language: en
---

# Nonlinear Inductor

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative
terminal.

## Parameters

### Main

### **Parameterized by** — Block parameterization `Single saturation point` (default) | `Single inductance (linear)` | `Magnetic flux versus current characteristic` | `Magnetic flux density versus magnetic field strength characteristic` | `Magnetic flux density versus magnetic field strength characteristic with hysteresis`

Parameterization method that you use to describe the
*B*-*H* curve. Choose one of these
options:

- `Single inductance (linear)`
  — Provide the values for number of turns, unsaturated
  inductance, and parasitic parallel conductance.
- `Single saturation point`
  — Provide the values for number of turns, unsaturated
  and saturated inductances, saturation magnetic flux, and
  parasitic parallel conductance.
- `Magnetic flux versus current
  characteristic` — In addition to the
  number of turns and the parasitic parallel conductance
  value, provide the current vector and the magnetic flux
  vector, to populate the magnetic flux versus current lookup
  table.
- `Magnetic flux density versus magnetic field
  strength characteristic` — In
  addition to the number of turns and the parasitic parallel
  conductance value, provide the values for effective core
  length and cross-sectional area, as well as the magnetic
  field strength vector and the magnetic flux density vector,
  to populate the magnetic flux density versus magnetic field
  strength lookup table.
- `Magnetic flux density versus magnetic field
  strength characteristic with hysteresis`
  — In addition to the number of turns and the
  effective core length and cross-sectional area, provide the
  values for the initial anhysteretic
  *B*-*H* curve
  gradient, the magnetic flux density and field strength at a
  certain point on the
  *B*-*H* curve, as well
  as the coefficient for the reversible magnetization, bulk
  coupling coefficient, and inter-domain coupling factor, to
  define magnetic flux density as a function of both the
  current value and the history of the field strength.

### **Number of turns** — Total number of turns `10` (default)

Total number of turns of wire wound around the inductor core.

### **Unsaturated inductance** — Unsaturated inductance `2e-4` `H` (default)

Inductance when the inductor operates in its linear region.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Single inductance
(linear)` or `Single saturation
point`.

### **Saturated inductance** — Saturated inductance `1e-4` `H` (default)

Inductance when the inductor operates beyond its saturation
point.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Single saturation
point`.

### **Saturation magnetic flux** — Saturation magnetic flux `1.3e-05` `Wb` (default)

Magnetic flux at which the inductor saturates.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Single saturation
point`.

### **Current vector, i** — Current data vector `[0, .64, 1.28, 1.92, 2.56, 3.2]` `A` (default)

Current data that the block uses to populate the magnetic flux versus
current lookup table.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux versus current
characteristic`.

### **Magnetic flux vector, phi** — Magnetic flux data `[0, 1.29, 2, 2.27, 2.36, 2.39] .* 1e-5` `Wb` (default)

Magnetic flux data that the block uses to populate the magnetic flux
versus current lookup table.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux versus current
characteristic`.

### **Magnetic field strength vector, H** — Magnetic field strength vector `[0, 200, 400, 600, 800, 1000]` `A/m` (default) | vector

Magnetic field intensity *H*, specified as a vector
with the same number of elements as the magnetic flux density vector
*B*.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic`.

### **Magnetic flux density vector, B** — Magnetic flux density data `[0, .81, 1.25, 1.42, 1.48, 1.49]` `T` (default) | vector

Magnetic flux density *B*, specified as a vector with
the same number of elements as the magnetic field strength vector
*H*.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic`.

### **Effective length** — Effective core length `0.032` `m` (default) | positive finite scalar

Effective core length. This parameter represents the average length of
the magnetic path around the core.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic` or
`Magnetic flux density versus magnetic field
strength characteristic with hysteresis`.

### **Effective cross-sectional area** — Effective core cross-sectional area `1.6e-5` `m^2` (default) | positive finite scalar

Effective core cross-sectional area. This parameter represents the
average area of the magnetic path around the core.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic` or
`Magnetic flux density versus magnetic field
strength characteristic with hysteresis`.

### **Anhysteretic B-H gradient when H is zero** — Gradient of anhysteretic B-H curve around zero field strength `0.005` `m*T/A` (default) | scalar

Gradient of the anhysteretic *B*-*H*
curve around zero field strength. Set this parameter to the average
gradient of the ascending and descending hysteresis curves.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic with
hysteresis`.

### **Flux density point on anhysteretic B-H curve** — Flux density point on anhysteretic B-H curve `1.49` `T` (default) | scalar

Flux density of the point for field strength measurement. You must
specify a point on the anhysteretic curve by providing its flux density
value. To obtain accurate results, pick a point at high field strength
where the ascending and descending hysteresis curves align.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic with
hysteresis`.

### **Corresponding field strength** — Corresponding field strength `1000` `A/m` (default) | scalar

Field strength that corresponds to the point that you define by the
**Flux density point on anhysteretic B-H curve**
parameter.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic with
hysteresis`.

### **Coefficient for reversible magnetization, c** — Coefficient for reversible magnetization `0.1` (default) | scalar in the range [0,1]

Coefficient for reversible magnetization in the Jiles-Atherton
equations, *c*. This parameter represents the
proportion of the magnetization that you can reverse.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic with
hysteresis`.

### **Bulk coupling coefficient, K** — Bulk coupling coefficient `200` `A/m` (default) | finite positive scalar

Bulk coupling coefficient in the Jiles-Atherton equations,
*K*. This parameter primarily controls the field
strength magnitude at which the
*B*-*H* curve crosses the zero
flux density line.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic with
hysteresis`.

### **Inter-domain coupling factor, alpha** — Inter-domain coupling factor `1e-4` (default) | scalar

Inter-domain coupling factor in the Jiles-Atherton equations,
*α*. This parameter primarily affects the points at
which the *B*-*H* curves intersect the
zero field strength line. Typical values are in the range of
`1e-4` to `1e-3`.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic with
hysteresis`.

### **Averaging period for power logging** — Averaging period for power logging `0` `s` (default) | scalar

Averaging period for the hysteresis losses calculation. These losses
are proportional to the area enclosed by the
*B*-*H* trajectory. If you excite
the block at a known, fixed frequency, you can set this value to the
corresponding excitation period to calculate the hysteresis loss. The
block logs the hysteresis loss once per AC cycle in the
`power_dissipated` variable in the logged
simulation data. If you are using a fixed-step solver, this value must
be an integer multiple of the simulation step size.

If you do not excite the block at a known, fixed frequency, set this
parameter to `0`. The block sets the
`power_dissipated` variable in the logged
simulation data to `0`. You can calculate the actual
hysteresis loss by post-processing the
`power_instantaneous` variable in the logged
simulation data.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux density versus
magnetic field strength characteristic with
hysteresis`.

### **Parasitic parallel conductance** — Parasitic parallel conductance `1e-9` `1/Ohm` (default)

Parasitic parallel conductance. Use this parameter to represent small
parasitic effects. For some circuit topologies, you need a small
parallel conductance.

### **Interpolation option** — Interpolation option `Linear` (default) | `Smooth`

Lookup table interpolation option. Select one of the following
interpolation methods:

- `Linear` — Select this option
  to get the best performance.
- `Smooth` — Select this option
  to produce a continuous curve with continuous first-order
  derivatives.

For more information about interpolation algorithms, see the
PS Lookup Table
(1D) block reference page.

#### Dependencies

To enable this parameter, set **Parameterized
by** to `Magnetic flux versus current
characteristic` or `Magnetic flux
density versus magnetic field strength
characteristic`.

### Initial Conditions

### **Specify initial state by** — Initial state specification option `Current` (default) | `Magnetic flux`

Initial state specification. Choose one of these options:

- `Current` — Specify the
  initial state of the inductor by the initial current through
  the inductor
  *i*L.
- `Magnetic flux` — Specify
  the initial state of the inductor by the magnetic flux.

#### Dependencies

To enable this parameter, in the **Main**
settings, set the **Parameterized by** parameter to
one of these options:

- `Single inductance
  (linear)`
- `Single saturation
  point`
- `Magnetic flux versus current
  characteristic`
- `Magnetic flux density versus magnetic field
  strength characteristic`

### **Initial current** — Initial current `0` `A` (default)

Initial current value that the block uses to calculate the value of
magnetic flux at time zero. This parameter is the current passing
through the inductor. Component current consists of current passing
through the inductor and current passing through the parasitic parallel
conductance.

#### Dependencies

To enable this parameter, set **Specify initial state
by** to `Current`.

### **Initial magnetic flux** — Initial magnetic flux `0` `Wb` (default)

Magnetic flux at time zero.

#### Dependencies

To enable this parameter, set **Specify initial state
by** to `Magnetic
flux`.

### **Initial magnetic flux density** — Initial magnetic flux density `0` `T` (default)

Magnetic flux density at time zero.

#### Dependencies

To enable this parameter, in the **Main**
settings, set the **Parameterized by** parameter to
`Magnetic flux density versus magnetic field
strength characteristic with hysteresis`.

### **Initial field strength** — Initial field strength `0` `A/m` (default)

Magnetic field strength at time zero.

#### Dependencies

To enable this parameter, in the **Main**
settings, set the **Parameterized by** parameter to
`Magnetic flux density versus magnetic field
strength characteristic with hysteresis`.

## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

## Description

Inductor with nonideal core

The Nonlinear Inductor block represents an inductor
with a nonideal core. A core may be nonideal due to its magnetic properties and
dimensions. To choose between these parameterization options, use the
**Parameterized by** parameter:

- Single inductance
  (linear)
- Single saturation
  point
- Magnetic flux versus
  current characteristic
- Magnetic flux density
  versus magnetic field strength characteristic
- Magnetic flux density
  versus magnetic field strength characteristic with hysteresis

### Single Inductance (Linear)

These equations define the relationships between voltage, current, and
flux,

i=iL+vGp

v=NwdΦdt

Φ=LNwiL

where:

- *v* is the terminal voltage.
- *i* is the terminal current.
- *i*L is the current through
  inductor.
- *G*p is the parasitic parallel
  conductance.
- *N*w is the number of winding
  turns.
- *Φ* is the magnetic flux.
- *L* is the unsaturated inductance.

### Single Saturation Point

These equations define the relationships between voltage, current, and
flux,

i=iL+vGp

v=NwdΦdt

Φ=LNwiL (for unsaturated)

Φ=LsatNwiL±Φoffset (for saturated)

where:

- *v* is the terminal voltage.
- *i* is the terminal current.
- *i*L is the current through
  inductor.
- *G*p is the parasitic parallel
  conductance.
- *N*w is the number of winding
  turns.
- *Φ* is the magnetic flux.
- *Φ*offset is the magnetic flux
  saturation offset.
- *L* is the unsaturated inductance.
- *L*sat is the saturated
  inductance.

### Magnetic Flux Versus Current Characteristic

These equations define the relationships between voltage, current, and
flux,

i=iL+vGp

v=NwdΦdt

Φ=f(iL)

where:

- *v* is the terminal voltage.
- *i* is the terminal current.
- *i*L is the current through
  inductor.
- *G*p is the parasitic parallel
  conductance.
- *N*w is the number of winding
  turns.
- *Φ* is the magnetic flux.

The block determines magnetic flux by using a one-dimensional table lookup, based
on the vector of electrical current values and the vector of corresponding magnetic
flux values that you provide. You can construct these vectors using negative and
positive data, or positive data only. If you use positive data only, the first
element of the vector must be 0. The block calculates negative values by rotating
the positive data by 180° about (0,0).

### Magnetic Flux Density Versus Magnetic Field Strength Characteristic

These equations define the relationships between voltage, current, and
flux,

i=iL+vGp

v=NwdΦdt

Φ=B⋅Ae

B=f(H)

H=NwleiL

where:

- *v* is the terminal voltage.
- *i* is the terminal current.
- *i*L is the current through
  inductor.
- *G*p is the parasitic parallel
  conductance.
- *N*w is the number of winding
  turns.
- *Φ* is the magnetic flux.
- *B* is the magnetic flux density.
- *H* is the magnetic field strength.
- *l*e is the effective core length.
- *A*e is the effective core
  cross-sectional area.

The block determines the magnetic flux density by one-dimensional table lookup,
based on the vector of magnetic field strength values and the vector of
corresponding magnetic flux density values that you provide. You can construct these
vectors using either negative and positive data, or positive data only. If you use
positive data only, the first element of the vector must be 0. The block calculates
negative values by rotating the positive data by 180° about (0,0).

### Magnetic Flux Density Versus Magnetic Field Strength Characteristic with Hysteresis

These equations define the relationships between voltage, current, and
flux,

i=iL+vGp

v=NwdΦdt

Φ=B⋅Ae

B=μ0(H+M)

H=NwleiL

where:

- *v* is the terminal voltage.
- *i* is the terminal current.
- *i*L is the current through
  inductor.
- *G*p is the parasitic parallel
  conductance.
- *N*w is the number of winding
  turns.
- *Φ* is the magnetic flux.
- *B* is the magnetic flux density.
- *μ*0 is the magnetic permeability
  of a vacuum.
- *H* is the magnetic field strength.
- *M* is the magnetization of the inductor core.
- *l*e is the effective core length.
- *A*e is the effective core
  cross-sectional area.

The magnetization acts to increase the magnetic flux density, and its value
depends on both the current value and the history of the field strength. The block
uses the Jiles-Atherton 1, 2] equations to
determine *M* at any given time. This figure shows a typical plot
of the resulting relationship between *B* and *H*.

As the field strength increases from *H* = 0, the plot initially follows an ascending hysteresis curve. At the
saturation point, further increases in field intensity no longer cause significant
increases in magnetic flux.

As you reduce the magnetic field strength from the saturation point, the plot
follows a descending hysteresis curve. The difference between ascending and
descending curves is due to the dependence of *M* on the trajectory
history. Physically, the behavior corresponds to magnetic dipoles in the core
aligning as the field strength increases, but not then fully recovering to their
original position as field strength decreases.

The starting point for the Jiles-Atherton equation is the split of the
magnetization effect into two parts, one part that is purely a function of effective
field strength *Heff* and another,
irreversible part that depends on history. This equation defines the relative
contributions of the anhysteretic magnetisation
*Man* and the irreversible magnetization
*Mirr* to the total magnetization
*M*,

M=cMan+(1−c)Mirr,

where *c* is the coefficient for reversible magnetization.

This equation relates *Man* to the
equivalent magnetization*Heff*:

Man=Ms(coth(Heffa)−aHeff).

The function defines a saturation curve with limiting values
±*Ms*, where:

- *M*s is the
  *saturation magnetization*.
- *a* is the *anhysteretic magnetization
  coefficient*, which determines the point of saturation.
  It approximately describes the average of the two hysteretic
  curves.

In the Nonlinear Inductor block mask, you provide
values for dMan/dHeff when *H*eff = 0 and a point [*H*1,
*B*1] on the anhysteretic
*B*-*H* curve. The block uses these values to
determine values for *a* and
*M*s.

The Jiles-Atherton model defines the irreversible term by a partial derivative
with respect to field strength,

dMirrdH=Man−MirrKδ−α(Man−Mirr)δ={1if dHdt≥0−1if dHdt<0

where:

- *K* is the *bulk coupling
  coefficient*, which shapes the irreversible
  characteristic.
- *α* is the *inter-domain coupling
  factor*.

Comparison of the equation with a standard first-order differential equation
reveals that as you change the total field strength *H*, the
irreversible term *Mirr* attempts to track
the reversible term *Man*, but with a
variable tracking gain of 1/(Kδ−α(Man−Mirr)). The tracking error acts to create the hysteresis at the points
where *δ* changes sign.

This equation defines the effective field strength of an anhysteretic
curve,

Heff=H+αM.

The value of *α* affects the shape of the hysteresis curve. Larger
values act to increase the *B*-axis intercepts. However, the
stability term Kδ−α(Man−Mirr) must be positive for *δ* > 0 and negative for *δ* < 0. There are therefore limits on the values of *α*
that you can provide. A typical maximum value is of the order 1e-3.

**Procedure for Finding Approximate Values for Jiles-Atherton (JA) Equation
Coefficients**

You can determine representative values for the equation coefficients using
this procedure:

1. Provide a value for the **Anhysteretic B-H gradient when H is
   zero** parameter (dMan/dHeff when *Heff* =
   0) and a data point
   [*H*1,
   *B1*] on the
   anhysteretic *B*-*H* curve. From these
   values, the block initialization determines values for
   *α* and
   *M*s.
2. Set the **Coefficient for reversible magnetization,
   c** parameter to achieve correct initial
   *B*-*H* gradient when starting a
   simulation from [*H*
   *B*] = [0 0]. The value of *c* is approximately
   the ratio of this initial gradient to the **Anhysteretic B-H
   gradient when H is zero**. The value of
   *c* must be greater than 0 and less than 1.
3. Set the **Bulk coupling coefficient, K** parameter to
   the approximate magnitude of *H* when
   *B* = 0 on the ascending hysteresis curve.
4. Start with a very small value for the **Inter-domain coupling
   factor, alpha** parameter, and gradually increase it to
   tune the value of *B* when crossing the
   *H* = 0 line. A typical value is in the range of
   1e-4 to 1e-3. Values that are too large cause the gradient of the
   *B*-*H* curve to tend to infinity,
   which is nonphysical and generates a run-time assertion error.

To get a good match against a predefined
*B*-*H* curve, iterate on these four
steps.
