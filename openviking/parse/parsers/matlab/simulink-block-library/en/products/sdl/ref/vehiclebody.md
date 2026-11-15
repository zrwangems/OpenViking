---
type: simulink-block
title: 'Vehicle Body'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Tires and Vehicles'
documentation_page: 'vehiclebody'
documentation_source_path: 'ref/vehiclebody.html'
language: en
---

# Vehicle Body

## Ports

### Input

### **W** — Headwind speed, m/s physical signal

Physical signal input port for headwind speed, in m/s.

### **beta** — Road incline angle, rad physical signal

Physical signal input port for road incline angle, in rad.

### **CG** — Center of gravity, m physical signal

Physical signal input port for the center of gravity of the
externally-defined mass relative to the CG of the vehicle body, in
m.

#### Dependencies

To enable this port, select **Externally-defined
additional mass**.

### **M** — Mass, kg physical signal

Physical signal input port for the externally-defined mass, in
kg.

#### Dependencies

To enable this port, select **Externally-defined
additional mass**.

### **J** — External moment of inertia, kg\*m^2 physical signal

Physical signal input port for the moment of inertia of the
externally-defined mass, in kg\*m^2.

#### Dependencies

To enable this port, select **Externally-defined
additional mass** and **Pitch
dynamics**.

### **CD** — Drag coefficient, unitless physical signal

Physical signal input port for the drag coefficient.

#### Dependencies

To enable this port, select **Variable drag
coefficient**.
### Output

### **V** — Longitudinal velocity, m/s physical signal

Physical signal output port for vehicle longitudinal velocity in the
vehicle reference frame, in m/s.

### **NF** — Front axle normal force, N physical signal

Physical signal output port for normal force on the front axle, in N.
Wheel forces are considered positive if acting downwards.

### **NR** — Rear axle normal force, N physical signal

Physical signal output port for normal force on the rear axle, in N.
Wheel forces are considered positive if acting downwards.
### Conserving

### **H** — Horizontal motion mechanical translational

Mechanical translational conserving port associated with the
horizontal motion of the vehicle body. Connect tire traction motion to
this port.

## Parameters

### Main

### **Mass** — Vehicle mass `1200` `kg` (default) | positive scalar

Mass of the vehicle.

### **Number of wheels per axle** — Wheel count `2` (default) | positive integer or two-element vector

Wheel counts on the front and rear axles. If the input is a scalar
number, the wheel counts of the front and rear axles are assumed the
same. For example, if the input is `2`, then the front
and rear axles are each assumed to have two wheels.

If the input is a two-element array, the first number is the
front-axle wheel count and the second number the rear-axle wheel count.
For example, if the input is the array `[2,1]`, then
the front axle is assumed to have two wheels and the rear axle one
wheel.

### **Horizontal distance from CG to front axle** — CG-to-front axle distance `1.4` `m` (default) | positive scalar

Horizontal distance, *a*, from the center of gravity
to the front wheel axle of the vehicle.

### **Horizontal distance from CG to rear axle** — CG-to-rear axle distance `1.6` `m` (default) | positive scalar

Horizontal distance, *b*, from the center of gravity
to the rear wheel axle of the vehicle.

### **CG height above ground** — CG-to-ground distance `0.5` `m` (default) | positive scalar

Distance, *h*, between the center of gravity of the
vehicle and the ground.

### **Gravitational acceleration** — Gravitational acceleration `9.81` `m/s^2` (default) | nonnegative scalar

Acceleration due to gravitational force acting at the center of
gravity of the vehicle.

### **Externally-defined additional mass** — Variable mass option `off` (default) | `on`

Option to include mass as time- or event-variant that affects the mass
and CG of the vehicle body. Use this option to represent vehicle
occupants or unconfined bodies.

### **Negative normal force warning** — Normal force warning `off` (default) | `on`

Whether the block generates a warning when normal force calculations
return negative values. The block can generate negative forces because
the equations assume that the wheels never lose contact.

### Drag

### **Frontal area** — Effective cross-sectional area `3` `m^2` (default) | positive scalar

Effective cross-sectional area, *A*, presented by the
vehicle in longitudinal motion. The block uses this value to calculate
the aerodynamic drag force on the vehicle.

### **Variable drag coefficient** — Variable drag option `off` (default) | `on`

Whether drag is variable. Control drag with port
**CD**.

### **Drag coefficient** — Aerodynamic drag coefficient `0.4` (default) | nonnegative scalar

Aerodynamic drag coefficient,
*C*d. The block uses this
value to calculate the aerodynamic drag force on the vehicle.

