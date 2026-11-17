---
type: simulink-block
title: 'Double-Shoe Brake'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Brakes & Detents / Rotational'
documentation_page: 'doubleshoebrake'
documentation_source_path: 'ref/doubleshoebrake.html'
language: en
---

# Double-Shoe Brake

## Ports
```yaml
ports:
- name: F
  summary: Actuating force physical signal
  direction: input
- name: S
  summary: Drum shaft rotation rotational mechanical
  direction: conserving
- name: H
  summary: Heat flow thermal
  direction: conserving
```

### Input

### **F** — Actuating force physical signal

Physical signal input port associated with the applied actuating
force.
### Conserving

### **S** — Drum shaft rotation rotational mechanical

Rotational conserving port associated with the rotating drum
shaft.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow.

#### Dependencies

This port is visible only when, in the
**Friction** settings, the **Thermal
Port** parameter is set to
`Model`.

Exposing this port makes related settings visible.
## Parameters
```yaml
parameters:
- name: Drum radius
  summary: Contact surface radius 150 mm (default) | positive scalar
  group: Geometry
- name: Actuator location radius
  summary: Center-to-center distance between drum and force line of action 100mm (default) | positive scalar
  group: Geometry
- name: Pin location radius
  summary: Center-to-center distance between hinge pin and drum 125mm (default) | positive scalar
  group: Geometry
- name: Pin location angle
  summary: Angular distance from hinge pin to brake symmetry axis 15deg (default) | nonnegative scalar
  group: Geometry
- name: Shoe beginning angle
  summary: Angle between hings pin and friction material 5deg (default) | positive scalar
  group: Geometry
- name: Shoe span angle
  summary: Friction material angle 120deg (default) | positive scalar
  group: Geometry
- name: Viscous friction coefficient
  summary: Viscous friction .01 n*m/(rad/s) (default) | nonnegatvie scalar
  group: Friction
- name: Thermal port
  summary: Thermal model Omit (default) | Model
  group: Friction
- name: Temperature
  summary: Temperature [280, 300, 320] K (default) | increasing vector
  group: Friction
- name: Contact friction coefficient
  summary: Coulomb friction 0.3 (default) | [0.1, 0.05, 0.03] (thermal model default) | positive scalar or vector
  group: Friction
- name: Angular velocity threshold
  summary: Rotational velocity required for near steady-state contact friction 0.01 rad/s (default) | positive scalar
  group: Friction
- name: Belt tension fault
  summary: Option to model belt tension fault Add fault
  group: Faults
- name: Belt force when faulted
  summary: Faulted belt force 0 N (default) | nonnegative scalar
  group: Faults
- name: Thermal mass
  summary: Resistance to temperature change 50 kJ/K (default) | scalar
  group: Thermal Port
```

### Geometry

### **Drum radius** — Contact surface radius `150` `mm` (default) | positive scalar

Radius of the drum contact surface. The value must be greater than
zero.

### **Actuator location radius** — Center-to-center distance between drum and force line of action `100``mm` (default) | positive scalar

Distance between the drum center and the force line of action. The
value must be greater than zero.

### **Pin location radius** — Center-to-center distance between hinge pin and drum `125``mm` (default) | positive scalar

Distance between the hinge pin and drum centers. The parameter must be
greater than zero.

### **Pin location angle** — Angular distance from hinge pin to brake symmetry axis `15``deg` (default) | nonnegative scalar

Angular coordinate of the hinge pin location from the brake symmetry
axis. The value must be greater than or equal to zero.

### **Shoe beginning angle** — Angle between hings pin and friction material `5``deg` (default) | positive scalar

Angle between the hinge pin and the beginning of the friction material
linen of the shoe. The value of the parameter must be in the range0 ≤ θsb ≤ (π-pin location
angle).

### **Shoe span angle** — Friction material angle `120``deg` (default) | positive scalar

Angle between the beginning and the end of the friction material linen
on the shoe. The value of the parameter must be in the range 0 < θsb ≤ (π -pin location
angle - shoe beginning angle).

