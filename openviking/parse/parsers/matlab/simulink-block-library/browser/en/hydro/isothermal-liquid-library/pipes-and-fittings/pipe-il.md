---
type: simulink-block
title: 'Pipe (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Pipes and Fittings'
documentation_page: 'pipeil'
documentation_source_path: 'ref/pipeil.html'
language: en
---

# Pipe (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port.
### Inputs

### **EL** — Elevation physical signal

Variable elevation from port **A** to port **B**,
specified as a physical signal. The block bounds the signal value at
**EL** between *-L* and
*L*, where *L* is the value of the
**Pipe length** parameter.

#### Dependencies

To enable this port, set **Elevation gain
specification** to
`Variable`.

### **G** — Gravitational acceleration physical signal

Variable gravitational acceleration, specified as a physical
signal.

#### Dependencies

To enable this port, set **Gravitational acceleration
specification** to
`Variable`.

## Parameters

### Configuration

### **Enable dynamic compressibility** — Whether to model fluid compressibility `on` (default) | `off`

Whether to model any change in fluid density due to fluid
compressibility. When you select **Enable dynamic
compressibility**, changes due to the mass flow rate into
the block are calculated in addition to density changes due to changes
in pressure. In the Isothermal Liquid Library, all blocks calculate
density as a function of pressure.

### **Enable fluid inertia** — Fluid acceleration `off` (default) | `on`

Whether to account for resistance to changes in the flow rate due to
the fluid mass.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Number of segments** — Number of pipe divisions `1` (default) | positive integer

Number of pipe divisions. Each division represents an individual
segment for which pressure is calculated, depending on the pipe inlet
pressure, fluid compressibility, and wall flexibility, if applicable.
The fluid volume in each segment remains fixed.

### **Pipe length** — Pipe length `5 m` (default) | positive scalar

Total pipe length across all pipe segments.

### **Cross-sectional geometry** — Pipe geometry `Circular` (default) | `Annular` | `Rectangular` | `Elliptical` | `Isosceles triangular` | `Custom`

Cross-sectional pipe geometry. A nominal hydraulic diameter and
nominal cross-sectional area is calculated based on the cross-sectional
geometry.

### **Pipe diameter** — Pipe diameter `0.1 m` (default) | positive scalar

Diameter for circular cross-sectional pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Circular`.

### **Pipe inner diameter** — Pipe inner diameter `0.05 m` (default) | positive scalar

Inner diameter for annular pipe flow, or flow between two concentric
pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Annular`.

### **Pipe outer diameter** — Pipe outer diameter `0.1 m` (default) | positive scalar

Outer diameter for annular pipe flow, or flow between two concentric
pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Annular`.

### **Pipe width** — Rectangular pipe width `0.1 m` (default) | positive scalar

Width of rectangular pipe.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Rectangular`.

### **Pipe height** — Rectangular pipe height `0.1 m` (default) | positive scalar

Height of rectangular pipe.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Rectangular`.

### **Pipe major axis** — Ellipsoidal pipe major axis `0.1 m` (default) | positive scalar

Major axis for ellipsoidal pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Elliptical`.

### **Pipe minor axis** — Ellipsoidal pipe minor axis `0.05 m` (default) | positive scalar

Minor axis for ellipsoidal pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to
`Elliptical`.

### **Pipe side length** — Triangular pipe side length `0.1 m` (default) | positive scalar

Length of the two equal sides of isosceles-triangular pipes.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to `Isosceles
triangular`.

### **Pipe vertex angle** — Triangular pipe vertex angle `30 deg` (default) | positive scalar

Vertex angle for triangular pipes. The value must be less than 180
degrees.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to `Isosceles
triangular`.

### **Hydraulic diameter** — Hydraulic diameter `0.1128 m` (default) | positive scalar

Hydraulic diameter used in calculations of the pipe Reynolds number.
For noncircular pipes, the hydraulic diameter is the effective diameter
of the fluid in the pipe. For circular pipes, the hydraulic diameter and
pipe diameter are the same.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to `Custom`.

