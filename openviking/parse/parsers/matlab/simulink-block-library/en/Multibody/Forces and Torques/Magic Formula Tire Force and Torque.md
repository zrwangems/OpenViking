---
type: simulink-block
title: 'Magic Formula Tire Force and Torque'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'magicformulatireforceandtorque'
documentation_source_path: 'ref/magicformulatireforceandtorque.html'
language: en
---

# Magic Formula Tire Force and Torque

## Ports
```yaml
ports:
- name: B
  summary: Base geometry geometry
  direction: input
- name: F
  summary: Follower frame frame
  direction: input
- name: lmux
  summary: Scaling factor of longitudinal friction coefficient, unitless physical signal
  direction: input
- name: lmuy
  summary: Scaling factor of lateral friction coefficient, unitless physical signal
  direction: input
- name: con
  summary: Contact signal, unitless physical signal
  direction: output
- name: ft
  summary: Tire force, *N* physical signal
  direction: output
- name: tt
  summary: Tire torque, *N\*m* physical signal
  direction: output
- name: t
  summary: Pneumatic trail, *m* physical signal
  direction: output
- name: kappa
  summary: Longitudinal slip, unitless physical signal
  direction: output
- name: kappas
  summary: Saturated longitudinal slip, unitless physical signal
  direction: output
- name: alpha
  summary: Slip angle, *rad* physical signal
  direction: output
- name: alphas
  summary: Saturated slip angle, *rad* physical signal
  direction: output
- name: phit
  summary: Turn slip, *rad/m* physical signal
  direction: output
- name: vx
  summary: Relative longitudinal velocity, *m/s* physical signal
  direction: output
- name: vy
  summary: Relative lateral velocity, *m/s* physical signal
  direction: output
- name: vsx
  summary: Longitudinal slip velocity, *m/s* physical signal
  direction: output
- name: vsy
  summary: Lateral slip velocity, *m/s* physical signal
  direction: output
- name: psid
  summary: Yaw velocity, *rad/s* physical signal
  direction: output
- name: gamma
  summary: Camber angle, *rad* physical signal
  direction: output
- name: gammas
  summary: Saturated camber angle, *rad* physical signal
  direction: output
- name: gammad
  summary: Camber velocity, *rad/s* physical signal
  direction: output
- name: omega
  summary: Spin velocity, *rad* physical signal
  direction: output
- name: romega
  summary: Free radius, *m* physical signal
  direction: output
- name: rl
  summary: Loaded radius, *m* physical signal
  direction: output
- name: re
  summary: Effective rolling radius, *m* physical signal
  direction: output
- name: rho
  summary: Radial deflection, *m* physical signal
  direction: output
- name: mux
  summary: Longitudinal friction coefficient, unitless physical signal
  direction: output
- name: muy
  summary: Lateral friction coefficient, unitless physical signal
  direction: output
- name: Rb
  summary: Base rotation, unitless physical signal
  direction: output
- name: pb
  summary: Base translation, *m* physical signal
  direction: output
- name: Rf
  summary: Follower rotation, unitless physical signal
  direction: output
- name: pf
  summary: Follower translation, *m* physical signal
  direction: output
```

### Geometry

### **B** — Base geometry geometry

Base geometry that represents the surface that the tire contacts. The
contact surface can move or be fixed relative to the world frame. You
must connect this port to an Infinite
Plane or Grid
Surface block.
### Frame

### **F** — Follower frame frame

Follower frame that represents the tire. The frame origin is located
at the center of the tire.
### Input

### **lmux** — Scaling factor of longitudinal friction coefficient, unitless physical signal

Physical signal port that accepts the scaling factor of the
longitudinal friction coefficient of the tire.

#### Dependencies

To enable this port, under **Scaling
Coefficients**, set **LMUX** to
`Provided by Input`.

### **lmuy** — Scaling factor of lateral friction coefficient, unitless physical signal

Physical signal port that accepts the scaling factor of the lateral
friction coefficient of the tire.

#### Dependencies

To enable this port, under **Scaling
Coefficients**, set **LMUY** to
`Provided by Input`.
### Output

### **con** — Contact signal, unitless physical signal

