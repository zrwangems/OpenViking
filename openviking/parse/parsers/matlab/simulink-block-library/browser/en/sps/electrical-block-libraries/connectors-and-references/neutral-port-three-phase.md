---
type: simulink-block
title: 'Neutral Port (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Connectors and References\u200b'
documentation_page: 'neutralportthreephase'
documentation_source_path: 'ref/neutralportthreephase.html'
language: en
---

# Neutral Port (Three-Phase)

## Ports

### Conserving

### **~** — Three-phase port electrical

Expandable composite (**a**,**b**,
**c**) three-phase
port.

### **n** — Neutral point electrical

Electrical conserving port associated with the neutral point

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### **Parasitic ground conductance** — Parasitic ground conductance `1e-12` `1/Ohm` (default)

Parasitic conductance to ground. A nonzero value is required for the
simulation of some circuit topologies.

## Libraries

Simscape / Electrical / Connectors & References

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Connect phases of three-phase system to electrical conserving port

The Neutral Port (Three-Phase) block connects the
phases of a three-phase system to an electrical conserving port.

**Note**

If you do not need to connect the neutral port to other blocks, use a
Floating Neutral (Three-Phase) block instead. If
you want to ground the neutral port, use a Grounded Neutral
(Three-Phase) block.
