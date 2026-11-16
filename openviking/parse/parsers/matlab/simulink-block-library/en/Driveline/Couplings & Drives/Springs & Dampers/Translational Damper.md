---
type: simulink-block
title: 'Translational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'translationaldamper'
documentation_source_path: 'ref/translationaldamper.html'
language: en
---

# Translational Damper

## Ports

### Conserving

### **R** — Rod interface mechanical translational

Mechanical translational conserving port associated with the
rod interface.

### **C** — Case interface mechanical translational

Mechanical translational conserving port associated with the
case interface.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow. Heat flow affects
damper temperature, and therefore, power transmission efficiency.

#### Dependencies

To enable this port, set **Thermal port** to
`Model`.

## Parameters

#### Main

### **Damping coefficient** — Damping coefficient `100` `N/(m/s)` (default) | nonnegative scalar

Damping coefficient due to viscous friction.

#### Faults

### **Damping fault** — Fault option `Add fault`

Whether to model a fault in the block. To add a fault, click the
**Add fault** hyperlink.

### **Faulted damping coefficient** — Faulted damping coefficient `1e6` `N*s/m` (default)

Damping coefficient when a fault is triggered.

#### Dependencies

To enable this parameter, first enable faults for the block by
clicking the **Add fault** hyperlink.

#### Thermal port

### **Thermal port** — Thermal modelling `Omit` (default) | `Model`

Option to model effects of heat flow and temperature change.

### **Thermal mass** — Thermal mass `50` `kJ/K` (default) | positive scalar

Thermal energy required to change the component temperature by a unit
increase. The thermal mass represents the ability of the damper to absorb
and retain heat energy.

## Libraries

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2024a: Model faults with the Simscape faults interface

The Translational Damper block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

## Description

Linear translational damper

The Translational Damper block models a linear translational viscous
damper. From the start of the simulation, the block uses the nominal damping
coefficient. If you enable faults for the block, the damping coefficient changes in
response to one or both of these triggers:

- Simulation time — A fault occurs at a specified time.
- Simulation behavior — If the magnitude of the translational
  acceleration exceeds a specified maximum value, the block increments the
  number of shocks by one. A fault occurs if the number of shocks exceeds a
  specified maximum number of shocks.

The defining equations are

F=Dv

and

v=vR−vC,

where

- *F* is the force transmitted through the damper.
- *D* is the damping (viscous friction) coefficient.
- *v* is the relative velocity.
- *vR* and
  *vC* are the absolute
  velocities of terminals **R** and **C**,
  respectively.

The positive block direction is from port **R** to port **C**.
Therefore, the torque is positive if it acts in the direction from **R** to
**C**.

### Faults

To model a fault in the Translational Damper block, in the
**Faults** section, click the **Add fault** hyperlink next
to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

When you trigger a fault, the block applies the value of the **Faulted
damping coefficient** parameter for the remainder of the
simulation.

### Thermal Modelling

You can model the effects of heat flow and temperature change by enabling the
optional thermal port. To enable the port, set **Thermal port** to
`Model`.

Enabling thermal modelling exposes the **Thermal mass**
parameter.
