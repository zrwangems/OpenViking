---
type: simulink-block
title: 'Current Sensor'
family: 'simscape'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sensors'
documentation_page: 'currentsensor'
documentation_source_path: '../simscape/ref/currentsensor.html'
language: en
---

# Current Sensor

## Ports
```yaml
ports:
- name: I
  summary: Current, A physical signal
  direction: output
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
```

### Output

### **I** — Current, A physical signal

Physical signal output port for the electrical current measurement.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the sensor positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the sensor negative terminal.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Electrical / Electrical Sensors Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Current sensor in electrical systems

The Current Sensor block represents an ideal current
sensor, that is, a device that converts current measured in any electrical branch into a
physical signal proportional to the current.

Use the **+** and **-** ports to connect the sensor in
series with the other blocks in the branch where you want to measure the current. Port
**I** outputs the measurement result as a physical signal. Use a PS-Simulink Converter block to connect this port to Simulink® blocks, such as Scope or Display.