### **Cross-sectional area** — Pipe cross-sectional area `0.01 m^2` (default) | positive scalar

Pipe cross-sectional area for a custom pipe geometry.

#### Dependencies

To enable this parameter, set **Cross-sectional
geometry** to `Custom`.

### **Elevation gain specification** — Pipe elevation specification `Constant` (default) | `Variable`

Whether the pipe elevation remains constant or variable from port
**A** to **B**.

### **Elevation gain from port A to port B** — Constant pipe elevation differential `0 m` (default) | scalar

Elevation differential for constant-elevation pipes.

#### Dependencies

To enable this parameter, set **Elevation gain
specification** to
`Constant`.

### **Gravitational acceleration specification** — Acceleration specification `Constant` (default) | `Variable`

Whether the gravitational constant is constant or variable.

### **Gravitational acceleration** — Gravitational acceleration `9.81 m/s^2` (default) | scalar

Gravitational acceleration for environments with constant
gravitational acceleration.

#### Dependencies

To enable this parameter, set **Gravitational acceleration
specification** to
`Constant`.

### Viscous Friction

### **Viscous friction parameterization** — Method of calculating pressure loss due to wall friction `Haaland correlation` (default) | `Nominal pressure drop vs. nominal mass flow rate` | `Tabulated data - Darcy friction factor vs. Reynolds number`

Parameterization of pressure losses due to wall friction. Both
analytical and tabular formulations are available.

### **Local resistances specification** — Method for quantifying pressure losses in the Haaland correlation `Aggregate equivalent length` (default) | `Local loss coefficient`

Method for quantifying pressure losses due to pipe
nonuniformities.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Haaland
correlation`.

### **Total local loss coefficient** — Defines loss coefficient over the pipe `0.1` (default) | positive scalar

Loss coefficient associated with each pipe nonuniformity. You can
input a single loss coefficient or the sum of all loss coefficients
along the pipe.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Haaland
correlation` and **Local resistance
specifications** to `Local loss
coefficient`.

### **Aggregate equivalent length of local resistances** — Contribution of pipe geometry to hydraulic losses `1 m` (default) | positive scalar

Length of pipe that would produce the equivalent hydraulic losses as
would a pipe with bends, area changes, or other nonuniform attributes.
The effective length of the pipe is the sum of the **Pipe
length** and the **Aggregate equivalent length of
local resistances**.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Haaland
correlation` and **Local resistance
specifications** to `Aggregate equivalent
length`.

### **Surface roughness specification** — Pipe material for roughness specification `Commercially smooth brass, lead, copper, or plastic pipe: 1.52 um` (default) | `Steel and wrought iron : 46 um` | `Galvanized iron or steel : 152 um` | `Cast iron : 259 um` | `Custom`

Absolute surface roughness based on pipe material. The provided values
are ASHRAE standard roughness values. You can also input your own value
by setting **Surface roughness specification** to
`Custom`.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Haaland
correlation`.

### **Internal surface absolute roughness** — Pipe wall roughness `15e-6 m` (default) | positive scalar

