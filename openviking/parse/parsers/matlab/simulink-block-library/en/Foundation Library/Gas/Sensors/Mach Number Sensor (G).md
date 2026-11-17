---
type: simulink-block
title: 'Mach Number Sensor (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Sensors'
documentation_page: 'machnumbersensorg'
documentation_source_path: 'ref/machnumbersensorg.html'
language: en
---

# Mach Number Sensor (G)

## Ports
```yaml
ports:
- name: Mach
  summary: Mach number measurement, unitless physical signal
  direction: output
- name: A
  summary: Sensor inlet gas
  direction: conserving
- name: B
  summary: Sensor outlet gas
  direction: conserving
```

### Output

### **Mach** — Mach number measurement, unitless physical signal

Physical signal output port for the Mach number measurement, unitless.
### Conserving

### **A** — Sensor inlet gas

Gas conserving port associated with the sensor inlet. The positive flow direction
is from port **A** to port **B**.

### **B** — Sensor outlet gas

Gas conserving port associated with the sensor outlet. The positive flow direction
is from port **A** to port **B**.
## Parameters
```yaml
parameters:
- name: Area of flow path
  summary: Flow path area 0.01 m^2 (default) | positive scalar
  group: ''
```

### **Area of flow path** — Flow path area `0.01 m^2` (default) | positive scalar

Cross-sectional area of the flow path.
## Libraries

Simscape / Foundation Library / Gas / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Measure Mach number of internal gas flow

The Mach Number Sensor (G) block represents an ideal sensor
that measures the Mach number of gas flow. The Mach number signifies the ratio of the flow
velocity to the local speed of sound, and quantifies the compressibility effects of the gas in
the line. The block calculates the Mach number such that

M=m˙ρ⋅a⋅A,

where:

- *ṁ* is the mass flow rate.
- *ρ* is the density.
- *a* is the local speed of sound.
- *A* is the cross-sectional area of the flow path, which you specify
  with the **Area of flow path** parameter.

These values depend on the setting of the Gas Properties
(G) block. When you align flow from port **A** to **B**,
the block outputs the Mach number of the flow at port **Mach**. The block saturates
the Mach number at 1. Using this block does not affect the flow.
