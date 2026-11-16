---
type: simulink-block
title: 'Floating Neutral (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'floatingneutralthreephase'
documentation_source_path: 'ref/floatingneutralthreephase.html'
language: en
---

# Floating Neutral (Three-Phase)

## Ports

### Conserving

### **~** — Three-phase port electrical

Expandable composite (**a**,**b**,
**c**) three-phase
port.

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

Internal floating neutral point for wye-connected network

The Floating Neutral (Three-Phase) block connects the
individual phases of a three-phase system to form a floating neutral point.

**Note**

If you want to create a neutral point that you can connect to other blocks, use
the Neutral Port (Three-Phase) block. If you want to
create a neutral point that is connected to ground, use the Grounded
Neutral (Three-Phase) block.
