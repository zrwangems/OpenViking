---
type: simulink-block
title: 'Temperature Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sensors'
documentation_page: 'temperaturesensor'
documentation_source_path: 'ref/temperaturesensor.html'
language: en
---

# Temperature Sensor

## Ports
```yaml
ports:
- name: T
  summary: Temperature measurement, K physical signal
  direction: output
- name: A
  summary: Sensor inlet thermal
  direction: conserving
- name: B
  summary: Sensor outlet thermal
  direction: conserving
```

### Output

### **T** — Temperature measurement, K physical signal

Physical signal output port for temperature measurement.
### Conserving

### **A** — Sensor inlet thermal

Thermal conserving port.

### **B** — Sensor outlet thermal

Thermal conserving port. The measurement is positive when the value at port
**A** is greater than the value at port
**B**.

#### Dependencies

To enable this port, set the **Measurement reference**
parameter to `Difference`.
## Parameters
```yaml
parameters:
- name: Measurement reference
  summary: Select between absolute and relative measurements Difference (default) | Absolute
  group: ''
```

### **Measurement reference** — Select between absolute and relative measurements `Difference` (default) | `Absolute`

Select between absolute and relative measurements:

- `Difference` — The sensor measures the
  temperature difference between two nodes in the model. Selecting this option exposes
  port **B** on the block icon.
- `Absolute` — The sensor measures absolute
  temperature at port **A**. The sensor contains an implicit
  reference node, which means that you need only one port to make absolute
  measurements. Selecting this option hides port **B** on the block
  icon.
## Libraries

Simscape / Foundation Library / Thermal / Thermal Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

### R2023a: Usability enhancement for sensors

The Temperature Sensor block now contains an implicit
reference node, which means that you need only one port to make absolute measurements of
temperature.

This change has no compatibility impact.

## Description

Ideal temperature sensor

The Temperature Sensor block represents an ideal
temperature sensor, that is, a device that measures either the absolute temperature at a node,
or the temperature difference between two nodes, without drawing any heat.

Connections **A** and **B** are thermal conserving ports
that connect to the two points where temperature is being monitored. Port
**T** is a physical signal port that outputs the temperature difference
value.

The block positive direction is from port **A** to port
**B**. The measured temperature is determined as *T =
TA – TB*.

To measure the absolute temperature at a node, set the set the **Measurement
reference** parameter to `Absolute` and connect port
**A** to the node being measured.
