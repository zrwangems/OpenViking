---
type: simulink-block
title: 'Ideal Rotational Motion Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sensors'
documentation_page: 'idealrotationalmotionsensor'
documentation_source_path: 'ref/idealrotationalmotionsensor.html'
language: en
---

# Ideal Rotational Motion Sensor

## Ports

### Output

### **α** — Acceleration, rad/s^2 physical signal

Physical signal output port for angular acceleration.

#### Dependencies

To enable this port, select the **Acceleration**
check box.

### **W** — Angular velocity, rad/s physical signal

Physical signal output port for angular velocity.

#### Dependencies

To enable this port, select the **Velocity**
check box.

### **A** — Position (angular displacement), rad physical signal

Physical signal output port for angular displacement.

#### Dependencies

To enable this port, select the **Position**
check box.
### Conserving

### **R** — Rod (positive probe) mechanical rotational

Mechanical rotational conserving port associated with the sensor
positive probe.

### **C** — Case (reference probe) mechanical rotational

Mechanical rotational conserving port associated with the sensor
negative (reference) probe.

#### Dependencies

To enable this port, set the **Measurement
reference** parameter to
`Difference`.

## Parameters

### **Measurement reference** — Select whether to perform absolute or relative measurements `Difference` (default) | `Absolute`

Select whether to perform absolute or relative measurements:

- `Difference` — Measure the acceleration,
  velocity, and position of port **R** relative to
  port **C**.
- `Absolute` — Disable port
  **C** and measure the acceleration, velocity,
  and position of port **R** with respect to ground
  (internal reference node).

### **Acceleration** — Control output port visibility to measure angular acceleration off (default) | on

Selecting this check box exposes output port **α**, which
lets you measure angular acceleration. Exposing port **α**
also involves additional computations, to measure acceleration based on
velocity, therefore this port is off by default.

### **Velocity** — Control output port visibility to measure angular velocity on (default) | off

Selecting this check box exposes output port **W**, which
lets you measure angular velocity.

### **Position** — Control output port visibility to measure angular displacement on (default) | off

Selecting this check box exposes output port **A**, which
lets you measure position (angular displacement).

### **Wrap angle to [0, 2\*pi]** — Control output range for angular displacement off (default) | on

When set to `On`, keeps angular displacement
output by the sensor within the range from 0 to 2π radians (360 degrees),
regardless of the number of revolutions performed by the object and the
direction of rotation. When set to `Off`, the
output range is unrestricted.

Selecting this check box simplifies development of models with complex
relationship between model parameters and rotation angle, such as pumps and
motors.

#### Dependencies

To enable this parameter, select the **Position**
check box.

### **Initial angle** — Sensor initial offset `0 rad` (default)

Sensor initial angular position (offset).

#### Dependencies

To enable this parameter, select the **Position**
check box.

## Libraries

Simscape / Foundation Library / Mechanical / Mechanical Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2022b: Measure acceleration, measure with respect to ground, and parametrically control visibility of output ports

The block enhancements include:

- An additional physical signal output port, **α**, that
  lets you measure angular acceleration.
- Additional parameters (**Acceleration**,
  **Velocity**, and **Position**) that
  control the visibility of physical signal output ports, letting you expose
  only the ports that are actually used for measurement in each particular
  instance. This enhancement helps improve the block diagram readability.
  Also, because exposing the acceleration measurement port involves additional
  computations, this port is hidden by default and it is recommended that you
  do not expose it unless you need to measure acceleration.
- In previous releases, the blocks measured only relative velocity and
  position of port **R** with respect to port
  **C**. Now, the new **Measurement
  reference** parameter lets you disable port
  **C** and measure with respect to ground (internal
  reference node).

These enhancements have no compatibility impact on models created in previous
releases.

## Description

Motion sensor in mechanical rotational systems

The Ideal Rotational Motion Sensor block represents an
ideal mechanical rotational motion sensor, that is, a device that converts an across
variable measured between two mechanical rotational nodes into a control signal
proportional to acceleration, angular velocity, or position (angle). You can specify the
initial angular position (offset) as a block parameter.

The sensor is ideal since it does not account for inertia, friction, delays, energy
consumption, and so on.

Connections **R** and **C** are mechanical
rotational conserving ports that connect the block to the nodes where motion is being
monitored. The block positive direction is from port R to port C. This means that the
velocity is measured as *ω* =
*ω*R –
*ω*C, where
*ω*R,
*ω*C are the absolute angular velocities at
ports **R** and **C**, respectively. The
**Measurement reference** parameter lets you disable port
**C** and measure with respect to ground.

Connections **α**, **W**, and **A**
are physical signal output ports for angular acceleration, velocity, and displacement,
respectively. The visibility of these ports is controlled by block parameters. If you
enable port **α**, the block performs additional computations, to
measure acceleration based on velocity. To avoid unnecessary model complexity, it is
recommended that in each instance of the block you enable only the ports that you
actually use for measurement.

The **Wrap angle to [0, 2\*pi]** check box lets you control the
angular displacement output range. When selected, it keeps angular displacement within
the range from 0 to 2π radians (360 degrees), regardless of the number of revolutions
performed by the object and the direction of rotation. When this check box is cleared,
the output range is unrestricted.

The figure demonstrates the difference between the two options.

Two plots output by the sensor.

In this example, the object is moving at 6 rad/s in the positive direction for the
first 5 seconds, and then switches to the negative direction at the same speed. The
default angular displacement output (line 1) shows that the object turned forward by 30
rad and then turned back in the negative direction, continuing until –20 rad. If you
select the **Wrap angle to [0, 2\*pi]** check box, the output (line 2)
stays in the range from 0 to 2π rad.

Selecting the **Wrap angle to [0, 2\*pi]** check box simplifies
development of models with complex relationship between model parameters and rotation
angle, such as pumps and motors.
