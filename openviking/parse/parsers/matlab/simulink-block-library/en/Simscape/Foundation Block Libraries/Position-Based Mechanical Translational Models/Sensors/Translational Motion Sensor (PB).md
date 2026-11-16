---
type: simulink-block
title: 'Translational Motion Sensor (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Sensors'
documentation_page: 'translationalmotionsensorpb'
documentation_source_path: 'ref/translationalmotionsensorpb.html'
language: en
---

# Translational Motion Sensor (PB)

## Ports

### Output

### **A** — Acceleration, m/s^2 physical signal

Physical signal output port for acceleration.

#### Dependencies

To enable this port, select the **Acceleration** check
box.

### **V** — Velocity, m/s physical signal

Physical signal output port for velocity.

#### Dependencies

To enable this port, select the **Velocity** check box.

### **P** — Position, m physical signal

Physical signal output port for position.

#### Dependencies

To enable this port, select the **Position** check box.
### Conserving

### **B** — Base port position-based mechanical translational

Position-based mechanical translational conserving port that represents the base
connection.

### **F** — Follower port position-based mechanical translational

Position-based mechanical translational conserving port that represents the
follower connection.

#### Dependencies

To enable this port, set the **Measurement reference**
parameter to `Difference`.

## Parameters

### **Measurement reference** — Select whether to perform absolute or relative measurements `Difference` (default) | `Absolute`

Select whether to perform absolute or relative measurements:

- `Difference` — Measure the acceleration, velocity, and
  position of port **F** relative to port
  **B**.
- `Absolute` — Disable port **B** and
  measure the acceleration, velocity, and position of port **F** with
  respect to the world frame.

### **Acceleration** — Control output port visibility to measure acceleration off (default) | on

Selecting this check box exposes output port **A**, which lets you
measure acceleration. Exposing port **A** also involves additional
computations, to measure acceleration based on velocity, therefore this port is off by
default.

### **Velocity** — Control output port visibility to measure velocity on (default) | off

Selecting this check box exposes output port **V**, which lets you
measure velocity.

### **Position** — Control output port visibility to measure position on (default) | off

Selecting this check box exposes output port **P**, which lets you
measure position.

## Libraries

Simscape / Foundation Library / Translational / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Motion sensor in position-based mechanical translational systems

The Translational Motion Sensor (PB) block measures
absolute or relative position, velocity, and acceleration in a position-based translational
network. The measurement is positive when the motion at port **F** is greater
than at port **B**. The sensor does not apply force to the network.

Connections **B** and **F** are position-based
mechanical translational conserving ports.

Connections **A**, **V**, and **P** are
physical signal output ports for acceleration, velocity, and position, respectively. The
visibility of these ports is controlled by block parameters. If you enable port
**A**, the block performs additional computations, to measure acceleration
based on velocity. To avoid unnecessary model complexity, it is recommended that in each
instance of the block you enable only the ports that you actually use for measurement.