Physical signal output port that provides a signal to determine
whether the tire and contact surface have a valid contact. When they are
in contact and the contact is valid, the signal equals
`1`, otherwise the signal equals
`0`.

If the follower frame is below the contact surface, the tire and the
surface have an invalid contact and the block does not apply force and
torque to the tire.

#### Dependencies

To enable this port, under **Sensing**, select
**Contact Signal**.

#### Force/Torque

### **ft** — Tire force, *N* physical signal

Physical signal output port that provides the magic formula tire force
that is applied to the contact frame of the block. The output contains
three parts:

- Fx is the longitudinal force tangential
  to the contact surface at the contact point.
- Fy is the lateral force which is
  orthogonal to the plane defined by Fx and
  Fz.
- Fz is the normal force that is normal
  to the contact surface at the contact point.

The block resolves the force in the follower frame of the tire if you
set the **Resolution Frame** parameter to
`Follower`.

#### Dependencies

To enable this port, under **Sensing >
Force/Torque**, select **Tire
Force**.

### **tt** — Tire torque, *N\*m* physical signal

Physical signal output port that provides the magic formula tire
torque that is applied to the contact frame of the block. The output
contains three parts:

- Mx is the overturning moment.
- My is the rolling resistance
  moment.
- Mz is the aligning torque.

The block resolves the torque in the follower frame of the tire if you
set the **Resolution Frame** parameter to
`Follower`.

#### Dependencies

To enable this port, under **Sensing >
Force/Torque**, select **Tire
Torque**.

### **t** — Pneumatic trail, *m* physical signal

Physical signal output port that provides the distance from the
contact point to the point of the resultant lateral force. The value has
a unit of length.

You can use the pneumatic trail to compute the aligning torque,
*M*z.

#### Dependencies

To enable this port, under **Sensing >
Force/Torque**, select **Pneumatic
Trail**.

#### Slip

### **kappa** — Longitudinal slip, unitless physical signal

Physical signal output port that provides the ratio of the
longitudinal slip velocity to the longitudinal speed of the tire.

#### Dependencies

To enable this port, under **Sensing > Slip**,
select **Longitudinal Slip**.

### **kappas** — Saturated longitudinal slip, unitless physical signal

Physical signal output port that provides the longitudinal slip
saturated to always be within the limits defined by the KPUMIN and
KPUMAX parameters.

#### Dependencies

To enable this port, under **Sensing > Slip**,
select **Saturated Longitudinal Slip**.

### **alpha** — Slip angle, *rad* physical signal

Physical signal output port that provides the angle of the right
triangle made by the lateral slip velocity,
*V*sy and the longitudinal
speed, *V*x. The value has a
unit of angle.

Slip angle illustration

#### Dependencies

To enable this port, under **Sensing > Slip**,
select **Slip Angle**.

### **alphas** — Saturated slip angle, *rad* physical signal

Physical signal output port that provides the slip angle saturated to
always be within the limits defined by the ALPMIN and ALPMAX parameters.
The value has a unit of angle.

#### Dependencies

To enable this port, under **Sensing > Slip**,
select **Saturated Slip Angle**.

### **phit** — Turn slip, *rad/m* physical signal

Physical signal output port that provides the ratio of the tire yaw
velocity to the magnitude of the tire velocity in the
*xy*-plane of the contact frame. The value has a
unit of angle/length.

Turn slip is useful when modeling low speed cornering, such as parking
maneuvers.

#### Dependencies

To enable this port, under **Sensing > Slip**,
select **Turn Slip**.

#### Linear Velocity

### **vx** — Relative longitudinal velocity, *m/s* physical signal

Physical signal output port that provides the component of the relative velocity between
the follower frame and the contact point on the base geometry along the
*x*-direction of the contact frame. The value has
a unit of length/time.

#### Dependencies

To enable this port, under **Sensing > Linear
Velocity**, select **Relative Longitudinal
Velocity**.

### **vy** — Relative lateral velocity, *m/s* physical signal

Physical signal output port that provides the component of the relative velocity between
the follower frame and the contact point on the base geometry along the
*y*-direction of the contact frame. The value has
a unit of length/time.

