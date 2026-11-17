---
type: simulink-block
title: 'Grounded Neutral (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'groundedneutralthreephase'
documentation_source_path: 'ref/groundedneutralthreephase.html'
language: en
---

# Grounded Neutral (Three-Phase)

## Ports
```yaml
ports:
- name: '~'
  summary: Three-phase port electrical
  direction: conserving
```

### Conserving

### **~** — Three-phase port electrical

Expandable composite (**a**,**b**,
**c**) three-phase
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

Simscape / Electrical / Connectors & References

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Connect phases of three-phase system to electrical reference

The Grounded Neutral (Three-Phase) block connects the
phases of a three-phase system to ground.

**Note**

If you want to connect the neutral point of the three-phase system to other
blocks, use the Neutral Port (Three-Phase) block
instead. If you want to create a floating neutral point, use the
Floating Neutral (Three-Phase) block.