### **Air density** — Ambient air density `1.18` `kg/m^3` (default) | nonnegative scalar

Density of the air that surrounds the vehicle.

### Pitch

### **Pitch dynamics** — Pitch dynamics option `off` (default) | `on`

Whether to model pitch dynamics.

### **Pitch moment of inertia** — Pitch moment of inertia `4000` `kg/m^2` (default) | positive scalar

Moment of inertia for pitch calculations.

#### Dependencies

To enable this parameter, select **Pitch
dynamics**.

### **Suspension model** — Suspension parameterization method `Linear` (default) | `By table lookup`

Parameterization method for suspension modeling. To specify the data
using scalar values, select `Linear`. To
specify the data using vector values, select `By table
lookup`.

#### Dependencies

To enable this parameter, select **Pitch
dynamics**.

### **Front suspension stiffness** — Front suspension stiffness `1e4` `N/m` (default) | positive scalar

Front suspension stiffness per axle.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `Linear`.

### **Front suspension damping** — Front suspension damping `1e4``N/(m/s)` (default) | positive scalar

Front suspension damping per axle.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `Linear`.

### **Rear suspension stiffness** — Rear suspension stiffness `1e4` `N/m` (default) | positive scalar

Rear suspension stiffness per axle.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `Linear`.

### **Rear suspension damping** — Rear suspension damping `1e4` `N/(m/s)` (default) | positive scalar

Rear suspension damping per axle.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `Linear`.

### **Front suspension stiffness force vector** — Front suspension stiffness force `[-2000, -1000, 0, 1000, 2000]` `N` (default) | increasing vector

Stiffness force of the front suspension. Specify the output values for the lookup table as a vector. The
number of elements in the output vector must be the same as the number of elements in the input
vector. The input vector parameter is the **Front
suspension deformation vector** parameter.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `By table lookup`.

### **Front suspension deformation vector** — Front suspension deformation `[-.4, -.2, 0, .2, .4]` `m` (default) | increasing vector

Deformation of the front suspension specified in terms of
displacement. Specify the input values for the lookup table as a vector. The values of the elements in the vector must increase from left to right. The minimum number of elements in the vector depends on the interpolation method that you select. For linear interpolation, provide at least two elements. For smooth interpolation, provide at least three elements. The output vector parameter is the **Front
suspension stiffness force vector** parameter.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `By table lookup`.

### **Front suspension damping force vector** — Front suspension damping force `[-200, -100, 0, 100, 200]` `N` (default) | increasing vector

Damping force of the front suspension. Specify the output values for the lookup table as a vector. The
number of elements in the output vector must be the same as the number of elements in the input
vector. The input vector parameter is the **Front
suspension velocity vector** parameter.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `By table lookup`.

### **Front suspension velocity vector** — Front suspension velocity `[-4, -2, 0, 2, 4]` `m/s` (default) | increasing vector

Velocity of the front suspension. Specify the input values for the lookup table as a vector. The values of the elements in the vector must increase from left to right. The minimum number of elements in the vector depends on the interpolation method that you select. For linear interpolation, provide at least two elements. For smooth interpolation, provide at least three elements. The output vector parameter is the **Front
suspension damping force vector** parameter.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `By table lookup`.

### **Rear suspension stiffness force vector** — Rear suspension stiffness force `[-2000, -1000, 0, 1000, 2000]` `N` (default) | increasing vector

Stiffness force of the rear suspension. Specify the output values for the lookup table as a vector. The
number of elements in the output vector must be the same as the number of elements in the input
vector. The input vector parameter is the **Rear
suspension deformation vector** parameter.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `By table lookup`.

### **Rear suspension deformation vector** — Rear suspension deformation `[-.4, -.2, 0, .2, .4]` `m` (default) | increasing vector

Deformation of the rear suspension specified in terms of displacement.
Specify the input values for the lookup table as a vector. The values of the elements in the vector must increase from left to right. The minimum number of elements in the vector depends on the interpolation method that you select. For linear interpolation, provide at least two elements. For smooth interpolation, provide at least three elements. The output vector parameter is the **Rear
suspension stiffness force vector** parameter.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `By table lookup`.

### **Rear suspension damping force vector** — Rear suspension damping force `[-200, -100, 0, 100, 200]` `N` (default) | increasing vector

Damping force of the rear suspension. Specify the output values for the lookup table as a vector. The
number of elements in the output vector must be the same as the number of elements in the input
vector. The input vector parameter is the **Rear
suspension velocity vector** parameter.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `By table lookup`.

### **Rear suspension velocity vector** — Rear suspension velocity `[-4, -2, 0, 2, 4]` `m/s` (default) | increasing vector

