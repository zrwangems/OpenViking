---
type: simulink-block
title: 'Ideal Torque Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sensors'
documentation_page: 'idealtorquesensor'
documentation_source_path: 'ref/idealtorquesensor.html'
language: en
---

# Ideal Torque Sensor

## Ports
```yaml
ports:
- name: T
  summary: Torque, N\*m physical signal
  direction: output
- name: R
  summary: Rod (positive probe) mechanical rotational
  direction: conserving
- name: C
  summary: Case (reference probe) mechanical rotational
  direction: conserving
```

### Output

### **T** — Torque, N\*m physical signal

Physical signal output port for torque.
### Conserving

### **R** — Rod (positive probe) mechanical rotational

Mechanical rotational conserving port associated with the sensor
positive probe.

### **C** — Case (reference probe) mechanical rotational

Mechanical rotational conserving port associated with the sensor
negative (reference) probe.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Mechanical / Mechanical Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Torque sensor in mechanical rotational systems

The Ideal Torque Sensor block represents a device that
converts a variable passing through the sensor into a control signal proportional to the
torque. The sensor is ideal because it does not account for inertia, friction, delays,
energy consumption, and so on.

Connections **R** and **C** are mechanical
rotational conserving ports. Connect this sensor in series with the block where you want
to measure the torque because torque is a Through variable (for the mechanical
rotational domain). The sensor constrains ports **R** and
**C** to allow no motion between them, therefore connecting the
sensor in parallel may affect the simulation results because it is analogous to adding a
bypass connection line between the connection points. A series connection within an
existing line does not affect the simulation results and provides an accurate
measurement.

Connection **T** is a physical signal port that outputs the
measurement result. The block positive direction is from port **R** to
port **C**. This means that positive torque applied to port
**R** (the sensor positive probe) generates a positive output
signal.