Pipe wall absolute roughness. This parameter is used to determine the
Darcy friction factor, which contributes to pressure loss in the
pipe.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Haaland
correlation` and **Surface roughness
specification** to
`Custom`.

### **Laminar flow upper Reynolds number limit** — Laminar flow upper threshold `2000` (default) | positive scalar

Upper Reynolds number limit to laminar flow. Beyond this number, the
fluid regime is transitional, approaches the turbulent regime, and
becomes fully turbulent at the **Turbulent flow lower Reynolds
number limit**.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to either:

- `Haaland correlation`
- `Tabulated data - Darcy friction factor
  vs. Reynolds number`

### **Turbulent flow lower Reynolds number limit** — Turbulent flow lower threshold `4000` (default) | positive scalar

Lower Reynolds number limit for turbulent flow. Below this number, the
flow regime is transitional, approaches laminar flow, and becomes fully
laminar at the **Laminar flow upper Reynolds number
limit**.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to either:

- `Haaland correlation`
- `Tabulated data - Darcy friction factor
  vs. Reynolds number`

### **Nominal mass flow rate** — Mass flow rate for calculating loss coefficient `[.1, 1] kg/s` (default) | positive scalar | 1-by-*n* vector

Nominal mass flow rate used for calculating the pressure loss
coefficient for rigid and flexible pipes, specified as a scalar or a
vector. All nominal values must be greater than 0 and have the same
number of elements as the **Nominal pressure drop**
parameter. When this parameter is supplied as a vector, the scalar value
*K*loss is determined as a
least-squares fit of the vector elements.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Nominal pressure
drop vs. nominal mass flow rate`.

### **Nominal pressure drop** — Pressure drop for calculating loss coefficient `[.001, .01] MPa` (default) | positive scalar | 1-by-*n* vector

Nominal pressure drop used for calculating the pressure loss
coefficient for rigid and flexible pipes, specified as a scalar or
vector. All nominal values must be greater than 0 and must have the same
number of elements as the **Nominal mass flow rate**
parameter. When this parameter is supplied as a vector, the scalar value
*K*loss is determined as a
least-squares fit of the vector elements.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Nominal pressure
drop vs. nominal mass flow rate`.

### **Mass flow rate threshold for flow reversal** — Mass flow rate threshold `1e-6 kg/s` (default) | positive scalar

Mass flow rate threshold for reversed flow. A transition region is
defined around 0 kg/s between the positive and negative values of the
mass flow rate threshold. Within this transition region, numerical
smoothing is applied to the flow response. The threshold value must be
greater than 0.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Nominal pressure
drop vs. nominal mass flow rate`.

### **Reynolds number vector for turbulent Darcy friction factor** — Vector of Reynolds numbers for tabular parameterization [400, 1000, 1500, 3000, 4000, 6000, 10000, 20000, 40000, 60000, 100000, 100000000] (default) | 1-by-*n* vector

Vector of Reynolds numbers for the tabular parameterization of the Darcy friction
factor. The vector elements form an independent axis with the
**Darcy friction factor vector** parameter. The
vector elements must be listed in ascending order. A positive Reynolds
number corresponds to flow from port **A** to port
**B**.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Tabulated data -
Darcy friction factor vs. Reynolds number`.

### **Darcy friction factor vector** — Vector of friction factors for tabular parameterization `[.264, .112, .071, .0417, .0387, .0268, .025, .0232, .0226, .022, .0214, .0214]` (default) | 1-by-*n* vector

Vector of Darcy friction factors for the tabular parameterization of
the Darcy friction factor. The vector elements must correspond
one-to-one with the elements in the **Reynolds number vector for
turbulent Darcy friction factor** parameter, and must be
unique and greater than or equal to 0.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to `Tabulated data -
Darcy friction factor vs. Reynolds number`.

### **Laminar friction constant for Darcy friction factor** — Friction constant for laminar flows `64` (default) | positive scalar

Friction constant for laminar flows. The Darcy friction factor
captures the contribution of wall friction in pressure loss
calculations. If **Cross-sectional geometry** is not
set to `Custom`, this parameter is internally
set to 64.

#### Dependencies

To enable this parameter, set **Viscous friction
parameterization** to either:

- `Haaland correlation`
- `Tabulated data - Darcy friction factor
  vs. Reynolds number`

and **Cross-sectional geometry** to
`Custom`.

### Pipe Wall

### **Pipe wall specification** — Specifies wall flexibility `Rigid` (default) | `Flexible`

Specifies wall flexibility. This parameter is independent of pipe
cross-sectional geometry. The `Flexible`
setting preserves the initial pipe shape and applies equal expansion of
the cross-sectional area. It may not be accurate for non-circular
cross-sectional geometry under high deformation.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Volumetric expansion specification** — Linear expansion correlation `Cross-sectional area vs. pressure` (default) | `Cross-sectional area vs. pressure - Tabulated` | `Hydraulic diameter vs. pressure` | `Based on material properties`

Linear expansion correlation. The settings correlate the new
cross-sectional area or hydraulic diameter to the pipe pressure.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible`.