#### Dependencies

To enable this port, under **Sensing > Linear
Velocity**, select **Relative Lateral
Velocity**.

### **vsx** — Longitudinal slip velocity, *m/s* physical signal

Physical signal output port that provides the component of the relative velocity between
the slip point on the tire and the coincident point on the base geometry
along the *x*-direction of the contact frame. The
value has a unit of length/time.

#### Dependencies

To enable this port, under **Sensing > Linear
Velocity**, select **Longitudinal Slip
Velocity**.

### **vsy** — Lateral slip velocity, *m/s* physical signal

Physical signal output port that provides the component of the relative velocity between
the slip point on the tire and the coincident point on the base geometry
along the *y*-direction of the contact frame. The
value has a unit of length/time.

#### Dependencies

To enable this port, under **Sensing > Linear
Velocity**, select **Lateral Slip
Velocity**.

#### Yaw

### **psid** — Yaw velocity, *rad/s* physical signal

Physical signal output port that provides the first derivative of the
yaw angle. The value has a unit of angle/time.

#### Dependencies

To enable this port, under **Sensing > Yaw**,
select **Velocity**.

#### Camber

### **gamma** — Camber angle, *rad* physical signal

Physical signal output port that provides the camber angle of the
tire. The value has a unit of angle.

#### Dependencies

To enable this port, under **Sensing > Camber**,
select **Angle**.

### **gammas** — Saturated camber angle, *rad* physical signal

Physical signal output port that provides the camber angle of the tire
saturated to always be within the limits defined by the CAMMIN and
CAMMAX parameters. The value has a unit of angle.

#### Dependencies

To enable this port, under **Sensing > Camber**,
select **Angle**.

### **gammad** — Camber velocity, *rad/s* physical signal

Physical signal output port that provides the first derivative of the
camber angle. The value has a unit of angle/time.

#### Dependencies

To enable this port, under **Sensing > Camber**,
select **Velocity**.

#### Spin

### **omega** — Spin velocity, *rad* physical signal

Physical signal output port that provides the first derivative of the
spin angle. The value has a unit of angle/time.

#### Dependencies

To enable this port, under **Sensing > Spin**,
select **Velocity**.

#### Tire Radius

### **romega** — Free radius, *m* physical signal

Physical signal output port that provides the free radius of the tire.
The radius increases as the tire rotates faster. The value has a unit of
length.

#### Dependencies

To enable this port, under **Sensing > Tire
Radius**, select **Free
Radius**.

### **rl** — Loaded radius, *m* physical signal

Physical signal output port that provides the distance from the center
of the tire to the contact point between the tire and the contact
surface. The value has a unit of length.

#### Dependencies

To enable this port, under **Sensing > Tire
Radius**, select **Loaded
Radius**.

### **re** — Effective rolling radius, *m* physical signal

Physical signal output port that provides the distance from the
follower frame to the slip point. The value has a unit of length.

#### Dependencies

To enable this port, under **Sensing > Tire
Radius**, select **Effective Rolling
Radius**.

### **rho** — Radial deflection, *m* physical signal

Physical signal output port that provides the difference between the
free radius output from the **romega** port and the
loaded radius output from the **rl** port. The value
has a unit of length.

#### Dependencies

To enable this port, under **Sensing > Tire
Radius**, select **Radial
Deflection**.

#### Friction

### **mux** — Longitudinal friction coefficient, unitless physical signal

Physical signal output port that provides the longitudinal friction
coefficient of the tire computed by the magic formula equations.

#### Dependencies

To enable this port, under **Sensing >
Friction**, select **Longitudinal Friction
Coefficient**.

### **muy** — Lateral friction coefficient, unitless physical signal

Physical signal output port that provides the lateral friction
coefficient of the tire computed by the magic formula equations.

#### Dependencies

To enable this port, under **Sensing >
Friction**, select **Lateral Friction
Coefficient**.

#### Contact Frame

### **Rb** — Base rotation, unitless physical signal

Physical signal port that outputs a 3-by-3 rotation matrix that maps the vectors
in the contact frame to vectors in the reference frame of the base geometry. The
output signal is resolved in the reference frame associated with the base
geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Base Rotation**.

