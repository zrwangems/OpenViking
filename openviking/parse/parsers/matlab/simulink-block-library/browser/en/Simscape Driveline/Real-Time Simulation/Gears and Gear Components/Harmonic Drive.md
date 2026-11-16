---
type: simulink-block
title: 'Harmonic Drive'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Gears / Gear Assemblies'
documentation_page: 'harmonicdrive'
documentation_source_path: 'ref/harmonicdrive.html'
language: en
---

# Harmonic Drive

## Ports

### Conserving

### **B** — Base shaft mechanical rotational

Mechanical rotational conserving port associated with the base shaft
and the strain wave generator.

When you select **Ring gear rotation**, this port
corresponds to port **S** of the
Planetary Gear block.

### **F** — Follower shaft mechanical rotational

Mechanical rotational conserving port associated with the follower
shaft and the flexible spline.

When you select **Ring gear rotation**, this port
corresponds to port **R** of the
Planetary Gear block.

### **C** — Circular spline mechanical rotational

Mechanical rotational conserving port associated with the circular
spline.

This port corresponds to port **C** of the
Planetary Gear block.

#### Dependencies

To enable this port, select **Ring gear
rotation**.

### **H** — Heat transfer thermal

Thermal conserving port associated with heat transfer.

#### Dependencies

To enable this port, set **Friction model** to
either `Temperature-dependent efficiency`
or `Temperature and load-dependent
efficiency`.

## Parameters

### Main

### **Ring gear rotation** — Option to simulate ring gear motion `off` (default) | `on`

Option to simulate ring gear rotation. Selecting this parameter
enables port **R**.

### **Number of teeth on elliptical gear** — Elliptical gear teeth `100` (default) | positive scalar

Total number of teeth protruding outward from the elliptical gear
perimeter. The value of this parameter should be slightly smaller than
the number of teeth on the circular ring gear. The default difference of
two teeth is common. The ratio of the two gear tooth numbers defines the
relative angular velocities of the base and follower shafts.

### **Number of teeth on circular gear** — Circular gear teeth `102` (default) | positive scalar

Number of teeth protruding inward from the circular ring gear
perimeter. The value of this parameter should be slightly larger than
the number of teeth on the elliptical gear. The default difference of
two teeth is common. The ratio of the two gear tooth numbers defines the
relative angular velocities of the base and follower shafts.

### Meshing Losses

### **Friction model** — Gear friction model `No meshing losses - Suitable for HIL simulation` (default) | `Constant efficiency` | `Load-dependent efficiency` | `Temperature-dependent efficiency` | `Temperature and load-dependent efficiency`

Option to include friction meshing losses:

- `No meshing losses - Suitable for HIL
  simulation` — The block ignores meshing
  losses.
- `Constant efficiency` — You
  specify a component efficiency that remains constant
  throughout the simulation.
- `Load-dependent efficiency` — The
  block reduces torque transfer by a variable efficiency
  factor. This factor falls in the range 0 < *η* <
  1 and varies with the torque load.
- `Temperature-dependent
  efficiency` — The block determines the
  torque transfer efficiency from the input at port
  **H**. This factor falls in the range 0 < *η* ≤ 1 and is independent from load.
- `Temperature and load-dependent
  efficiency` — The block reduces torque
  transfer by a variable efficiency factor that depends on
  temperature and load. This factor falls in the range 0 < *η* <
  1 and varies with the torque load.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation**.

### **Efficiency** — Torque transfer efficiency `0.95` (default) | positive scalar in the range of (0, 1]

Torque transfer efficiency (*η*) between base and
follower shafts. This parameter is inversely proportional to the meshing
power losses.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to `Constant efficiency`.

### **Follower power threshold** — Value above which the full efficiency factor is applied `0.001` `W` (default) | positive scalar

Absolute value of the follower shaft power above which the full
efficiency factor is in effect. A hyperbolic tangent function smooths
the efficiency factor from zero when at rest to the full efficiency
value at the power threshold.