### **Static gauge pressure to cross-sectional area gain** — Coefficient for area-dependent pipe deformation `1e-6 m^2/MPa` (default) | positive scalar

Coefficient for calculating pipe deformation for the
`Cross-sectional area vs. pressure`
setting. The gain is multiplied by the pressure differential between the
segment pressure and atmospheric pressure.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**,
and set **Pipe wall specification** to
`Flexible` and **Volumetric
expansion specification** to
`Cross-sectional area vs.
pressure`.

### **Static gauge pressure vector** — Vector of gauge pressures `[.1,1] MPa` (default) | vector

Vector that contains the gauge pressures. The block uses this vector
in a table lookup to calculate the pipe cross-sectional area. The vector
entries must be strictly positive and monotonically increasing and the
vector must be the same length as the **Cross sectional area
gain vector** parameter.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible` and **Volumetric
expansion specification** to
`Cross-sectional area vs. pressure -
Tabulated`.

### **Cross sectional area gain vector** — Vector of pipe cross-sectional areas `[1e-05, 1.1e-05] m^2` (default) | vector

Vector that contains the pipe cross-sectional areas. The block uses
this vector in a table lookup to calculate the pipe cross sectional-area
at other pressures. The vector entries must be strictly positive and
monotonically increasing and the vector must be the same length as the
**Static gauge pressure vector** parameter.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible` and **Volumetric
expansion specification** to
`Cross-sectional area vs. pressure -
Tabulated`.

### **Static gauge pressure to hydraulic diameter gain** — Coefficient for diameter-dependent pipe deformation `1e-6 m/MPa` (default) | positive scalar

Coefficient for calculating pipe deformation for the
`Hydraulic diameter vs. pressure` setting.
The gain is multiplied by the pressure differential between the segment
pressure and atmospheric pressure.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible` and **Volumetric
expansion specification** to `Hydraulic
diameter vs. pressure`.

### **Material behavior** — Method used to specify material behavior `Linear Elastic` (default) | `Multilinear Elastic`

Method the block uses to calculate the material behavior.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible` and **Volumetric
expansion specification** to `Based on
material properties`.

### **Pipe wall thickness** — Width of pipe wall `0.05 m` (default) | positive scalar

Thickness of the pipe wall. The block uses this value to calculate
stress.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible` and **Volumetric
expansion specification** to `Based on
material properties`.

### **Young's modulus** — Young's modulus of pipe wall material `69 GPa` (default) | positive scalar

Young's modulus of the material that makes up the pipe wall.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible`, **Volumetric
expansion specification** to `Based on
material properties`, and **Material
behavior** to `Linear
Elastic`.

### **Poisson's ratio** — Poisson's ratio of pipe wall material `0.33` (default) | positive scalar

Poisson's ratio of the material that makes up the pipe wall.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible` and **Volumetric
expansion specification** to `Based on
material properties`.

### **Stress vector** — Stress vector of pipe wall material `[276, 310] MPa` (default) | vector

Vector containing the stress values for the material that makes up the
pipe wall.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible`, **Volumetric
expansion specification** to `Based on
material properties`, and **Material
behavior** to `Multilinear
Elastic`.

### **Strain vector** — Strain vector of pipe wall material `[.004, .02]` (default) | vector

Vector containing the strain values for the material that makes up the
pipe wall.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible`, **Volumetric
expansion specification** to `Based on
material properties`, and **Material
behavior** to `Multilinear
Elastic`.

### **Check if stress exceeds specified allowable level** — Notification when stress is above specified max `None` (default) | `Warning` | `Error`