### **pb** — Base translation, *m* physical signal

Physical signal port that outputs a 3-by-1 vector that contains the coordinates of
the origin of the contact frame resolved in the reference frame of the base
geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Base Translation**.

### **Rf** — Follower rotation, unitless physical signal

Physical signal port that outputs a 3-by-3 rotation matrix that maps vectors in
the contact frame to vectors in the reference frame of the follower geometry. The
output signal is resolved in the reference frame associated with the follower
geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Follower Rotation**.

### **pf** — Follower translation, *m* physical signal

Physical signal port that outputs a 3-by-1 vector that contains the coordinates of
the origin of the contact frame resolved in the reference frame of the follower
geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Follower Translation**.
## Parameters
```yaml
parameters:
- name: Tire Side
  summary: Tire position during modeling Left (default) | Right
  group: ''
- name: Tire Parameters
  summary: Parameters of tire [] (default) | scalar structure array
  group: ''
- name: Slip Mode
  summary: Slip mode Combined (default) | Combined + Turn
  group: ''
- name: Contact Frame Method
  summary: Method to use to compute location and orientation of contact frame Closest Point (default) | Weighted Penetration
  group: ''
- name: LMUX
  summary: Scaling factor of longitudinal friction coefficient From Tire Parameters (default) | Provided by Input
  group: Scaling Coefficients
- name: LMUY
  summary: Scaling factor of lateral friction coefficient From Tire Parameters (default) | Provided by Input
  group: Scaling Coefficients
- name: Resolution Frame
  summary: Frame to resolve measurements Contact (default) | Follower
  group: Sensing
```

### **Tire Side** — Tire position during modeling `Left` (default) | `Right`

Tire position during modeling, specified as either `Left` or
`Right`. Set the parameter to the side of the vehicle
to which the tire is mounted.

### **Tire Parameters** — Parameters of tire [] (default) | scalar structure array

Tire parameters, specified as a scalar structure array. Use the `simscape.multibody.tirread` function to generate the
structure array from a TIR file. The structure array must include all the
necessary tire parameters, while any extra parameters are ignored in the
tire modeling. For the list of required parameters, see Required Tire Parameters.

### **Slip Mode** — Slip mode `Combined` (default) | `Combined + Turn`

Slip mode, specified as either `Combined` or
`Combined + Turn`.

To model combined slip, select `Combined`. To model combined
slip with turn slip effects, select `Combined +
Turn`. When selecting this option, the tire parameters
require the turn slip coefficients.

**Turn Slip Coefficients**

|  |  |
| --- | --- |
| PDXP1 | Peak FX reduction due to spin parameter |
| PDXP2 | Peak FX reduction due to spin with varying load parameter |
| PDXP3 | Peak FX reduction due to spin with kappa parameter |
| PKYP1 | Cornering stiffness reduction due to spin |
| PDYP1 | Peak FY reduction due to spin parameter |
| PDYP2 | Peak FY reduction due to spin with varying load parameter |
| PDYP3 | Peak FY reduction due to spin with alpha parameter |
| PDYP4 | Peak FY reduction due to square root of spin parameter |
| PHYP1 | FY-alpha curve lateral shift limitation |
| PHYP2 | FY-alpha curve maximum lateral shift parameter |
| PHYP3 | FY-alpha curve maximum lateral shift varying with load parameter |
| PHYP4 | FY-alpha curve maximum lateral shift parameter |
| PECP1 | Camber w.r.t. spin reduction factor parameter in camber stiffness |
| PECP2 | Camber w.r.t. spin reduction factor varying with load parameter in camber stiffness |
| QDTP1 | Pneumatic trail reduction factor due to turn slip parameter |
| QCRP1 | Turning moment at constant turning and zero forward speed parameter |
| QCRP2 | Turn slip moment (at alpha=90deg) parameter for increase with spin |
| QBRP1 | Residual (spin) torque reduction factor parameter due to side slip |
| QDRP1 | Turn slip moment peak magnitude parameter |

[1]

### **Contact Frame Method** — Method to use to compute location and orientation of contact frame `Closest Point` (default) | `Weighted Penetration`

