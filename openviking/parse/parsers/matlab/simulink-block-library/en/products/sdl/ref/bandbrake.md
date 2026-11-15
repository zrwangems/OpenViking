---
type: simulink-block
title: 'Band Brake'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Brakes and Detents'
documentation_page: 'bandbrake'
documentation_source_path: 'ref/bandbrake.html'
language: en
---

# Band Brake

## Ports

### Input

### **F** — Belt tensioning force physical signal

Physical signal inport associated with the external tensioning force
that is applied to the belt.
### Conserving

### **S** — Drum shaft rotation rotational mechanical

Rotational conserving port associated with the rotating drum
shaft.

### **H** — Heat flow, in W thermal

Thermal conserving port associated with heat flow.

#### Dependencies

This port is visible only when, in the
**Friction** settings, the **Thermal
Port** parameter is set to
`Model`.

Exposing this port makes related settings visible.

## Parameters

### Geometry

### **Drum radius** — Contact surface radius `150` `mm` (default) | positive scalar

Radius of the drum contact surface. The parameter must be greater than
zero.

### **Wrap angle** — Contact angle `270` `deg` (default) | positive scalar

Contact angle between the flexible belt and the rotating drum. The
parameter must be greater than zero.

### Friction

### **Viscous friction coefficient** — Viscous friction `.01` `n*m/(rad/s)` (default) | nonegative scalar

Viscous friction coefficient at the belt-drum contact surface. The
parameter must be greater than or equal to zero.

### **Thermal port** — Thermal model `Omit` (default) | `Model`

Model for heat flow and temperature change:

- `Omit` — Neglect thermal
  dynamics.
- `Model` — Include thermal
  dynamics.

#### Dependencies

When this parameter is set to `Model`,
the thermal port and related parameters and variables are
visible.

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | increasing vector

Array of temperatures used to construct a 1-D temperature-efficiency
lookup table. The array values must increase left to right.

#### Dependencies

This parameter is only visible when the **Thermal
Port** parameter is set to
`Model`.

### **Contact friction coefficient** — Coulomb friction `0.3` (default) | positive scalar

Coulomb friction coefficient at the belt-drum contact surface. The
value must be greater than zero.

#### Dependencies

This parameter is only visible when the **Thermal
Port** parameter is set to
`Omit`.

### **Contact friction coefficient vector** — Coulomb friction `[.1, .05, .03]` (default) | increasing vector of positive values

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

### **Angular velocity threshold** — Rotational velocity required for near steady-state contact friction `0.01` `rad/s` (default) | positive scalar

Angular velocity at which the contact friction coefficient practically
reaches its steady-state value. The value must be greater than
zero.

### Faults

To modify the faults, create a fault and, in the block dialog, click
**Open fault properties**. In the Property Inspector, click the
**Fault behavior** link to open the faults.

### **Belt tension fault** — Option to model a belt tension failure `Add fault`

Whether to model a belt tension fault in the block. The fault replaces
the value at port **F** with the value of the **Belt
tension when faulted** parameter. To add a fault, click the
**Add fault** hyperlink.

### **Belt tension when faulted** — Faulted belt tension `0` `N` (default) | positive scalar

Belt tension when a fault is triggered. When you trigger a fault, the
block applies the value of the **Belt tension when
faulted** parameter instead of the value at port
**F** for the remainder of the simulation. When the value
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

The Band Brake block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

## Description

Frictional brake with flexible band wrapped around rotating drum

The Band Brake block represents a frictional brake with
a flexible band that wraps around the periphery of a rotating drum to produce a braking
action. A positive actuating force causes the band to tighten around the rotating drum
and it places the friction surfaces in contact. Viscous and contact friction between the
surfaces of the drum and the flexible band causes the rotating drum to
decelerate.

You can model the effects of heat flow and temperature change for the block by using
port **H**, an optional thermal conserving port.

Band brakes provide high braking torque at the cost of reduced braking precision in
applications that include winch drums, chainsaws, go-karts, and mini-bikes.

### Equations

The block uses a simple parameterization with simple brake geometry and friction
parameters.

The braking torque as a function of the external brake actuation force that
tightens the belt is

T=(FTB−FA)⋅rD+μvisc⋅ω

Where:

- *T* is the braking torque.
- *FTB* is the tension force
  acting on the tense branch of the band.
- *FA* is the external brake
  actuation force.
- *rD* is the drum
  radius.
- *μvisc* is the viscous
  friction coefficient.
- *μ* is the contact friction coefficient.
- *ϕ* is the wrap angle.

Forces *FTB* and
*FA* satisfy the relationship

FTBFA=eμϕ

Replacing the relationship in the braking torque formula eliminates force
*FTB* such that

T=FA(eμϕ−1)⋅rD+μvisc⋅ω

To avoid discontinuity at zero relative velocity, the model defines the actuation
force, *FS*, as a hyperbolic function

FA=Fin⋅tanh(4ωωthreshold)

Where:

- *Fin* is the force input
  signal.
- *ωthreshold* is the angular
  velocity threshold.

### Faults

To model a fault in the Band Brake block, in the
**Faults** section, click the **Add fault** hyperlink next
to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

When you trigger a fault, the block applies the value of the **Belt force
when faulted** parameter instead of the value at port **F**
for the remainder of the simulation. When the value is `0`, no
braking occurs. When the value is relatively large, the brake is stuck.

### Thermal Model

You can model the effects of heat flow and temperature change by exposing the
optional thermal port. To expose the port, in the **Friction**
settings, set the **Thermal Port** parameter to
`Model`.

### Limitations and Assumptions

The model does not account for actuator flow consumption.