Whether the block does nothing, generates a warning, or generates an
error when the stress is above the maximum stress specified by the
**Maximum allowable stress** parameter.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible`, **Volumetric
expansion specification** to `Based on
material properties`, and **Material
behavior** to `Multilinear
Elastic`.

### **Maximum allowable stress** — Maximum allowed stress on pipe wall `400 MPa` (default) | positive scalar

Maximum stress the block allows on the pipe wall. Control what the
block does if the stress exceeds this value with the **Check if
stress exceeds specified allowable level**
parameter.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible`, **Volumetric
expansion specification** to `Based on
material properties`, **Material
behavior** to `Multilinear
Elastic` and **Check if stress exceeds
specified allowable level** to
`Warning` or
`Error`.

### **Volumetric expansion time constant** — Pipe deformation time constant `0.01 s` (default) | positive scalar

Time required for the wall to reach steady-state after pipe
deformation. This parameter impacts the dynamic change in pipe
volume.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and set **Pipe wall specification** to
`Flexible`.

### Initial Conditions

### **Initial liquid pressure** — Initial pressure in pipe or pipe segment `0.101325 MPa` (default) | positive scalar | 1-by-*n* vector

Initial liquid pressure, specified as a scalar or vector. A vector
*n* elements long defines the liquid pressure for
each of *n* pipe segments. If the vector is two
elements long, the pressure along the pipe is linearly distributed
between the two element values. If the vector is three or more elements
long, the initial pressure in the *n*th segment is set
by the *n*th element of the vector.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Initial mass flow rate from port A to port B** — Initial mass flow rate for inertia calculation `0 kg/s` (default) | scalar

Initial mass flow rate for pipes with simulated fluid inertia.

#### Dependencies

To enable this parameter, select **Enable dynamic compressibility**
and **Enable fluid inertia**.

## Libraries

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2023b: Model pipe with length shorter than elevation gain

You can now model a pipe with length shorter than the elevation change when
**Elevation gain specification** is
`Constant`. The block issues a warning rather than an
error if the value of the **Elevation gain from port A to port B**
parameter is greater than the value of the **Pipe length**
parameter.

### R2023a: Use Additional Flexible Pipe Parameterizations

You can now use new parameterization methods when the **Pipe wall
specification** parameter is `Flexible`. To
use the new parameterizations, set the **Volumetric expansion
specification** parameter to `Cross-sectional area vs.
pressure - Tabulated` or `Based on material
properties`.

## Description

Pipe segment in an isothermal liquid network

The Pipe (IL) block models flow in a rigid or flexible-walled pipe with losses due to wall
friction. The effects of dynamic compressibility, fluid inertia, and pipe elevation can
be optionally modeled. You can define multiple pipe segments and set the liquid pressure
for each segment. By segmenting the pipe and selecting **Enable fluid
inertia**, you can model events such as water hammer in your system.

### Pipe Characteristics

The pipe block can be divided into segments with the **Number of
segments** parameter. When the pipe is composed of a number of
segments, the pressure in each segment is calculated based on the inlet pressure and
the effect on the segment mass flow rate of the fluid compressibility and wall
flexibility, if applicable. The fluid volume in each segment remains fixed. For a
two-segment pipe, the pressure evolves linearly with respect to the pressure defined
at ports **A** and **B**. For a pipe with three or
more segments, you can specify the fluid pressure in each segment in vector or
scalar form in the **Initial liquid pressure** parameter. The
scalar form will apply a constant value over all segments.

**Flexible Walls**

You can model flexible walls for all cross-sectional geometries. When you set
**Pipe wall specification** to
`Flexible`, the block assumes uniform expansion
along all directions and preserves the defined cross-sectional shape. This
setting may not result in physical results for noncircular cross-sectional areas
undergoing high pressure relative to atmospheric pressure. When you model
flexible walls, you can use the **Volumetric expansion
specification** parameter to control the method for specifying the
volumetric expansion of the pipe cross-sectional area.