Velocity of the rear suspension. Specify the input values for the lookup table as a vector. The values of the elements in the vector must increase from left to right. The minimum number of elements in the vector depends on the interpolation method that you select. For linear interpolation, provide at least two elements. For smooth interpolation, provide at least three elements. The output vector parameter is the **Rear
suspension damping force vector** parameter.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `By table lookup`.

### **Interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Interpolation methods for approximating the output value when the
input value is between two consecutive grid points are:

- `Linear` — Select this
  default option to get the best performance. Provide at least
  two values per dimension.
- `Smooth` — Select this
  option to produce a continuous curve with continuous
  first-order derivatives. Provide at least three values per
  dimension.

For more information on interpolation algorithms, see the PS Lookup Table (1D)
block reference page.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `By table lookup`.

### **Extrapolation method** — Extrapolation method `Linear` (default) | `Nearest` | `Error`

Extrapolation method for determining the output value when the input
value is outside the range specified in the argument list are:

- `Linear` — Produces a
  curve with continuous first-order derivatives in the
  extrapolation region and at the boundary with the
  interpolation region.
- `Nearest` — Produces an
  extrapolation that does not go above the highest point in
  the data or below the lowest point in the data.
- `Error` — Issues an error
  if the input signal is outside the range of the table.
  Select this option to avoid going into the extrapolation
  mode when you want your data to be within the table
  range.

For more information on extrapolation algorithms, see the PS Lookup Table (1D)
block reference page.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and set **Suspension
model** to `By table lookup`.

### **Hard stop** — Hard stop modeling option `off` (default) | `on`

Option to model hard stops for the front and rear suspension.

#### Dependencies

To enable this parameter, select **Pitch
dynamics**.

### **Front upper bound** — Hard stop front suspension upper bound `.25` (default) | positive scalar

Upper bound of the hard stop for the front suspension.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and **Hard stop**.

### **Front lower bound** — Vehicle front lower bound `-.25` (default) | negative scalar

Lower bound of the hard stop for the front suspension.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and **Hard stop**.

### **Front contact stiffness** — Vehicle front contact stiffness `1e6` (default) | positive scalar

Contact stiffness of the hard stop for the front suspension.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and **Hard stop**.

### **Front contact damping** — Vehicle front contact damping `150` (default) | positive scalar

Contact damping of the hard stop for the front suspension.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and **Hard stop**.

### **Rear upper bound** — Vehicle rear upper bound `.25` (default) | positive scalar

Upper bound of the hard stop for the rear suspension.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and **Hard stop**.

### **Rear lower bound** — Vehicle rear lower bound `-.25` (default) | negative scalar

Lower bound of the hard stop for the rear suspension.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and **Hard stop**.

### **Rear contact stiffness** — Vehicle rear contact stiffness `1e6` (default) | positive scalar

Contact stiffness of the hard stop for the rear suspension.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and **Hard stop**.

### **Rear contact damping** — Vehicle rear contact damping `150` (default) | positive scalar

Contact damping of the hard stop for the rear suspension.

#### Dependencies

To enable this parameter, select **Pitch
dynamics** and **Hard stop**.

### **Initial pitch** — Pitch at the beginning of the simulation `0` `rad` (default) | nonnegative scalar

Pitch at the beginning of the simulation.

#### Dependencies

To enable this parameter, select **Pitch
dynamics**.

### **Initial pitch rate** — Pitch rate at the beginning of the simulation `0` `rad/s` (default) | nonnegative scalar

Pitch rate at the beginning of the simulation.

#### Dependencies

To enable this parameter, select **Pitch
dynamics**.

## Libraries

Simscape / Driveline / Tires & Vehicles

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

### R2024b: Track power dissipated due to aerodynamic drag

The block now logs `power_dissipated` in the
`simlog` workspace variable, which represents the power
dissipated due to aerodynamic drag.

### R2024b: Control Drag with a Physical Signal

To control the drag coefficient with a physical signal at port **CD**,
select **Variable drag coefficient**.

## Description

Vehicle body with two axles in longitudinal motion

The Vehicle Body block represents a two-axle vehicle
body in longitudinal motion. The vehicle can have the same or a different number of
wheels on each axle. For example, two wheels on the front axle and one wheel on the rear
axle. The vehicle wheels are assumed identical in size. The vehicle can also have a
center of gravity (CG) that is at or below the plane of travel.

The block accounts for body mass, aerodynamic drag, road incline, and weight
distribution between axles due to acceleration and road profile. Optionally include
pitch and suspension dynamics. The vehicle does not move vertically relative to the
ground.

