---
type: simulink-block
title: 'Ideal Translational Motion Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sensors'
documentation_page: 'idealtranslationalmotionsensor'
documentation_source_path: 'ref/idealtranslationalmotionsensor.html'
language: en
---

# Ideal Translational Motion Sensor

## Ports

### Output

### **A** — Acceleration, m/s^2 physical signal

Physical signal output port for acceleration.

#### Dependencies

To enable this port, select the **Acceleration**
check box.

### **V** — Velocity, m/s physical signal

Physical signal output port for velocity.

#### Dependencies

To enable this port, select the **Velocity**
check box.

### **P** — Position, m physical signal

Physical signal output port for position.

#### Dependencies

To enable this port, select the **Position**
check box.
### Conserving

### **R** — Rod (positive probe) mechanical translational

Mechanical translational conserving port associated with the sensor
positive probe.

### **C** — Case (reference probe) mechanical translational

Mechanical translational conserving port associated with the sensor
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

### **Acceleration** — Control output port visibility to measure acceleration off (default) | on

Selecting this check box exposes output port **A**, which
lets you measure acceleration. Exposing port **A** also
involves additional computations, to measure acceleration based on velocity,
therefore this port is off by default.

### **Velocity** — Control output port visibility to measure velocity on (default) | off

Selecting this check box exposes output port **V**, which
lets you measure velocity.

### **Position** — Control output port visibility to measure position on (default) | off

Selecting this check box exposes output port **P**, which
lets you measure position.

### **Initial position** — Sensor initial offset `0 m` (default)

Sensor initial position (offset).

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

- An additional physical signal output port, **A**, that
  lets you measure acceleration.
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

Motion sensor in mechanical translational systems

The Ideal Translational Motion Sensor block represents
a device that converts an across variable measured between two mechanical translational
nodes into a control signal proportional to acceleration, velocity, or position. You can
specify the initial position (offset) as a block parameter.

The sensor is ideal since it does not account for inertia, friction, delays, energy
consumption, and so on.

Connections **R** and **C** are mechanical
translational conserving ports that connect the block to the nodes where motion is being
monitored. The block positive direction is from port R to port C. This means that the
velocity is measured as *v* =
*v*R –
*v*C, where
*v*R,
*v*C are the absolute velocities at ports
**R** and **C**, respectively. The
**Measurement reference** parameter lets you disable port
**C** and measure with respect to ground.

Connections **A**, **V**, and **P**
are physical signal output ports for acceleration, velocity, and position, respectively.
The visibility of these ports is controlled by block parameters. If you enable port
**A**, the block performs additional computations, to measure
acceleration based on velocity. To avoid unnecessary model complexity, it is recommended
that in each instance of the block you enable only the ports that you actually use for
measurement.