When the **Volumetric expansion specification** parameter is
`Cross-sectional area vs. pressure`, the change in
volume is modeled by

V˙=L(A−Sτ),

where:

- A=SN+Kps(p−patm).
- *L* is the **Pipe length**
  parameter.
- *SN* is the nominal pipe
  cross-sectional area defined for each shape.
- *S* is the current pipe cross-sectional
  area.
- *p* is the internal pipe pressure.
- *patm* is the atmospheric
  pressure.
- *K*ps is the
  **Static gauge pressure to cross-sectional area
  gain** parameter.

  To calculate *Kps*
  assuming uniform elastic deformation of a thin-walled, open-ended
  cylindrical pipe, use:

  Kps=ΔDΔp=πDN34tE,

  where *t* is the pipe wall
  thickness and *E* is Young's modulus.
- *τ* is the **Volumetric expansion time
  constant**.

When the **Volumetric expansion specification** parameter is
`Cross-sectional area vs. pressure - Tabulated`,
the block uses the same equation for V˙ as the `Cross-sectional area vs.
pressure` setting. The block calculates *A*
with the table lookup function

A=SN+tablelookup(pps,Aps,(p−patm),interpolation=linear,extrapolation=linear),

where *pps* is the **Static
gauge pressure vector** parameter and
*Aps* is the **Cross
sectional area gain vector** parameter.

When the **Volumetric expansion specification** parameter is
`Hydraulic diameter vs. pressure`, the change in
volume is modeled by

V˙=π2DL(Dstatic−Dτ),

where:

- Dstatic=DN+Kpd(p−patm).
- *DN* is the nominal
  hydraulic diameter defined for each shape.
- *D* is the current pipe hydraulic
  diameter.
- *K*pd is the
  **Static gauge pressure to hydraulic diameter
  gain** parameter. To calculate
  *Kps* assuming
  uniform elastic deformation of a thin-walled, open-ended cylindrical
  pipe, use:

  Kpd=ΔDΔp=DN22tE.

When the **Volumetric expansion specification** parameter is
`Based on material properties`, the block uses the
same equation for V˙ as the `Hydraulic diameter vs.
pressure` setting but calculates
*Dstatic* depending on the value
of the **Material behavior** parameter

Dstatic=DN(1+ϵhoop).

This parameterization assumes a cylindrical thin-walled pressure vessel where σradial=0.

When the **Material behavior** parameter is `Linear
elastic`,

ϵhoop=1E[σhoop−vσlongitudinal],

where:

- *E* is the value of the **Young's
  modulus** parameter.
- *v* is the value of the  **Poisson's
  ratio** parameter.
- σhoop=pD2t where *t* is the value of the
  **Pipe wall thickness** parameter.
- σlongitudinal=pD4t.

When the **Material behavior** parameter is `Multilinear
elastic`, the block calculates the von Mises stress,
*σv*, which simplifies to σv=34pD2t, to determine the equivalent strain. The hoop strain is

ϵhoop=ϵhoopelastic+ϵhoopplastic

ϵhoopelastic=1E[σhoop−vσlongitudinal]ϵhoopi,jplastic=32(1Es−1E)Si,j

where:

- The block calculates the Young's Modulus, *E*,
  from the first elements of the **Stress vector**
  and **Strain vector** parameters.
- ES=σtotalϵtotal, where
  *σtotal* and
  *εtotal* are the
  equivalent total stress and the equivalent total strain,
  respectively. The block calculates the equivalent total strain from
  the von Mises stress and the stress-strain curve.
- Si,j=σi,j−[σhoop+σlongitudinal+σradial3]δi,j, where
  *σi,j* are the elements
  of the Cauchy stress tensor.

If you do not model flexible walls,
*SN* = *S* and
*DN* =
*D*.

**Circular**