Method to use to compute the location and orientation of the contact
frame, specified as:

- `Closest Point`: This method
  determines the contact point by locating the point on the
  contact surface that is closest to the center of the tire and
  lies in the plane of the tire. The contact normal vector is at
  the contact point and perpendicular to the contact patch at the
  contact point.
- `Weighted Penetration`: This method
  simplifies the computation due to the irregularities of the
  contact surface and computes an equivalent plane at each
  simulation time step to approximate the actual contact area. The
  contact point is the nearest point on this equivalent plane to
  the center of the tire. The contact normal vector is at the
  contact point and perpendicular to the equivalent plane. For
  more information, see the description of Custom Tire Force and Torque.

For both settings, the contact frame is at the contact point and the
*z*-axis of the frame is aligned with
the contact normal.

### Scaling Coefficients

### **LMUX** — Scaling factor of longitudinal friction coefficient `From Tire Parameters` (default) | `Provided by Input`

Scaling factor for the longitudinal friction coefficient. Select `From Tire
Parameters` to use the constant scaling factor provided
by the TIR file, or select `Provided by Input`
to use input signals as scaling factors.

### **LMUY** — Scaling factor of lateral friction coefficient `From Tire Parameters` (default) | `Provided by Input`

Scaling factor for the lateral friction coefficient. Select `From Tire
Parameters` to use the constant scaling factor provided
by the TIR file, or select `Provided by Input`
to use input signals as scaling factors.

### Sensing

#### Force/Torque

### **Resolution Frame** — Frame to resolve measurements `Contact` (default) | `Follower`

Frame used to resolve the calculated tire force and torque, specified
as either `Contact` or
`Follower`.
## Libraries

Simscape / Multibody / Forces and Torques

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

### R2024b: Compute contact frame

Use the closest point or the weighted penetration method to compute the location and
orientation of the contact frame between the tire and the contact surface.

### R2024b: Compute radial deflection

Use the **rho** port to output the radial deflection. The radial
deflection is the difference between the tire free radius and the loaded
radius.

### R2023a: Base geometry supports the Grid Surface block

Use the Grid Surface block to represent the contact
surface.

## Description

Apply steady-state tire force and torque by using Magic Formula tire equations

The Magic Formula Tire Force and Torque block implements the
combined slip steady-state Magic Formula model and can optionally include turn slip
effects [1]. You can use the block
for tires that have square-like cross-sections, such as the tires of passenger cars,
trucks, and off-road vehicles.

The block calculates only the tire force and torque. To model the geometry and inertia
properties of the tire, you must use a solid block, such as the Cylindrical
Solid block. The Magic Formula tire model assumes that tires are
disks, as shown in the diagram.

The follower frame is at the center of the tire and rotates with the tire. The contact frame
is at the contact point between the tire and the contact surface. The tire block has two
methods to compute the location and orientation of the contact frame. For scenarios that
require only single-point contact, use the closest point method. For driving conditions
that require multiple-point contacts, use the weighted penetration method. For more
information, see Contact Frame Method.

The image shows the contact and follower frames of the tire at zero
configuration.

The yaw, camber, and spin angles correspond to a
*y*-*x*-*z* sequence rotation
about the follower frame of the tire.

To specify the properties of a tire model, generate a scalar structure array by using
the `simscape.multibody.tirread` function and enter the array in the
**Tire Parameters** parameter. The structure array must include all
the necessary tire parameters, while any extra parameters are ignored in the tire
modeling. For the list of required parameters, see Required Tire Parameters. The block uses the
ISO sign conventions.

To specify the side of the vehicle to which a tire is mounted, use the **Tire
Side** parameter. Specifying the wrong side can lead to unexpected
simulation results. To correctly orient the tires on a vehicle, you must align the
*z*-axes of the follower frames with the blue arrows shown in the
diagram.

The z-axes of the follower frames for tires

The signal output by the **con** port indicates whether the tire and the
contact surface have a valid contact. If the tire and the surface are not in contact or
the contact is not valid, all sensed outputs, such as the tire force, tire torque, and
slip angle, become zero.