The block has an option to include an externally-defined mass and an
externally-defined inertia. The mass, inertia, and center of gravity of the vehicle body
can vary over the course of simulation in response to system changes. You can also
optionally control the drag coefficient with a physical signal.

### Model

The vehicle axles are parallel and form a plane. The longitudinal,
*x*, direction lies in this plane and perpendicular to the
axles. If the vehicle is traveling on an incline slope, *β*, the
normal, *z*, direction is not parallel to gravity but is always
perpendicular to the axle-longitudinal plane.

This figure and table define the vehicle motion model variables.

**Vehicle Dynamics and Motion**

Inclined vehicle body diagram

**Vehicle Model Variables**

| Symbol | Description |
| --- | --- |
| *g* | **Gravitational acceleration** parameter. |
| *β* | Road incline angle, parameter **beta**. |
| *m* | Mass of the vehicle, specified by either the **Mass** parameter or port **M**. |
| *h* | Height of vehicle center of gravity (CG) above the ground. |
| *a*, *b* | Distance of front and rear axles, respectively, from the normal projection point of vehicle CG onto the common axle plane. |
| *Vx* | Velocity of the vehicle. When *Vx* > 0, the vehicle moves forward. When *Vx* < 0, the vehicle moves backward. |
| *Vw* | Wind speed. When *Vw* > 0, the wind is headwind. When *Vw* < 0, the wind is tailwind. |
| *n* | **Number of wheels per axle** parameter. You can use an integer or a two-element vector where the elements represent the front and rear axles, respectively. |
| *Fxf*, *Fxr* | Longitudinal forces on each wheel at the front and rear ground contact points, respectively. |
| *Fzf*, *Fzr* | Normal load forces on each wheel at the front and rear ground contact points, respectively. |
| *A* | Effective frontal vehicle cross-sectional area. |
| *Cd* | Aerodynamic drag coefficient. |
| *ρ* | Mass density of air. |
| *Fd* | Aerodynamic drag force. |

### Equations

**Vehicle Dynamics**

The vehicle motion is a result of the net effect of all the forces and torques
acting on it. The longitudinal tire forces push the vehicle forward or backward.
The weight *mg* of the vehicle acts through its center of
gravity (CG). Depending on the incline angle, the weight pulls the vehicle to
the ground and pulls it either backward or forward. Whether the vehicle travels
forward or backward, aerodynamic drag slows it down. For simplicity, the drag is
assumed to act through the CG.

mV˙x=Fx−​ Fd−mg⋅sinβ

Integer nFx=n(Fxf+Fxr)Vector nFx=n(1)Fxf+n(2)Fxr

Fd=12CdρA(Vx+Vw)2⋅sgn(Vx+Vw)

Zero normal acceleration and zero pitch torque determine the normal force on
each front and rear wheel.

Integer nFzf=−h(Fd+mgsinβ+mV˙x)+b⋅mgcosβn(a+b)Vector nFzf=−h(Fd+mgsinβ+mV˙x)+b⋅mgcosβn(1)a+n(2)b

Integer nFzr=+h(Fd+mgsinβ+mV˙x)+a⋅mgcosβn(a+b)Vector nFzr=+h(Fd+mgsinβ+mV˙x)+a⋅mgcosβn(1)a+n(2)b

The wheel normal forces satisfy

Integer nFzf+Fzr=mgcosβnVector nn(1)Fzf+n(2)Fzr=mgcosβ

If you include an externally-defined mass or inertia, the equations are
shifted by the weighted value of the input.

**Pitch dynamics**

Pitch acceleration depends on three torque components and the inertia of the
vehicle:

α=(f⋅h)+(Fzfa)−(Fzrb)J

Where:

- *ɑ* is the pitch acceleration.
- *f* is the longitudinal force.
- *h* is the height of the center of gravity when
  measured parallel to the *z*-axis.
- *J* is the inertia.

If you choose a linear model for suspension stiffness and damping, the block
uses small angle approximation for pitch calculations. If you choose a table
lookup model, the block uses the vectors that you specify calculate pitch
dynamics. For hard stop equations, see Translational Hard
Stop.

**Energy Accounting**

You can track the power dissipated due to aerodynamic drag. The
`simlog` workspace variable contains the
`power_dissipated` variable.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

### Limitations and Assumptions

The Vehicle Body block lets you model only
longitudinal dynamics, parallel to the ground and oriented along the direction of
motion. The vehicle is assumed to be in pitch and normal equilibrium. The block does
not model pitch or vertical movement. As such, the equations assume that the wheels
never lose contact. This constraint can result in negative normal forces.
