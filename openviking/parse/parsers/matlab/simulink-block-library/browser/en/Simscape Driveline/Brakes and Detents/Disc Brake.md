---
type: simulink-block
title: 'Disc Brake'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Brakes and Detents'
documentation_page: 'discbrake'
documentation_source_path: 'ref/discbrake.html'
language: en
---

# Disc Brake

## Ports

### Input

### **P** — Cylinder pressure physical signal

Physical signal port associated with cylinder pressure, in
bars.
### Conserving

### **S** — Shaft rotational mechanical

Rotational mechanical conserving port associated with the
shaft.

### **H** — Heat thermal

Thermal conserving port associated with heat flow.

#### Dependencies

This port is visible only when, in the
**Friction** settings, the **Thermal
Port** parameter is set to
`Model`.

Exposing this port makes related parameters and variables
visible.

## Parameters

### Geometry

### **Mean pad radius** — Pad radius `150` `mm` (default) | positive scalar

Mean radius of the friction pads.

### **Cylinder bore** — Bore diameter `10` `mm` (default) | positive scalar

Diameter of the piston.

### **Number of brake pads** — Pad quantity `2` (default) | positive scalar integer

Number of friction pads.

### Friction

### **Thermal port** — Thermal model `Omit` (default) | `Model`

Model for heat flow and temperature change:

- `Omit` — Neglect thermal
  dynamics.
- `Model` — Include thermal
  dynamics.

#### Dependencies

When this parameter is set to `Model`,
the thermal port and related parameter and variables are
visible.

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | increasing vector

Array of temperatures used to construct a 1-D temperature-efficiency
lookup table. The array values must increase left to right.

#### Dependencies

This parameter is only visible when the **Thermal
Port** parameter is set to
`Model`.

### **Static friction coefficient** — Static friction `0.9` (default) | scalar

Coefficient of static friction. The value that you specify for this
parameter must be greater than the value that you specify for the
**Coulomb friction coefficient** parameter.

#### Dependencies

This parameter is only visible when the **Thermal
Port** parameter is set to
`Omit`.

### **Static friction coefficient vector** — Static friction `[.9, .8, .7]` | vector

Coefficient of static friction, such that:

- The number of elements in the vector must be the same as
  the number of elements in the specified vector for the
  **Temperature** parameter
- The values must be greater than the corresponding value
  that you specify for the **Coulomb friction
  coefficient vector** parameter.

#### Dependencies

This parameter is only visible when the **Thermal
Port** parameter is set to
`Model`.

### **Coulomb friction coefficient** — Contact friction `0.7` (default) | positive scalar

Coulomb friction coefficient at the belt-drum contact surface. The
value must be greater than zero.

#### Dependencies

This parameter is only visible when the **Thermal
Port** parameter is set to
`Omit`.

### **Coulomb friction coefficient vector** — Contact friction `[.8, .7, .6]` (default) | increasing vector of positive values

Coulomb friction coefficient at the belt-drum contact surface, such that:

- The number of elements in the vector must be the same as
  the number of elements in the specified vector for the
  **Temperature** parameter
- The values increase left to right.
- Each value must be greater than zero.

#### Dependencies

This parameter is only visible when the **Thermal
Port** parameter is set to
`Model`.

### **Breakaway friction velocity** — Friction threshold `0.1` `rad/s` (default) | scalar

Angular speed at which friction switches from static to
kinetic.

### **Viscous friction coefficient** — Viscous friction `0` `N*m/(rad/s)` (default) | nonnegative scalar

For a wet brake, the viscous friction represents the energy loss to
the cooling/lubricating fluid between the clutch plates. To model a wet
brake, specify a nonzero value for the coefficient of viscous friction.
The default value represents a dry brake.

### Faults

To modify the faults, create a fault and, in the block dialog, click
**Open fault properties**. In the Property Inspector, click the
**Fault behavior** link to open the faults.

### **Brake pressure fault** — Option to model brake pressure fault `Add fault`

Whether to model a fault in the block. To add a fault, click the
**Add fault** hyperlink.

### **Brake pressure when faulted** — Set faulted brake pressure `0` `bar` (default) | positive scalar

Belt force when a fault is triggered. When you trigger a fault, the
block applies the value of the **Brake pressure when
faulted** parameter instead of the value at port
**P** for the remainder of the simulation. When the value
is `0`, no braking occurs. When the value is relatively
large, the brake is stuck.

#### Dependencies

To enable this parameter, enable faults for the block by clicking
the **Add fault** hyperlink.

### Thermal Port

### **Thermal mass** — Resistance to temperature change `50` `kJ/K` (default) | scalar

Thermal energy required to change the component temperature by a
single degree. The greater the thermal mass, the more resistant the
component is to temperature change.

#### Dependencies

This parameter is only visible when in the
**Friction** settings, the **Thermal
Port** parameter is set to
`Model`.

## Libraries

Simscape / Driveline / Brakes & Detents / Rotational

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2024a: Model faults with the Simscape faults interface

The Disc Brake block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

## Description

Frictional brake with pressure-applying cylinder and pads

The Disc Brake block represents a brake arranged as a cylinder applying
pressure to one or more pads that can contact the shaft rotor. Pressure from the
cylinder causes the pads to exert friction torque on the shaft. The friction torque
resists shaft rotation.

### Disc Brake Model

This figure shows the side and front views of a disc brake.

A disc brake converts brake cylinder pressure from the brake cylinder into force.
The disc brake applies the force at the brake pad mean radius.

The equation that the block uses to calculate brake torque, depends on the wheel
speed, *Ω*, such that when Ω≠0,

T=μkPπDb2RmN4.

However when Ω=0, the torque applied by the brake is equal to the torque that is
applied externally for wheel rotation. The maximum value of the torque that the
brake can apply when Ω=0, is

T=μsPπDb2RmN4.

In both cases, Rm=Ro+Ri2.

Where:

- *T* is the brake torque.
- *P* is the applied brake pressure.
- *Ω* is the wheel speed.
- *N* is the number of brake pads in disc brake
  assembly.
- *μs* is the disc pad-rotor
  coefficient of static friction.
- *μk* is the disc pad-rotor
  coefficient of kinetic friction.
- *Db* is the brake actuator
  bore diameter.
- *Rm* is the mean radius of
  brake pad force application on brake rotor.
- *Ro* is the outer radius of
  brake pad.
- *Ri* is the inner radius of
  brake pad.

The block default models a dry brake. You can model fluid friction in
a wet brake by setting the **Viscous friction coefficient**,
*k*v, to a nonzero value. The torque on
the wheel in a wet brake system is:

Twet=T+kvΩ.

### Faults

To model a fault in the Disc Brake block, in the
**Faults** section, click the **Add fault** hyperlink next
to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

When you trigger a fault, the block applies the value of the **Brake
pressure when faulted** parameter instead of the value at port
**P** for the remainder of the simulation. When the value is
`0`, no braking occurs. When the value is relatively large, the
brake is stuck.

### Thermal Model

You can model the effects of heat flow and temperature change by exposing the
optional thermal port. To expose the port, in the **Friction**
settings, set the **Thermal Port** parameter to
`Model`. Exposing the port also exposes or changes the
default value for these related settings, parameters, and variables:

- **Friction** > **Temperature**
- **Friction** > **Static friction coefficient vector**
- **Friction** > **Coulomb friction coefficient vector**
- **Thermal Port** > **Thermal mass**
- **Variables** > **Temperature**
