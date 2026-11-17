---
type: simulink-block
title: 'Phase Voltage Sensor (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'phasevoltagesensorthreephase'
documentation_source_path: 'ref/phasevoltagesensorthreephase.html'
language: en
---

# Phase Voltage Sensor (Three-Phase)

## Ports
```yaml
ports:
- name: V
  summary: Three-elements vector physical signal
  direction: output
- name: ~1
  summary: Three-phase port electrical
  direction: conserving
- name: ~2
  summary: Three-phase port electrical
  direction: conserving
```

### Output

### **V** — Three-elements vector physical signal

Three-element physical signal vector output port associated with the
phase voltages
### Conserving

### **~1** — Three-phase port electrical

Expandable three-phase
port.

### **~2** — Three-phase port electrical

Expandable three-phase
port.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to model composite or expanded three-phase ports Composite three-phase ports (default) | Expanded three-phase
    ports
  group: ''
```

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.
## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Ideal three-phase phase voltage measurement

The Phase Voltage Sensor (Three-Phase) block represents
an ideal three-phase voltage sensor. It measures the voltages across the three-phase
ports **~1** and **~2** and outputs a single
three-element, physical signal vector. Each element of the physical signal output vector
is equal to the voltage in the respective phase.

**Note**

You must connect the Phase Voltage Sensor
(Three-Phase) block in shunt or in parallel with the three-phase
element. For more information on how to use this block, see Build and Simulate Composite and Expanded Three-Phase Models.