The nominal hydraulic diameter and the **Pipe diameter**,
*d*circle, are the same. The pipe
cross sectional area is: SN=π4dcircle2.

**Annular**

The nominal hydraulic diameter,
*D*h,nom, is the difference between
the **Pipe outer diameter** and **Pipe inner
diameter**, *d*o –
*d*i. The pipe cross sectional area
is SN=π4(do2−di2).

**Rectangular**

The nominal hydraulic diameter is:

DN=2hwh+w,

where:

- *h* is the **Pipe
  height**.
- *w* is the **Pipe
  width**.

The pipe cross sectional area is SN=wh.

**Elliptical**

The nominal hydraulic diameter is:

DN=2amajbmin(64-16(amaj-bminamaj+bmin)2)(amaj+bmin)(64-3(amaj-bminamaj+bmin)4),

where:

- *a*maj is the
  **Pipe major axis**.
- *b*min is the
  **Pipe minor axis**.

The pipe cross sectional area is SN=π4amajbmin.

**Isosceles Triangular**

The nominal hydraulic diameter is:

DN=lsidesin(θ)1+sin(θ2)

where:

- *l*side is the
  **Pipe side length**.
- *θ* is the **Pipe vertex
  angle**.

The pipe cross sectional area is SN=lside22sin(θ).

### Pressure Loss Due to Friction

**Haaland Correlation**

The analytical Haaland correlation models losses due to wall friction either
by *aggregate equivalent length*, which accounts for
resistances due to nonuniformities as an added straight-pipe length that results
in equivalent losses, or by *local loss coefficient*, which
directly applies a loss coefficient for pipe nonuniformities.

When the **Local resistances specification** parameter is set
to `Aggregate equivalent length` and the flow in the
pipe is lower than the **Laminar flow upper Reynolds number
limit**, the pressure loss over all pipe segments is:

Δpf,A=υλ2D2SL+Ladd2m˙A,

Δpf,B=υλ2D2SL+Ladd2m˙B,

where:

- *ν* is the fluid kinematic viscosity.
- *λ* is the **Laminar friction constant
  for Darcy friction factor**, which you can define when
  **Cross-sectional geometry** is set to
  `Custom` and is otherwise equal to
  64.
- *D* is the pipe hydraulic diameter.
- *L*add is the
  **Aggregate equivalent length of local
  resistances**.
- m˙A is the mass flow rate at
  port **A**.
- m˙B is the mass flow rate at
  port **B**.

When the Reynolds number is greater than the **Turbulent
flow lower Reynolds number limit**, the pressure loss in the pipe is:

Δpf,A=f2ρIDS2L+Ladd2m˙A|m˙A|,

Δpf,B=f2ρIDS2L+Ladd2m˙B|m˙B|,

where:

- *f* is the Darcy friction factor. This is approximated by the
  empirical Haaland equation and is based on the **Surface
  roughness specification**, *ε*, and
  pipe hydraulic diameter:

  f={−1.8log10[6.9Re+(ε3.7Dh)1.11]}−2,

  Pipe roughness for brass, lead, copper, plastic,
  steel, wrought iron, and galvanized steel or iron are provided as
  ASHRAE standard values. You can also supply your own
  **Internal surface absolute roughness** with
  the `Custom` setting.
- *ρ*I is the internal fluid
  density.

When the **Local resistances specification** parameter is set
to `Local loss coefficient` and the flow in the pipe is
lower than the **Laminar flow upper Reynolds number limit**,
the pressure loss over all pipe segments is:

Δpf,A=υλ2D2SL2m˙A.

Δpf,B=υλ2D2SL2m˙B.

When the Reynolds number is greater than the
**Turbulent flow lower Reynolds number limit**, the
pressure loss in the pipe is:

Δpf,A=(fL2D+Closs,total)12ρIS2m˙A|m˙A|,

Δpf,B=(fL2D+Closs,total)12ρIS2m˙B|m˙B|,

