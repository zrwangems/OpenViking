---
type: simulink-block
title: 'Variable Inertia'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Inertias & Loads'
documentation_page: 'variableinertia'
documentation_source_path: 'ref/variableinertia.html'
language: en
---

# Variable Inertia

## Ports

### Input

### **LConn 1** — Inertia, kg/m2 physical signal

Physical input signal associated with the inertia, in
kg/m2.
### Conserving

### **LConn 2** — Rotational connection mechanical rotational

Mechanical rotational conserving port.

## Parameters

### **Minimum inertia** — Minimum inertia `0.1` `kg*m^2` (default) | positive scalar

Lowest value that the variable inertia can take on during simulation. The
physical signal input saturates at this value. If the input falls below the
minimum inertia, it is set equal to the minimum inertia value.

## Libraries

Simscape / Driveline / Inertias & Loads

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Time-varying inertia specified as physical signal input

The Variable Inertia block represents the effect of a
time-varying inertia. Components with variable inertia include satellites unfolding
arrays of solar panels. A physical signal input port provides the instantaneous inertia
at each time step throughout simulation. To minimize solver errors, avoid
discontinuities and abrupt changes in the input signal.

As the component inertia changes, so does the inertial torque acting on that component:

TI=Iω˙,

where:

- *TI* is the inertial
  torque.
- *I* is the variable inertia.
- *ω* is the angular velocity of the inertia.

The physical signal input saturates at the minimum inertia specified in the block
property inspector. Whenever the input falls below the minimum inertia, the block
performs its calculations on the minimum inertia instead. The inertial torque becomes:

TI=IMinω˙,

where *IMin* is the minimum
inertia allowed.

The angular momentum of the variable inertia is conserved. In the absence of external
torques, a decrease in the moment of inertia leads to a proportional increase in angular
velocity. The angular momentum remains constant until a net external torque causes it to
change.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
