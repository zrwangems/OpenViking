---
type: simulink-block
title: 'Force Sensor (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Sensors'
documentation_page: 'forcesensorpb'
documentation_source_path: 'ref/forcesensorpb.html'
language: en
---

# Force Sensor (PB)

## Ports

### Output

### **f** — Force, N physical signal

Physical signal output port for force.
### Conserving

### **B** — Base port position-based mechanical translational

Position-based mechanical translational conserving port that represents the base
connection.

### **F** — Follower port position-based mechanical translational

Position-based mechanical translational conserving port that represents the
follower connection.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Translational / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Force sensor in position-based mechanical translational systems

The Force Sensor (PB) block measures force in a
position-based translational network. The sensor represents a rigid load cell. There is no
position or velocity change across the sensor. The length of the sensor is 0 m.

Connections **B** and **F** are position-based
mechanical translational conserving ports. The physical signal port **f**
outputs the force applied in the direction from port **B** to port
**F**.

Connect this sensor in series with the block where you want to measure the force, because
force is a Through variable. For more information, see Through and Across Variables.

The Force Sensor (PB) block positive direction is from port
**B** to port **F**. When you align the sensor positive
direction with the network positive direction, then:

- A positive output signal indicates that the measured point in the network is in a
  state of compression.
- A negative output signal indicates that the measured point in the network is in a
  state of tension.

Alternatively, if the sensor positive direction is opposite of the network positive
direction, then a positive output signal indicates that the network is in a state of tension
and a negative output signal indicates that the network is in a state of compression.
