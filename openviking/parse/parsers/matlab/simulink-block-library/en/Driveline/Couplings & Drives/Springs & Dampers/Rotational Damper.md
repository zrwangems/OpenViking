---
type: simulink-block
title: 'Rotational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'rotationaldamper'
documentation_source_path: 'ref/rotationaldamper.html'
language: en
---

# Rotational Damper

## Ports
```yaml
ports:
- name: R
  summary: Rod interface mechanical rotational
  direction: conserving
- name: C
  summary: Case interface mechanical rotational
  direction: conserving
- name: H
  summary: Heat flow thermal
  direction: conserving
```

### Conserving

### **R** — Rod interface mechanical rotational

Mechanical rotational conserving port associated with the rod
interface.

### **C** — Case interface mechanical rotational

Mechanical rotational conserving port associated with the case
interface.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow. Heat flow affects
damper temperature, and therefore, power transmission efficiency.

#### Dependencies

To enable this port, set **Thermal port** to
`Model`.
## Parameters
```yaml
parameters:
- name: Damping coefficient
  summary: Damping coefficient 1e-3 N*m/(rad/s) (default) | positive scalar
  group: Main
- name: Damping fault
  summary: Option to model damping fault Add fault
  group: Faults
- name: Faulted damping coefficient
  summary: Damping coefficient when faulted 100 N*m*s/rad (default) | positive scalar
  group: Faults
- name: Thermal port
  summary: Thermal modelling Omit (default) | Model
  group: Thermal port
- name: Thermal mass
  summary: Thermal mass 50 kJ/K (default) | positive scalar
  group: Thermal port
```

### Main

### **Damping coefficient** — Damping coefficient `1e-3` `N*m/(rad/s)` (default) | positive scalar

The oscillation-reducing torque due to viscous friction that the block
applies if no trigger event occurs. Specify a value that is greater than
or equal to zero.

### Faults

To modify the faults, create a fault and, in the block dialog, click
**Open fault properties**. In the Property Inspector, click the
**Fault behavior** link to open the faults.

### **Damping fault** — Option to model damping fault `Add fault`

Whether to model a fault in the block. To add a fault, click the
**Add fault** hyperlink.

### **Faulted damping coefficient** — Damping coefficient when faulted `100` `N*m*s/rad` (default) | positive scalar

Damping coefficient once a fault trigger occurs.

#### Dependencies

To enable this parameter, enable faults for the block by clicking
the **Add fault** hyperlink.

### Thermal port

### **Thermal port** — Thermal modelling `Omit` (default) | `Model`

Option to model effects of heat flow and temperature change.

### **Thermal mass** — Thermal mass `50` `kJ/K` (default) | positive scalar

Thermal energy required to change the component temperature by a unit
increase. The thermal mass represents the ability of the damper to
absorb and retain heat energy.
## Libraries

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2024a: Model faults with the Simscape faults interface

The Rotational Damper block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

## Description

Linear rotational damper

The Rotational Damper block represents a linear
rotational viscous damper. The block calculates the torque transmitted by the damper
such that

T=Dω

and

ω=ωR−ωC,

where

- *T* is the torque transmitted through the damper.
- *D* is the damping (viscous friction) coefficient.
- *ω* is the relative velocity.
- *ωR* and
  *ωC* are the absolute
  velocities of ports **R** and **C**, respectively.

The positive block direction is from port **R** to port **C**.
Therefore, the torque is positive if it acts in the direction from **R** to
**C**.

### Faults

To model a fault in the Rotational Damper block, in the
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

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
