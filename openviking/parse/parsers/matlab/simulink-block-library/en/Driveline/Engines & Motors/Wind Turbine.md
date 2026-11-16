---
type: simulink-block
title: 'Wind Turbine'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors'
documentation_page: 'windturbine'
documentation_source_path: 'ref/windturbine.html'
language: en
---

# Wind Turbine

## Ports

### Inputs

### **V** — Incident wind velocity, m/s physical signal

Physical signal input associated with the incident wind velocity, in
m/s.

### **β** — Pitch angle, deg physical signal

Physical signal input associated with the pitch angle of the turbine
blades, in deg.
### Outputs

### **T** — Thrust, N physical signal

Physical signal output port associated with the axial force that the
wind applies to the turbine blades, in N.

#### Dependencies

To enable this port, select **Output thrust**.
### Conserving

### **R** — Turbine shaft mechanical rotational

Mechanical rotational conserving port associated with the wind turbine
shaft.

## Parameters

### Wind Turbine

### **Parameterization** — Wind turbine parameterization option `Tabulated data for power and thrust coefficients` (default) | `Tabulated data for airfoil lift and drag coefficients`

Whether to parameterize the wind turbine by thrust and power
coefficients or airfoil lift and drag coefficients.

#### Dependencies

### **Turbine radius** — Blade tip radius `80` `m` (default) | positive scalar

Distance from the turbine hub center to the blade tips.

### **Pitch angle vector, β** — Reference pitch angle `[0, 3, 5, 10, 20, 90]` `deg` (default) | vector of length *M*

Reference collective blade pitch angle. The length of this vector
defines the number of rows in the **Power coefficient table,
Cp(β, λ)** and **Thrust coefficient table, Ct(β,
λ)** parameters.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for power and thrust
coefficients`.

### **Tip speed ratio vector, λ** — Reference tip speed ratio `[0, 2, 4, 6, 8, 10, 12, 14, 15]` (default) | vector of length *N*

Reference tip speed ratio (λ). λ is the ratio of the blade tip speed
to wind speed. The length of this vector defines the number of columns
in the **Power coefficient table, Cp(β, λ)** and
**Thrust coefficient table, Ct(β, λ)** parameters.
The block supports negative λ values. The values must be strictly
monotonically increasing.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for power and thrust
coefficients`.

### **Power coefficient table, Cp(β,λ)** — Power coefficient table *M*-by-*N* matrix

Power coefficients for a given pitch angle and tip speed ratio. Each
row corresponds to an element in the **Pitch angle vector,
β** parameter, and each column corresponds to an element in
the **Tip speed ratio vector, λ** parameter. The
default parameter value is `[0.0010, 0.0161, 0.1446, 0.3865,
0.5009, 0.4404, 0.2545, 0.0002, -0.1384; 0.0016, 0.0173, 0.1079,
0.2676, 0.3779, 0.4111, 0.3838, 0.3176, 0.2753; 0.0027, 0.0197,
0.1151, 0.2606, 0.3469, 0.3558, 0.3069, 0.2222, 0.1718; 0.0054,
0.0283, 0.1315, 0.2364, 0.2589, 0.2022, 0.0929, -0.0455, -0.1204;
0.0109, 0.0536, 0.1320, 0.1256, 0.0120, -0.1752, -0.4017, -0.6435,
-0.7655; -0.01 * ones(1, 9)]`. The block asserts *Cp*(λ=0)≅
0.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for power and thrust
coefficients`.

### **Thrust coefficient table, Ct(β,λ)** — Thrust coefficient table *M*-by-*N* matrix

Thrust coefficients for a given pitch angle and tip speed ratio. Each
row corresponds to an element in the **Pitch angle vector,
β** parameter, and each column corresponds to an element in
the **Tip speed ratio vector, λ** parameter. The
default parameter value is `[0.0000, 0.2451, 0.6740, 0.9616,
1.0000, 0.9882, 0.8430, 0.0002, -0.1341; 0.0016, 0.2541, 0.5942,
0.8582, 0.9561, 0.9754, 0.9599, 0.9092, 0.8669; 0.0027, 0.2705,
0.6113, 0.8503, 0.9339, 0.9407, 0.8993, 0.8016, 0.7239; 0.0054,
0.3215, 0.6475, 0.8205, 0.8482, 0.7727, 0.5565, -0.0450, -0.1171;
0.2035, 0.4335, 0.6485, 0.6348, 0.2129, -0.1684, -0.3701, -0.5712,
-0.6681; -0.05 * ones(1, 9)]` .

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for power and thrust
coefficients` and select **Output
thrust**.