where *C*loss,total
is the loss coefficient, which can be defined in the **Total local loss
coefficient** parameter as either a single coefficient or the sum
of all loss coefficients along the pipe.

**Nominal Pressure Drop vs. Nominal Mass Flow Rate**

The Nominal Pressure Drop vs. Nominal Mass Flow Rate parameterization characterizes losses
with a loss coefficient for rigid or flexible walls. When the fluid is
incompressible, the pressure loss over the entire pipe due to wall friction is:

Δpf,A=Kpm˙Am˙A2+m˙th2,

where *K*p is:

Kp=ΔpNm˙N2,

where:

- *Δp*N is the
  **Nominal pressure drop**, which can be defined
  either as a scalar or a vector.
- m˙N is the **Nominal mass flow
  rate**, which can be defined either as a scalar or a
  vector.

When the **Nominal pressure drop** and
**Nominal mass flow rate** parameters are supplied as
vectors, the scalar value *K*p is
determined from a least-squares fit of the vector elements.

**Tabulated Data – Darcy Friction Factor vs. Reynolds Number**

Pressure losses due to viscous friction can also be determined from
user-provided tabulated data of the **Darcy friction factor
vector** and the **Reynolds number vector for turbulent
Darcy friction factor** parameters. Linear interpolation is
employed between data points.

### Pipe Discretization

You can divide the pipe into multiple segments. If a pipe has more than one segment, the
mass flow and momentum balance equations are calculated for each segment.

If you would like to capture specific phenomena in your application, such as water
hammer, choose a number of segments that provides sufficient resolution of the
transient. The following formula, from the Nyquist sampling theorem, provides a rule
of thumb for pipe discretization into a minimum of *N* segments:

N=2Lfc,

where:

- *L* is the **Pipe length**.
- *f* is the transient frequency.
- *c* is the speed of sound.

### Mass and Momentum Balance

When you clear the **Enable dynamic compressibility** checkbox, the mass
flow into the pipe equals the mass flow out of the pipe

m˙A+m˙B=0.

When you select **Enable dynamic
compressibility** and set **Pipe wall specification**
to `Rigid`, the difference between the mass flow into and
out of the pipe depends on the fluid density change due to compressibility,

m˙A+m˙B=p˙IdρIdpIV,

When you select **Enable dynamic
compressibility** and set **Pipe wall specification**
to `Flexible`, the difference between the mass flow into
and out of the pipe is based on the change in fluid density due to compressibility,
and the amount of fluid accumulated in the newly deformed regions of the pipe:

m˙A+m˙B=p˙IdρIdpIV+ρIV˙.

The changes in momentum between the pipe inlet and outlet
comprises the changes in pressure due to pipe wall friction, which is modeled
according to the **Viscous friction parameterization** and pipe
elevation.

When you clear the **Enable fluid inertia** checkbox, the momentum balance is:

pA−pI=Δpf,A+ρIΔz2g,

pB−pI=Δpf,B−ρIΔz2g,

where:

- *p*A is the pressure at port
  **A**.
- *p*I is the fluid volume
  internal pressure.
- *p*B is the pressure at port
  **B**.
- *Δp*f is the pressure loss due
  to wall friction, parameterized by the **Viscous friction
  losses** specification according to the respective
  port.
- *Δz* is the pipe elevation. In the case of
  constant-elevation pipes, this is the **Elevation gain from port
  A to port B** parameter; otherwise, it is received as a
  physical signal at port **EL**.
- *g* is the gravitational acceleration. In the case of
  a fixed gravitational constant, this is the **Gravitational
  acceleration** parameter; otherwise, it is received as a
  physical signal at port **G**.

When you select **Enable fluid inertia**, the
momentum balance is:

pA−pI=Δpf,A+ρIΔz2g+m¨AL2S,

pB−pI=Δpf,B−ρIΔz2g+m¨BL2S,

where:

- m¨ is the fluid acceleration at its respective
  port.
- *S* is the pipe cross-sectional area.