### Friction

### **Viscous friction coefficient** — Viscous friction `.01` `n*m/(rad/s)` (default) | nonnegatvie scalar

Viscous friction coefficient at the contact surface. The value must be
greater than or equal to zero.

### **Thermal port** — Thermal model `Omit` (default) | `Model`

Model for heat flow and temperature change:

- `Omit` — Neglect thermal
  dynamics.
- `Model` — Include thermal
  dynamics.

#### Dependencies

When this parameter is set to `Model`,
thermal port **H** and related settings are
visible.

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | increasing vector

Array of temperatures used to construct a 1-D temperature-efficiency
lookup table. The array values must increase left to right.

#### Dependencies

This parameter is only visible when the **Thermal
Port** parameter is set to
`Model`.

### **Contact friction coefficient** — Coulomb friction `0.3` (default) | `[0.1, 0.05, 0.03]` (thermal model default) | positive scalar or vector

Coulomb friction coefficient at the belt-drum contact surface. The
value must be greater than zero. For the thermal model:

- The number of elements in the vector must be the same as
  the number of elements in the specified vector for the
  **Temperature** parameter
- The values increase left to right.
- Each value must be greater than zero.

#### Dependencies

This parameter is specified as a:

- Scalar when the **Thermal
  Port** parameter is set to
  `Omit`.
- Vector when the **Thermal
  Port** parameter is set to
  `Model`.

### **Angular velocity threshold** — Rotational velocity required for near steady-state contact friction `0.01` `rad/s` (default) | positive scalar

Angular velocity at which the contact friction coefficient practically
reaches its steady-state value. The value must be greater than
zero.

### Faults

To modify the faults, create a fault and, in the block dialog, click
**Open fault properties**. In the Property Inspector, click the
**Fault behavior** link to open the faults.

### **Belt tension fault** — Option to model belt tension fault `Add fault`

Whether to model a belt tension fault in the block. To add a fault,
click the **Add fault** hyperlink.

### **Belt force when faulted** — Faulted belt force `0` `N` (default) | nonnegative scalar

Belt force when faulted. When you trigger a fault, the block applies
the value of the **Belt force when faulted** parameter
instead of the value at port **F** for the remainder of the
simulation. When the value is `0`, no braking occurs.
When the value is relatively large, the brake is stuck.

#### Dependencies

To enable this parameter, first enable faults for the block by
clicking the **Add fault** hyperlink.

### Thermal Port

### **Thermal mass** — Resistance to temperature change `50` `kJ/K` (default) | scalar

Thermal energy required to change the component temperature by a
single degree. The greater the thermal mass, the more resistant the
component is to temperature change.

#### Dependencies

To enable this parameter, set **Thermal Port** to
`Model`.
## Libraries

Simscape / Driveline / Brakes & Detents / Rotational

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

### R2024a: Model faults with the Simscape faults interface

The Double-Shoe Brake block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

## Description

Frictional brake with two pivoted shoes diametrically positioned about a rotating drum with triggered faulting

The Double-Shoe Brake block represents a frictional
brake with two pivoted rigid shoes that press against a rotating drum to produce a
braking action. The rigid shoes sit inside or outside the rotating drum in a
diametrically opposed configuration. A positive actuating force causes the rigid shoes
to press against the rotating drum. Viscous and contact friction between the drum and
the rigid shoe surfaces cause the rotating drum to decelerate.

Double-shoe brakes provide high braking torque with small actuator deflections in
applications that include motor vehicles and some heavy machinery. The model employs a
simple parameterization with readily accessible brake geometry and friction
parameters.

### Equations

In the schematic, a) represents an internal double-shoe brake, and b) represents
an external double-shoe brake. In both configurations, a positive actuation force
*F* brings the shoe and drum friction surfaces into contact.
The result is a friction torque that causes deceleration of the rotating drum. Zero
and negative forces do not bring the shoe and drum friction surfaces into contact
and produce zero braking torque.

The model uses the long-shoe approximation. The equations for the friction torque
that the leading and trailing shoes develop are:

