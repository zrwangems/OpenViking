---
type: simulink-block
title: 'Current Sensor (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'currentsensorthreephase'
documentation_source_path: 'ref/currentsensorthreephase.html'
language: en
---

# Current Sensor (Three-Phase)

## Ports
```yaml
ports:
- name: I
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

### **I** — Three-elements vector physical signal

Three-element physical signal vector output port associated with the
phase currents.
### Conserving

### **~1** — Three-phase port electrical

Expandable three-phase
electrical conserving port.

### **~2** — Three-phase port electrical

Expandable three-phase
electrical conserving port.
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

Ideal three-phase current measurement

The Current Sensor (Three-Phase) block represents an
ideal three-phase current sensor. The block measures each of the three currents flowing
from port **~1** to port **~2** and outputs a single
three-element, physical signal vector. Each element of the physical signal output vector
is proportional to the current in its respective phase.

**Note**

You must connect the Current Sensor (Three-Phase)
block in series with a three-phase element. For more information on how to use this
block, see Build and Simulate Composite and Expanded Three-Phase Models.
