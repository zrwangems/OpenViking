---
type: simulink-block
title: 'Magnetic Core'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'magneticcore'
documentation_source_path: 'ref/magneticcore.html'
language: en
---

# Magnetic Core

## Ports
```yaml
ports:
- name: N
  summary: North terminal magnetic
  direction: conserving
- name: S
  summary: South terminal magnetic
  direction: conserving
- name: H
  summary: Thermal mass thermal
  direction: conserving
```

### Conserving

### **N** — North terminal magnetic

Magnetic conserving port associated with the north terminal.

### **S** — South terminal magnetic

Magnetic conserving port associated with the south terminal.

### **H** — Thermal mass thermal

Thermal port associated with the thermal mass.

#### Dependencies

To enable this port, select the **Model thermal effects**
parameter.
## Parameters
```yaml
parameters:
- name: Effective length
  summary: Effective core length 0.032 m (default) | positive finite scalar
  group: Main
- name: Effective cross-sectional area
  summary: Effective core cross-sectional area 1.6e-5 m^2 (default) | positive finite scalar
  group: Main
- name: Parameterization option
  summary: Parameterization method Magnetic Characteristics (default) | Jiles-Atherton Model | Saturated BH Curve
  group: Main
- name: Magnetic remanence of saturation cycle
  summary: Residual magnetism 0.68 T (default) | positive scalar
  group: Main
- name: Magnetic coercivity of saturation cycle
  summary: Magnitude of field strength to demagnetize core 151 A/m (default) | positive scalar
  group: Main
- name: Magnetic flux density at saturation point
  summary: Maximum flux density magnitude 1.25 T (default) | positive scalar
  group: Main
- name: Magnetic field intensity at saturation point
  summary: Field intensity at saturation point 3000 A/m (default) | positive scalar
  group: Main
- name: Saturation magnetization, Ms
  summary: Saturation magnetization, Ms 1e6 A/m (default) | positive finite scalar
  group: Main
- name: Anhysteretic magnetization coefficient, a
  summary: Anhysteretic magnetization coefficient, a 82 A/m (default) | finite positive scalar
  group: Main
- name: Inter-domain coupling factor, alpha
  summary: Inter-domain coupling factor, alpha 0.0001 (default) | scalar
  group: Main
- name: Coefficient for reversible magnetization, c
  summary: Coefficient for reversible magnetization 0.1 (default) | scalar in the range [0,1]
  group: Main
- name: Bulk coupling coefficient, k
  summary: Bulk coupling coefficient 200 A/m (default) | finite positive scalar
  group: Main
- name: Magnetic flux density, B(H)
  summary: Magnetic flux density vector [-1.25,-0.68,0,0.885,1.124,1.25] T (default) | vector
  group: Main
- name: Magnetic field intensity, H
  summary: Magnetic field intensity vector [-3000,0,151,500,1000,3000] A/m (default) | vector
  group: Main
- name: Averaging period for hysteresis losses
  summary: Averaging period for hysteresis loss calculation 1e-3 s (default) | positive scalar
  group: Losses
- name: Model eddy losses
  summary: Option to model eddy losses Off (default) | On
  group: Losses
- name: Geometrical coefficient
  summary: Geometrical coefficient 6 (default) | positive scalar
  group: Losses
- name: Thickness of laminations
  summary: Characteristic cross-sectional dimension 1 mm (default) | positive scalar
  group: Losses
- name: Electrical resistivity
  summary: Electrical resistivity of core 1.03e-7 Ohm*m (default) | positive scalar
  group: Losses
- name: Model thermal effects
  summary: Option to model thermal effects Off (default) | On
  group: Thermal
- name: Thermal mass
  summary: Thermal mass associated with H port 2 J/K (default) | positive scalar
  group: Thermal
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Effective length** — Effective core length `0.032` `m` (default) | positive finite scalar

Effective core length. This parameter represents the average length of the magnetic path
around the core.

### **Effective cross-sectional area** — Effective core cross-sectional area `1.6e-5` `m^2` (default) | positive finite scalar

Effective core cross-sectional area. This parameter represents the average area of the
magnetic path around the core.

### **Parameterization option** — Parameterization method `Magnetic Characteristics` (default) | `Jiles-Atherton Model` | `Saturated BH Curve`

Parameterization method that you use to describe the
*B*-*H* curve. Choose one of these options:

- `Magnetic Characteristics` — Specify the magnitude
  of the *B* and *H* intercepts,
  *B*r and
  *H*c, and the magnitude of
  *B* and *H* at the saturation point,
  *B*m and
  *H*m.
- `Jiles-Atherton Model` — Specify the Jiles-Atherton
  parameters directly.
- `Saturated BH Curve` — Tabulate the ascending or
  descending *B*-*H* curve.

### **Magnetic remanence of saturation cycle** — Residual magnetism `0.68` `T` (default) | positive scalar

Residual magnetism left in the core after it magnetizes to its saturation point
and the external magnetic field reduces to zero,
*Br*. This parameter is the magnitude of the
flux density where the *B*-*H* curve intersects the
*B*-axis.

#### Dependencies

To enable this parameter, set **Parameterization option** to
`Magnetic Characteristics`.

### **Magnetic coercivity of saturation cycle** — Magnitude of field strength to demagnetize core `151` `A/m` (default) | positive scalar

Magnitude of the magnetic field strength that you need to demagnetize the core,
*Hc*. This parameter is the magnitude of
the field intensity where the *B*-*H* curve
intersects the *H*-axis.

To enable this parameter, set **Parameterization option** to
`Magnetic Characteristics`.

### **Magnetic flux density at saturation point** — Maximum flux density magnitude `1.25` `T` (default) | positive scalar

Maximum flux density magnitude that the core can achieve,
*Bm*.

To enable this parameter, set **Parameterization option** to
`Magnetic Characteristics` or `Saturated BH
Curve`.

### **Magnetic field intensity at saturation point** — Field intensity at saturation point `3000` `A/m` (default) | positive scalar

Field intensity at the saturation point,
*Hm*. This parameter is the magnitude of the
field intensity at which further increases in the magnitude of *H* no
longer cause significant increases in the magnitude of *B*.

To enable this parameter, set **Parameterization option** to
`Magnetic Characteristics`.

### **Saturation magnetization, Ms** — Saturation magnetization, Ms `1e6` `A/m` (default) | positive finite scalar

Saturation magnetization in the Jiles-Atherton equations,
*M*s.

#### Dependencies

To enable this parameter, set **Parameterization option** to
`Jiles-Atherton Model`.

### **Anhysteretic magnetization coefficient, a** — Anhysteretic magnetization coefficient, a `82` `A/m` (default) | finite positive scalar

Anhysteretic magnetization coefficient in the Jiles-Atherton equations,
*a*. This parameter determines the point of saturation and
approximately describes the average of the two hysteretic curves.

#### Dependencies

To enable this parameter, set **Parameterization option** to
`Jiles-Atherton Model`.

### **Inter-domain coupling factor, alpha** — Inter-domain coupling factor, alpha `0.0001` (default) | scalar

Inter-domain coupling factor in the Jiles-Atherton equations,
*α*. This parameter primarily affects the points at which the
*B*-*H* curves intersect the zero field strength
line. Typical values are in the range of `1e-4` to
`1e-3`.

#### Dependencies

To enable this parameter, set **Parameterization option** to
`Jiles-Atherton Model`.

### **Coefficient for reversible magnetization, c** — Coefficient for reversible magnetization `0.1` (default) | scalar in the range [0,1]

Coefficient for reversible magnetization in the Jiles-Atherton equations,
*c*. This parameter represents the proportion of the magnetization
that you can reverse.

#### Dependencies

To enable this parameter, set **Parameterization option** to
`Jiles-Atherton Model`.

### **Bulk coupling coefficient, k** — Bulk coupling coefficient `200` `A/m` (default) | finite positive scalar

Bulk coupling coefficient in the Jiles-Atherton equations, *k*.
This parameter primarily controls the field strength magnitude at which the
*B*-*H* curve crosses the zero flux density
line.

#### Dependencies

To enable this parameter, set **Parameterization option** to
`Jiles-Atherton Model`.

### **Magnetic flux density, B(H)** — Magnetic flux density vector `[-1.25,-0.68,0,0.885,1.124,1.25]` `T` (default) | vector

Magnetic flux density *B*, specified as a vector with the same
number of elements as the magnetic field strength vector *H*. Provide
data points along the ascending curve or the descending curve. You must specify at
least one data point in the first and third quadrants. For ascending curves, you must
also specify at least one point in the fourth quadrant. For descending curves, you
must also specify at least one point in the second quadrant.

#### Dependencies

To enable this parameter, set **Parameterization option** to
`Saturated BH Curve`.

### **Magnetic field intensity, H** — Magnetic field intensity vector `[-3000,0,151,500,1000,3000]` `A/m` (default) | vector

Magnetic field intensity *H*, specified as a vector with the same
number of elements as the magnetic flux density vector *B*. Provide
data points along the ascending curve or the descending curve. You must specify at
least one data point in the first and third quadrants. For ascending curves, you must
also specify at least one point in the fourth quadrant. For descending curves, you
must also specify at least one point in the second quadrant.

To enable this parameter, set **Parameterization option** to
`Saturated BH Curve`.

### Losses

### **Averaging period for hysteresis losses** — Averaging period for hysteresis loss calculation `1e-3` `s` (default) | positive scalar

Averaging period for hysteresis loss calculation. To obtain accurate results, you
must specify a value larger than the *B*-*H* cycle
time. If you specify a smaller value, the hysteresis loss at some instances is equal
to the magnetic energy of the core, which is larger than the real losses. The best
option is to specify a value that is an exact multiple of the
*B*-*H* cycle time.

### **Model eddy losses** — Option to model eddy losses `Off` (default) | `On`

Option to model eddy losses.

### **Geometrical coefficient** — Geometrical coefficient `6` (default) | positive scalar

Geometrical coefficient *β* that accounts for the effect of the
shape of the core on eddy losses. For a laminated core, set this parameter to the
default value of `6`. For a cylindrical core, set this parameter to
`16`. For a spherical core, set this parameter to
`20`.

#### Dependencies

To enable this parameter, select the **Model eddy losses**
parameter.

### **Thickness of laminations** — Characteristic cross-sectional dimension `1` `mm` (default) | positive scalar

Characteristic cross-sectional dimension. For laminated cores, this value
corresponds to the thickness of the laminations. If the core does not have
laminations, specify a value that corresponds to the thickness at the widest
cross-section, for example, the diameter of cylindrical or spherical cores.

#### Dependencies

To enable this parameter, select the **Model eddy losses**
parameter.

### **Electrical resistivity** — Electrical resistivity of core `1.03e-7` `Ohm*m` (default) | positive scalar

Electrical resistivity of the core.

#### Dependencies

To enable this parameter, select the **Model eddy losses**
parameter.

### Thermal

### **Model thermal effects** — Option to model thermal effects `Off` (default) | `On`

Option to model thermal effects. Select this parameter to enable the
**H** port.

### **Thermal mass** — Thermal mass associated with H port `2` `J/K` (default) | positive scalar

Thermal mass associated with the **H** port. This parameter represents
the energy required to raise the temperature of the thermal port by 1 K.

#### Dependencies

To enable this parameter, select the **Model thermal effects**
parameter.
## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

### R2025a: Extract Jiles-Atherton Parameters

If you parameterize the Magnetic Core block using magnetic characteristics or a saturated
B-H curve, MATLAB now displays estimates of the Jiles-Atherton parameters at the start of the
simulation.

The Magnetic Core block estimates the Jiles-Atherton
parameters based on the assumption that the core is saturated iron. This estimate is not
always accurate for other types of core, such as ferrites with small values of coercivity
and remanence. You can now obtain an initial estimate of the Jiles-Atherton parameters by
parameterizing the Magnetic Core block using magnetic
characteristics or a saturated *B*-*H* curve. Then,
examine the predicted *B*-*H* curve and adjust the
Jiles-Atherton parameters to get a better fit with your data. For more information, see the
Model Ferrite Core Using Magnetic Core Block
example.

## Description

Nonlinear reluctance, hysteresis, and optional eddy losses

The Magnetic Core block models magnetic reluctance with
hysteresis. Use this block to model custom inductances and build transformer models. To
connect this block to your electrical network, use an Electromagnetic Converter block or a Winding block
to represent the interface between the electrical and magnetic domains.

The block uses the Jiles-Atherton model to calculate the magnetic flux density
*B* and magnetic field strength *H*. You can choose to
specify the Jiles-Atherton parameters directly, specify characteristic magnetic parameters, or
tabulate the *B*-*H* saturation curve using the
**Parameterization option** parameter.

To define the geometry for the part of the magnetic network that you are modeling, use the
**Effective length** and **Effective cross-sectional
area** parameters. The block uses this geometry information to map
*B* and *H* to the magnetomotive force and magnetic flux,
which are the Through and Across variables in the magnetic domain.

To model eddy losses, in the **Losses** settings, select the
**Model eddy losses** parameter. To model thermal effects, in the
**Thermal** settings, select the **Model thermal
effects** parameter.

### Equations

These equations define the flux density and magnetomotive force,

B=φ/seff

mmf=leffH

where:

- *B* is the magnetic flux density induced in the core.
- *φ* is the magnetic flux.
- *seff* is the value of the
  **Effective cross-sectional area** parameter.
- *mmf* is the magnetomotive force (mmf) across the
  component.
- *leff* is the value of the
  **Effective length** parameter.
- *H* is the total field strength.

This equation relates *B* and *H* to the total
magnetization of the core *M*,

B=μ0(H+M),

where *μ*0 is the magnetic
permeability of a vacuum.

The magnetization acts to increase the magnetic flux density, and its value depends on
both the current value and the history of the field strength. The block uses the
Jiles-Atherton [1,2] equations to
determine *M* at any given time. This figure shows a typical plot of the
resulting relationship between *B* and *H*.

In this figure:

- *Bm* is the magnetic flux density at the
  saturation point.
- *Br* is the magnetic remanence of the
  saturation cycle.
- *Hc* is the magnetic coercivity of the
  saturation cycle.
- *Hm* is the magnetic field intensity at
  the saturation point.

As the field strength increases from *H* = 0, the plot initially follows an ascending hysteresis curve. At the
saturation point, further increases in field intensity no longer cause significant increases
in magnetic flux.

As you reduce the magnetic field strength from the saturation point, the plot follows a
descending hysteresis curve. The difference between ascending and descending curves is due
to the dependence of *M* on the trajectory history. Physically, the
behavior corresponds to magnetic dipoles in the core aligning as the field strength
increases, but not then fully recovering to their original position as field strength
decreases.

The starting point for the Jiles-Atherton equation is the split of the magnetization
effect into two parts, one part that is purely a function of effective field strength
*Heff* and another, irreversible part that
depends on history. This equation defines the relative contributions of the anhysteretic
magnetisation *Man* and the irreversible
magnetization *Mirr* to the total magnetization
*M*,

M=cMan+(1−c)Mirr,

where *c* is the coefficient for reversible magnetization.

This equation relates *Man* to the equivalent
magnetization *Heff*:

Man=Ms(coth(Heffa)−aHeff).

The function defines a saturation curve with limiting values
±*Ms*, where:

- *M*s is the *saturation
  magnetization*.
- *a* is the *anhysteretic magnetization
  coefficient*, which determines the point of saturation. It approximately
  describes the average of the two hysteretic curves.

The Jiles-Atherton model defines the irreversible term by a partial derivative with
respect to field strength,

dMirrdH=Man−Mirrkδ−α(Man−Mirr)δ={1if dHdt≥0−1if dHdt<0

where:

- *k* is the *bulk coupling coefficient*,
  which shapes the irreversible characteristic.
- *α* is the *inter-domain coupling
  factor*.

Comparison of the equation with a standard first-order differential equation reveals
that as you change the total field strength *H*, the irreversible term
*Mirr* attempts to track the reversible term
*Man*, but with a variable tracking gain of 1/(kδ−α(Man−Mirr)). The tracking error acts to create the hysteresis at the points where
*δ* changes sign.

This equation defines the effective field strength of an anhysteretic curve without eddy
losses,

Heff=H+αM.

The value of *α* affects the shape of the hysteresis curve. Larger
values act to increase the *B*-axis intercepts. However, the stability term kδ−α(Man−Mirr) must be positive for *δ* > 0 and negative for *δ* < 0. There are therefore limits on the values of *α* that you
can provide. A typical maximum value is of the order 1e-3.

You can choose how to parameterize the *B*-*H* curve.
Set the **Parameterization option** parameter to one of these options:

- `Jiles-Atherton Model` — Specify the Jiles-Atherton
  parameters directly:

  - Saturation magnetization *M*s
  - Anhysteretic magnetization constant *a*
  - Inter-domain coupling factor *α*
  - Coefficient for reversible magnetization *c*
  - Bulk coupling coefficient *k*
- `Saturated BH Curve` — Tabulate the ascending or
  descending *B*-*H* curve. You must specify at least
  one data point in the first and third quadrant. For ascending curves, you must also
  specify at least one point in the fourth quadrant. For descending curves, you must
  also specify at least one point in the second quadrant.
- `Magnetic Characteristics` — Specify the magnitude of the
  *B* and *H* intercepts,
  *B*r and
  *H*c, and the magnitude of
  *B* and *H* at the saturation point,
  *B*m and
  *H*m.

If you set the **Parameterization option**
parameter to `Magnetic characteristics` or `Saturated
BH Curve`, MATLAB® displays estimates of the Jiles-Atherton parameters at the start of the
simulation *(since R2025a)*.

### Model Losses

The block computes hysteresis losses and eddy current losses.

The block calculates hysteresis losses using an averaging time. The instantaneous value
of the area inside the *B*-*H* curve is proportional to
the sum of the magnetic energy of the core and the thermal power dissipation. To obtain
accurate results, you must specify an **Averaging period for hysteresis
losses** parameter value that is greater than the
*B*-*H* cycle time. If you specify a smaller value, the
hysteresis loss at some instances is equal to the magnetic energy of the core which is
larger than the real losses. The best option is to specify a value that is an exact multiple
of the *B*-*H* cycle time.

These equations define the energy density dissipated by eddy currents
*W*eddy in the time interval *Δt*
[3-5],

Weddy=σd212β∫Δt(dBdt)2dt

dWeddydt=σd22β(dBdt)2

where:

- *σ* is the conductivity.
- *d* is the value of the **Thickness of
  laminations** parameter. If the core does not have laminations, this value
  corresponds to the thickness at the widest cross-section; for example, the diameter of
  cylindrical or spherical cores.
- *β* is the value of the **Geometrical
  coefficient** parameter. For a laminated core, *β* =
  `6`. For a cylindrical core, *β* =
  `16`. For a spherical core, *β* =
  `20` [5].

Eddy currents induce a magnetic field *HEddy*:

HEddy=σd212βdBdt.

This field also modifies the effective field strength:

Heff=H+αM−HEddy.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

**Note**

In the **Initial Targets** section, you can specify values for the
**Field strength** and **Flux density** parameters.
The values you provide must approximately correspond to a point on the
*B*-*H* curve.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