TLS=cμparD2(cosθsb−cosθs)sinθa,

TTS=cμpbrD2(cosθsb−cosθs)sinθa,

c=ra+rpcosθp,

where for 0≤θs≤π2,

θa=θs,

and for θs≥π2,

θa=π2.

Where:

- *TLS* is the brake torque the
  leading shoe develops.
- *TTS* is the brake torque the
  trailing shoe develops.
- *μ* is the effective contact friction
  coefficient.
- *pa* is the maximum linear
  pressure in the leading shoe-drum contact.
- *pb* is the maximum linear
  pressure in the trailing shoe-drum contact.
- *rD* is the drum
  radius.
- *θsb* is the shoe beginning
  angle.
- *θs* is the shoe span
  angle.
- *θa* is the angle from hinge
  pin to maximum pressure point.
- *c* is the arm length of the cylinder force with
  respect to the hinge pin.
- *rp* is the pin location
  radius.
- *θp* is the hinge pin location
  angle.
- *ra* is the actuator location
  radius.

The model assumes that only Coulomb friction acts at the shoe-drum surface
contact. Zero relative velocity between the drum and the shoes produces zero Coulomb
friction. To avoid discontinuity at zero relative velocity, the friction coefficient
formula employs the hyperbolic function

μ=μCoulombtanh(4ωshaftωthreshold),

where:

- *μ* is the effective contact friction
  coefficient.
- *μCoulomb* is the contact
  friction coefficient.
- *ωshaft* is the shaft
  velocity.
- *ωthreshold* is the angular
  velocity threshold.

Balancing the moments that act on each shoe with respect to the pin yields the
pressure acting at the shoe-drum surface contact. The equations for determining the
balance of moments for the leading shoe are

F=MN−MFc,

MN=parprDsinθa(12[θs−θsb]−14[sin2θs−sin2θsb]),

and

MF=μparDsinθa(rD[cosθsb−cosθs]+rp4[cos2θs−cos2θsb]),

where:

- *F* is the actuation force.
- *MN* is the moment acting on
  the leading shoe due to normal force.
- *MF* is the moment acting on
  the leading shoe due to friction force.
- *c* is the arm length of the cylinder force with
  respect to the hinge pin.
- *pa* is the maximum linear
  pressure at the shoe-drum contact surface.
- *rp* is the pin location
  radius.
- *θp* is the hinge pin location
  angle.
- *ra* is the actuator location
  radius.

The model does not simulate self-locking brakes. If brake geometry and friction
parameters cause a self-locking condition, the model produces a simulation error. A
brake self-locks if the friction moment exceeds the moment due to normal forces,
that is, when *MF* >
*MN*.

The balance of moments for the trailing shoe is

F=MN+MFc.

The net braking torque is

T=TLS+TTS+μvisc\*ωshaft,

where *μvisc* is the viscous friction
coefficient.

### Faults

To model a fault in the Double-Shoe Brake block, in the
**Faults** section, click the **Add fault** hyperlink next
to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

When you trigger a fault, the block applies the value of the **Belt force
when faulted** parameter instead of the value at port **F**
for the remainder of the simulation. When the value is `0`, no
braking occurs. When the value is relatively large, the brake is stuck.

### Thermal Model

You can model the effects of heat flow and temperature change by exposing the optional thermal
port. To expose the port, in the **Friction** settings, set the
**Thermal Port** parameter to `Model`.
Exposing the port also exposes or changes the default value for these related settings,
parameters, and variables:

- **Friction** > **Temperature**
- **Friction** > **Static friction coefficient vector**
- **Friction** > **Coulomb friction coefficient vector**
- **Friction** > **Contact friction coefficient vector**
- **Thermal Port** > **Thermal mass**
- **Variables** > **Temperature**

### Limitations and Assumptions

- Contact angles smaller than 45° produce less accurate results.
- The brake uses the long-shoe approximation.
- The brake geometry does not self-lock.
- The model does not account for actuator flow consumption.