As a guideline, the power threshold should be lower than the expected
power transmitted during simulation. Higher values might cause the block
to underestimate efficiency losses. However, very low values may raise
the computational cost of simulation.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to `Constant efficiency`.

### **Input shaft torque at no load** — Net torque on idle shaft `0.1` `N*m` (default) | positive scalar

Net torque (*τ*idle) acting on
the input shaft in idle mode, e.g., when torque transfer to the output
shaft equals zero. For nonzero values, the power input in idle mode
completely dissipates due to meshing losses.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to `Load-dependent efficiency`.

### **Nominal output torque** — Value of torque at which efficiency is normalized `5` `N*m` (default) | positive scalar

Output torque (*τ*F) at which
to normalize the load-dependent efficiency.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to `Load-dependent efficiency`.

### **Efficiency at nominal output torque** — Transfer efficiency `0.95` (default) | positive scalar in the range of (0,1]

Torque transfer efficiency (*η*) at the nominal
output torque. Larger efficiency values correspond to greater torque
transfer between the input and output shafts.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to `Load-dependent efficiency`.

### **Follower angular velocity threshold** — Value above which the full efficiency factor is applied `0.01` `rad/s` (default) | positive scalar

Absolute value of the follower shaft angular velocity above which the
full efficiency factor is in effect
(*ω*F). Below this value, a
hyperbolic tangent function smooths the efficiency factor to one,
lowering the efficiency losses to zero when at rest.

As a guideline, the angular velocity threshold should be lower than
the expected angular velocity during simulation. Higher values might
cause the block to underestimate efficiency losses. However, very low
values may raise the computational cost of simulation.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to `Load-dependent efficiency`.

### **Temperature** — Array for tabular parameterization of efficiency `[280 300 320]` `K` (default) | vector

Array of temperatures used to construct an efficiency lookup table.
The array values must increase from left to right. The temperature array
must be the same size as the efficiency array in temperature-dependent
models. The array must be the same size as the
**Efficiency** array.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to either:

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

### **Efficiency** — Array of gear efficiencies `[0.95 0.9 0.85]` (default) | vector

Array of efficiencies used to construct a 1-D temperature-efficiency
lookup table for temperature-dependent efficiency models. The array
elements are the efficiencies at the temperatures in the
**Temperature** array. The two arrays must be the
same size.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to either:

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

### **Follower power threshold** — Power below which numerical smoothing is applied `0.001` `W` (default) | positive scalar

Absolute value of the follower shaft power above which the full
efficiency factor is in effect. A hyperbolic tangent function smooths
the efficiency factor between zero when at rest and the value provided
by the temperature-efficiency lookup table when at the power
threshold.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to `Temperature-dependent
efficiency`.

### **Load at elliptical gear** — Elliptical-gear loads for tabular parameterization of efficiency `[1 5 10]` `N*m` (default) | numerical array

Array of elliptical-gear loads used to construct a 2-D
temperature-load-efficiency lookup table for
temperature-and-load-dependent efficiency models. The array values must
increase from left to right. The load array must be the same size as a
single column of the efficiency matrix.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to `Temperature and load-dependent
efficiency`.

### **Efficiency matrix** — Efficiency array for tabular parameterization of efficiency `[ 0.85 0.8 0.75; 0.95 0.9 0.85; 0.85 0.8 0.7 ]` (default) | numerical array

Matrix of component efficiencies used to construct a 2-D
temperature-load-efficiency lookup table. The matrix elements are the
efficiencies at the temperatures in the **Temperature**
array and at the loads in the **Load at elliptical
gear** array.

The number of rows must be the same as the number of elements in the
**Temperature** array. The number of columns must
be the same as the number of elements in the **Load at
elliptical gear** array.

#### Dependencies

To enable this parameter, clear **Ring gear
rotation** and set **Friction model**
to `Temperature and load-dependent
efficiency`.

### **Follower angular velocity threshold** — Angular velocity below which numerical smoothing is applied `0.01` `rad/s` (default) | positive scalar