### **Number of blades** — Number of blades `3` (default) | positive integer

Number of wind turbine blades.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for airfoil lift and drag
coefficients`.

### **Nondimensional radial location vector, r** — Radial location `[.1, .17, .23, .36, .5, .63, 1]` (default) | vector

Radial location for a given set of blade dimensions.
`1` is equivalent to the radius of the blade. The
first element of this vector defines *e*, the root
cutout.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for airfoil lift and drag
coefficients`.

### **Blade twist vector, θ\_tw(r)** — Blade element twist `[13.31, 13.31, 11.48, 9.01, 6.54, 4.19, .11]` `deg` (default) | vector

Blade twist angles, *θ*, for a given radial location.
The elements of this vector correspond one-to-one with the
**Nondimensional radial location vector, r**
parameter.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for airfoil lift and drag
coefficients`.

### **Normalized chord length vector, c(r)/R** — Blade element chord length `[.068, .074, .076, .069, .061, .053, .023]` (default) | vector

Chord length normalized by radius for a given radial location along the blade. The
elements of this vector correspond one-to-one with the
**Nondimensional radial location vector, r**
parameter and the columns of the **Airfoil lift coefficient
table, Cl(α,r)** and **Airfoil drag coefficient
table, Cd(α,r)** parameters.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for airfoil lift and drag
coefficients`.

### **Airfoil angle of attack vector, α** — Angle of attack `[-180 : 10 : 180]` `deg` (default) | vector of length *M*

Angle of attack range. The elements of this vector correspond
one-to-one with the rows of the **Airfoil lift coefficient
table, Cl(α,r)** and **Airfoil drag coefficient
table, Cd(α,r)** parameters.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for airfoil lift and drag
coefficients`.

### **Airfoil lift coefficient table, Cl(α,r)** — Airfoil lift coefficients *M* x *N* matrix

Airfoil lift coefficients for a given angle of attack and radial
location along the blade. The rows in this matrix correspond one-to-one
with the **Airfoil angle of attack vector, α**
parameter. The columns in this matrix correspond one-to-one with the
**Nondimensional radial location vector, r**
parameter.

The default value is `[0, 0, 0, 0, 0, 0, 0; 0, .397, .547,
.547, .735, .788, .749; 0, .642, .685, .685, .695, .67, .659; 0,
.757, .816, .816, .828, .797, .783; 0, .762, .832, .832, .846, .813,
.798; 0, .68, .756, .756, .771, .739, .724; 0, .532, .609, .609,
.624, .596, .581; 0, .337, .411, .411, .426, .403, .39; 0, .114,
.182, .182, .195, .179, .169; 0, -.12, -.061, -.061, -.05, -.06,
-.067; 0, -.349, -.302, -.302, -.294, -.295, -.299; 0, -.557, -.523,
-.523, -.518, -.512, -.512; 0, -.727, -.708, -.708, -.706, -.693,
-.689; 0, -.842, -.838, -.838, -.839, -.82, -.814; 0, -.886, -.895,
-.895, -.898, -.875, -.866; 0, -.839, -.858, -.858, -.862, -.838,
-.829; 0, -.685, -1.013, -1.013, -.815, -.869, -.958; 0, -.311,
-.8496, -.8496, -.8284, -.8284, -.711; 0, .137, .288, .288, .444,
.521, .442; 0, 1.368, 1.458, 1.458, 1.442, 1.358, 1.382; 0, 1.7825,
1.398, 1.398, 1.354, 1.311, 1.428; 0, 1.904, 1.265, 1.265, 1.076,
.962, .926; 0, 1.903, 1.258, 1.258, 1.064, .95, .804; 0, 1.69,
1.146, 1.146, .98, .884, .763; 0, 1.323, .932, .932, .81, .74, .656;
0, .88, .657, .657, .582, .54, .495; 0, .449, .362, .362, .326,
.304, .291; 0, .124, .092, .092, .072, .053, .053; 0, -.118, -.15,
-.15, -.17, -.198, -.199; 0, -.348, -.379, -.379, -.399, -.434,
-.436; 0, -.549, -.578, -.578, -.596, -.637, -.64; 0, -.702, -.727,
-.727, -.743, -.787, -.79; 0, -.787, -.807, -.807, -.821, -.864,
-.868; 0, -.782, -.797, -.797, -.806, -.847, -.85; 0, -.664, -.673,
-.673, -.679, -.711, -.714; 0, -.41, -.547, -.547, -.735, -.788,
-.749; 0, 0, 0, 0, 0, 0, 0]`.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for airfoil lift and drag
coefficients`.

