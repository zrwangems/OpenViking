---
type: simulink-block
title: 'Wheel and Axle'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Mechanisms'
documentation_page: 'wheelandaxle'
documentation_source_path: 'ref/wheelandaxle.html'
language: en
---

# Wheel and Axle

## Ports

### Conserving

### **A** — Axle mechanical rotational

Mechanical rotational conserving port associated with the axle.

### **P** — Wheel periphery mechanical translational

Mechanical translational conserving port associated with the wheel
periphery.

## Parameters

### **Wheel radius** — Radius of the wheel `0.05 m` (default)

Radius of the wheel.

### **Mechanism orientation** — Relationship between axle rotation and direction of translational motion `Drives in positive direction` (default) | `Drives in negative direction`

The value `Drives in positive direction`
specifies a mechanism where axle rotation in the globally assigned positive
direction is converted into translational motion in positive direction. The
value `Drives in negative direction` specifies a
mechanism where axle rotation in the globally assigned positive direction is
converted into translational motion in negative direction.

## Libraries

Simscape / Foundation Library / Mechanical / Mechanisms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Wheel and axle mechanism in mechanical systems

The Wheel and Axle block represents a wheel and axle mechanism shown in
the following schematic.

The wheel and the axle have the same axis, and the axis is assumed to be rigidly
connected to the frame, thus making this mechanism an ideal converter of mechanical
rotational into mechanical translational motion. The mechanism has two connections: a
mechanical rotational port A, which corresponds to the axle, and a mechanical
translational port P, which corresponds to the wheel periphery. The mechanism is
described with the following equations:

T=r·F·or

v=r·ω·or

where

- *T* is torque on the axle.
- *F* is force on the wheel periphery.
- *ω* is angular velocity.
- *v* is linear velocity on the wheel periphery.
- *r* is wheel radius.
- *or* is mechanism orientation indicator. The value is +1 if
  axle rotation in the globally assigned positive direction is converted into
  translational motion in positive direction. The value is –1 if positive rotation
  results in translational motion in negative direction.

Use the block in simulation of rack-pinions, steering wheels, hoisting devices,
windlasses, and so on.

The block positive directions are from A to the reference point and from the reference
point to P.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