Absolute value of the follower shaft angular velocity above which the
full efficiency factor is in effect. Below this value, a hyperbolic
tangent function smooths the efficiency factor to one, lowering the
efficiency losses to zero when at rest.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature and load-dependent
efficiency`.

### **Friction model** — Friction model `No meshing losses - Suitable for HIL simulation` (default) | `Constant efficiency` | `Temperature-dependent efficiency`

Friction model for the block:

- `No meshing losses - Suitable for HIL
  simulation` — Gear meshing is ideal.
- `Constant efficiency` — Transfer
  of torque between the gear wheel pairs is reduced by a
  constant efficiency, *η*, such that 0 < *η* ≤ 1.
- `Temperature-dependent
  efficiency` — Transfer of torque between
  the gear wheel pairs is defined by the table lookup based on
  the temperature.

#### Dependencies

To enable this parameter, select **Ring gear
rotation**.

### **Sun-planet and ring-planet ordinary efficiencies** — Torque transfer efficiency vector `[.96, .98]` (default) | vector

Vector of torque transfer efficiencies where the first element
represents the relationship between the strain wave generator and the
elliptical gear, and the second element represents the relationship
between the elliptical gear and the circular ring gear.

#### Dependencies

To enable this parameter, select **Ring gear
rotation** and set **Friction model**
to `Constant efficiency`.

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | vector

Vector of temperatures used to construct a 1-D temperature-efficiency
lookup table. The vector elements must increase from left to
right.

#### Dependencies

To enable this parameter, select **Ring gear
rotation** and set **Friction model**
to `Temperature-dependent
efficiency`.

### **Sun-planet efficiency** — Sun gear to planet gear torque transfer efficiency `[.95, .9, .85]` (default) | vector

Vector of output-to-input power ratios that describe the power flow
from the strain wave generator to the elliptical gear. The block uses
the values to construct a 1-D temperature-efficiency lookup
table.

Each element is an efficiency that
relates to a temperature in the **Temperature** vector.
The length of the vector must be equal to the length of the
**Temperature** vector. Each element in the vector
must be in the range (0,1].

#### Dependencies

To enable this parameter, select **Ring gear
rotation** set **Friction model** to
`Temperature-dependent
efficiency`.

### **Ring-planet efficiency** — Torque transfer efficiency from the ring gear to the planet gear `[.95, .9, .85]` (default) | vector

Vector of output-to-input power ratios that describe the power flow
from the elliptical gear to the flexible gear. The block uses the values
to construct a 1-D temperature-efficiency lookup table.

Each element is an efficiency that
relates to a temperature in the **Temperature** vector.
The length of the vector must be equal to the length of the
**Temperature** vector. Each element in the vector
must be in the range (0,1].

#### Dependencies

To enable this parameter, select **Ring gear
rotation** set **Friction model** to
`Temperature-dependent
efficiency`.

### **Sun-carrier and planet-carrier power thresholds** — Minimum efficiency power threshold for the sun-carrier and planet-carrier gear couplings `[.001, .001]` `W` (default) | vector

Vector of power thresholds above which full efficiency factors apply.
Enter the thresholds in the order strain wave generator-circular gear,
elliptical gear-circular gear. Below these values, a hyperbolic tangent
function smooths the efficiency factor.

When you set **Friction model** to
`Constant efficiency`, the block lowers the
efficiency losses to zero when no power is transmitted. When you set
**Friction model** to
`Temperature-dependent efficiency`, the
block smooths the efficiency factors between zero when at rest and the
values provided by the temperature-efficiency lookup tables at the power
thresholds.

#### Dependencies

To enable this parameter, select **Ring gear
rotation** set **Friction model** to
`Constant efficiency` or
`Temperature-dependent
efficiency`.

### Viscous Losses

### **Viscous friction coefficients at base (B) and follower (F)** — Fluid dynamic friction coefficients `[0 0]` `N*m/(rad/s)` (default) | positive two-element vector

Two-element array with the viscous friction coefficients in effect at the base
and follower shafts. The default array corresponds to zero viscous
losses.

### Inertia

### **Inertia** — Option to include inertia `off` (default) | `on`

Whether to include inertia due to ring gear rotation.

#### Dependencies

To enable this parameter, select **Ring gear
rotation**.

### **Wave generator gear inertia** — Inertia of the wave generator gear `0.001` `kg*m^2` (default) | positive scalar

Inertia of the wave generator gear.

#### Dependencies

To enable this parameter, select **Ring gear
rotation** and **Inertia**.

### **Flexspline gear inertia** — Inertia of the flexspline gear `0.0005` `kg*m^2` (default) | positive scalar

Inertia of the flexspline gear.

#### Dependencies

To enable this parameter, select **Ring gear
rotation** and **Inertia**.

### **Ring gear inertia** — Ring gear inertia `0.001` `kg*m^2` (default) | positive scalar

Inertia due to rotation of the ring gear.

#### Dependencies

To enable this parameter, select **Ring gear
rotation** and **Inertia**.

### Thermal Port

### **Thermal mass** — Thermal mass `50` `J/K` (default) | positive scalar

Thermal energy required to change the component temperature by a single
degree. The greater the thermal mass, the more resistant the component is to
temperature change.

### **Initial temperature** — Initial temperature `300` `K` (default) | positive scalar

Component temperature at the start of simulation. The initial temperature
alters the component efficiency according to an efficiency vector that you
specify, affecting the starting meshing or friction losses.

## Libraries

Simscape / Driveline / Gears

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014a**

### R2025a: Enumeration Updates

The **Ring gear rotation** and **Inertia**
parameters now use check boxes. These parameters used drop downs in previous
releases.

### R2024b: Inertia updates

You now can specify the inertia of all gear subcomponents including the sun, ring,
and carrier gears. You also now can include the effects of planet procession in the
planet inertia behavior.

## Description

High-ratio speed reducer based on elastic deformation of an elliptical gear

The Harmonic Drive block represents a compact,
high-ratio speed reduction mechanism that contains three key components:

- Strain wave generator
- Elliptical gear
- Circular ring gear

A harmonic drive is backlash-free with a high-ratio of speed reduction by design. This
is advantageous for systems that require precise gear positioning. The base shaft turns
the strain wave generator, which is elliptical with bearings around the circumference.
The bearings allow the strain wave generator to rotate within the elliptical gear. The
elliptical gear is flexible, and the motion of the strain wave generator causes the
vertices of the elliptical gear to move. This deformation of the ellipse causes the
teeth of the elliptical gear to slowly climb the teeth of the circular ring gear. The
ring gear has more teeth than the elliptical gear to allow for this motion. The
elliptical gear transmits torque to the output shaft while rotating within the ring
gear.

Meshing occurs concurrently at both vertices of the elliptical gear. This design
doubles the teeth in mesh, thereby increasing the torque capacity of the drive system.

The internal meshing between the two gears causes the elliptical gear axis to spin
counter to the elliptical strain wave generator.

Large reduction ratios arise from the near-equal gear tooth numbers. The effective
gear reduction ratio is

r=nEnC−nE ,

where:

- *r* is the gear reduction ratio.
- *n*C is the number of teeth on the
  circular ring gear.
- *n*E is the number of teeth on the
  elliptical gear.

The Simple Gear block provides the
foundation for this block.

### Ring Gear Rotation

You can enable rotation of the circular ring gear by selecting the **Ring
gear rotation** parameter. The block enables port
**R**, which allows you to control the rotational motion of the
ring gear by using a mechanical rotational input signal.

**Note**

The **Ring gear rotation** parameter determines how you
parameterize meshing losses.

When you clear **Ring gear rotation**, the block calculates the
efficiencies using the Simple Gear block
implementation. In this case, you parameterize the meshing losses the same way you
would for the Simple Gear block. When you select
**Ring gear rotation**, the block calculates the efficiencies
by implementing the Planetary Gear block. For this
case, you parameterize the meshing losses the same way you would for the
Planetary Gear block.

### Thermal Model

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.

### Variables

Use the **Variables** settings to set the priority and initial target
values for the block variables before simulating. For more information, see Set Priority and Initial Target for Block Variables.