### **Airfoil drag coefficient table, Cd(α,r)** — Airfoil drag coefficients *M* x *N* matrix

Airfoil drag coefficients for a given angle of attack and radial
location along the blade. The rows in this matrix correspond one-to-one
with the **Airfoil angle of attack vector, α**
parameter. The columns in this matrix correspond one-to-one with the
**Nondimensional radial location vector, r**
parameter.

The default value is `[.35, .0602, .0267, .0267, .0202, .0185,
.0198; .35, .1107, .0968, .0968, .0943, .0945, .0955; .35, .3045,
.2876, .2876, .2848, .2809, .2807; .35, .5355, .5232, .5232, .5215,
.5112, .5086; .35, .7685, .7656, .7656, .766, .7485, .7427; .35,
.9788, .9882, .9882, .9911, .9665, .9574; .35, 1.1499, 1.173, 1.173,
1.1787, 1.1476, 1.1355; .35, 1.2716, 1.3084, 1.3084, 1.3168, 1.2805,
1.2656; .35, 1.3378, 1.3875, 1.3875, 1.3984, 1.3582, 1.341; .35,
1.346, 1.407, 1.407, 1.4201, 1.3774, 1.3587; .35, 1.2964, 1.3664,
1.3664, 1.3811, 1.3376, 1.3181; .35, 1.1918, 1.2676, 1.2676, 1.2833,
1.2409, 1.2212; .35, 1.0376, 1.1156, 1.1156, 1.1315, 1.0919, 1.0731;
.35, .8429, .9187, .9187, .9341, .899, .882; .35, .6215, .6904,
.6904, .7042, .6754, .661; .35, .3932, .4503, .4503, .4616, .4405,
.4295; .35, .1861, .2388, .2388, .2237, .1983, .1785; .35, .0931,
.0718, .0718, .0287, .0287, .0111; .35, .0113, .0087, .0087, .0065,
.0057, .0052; .35, .0393, .0192, .0192, .0262, .0255, .015; .35,
.3998, .2689, .2689, .228, .1987, .2379; .35, .8441, .5843, .5843,
.5149, .4813, .4294; .35, 1.2873, .897, .897, .7901, .7396, .6452;
.35, 1.6401, 1.1686, 1.1686, 1.0378, .9781, .8664; .35, 1.836,
1.3647, 1.3647, 1.2333, 1.1796, 1.0693; .35, 1.8347, 1.4621, 1.4621,
1.3587, 1.3297, 1.2438; .35, 1.6334, 1.4544, 1.4544, 1.4063, 1.4202,
1.3809; .35, 1.3879, 1.3938, 1.3938, 1.3985, 1.4512, 1.4565; .35,
1.3795, 1.3798, 1.3798, 1.381, 1.4294, 1.4345; .35, 1.3114, 1.3063,
1.3063, 1.3041, 1.3464, 1.3512; .35, 1.1864, 1.1763, 1.1763, 1.1709,
1.2057, 1.2099; .35, 1.0102, .9962, .9962, .9883, 1.0144, 1.0179;
.35, .7935, .7771, .7771, .7676, .7845, .7871; .35, .5532, .5364,
.5364, .5264, .5346, .5363; .35, .3147, .3, .3, .2912, .2922, .2931;
.35, .1144, .1051, .1051, .0995, .0969, .0971; .35, .0602, .0267,
.0267, .0202, .0185, .0198]`.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for airfoil lift and drag
coefficients`.

### **Number of blade elements** — Number of blade elements `20` (default) | positive integer

Number of blade elements for a single blade.

#### Dependencies

To enable this parameter, set
**Parameterization** to
`Tabulated data for airfoil lift and drag
coefficients`.

### Environment and Dynamics

### **Output thrust** — Option to model turbine thrust output `off` (default) | `on`

Whether to model the thrust forces that the turbine encounters.
Selecting this parameter enables port **T**.

### **Model inertia** — Inertia option `off` (default) | `on`

Whether to simulate inertia due to the motion of the rotor. The block
applies inertia at port **R**.

### **Rotor inertia** — Windmill rotor inertia `3.5e7` `kg*m^2` (default)

Inertia of the windmill rotor.

#### Dependencies

To enable this parameter, select **Model
inertia**.

### **Initial rotor rotational velocity** — Rotor initial angular velocity `0` `rad/s` (default)

Initial rotational velocity at port **R**.

#### Dependencies

To enable this parameter, select **Model
inertia**.

### **Air density** — Air density `1.225` `kg/m^3` (default) | positive scalar

Constant density of air.

### Advanced

### **Wind velocity threshold** — Wind velocity smoothing threshold `0.01` `m/s` (default) | positive scalar

Wind velocity at which the block applies smoothing.

### **Rotational velocity threshold** — Angular velocity smoothing threshold `0.01` `rad/s` (default) | positive scalar

Rotational velocity at which the block applies smoothing. This
parameter smooths the torque and power when the rotational speed
approaches or crosses 0. The block applies more smoothing over greater
velocity ranges as you increase the value of this parameter.

## Libraries

Simscape / Driveline / Engines & Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2024a: Parameterize block using airfoil lift and drag coefficients

To parameterize the block using airfoil lift and drag coefficients, set
**Parameterization** to `Tabulated data for
airfoil lift and drag coefficients`.

### R2023a: Performance Updates

Port **C** is no longer required and has been removed.

The default value for the **Power coefficient table, Cp(β, λ)**
has been updated. The block asserts *Cp*(λ=0)≅ 0.

### R2023a: New Inertia Option

Include inertia within the Wind Turbine block by
selecting **Model inertia**.

## Description

Turbine that converts wind kinetic energy into rotational motion

The Wind Turbine block represents a wind turbine that
converts wind motion into mechanical rotational energy. Wind turbines harness wind
energy for electricity generation. Wind turbine development focuses on enhancing the
efficiency, reliability, and cost-effectiveness of individual turbines, while wind
turbine farm development involves the strategic placement of multiple turbines to
optimize energy capture. You can use the block to simulate individual wind turbines and
entire wind farms. You can analyze the turbine performance, power generation, and
interactions in a wind farm, or the effect of different turbine geometries,
configurations, control algorithms, and layout designs on wind farm performance and
energy output.

You specify the incident wind velocity and collective blade pitch as inputs, and you
can optionally output the thrust acting on the turbine. You can include the effects of
thrust and inertia. Parameterize the block using tabulated power and thrust coefficients
or airfoil lift and drag coefficients.

### Parameterize by Power and Thrust Coefficients

When you set **Parameterization** to `Tabulated
data for power and thrust coefficients`, the block calculates the
coefficients of power and torque using table lookups, such that

CP=tablelookup(βRef,λRef,CP,Ref,β,λSmooth,interpolation = linear,extrapolation = nearest)CT=tablelookup(βRef,λRef,CT,Ref,β,λSmooth,interpolation = linear,extrapolation = nearest)

where:

- *βRef* is the reference pitch
  angle.
- *λRef* is the reference tip
  speed ratio.
- *CP,Ref* and
  *CT,Ref* are the
  **Power coefficient table** and **Thrust
  coefficient table** parameters, respectively.
- *λSmooth* is the smoothed tip
  speed ratio.

The block uses this equation as the basis for the instantaneous tip
speed ratio

λ=Rωv,

where:

- *R* is the **Turbine radius**
  parameter.
- *ɷ* is the differential angular velocity between the
  shaft and the case.
- *v* is the incident air velocity on the rotor. This
  value is the physical signal input port **V**.

The block uses this equation to describe the smoothed version of the
instantaneous tip speed ratio equation

λSmooth=Rωv(v2+vThr2)2,

where *vThr* is the
**Wind velocity threshold** parameter. The block uses these
equations as a basis for the power and thrust

Power=12CPρAv3=Torque⋅ωThrust=12CTρAv2

where:

- *ρ* is the **Air density**
  parameter.
- *A* is the area of the circle swept by the turbine
  blades, and *A* =
  *πr2*

To relate the block parameters to the wind turbine mechanical power
rating, determine the wind turbine power at the peak power coefficient and the rated
wind speed. The rated power corresponds to the block parameters using this equation

Powerrated=0.5CP,maxρAvrated3,

where:

- *CP,max* is the peak power
  coefficient. This is the maximum value in the **Power
  coefficient table, Cp(β,λ)** parameter.
- *Vrated* is the rated wind
  speed. Rated wind speeds are typically 10 to 15 m/s. Wind turbine
  controller designs may alter strategy at this wind speed to maintain the
  rated power.
- *A* is the rotor swept area, where *A =
  πr2*.

The block uses numerically smoothed equations for the thrust, power, and torque,
such that

Power=ρACP|v|32TorqueSmooth={0if ω<−ωThrPowerω2+ωThr2if ω>0PowerSmooth=TorqueSmoothωThrustSmooth=12CTρA(v2+vThr2)

where *ωThr* is the
**Rotational velocity threshold** parameter. When
*ɷ* < *-ɷThr*, the
block smoothly saturates the power to zero.

The block asserts *Cp*(λ=0)≅ 0. Generated power equals zero when the rotor rotational velocity is
zero, and a non-zero value of *Cp*(λ=0)
affects the start-up torque. The start-up torque relates to
*Cp*(λ=0) such that

TorqueStartup=ρACP(λ=0)|v|32ωThr.

Your model may be sensitive to this start-up torque behavior if
you simulate braking the rotor in strong winds.

### Parameterize by Airfoil Lift and Drag Coefficients

When you set **Parameterization** to `Tabulated data for
airfoil lift and drag coefficients`, you can parameterize the lift
and drag coefficients and the airfoil geometry for a given blade element. The
default values represent an NREL 5 MW reference wind turbine. The block treats the
propeller as a continuous disc. Conservation of momentum applies to the air that
crosses the disc when the block calculates the induced velocity,
*vi*. The block uses the induced
velocity to find the magnitude and direction of the total flow velocity at a vector
of radial locations along the blade, which it then uses to find lift and drag based
on the lift and drag coefficient lookup tables. These quantities are specific to
this parameterization:

- *TMT* — Thrust calculated by
  momentum theory
- *vi* — Axial flow velocity
  induced by the motion of the wind turbine blades
- *vr* —Radial velocity at the
  blade location
- *vax* — Axial velocity at the
  blade location
- *TBET* — Thrust calculated by
  blade element theory
- *QBET* — Torque calculated by
  blade element theory
- *Nblades* — Number of
  propeller blades
- *e* — Nondimensional location of the root cutout as
  given by the first element of the **Nondimensional radial
  location vector, r** parameter
- *Ω* — Wind turbine rotational velocity
- *R* — Wind turbine blade radius
- *Cl,Cd*
  — Element-wise coefficients of the lift and drag, respectively
- *ϕ(y)* — Flow angle at a given point along the
  blade
- *a* = -*vi/v*
  — Axial induction factor
- *a'=ω/2R* — Angular induction factor
- λr=RyΩv2+vThr2 — Smoothed local tip speed ratio at each blade
  element

The block uses momentum theory to define a smoothed thrust equation such that

TMT=CTρπR2(v2+vThr2)22,

where the block uses the Glauert correction in the turbulent wake
state when *a > 0.4*, such that

CT={4a(1−a)⋅sign(v)a≤0.4(89±49a+149a2)⋅sign(v)a>0.4

The block uses the axial induction factor to solve for
*vi*, such that

vi=−av.

The block interpolates the values from the **Nondimensional radial location
vector, r** parameter to find *y*. Then the block
interpolates the lift and drag coefficients to find
*Cl(y)* and
*Cd(y)* based upon the tabulated
angle of attack and lift and drag coefficients. The block uses blade element theory
to calculate the thrust and torque such that

TBET=NbladesρD24∫e1(vr2+vax2)⋅(Clcosϕ(y)+Cdsinϕ(y))⋅cdyQBET=NbladesρD38∫e1(vr2+vax2)⋅(Clsinϕ(y)+Cdcosϕ(y))⋅cydy

where:

vr=RyΩ(1+a')vax=v(1−a)

The block performs this integration across the each discrete
blade element. The block discretizes *y* according to the
specification in the **Number of blade elements** parameter and
calculates the angular induction factor at each blade element as

a'=−12+121+4λr2a(1−a).

### Assumptions and Limitations

The block generates torque and power only for positive angular velocities.
